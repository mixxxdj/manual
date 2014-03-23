Introduction to Mixxx
*********************

Mixxx allows you to perform live DJ mixes with your digital music collection.
It helps you rock the party with MIDI controllers, vinyl turntables, or even
just your keyboard.

Mixxx is used by professional DJs and bedroom DJs alike. It is designed by an
international team of volunteer DJs who want to bring the joy of DJing to
everyone. The project is non-profit, open-source and community driven. Together
and with your help we aim to build the best DJ software ever created.

Mixxx Features
==============

.. sectionauthor::
   S.Brandt <s.brandt@mixxx.org>

* **Dual Decks**: A scratchable, scrolling waveform marks beats and cue points
  of a track, along with a whole-song waveform overview for quick seeking.
* **Advanced Controls**: Change playback with time stretching, and loop beat
  segments.
* **Sampler Decks**: Perfect for dropping that vocal sample or airhorn.
* **iTunes Integration**: Use your playlists and songs from iTunes, Traktor,
  Rhythmbox, and Banshee.
* **BPM Detection and Sync**: Instantly detect and sync the tempo of your songs.
* **DJ Controller Support**: Control your DJ mixes with MIDI/HID controllers.
* **Timecode Support**: Use a real turntable or DJ-CD player as a controller.
* **Live Broadcasting**: Start a radio station and stream your mixes live over
  the Internet.
* **Powerful Mixing Engine**: Supports various file formats, custom EQ shelves,
  recording, etc.
* **Automatic Mixing**: Create a quick playlist and let Auto DJ take over.
* **Microphone Input**: Drop vocals or give shoutouts on the air.

New in Mixxx |version|
========================

.. sectionauthor::
   RJ Ryan <rryan@mixxx.org>
   S.Brandt <s.brandt@mixxx.org>

* 4 decks (including 4 vinyl control inputs if you want to use 4 turntables)
* Master sync
* Key detection and pitch shifting (independent of tempo) for harmonic mixing.
* 4 effect units for built-in effects (this also introduces all the necessary
  plumbing for LV2/VST, effect send/receive, and advanced chaining in a future
  release)
* Beatloop rolls (now you can create beatloops and automatically jump to where
  the track would have been if you hadn't enabled the loop when you release it)
* Resizable skins (yes, finally!)
* Vinyl control deck passthrough (switch to real vinyl temporarily)
* Auxiliary inputs that pass through to the master mix.
* Custom key notations (pick between traditional, OpenKey, Lancelot notation or
  a custom one)
* Beat jumping and loop move
* Multiple library folders
* Mono output and input support (easily do the Master/Headphone trick on one
  stereo output)
* Along with over 100 performance, quality and usability improvements.

* For a full list of features go to: `<http://mixxx.org/features/>`_
* For an overview of the new features, go to:
  `<http://mixxx.org/whats-new-in-mixxx-1-12>`_
* For a full list of new features and bugfixes, go to:
  `https://launchpad.net/mixxx/1.12.0 <https://launchpad.net/mixxx/+milestone/1.12.0>`_

.. seealso:: For an overview of previous changes, go to
             :ref:`appendix-version-history`.

System Requirements
===================

Mixxx is available for Windows, Mac OS X and GNU/Linux. Mixxx is designed to
use very few system resources, but the Mixxx Development Team suggests these
minimum requirements for having a great experience with Mixxx:

* A 2GHz or faster CPU
* At least 1GB of RAM
* A soundcard with 2 stereo audio outputs

About the Mixxx Project
=======================

Mixxx is designed by an international team of volunteer DJs who want to bring
the joy of DJing to everyone. The project is non-profit, open-source and
community driven. Together and with your help we aim to build the best DJ
software ever created.

Mixxx started as an open-source project because of demand for DJing software on
Linux, and discontent with proprietary DJ software on Windows and Mac OS X.
Today, Mixxx development is driven by the simple idea that together we can
create a better way to DJ, and that has brought Mixxx to the cutting edge.

Mixxx is the only free cross-platform vinyl control software and has the most
advanced MIDI/HID controller support via our innovative JavaScript-based
scripting engine. We are continuing to pursue new and exciting features that
give DJs more tools to create better live mixes.

Project History
---------------

Mixxx was originally created in 2002 as part of a PhD thesis on new interfaces
for DJing by Tue Haste Andersen. After releasing the project as open source,
dozens of contributors began modifying and improving Mixxx.

In 2006, a new development team lead by Adam Davison and Albert Santoni began
reorganizing the project to ensure smooth growth of both the code-base and the
number of contributors. A renewed focus on usability and stability has helped
Mixxx grow to become the most popular free DJ software in the world, receiving
over 1,000,000 downloads annually. Our committed team has worked hard to create
great DJ software, and this growth is a sign of our success.

In 2011, RJ Ryan took over as Lead Developer to successfully continue the teams
endeavor to make Mixxx a world-class DJ software.

As our user community grows, so does our development team - Over 150 developers,
artists, and translators have helped create Mixxx!

About the Mixxx Manual
======================

.. sectionauthor::
   S.Brandt <s.brandt@mixxx.org>

Some effort has been made to present the material in a way that is neither too
technical nor too dumbed-down. Take some time to look through it and you'll
find lots of hints that will enhance both your enjoyment and your productivity.

Through the manual you'll find text formatted like this:

* :menuselection:`Library --> Add new Playlist`

  This is to simplify the business of choosing commands in menus. In this
  example, the instruction means “Open the *Library* menu at the top of the
  application window and then choose the *Add new Playlist* command”.

* :guilabel:`Apply`

  This is used to indicate a certain area of the :term:`GUI`, including button
  labels, tabs, checkboxes, field names, values in selection lists etc. .

* :kbd:`STRG` + :kbd:`G`

  This is used to mark a keystroke, or a sequence of keystrokes. In this
  example, you would have to hold down the *STRG* key, then to press *G*.

* `<http://www.wikipedia.org/>`_

  Links to external websites are marked like this.

Important information in this manual are highlighted like this:

* .. note:: For anything that should receive a bit more attention.

* .. hint:: For supplementary information that lightens the work load.

* .. seealso:: For references to other documents or websites if they need
               special attention.

* .. warning:: For anything that needs to be done with caution.

Improving the Manual
--------------------

* **Send Feedback**: If you have comments, corrections or suggestions regarding
  the manual, `write us an email <feedback@mixxx.org?subject=Mixxx-Manual>`_.

* **Get the Source Code**: To download the source code for the Mixxx manual, go
  to: `<https://github.com/mixxxdj/manual>`_

Additional Resources
====================

.. sectionauthor::
   S.Brandt <s.brandt@mixxx.org>

Got questions? Need more information? Want to :ref:`contribute <contributing>` ?
There are a variety of other resources you can use to find out more.

* **Mixxx Website**: For general information and updates, as well as the latest
  news on Mixxx, go to: `<http://mixxx.org>`_

* **Mixxx Support Websites**: To get support from the Mixxx wiki, IRC channel
  or Developer mailing list, go to: `<http://mixxx.org/support>`_

* **Mixxx Community Forums**: To search for answers, post your question or
  answer other DJ's questions, go to: `<http://mixxx.org/forums>`_

* **Mixxx Source Code**: To download the source code for Mixxx, go to:
  `<https://github.com/mixxxdj/mixxx>`_

* **Mixxx Bug Tracker**: To report a bug or request a feature, go to:
  `<https://bugs.launchpad.net/mixxx>`_

* **Mixxx Translations**: To translate Mixxx and promote your mother tongue, go
  to: `<https://www.transifex.com/projects/p/mixxxdj/>`_ . Please read the 
  `Translation FAQ <http://mixxx.org/wiki/doku.php/internationalization>`_ first.

* **Social Media**: Follow us on `Twitter <http://twitter.com/mixxxdj>`_ ,
  `Facebook <https://www.facebook.com/pages/Mixxx-DJ-Software/21723485212>`_ ,
  and `Google+ <https://plus.google.com/102441931224839455484/posts>`_ . 
