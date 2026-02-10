# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "CollabXR Documentation"
copyright = "2026, Purdue University Envision Center"
author = "Purdue University Envision Center"

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
    "sphinx_copybutton",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_logo = "../static/logo-collab.png"
html_favicon = "../static/favicon.ico"

# Optionally configure the theme: https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
# Adding onto the theme css: https://docs.readthedocs.com/platform/stable/guides/adding-custom-css.html
html_theme_options = {}

# -- Options for EPUB output
epub_show_urls = "footnote"
