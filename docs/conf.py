# -*- coding: utf-8 -*-
import os
import sys
import shutil
import warnings
from datetime import date

sys.path.insert(0, os.path.abspath(".."))

# -- Global variables

# The full version, including alpha/beta/rc tags
VERSION_DICT = {}
with open("../evadb/version.py", "r") as version_file:
    exec(version_file.read(), VERSION_DICT)

# Set the latest version.
LATEST_VERSION = VERSION_DICT["VERSION"]

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinxemoji.sphinxemoji",
    "sphinx_external_toc",
    "sphinx_design",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_click.ext",
    "sphinx-jsonschema",
    "sphinx_copybutton",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
#    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx_thebe",
    "sphinxcontrib.autodoc_pydantic",
    "sphinxcontrib.redoc",
    "sphinxcontrib.youtube",
    "sphinx_inline_tabs",
    "sphinx.ext.intersphinx",
    "myst_nb",
    "versionwarning.extension",
    "IPython.sphinxext.ipython_console_highlighting",
]

suppress_warnings = ["etoc.toctree", "myst.header"]

source_suffix = [".ipynb", ".html", ".md", ".rst"]

autodoc_pydantic_model_show_json = False
autodoc_pydantic_field_list_validators = False
autodoc_pydantic_config_members = False
autodoc_pydantic_model_show_config_summary = False
autodoc_pydantic_model_show_validator_members = False
autodoc_pydantic_model_show_field_summary = False
autodoc_pydantic_model_members = False
autodoc_pydantic_model_undoc_members = False

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
]


# Thebe configuration for launching notebook cells within the docs.
thebe_config = {
    "selector": "div.highlight",
    "repository_url": "https://github.com/georgia-tech-db/eva",
    "repository_branch": "master",
}

# The suffix(es) of source filenames.
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "EvaDB"
copyright = str(date.today().year) + ", EvaDB."
author = u"EvaDB"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md", "images/reference/README.md"]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> eva-master
=======
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 065f25fb (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> georgia-tech-db-main

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))

=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "github-dark"

# List of substitutions
rst_prolog = """
.. |rst| replace:: restructuredText
"""
# -- Options for not found extension ---------------------------------------

# Template used to render the 404.html generated by this extension.
notfound_template = "404.html"

# Prefix added to all the URLs generated in the 404 page.
notfound_urls_prefix = ""

# -- Options for HTML output ----------------------------------------------

# The theme to use for pages.
html_theme = "furo"

html_title = project + "\n" + LATEST_VERSION
html_static_path = ["_static"]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for the theme, see the
# documentation.
html_theme_options = {
    "navigation_with_keys": True,
    "light_css_variables": {
        "color-background-secondary": "#fff",
        "color-sidebar-background-border": "none",
        "font-stack": "Inter, Arial, sans-serif",
        "font-stack--monospace": "Fira Code, Courier, monospace"
    },
    "dark_css_variables": {
        "color-background-secondary": "#000",
        "font-stack": "Inter, Arial, sans-serif",
        "font-stack--monospace": "Fira Code, Courier, monospace"        
    },
    # Add important announcement here
    "announcement": "<div class='topnav'></div>",
}

external_toc_path = "_toc.yml"  # optional, default: _toc.yml
external_toc_exclude_missing = False  # optional, default: False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", (None, "python-inv.txt"))
}


# Adding custom css file
html_static_path = ["_static"]
html_css_files = [
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 114c0bdd (docs: updates)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
    "custom.css", 
    "algolia.css",
    "https://cdn.jsdelivr.net/npm/@docsearch/css@3",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css"
]
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
                    "custom.css", 
<<<<<<< HEAD
<<<<<<< HEAD
                    "algolia.css",
                    "https://cdn.jsdelivr.net/npm/@docsearch/css@3",
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
                    "custom.css", 
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
=======
                    "custom.css", 
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> georgia-tech-db-main
=======
                    "algolia.css",
                    "https://cdn.jsdelivr.net/npm/@docsearch/css@3",
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css"]
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 114c0bdd (docs: updates)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
>>>>>>> a9124e1e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main

# Check link: https://stackoverflow.com/questions/14492743/have-sphinx-report-broken-links/14735060#14735060
nitpicky = True
# BUG: https://stackoverflow.com/questions/11417221/sphinx-autodoc-gives-warning-pyclass-reference-target-not-found-type-warning
nitpick_ignore_regex = [('py:class', r'.*')]
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
=======
=======
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
=======
=======
=======

<<<<<<< HEAD

for i in os.listdir("../tutorials"):
    if i in [
        "13-privategpt.ipynb",
        "08-chatgpt.ipynb",
        "12-query-pdf.ipynb",
        "02-object-detection.ipynb",
        "03-emotion-analysis.ipynb",
        "07-object-segmentation-huggingface.ipynb",
        "chatgpt.png",
    ]:
        shutil.copy(f"../tutorials/{i}", "./source/usecases/")

nb_execution_mode = "off"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD

for i in os.listdir("../tutorials"):
    if i in [
        "13-privategpt.ipynb",
        "08-chatgpt.ipynb",
        "12-query-pdf.ipynb",
        "02-object-detection.ipynb",
        "03-emotion-analysis.ipynb",
        "07-object-segmentation-huggingface.ipynb",
        "chatgpt.png",
    ]:
        shutil.copy(f"../tutorials/{i}", "./source/usecases/")

nb_execution_mode = "off"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 7dd70375 (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD

for i in os.listdir("../tutorials"):
    if i in [
        "13-privategpt.ipynb",
        "08-chatgpt.ipynb",
        "12-query-pdf.ipynb",
        "02-object-detection.ipynb",
        "03-emotion-analysis.ipynb",
        "07-object-segmentation-huggingface.ipynb",
        "chatgpt.png",
    ]:
        shutil.copy(f"../tutorials/{i}", "./source/usecases/")

nb_execution_mode = "off"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eva-master

=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD

for i in os.listdir("../tutorials"):
    if i in [
        "13-privategpt.ipynb",
        "08-chatgpt.ipynb",
        "12-query-pdf.ipynb",
        "02-object-detection.ipynb",
        "03-emotion-analysis.ipynb",
        "07-object-segmentation-huggingface.ipynb",
        "chatgpt.png",
    ]:
        shutil.copy(f"../tutorials/{i}", "./source/usecases/")

nb_execution_mode = "off"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> a9124e1e (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD

for i in os.listdir("../tutorials"):
    if i in [
        "13-privategpt.ipynb",
        "08-chatgpt.ipynb",
        "12-query-pdf.ipynb",
        "02-object-detection.ipynb",
        "03-emotion-analysis.ipynb",
        "07-object-segmentation-huggingface.ipynb",
        "chatgpt.png",
    ]:
        shutil.copy(f"../tutorials/{i}", "./source/usecases/")

nb_execution_mode = "off"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD

for i in os.listdir("../tutorials"):
    if i in [
        "13-privategpt.ipynb",
        "08-chatgpt.ipynb",
        "12-query-pdf.ipynb",
        "02-object-detection.ipynb",
        "03-emotion-analysis.ipynb",
        "07-object-segmentation-huggingface.ipynb",
        "chatgpt.png",
    ]:
        shutil.copy(f"../tutorials/{i}", "./source/usecases/")

nb_execution_mode = "off"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 7dd70375 (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD

for i in os.listdir("../tutorials"):
    if i in [
        "13-privategpt.ipynb",
        "08-chatgpt.ipynb",
        "12-query-pdf.ipynb",
        "02-object-detection.ipynb",
        "03-emotion-analysis.ipynb",
        "07-object-segmentation-huggingface.ipynb",
        "chatgpt.png",
    ]:
        shutil.copy(f"../tutorials/{i}", "./source/usecases/")

nb_execution_mode = "off"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
>>>>>>> c63abee7 (release: merge staging into master (#1032))

<<<<<<< HEAD
<<<<<<< HEAD

for i in os.listdir("../tutorials"):
    if i in [
        "13-privategpt.ipynb",
        "08-chatgpt.ipynb",
        "12-query-pdf.ipynb",
        "02-object-detection.ipynb",
        "03-emotion-analysis.ipynb",
        "07-object-segmentation-huggingface.ipynb",
        "chatgpt.png",
    ]:
        shutil.copy(f"../tutorials/{i}", "./source/usecases/")

nb_execution_mode = "off"
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))

=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
<<<<<<< HEAD
>>>>>>> eva-source
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
=======
>>>>>>> 5d9d82f0 (feat: sync master staging (#1050))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> b87af508 (feat: sync master staging (#1050))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
=======
>>>>>>> f431fb09 (feat: sync master staging (#1050))
=======
>>>>>>> 53dafecf (feat: sync master staging (#1050))
=======
>>>>>>> f75511e6 (feat: sync master staging (#1050))
>>>>>>> georgia-tech-db-main
>>>>>>> 2dacff69 (feat: sync master staging (#1050))
# -- Initialize Sphinx ----------------------------------------------
def setup(app):
    warnings.filterwarnings(
        action="ignore",
        category=UserWarning,
        message=r".*Container node skipped.*",
    )
    # Custom JS
    app.add_js_file("js/top-navigation.js", defer="defer")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
<<<<<<< HEAD
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> eva-source
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
    app.add_js_file("https://cdn.jsdelivr.net/npm/@docsearch/js@3.3.3/dist/umd/index.js",defer="defer")
    app.add_js_file("js/algolia.js",defer="defer")
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
    app.add_js_file("https://cdn.jsdelivr.net/npm/@docsearch/js@3.3.3/dist/umd/index.js",defer="defer")
    app.add_js_file("js/algolia.js",defer="defer")
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
    app.add_js_file("https://cdn.jsdelivr.net/npm/@docsearch/js@3.3.3/dist/umd/index.js",defer="defer")
    app.add_js_file("js/algolia.js",defer="defer")
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f028c383 (release: merge staging into master (#1032))
<<<<<<< HEAD
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
>>>>>>> georgia-tech-db-main
    app.add_js_file("https://cdn.jsdelivr.net/npm/@docsearch/js@3.3.3/dist/umd/index.js",defer="defer")
    app.add_js_file("js/algolia.js",defer="defer")
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
    app.add_js_file("https://cdn.jsdelivr.net/npm/@docsearch/js@3.3.3/dist/umd/index.js",defer="defer")
    app.add_js_file("js/algolia.js",defer="defer")
>>>>>>> 40a10ce1 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> georgia-tech-db-main
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
>>>>>>> eva-source
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> eva-master
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> 7dd70375 (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
>>>>>>> f028c383 (release: merge staging into master (#1032))
=======
=======
>>>>>>> 7cac771f (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 065f25fb (release: merge staging into master (#1032))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> eva-source
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
=======
>>>>>>> georgia-tech-db-main
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
=======
>>>>>>> 6d6a14c8 (Bump v0.3.4+ dev)
>>>>>>> 8da6decc (Bump v0.3.4+ dev)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
>>>>>>> eva-source
=======
>>>>>>> 22e78346 (Bump v0.3.4+ dev)
<<<<<<< HEAD
=======
    app.add_js_file("https://cdn.jsdelivr.net/npm/@docsearch/js@3.3.3/dist/umd/index.js",defer="defer")
    app.add_js_file("js/algolia.js",defer="defer")
=======
>>>>>>> 8c5b63dc (release: merge staging into master (#1032))
>>>>>>> a9124e1e (release: merge staging into master (#1032))
=======
>>>>>>> c5f43c65 (Bump v0.3.4+ dev)
=======
=======
>>>>>>> c63abee7 (release: merge staging into master (#1032))
>>>>>>> 30d7834d (release: merge staging into master (#1032))
=======
>>>>>>> ae08f806 (Bump v0.3.4+ dev)
=======
>>>>>>> f028c383 (release: merge staging into master (#1032))
>>>>>>> 54907d3e (release: merge staging into master (#1032))
=======
>>>>>>> 2170a7a9 (Bump v0.3.4+ dev)
>>>>>>> bf18bc80 (Bump v0.3.4+ dev)
=======
>>>>>>> 28d8bad1 (release: merge staging into master (#1032))
>>>>>>> 66bd4f55 (release: merge staging into master (#1032))
=======
>>>>>>> 922824b7 (Bump v0.3.4+ dev)
>>>>>>> georgia-tech-db-main
