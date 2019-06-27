# Environment Setup

The analysis notebook within this project relies on a conda environment
specified in `environment.yml` and `environment.lock.yml`. The `pyrosetta`
package is available for linux and osx via the "conda.graylab.jhu.edu"
conda repository. To access to this channel obtain a PyRosetta license via
https://www.rosettacommons.org/software/license-and-download, then update
the included `environment.lock.yaml` with your license credentials.

To setup the working environment, run:

```
conda env create -f environment.lock.yml
```

then activate via:

```
conda activate rosetta_pydata_integration_local_analysis
```
