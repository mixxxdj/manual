Introduction to Mixxx
*********************

Mixxx allows you to perform live DJ mixes with your digital music collection.
It helps you rock the party with DJ controllers, vinyl turntables, or even
just your keyboard.

Mixxx is used by professional DJs and bedroom DJs alike. It is designed by an
international team of volunteer DJs who want to bring the joy of DJing to
everyone. The project is non-profit, open-source and community driven. Together
and with your help we aim to build the best DJ software ever created.

What Mixxx Does
===============
Mixxx is different from typical music player applications because it is designed
to play multiple audio files simultaneously and has many features to manipulate
the playback of the audio files. This allows for creatively mixing different music
together on the fly. Additionally, it allows you to preview the next track you
would like to play before the audience hears it, also known as headphone cueing.
In order to use headphone cueing, you need at least 2 separate audio outputs,
typically provided by a USB soundcard (also known as an “audio interface”). Mixxx can
be used in two different ways to provide headphone cueing:

**Internal Mixing**

  Mixxx plays multiple audio files on the computer at the same
  time, mixes them together, and sends the mixed output to one output. A
  separate signal is sent to the other output for headphone cueing. Often a DJ controller
  is used with internal mixing to provide easier control over Mixxx than a mouse and keyboard.

  .. figure:: ../_static/mixxx_setup_midi_integrated_sound.png
     :align: center
     :width: 75%
     :figwidth: 100%
     :alt: Using Mixxx together with a DJ controller and integrated soundcard
     :figclass: pretty-figures

     Using Mixxx together with a DJ controller for internal mixing. The DJ controller has an
     integrated soundcard that provides two separate stereo outputs.


**External Mixing**

  Mixxx plays multiple audio files on the computer at the same
  time and sends each track to a separate soundcard output. The soundcard's
  outputs are plugged into an external hardware mixer. The hardware mixer performs
  the actual mixing of the audio signals and provides separate outputs for the mixed
  signal to play to the audience and for the DJ to use headphone cueing. External mixing
  is typically used with vinyl control, and sometimes a small DJ controller is used to
  control features of Mixxx that are not available on the hardware mixer.

  .. figure:: ../_static/mixxx_setup_timecode_vc.png
     :align: center
     :width: 75%
     :figwidth: 100%
     :alt: Using Mixxx together with turntables and external mixer
     :figclass: pretty-figures

     Using Mixxx together with a USB sound card, external mixer, and timecode vinyl for
     external mixing

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

* `<https://www.wikipedia.org/>`_

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
  to: `<https://www.transifex.com/mixxx-dj-software/public/>`_ . Please
  read the `Translation FAQ <http://mixxx.org/wiki/doku.php/internationalization>`_
  first.

* **Social Media**: Follow us on `Twitter <https://twitter.com/mixxxdj>`_ ,
  `Facebook <https://www.facebook.com/pages/Mixxx-DJ-Software/21723485212>`_ ,
  and `Google+ <https://plus.google.com/+mixxx/posts>`_ .
