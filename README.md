# Firecrown Examples

This repository contains examples demonstrating the use of Firecrown, a Python package that provides the DESC framework to implement likelihoods, as well as specific likelihood implementations. Firecrown is intended to be usable from external statistical analysis tools.

Currently, it supports Cobaya, CosmoSIS, and NumCosmo, providing the necessary classes or modules to allow users the sampling frameworks to call any Firecrown likelihood from within those samplers.

## Documentation

For detailed information on how to contribute to the Firecrown project, please refer to the official [Firecrown ReadTheDocs](https://firecrown.readthedocs.io/en/latest/) documentation.

## Contributing

If you are a member of DESC and part of the developer's team, please follow these steps:

1. Create a branch from `master` with a descriptive name for your feature or fix.
2. Make your changes, ensuring that your code adheres to the project's coding conventions.
3. Test your changes thoroughly.
4. Create a pull request, providing a clear and concise description of your changes.

If you are not a member of DESC, please follow these steps:

1. Fork the repository and create your branch from `master`.
2. Make your changes, ensuring that your code adheres to the project's coding conventions.
3. Test your changes thoroughly.
4. Create a pull request, providing a clear and concise description of your changes.

Please ensure that you have read and understood the [Contributing Guidelines](https://firecrown.readthedocs.io/en/latest/contrib.html) before making a contribution. See also Firecrown's [code development hygene](https://firecrown.readthedocs.io/en/latest/_static/intro_article.html#code-development-hygiene).


## Beginner's guide

### Cluster_model examples for running the prediction and likelihood examples:
1.  Make sure that you have installed [firecrown](https://firecrown.readthedocs.io/en/latest/install_quick.html), and have setup the firecrown conda environment (if using).
2.  If you haven't done it yet, make sure you've installed or can use jupyter notebook.
3.  The cluster abundance prediction.ipynb makes cluster abundance (counts) predictions for one set of inpute parameters (cosmology and richness-mass scaling relation parameters). You may wish to try to run this notebook first.
4.  Before running the `build_likelihood.ipynb`, first you need to generate the sacc files. You can do so by going to your `${FIRECROWN_DIR}/examples/cluster_number_counts/` folder and run `generate_rich_mean_mass_sacc_data.py`.
5. `build_likelihood.ipynb` builds a likelihood and compute likelihood for one set of input parameters and observational data points.
6. If you would like to run a chain based on those predictions and likelihoods, there are cosmosis ini files that live in the `${FIRECROWN_DIR}/examples/cluster_number_counts/` folder. you can run those using cosmosis commands.

