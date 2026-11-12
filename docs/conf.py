"""Sphinx configuration file."""

import os
import sys
import time

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

import terminaltables3


# General configuration.
author = "Robpol86, Matthew Dean Martin"
copyright = "{}, {}".format(time.strftime("%Y"), author)
html_last_updated_fmt = "%Y-%m-%d"
root_doc = "index"
project = "terminaltables3"
pygments_style = "friendly"
release = version = terminaltables3.__version__
templates_path = []
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}


# Options for HTML output.
html_context = {
    "conf_py_path": "/docs/",
    "display_github": True,
    "github_repo": "terminaltables3",
    "github_user": "matthewdeanmartin",
    "github_version": "master",
    "source_suffix": ".rst",
}
html_copy_source = False
html_favicon = "favicon.ico"
html_theme = "sphinx_rtd_theme"
html_title = project


# extlinks.
extlinks = {
    "github": (
        f"https://github.com/matthewdeanmartin/{project}/blob/v{version}/%s",
        "%s",
    )
}
