.. include:: /shortcuts.rstext

DJing With Mixxx
****************

Mixxx was designed to be easy to learn for both novice and experienced DJs.

This part of the manual provides you with directions for using Mixxx's features
to create your own mixes.

.. _djing-gain-staging:

Setting Your Levels Properly (Gain Staging)
===========================================
.. sectionauthor::
   Be <be.0@gmx.com>

.. figure:: ../_static/level-meter-green.png
   :align: left
   :alt: A level meter in Mixxx with the gain set properly for the loudest part of a track
   :figclass: pretty-figures

Setting your levels properly, also known as gain staging, is essential for
getting the best sound quality out of the equipment you are using. At every link
in your signal chain, from Mixxx's channel gains to the power amplifier, the
level should be well above the noise floor, but lower than the maximum level
before the signal clips. The :term:`level meters <level meter>` should mostly be
around the top of their green region. The level meter pictured to the left shows
where Mixxx's level meters should average at the loudest parts of tracks. The
average level should not be in the yellow region. Use the yellow region to leave
headroom, or available level above the average before the signal clips. The
loudest parts of the music (the transients) should briefly go into the yellow
region.

.. figure:: ../_static/waveform-good.png
   :align: center
   :alt: A waveform at a good level
   :figclass: pretty-figures

   A waveform at a good level. Note that the example waveforms in this section
   were made by adjusting the visual gain of the waveform display in Mixxx to
   illustrate the concepts. Adjusting the visual gain of the waveform display
   does not change the level of the audio.

.. figure:: ../_static/level-meter-red.png
   :align: right
   :alt: A level meter in Mixxx indicating clipping. The gain should be turned down!
   :figclass: pretty-figures

**If a level meter is in its red region, the signal is clipping and the gain
should be turned down.** Some equipment doesn't have a level meter and only has
an LED that turns on when the signal clips. Clipping means that the peaks of the
waveform are flattened because the equipment has reached the maximum level that
it can amplify the signal to. This distorts sound in an unpleasant way and can
damage equipment by driving it with more power than it is designed to handle.
Increasing the gain past the point where clipping begins (further into the red
on a meter) will distort the signal more. If you want to make the sound louder
when every part of the signal chain is at its maximum without clipping, use more
speakers or use speakers that are more sensitive and convert electrical energy
into acoustic energy more efficiently.

.. figure:: ../_static/waveform-clipping.png
   :align: center
   :alt: A clipping waveform
   :figclass: pretty-figures

   A clipping waveform

.. figure:: ../_static/level-meter-too-low.png
   :align: left
   :alt: A level meter in Mixxx with the gain set too low
   :figclass: pretty-figures

On the other hand, the signal should not be too low. This is because every audio
device generates a little noise at a level referred to as its noise floor.
Additionally, analog signals pick up noise as they travel along wires. The signal
measured by the meter on the left is relatively close to the noise floor. When a
device is turned up, the noise floor does not go up; only the signal does.
However, every time the signal is amplified by the gain of another piece
of equipment, both the noise and the signal from previous devices in the signal
chain are amplified. For example, if your sound card is turned down and you turn
the gain up on your mixer to compensate, the signal-to-noise ratio (SNR) of the
sound card output will be low and the mixer's gain will amplify the signal and
the noise from the sound card, plus the noise picked up along the wire. The end
result will have more noise than if the output of the sound card was turned up
before the signal reached the mixer and the mixer's gain did not have to be
turned up.

.. figure:: ../_static/waveform-too-low.png
   :align: center
   :alt: A waveform at too low of a level
   :figclass: pretty-figures

   A waveform that is too close to the noise floor

   .. note:: To adjust the output volume of a sound system while maintaining a
             high signal-to-noise ratio, the gain should be adjusted as close to
             the speakers as possible. Refer to the
             :ref:`Gain Knob <interface-gain-knob>` section for details.

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

.. _master-sync:

Master Sync
===========

:term:`Master Sync` is an intelligent assistant that allows you to leave the
beatmatching to Mixxx so you can focus on track selection, effects manipulation,
looping, 4 deck mixing, and other advanced DJing techniques.

To activate Master Sync on a deck, push and hold (or click and hold) the
:guilabel:`SYNC` button. You'll know Master Sync is on because the sync button
will remain lit.  Changing the rate of any deck that has Sync lit will change
the rates of all other decks that also have the Sync button lit.  There is no
need to set specific decks to be a master or followers.  You can play, stop,
eject, load, and queue any track with master sync and it won't interrupt the
playback of the other decks.  However, changing the rate of a stopped deck will
change the rate of playing decks.

.. hint:: Usually, Master Sync will only make sure the rate sliders are set
          correctly.  If you also want to make sure your beats are perfectly in
          sync, turn on the :guilabel:`QUANTIZE` button.  When activated,
          Quantize will ensure that the beats are perfectly lined up as well.

.. _harmonic-mixing:

Harmonic Mixing
===============

Harmonic mixing is a technique to mix songs with matching melodies and
harmonies. To learn more about harmonic mixing you might want to check out `the
mixshare archive`_.

.. _the mixshare archive: https://web.archive.org/web/20161123191234/http://www.mixshare.com/wiki/doku.php?id=harmonic_mixing

Mixxx has two features to help you with harmonic mixing. The first is a
:term:`key lock`. When it is active changing the speed of a track won't affect
the key. To enable :term:`key lock`, click the :guilabel:`key lock` button in
the :ref:`interface-button-grid`. The second is that Mixxx can automatically
detect the key of a track and will display it in the library and the decks. The
notation which is used to display a key can be changed in :ref:`Key Detection
Preferences <configuration-key-detection>`.

.. _djing-recording-your-mix:

Recording Your Mix
==================

.. sectionauthor::
   S.Brandt <s.brandt@mixxx.org>

With the integrated recording feature you can record your mix as an audio file
and listen to it later, distribute it as a :term:`Podcast` or burn it to CD.

By default, Mixxx records the Master output. Alternatively, Mixxx can record
the output of an external mixer if you have an audio interface configured for
the :guilabel:`Record/Broadcast` input in :menuselection:`Preferences --> Sound
Hardware`. Refer to :ref:`microphones-record-broadcast-external-mixer` for
details.

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

.. hint:: Recording your mixes and listening to them later to critique
          yourself is a great tool for improving your DJing skills. Sending
          your mixes to other DJs for feedback can also be helpful.

Record your mix to disk
-----------------------

.. versionadded:: 2.1

   Added recording widget to toggle a recording session.

Click on the recording icon on top of the application window to start,
and stop the recording session. The duration of the running recording is
displayed next to the icon.

.. note:: The recording widget might not be available in some skins.

Alternatively:

* Click on the *Recordings* icon in the sidebar to switch to the
  :guilabel:`Recordings` view
* Click the :guilabel:`Start Recording` button or click
  :menuselection:`Options --> Record Mix` in the menu on top of the Mixxx
  application window.
* The display above the track table shows how much data has already been
  recorded, as well as the duration of the recording.
* Perform your mix
* Click the :guilabel:`Stop Recording` button to stop the recording when the mix
  has finished.

.. hint:: You can instantly play your recording as a track in Mixxx. Simply
          drag-and-drop the track to a deck.

.. _djing-auto-dj:

Using Auto DJ For Automatic Mixing
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

.. figure:: ../_static/Mixxx-200-Library-Add-to-Auto-DJ.png
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

.. _djing-auto-dj-crates:

Using Auto DJ crates
--------------------

Instead of inserting the contents of the crates directly into the Auto DJ
playlist, :ref:`Auto DJ crates <library-auto-dj-crates>` are associated
crates that become a source of random track selections.

* **Add a crate to the Auto DJ track sources**:  Expand the :guilabel:`Auto DJ` item
  in the sidebar, and right-click on the :guilabel:`Crates` sub-item. Select
  one of the existing crates from the list. This makes the content of the crate
  available for random selection into the :ref:`Auto DJ <library-auto-dj>`
  queue for automatic mixing. The name of the crate is now listed as sub-item
  below.

  If you do not have any crates available for selection in the list, go
  and create a crate first and add some tracks, see :ref:`library-crates`.

* **Manually add tracks from track sources to Auto DJ**: Click the
  :guilabel:`Auto DJ` item in the sidebar and switch to the Auto DJ view of the
  library. Click the :guilabel:`Add random` button to add one track at the time
  from Auto DJ track sources to the bottom of the Auto DJ playlist.

  .. note:: If you did not set any crates as an Auto DJ track source, clicking the
            :guilabel:`Add Random` button will add a randomly selected track from the
            whole library instead.

* **Automatically add tracks from track sources to Auto DJ**: Mixxx can randomly
  add tracks to the Auto DJ playlist from track sources as soon as a
  specified minimum number of tracks remain. Select
  :menuselection:`Preferences --> Auto DJ --> Enable random track addition to
  queue --> On`. Set :menuselection:`Minimum allowed tracks before addition` to
  change the minimum number of tracks after which random tracks may be added.

  .. note:: If you did not set any crates as an Auto DJ track source, tracks are
            selected from the whole library instead.

* **Remove a crate from the Auto DJ track sources**: Expand the :guilabel:`Auto DJ`
  item in the sidebar, and right-click on one of the crates listed below the
  :guilabel:`Crates` sub-item. Select :guilabel:`Remove Crate as Track
  Source` to remove the crate from the Auto DJ track sources.

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

.. hint:: You can add a track to the end of the Auto DJ playlist once it is
          played instead of removing it. Set :menuselection:`Preferences -->
          Auto DJ --> Re-queue tracks after playback --> On`.
