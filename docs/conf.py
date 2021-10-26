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
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'TigaseDoc'
copyright = '2021, Qian Luo'
author = 'Qian Luo'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Use localized Python docs on Read the Docs build(copy form weblate org repo)
rtd_lang = os.environ.get("READTHEDOCS_LANGUAGE")

python_doc_url = "https://docs.python.org/3.9/"
if rtd_lang == "zh_CN":
    python_doc_url = "https://docs.python.org/zh-cn/3.9/"
#elif rtd_lang in ("es", "fr", "ja", "ko"):
#    python_doc_url = f"https://docs.python.org/{rtd_lang}/3.9/"
#elif rtd_lang == "zh_CN":
#    python_doc_url = "https://docs.python.org/zh-cn/3.9/"
#elif rtd_lang == "zh_TW":
#    python_doc_url = "https://docs.python.org/zh-tw/3.9/"

django_doc_url = "https://docs.djangoproject.com/en/stable/"
#if rtd_lang in ("el", "es", "fr", "id", "ja", "ko", "pl"):
#    django_doc_url = f"https://docs.djangoproject.com/{rtd_lang}/stable/"
if rtd_lang == "pl":
    django_doc_url = "https://docs.djangoproject.com/pl/stable/"
#elif rtd_lang == "pt_BR":
#    django_doc_url = "https://docs.djangoproject.com/pt-br/stable/"
elif rtd_lang == "zh_CN":
    django_doc_url = "https://docs.djangoproject.com/zh-hans/stable/"

sphinx_doc_url = "https://www.sphinx-doc.org/en/stable/"
if rtd_lang in (
    "pl",
    "zh_CN",
):
    sphinx_doc_url = f"https://www.sphinx-doc.org/{rtd_lang}/stable/"

# Configuration for intersphinx
intersphinx_mapping = {
    "python": (python_doc_url, None),
    "django": (django_doc_url, f"{django_doc_url}_objects/"),
    "psa": ("https://python-social-auth.readthedocs.io/en/latest/", None),
    "tt": (
        "http://docs.translatehouse.org/projects/translate-toolkit/en/latest/",
        None,
    ),
    "amagama": ("https://docs.translatehouse.org/projects/amagama/en/latest/", None),
    "virtaal": ("http://docs.translatehouse.org/projects/virtaal/en/latest/", None),
    "ldap": ("https://django-auth-ldap.readthedocs.io/en/latest/", None),
    "celery": ("https://docs.celeryproject.org/en/latest/", None),
    "sphinx": (sphinx_doc_url, None),
    "rtd": ("https://docs.readthedocs.io/en/latest/", None),
    "venv": ("https://virtualenv.pypa.io/en/stable/", None),
    "borg": ("https://borgbackup.readthedocs.io/en/stable/", None),
    "pip": ("https://pip.pypa.io/en/stable/", None),
    "compressor": ("https://django-compressor.readthedocs.io/en/stable/", None),
}

gettext_compact = False 

locale_dirs = ["locale/"]