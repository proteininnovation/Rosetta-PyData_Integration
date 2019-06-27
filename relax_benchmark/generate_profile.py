import json
import timeit
import psutil

import dask.delayed
import dask.bag
import dask.distributed
from dask_jobqueue import SLURMCluster

import dask.bag
import dask.delayed
from pyrosetta.distributed.io import pose_from_file
from pyrosetta.distributed.tasks.rosetta_scripts import SingleoutputRosettaScriptsTask


def main():

    # Setup basic parallel relax task with adjustable batch size.
    relax_protocol = """
    <ROSETTASCRIPTS>
    <SCOREFXNS> </SCOREFXNS>
    <TASKOPERATIONS></TASKOPERATIONS>
    <FILTERS></FILTERS>
    <MOVERS>
      <FastRelax name="fastrelax" />
    </MOVERS>
    <PROTOCOLS>
      <Add mover="fastrelax"/>
    </PROTOCOLS>
    </ROSETTASCRIPTS>
    """

    def parallel_relax(infile, nstruct):
        input_pose = dask.delayed(pose_from_file)(infile)
        relax_task = dask.delayed(SingleoutputRosettaScriptsTask(relax_protocol))
        as_list = dask.delayed(lambda obj: [obj])

        batch_results = dask.bag.from_delayed(
            [as_list(relax_task(input_pose)) for _ in range(nstruct)]
        )

        return batch_results.topk(
            1, key=lambda result: -result.scores["total_score"]
        ).compute()[0]

    infile = "133l.pdb1.gz"

    with open("profile_result.txt", "wt") as outfile:

        # Time runs on local cluster spanning all cores with threads
        ncores = psutil.cpu_count(False)
        nthreads = ncores
        cluster = dask.distributed.LocalCluster(
            n_workers=1, threads_per_worker=nthreads
        )
        client = dask.distributed.Client(cluster)

        for i in (1, 2, 4, 8, 16, 24, 48):
            for _repeat in range(3):
                client.restart()
                print(
                    json.dumps(
                        dict(
                            protocol="threaded_parallel",
                            nstruct=i,
                            walltime=timeit.timeit(
                                lambda: parallel_relax(infile, i), number=1
                            ),
                        )
                    ),
                    file=outfile,
                )

        # Launch distributed workers, here we 6 cores-per-worker on 24 core
        # nodes using AWS m5.24xlarge instances.
        cluster = SLURMCluster(
            walltime="UNLIMITED",
            memory="168 GB",
            cores=24,
            processes=4,
            job_extra=("--exclusive",),
        )
        cluster.scale(n=16)
        client = dask.distributed.Client(cluster)

        for i in (1, 2, 4, 8, 16, 24, 36, 48):
            for _repeat in range(3):
                client.restart()
                print(
                    json.dumps(
                        dict(
                            protocol="distributed_parallel",
                            nstruct=i,
                            walltime=timeit.timeit(
                                lambda: parallel_relax(infile, i), number=1
                            ),
                        )
                    ),
                    file=outfile,
                )


if __name__ == "__main__":
    main()
