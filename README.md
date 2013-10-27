Mixxx 1.11 User Manual
======================

This repository contains the sources for generating the Mixxx User Manual as
found at <http://mixxx.org/manual/1.11/>.

The user manual for Mixxx is written in [reStructuredText] format using the 
[Sphinx] documentation generator.

Sphinx and RST syntax guides:

* <http://sphinx-doc.org/rest.html>
* <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>
* <http://www.siafoo.net/help/reST>
* <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>

## Steps for use:

* [Install Sphinx], the documentation generator
* [Install Graphviz], a graph visualization software
* Download the [Mixxx 1.11 manual source]
* Edit .rst files in `source/`
* Run `make html`
* Open the file `build/html/index.html` in your Web browser to view the results

Run `make linkcheck` in the terminal. Sphinx will validate all internal and
external links in the document, and let you know if any links are malformed, or point to dead URLs.

## Guidelines

Open the file `build/html/manual_guidelines.html` in your Web browser to view the  
Guidelines for Mixxx Manual writers.

### Editors with Restructured Text (reST) syntax highlighting

* Windows, Linux, Mac OSX : [Sublime]
* Linux: [Kate] or [Retext]
* Windows: [Intype]

### Still not enough?

Even more resources:
<http://stackoverflow.com/questions/2746692/restructuredtext-tool-support>

[reStructuredText]: http://docutils.sourceforge.net/rst.html
[Sphinx]: http://sphinx-doc.org
[Install Sphinx]: http://sphinx-doc.org/latest/install.html
[Install Graphviz]: http://graphviz.org/Download..php
[Sublime]: http://www.sublimetext.com
[Kate]: http://kate-editor.org/
[Retext]: http://sourceforge.net/p/retext/
[Intype]: http://inotai.com/intype/
[Mixxx 1.11 manual source]: https://github.com/mixxxdj/manual/tree/manual-1.11.x
