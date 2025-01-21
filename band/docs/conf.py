import os
import sys
import django
sys.path.insert(0, os.path.abspath('../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'band.settings'
django.setup()
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'band'
copyright = '2025, clever'
author = 'clever'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Autodoc options ---------------------------------------------------------

autoclass_content = 'both'  # Include both class and method docstrings
autodoc_member_order = 'bysource'  # Order by the source file order
autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']

autosummary_generate = True  # Generate summary tables automatically