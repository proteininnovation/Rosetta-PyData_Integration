# Environment Setup

The analysis notebooks within this project rely on a conda environment
specified in `environment.yml` and `environment.lock.yml`. The `pyrosetta`
package is available for linux and osx via the
[`conda.graylab.jhu.edu`](http:/conda.graylab.jhu.edu) conda repository.
To access to this channel obtain a PyRosetta license via
[rosettacommons.org]
https://www.rosettacommons.org/software/license-and-download), then update
the included `environment.yaml` with your license credentials.

To setup the working environment, run:

```
conda env create -f environment.yml -n rosetta_pydata_integration
```

Activate via:

```
conda activate rosetta_pydata_integration
```

Launch the jupyter interface via:

```
jupyter lab
```
