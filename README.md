Mixxx User Manual
=================

This repository contains the sources for the Mixxx User Manual as
found at <http://mixxx.org/manual/latest/>.

The manual is written in [reStructuredText] format using the
[Sphinx] documentation generator.

## Steps for use:

* [Install Sphinx], the documentation generator
* [Install Graphviz], a graph visualization software (is used to draw some diagrams)
* [Download] the latest Mixxx manual source or clone the repository
  `git clone https://github.com/mixxxdj/manual.git`
* Edit .rst files in `source/`
* Run `make html` to build an HTML version of the manual
* Open the file `build/html/index.html` in your Web browser to view the results

Run `make linkcheck` in the terminal. Sphinx will validate all internal and
external links in the document, and let you know if any links are malformed, or
point to dead URLs.

## Guidelines for Mixxx Manual writers

The Mixxx manual is based on sound learning principles, and is supposed to be
user-friendly & motivational. Please refer to the guidelines for style
conventions:

  * Run `make html` to build an HTML version of the manual, then open
    `build/html/manual_guidelines.html` in your browser (recommended).
  * Alternatively, open https://github.com/mixxxdj/manual/blob/manual/source/manual_guidelines.rst
    for a quick overview. Github may not render all code correct.

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

* Install [sphinx-intl], a utility tool that provides several features that make it easy to translate and to apply translation to Sphinx generated documents.
* Install [transifex-client]. Transifex allows collaborative translation via a web interface. The Python-based command line client makes it easy to fetch and push translations.

  Install transifex-client on Linux and Mac OS X

  `pip install transifex-client`

  Install transifex-client on Windows

  `http://files.transifex.com/transifex-client/0.11b3/tx.exe`

### Maintaining the Mixxx manual translations

* Clean the build directory

 `make clean`

* Extract translatable strings into translation templates (`.pot` files):

 `make gettext`

* Generate the Transifex file-to-resource mappings in `.tx/config`:

 `sphinx-intl update-txconfig-resources --pot-dir source/locale/pot --transifex-project-name mixxxdj-manual --locale-dir source/locale`

* Push the `.pot` files to Transifex with:

 `tx push -s`

* (optional) Translate on Transifex


* Download the translated strings from Transifex:

 `tx pull -l`

* Build the translated manual for the target language, e.g `de-DE` for German/Germany:

`sphinx-intl build --locale-dir source/locale
make -e SPHINXOPTS="-D language='de-DE'" html`


**Congratulations! You got the translated manual in the** `_build/html` **directory.**


For more infos on Translating with Sphinx, see [Sphinx i18n].

## Release Checklist for maintainers

* Fix and delete todos listed in `build/html/todolist.html`
* Fix and close issues listed in https://github.com/mixxxdj/manual/issues
* Temporarily disable the *For documentation writers* toctree from TOC in `/index.rst`
* Update the release and version tags in `/conf.py`
* [Tag] the repository with the version number, and [create a new release].
* Run `make html` to produce html output ready for upload to http://mixxx.org/manual/latest/
* Check the output compiles correctly and does not produce any warnings
* Add translated html output for all available languages, see [i18n]
* Run `make latexpdf` to produce pdf output for distribution
* Run `make latexpdf` again, or the TOC is missing from the resulting pdf

## Resources

### Sphinx and RST syntax guides:

* <http://sphinx-doc.org/rest.html>
* <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>
* <http://www.siafoo.net/help/reST>
* <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>

### Editors with Restructured Text (reST) syntax highlighting

* Windows, Linux, Mac OSX : [Atom], [Sublime]
* Linux: [Kate], [Retext]
* Windows: [Intype]
* Webapp: [Notex]

### Still not enough?

Even more [reStructuredText] resources:
<http://stackoverflow.com/questions/2746692/restructuredtext-tool-support>

[reStructuredText]: http://docutils.sourceforge.net/rst.html
[Sphinx]: http://sphinx-doc.org
[Install Sphinx]: http://sphinx-doc.org/latest/install.html
[Sphinx i18n]: http://sphinx-doc.org/intl.html
[Install Graphviz]: http://graphviz.org/Download..php
[sphinx-intl]: https://pypi.python.org/pypi/sphinx-intl

[Transifex]: https://www.transifex.com/organization/mixxx-dj-software/dashboard/mixxxdj-manual
[transifex-client]: http://docs.transifex.com/client/setup/
[Atom]: https://atom.io/
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
[i18n]: #internationalization-\(i18n\)
