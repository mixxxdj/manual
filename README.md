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
conventions.

* Open the files `source/manual_guidelines.rst` in your editor or
  `build/html/manual_guidelines.html` in your Web browser.

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

---
### Sphinx and RST syntax guides:

* <http://sphinx-doc.org/rest.html>
* <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>
* <http://www.siafoo.net/help/reST>
* <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>

### Editors with Restructured Text (reST) syntax highlighting

* Windows, Linux, Mac OSX : [Sublime]
* Linux: [Kate] or [Retext]
* Windows: [Intype]

### Still not enough?

Even more [reStructuredText] resources:
<http://stackoverflow.com/questions/2746692/restructuredtext-tool-support>

---
## Release Checklist for maintainers

* Fix and delete todos listed in `build/html/todolist.html`
* Fix and close issues listed in https://github.com/mixxxdj/manual/issues
* Temporarily disable the *For documentation writers* toctree from TOC in `/index.rst`
* Update the release and version tags in `/conf.py`
* [Tag] the repository with the version number, and [create a new release].
* Run `make html` to produce html output ready for upload to http://mixxx.org/manual/latest/
* Check the output compiles correctly and does not produce any warnings
* Run `make latexpdf` to produce pdf output for distribution
* Run `make latexpdf` again, or the TOC is missing from the resulting pdf

[reStructuredText]: http://docutils.sourceforge.net/rst.html
[Sphinx]: http://sphinx-doc.org
[Install Sphinx]: http://sphinx-doc.org/latest/install.html
[Install Graphviz]: http://graphviz.org/Download..php
[Sublime]: http://www.sublimetext.com
[Kate]: http://kate-editor.org/
[Retext]: http://sourceforge.net/p/retext/
[Intype]: http://inotai.com/intype
[Download]: https://github.com/mixxxdj/manual/archive/manual.zip
[file edits]: https://help.github.com/articles/creating-and-editing-files-in-your-repository#editing-a-file
[Fork and Edit]: https://github.com/blog/844-forking-with-the-edit-button
[pull request]: https://help.github.com/articles/creating-a-pull-request
[Tag]: https://github.com/mixxxdj/manual/tags
[create a new release]: https://github.com/mixxxdj/manual/releases/new
