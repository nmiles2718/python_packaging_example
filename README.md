# Python Packaging Tutorial 

This repository is a self-contained tutorial on python packaging 
using setup tools and TOML (the pyproject.toml file).

```
python_packaging_example
│ --> README.md
│ --> pyproject.toml 
│ --> .gitignore    
└─── example package
    │ --> __init__.py
    │ --> example_module_1.py
    └─── subpackage
        │ --> __init__.py
        │ --> example_module_2.py
```

In this example, we follow [PEP 621](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata)  and utilize pyproject.toml to package the project. The TOML file is configured to use  [setuptools](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html) and [setuptools-git-versioning](https://setuptools-git-versioning.readthedocs.io/en/v1.13.3/index.html) to build and dynamically assign the version according to the git history of the repository. This is particularly helpful when building packages locally in "editable" mode with `pip` (i.e. `pip install -e ./ ` within the repo.). During the build process, there are three possible scenarios that can occur depending on the state of the source code:
```toml
[tool.setuptools-git-versioning]
enabled = true
template = "{tag}"
dirty_template = "{tag}+git.{sha}+changes"
dev_template = "{tag}+git.{sha}"
```

1. If the repository has no untracked files and the current commit is tagged, then the version number is set to the value specified by the [`template`](https://setuptools-git-versioning.readthedocs.io/en/stable/options/template.html) key in the `pyproject.toml` file. In this case, the value is set to `{tag}` which is a special keyword that tells setuptools to set the version number to the tag of the current commit. 
    - `example-package-name          1.0.0`
1. If the repository has no untracked files, but the current commit is untagged, then the version number is set to the value give by the `dev_template` key. Here we set it to show the most recent tag in the repo, and then the hash of the current commit.
    - `example-package-name      1.0.0+git.6d6976af`
1. If the repository has untracked files or uncommitted changes, then the version number is set to the value specified by the [`dirty_template`](https://setuptools-git-versioning.readthedocs.io/en/stable/options/dirty_template.html#dirty-template-option) key in the `pyproject.toml` file. In this case, it will set the value to the current tag and add additional git information to identify the commit used to build to code.  
    - `example-package-name      1.0.0+git.5521b651.changes`
    
Installation
-------------
- Local install in "editable" mode.
```shell
git clone https://github.com/nmiles2718/python_packaging_example.git
cd python_packaging_example
pip install -e ./
```
- Local install
```shell
git clone https://github.com/nmiles2718/python_packaging_example.git
cd python_packaging_example
pip install ./
```
- Local install using github https
```shell
pip install git+https://github.com/nmiles2718/python_packaging_example.git
```
- Local install using github ssh
```shell
pip install git+ssh://git@github.com/nmiles2718/python_packaging_example.git
```
- In the installs using github links, you can specify a tag for the build. Here
we specify tag 1.2.0 and we use ssh, instead of https. 
````
 pip install git+ssh://git@github.com/nmiles2718/python_packaging_example.git@1.2.0
````

Command Line Interface
----------------------
As part of the build process, a simple command line interface is setup and can be utilized as follows:
```bash
user@host % cli --help
 cli --help

 Usage: cli [OPTIONS]

 Entry point for the CLI
 The point of this function is to define the CL arguments and pass them to the
 desired endpoint.
 Parameters 
 ---------- 
 input1 : str
      The first input for the CLI      
 input2 : str
      The second input for the CLI 
 Returns 
 -------

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ *  --input1        INTEGER  Option help message [default: None] [required]   │
│ *  --input2        INTEGER  Argument help message [default: None] [required] │
│    --help                   Show this message and exit.                      │
╰──────────────────────────────────────────────────────────────────────────────╯
```
Input 1 is passed to module 1 and input 2 is passed to module 2 in the example subpackage.
```bash
user@host % cli --input1 23 --input2 4
func1 input 1: 23
func1 input 2: 4
```
Type checking is handled by `typer` package
```bash
user@host % cli --input1 'asdf' --input2 12
Usage: cli [OPTIONS]
Try 'cli --help' for help.
╭─ Error ──────────────────────────────────────────────────────────────────────╮
│ Invalid value for '--input1': 'asdf' is not a valid integer.                 │
╰──────────────────────────────────────────────────────────────────────────────╯
```