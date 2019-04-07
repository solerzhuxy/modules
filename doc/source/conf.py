# -*- coding: utf-8 -*-
#
# Modules documentation build configuration file, created by
# sphinx-quickstart on Mon Oct  2 06:17:09 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Modules'
copyright = '1996-1999 John L. Furlani & Peter W. Osel, 1998-2017 R.K.Owen, 2002-2004 Mark Lakata, 2004-2017 Kent Mein, 2016-2019 Xavier Delaruelle'
author = ''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

from subprocess import Popen, PIPE
def get_version_release_from_git():
    """
    Returns project version and release as string from 'git' repository data.
    """
    DEVNULL = open(os.devnull, 'w')
    pipe = Popen('git describe --tags --abbrev=0', stdout=PIPE, stderr=DEVNULL, shell=True)
    git_current_tag = pipe.stdout.read()
    pipe = Popen('git describe --tags', stdout=PIPE, stderr=DEVNULL, shell=True)
    git_current_desc = pipe.stdout.read()
    pipe = Popen('git rev-parse --abbrev-ref HEAD', stdout=PIPE, stderr=DEVNULL, shell=True)
    git_current_branch = pipe.stdout.read()

    if git_current_desc:
        version = git_current_tag.lstrip('v').rstrip()
        if git_current_tag == git_current_desc:
            return version, ''
        else:
            branch = git_current_branch.rstrip()
            tags = git_current_desc.lstrip(git_current_tag + '-').rstrip()
            # workaround for RTD, where master branch is not detected
            if branch == 'master' or os.environ.get('READTHEDOCS', None) == 'True':
                return version, version + '+' + tags
            else:
                return version, version + '+' + branch + '-' + tags
    else:
        return 'X.Y', ''

# The short X.Y version.
# The full version, including alpha/beta/rc tags.
if os.access('version.py', os.R_OK):
    # get version and release information from version.py file
    exec(open('version.py').read())
else:
    # or fetch them from git repository data
    version, release = get_version_release_from_git()

today_fmt = '%Y-%m-%d'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
os_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if os_rtd:
    html_theme = 'default'
else:
    html_theme = 'bizstyle'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# ensure quotes and dashes are preserved and not converted to lang-specific
# entities (fix issue#250). `html_use_smartypants` option is for Sphinx <1.6
# and `smartquotes` option is for Sphinx >=1.6.
html_use_smartypants = False
smartquotes = False

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Modulesdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
]


# replace locations by pattern to pre-generate pages in dist
if 'pathsubs' in tags:
    prefix = '@prefix@'
    bindir = '@bindir@'
    libexecdir = '@libexecdir@'
    etcdir = '@etcdir@'
    initdir = '@initdir@'
    modulefilesdir = '@modulefilesdir@'
# or set default distributions location
else:
    prefix = '/usr/share/Modules'
    bindir = prefix + '/bin'
    libexecdir = prefix + '/libexec'
    etcdir = prefix + '/etc'
    initdir = prefix + '/init'
    modulefilesdir = prefix + '/modulefiles'

rst_epilog = '\n'
rst_epilog += '.. |prefix| replace:: %s\n' % prefix
rst_epilog += '.. |emph prefix| replace:: *%s*\n' % prefix
rst_epilog += '.. |bold prefix| replace:: **%s**\n' % prefix
rst_epilog += '.. |bindir| replace:: %s\n' % bindir
rst_epilog += '.. |emph bindir| replace:: *%s*\n' % bindir
rst_epilog += '.. |bold bindir| replace:: **%s**\n' % bindir
rst_epilog += '.. |libexecdir| replace:: %s\n' % libexecdir
rst_epilog += '.. |emph libexecdir| replace:: *%s*\n' % libexecdir
rst_epilog += '.. |bold libexecdir| replace:: **%s**\n' % libexecdir
rst_epilog += '.. |etcdir| replace:: %s\n' % etcdir
rst_epilog += '.. |emph etcdir| replace:: *%s*\n' % etcdir
rst_epilog += '.. |bold etcdir| replace:: **%s**\n' % etcdir
rst_epilog += '.. |initdir| replace:: %s\n' % initdir
rst_epilog += '.. |emph initdir| replace:: *%s*\n' % initdir
rst_epilog += '.. |bold initdir| replace:: **%s**\n' % initdir
rst_epilog += '.. |modulefilesdir| replace:: %s\n' % modulefilesdir
rst_epilog += '.. |emph modulefilesdir| replace:: *%s*\n' % modulefilesdir
rst_epilog += '.. |bold modulefilesdir| replace:: **%s**\n' % modulefilesdir


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('module', 'module', u'command interface to the Modules package', [], 1),
    ('modulefile', 'modulefile', u'files containing Tcl code for the Modules package', [], 4)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
]
