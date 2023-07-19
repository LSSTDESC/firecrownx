This repository contains examples demonstrating the use of Firecrown.

For examples on how to use the ClusterNumberCounts statiscs object and its required models, check the [cluster_model](https://github.com/LSSTDESC/firecrownx/tree/cluster_counts_examples/cluster_model) folder.

__Beginner's guide__

cluster_model folder, running the prediction and likelihood examples:  
(1) make sure that you have installed [firecrown](https://firecrown.readthedocs.io/en/latest/install_quick.html), and have setup the firecrown conda environment (if using). 
(2) If you haven't done it yet, make sure you've installed or can use jupyter notebook. 
(3) The cluster abundance prediction.ipynb makes cluster abundance (counts) predictions for one set of inpute parameters (cosmology and richness-mass scaling relation parameters). You may wish to try to run this notebook first. 
(4) Before running the `build_likelihood.ipynb`, first you need to generate the sacc files. You can do so by going to your `${FIRECROWN_DIR}/examples/cluster_number_counts/` folder and run `generate_rich_mean_mass_sacc_data.py`. 
(5) `build_likelihood.ipynb` builds a likelihood and compute likelihood for one set of input parameters and observational data points. 
(6) If you would like to run a chain based on those predictions and likelihoods, there are cosmosis ini files that live in the `${FIRECROWN_DIR}/examples/cluster_number_counts/` folder. you can run those using cosmosis commands. 

