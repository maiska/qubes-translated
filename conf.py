# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'qubes-docs-translated'
copyright = '2021, test'
author = 'test'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'myst_parser'
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
    "frontmatter",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = [ '.md']


root_doc = "doc"
master_doc = "doc"


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_static_path = ['../'] goes into recursion

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/main.css',
]


#html_theme = 'alabaster'
html_theme = 'classic'

html_theme_options = {
    'externalrefs': True, 
    #'bgcolor': '#eff2f6',
    'bgcolor': 'white',
    'display_version': True,
    'linkcolor': '#99bfff',
    'textcolor': '#000000',
    'visitedlinkcolor': '#7b7b7b',
    'style_nav_header_background': 'white',
    'bodyfont': '"Open Sans", Arial, sans-serif',
#    'codebgcolor': '$color-qube-light',
    'codebgcolor': 'grey'
}



#extensions = [
#    'sphinx_jekyll_builder'
#]

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}


#source_suffix = ['.rst', '.md']

gettext_uuid=True
gettext_compact=False

language="de"