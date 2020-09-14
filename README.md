# python-mistery

Python library to interact with the MIST API.

[![image](https://img.shields.io/pypi/pyversions/mistery.svg)](https://pypi.org/project/mistery/)
[![codecov](https://codecov.io/gh/broadinstitute/python-mistery/branch/master/graph/badge.svg)](https://codecov.io/gh/broadinstitute/python-mistery)

## Basics

The documentation on interacting with the MIST API can be found at [https://api.mist.com/api/v1/docs/Home](https://api.mist.com/api/v1/docs/Home).

## Features

A list of features this package provides

## Installing

How do you install this package?

## Examples

Code examples using this package

## Contributing

Pull requests to add functionality and fix bugs are always welcome.  Please check the CONTRIBUTING.md for specifics on contributions.

### Testing

How do you run unit tests on the code in this repo?

## Releases

Releases to the codebase are typically done using the [bump2version][2] tool.  This tool takes care of updating the version in all necessary files, updating its own configuration, and making a GitHub commit and tag.  We typically do version bumps as part of a PR, so you don't want to have [bump2version][2] tag the version at the same time it does the commit as commit hashes may change.  Therefore, to bump the version a patch level, one would run the command:

```sh
bump2version --verbose --no-tag patch
```

Once the PR is merged, you can then checkout the new master branch and tag it using the new version number that is now in `.bumpversion.cfg`:

```sh
git checkout master
git pull --rebase
git tag 1.0.0 -m 'Bump version: 0.1.0 → 1.0.0'
git push --tags
```

# Credits

This package was created with [Cookiecutter][3] and the `broadinstitute/cookiecutter-bits-pypi` project template.

* [Cookiecutter][3]
* [https://github.com/broadinstitute/cookiecutter-bits-pypi](broadinstitute/cookiecutter-bits-pypi)

[1]: https://www.python.org/ "Python"
[2]: https://pypi.org/project/bump2version/ "bump2version"
[3]: https://cookiecutter.readthedocs.io/en/latest/index.html "Cookiecutter"
