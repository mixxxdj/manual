Vestax VCI-300
==============

The VCI-300 is a dedicated USB MIDI controller. It also comes with a built in audio interface with standard 4-in/4-out and headphone connection, which means all you need for DJing is the VCI-300, a
laptop and a set of headphones.

This controller has been discontinued as Vestax went out of business in 2014.

-  `Forum thread <https://mixxx.discourse.group/t/vestax-vci-300mk-ii/11496>`__

.. versionadded:: 1.11


Differences between VCI-300 and VCI-300 MKII
--------------------------------------------

In 2010 Vestax made changes to the original VCI-300 that improved the controller. There were *no* changes in the MIDI mapping.

Volume Boost (Gain Boost)*\*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Higher output gain level and headphone volume level when supplying power with the optional power adaptor.
-  *Important Note:* Optional power supply DC-7 must be used in order to get the boost on the headphones and Master output. Without the power supply the MKII will perform just like the original
   VCI-300. Also, using the DC-7 on the original VCI-300 will do nothing.

Optional Vestax Digital Fader (not included)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The VCI-300MKII Cross fader can be upgraded to Vestax’s new magnetic sensor system digital fader CF-X2.

New Direct Audio Thru
~~~~~~~~~~~~~~~~~~~~~

Audio fed to the MIC/AUX input can now be directly sent to the Master outputs with the THRU switch turned ON, minimizing latency of when fed through ITCH.

New adjust knobs for the JOG sensor control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New JOG sensor adjust knobs for speedy and accurate adjustments.the VCI-300MKII’s JOG wheels have excellent tracking ability,and flexibility for various play styles.You can control songs with analog
precision.

New Mini Head-Phone Jack
~~~~~~~~~~~~~~~~~~~~~~~~

The MKII features a 1/8 inch headphone connection along with standard 1/4 inch connection.

Mapping description
-------------------

.. figure:: ../../_static/controllers/vestax_vci_300.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Vestax VCI-300 (schematic view)
   :figclass: pretty-figures

   Vestax VCI-300 (schematic view)
   Image (c) Vestax


Mixxx supports the VCI-300 out of the box. The mapping for Mixxx closely resemble the original to make the transition easy.

===== ===================== =================================================================================================================================================================
#     KEY                   FUNCTION
01    Pitch Slider          Adjusts playback speed.
02    Auto Tempo            Toggle quantize (1.11.0: Trigger beatsync)
\     Shift + Auto Tempo    Trigger beatsync (1.11.0: Toggle quantize)
\     Scroll + Auto Tempo   Tap BPM. When taped repeatedly, adjust the tracks BPM to the tapped BPM.
03    Keylock               Trigger beatsync
\     Shift + Keylock       Reset pitch to 0.00% (quartz)
04    Pitch Shift           Pitch bend
\     Shift + Pitch Shift   Fine tune playback speed +/-0.01
05    Cue [1-3]/In          Set/Activate Hotcue
\     Shift + Cue [1-3]/In  Delete Hotcue
06    Scratch               Toggle scratching on jogwheel
07    Out 1/Loop            Set manual loop in point
\     Shift + Out 1/Loop    Clear loop point
\     Out 2/Loop            Set manual loop out point
\     Shift + Out 2/Loop    Clear loop point
\     Out 3/Loop            Enable/disable loop
08    Shift                 Holding shift engages shift functions of many of the buttons, secondary functions are printed inside a grey box.
09    Trim                  This controls the volume of the track before it goes to the EQ and fader.
10    Censor                Temporary play backwards while pressed, resumes from where the playhead would have been if the button was not pressed
\     Shift + Censor        1.11: Toggle reverse playback. Pressing Censor again during reverse playback, will return to normal playback.
\                           1.12 (work in progress): Enable/disable effect unit with preselected *Filter* effect. The filter parameter is controlled with the Mid EQ knob next to the button.
11    Auto Loop             Enable beatloop of the current beatloop value (default: 4 beats) for tracks that have BPM calculated
\     Shift + Auto Loop     Enter/Exit beatloop roll
\     Scroll + Auto Loop    Reset number of beats to 4 if beatloop not active
12    Equalizers            Adjust the gain of the high/mid/low EQ filter.
13    Half                  Halve loop length
\     Shift + Half          Jump to start of track (while paused)
\     Scroll + Half         Seek backward (while paused)
\     Double                Double loop length
\     Shift + Double        Jump to end of track (while paused)
\     Scroll + Double       Seek forward (while paused)
14    Master Level          This knob controls the overall output of the VCI-300, ensure this is right down before running the software.
15    Monitor Select        Controls the balance in the headphones between the mix output and the PFL headphone cue
16    Monitor Volume        Controls the volume of the headphones.
17    Cue                   If a cue point is set, jumps to the cue point when pressed.
\     Shift + Cue           Set the cue point (while playing), clear the cue point (while paused), jump to beginning of track (if no cue point is set)
18    Play                  Start/Pause playback
\     Shift + Play          Stutter Play
19    Crossfader            Fades between the left and right channels.
20    Input faders          Control the volume of their respective tracks.
21/23 PFL A/B               Sends the left/right deck to the headphone mix.
\     Shift + PFL A/B       Load selected track into the deck (while paused) and switch PFL to this deck
22    Scroll + Jogwheel     Scroll playlist (while paused)
24    Cursor Up/Down        Scrolls to the next/previous track in the track table.
\     Cursor Left/Right     Switches to the next view (Library, Queue, etc.)
\     Tab                   Toggles (expands/collapses) the currently selected sidebar item.
25    Jog (platter touched) Track search (while paused when scratching is disabled)
\                           Pitch bend / nudge (while playing when scratching is disabled)
\                           Scratch (when scratching is enabled)
\     Jog (outer rim)       Pitch bend / nudge
\     Shift + Jog           Fast track search (while paused)
\     Scroll + Jog          Scroll playlist (while paused)
===== ===================== =================================================================================================================================================================
