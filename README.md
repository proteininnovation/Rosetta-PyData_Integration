# Overview

This repo contains three high-level examples of Rosetta-PyData integration
using the `pyrosetta.distributed` namespace:

* `ddg_analysis` - Development of a hybrid RosettaScripts-python modeling
  protocol, combining pyrosetta-based model preparation,
  RosettaScripts-based modeling and dynamic templating of RosettaScripts
  protocols.
* `miniprotein_design` - A hybrid batch-and-interactive workflow,
  demonstrating post-run analysis of a large-scale simulation.
* `relax_benchmark` - Baseline performance profiling of a simple `dask` implemented
   simulation via both multi-threaded and multi-node distributed clusters.

# Non-Interactive Views

As these notebooks may include custom view components, particularly
a [3dmol.js](https://3dmol.csb.pitt.edu) based viewer, we recommend using
the
[nbviewer](https://nbviewer.jupyter.org/github/proteininnovation/Rosetta-PyData_Integration/tree/master/)
interface as a non-interactive way to view these components.

# Interactive Environment

The analysis notebooks within this project rely on a conda environment
specified in `environment.yml`. Conda packages for this environment are
available on the Linux 64-bit platform.

## Installation 

1. Install and configure `conda` in your environment. We strongly
  recommend the [miniconda](https://docs.conda.io/en/latest/miniconda.html)
  installer.

2. Clone this git repository:

```
git clone https://github.com/proteininnovation/Rosetta-PyData_Integration
```

3. The `pyrosetta` package is available for linux and osx via the
  [`conda.graylab.jhu.edu`](http:/conda.graylab.jhu.edu) conda repository.
  To access this channel, obtain a [PyRosetta license](http://c4c.uwc4c.com/express_license_technologies/pyrosetta).
  Then, update configure your `.condarc` to access the specified channel via:

```
conda config --add channels https://{USERNAME}:{PASSWORD}@conda.graylab.jhu.edu
```

4. Setup the working environment, including python, pyrosetta and
   jupyterlab via:

```
conda env create -f environment.yml -n rosetta_pydata_integration
```
  

## Evaluation 

Activate the working environment via:

```
conda activate rosetta_pydata_integration
```

Launch the jupyter interface via:

```
jupyter lab
```
