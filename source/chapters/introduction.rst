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

DJ Hardware
===========
Although Mixxx can be used with just a laptop computer, fully taking advantage of
Mixxx's features requires specialized DJ hardware.

.. seealso:: The `Mixxx DJ Hardware Guide
             <http://mixxx.org/wiki/doku.php/hardware_compatibility>`_
             lists controllers, sound cards, and mixers with information about
             their compatibility with Mixxx and different
             :term:`operating systems<operating system>`. It also has
             suggestions for what to consider when you are shopping for DJ
             equipment.

Controllers
-----------
DJs often use a device called a DJ controller which has knobs, faders, buttons,
jog wheels, and other components to control DJ software such as Mixxx. It is difficult
to manipulate Mixxx's controls fast enough while music is playing with only a keyboard
and mouse while looking at a computer screen. Controllers allow quick access to different
controls while providing tactile and visual feedback indicating the state of each control,
such as the position of a knob or whether a switch is on or off. This allows the DJ to
focus on manipulating the music without needing to look at their computer screen all
the time. Controllers also allow the DJ to use two hands to manipulate two different
controls at the same time, which is required for many mixing techniques.

DJ controllers typically do not do any actual audio processing. Instead, they
send signals (typically :term:`MIDI` or :term:`HID` over a USB cable) to the computer
to instruct DJ software how to manipulate the audio. Many DJ controllers include a
soundcard with 2 separate stereo outputs built into the device. This allows the DJ to
transport and setup only one piece of hardware in addition to a laptop. Some devices can
be used as both controllers and hardware mixers.

Soundcards
----------
A soundcard or audio interface is a device that allows a computer to send output to
and receive input from audio equipment. Whether using internal or external mixing,
it is recommended to use a single soundcard with at least 4 independent output channels
(2 separate stereo pairs). Although the term "soundcard" originated with card-shaped
devices installed directly into desktop computers, most DJs today use USB soundcards
with laptop computers.

The headphone jack on most laptops is not a second audio output.
Rather, plugging headphones into the jack simply redirects the laptop's single
stereo output from its speakers to your headphones. A splitter cable can be used
to separate the stereo output of a headphone jack into two separate mono outputs
for headphone cueing, but it is recommended to use a sound card with at least
four mono outputs (for two stereo pairs). Such sound cards tend to be higher quality
than those built into laptops and allow your mix to be enjoyed in stereo by your
audience.

Unlike some proprietary DJ systems, Mixxx can use any soundcard and any
:term:`MIDI` or :term:`HID` controller that your :term:`OS <operating system>`
has drivers to use. If your controller has an integrated soundcard, you may
choose to use a different soundcard for higher quality audio. Mixxx can also
use multiple audio devices simultaneously.

Mixers
------
Mixers are devices that combine audio signals. Many DJ mixers have a USB soundcard
built into them to send unmixed audio files from DJ software directly to the mixer
without needing a separate stand-alone soundcard.

.. hint:: Often DJs who use DJ software with internal mixing send their master output to
          a hardware mixer. This can be helpful to send the mixed signal to both a main
          speaker output for the audience and booth speakers for the DJ with separate gain
          controls for each output. It also facilitates smooth transitions between DJs. However,
          using an external mixer with internal mixing is not necessary. Each piece of
          equipment an audio signal passes through reduces the sound quality, so avoiding
          unnecessary equipment in the signal path can provide better sound quality. Many DJ
          controllers provide separate master and booth outputs with independent volume controls.
          Alternatively, a sound card with at least 6 output channels can be used with Mixxx's
          Booth output.

.. hint:: Many people confuse "analog mixers" and "hardware mixers", but these are
          are not the same. Many hardware mixers process audio digitally with
          specialized signal processors as opposed to a general purpose CPU like those in
          laptop and desktop computers.

Turntables
----------

CDJs
----

Microphones
-----------

.. warning:: USB microphones are not recommended for use with Mixxx. These microphones
             have their own soundcard built in, which often creates complications when
             configuring it at the same time as a different soundcard for output. Some
             USB microphones have headphone jacks for direct monitoring, but this directly
             monitored signal only includes the microphone signal without the music from
             Mixxx.

New in Mixxx |version|
========================

.. sectionauthor::
   RJ Ryan <rryan@mixxx.org>
   S.Brandt <s.brandt@mixxx.org>

* 4 decks
* Master sync
* Color-coded waveforms showing the frequencies in tracks
* Key detection and pitch shifting (independent of tempo) for harmonic mixing
* Choice of traditional, OpenKey, Lancelot, and custom key notations
* 4 effect units with built-in effects
* Controller mapping :term:`GUI`
* Resizable skins
* Beat jumping and loop move
* Multiple library folders
* Hierarchical library sorting
* Cover/album art support
* Vinyl passthrough mode to switch between control vinyl and music
  vinyl
* Auxiliary inputs that pass through to the master mix
* Mono output and input support
* Improved support for using multiple sound cards
* MusicBrainz tagging support
* Over 100 other performance, quality and usability improvements

* For a full list of features go to: `<http://mixxx.org/features/>`_
* For an overview of the new features, go to:
  `<http://mixxx.org/whats-new-in-mixxx-2-0>`_
* For a full list of new features and bugfixes, go to:
  `https://launchpad.net/mixxx/2.0.0 <https://launchpad.net/mixxx/+milestone/2.0.0>`_

.. seealso:: For an overview of previous changes, go to
             :ref:`appendix-version-history`.

System Requirements
===================

Mixxx is available for Windows, Mac OS X and GNU/Linux. Mixxx is designed to
use very few system resources, but the Mixxx Development Team suggests these
minimum requirements for having a great experience with Mixxx:

* A 2GHz or faster CPU
* At least 1GB of RAM
* A soundcard with 2 stereo audio outputs (4 mono output channels)

.. hint:: The EQs can be disabled to save CPU usage. Using this feature, Mixxx
          can be used with an external mixer and a less powerful computer such
          as a netbook.

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

In 2011, RJ Ryan took over as Lead Developer to successfully continue the team's
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
