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

project = 'qubes-docs'
copyright = '2021, test'
author = 'test'

title = "Qubes Docs"
html_title = "Qubes Docs"

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'myst_parser',
        'sphinx.ext.duration',
        'sphinx.ext.doctest',
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.intersphinx',
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
#    "frontmatter",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = [ '.md']


root_doc = "doc"
master_doc = "doc"

language = "de"
locale_dirs = ['locale /']


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
#html_static_path = ['_static']

# html_static_path = ['../'] goes into recursion

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
#html_css_files = [
#    'css/main.css',
#]



html_theme = 'classic'

#html_theme = 'alabaster'
html_theme_options = {
    'externalrefs': True, 
    #'bgcolor': '#eff2f6',
    'bgcolor': 'white',
    'linkcolor': '#99bfff',
    'textcolor': '#000000',
    'visitedlinkcolor': '#7b7b7b',
    'bodyfont': '"Open Sans", Arial, sans-serif',
    'codebgcolor': '$color-qube-light',
    'codebgcolor': 'grey'
}

#html_theme = 'sphinx_rtd_theme'
#html_theme_options = {
#    'navigation_depth': -1, 
#}



#extensions = [
#    'sphinx_jekyll_builder'
#]

#source_parsers = {
#   '.md': 'recommonmark.parser.CommonMarkParser',
#}



gettext_uuid=True
gettext_compact=False


epub_show_urls = 'footnote'
latex_show_urls ='footnote'

