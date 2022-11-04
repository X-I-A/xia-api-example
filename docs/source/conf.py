# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import codecs
import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))

project = os.getcwd().split(os.path.sep)[-3]
copyright = str(date.today().year) + ', X-I-A.com'
author = 'X-I-A'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'display_version': True,
}

# Supporting md files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}