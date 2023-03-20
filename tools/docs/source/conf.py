# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
base_framework_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','..','..')
# Add new Paths here for new docs
sys.path.insert(0, os.path.join(base_framework_path, 'keywords'))
sys.path.insert(0, os.path.join(base_framework_path, 'keywords', 'xapi_base' ))

project = 'AutoIQ Keywords'
copyright = '2023, AutoIQ Group'
author = 'AutoIQ Group'
release = '5.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = ['sphinx.ext.viewcode',
              'sphinx.ext.autodoc',
              'sphinx.ext.napoleon']

autodoc_default_flags = ['members','undoc-members']
toc_object_entries_show_parents = 'none'

templates_path = ['_templates']
exclude_patterns = []
source_suffix = ['.rst', '.md']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'bizstyle'
