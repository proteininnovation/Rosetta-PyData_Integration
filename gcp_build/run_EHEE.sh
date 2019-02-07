#!/bin/bash
dsub \
	--provider local \
	--logging gs://ipi-main/chris_bahl/rosetta_docker_demo/runlogs \
	--tasks gs://ipi-main/chris_bahl/rosetta_docker_demo/tasks.tsv \
	--input SCRIPT=gs://ipi-main/chris_bahl/rosetta_docker_demo/build_and_disulfidize.xml \
	--input BLUEPRINT=gs://ipi-main/chris_bahl/rosetta_docker_demo/EHEE.blueprint \
	--input PDB=gs://ipi-main/chris_bahl/rosetta_docker_demo/example_EHEE.pdb \
	--output-recursive OUTPUT=gs://ipi-main/chris_bahl/rosetta_docker_demo/output \
	--image gcr.io/ipi-main/rosetta-main:2018.33_HEAD.7111c54 \
	--command 'rosetta_scripts \
		-in:file:s ${PDB} \
		-parser:protocol ${SCRIPT} \
		-out:path:all ${OUTPUT} \
		-out:suffix ${SUFFIX} \
		-parser:script_vars \
			blueprint=${BLUEPRINT} \
			topology=1-3.A.0;2-3.A.0 \
		-nstruct 5 \'
