Roland DJ-505
=============

.. sectionauthor::
   Jan Holthuis <jholthuis@mixxx.org>

.. figure:: ../../_static/controllers/roland_dj_505.svg
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Roland DJ-505 (schematic view)
   :figclass: pretty-figures

   Roland DJ-505 (schematic view)


The Roland DJ-505 is an all-in-one USB MIDI controller with an
integrated audio interface. It has controls for 2 decks that can be
toggled between decks to play with 4 decks. It also features a TR-S step
sequencer with sounds from the TR-808 and the TR-909 drum machines
(TR-606 and TR-707 are available via firmware update).

-  `Manufacturer’s product page <https://www.roland.com/global/products/dj-505/>`__
-  `Serato DJ Hardware Page <https://serato.com/dj/hardware/roland-dj-505>`__
-  `Owner’s Manual <https://www.roland.com/global/support/by_product/dj-505/owners_manuals/>`__
-  `Driver/Firmware/TR-S Samples Download Page <https://www.roland.com/global/products/dj-505/downloads>`__
-  `Mapping Forum Thread <https://mixxx.discourse.group/t/roland-dj-505/17916>`__

Drivers
-------

You can download the latest Windows & MacOS drivers and firmware from
the `manufacturer’s
website <https://www.roland.com/global/products/dj-505/downloads/>`__.
Since the DJ-505 is a USB class compliant MIDI and audio device, the
device is plug-and-play on Linux.

Audio Setup
-----------

The mapping relies on the following channel assignments (for line/phono
input support, applying effects to the TR-S output, etc.):

===================== ================
Output Channels       Assigned to
===================== ================
1-2                   Master
3-4                   Headphones
===================== ================

===================== ================
Input Channels        Assigned to
===================== ================
1-2 (CH 1 Line/Phono) Vinyl Control 1
3-4 (CH 2 Line/Phono) Vinyl Control 2
5-6 (Mix)             Record/Broadcast
7-8 (TR-S output)     Auxiliary 1
===================== ================

The microphone, TR-S drum machine, and external inputs are mixed
together in input channels 5-6, so Mixxx can record and broadcast them.

The knobs for MASTER LEVEL, BOOTH LEVEL, PHONES VOLUME, MIC LEVEL,
TR/SAMPLER LEVEL and CUE/MASTER MIXING are controlling the hardware
mixer of the built-in audio interface. Hence, turning the knobs will not
change values in the Mixxx GUI and you’ll need to set the Mixxx knobs to their
default values when using the controller:

- Set the master/booth/headphones/microphone/aux channel levels to 100% (knob center position)
- Set cue/master mixing to cue-only (leftmost position)

.. note::
   You should assign the Vinyl Control input channels even if you
   do not intend to use timecode vinyl. These channel assignments are also
   needed to make the CH 1/2 PC/LINE/PHONO switches work (i. e. passing
   through line or phono input to the left/right deck).

Controller Mapping
------------------

The control numbering in the schematic drawings matches the those found on the
specified page in the Owner’s Manual.


Browser Section (p. 4)
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/roland_dj_505_browser.svg
   :align: center
   :width: 45%
   :figwidth: 100%
   :alt: Roland DJ-505 (browser section)
   :figclass: pretty-figures

   Roland DJ-505 (browser section)

+--------+------------------+------------------------------------------+
| No.    | Control          | Function                                 |
+========+==================+==========================================+
| 1      | [LOAD] buttons   | Load song into deck.                     |
+--------+------------------+------------------------------------------+
| 1      | [SHIFT] + [LOAD] | Sort library by BPM (press repeatedly to |
|        | button (left)    | toggle ascending/descending order).      |
+--------+------------------+------------------------------------------+
| 1      | [SHIFT] + [LOAD] | Sort library by key (press repeatedly to |
|        | button (right)   | toggle ascending/descending order).      |
+--------+------------------+------------------------------------------+
| 2      | Rotary Selector  | Turn to move tracklist cursor up/down.   |
+--------+------------------+------------------------------------------+
| 2      | [SHIFT] + Rotary | Turn to move sidebar cursor up/down.     |
|        | Selector         | Press to toggle the selected item.       |
+--------+------------------+------------------------------------------+
| 3      | [BACK] button    | *Not yet mapped.*                        |
+--------+------------------+------------------------------------------+
| 3      | [SHIFT] + [BACK] | Sort library by title (press repeatedly  |
|        | button           | to toggle ascending/descending order).   |
+--------+------------------+------------------------------------------+
| 4      | [ADD PREPARE]    | (Un-)Maximizes the library view.         |
|        | button           |                                          |
+--------+------------------+------------------------------------------+
| 4      | [SHIFT] + [ADD   | Sort library by artist (press repeatedly |
|        | PREPARE] button  | to toggle ascending/descending order).   |
+--------+------------------+------------------------------------------+


Deck Section (p. 5-6)
~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/roland_dj_505_deck.svg
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Roland DJ-505 (deck section)
   :figclass: pretty-figures

   Roland DJ-505 (deck section)

+--------+------------------+---------------------------------------------------------------+
| No.    | Control          | Function                                                      |
+========+==================+===============================================================+
| 1      | Jog dial (top    | Perform scratch operation.                                    |
|        | surface)         |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 1      | Jog dial (outer  | Rotate to lower/raise playback speed                          |
|        | edge)            | (and pitch if key lock is off).                               |
+--------+------------------+---------------------------------------------------------------+
| 1      | [SHIFT] + Jog    | Search fast through the playback                              |
|        | dial (top        | location.                                                     |
|        | surface)         |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 2      | [SLIP] button    | Hold to turn on slip mode temporarily or                      |
|        |                  | double press to turn it on permanently.                       |
+--------+------------------+---------------------------------------------------------------+
| 2      | [SHIFT] + [SLIP] | Toggle vinyl control mode.                                    |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 3      | [SHIFT] button   | Hold down to access other functions.                          |
+--------+------------------+---------------------------------------------------------------+
| 4      | [SYNC] button    | Match tempo and phase of other deck.                          |
|        |                  | Long press to enable Master Sync.                             |
+--------+------------------+---------------------------------------------------------------+
| 4      | [SHIFT] + [SYNC] | Cancels Sync mode.                                            |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 5      | [CUE] button     | Specifies, plays or recalls temporary                         |
|        |                  | cue point.                                                    |
+--------+------------------+---------------------------------------------------------------+
| 5      | [SHIFT] + [CUE]  | Returns to the beginning of the song.                         |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 6      | [PLAY/PAUSE]     | Plays or pause the song.                                      |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 6      | [SHIFT] +        | Hold to play backwards.                                       |
|        | [PLAY/PAUSE]     |                                                               |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 7      | Pad Mode Select  | See :ref:`Performance Pads <roland-dj-505-performancepads>`.  |
+--------+------------------+---------------------------------------------------------------+
| 8      | Performance Pads | See :ref:`Performance Pads <roland-dj-505-performancepads>`.  |
+--------+------------------+---------------------------------------------------------------+
| 9      | PARAMETER area   | See :ref:`Performance Pads <roland-dj-505-performancepads>`.  |
+--------+------------------+---------------------------------------------------------------+
| 10     | LOOP area: [AUTO | Turns auto loop on/off.                                       |
|        | LOOP] button     |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 10     | LOOP area:       | Set the loop playback length to                               |
|        | [1/2X], [2X]     | half/double.                                                  |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 10     | LOOP area:       | Move the loop by it’s length toward the                       |
|        | [SHIFT] + [1/2X] | left.                                                         |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 10     | LOOP area:       | Move the loop by it’s length toward the                       |
|        | [SHIFT] + [2X]   | right.                                                        |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 10     | LOOP area: [IN], | Specify loop-in/loop-out points.                              |
|        | [OUT] button     |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 10     | LOOP area:       | Toggle beats quantization.                                    |
|        | [SHIFT] + [IN]   |                                                               |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 10     | LOOP area:       | Cancels loop playback, go to loop-in                          |
|        | [SHIFT] + [OUT]  | point and resume playback.                                    |
|        | button           |                                                               |
+--------+------------------+---------------------------------------------------------------+
| 11     | [DECK 3], [DECK  | Switches the deck (left: decks 1 and 3,                       |
|        | 4] buttons       | right: decks 2 and 4)                                         |
+--------+------------------+---------------------------------------------------------------+
| 12     | [KEY LOCK]       | Toggle key lock.                                              |
+--------+------------------+---------------------------------------------------------------+
| 12     | [SHIFT] + [KEY   | Cycles through tempo slider range (8%,                        |
|        | LOCK]            | 16%, 50%).                                                    |
+--------+------------------+---------------------------------------------------------------+
| 13     | Tempo slider     | Adjust song playback speed (and pitch if                      |
|        |                  | key lock if off).                                             |
+--------+------------------+---------------------------------------------------------------+


Mixer Section (p. 7)
~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/roland_dj_505_mixer.svg
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Roland DJ-505 (mixer section)
   :figclass: pretty-figures

   Roland DJ-505 (mixer section)

+--------+------------------+------------------------------------------+
| No.    | Control          | Function                                 |
+========+==================+==========================================+
| 1      | [TRIM] knobs     | Adjust the deck gain (prefader)          |
+--------+------------------+------------------------------------------+
| 2      | [HI], [MID],     | Adjust the high/mid/low-frequency        |
|        | [LOW] knobs      | regions of the song.                     |
+--------+------------------+------------------------------------------+
| 3      | [FILTER] knobs   | QuickEffect superknob (filter by         |
|        |                  | default, can be changed to a different   |
|        |                  | effect in Mixxx preferences)             |
+--------+------------------+------------------------------------------+
| 4      | Channel [CUE]    | Toggle PFL for each channel.             |
|        | buttons          |                                          |
+--------+------------------+------------------------------------------+
| 4      | [SHIFT] + [CUE]  | Adjust beatgrid so that the closest beat |
|        | buttons (short   | is set to the current cursor position.   |
|        | press)           |                                          |
+--------+------------------+------------------------------------------+
| 4      | [SHIFT] + [CUE]  | Adjust beatgrid to match another playing |
|        | buttons (long    | deck.                                    |
|        | press)           |                                          |
+--------+------------------+------------------------------------------+
| 4      | [SHIFT] + [CUE]  | Set tempo by tapping on each beat.       |
|        | buttons (tap     |                                          |
|        | repeatedly)      |                                          |
+--------+------------------+------------------------------------------+
| 5      | Channel faders   | Adjust the output level for each         |
|        |                  | channel.                                 |
+--------+------------------+------------------------------------------+
| 6      | Cross fader      | Fades between left and right deck.       |
+--------+------------------+------------------------------------------+
| 7      | [MASTER LEVEL]   | Adjusts the master output level.         |
|        | knob             |                                          |
+--------+------------------+------------------------------------------+
| 8      | [BOOTH LEVEL]    | Adjusts the output level of the BOOTH    |
|        | knob             | OUT jacks.                               |
+--------+------------------+------------------------------------------+
| 9      | [MIXING] knob    | Fades between PFL and master output in   |
|        |                  | headphones                               |
+--------+------------------+------------------------------------------+
| 10     | [TR/SAMPLER      | Adjusts output of the TR-S (Aux 3) and   |
|        | LEVEL] knob      | Samplers 1-16.                           |
+--------+------------------+------------------------------------------+
| 11     | TR/SAMPLER [CUE] | Toggle PFL of the TR-S (Aux 3) and       |
|        | button           | Samplers 1-16.                           |
+--------+------------------+------------------------------------------+
| 12     | Level indicator  | Indicate the output level of each        |
|        |                  | channel and master.                      |
+--------+------------------+------------------------------------------+


Effects Section (p. 7)
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/roland_dj_505_effects.svg
   :align: center
   :width: 60%
   :figwidth: 100%
   :alt: Roland DJ-505 (effects section)
   :figclass: pretty-figures

   Roland DJ-505 (effects section)

+--------+------------------+----------------------------------------------------------------------------------------------------+
| No.    | Control          | Function                                                                                           |
+========+==================+====================================================================================================+
| 1      | CH ASSIGN area   | Toggle FX 1/2 for decks 1/2 (3/4 if                                                                |
|        |                  | [SHIFT] is pressed) or the TR-S (Aux 3)                                                            |
|        |                  | and Samplers 1-16.                                                                                 |
+--------+------------------+----------------------------------------------------------------------------------------------------+
| 2-5    | *Various*        | See `Standard Effects Mapping <https://github.com/mixxxdj/mixxx/wiki/Standard-Effects-Mapping>`__. |
+--------+------------------+----------------------------------------------------------------------------------------------------+


TR-S Section (p. 8)
~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/roland_dj_505_trs.svg
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Roland DJ-505 (TR-S section)
   :figclass: pretty-figures

   Roland DJ-505 (TR-S section)

+--------+------------------+------------------------------------------+
| No.    | Control          | Function                                 |
+========+==================+==========================================+
| 1      | [VALUE] knob     | *See Owner’s Manual.*                    |
+--------+------------------+------------------------------------------+
| 2      | [SHIFT] button   | Hold down to access other functions.     |
+--------+------------------+------------------------------------------+
| 3      | Display          | *See Owner’s Manual.*                    |
+--------+------------------+------------------------------------------+
| 4      | [SYNC] button    | Match tempo of playing deck (phase       |
|        |                  | matching is not implemented yet, use the |
|        |                  | NUDGE button instead).                   |
+--------+------------------+------------------------------------------+
| 4      | [SHIFT] + [SYNC] | *Currently not mapped.*                  |
|        | button           |                                          |
+--------+------------------+------------------------------------------+
| 5-17   | *Various*        | *See Owner’s Manual.*                    |
+--------+------------------+------------------------------------------+

Front Panel (p. 8)
~~~~~~~~~~~~~~~~~~

+--------+------------------+------------------------------------------+
| No.    | Control          | Function                                 |
+========+==================+==========================================+
| 1      | [PHONES] jacks   | Connect headphones here.                 |
+--------+------------------+------------------------------------------+
| 2      | [VOLUME] knob    | Adjust the volume of the headphones.     |
+--------+------------------+------------------------------------------+
| 3      | [CROSS FADER]    | Switch the cross fader response curve.   |
|        | switch           |                                          |
+--------+------------------+------------------------------------------+
| 4      | [REVERSE] switch | Switch cross fader reverse (hamster)     |
|        |                  | mode on/off.                             |
+--------+------------------+------------------------------------------+
| 5      | [CH1], [CH 2]    | Selects Mixxx deck as input source       |
|        | switches: [PC]   | (Unmute the Mixxx deck and mute Aux      |
|        |                  | 1/2).                                    |
+--------+------------------+------------------------------------------+
| 5      | [CH1], [CH 2]    | Selects Line/Phono input source (Mute    |
|        | switches:        | the Mixxx deck and unmute Aux 1/2).      |
|        | [LINE/PHONO]     |                                          |
+--------+------------------+------------------------------------------+
| 6      | [MIC LEVEL] knob | Adjust the microphone volume.            |
+--------+------------------+------------------------------------------+

.. _roland-dj-505-performancepads:

Performance Pads
~~~~~~~~~~~~~~~~

You can use the Pad Mode Select buttons to select a mode for the
performance pads.

======================================== ===================== ==========
Control                                  Mode                  LED Color
======================================== ===================== ==========
[HOT CUE] button                         Hot Cue Mode          White
[SHIFT] + [HOT CUE] button               Cue Loop Mode         Blue
[SHIFT] + [HOT CUE] button (press twice) Prepare Mode          Red
[ROLL] button                            Roll Mode             Light blue
[ROLL] button (press twice)              Loop Mode             Green
[TR] button                              TR Mode               Red
[SHIFT] + [TR] button                    Pattern Mode          Green
[TR] button (press twice)                TR Velocity Mode      Orange
[SAMPLER] button                         Sampler Mode          Magenta
[SHIFT] + [SAMPLER] button               Velocity Sampler Mode Purple
[SAMPLER] button (press twice)           Pitch Play Mode       Green
======================================== ===================== ==========

Most pad modes are similar to those found when used with Serato. A
notable exception is the Loop Mode, which replaces the Serato’s Saved
Loop Mode. In this mapping, the Loop Mode is similar to the Roll mode,
but sets a non-rolling beatloop instead.

Modes that are described in the owner’s manual (Slicer, Slicer
Loop, Saved Loop, Flip) but not listed below are currently not mapped.

Hot Cue Mode
^^^^^^^^^^^^

.. figure:: ../../_static/controllers/roland_dj_505_performancepads.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Roland DJ-505 (performance pads)
   :figclass: pretty-figures

   Roland DJ-505 (performance pads)

Bookmark positions in the track and jump to them.

+------+---------------------------------+------------------------------------------+
| No.  | Control                         | Function                                 |
+======+=================================+==========================================+
| 1-8  | Pad (unlit)                     | Save current position as hot cue.        |
+------+---------------------------------+------------------------------------------+
| 1-8  | Pad (lit)                       | Jump to hot cue. If the track is         |
|      |                                 | stopped, holding the pad will preview    |
|      |                                 | the hot cue until the pad is released.   |
+------+---------------------------------+------------------------------------------+
| 1-8  | [SHIFT] + Pad (lit)             | Clear hot cue.                           |
+------+---------------------------------+------------------------------------------+
| 9    | PARAMETER - button              | Change color of last used hotcue to the  |
|      |                                 | previous color in the palette.           |
+------+---------------------------------+------------------------------------------+
| 10   | PARAMETER + button              | Change color of last used hotcue to the  |
|      |                                 | next color in the palette.               |
+------+---------------------------------+------------------------------------------+
| 9    | [SHIFT] + PARAMETER - button    | Move beatgrid left.                      |
+------+---------------------------------+------------------------------------------+
| 10   | [SHIFT] + PARAMETER + button    | Move beatgrid right.                     |
+------+---------------------------------+------------------------------------------+

Cue Loop Mode
^^^^^^^^^^^^^

.. figure:: ../../_static/controllers/roland_dj_505_performancepads.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Roland DJ-505 (performance pads)
   :figclass: pretty-figures

   Roland DJ-505 (performance pads)

Set beatloop from a hot cue point.

+------+---------------------------------+------------------------------------------+
| No.  | Control                         | Function                                 |
+======+=================================+==========================================+
| 1-8  | Pad (lit)                       | Set a beatloop at the position of the    |
|      |                                 | hotcue and jump to it.                   |
+------+---------------------------------+------------------------------------------+
| 1-8  | Pad (unlit)                     | Save the current position as hot cue and |
|      |                                 | set a beatloop.                          |
+------+---------------------------------+------------------------------------------+
| 9    | PARAMETER - button              | Halve the size of the current loop.      |
+------+---------------------------------+------------------------------------------+
| 9    | PARAMETER + button              | Double the size of the current loop.     |
+------+---------------------------------+------------------------------------------+
| 9-10 | [SHIFT] + PARAMETER -/+ buttons | *Currently not mapped*.                  |
+------+---------------------------------+------------------------------------------+

Prepare Mode
^^^^^^^^^^^^

.. figure:: ../../_static/controllers/roland_dj_505_performancepads.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Roland DJ-505 (performance pads)
   :figclass: pretty-figures

   Roland DJ-505 (performance pads)

This mode allow you to prepare tracks by setting intro/outro cues.

+------+---------------------------------+------------------------------------------+
| No.  | Control                         | Function                                 |
+======+=================================+==========================================+
| 1    | Pad (unlit)                     | Set current position as intro start.     |
+------+---------------------------------+------------------------------------------+
| 1    | Pad (lit)                       | Jump to intro start position.            |
+------+---------------------------------+------------------------------------------+
| 2    | Pad (unlit)                     | Set current position as intro end.       |
+------+---------------------------------+------------------------------------------+
| 2    | Pad (lit)                       | Jump to intro end position.              |
+------+---------------------------------+------------------------------------------+
| 3    | Pad (unlit)                     | Set current position as outro start.     |
+------+---------------------------------+------------------------------------------+
| 3    | Pad (lit)                       | Jump to outro start position.            |
+------+---------------------------------+------------------------------------------+
| 4    | Pad (unlit)                     | Set current position as outro end.       |
+------+---------------------------------+------------------------------------------+
| 4    | Pad (lit)                       | Jump to outro end position.              |
+------+---------------------------------+------------------------------------------+
| 5-8  | Pad                             | *Currently not mapped*.                  |
+------+---------------------------------+------------------------------------------+
| 9-10 | [SHIFT] + PARAMETER -/+ buttons | *Currently not mapped*.                  |
+------+---------------------------------+------------------------------------------+

.. note:: This mode has been added by the Mixxx developers and is not available in
          Serato.

Roll Mode
^^^^^^^^^

.. figure:: ../../_static/controllers/roland_dj_505_performancepads.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Roland DJ-505 (performance pads)
   :figclass: pretty-figures

   Roland DJ-505 (performance pads)

The Roll Mode provides quick access to rolling loops and beatjumps.

+------+---------------------------------+------------------------------------------+
| No.  | Control                         | Function                                 |
+======+=================================+==========================================+
| 1-4  | Pad (hold)                      | Play a rolling loop with the beatlength  |
|      |                                 | that is assigned to the pad.             |
+------+---------------------------------+------------------------------------------+
| 5    | Pad (press)                     | Beatjump left.                           |
+------+---------------------------------+------------------------------------------+
| 6    | Pad (press)                     | Decrease beatjump size.                  |
+------+---------------------------------+------------------------------------------+
| 7    | Pad (press)                     | Increase beatjump size.                  |
+------+---------------------------------+------------------------------------------+
| 8    | Pad (press)                     | Beatjump right.                          |
+------+---------------------------------+------------------------------------------+
| 9    | PARAMETER - button              | Halve the size of the current loop.      |
+------+---------------------------------+------------------------------------------+
| 9    | PARAMETER + button              | Double the size of the current loop.     |
+------+---------------------------------+------------------------------------------+
| 9-10 | [SHIFT] + PARAMETER -/+ buttons | *Currently not mapped*.                  |
+------+---------------------------------+------------------------------------------+

TR/Pattern/TR Velocity Modes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These modes are hardcoded in the device firmware, so they work exactly as
described in the Owner’s Manual.


Sampler/Velocity Sampler Play Modes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/controllers/roland_dj_505_performancepads.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Roland DJ-505 (performance pads)
   :figclass: pretty-figures

   Roland DJ-505 (performance pads)

The sampler modes allow you to load, play and stop samples in the first 8 sample slots.

+------+---------------------------------+------------------------------------------+
| No.  | Control                         | Function                                 |
+======+=================================+==========================================+
| 1-8  | Pad (unlit)                     | Load currently selected track into the   |
|      |                                 | sample slot associated with the pad.     |
+------+---------------------------------+------------------------------------------+
| 1-8  | [SHIFT} + Pad (lit)             | If the sample is playing, stop the       |
|      |                                 | playback. If the sample is not playing,  |
|      |                                 | eject the sample from the sample slot.   |
+------+---------------------------------+------------------------------------------+
| 1-8  | Pad (lit)                       | Play the sample in the sample slot       |
|      |                                 | associated with the pad.                 |
|      |                                 | *Velocity Sampler Mode*: The playback    |
|      |                                 | volume of the sample depends on the      |
|      |                                 | pressure (velocity).                     |
+------+---------------------------------+------------------------------------------+
| 9-10 | PARAMETER -/+ buttons           | *Currently not mapped*.                  |
+------+---------------------------------+------------------------------------------+


Pitch Play Mode
^^^^^^^^^^^^^^^

.. figure:: ../../_static/controllers/roland_dj_505_performancepads.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Roland DJ-505 (performance pads)
   :figclass: pretty-figures

   Roland DJ-505 (performance pads)

Play the track from a hot cue position and change the pitch in semitone steps.
Pads right of the white lit pad raise the pitch, pads left of it lower it.

+------+---------------------------------+------------------------------------------+
| No.  | Control                         | Function                                 |
+======+=================================+==========================================+
| 1-8  | Pad                             | Play currently selected hotcue with      |
|      |                                 | modified pitch.                          |
+------+---------------------------------+------------------------------------------+
| 1-8  | [SHIFT] + Pad (dimly lit)       | Select hot cue for pitch play. The pad   |
|      |                                 | of the currently selected hotcue pad is  |
|      |                                 | lit.                                     |
+------+---------------------------------+------------------------------------------+
| 9-10 | PARAMETER -/+ buttons           | Cycles through semitone ranges (Up, Mid, |
|      |                                 | Down).                                   |
+------+---------------------------------+------------------------------------------+

Known Issues
~~~~~~~~~~~~

-  TR-S Syncing currently works at the BPM level, but phase syncing is
   not implemented yet. As a workaround, the NUDGE button can be used to
   adjust the phase. This depends on MIDI clock I/O (`Launchpad Bug
   #682221 <https://bugs.launchpad.net/mixxx/+bug/682221>`__).
-  Some performance pad modes are missing (Slicer [ `Launchpad Bug
   #1828886 <https://bugs.launchpad.net/mixxx/+bug/1828886>`__ ], Slicer
   Loop, Saved Loop [ `Launchpad Bug
   #1367159 <https://bugs.launchpad.net/mixxx/+bug/1367159>`__, `PR
   #2194 <https://github.com/mixxxdj/mixxx/pull/2194>`__ ], Flip [
   `Launchpad Bug
   #1768113 <https://bugs.launchpad.net/mixxx/+bug/1768113>`__ ])
-  Some buttons are not mapped yet (e.g. BACK)
-  LEDs on BACK/ADD PREPARE do not work (this seems to be a
   hardware/firmware bug and does not work in Serato either)
-  Controller does not send current cross fader value on Serato Sysex
   Message (this seems to be a hardware/firmware bug and does not work
   in Serato either)
