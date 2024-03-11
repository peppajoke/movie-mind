
# Movie Mind

### What is included on this template?

- 🖼️ Templates for starting multiple application types:
  * **Basic low dependency** Python program (default) [use this template](https://github.com/rochacbruno/python-project-template/generate)
  * **Flask** with database, admin interface, restapi and authentication [use this template](https://github.com/rochacbruno/flask-project-template/generate).
  **or Run `make init` after cloning to generate a new project based on a template.**
- 📦 A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your project.  
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Containerfile](Containerfile) to build a container image for your project.  
  `Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <movie_mind>` or `$ movie_mind` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments

---
# movie_mind

[![codecov](https://codecov.io/gh/peppajoke/movie-mind/branch/main/graph/badge.svg?token=movie-mind_token_here)](https://codecov.io/gh/peppajoke/movie-mind)
[![CI](https://github.com/peppajoke/movie-mind/actions/workflows/main.yml/badge.svg)](https://github.com/peppajoke/movie-mind/actions/workflows/main.yml)

Awesome movie_mind created by peppajoke

## Install it from PyPI

```bash
pip install movie_mind
```

## Usage

```py
from movie_mind import BaseClass
from movie_mind import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m movie_mind
#or
$ movie_mind
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
