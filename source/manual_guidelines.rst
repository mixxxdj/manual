.. include:: /shortcuts.rstext

Guidelines for Mixxx Manual writers
***********************************

.. sectionauthor:: S.Brandt <s.brandt@mixxx.org>

What is the intended outcome of the manual?
===========================================
A user who doesn\'t know Mixxx yet should be able to mix two tracks from their
music library in the shortest possible time.

(Future) characteristics of the Mixxx manual:

**User-friendly**
  Easy to use when, where, and how you need it. Watch how someone else uses the
  application. Watch them look for information in the manual (preferably someone
  who has never seen it before). Be consistent with the instructional design so
  users can follow a set pattern. Don't use software development terms.

**Based on sound learning principles**
  For example users should actually learn from it, not just refer to it. Use
  the KISS principle: keep it short and simple. Too much information can be
  overwhelming, so present one concept at a time. Explain simple features in a
  matrix.

**Motivational**
  Keeps users willing to push forward to higher levels. Present general concepts
  first to provide a frame of reference. Then move to more complex topics.

Group problems the user might hit in a particular task right there with the
instruction for that task. Do not force a user to go to a separate
“Troubleshooting” section. We can have such separate sections, but as an author
you should duplicate pitfalls and problems and include a solution in the task.

Technical conventions
=====================

Line Widths
-----------

Please configure your editor to have a max column-width of 80-columns. While it
is not a strict requirement, 80-column cleanliness makes it easy to tile
multiple buffers of code across a laptop screen, which provides significant
efficiency gains to developers.

Screenshots
-----------

Use English language settings when creating screen-shots of the Mixxx interface.
This might change if we ever have true
`i18n <https://en.wikipedia.org/wiki/Internationalization_and_localization>`_.
The preferred file format is PNG. **Don't add shadows** to application window
screen-shots as they are added automatically to the document with style-sheets.

Always include descriptive alt text and a figure description. The latter will be
numbered in the PDF export. That sets them apart from the text below.
Place screen-shots above the context you are going to explain.

Screenshots should only show the necessary area and not the entire screen where
not necessary. Use annotation on the screenshot if necessary to emphasize
elements, use color ``#FF1F90`` if possible for consistency.

.. rst:directive:: figure

   Use this directive to place images like Screen-shots. Example markup: ::

    .. figure:: /_static/icons/mixxx-icon.png
       :width: 64px
       :align: center
       :height: 64px
       :alt: Alternate text on mouse over
       :figclass: pretty-figures

       Insert descriptive caption here

Nice screenshot tools with build-in editor for annotations:

* macOS: `Skitch <https://evernote.com/products/skitch>`_
* Linux: `Shutter <http://shutter-project.org/>`_
* Windows: `ShareX <https://getsharex.com//>`_

Alternatively, import your screenshots into
`Inkscape <https://inkscape.org/>`_, add annotations and export as .png to
:file:`/static`. Then save the original work as .svg to :file:`/static` as well,
so any future contributor can work on your annotations at a later time.

File naming
-----------

As the manual grows over the time with new versions of Mixxx and new screenshots,
it is important to have files named consistently. Save files to the
:file:`/static` folder or create a sub-folder in there.

::

   Mixxx-<major><minor>-<where>-<what>.png

This scheme makes it easy to know which version a screenshot was taken from and
where it belongs and if it must replaced, like e.g.
:file:`Mixxx-111-Preferences-Recording.png`

.. warning:: Do not include any dot in the file names of your screenshots your
             file name or you won't be able to generate PDF with LaTeX.

Double quotes
-------------

Use curly double quotes (“ ”). Avoid typewriter double quotes (" ")
produced by the convenient quotation mark button on your keyboard.
For details and key combinations, see
`Wikipedia <https://en.wikipedia.org/wiki/Quotation_marks_in_English#Typing_quotation_marks_on_a_computer_keyboard>`_ .

Admonitions
-----------

The following admonitions are in use:

.. rst:directive:: note

   For anything that should receive a bit more attention. Example markup: ::

      .. note::
         a note

.. rst:directive:: hint

   For supplementary information that lightens the work load. Example markup: ::

      .. hint::
         a helpful hint

.. rst:directive:: seealso

   For references to other documents or websites if they need special attention.
   References to other documents can also be included in the text inline.
   Example markup: ::

      .. seealso::
         a reference and inline link `Google <https://google.com>`_

.. rst:directive:: warning

  Recommended over :rst:dir:`note` for anything that needs to be done with
  caution. Example markup: ::

      .. warning::
         a warning

.. rst:directive:: todo

   Allow inserting todo items into documents and to keep a
   :ref:`automatically generated TODO list <todo-list>` Example markup: ::

      .. todo::
         some task

Substitution
------------

Replacement images or text can be included in the text. They are added through
a substitution (aka alias). This may be appropriate when the replacement image
or text is repeated many times throughout one or more documents, especially if
it may need to change later.

All replacements are kept in the file :file:`shortcuts.rstext` which is included
at the beginning of each file in which a substitution is used.

To use an alias for the Mixxx logo, simply put the definition into
:file:`shortcuts.rstext`.

::

   .. |logo| image:: /_static/icons/mixxx-icon.png

Using this image alias, you can insert it easily in the text with ``|logo|`` ,
like this:  |logo|

For a text replacement the code looks similar:

::

   .. |longtext| replace:: Loooooooong text is looooooooong

Using this text alias, you can insert it easily with ``|longtext|`` , like this:
 |longtext| .

.. seealso:: The substitute section in the docs.
             `Here <http://www.thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#more-about-aliases>`_
             and `also here <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#substitution-definitions>`_

Headings
--------
Normally, there are no heading levels assigned to certain characters as the
structure is determined from the succession of headings. However, for the Python
documentation, this convention is used which you may follow:

   | ``#`` with overline, for parts
   | ``*`` with overline, for chapters
   | ``=`` for sections
   | ``-`` for subsections
   | ``^`` for subsubsections
   | ``"`` for paragraphs

Of course, you are free to use your own marker characters (see the reST
documentation), and use a deeper nesting level, but keep in mind that most
target formats (HTML, LaTeX) have a limited supported nesting depth.

Paragraph-level markup
----------------------

These directives create short paragraphs and can be used inside information
units as well as normal text:

.. rst:directive:: .. versionadded::  version

   This directive documents the version of the project which added the described
   feature. Example markup: ::

      .. versionadded:: 2.5 Add feature description.

.. rst:directive:: .. versionchanged:: version

   Similar to :rst:dir:`versionadded`, but describes when and what changed in
   the named feature in some way (new parameters, changed side effects, etc.).

Other semantic markup
---------------------
The following roles don't do anything special except formatting the text in a
different style. Nonetheless, use them:

.. rst:role:: guilabel

   Any label used in the interface should be marked with this role, including
   button labels, window titles, field names, menu and menu selection names,
   and even values in selection lists. An accelerator key for the GUI label can
   be included using an ampersand; this will be stripped and displayed
   underlined in the output. To include a literal ampersand, double it. Example
   markup: :guilabel:`&Cancel` ::

     :guilabel:`&Cancel`

.. rst:role:: kbd

   Mark a sequence of keystrokes. Example markup: :kbd:`STRG` + :kbd:`G` ::

     :kbd:`STRG` + :kbd:`G`

.. rst:role:: menuselection

   This is  used to mark a complete sequence of menu selections, including
   selecting submenus and choosing a specific operation. Example markup:
   :menuselection:`Options --> Enable Live Broadcasting` ::

       :menuselection:`Options --> Enable Live Broadcasting`

.. rst:role:: file

   The name of a file or directory. Example markup: :file:`Mixxx/Recordings` ::

       :file:`Mixxx/Recordings`

Meta-information markup
-----------------------

.. rst:directive:: .. sectionauthor:: name <email>

   Identifies the author of the current section and helps to keep track of
   contributions. By default, this markup isn't reflected in the output in any
   way. Example markup: ::

      .. sectionauthor:: Jon Doe <name@domain.tld>
