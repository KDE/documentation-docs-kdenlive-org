# Official Documentation for Kdenlive

[![Build Status](https://binary-factory.kde.org/job/Website_docs-kdenlive-org/badge/icon)](https://binary-factory.kde.org/job/Website_docs-kdenlive-org/)  
[Link to Kdenlive Sphinx documentation](https://docs.kdenlive.org)

Kdenlive documentation based on [Sphinx](https://www.sphinx-doc.org)

## Setting up Development Environment

1. First you need to install [python3](https://www.python.org) and PIP as it is required to install sphinx.
2. You can check whether python was installed successfully (and your version is 3 and not 2) by running `python --version`
3. Now you can sphinx and the sphinx theme we are using with `python3 -m pip install --upgrade sphinx sphinx_rtd_theme`
4. You can check whether sphinx was installed successfully by running `sphinx-build --version`

## Running sphinx

After you cloned this repository (only need to be done once), use a command line to go to its root folder (e.g. with `cd /path/to/kdenlive-docs`)

### To generate a html web documentation run  

**Linux:** `make html`  
**Windows:** `.\make html`

The HTML is generated in `build/html` (e.g. with `/path/to/kdenlive-docs/build/html`). Open the web document by double click `index.html`.

### To generate an epub ebook run  

**Linux:** `make epub`  
**Windows:** `.\make epub`

The epub ebook is generated in `build/epub` (e.g. with `/path/to/kdenlive-docs/build/epub`). Open the ebook by double click `index.xhtml`.
  
## Status of translation
  
The status of the Kdenlive documentation you can see [here](https://l10n.kde.org/stats/gui/trunk-kf5/package/documentation-docs-kdenlive-org/).
