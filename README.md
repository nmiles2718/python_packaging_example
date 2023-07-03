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
        │ --> examplpe_module_2.py
```

In this example, we follow [PEP 621](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata)  and utilize pyproject.toml to package the project. The TOML file is configured to use  [setuptools](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html) and [setuptools-git-versioning](https://setuptools-git-versioning.readthedocs.io/en/v1.13.3/index.html) to build and dynamically assign the version according to the git history of the repository. There are three possible scenarios that can occur depending on the state of the repository:
```toml
[tool.setuptools-git-versioning]
enabled = true
template = "{tag}"
dirty_template = "{tag}+git.{sha}+changes"
dev_template = "{tag}+git.{sha}"
```


1. If the repository has no untracked files and the current commit is tagged, then the version number is set to the value specified by the [`template`](https://setuptools-git-versioning.readthedocs.io/en/stable/options/template.html) key in the `pyproject.toml` file. In this case, the value is set to `{tag}` which is a specified keyword that tells setuptools to set the version number to the latest git tag. 
1. If the repository has untracked files or uncommitted changes, then the version number is set to the value specified by the [`dirty_template`](https://setuptools-git-versioning.readthedocs.io/en/stable/options/dirty_template.html#dirty-template-option) key in the `pyproject.toml` file.  
    - ` "{tag}+git.{sha}+changes"`