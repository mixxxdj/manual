# Mixxx User Manual

This repository contains the sources for the Mixxx User Manual as
found at <http://mixxx.org/manual/latest/>.

The manual is written in [reStructuredText] format using the
[Sphinx] documentation generator.

## Getting Started

First [Download] the latest Mixxx manual source or clone the repository

    $ git clone https://github.com/mixxxdj/manual.git

Next, install the dependencies using [pip]. From within the repository root
(type ```cd manual``` after typing the above command):

    $ pip install -r requirements.txt

If you do not wish to use pip:
* [Install Sphinx], the documentation generator.
* [Install Graphviz], graph visualization software (used to draw some diagrams)

To upgrade dependencies using pip:

    $ pip install -r requirements.txt --upgrade

If you'd like to build manual PDFs, you will need a functioning LaTeX installation.
* On Mac, install [MacTeX (Basic TeX)].
* On Debian-based systems, install `texlive-fonts-recommended` and
  `texlive-latex-extra`.

Once you have the repository cloned and dependencies installed you can edit and
build the manual to see your changes.

* Edit .rst files in `source/`
* Run `make html` to build an HTML version of the manual
* Open the file `build/html/index.html` in your Web browser to view the results

Run `make linkcheck` in the terminal. Sphinx will validate all internal and
external links in the document, and let you know if any links are malformed, or
point to dead URLs.

## Guidelines for Mixxx Manual writers

The Mixxx manual is based on sound learning principles, and is supposed to be
user-friendly & motivational. Please refer to the [guidelines](manual_guidelines.rst) for style
conventions.

## Editing the manual using git (recommended)

* Clone the repository `git clone https://github.com/mixxxdj/manual.git`
* Perform changes
* Commit changes `git commit -m "Insert short summary of your changes here"`
* Push changes `git push`
* Submit a [pull request]

## Editing the manual on Github

* Commit [file edits] through the GitHub web interface using the [Fork and Edit]
  button
* Submit a [pull request]

## Internationalization (i18n)

The Mixxx manual is translated using the [Transifex] web service for team translation.

### Prerequisites

If you did **not** install requirements with `pip install -r requirements.txt`
above then you must manually install the following dependencies:

* [sphinx-intl], a utility that makes it easy to translate and compile
  translations to Sphinx projects.
* [transifex-client]. Transifex allows collaborative translation via a web
  interface. The Python-based command line client makes it easy to fetch and
  push translations.

**Install transifex-client on Linux and macOS**

    $ pip install transifex-client

**Install transifex-client on Windows**

   The easiest way to install it is with pip:

    $  easy_install pip
    $  pip install transifex-client

  The first line installs pip on a system level. Then it installs the Transifex
  Client using pip.

  If you do not wish to use pip, download the latest releases from
  https://github.com/transifex/transifex-client/releases

You will need to make a `.transifexrc` in your home directory with your
username and password to use the Transifex client. See
[transifex-configuration] for more details.

### Maintaining translations

These steps document how to maintain the translations of the Mixxx
manual. **Typically, unless you are a manual maintainer you do not need to
perform these steps.** However, it is appreciated if you update the source
translations when making changes to the manual.

#### Update source translations

For every change to the manual source files (.rst) the source translation files
(.pot) must be re-generated. These are stored in `source/locale/pot` and contain
the text of every English phrase in the manual in a common format used for
translation.

Additionally, for every new source file added (i.e. new chapters or manual
pages) the Transifex configuration file (stored in `.tx/config`) needs updating.

To do both of these, run:

    fab i18n_update_source_translations

Commit the new source translations and Transifex configuration with:

    git add source/translations/pot .tx
    git commit -m "Update source translations and Transifex configuration."

#### Push source translations to Transifex

After generating new source translation files and updating the Transifex
configuration, you must push the new source files to Transifex to be translated.

To do this, run:

    fab tx_push

#### Pull completed translations from Transifex

To pull newly completed translation (.po) files from Transifex, run:

    fab tx_pull

Commit the changes to the repository with:

    git add source/translations
    git commit -m "Pull latest translations from Transifex."

#### Compile the translations from Transifex and verify there are no errors.

To compile the translations (.po) from Transifex into compiled translation (.mo)
files, run:

    fab i18n_build

We do not check .mo files into the repository, so make sure you do not add
them (they are ignored by our `.gitignore`).

### To build a translated manual in a particular language:

**Note:** it's good practice to clean your build directory first:

    fab clean

For example, to build an HTML manual for `de-DE` (Germany/Germany):

    fab i18n_build html:language=de-DE

Unless an error occurred, your translated HTML manual is in the `build/html`
directory.

To build a PDF manual:

    fab i18n_build pdf:language=de-DE

Your translated PDF manual is located at `build/latex/Mixxx-Manual.pdf`.

For more information on Translating with Sphinx, see [Sphinx i18n].

## Release Checklist for maintainers

* Fix and delete todos listed in `build/html/todolist.html`
* Fix and close issues listed in https://github.com/mixxxdj/manual/issues
* Temporarily disable the *For documentation writers* toctree from TOC in `/index.rst`
* Update the release and version tags in `/conf.py`
* [Tag] the repository with the version number, and [create a new release].
* Run `fab html` to produce html output ready for upload to
  http://mixxx.org/manual/latest/
* Check the output compiles correctly and does not produce any warnings
* Add translated html output for all available languages, see [i18n]
* Run `fab pdf` to produce PDF output for distribution

## Troubleshooting

### Linux troubleshooting
ON some systems, using the system package version of pip and running the command
`pip install -r requirements.txt` might damage the python installation.
Concretely, pyopenssl might get damaged and you might get an error saying
`'module' object has no attribute 'SSL_ST_INIT'`

This happens because the repository has an old version and when
installing/updating the requirements, the scripts break.

The solution to fix this consists on deleting the broken files,
remove the installed package and install it manually (all commands require
access privileges, so use sudo or whatever you need)

Fix python:
```
rm -rf /usr/lib/python2.7/dist-packages/OpenSSL
rm -rf /usr/lib/python2.7/dist-packages/pyOpenSSL-0.15.1.egg-info
```
Remove pip and repair python just in case:
```
apt-get purge python-pip
apt-get install --reinstall python
```
Install pip manually:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Alternatively, instead of installing pip on the system, you can also install a
python-virtualenv and then use PyPI in that virtualenv.

### Windows troubleshooting
First, in order to have "pip", you need to install python. Python 2.7.12 and
onwards already include pip, but you should follow the steps to upgrade it:
```
python -m pip install -U pip
```
When installing the required dependencies, you will most probably get an error
which says that you need to manually install Visual studio.
Concretely, you will see this:
```
error: Microsoft Visual C++ 9.0 is required (Unable to find vcvarsall.bat).
Get it from http://aka.ms/vcpython27
```
Follow that link to download an installer named VCForPython27.msi.
Also, in that same link, open the "System requirements" section and download the
x86 or x64 (or both) version of the Microsoft Visual C++ runtimes.

### macOS troubleshooting

After installing the requirements via ``pip install -r requirements.txt`` and
running ``make html``, you might get the error
```
WARNING: dot command 'dot' cannot be run (needed for graphviz output), check the
graphviz_dot setting
```

Graphviz possibly is not installed to its default location (the path must
contain an executable, not only a directory)
``/usr/local/bin/dot`` or ``/usr/bin/dot``.

Check the path with
```
pip show graphviz
```

Uninstall
```
pip uninstall graphviz
```

install again using [brew]

```
brew install graphviz
```

## Resources

### Sphinx and RST syntax guides:

* <http://sphinx-doc.org/rest.html>
* <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>
* <http://www.siafoo.net/help/reST>
* <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>

### Editors with Restructured Text (reST) syntax highlighting

* Windows, Linux, macos : [Atom], [Visual Studio Code], [Sublime]
* Linux: [Kate], [Retext]
* Windows: [Intype]
* Webapp: [Notex]

### Still not enough?

Even more [reStructuredText] resources:
<http://stackoverflow.com/questions/2746692/restructuredtext-tool-support>

[pip]: https://pip.pypa.io/
[reStructuredText]: http://docutils.sourceforge.net/rst.html
[Sphinx]: http://sphinx-doc.org
[Install Sphinx]: http://sphinx-doc.org/latest/install.html
[Sphinx i18n]: http://sphinx-doc.org/intl.html
[Install Graphviz]: http://graphviz.org/Download..php
[sphinx-intl]: https://pypi.python.org/pypi/sphinx-intl

[Transifex]: https://www.transifex.com/organization/mixxx-dj-software/dashboard/mixxxdj-manual
[transifex-client]: https://docs.transifex.com/client/installing-the-client
[transifex-configuration]: https://docs.transifex.com/client/client-configuration/
[Atom]: https://atom.io/
[Visual Studio Code]: https://code.visualstudio.com/
[Sublime]: http://www.sublimetext.com
[Kate]: http://kate-editor.org/
[Retext]: http://sourceforge.net/p/retext/
[Intype]: http://inotai.com/intype
[Notex]: https://www.notex.ch/
[Download]: https://github.com/mixxxdj/manual/archive/manual.zip
[file edits]: https://help.github.com/articles/creating-and-editing-files-in-your-repository#editing-a-file
[Fork and Edit]: https://github.com/blog/844-forking-with-the-edit-button
[pull request]: https://help.github.com/articles/creating-a-pull-request
[Tag]: https://github.com/mixxxdj/manual/tags
[create a new release]: https://github.com/mixxxdj/manual/releases/new
[i18n]: #internationalization-i18n
[MacTeX (Basic TeX)]: https://tug.org/mactex/morepackages.html
[brew]: https://brew.sh/
