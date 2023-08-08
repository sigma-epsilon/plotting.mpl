# **sigmaepsilon.TEMPLATE** - A template namespace package

This is a template package to help setting up new modules in the SigmaEpsilon ecosystem. Following the steps of this readme file can save you a lot of time setting up a Python package. Some of these steps are optional, but it is suggested to follow the description as much as possible.

## Module layout

Submodules are expected to be organized according to the so-called `src-layout`. In the mirror of the SigmaEpsilon namespace, this implies the following directory structure:

```raw
sigmaepsilon.TEMPLATE
├── pyproject.toml
├── README.md
├── ...
└── src/
    └── sigmaepsilon/
        └── TEMPLATE/
            ├── __init__.py
            ├── ...
```

This layout would create the implicit namespace package `sigmaepsilon.TEMPLATE`.

## Setting up project information

Setting a few variables can kick off a whole bunch of mechanisms predefined for your project from creating docs to setting up a CI/CD pipeline.

### Set the name of the module

Wherever you see the tag `TEMPLATE` (like in the header of this file), you should replace it with the name of the actual module. The source code should be under the folder `src\sigmaepsilon.TEMPLATE`. This folder is referred to as the root of your source. The first thing to do is to rename this folder to matvh the name of your module. Later the name of this folder is used in both `setup.py` and in the CircleCI config file to guess the name of the module.

### Edit `__init__.py`

Edit the variable `__description__` in `__init__.py` in the root of your module. This should be a short, one line description of the module you are about to create, eg. 'A Python package to handle polygonal meshes'.

## Branching strategy

For the preconfigured CI/CD in CircleCI to work as expected, it is suggested that

- the main/master branch is called 'main'
- there is a branch called 'nightly'

You can deviate from that, but then you have to modify `.circleci/config.yaml` to make up for it.

## CI/CD

CI/CD is configured for CircleCI. You have to add the project in CircleCI to the set of managed projects. Of course, you can use GitHub actions as well.

## Documentation

We use Sphinx together with the PyData theme to document our projects. Check out other SigmaEpsilon projects.

## Versioning

We follow [schemantic versioning](https://semver.org/) in all of our projects. If you deviate from that, it must be indicated in the README.md file of your project.

## Publishing to PyPI

If the module is about to be published to PyPI, you can either rely on the CircleCI pipeline, or do it manually (you might need to do the first deployment manually).

### Test publishing to TestPyPI

```shell
pip install wheel twine
pip install .
pip install 'build<0.10.0'
python -m build
python -m twine upload --repository testpypi --skip-existing dist/*
```

### Publish to PyPI

```shell
pip install wheel twine
pip install .
pip install 'build<0.10.0'
python -m build
python -m twine upload --skip-existing dist/*
```

## License

Choosing a license for your model is important to protect you and your potential users. If you are developing an open source library, we suggest you to go with the very permissive MIT license or a less permissive GNU type license.

[Five types of software licenses you need to understand](https://www.synopsys.com/blogs/software-security/5-types-of-software-licenses-you-need-to-understand/)
[OSI Approved Licenses](https://opensource.org/licenses/)