#!/bin/bash
#SBATCH -c 1                        # Request one core
#SBATCH -N 1                        # Request one node
#SBATCH --array=0-800               # Specify the number of jobs in the array
#SBATCH -t 0-20:00                  # Runtime in D-HH:MM format
#SBATCH -p medium                   # Partition to run in
#SBATCH --mem=4G                    # Memory total in MB (for all cores)
#SBATCH -o /dev/null                # File to which STDOUT will be written, including job ID
#SBATCH -e runlogs/%A_%a.err        # File to which STDERR will be written, including job ID

SCRIPT=build_and_disulfidize.xml
BLUEPRINT=EHEE.blueprint
PDB=EHEE.pdb
OUTPUT=output
SUFFIX=_${SLURM_ARRAY_TASK_ID}
PREFIX=${SLURM_JOB_ID}_

rosetta_scripts.default.linuxgccrelease \
        -in:file:s ${PDB} \
        -parser:protocol ${SCRIPT} \
        -out:path:all ${OUTPUT} \
        -out:suffix ${SUFFIX} \
        -out:prefix ${PREFIX} \
        -parser:script_vars \
                blueprint=${BLUEPRINT} \
                topology=1-3.A.0;2-3.A.0 \
        -nstruct 100 \
