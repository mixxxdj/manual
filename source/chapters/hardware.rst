.. _hardware:

DJ Hardware
***********

.. sectionauthor::
   T.Rafreider <trafreider@mixxx.org>
   S.Brandt <s.brandt@mixxx.org>
   Be <be.0@gmx.com>

Although Mixxx can be used with just a laptop computer, fully taking advantage of
Mixxx's features requires specialized DJ hardware. Depending on your budget and
application area, your setup and requirements may vary. This section provides 
useful information for club, hobby, and radio DJs alike.

.. seealso:: The `Mixxx DJ Hardware Guide <http://mixxx.org/wiki/doku.php/hardware_compatibility>`_
             lists controllers and sound cards with information about
             their compatibility with Mixxx and different
             :term:`operating systems<operating system>`.
             
Types of DJ Hardware
====================

Controllers
-----------
DJ controllers are devices with knobs, faders, buttons, and jog wheels to 
control DJ software such as Mixxx. Controllers allow quick access to different 
controls while providing tactile and visual feedback indicating 
the state of each control, such as the position of a knob or whether a switch 
is on or off. This allows the DJ to focus on manipulating the music without 
needing to look at their computer screen all the time. Controllers also allow 
the DJ to use two hands to manipulate two different controls at the same time, 
which is required for many mixing techniques.

DJ controllers typically do not do any actual audio processing. Instead, they
send signals (typically :term:`MIDI` or :term:`HID` over a USB cable) to the
computer to instruct DJ software how to manipulate the audio. Many DJ
controllers include a soundcard with 2 separate stereo outputs built into the
device. This allows the DJ to transport and setup only one piece of hardware in
addition to a laptop. Some devices can be used as both controllers and hardware
mixers.

Soundcards
----------
A soundcard or audio interface is a device that allows a computer to send
output to and receive input from audio equipment. Whether using internal or
external mixing, it is recommended to use a single soundcard with at least 4
independent output channels (2 separate stereo pairs). Although the term
"soundcard" originated with card-shaped devices installed directly into desktop
computers, most DJs today use USB soundcards with laptop computers.

The headphone jack on most laptops is not a second audio output. Rather,
plugging headphones into the jack simply redirects the laptop's single stereo
output from its speakers to your headphones. A splitter cable can be used to
separate the stereo output of a headphone jack into two separate mono outputs
for headphone cueing, but it is recommended to use a sound card with at
least four mono outputs (for two stereo pairs). Such sound cards tend to be
higher quality than those built into laptops and allow your mix to be enjoyed
in stereo by your audience.

Unlike some proprietary DJ systems, Mixxx can use any soundcard and any
:term:`MIDI` or :term:`HID` controller that your :term:`OS <operating system>`
has drivers to use. If your controller has an integrated soundcard, you may
choose to use a different soundcard for higher quality audio. Mixxx can also
use multiple audio devices simultaneously.

Mixers
------
Mixers are devices that combine audio signals. Many DJ mixers have a
USB soundcard built into them to send unmixed audio files from DJ software
directly to the mixer without needing a separate stand-alone soundcard.

.. hint:: Often DJs who use DJ software with internal mixing send their
          master output to a hardware mixer. This can be helpful to send the
          mixed signal to both a main speaker output for the audience and booth
          speakers for the DJ with separate gain controls for each output. It
          also facilitates smooth transitions between DJs. However, using an
          external mixer with internal mixing is not necessary. Each piece of
          equipment an audio signal passes through reduces the sound quality,
          so avoiding unnecessary equipment in the signal path can provide
          better sound quality. Many DJ controllers provide separate master and
          booth outputs with independent volume controls. Alternatively, a
          sound card with at least 6 output channels can be used with Mixxx's
          Booth output.

.. hint:: Many people confuse "analog mixers" and "hardware mixers", but
          these are are not the same. Many hardware mixers process audio
          digitally with specialized signal processors as opposed to a general
          purpose CPU like those in laptop and desktop computers.

Turntables
----------

CDJs
----

Microphones
-----------

.. warning:: USB microphones are not recommended for use with Mixxx. These
             microphones have their own soundcard built in, which often creates
             complications when configuring it at the same time as a different
             soundcard for output. Some USB microphones have headphone jacks
             for direct monitoring, but this directly monitored signal only
             includes the microphone signal without the music from Mixxx.

Example Setups
==============

.. seealso:: :ref:`getting-started-sound-io` has details about each available
             input and output option.

.. _setup-laptop-only:

Laptop Only
-----------

.. figure:: ../_static/Mixxx-111-Preferences-Soundhardware.png
   :align: center
   :width: 75%
   :figwidth: 100%
   :alt: Using Mixxx with your built-in sound card
   :figclass: pretty-figures

   Using Mixxx with your built-in sound card

The built-in soundcard on most computers and laptops comes with a single stereo 
line-out and a microphone input. The figure above depicts how the sound 
configuration might look. The stereo output of your soundcard (channels 1-2) 
will be connected to the **Master out**.

#. Open :menuselection:`Preferences --> Sound Hardware`
#. Select the :guilabel:`Output` tab
#. From the :guilabel:`Master` drop-down menu, select your built-in soundcard,
   then :guilabel:`Channels 1-2`
#. Depending on your soundcard, you can specify a
   :ref:`microphone <interface-mic>`

   a. Use your built-in microphone or connect a microphone to your computer
   b. Check that your microphone is detected by your :term:`OS <operating system>`
   c. Open the :guilabel:`Input` tab
   d. From the :guilabel:`Microphone` drop-down menu, select the input your
      microphone is connected to
#. Click :guilabel:`Apply` to save the changes.

.. _setup-laptop-with-splitter:

Laptop and Splitter Cable
-------------------------

.. figure:: ../_static/mixxx_setup_splitter_adaptors.png
   :align: center
   :width: 75%
   :figwidth: 100%
   :alt: Using Mixxx with your built-in sound card and a DJ splitter cable
   :figclass: pretty-figures

The cheapest way to DJ and :term:`cue` with headphones uses a 
stereo-to-mono DJ splitter cable (also known as a “Y cable”) plugged
into the headphone jack of a laptop or other computer. This cable divides the
stereo output from a single jack into two separate mono singals.

This setup allows you to start DJing without having to invest in expensive 
equipment. However, your audience will not be able to enjoy music producers' 
artistic use of stereophonic sound (although many club PA systems are wired in 
mono anyway). Furthermore, soundcards built into computers are usually low
quality and often pick up interface from other components of the computer.

**Using a built-in soundcard and a stereo-to-mono splitter**

#. Open :menuselection:`Preferences --> Sound Hardware`
#. Select the :guilabel:`Output` tab
#. Check that your headphones are plugged into the side of the cable with a
   headphones symbol and that the speakers are plugged into the side of the cable
   with a speaker symbol.
#. From the :guilabel:`Master` drop-down menu, select your built-in soundcard,
   then :guilabel:`Channel 1`
#. From the :guilabel:`Headphones` drop-down menu, select your built-in 
   soundcard, then :guilabel:`Channel 2`
#. Click :guilabel:`Apply` to save the changes.

.. seealso:: See `the wiki
             <http://mixxx.org/wiki/doku.php/hardware_compatibility#splitter_cables>`_
             for a list of DJ splitter cables.

.. warning:: Most splitter cables, particularly those marketed as headphone
             splitter cables, output the same stereo signal to two headphone
             jacks and will not work for this DJ setup. Also, if you use a
             generic stereo-to-mono splitter adapter, you may only be able to
             hear out of one side of your speakers and headphones. DJ splitter
             cables allow you to hear the same mono signal on both sides of your
             headphones and speakers.

.. _setup-laptop-and-external-card:

Laptop and External USB Soundcard
---------------------------------

.. figure:: ../_static/mixxx_setup_ext_soundcard.png
   :align: center
   :width: 75%
   :figwidth: 100%
   :alt: Using Mixxx together with an external soundcard
   :figclass: pretty-figures

   Using Mixxx together with an external soundcard

**Using two soundcards (built-in + external)**

#. Open :menuselection:`Preferences --> Sound Hardware`
#. Select the :guilabel:`Output` tab
#. From the :guilabel:`Master` drop-down menu, select the external soundcard,
   then :guilabel:`Channels 1-2`
#. From the :guilabel:`Headphones` drop-down menu, select the built-in
   soundcard, then :guilabel:`Channels 1-2`
#. Select the :guilabel:`Input` tab
#. From the :guilabel:`Microphone 1` drop-down menu, select the external soundcard,
   then :guilabel:`Channel 1`
#. From the :guilabel:`Microphone Mix Mode` drop-down menu, select the
   :guilabel:`Direct monitor (recording and broadcasting only)` option.
#. Configure the soundcard to directly monitor the microphone input. Refer
   to the soundcard's manual for details.
#. Click :guilabel:`Apply` to save the changes.

**Using an external multi-channel soundcard**

#. Open :menuselection:`Preferences --> Sound Hardware`
#. Select the :guilabel:`Output` tab
#. From the :guilabel:`Master` drop-down menu, select the external soundcard,
   then :guilabel:`Channels 1-2`
#. From the :guilabel:`Headphones` drop-down menu, select the external
   soundcard, then :guilabel:`Channels 3-4`
#. Click :guilabel:`Apply` to save the changes.

.. _setup-controller-and-external-card:

Laptop and MIDI or HID Controller
---------------------------------

Most DJs prefer the tactile and intuitive control provided by DJ MIDI or HID
controllers over only a keyboard and mouse. Mixxx can work with any :term:`MIDI`
or :term:`HID` :term:`controller` as long as there is a mapping file
to tell Mixxx how to understand the controller's signals. Mixxx comes bundled
with a number of MIDI and HID mapping presets, which are listed in the
`Mixxx DJ Hardware Guide <http://mixxx.org/wiki/doku.php/hardware_compatibility>`_
on the wiki. For controllers that Mixxx does not yet support, you can `search
the forum <http://mixxx.org/forums/search.php?fid[]=7>`_ to see if anyone has
started a mapping. You can also start one yourself using the information in the
`Controller Mapping Documentation <http://mixxx.org/wiki/doku.php/start#controller_mapping_documentation>`_
on the wiki.

Controllers with an integrated soundcard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many DJ controllers include an integrated *multi-channel* soundcard.
A setup with this kind of controller may look like the diagram below:

.. figure:: ../_static/mixxx_setup_midi_integrated_sound.png
   :align: center
   :width: 75%
   :figwidth: 100%
   :alt: Using Mixxx together with a DJ controller and integrated soundcard
   :figclass: pretty-figures

   Using Mixxx together with a DJ controller and integrated soundcard

**Using a controller with an integrated multi-channel soundcard**

#. Open :menuselection:`Preferences --> Sound Hardware`
#. Select the :guilabel:`Output` tab
#. From the :guilabel:`Master` drop-down menu, select your controller's
   soundcard, then :guilabel:`Channels 1-2`
#. From the :guilabel:`Headphones` drop-down menu, select your controller's
   soundcard, then :guilabel:`Channels 3-4`
#. Click :guilabel:`Apply` to save the changes.

Controllers without an integrated sound card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Controllers without an integrated soundcard can be used together with a USB
soundcard as depicted in the diagram below:

.. figure:: ../_static/mixxx_setup_midi_with_ext_sound.png
   :align: center
   :width: 75%
   :figwidth: 100%
   :alt: Using Mixxx together with a DJ controller and external soundcard
   :figclass: pretty-figures

   Using Mixxx together with a DJ controller and external soundcard
          
**Using a controller without an integrated soundcard**

#. Open :menuselection:`Preferences --> Sound Hardware`
#. Select the :guilabel:`Output` tab
#. From the :guilabel:`Master` drop-down menu, select the external soundcard,
   then :guilabel:`Channels 1-2`
#. From the :guilabel:`Headphones` drop-down menu, select the built-in
   soundcard, then :guilabel:`Channels 1-2`
#. Click :guilabel:`Apply` to save the changes.

.. note:: You can connect as many controllers as you have ports on your
          computer. Just follow the steps in :ref:`control-midi` for each
          controller you want to use.

.. raw:: pdf

   PageBreak

.. _setup-vinyl-control:

Laptop, External Hardware Mixer and Vinyl Control
-------------------------------------------------

.. figure:: ../_static/mixxx_setup_timecode_vc.png
   :align: center
   :width: 75%
   :figwidth: 100%
   :alt: Using Mixxx together with turntables and external mixer
   :figclass: pretty-figures

   Using Mixxx together with turntables and external mixer

This setup allows DJs to use the techniques of DJing with vinyl record 
turntables combined with the portability and flexibility of a laptop computer. 
Instead of carrying crates of records or CDs, DJs can carry their entire music 
collection on their laptop. In addition to a laptop and headphones, this setup 
requires a soundcard with at least two pairs of stereo inputs and outputs
as well as a pair of :term:`timecode` records.

.. seealso:: Go to the chapter :ref:`vinyl-control` for detailed information.
