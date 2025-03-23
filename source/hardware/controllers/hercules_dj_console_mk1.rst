Hercules DJ Console MK1
=======================

`Manufacturer's product page <https://support.hercules.com/en/product/djconsole-en/>`_ ·
`Forum thread <https://mixxx.discourse.group/t/hercules-dj-console-mk1-hid-mapping-v0-1/12766>`_

.. versionadded:: 1.11

The Hercules DJ Console (retroactively called the Mark 1) is a USB-HID 2-deck
controller with a built in sound card.

Audio
-----

===================== ================
Output Channels       Assigned to
===================== ================
1-2 (front)           Headphones
3-4 (center/LFE)      Main
5-6 (rear)            Booth
===================== ================

The DJ Console's soundcard is a class compliant audio device and works out of
the box on Linux.

On the rear are RCA jacks labeled 1–6, as well as 3.5mm stereo plugs labeled 1-2
(Front), 3-4 (Center/LFE), and 5-6 (rear).
These correspond to the same channels in the digital interface.
The device has a 1/4" TRS headphone output on the front.
Unlike most audio devices, the headphones are mapped to channels 1-2 as well,
but have their own independent volume knob that is managed by the hardware and
is not mappable.

The device also has MIDI input and output ports and exposes a MIDI device over
the USB interface so that it can be used as a MIDI receiver and optical audio
inputs and outputs.
There are also mono RCA "in" and "out" jacks on the rear.
Finally, the front also has RCA line inputs and a 1/4" TRS microphone input
which also has its own hardware managed gain knob.

Main Controls
-------------

.. csv-table::
   :header: "Control", "Name", "Function"
   :widths: 5 25 70

   "Play/Pause", ":hwlabel:`⏵`", "Play/pause playback"
   "Cue", ":hwlabel:`Cue`", "If track is playing: stops the track and resets position to the main cue point

   If playback is stopped: sets the main cue point"
   "Cue", ":hwlabel:`Cue` (hold)", "Play the track from main cue point, release to stop playback and return to the main cue point. Playback must be initially stopped on the main cue point."
   "Left", ":hwlabel:`◀` (left deck)", "Navigate up in library"
   "Right", ":hwlabel:`▶` (left deck)", "Navigate down in library"
   "Left", ":hwlabel:`◀` (right deck)", "Load selected track to deck 1"
   "Right", ":hwlabel:`▶` (right deck)", "Load selected track to deck 2"
   "Jog Wheels", "—", "Scratch when paused, fine seek when playing."


.. hint::
   The actual behavior of CUE and Play/Pause buttons depends on Mixxx settings. See :ref:`interface-cue-modes` for more info.

Settings
--------

In the original version of this mapping included in Mixxx 1.11 up through 2.5.0
the knob labeled "Volume" was used to set the tempo and the buttons labeled
"Pitch Bend" were mapped to the same functionality as the jog wheels.
This has been changed in newer versions, and settings have been introduced for
backwards compatibility to allow reverting to the old functionality.
