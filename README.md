# (Unofficial) Documentation for Kdenlive

**IMPORTANT: This repository does NOT contain the official Kdenlive Documentation it is created for testing purposes. The official manual is located at https://userbase.kde.org/Kdenlive/Manual**

Kdenlive documentation based on [Sphinx](https://www.sphinx-doc.org)

## Setting up Development Environment

1. First you need to install [python3](https://www.python.org) and PIP as it is required to install sphinx.
2. You can check whether python was installed successfully (and your version is 3 and not 2) by running `python --version`
3. Now you can sphinx and the sphinx theme we are using with `python3 -m pip install --upgrade sphinx sphinx_rtd_theme`
4. You can check whether sphinx was installed successfully by running `sphinx-build --version`

## Running sphinx

After you cloned this repository (only need to be done once), use a command line to go to its root folder (e.g. with `cd /path/to/kdenlive-docs`)

To generate a html web documentation run 
**Linux:** `make html`
**Windows:** `.\make html`

To generate an epub ebook run
**Linux:** `make epub`
**Windows:** `.\make epub`
