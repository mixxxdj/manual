.. include:: /shortcuts.rstext

DJing With Mixxx
****************

Mixxx was designed to be easy to learn for both novice and experienced DJs.

This part of the manual provides you with directions for using Mixxx's features 
to create your own mixes.

.. _beatmatching-and-mixing:

Beatmatching and Mixing
=======================

:term:`Beatmatching` is the process of adjusting the playback rate of a track so
that it matches the tempo of another track. Beatmatching also involves adjusting
the :term:`phase` of the beats in a track so that they are aligned with the
beats in the other track. Matching the :term:`tempo` and aligning the beats are
the two things a DJ must do to beatmatch.

Mixxx can match the tempo and align the beats for you but this requires an
accurately detected BPM value and a correct beat grid for both tracks. To enable
this feature, tap the :guilabel:`SYNC` button. To beatmatch manually, the tempo
of the two tracks must be synchronized by adjusting the playback rate
sliders. You can adjust the phase of the beats by right-clicking and dragging on
either waveform display to temporarily speed up or slow down one of the tracks
until the beats are aligned. The temporary pitch bend buttons can also be used
to momentarily adjust the playback rate, allowing you to “shuffle” the beats in
a track forwards or backwards, so they can be aligned with another track. See
the chapter :ref:`interface-rate`.

Two tracks are beatmatched once their tempos are matched and their beats are
aligned. A “perfect” beatmatch is nearly impossible - there will always be a
tiny difference in the playback rates. A keen DJ will keep his or her ears open
and listen for the beats drifting out of alignment. This has a distinct “double
bass kick” sound which is often preceded by the kick weakening in intensity as
the two kicks drift out of phase. When this happens, the beats can be realigned
by simply tapping one of the temporary pitch bend buttons a few times in the
appropriate direction.

.. _djing-with-effects:

Use Effects
===========

.. versionadded:: 1.12

Mixxx comes with a set of native effects.

.. _effects-flanger:

Flanger
-------

.. figure:: ../_static/Mixxx-111-Deere-Mixer-FX.png
   :align: center
   :width: 321px
   :figwidth: 100%
   :alt: The effect control section of the mixer
   :figclass: pretty-figures

   Flanger controls

This effect applies a “sweeping” sound to the channel and can add extra depth to
a mix when used tactfully.

**FX Button**
  The FX (“Effects”) button enables a built-in flanger effect on the selected
  channel.

**Delay/Depth/LFO Knobs**
  Adjusts the phase delay, intensity and the wavelength of the flange effect.

.. hint :: For the most noticeable effect, enable the FX button and turn the
           Depth knob completely to the right.


.. _effects-bitcrusher:

BitCrusher
----------

.. figure:: ../_static/Mixxx-112-LateNight-Effects-BitCrusher.png
   :align: center
   :width: 321px
   :figwidth: 100%
   :alt: The effect control section of the mixer
   :figclass: pretty-figures

   BitCrusher controls

The BitCrusher is an effect that adds quantisation noise to the signal
by the reduction of the resolution or bandwidth of the samples

**Bit Depth**
  Adjusts the bit depth of the samples.

**Downsampling**
  Adjusts the sample rate, to which the signal is downsampled.

.. _effects-filter:

Filter
------

.. figure:: ../_static/Mixxx-112-LateNight-Effects-Filter.png
   :align: center
   :width: 321px
   :figwidth: 100%
   :alt: The effect control section of the mixer
   :figclass: pretty-figures

   Filter controls

The filter changes the tone of the music by allowing only high or low
frequencies to pass through.

**LPF**
  Corner frequency ratio of the low pass filter

**Q**
  Resonance of the filters, default = Flat top

**HPF**
  Corner frequency ratio of the high pass filter

.. _effects-reverb:

Reverb
------
.. figure:: ../_static/Mixxx-112-LateNight-Effects-Reverb.png
   :align: center
   :width: 321px
   :figwidth: 100%
   :alt: The effect control section of the mixer
   :figclass: pretty-figures

   Reverb controls


This is a port of the GPL'ed CAPS Reverb plugin, which has the following
description: This is based on some of the famous Stanford CCRMA reverbs (NRev,
KipRev) all based on the Chowning/Moorer/Schroeder reverberators, which use
networks of simple allpass and comb delay filters.

**Bandwidth**
  Higher bandwidth values cause more bright (high-frequency) tones to be
  included

**Damping**
  Higher damping values cause reverberations to die out more quickly.

.. note:: This effect is not available in the Mac App Store version of Mixxx.

.. _effects-echo:

Echo
----

.. figure:: ../_static/Mixxx-112-LateNight-Effects-Echo.png
   :align: center
   :width: 321px
   :figwidth: 100%
   :alt: The effect control section of the mixer
   :figclass: pretty-figures

   Echo controls

Simple Echo with pingpong

**Send**
  How much of the signal to send into the delay buffer

**Delay**
  Delay time (seconds)

**Feedback**
  Amount the echo fades each time it loops

**PingPong**
  As the ping-pong amount increases, increasing amounts of the echoed signal is
  bounced between the left and right speakers.

.. _master-sync:

Master Sync
===========

.. versionadded:: 1.12

:term:`Master Sync` is an intelligent assistant that allows you to leave the
beatmatching to Mixxx so you can focus on track selection, effects manipulation,
looping, 4 deck mixing, and other advanced DJing techniques.

To activate Master Sync on a deck, push and hold (or click and hold) the
:guilabel:`SYNC` button. You'll know Master Sync is on because the sync button
will remain lit.  Changing the rate of any deck that has Sync lit will change
the rates of all other decks that also have the Sync button lit.  There is no
need to set specific decks to be a master or followers.  You can play, stop,
eject, load, and queue any track with master sync and it won't interrupt the
playback of the other decks.  Changing the rate of stopped deck will change the
rate of playing decks, however.

Master Sync will also notice if one of your tracks is double the BPM of another
track and match them correctly.  So if you want to mix a 140 BPM drum & bass
track with a 70 bpm dubstep track, Master Sync will make sure they are lined up
properly.

.. hint:: Usually, Master Sync will only make sure the rate sliders are set
          correctly.  If you also want to make sure your beats are perfectly in
          sync, turn on the :guilabel:`QUANTIZE` button.  When activated,
          Quantize will ensure that the beats are perfectly lined up as well.

.. _harmonic-mixing:

Harmonic Mixing
===============

Harmonic mixing is a technique to mix songs with matching melodies and
harmonies. To learn more about harmonic mixing you might want to check out `the
mixshare site`_.

.. _the mixshare site: http://www.mixshare.com/wiki/doku.php?id=harmonic_mixing

Mixxx has two features to help you with harmonic mixing. The first is a
:term:`key lock`. When it is active changing the speed of a track won't affect
the key. To enable :term:`key lock`, click the :guilabel:`key lock` button in
the :ref:`interface-button-grid`. The second is that Mixxx can automatically
detect the key of a track and will display it in the library and the decks. The
standart which is used to display a key can be changed in `key preferences`_.

.. _key preferences: key-detection_

.. _headphone-cueing:

Headphone Cueing
================

Headphone cueing is a technique DJs use to listen to the next track they want to
play in their headphones before playing it on the main speakers. Headphone
cueing is useful because it allows a DJ to beatmatch the next track in their
headphones before bringing it into their mix by sliding the crossfader.

Mixxx allows a DJ to route audio from either deck to their headphones by
toggling either of the :guilabel:`Headphone` buttons in the mixer section of
Mixxx's interface. See the chapter :ref:`interface-mixer`.

.. _djing-recording-your-mix:

Recording your Mix
==================

.. sectionauthor::
   S.Brandt <s.brandt@mixxx.org>

With the integrated recording feature you can record your mix as an audio file
and listen to it later, distribute it as :term:`Podcast` or burn it to CD.
Mixxx records the master output - the audio you hear from the speakers including
the microphone.

.. figure:: ../_static/Mixxx-111-Library-Recordings.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Mixxx library - Recordings view
   :figclass: pretty-figures

   Mixxx library - Recordings view

Mixxx can record your mix in various audio formats and quality settings. You can
split your recordings, generate :term:`cue files <cue sheet>`, choose a custom
recording directory and even set your own :term:`metadata`. By default, Mixxx
saves your recordings as lossless :term:`wav` files to a
:file:`Mixxx/Recordings` sub-folder in the Mixxx music directory. Before you
start recording, we recommend that you adjust the settings in
:menuselection:`Preferences --> Recording`.

If you click on the *Recordings* icon in the sidebar of the Mixxx library, the
track table to the right displays the content of your recordings directory. New
recordings are automatically saved to this directory as well as CUE files if you
choose to create them in the preferences.

Record your mix to disk
-----------------------

.. versionadded:: 1.12
   Displays the duration of the recording.

* Click on the *Recordings* icon in the sidebar to switch to the
  :guilabel:`Recordings` view
* Click the :guilabel:`Start Recording` button or click
  :menuselection:`Options --> Record Mix` in the menu on top of the Mixxx
  application window.
* The display above the track table shows how many data has already been
  recorded, as well as the duration of the recording.
* Perform your mix
* Click the :guilabel:`Stop Recording` button to stop the recording when the mix
  has finished.

.. hint:: You can instantly play your recording as track in Mixxx. Simply
          drag-and-drop the track to a deck.

Burn your recorded mix to a CD/DVD
----------------------------------

* Select your recording in the :guilabel:`Recordings` view
* Right-click and select :guilabel:`Open in File Browser` to locate the file on
  your disk
* Now burn the recording to a CD/DVD using a 3rd-party program, for example
  `CDBurnerXP <http://www.cdburnerxp.se/>`_ for Windows or
  `Burn <http://burn-osx.sourceforge.net/>`_ for Mac OS X.

.. note:: Due to licensing restrictions, :term:`MP3` recording is not enabled
          per default. In order to enable MP3 streaming you must install the
          :term:`LAME` MP3 :term:`codec` yourself. Go to the chapter
          :ref:`MP3 Streaming` for more information.

.. _djing-auto-dj:

Using Auto DJ for automatic mixing
==================================

.. sectionauthor::
   S.Brandt <s.brandt@mixxx.org>

.. figure:: ../_static/Mixxx-111-Library-Auto-DJ.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Mixxx library - Auto DJ view
   :figclass: pretty-figures

   Mixxx library - Auto DJ view

Auto DJ allows you to automatically load tracks from the Auto DJ playlist when
the current track is nearly finished, and crossfade into it.  See
:ref:`library-auto-dj`.

Loading tracks into Auto DJ
---------------------------

To play tracks automatically, they must first be loaded into the Auto DJ
playlist. The Auto DJ playlist is empty by default.

.. figure:: ../_static/Mixxx-111-Library-Add-to-Auto-DJ.png
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Mixxx library - Adding a playlist to Auto DJ
   :figclass: pretty-figures

   Mixxx library - Adding a playlist to Auto DJ

There are several ways to load tracks into the Auto DJ playlist:

* Select single or multiple tracks from the library, a regular playlist or crate
  and drag them to the Auto DJ icon on the left.
* Select a regular playlist or crate, right-click with the mouse and select
  :guilabel:`Add to Auto DJ` from the mouse menu. This adds all tracks to Auto DJ.
* While in the Auto DJ view of the library, drag tracks from external file
  managers to the Auto DJ icon in the sidebar or to the Auto DJ track table on
  the right.

Playing tracks in Auto DJ
-------------------------

Now that you have loaded tracks into the Auto DJ playlist, you can activate Auto
DJ as follows:

* Click on the *Auto DJ* icon in the sidebar to switch to the :guilabel:`Auto
  DJ` view of the library.
* Click the :guilabel:`Enable Auto DJ` button.
* The first tracks from your list are loaded into the decks and the playback
  starts.
* Mixxx will continue to automatically mix until the Auto DJ playlist is empty.
* Click the :guilabel:`Disable Auto DJ` button to stop the automatic mixing
