Denon MC7000
============

The Denon MC7000 is a professional DJ controller which has got 4-channel capability and dual USB connections. These two USB audio interfaces enable two DJs to play together. This controller includes Denon’s high build quality and superior 24-bit audio reproduction, makes this suited to both mobile and club DJs.

The dual 6" platters have a touch-capacitive design with rotational LED displays. The MC7000 has exclusive and dedicated Key Matching and Changing controls that deliver an unprecedented ability to instantly and harmonically match musical keys. The unit’s comprehensive, multi-input mixer also provides access to line/phono inputs from both authentic analogue (vinyl) and digital sources.

-  4-channel DJ controller with digital mixer
-  Dual USB audio interfaces - connect 2 computers at once
-  16 velocity-sensitive performance pads
-  New dedicated key-matching and changing controls
-  Solid 6-inch touch-capacitive platters with tracking LED
-  2 mic inputs with dedicated controls
-  XLR Booth and Master connections


-  `Denon MC7000 Mapping thread <https://mixxx.discourse.group/t/denon-mc7000-mapping/18235>`__
-  `Manufacturer’s product page <https://www.denondj.com/professional-dj-controller-for-serato-mc7000xus>`__
-  `User Guide <http://cdn.inmusicbrands.com/denondj/MC7000/MC7000-UserGuide-v1.1.pdf>`__
-  `Hardware Setting Specification <http://cdn.inmusicbrands.com/denondj/MC7000/MC7000-Hardware-Settings-Mode-Specification-v1_4.pdf>`__

.. versionadded:: 2.2.4

Compatibility
~~~~~~~~~~~~~

-  **Mac** users should be just fine connecting the MC7000 and go.
-  **Windows** users need to install the latest Windows Driver from `Denon Download Site <https://www.denondj.com/downloads>`__.
-  **Linux** users need to know that the MC7000 internal audio interface
   is not available out-of-the-box for older Linux Kernels. You have to
   upgrade your **Kernel** to minimum versions LTS: **4.19.105** or
   **5.4.21**. All kernel versions **5.6.x** and following are supporting the device.
   All recent Linux distributions are shipped with Audio support for the MC7000, like

  - Ubuntu 20.04 and 20.10
  - Ubuntu based like Linux Mint and KDE Neon
  - Manjaro Linux 19.x & 20.x
  - OpenSUSE Tumbleweed
  - Gentoo stable

Mapping
~~~~~~~

.. figure:: ../../_static/controllers/denon_mc7000_layout.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Denon MC7000 (schematic view)
   :figclass: pretty-figures

   Denon MC7000 (schematic view)


This controller is made for Serato DJ and most of the mapping is made
for Mixxx accordingly. Anyhow, there are several differences for
functions not matching the Serato mapping. If you have any wishes to
improve the mapping, then please discuss it in the `Denon MC7000
Mapping <https://mixxx.discourse.group/t/denon-mc7000-mapping/18235>`__
thread.

User Variables
~~~~~~~~~~~~~~

Please check the :file:`Denon-MC7000-scripts.js` mapping file for user variables to:

-  activate NeedleDrop sensor while a track is playing (default: false)
-  set the Pitch Fader ranges in % to toggle between them
   (default: 4, 6, 8, 10, 16, 24)
-  Platter Ring LED mode: single LED on or off (default: 1). Can be
   switched with SHIFT + Deck button
-  Vinyl Mode on or off at Mixxx start which also triggers the Platter
   Ring LED function (default: 1)
-  Scratch Parameters (default: 33.3, 1/10, 1/10/32)
-  Jog Parameters (default: 1, 3)


Mixer Section
~~~~~~~~~~~~~

========  ===============================================================  ===============================================================
No.       Control                                                          Function
========  ===============================================================  ===============================================================
1.        Input Selector Switch                                            Set to the desired audio source from this channel. :hwlabel:`LINE/PHONO` will disable the corresponding Deck (switches off all LEDs and the controller will not send MIDI signals to control Mixxx). This allows the mixer to use an external source.  :hwlabel:`USB` will turn the corresponding Deck on and allows to control Mixxx via USB connection.
2.        :hwlabel:`USB1 / USB2` button                                    Press to select whether the deck is controlling the computer connected to USB Port 1 or USB Port 2. If only one USB Port is connected the controller activates this automatically.
3.        :hwlabel:`LEVEL` knob                                            Turn to adjust the level of the pre-fader, pre-EQ audio signal for the channel.
4.        Channel Level Meters                                             Display the audio signal level of the channel as in Mixxx GUI.
5.        Channel EQ knobs                                                 Turn to boost or cut the :hwlabel:`HI`, :hwlabel:`MID` and :hwlabel:`LOW` frequencies for the channel.
6.        :hwlabel:`FILTER`                                                Turn this knob to adjust the filter applied to the channel. Turn the knob counterclockwise to apply a low-pass filter. Turn the knob clockwise to apply a high-pass Filter.
7.        :hwlabel:`CUE` button                                            Press to send the channel’s pre-fader signal to the headphones’ cue channel.
8.        Channel fader                                                    Use to adjust the channel’s volume level.
9.        Crossfader Assign                                                Routes the audio playing on the corresponding channel to either side of the crossfader (:hwlabel:`A` or :hwlabel:`B`), or bypasses the crossfader and sends the audio directly to the program mix (:hwlabel:`THRU`).
10.       Crossfader                                                       Use this crossfader to mix between the left and right decks.
12.       :hwlabel:`SAMPLER LEVEL`                                         Turn this knob to adjust the volume level of the software’s sampler. If the volume is set to 0 then the Sampler banks are hidden, otherwise shown.
13.       Master Level Meters                                              These LEDs show the Master Audio signal.
14.       :hwlabel:`MASTER LEVEL` knob                                     Turn to adjust the volume level of the master outputs.
15.       :hwlabel:`BOOTH LEVEL` knob                                      Turn to adjust the volume level of the booth outputs.
20.       :hwlabel:`PHONES LEVEL` knob                                     Turn to adjust the volume level of the headphones.
21.       :hwlabel:`PHONES MIX` knob                                       Adjusts the software’s audio output to the headphones, mixing between the cue output and the master mix output.
22.       :hwlabel:`SPLIT` switch                                          When this switch is in the :hwlabel:`ON` position, the headphone audio will be “split” such that all channels sent to cue channel are summed to mono and sent to the left headphone channel and the master mix is summed to mono and sent to the right channel. When the switch is in the Off position, the cue channel and master mix will be “blended” together.
          :hwlabel:`X FADER CONTOUR`                                       Turn to ajust the slope of the crossfader curve, to the left for a smooth fade (mixing) or to the right for a sharp cut (scratching.
========  ===============================================================  ===============================================================

.. note::
   Input source selection, the :hwlabel:`LEVEL` meter, the :hwlabel:`MASTER LEVEL`/:hwlabel:`BOOTH LEVEL`/:hwlabel:`PHONES LEVEL`/:hwlabel:`PHONES MIX` knobs and the :hwlabel:`SPLIT` button are handled by the controller.
   The status of Mixxx will not be changed.


Microphone Sections
~~~~~~~~~~~~~~~~~~~

========  =================================================================  ===============================================================
No.       Control                                                            Function
========  =================================================================  ===============================================================
16.       :hwlabel:`MIC ON/OFF` button                                       Press to activate/deactivate the microphones.
17.       :hwlabel:`MIC LEVEL` knobs                                         Turn to adjust the volume levels of the corresponding microphone inputs.
18.       :hwlabel:`MIC 1 HI`/:hwlabel:`MIC 1 LOW` knobs (left deck)         Turn to boost or cut the high or low frequencies for Microphone 1.
18.       :hwlabel:`MIC 2 TONE` knob (right deck)                            Turn to adjust the tone (high-low) for Microphone 2.
18.       :hwlabel:`ECHO MIC 1&2` knob (right deck)                          Turn to adjust the amount of the echo effect for both Microphones.
19.       :hwlabel:`TALKOVER MIC 1&2` button (left deck)                     Press to use the “talkover” feature, which automatically reduces the volume level of the master mix when you speak into the microphones.
19.       :hwlabel:`SHIFT` + :hwlabel:`TALKOVER MIC 1&2` button (left deck)  Press to activate/deactivate the “post” feature. When on, the microphones signal will be sent to the Booth Outputs. When off, the microphones signal will not be routed to the Booth Outputs.
19.       :hwlabel:`ECHO MIC 1&2` button (right deck)                        Press this button to activate or deactivate the echo effect on the microphones’ audio signal.
========  =================================================================  ===============================================================

.. note::
   The :hwlabel:`MIC LEVEL`, :hwlabel:`ECHO MIC 1&2` and :hwlabel:`TALKOVER MIC 1&2` knobs and the :hwlabel:`MIC ON/OFF` button are handled by the controller.
   The status of Mixxx will not be changed.


Deck Sections
~~~~~~~~~~~~~

========  ===============================================================  ===============================================================
No.       Control                                                          Function
========  ===============================================================  ===============================================================
23.       :hwlabel:`DECK` button                                           Selects which deck in the software is controlled by that hardware deck. The left deck can control Deck 1 or 3; the right deck can control Deck 1 or 4.
23.       :hwlabel:`SHIFT` + :hwlabel:`DECK` button                        Press to switch Platter Ring LED Mode. See Chapter "LEDs" below for details.
24.       :hwlabel:`SHIFT` button                                          Press and hold this button to access secondary functions of other controls.
25.       :hwlabel:`SYNC` button                                           Press to automatically match the corresponding deck’s :term:`tempo` with the tempo and phase of the opposite deck. Press again to deactivate Sync. Hold this button down for one sec to permanently match the tempo.
26.       :hwlabel:`CUE` button                                            During playback, press this button to return the track to the cue point. If a cue point is not set yet, then press this button to set it at the current track position. If the deck is paused, press and hold this button to play the track from the cue point. Release the button to return the track to the cue point and pause it. To continue playback without returning to the cue point, press and hold this button and then press the :hwlabel:`PLAY` button, afterwards release cue button.
26.       :hwlabel:`SHIFT` + :hwlabel:`CUE` button                         Press to return to the start of the track.
27.       :hwlabel:`PLAY / PAUSE` btton                                    Press to pause or resume playback.
27.       :hwlabel:`SHIFT` + :hwlabel:`PLAY / PAUSE` button                Press to stutter play the track from the last set cue point.
28.       Jog Wheel                                                        Controls the audio playhead when the wheel is touched and moved. When the :hwlabel:`VINYL` button is on, move the platter to “scratch” the track as you would with a vinyl record. When the :hwlabel:`VINYL` button is off (or if you are touching only the side of the platter), move the platter to temporarily adjust the track’s speed.

28.       :hwlabel:`SHIFT` + Jog Wheel                                     Navigates quickly through the track. This only applies if touching the side of the platter or with :hwlabel:`VINYL` deactivated.
29.       :hwlabel:`STOP TIME` knob                                        Controls the rate at which the track slows to a complete stop (“brake time”) during backspin. This also affects how quickly the track starts after a backspin ("Soft Start").
30.       :hwlabel:`VINYL` button                                          Press to activate/deactivate a “vinyl mode” for the platter. When activated, you can use the platter to “scratch” the track as you would with a vinyl record.
31.       Pitch Fader                                                      Move to adjust the speed (pitch) of the track.
32.       :hwlabel:`PITCH BEND –/+` buttons                                Press to momentarily reduce or increase the speed of the track.
32.       :hwlabel:`SHIFT` + :hwlabel:`PITCH BEND –/+` buttons             Press to set the range of the Pitch Fader to values of 4%, 6%, 8%, 10%, 16% and 24%.
33.       :hwlabel:`KEY LOCK` button                                       Press to activate/deactivate Key Lock. When Key Lock is activated, the track’s key will remain the same even if you adjust its speed.
33.       :hwlabel:`SHIFT` + :hwlabel:`KEY LOCK`                           Press to automatically match the corresponding deck’s key with the key of the opposite deck.
34.       :hwlabel:`KEY SELECT/RESET` knob                                 Turn to raise or lower the key of the track. Press to reset the track’s key to its original key.
34.       :hwlabel:`SHIFT` + :hwlabel:`KEY SELECT/RESET` knob              Turn to zoom in and out the waveform or push the knob to reset the Waveform zoom to the level set in preferences.
35.       Performance Pads                                                 *See below.*
40.       :hwlabel:`AUTO LOOP` button                                      Press to create an auto-loop with the length set with loop length. You may change the length of beats by using the :hwlabel:`X1/2` or :hwlabel:`X2` buttons.
40.       :hwlabel:`SHIFT` + :hwlabel:`AUTO LOOP` button                   Press to toggle the current loop on or off. If the loop is ahead of the current play position, the track will keep playing normally until it reaches the loop.
41.       :hwlabel:`X1/2` button                                           Press to halve the length of the current loop.
41.       :hwlabel:`SHIFT` + :hwlabel:`X1/2`                               Press to create a loop in point at the current Location.
42.       :hwlabel:`X2` button                                             Press to double the length of the current loop.
42.       :hwlabel:`SHIFT` + :hwlabel:`X2`                                 Press to create a loop out point at the current Location.
43.       :hwlabel:`</> PARAM 1 2` buttons                                 Press to add/remove rating stars to the loaded track.
43.       :hwlabel:`SHIFT` + :hwlabel:`</> PARAM 1 2` buttons              Press to change the track color in the library.
44.       :hwlabel:`SLIP` button                                           Press to enable or disable Slip Mode. In Slip Mode, you can jump to cue points, trigger loops or use the platters, while the track’s timeline continues. In other words, when you deactivate Slip Mode, the track will resume normal playback from where it would have been if you had never done anything (i.e., as if the track had been playing forward the whole time).
45.       :hwlabel:`CENSOR` button                                         Press and hold this button to play the track in :hwlabel:`REVERSE`. When releasing the button, the track immediately starts playing from it's momentary position. If :hwlabel:`SLIP` was active then after releasing the button the track continues as it had been playing forward the whole time (:hwlabel:`CENSOR`). If you want to use the Censor function a 2nd time, make sure to enable :hwlabel:`SLIP` again.
45.       :hwlabel:`SHIFT` + :hwlabel:`CENSOR` button                      Press to activate a backspin with the length set by the :hwlabel:`STOP TIME` knob.
46.       :hwlabel:`BEAT GRID ADJUST` button                               Press to adjust the Beat Grid to the current play position.
46.       :hwlabel:`SHIFT` + :hwlabel:`BEAT GRID ADJUST` button            Press to activate Quantize mode.
47.       :hwlabel:`BEAT GRID SLIDE` button                                Press to adjust the Beat Grid to another playing track.
48.       :hwlabel:`SELECT/LOAD` knob                                      Turn to navigate through lists. Press the left side button to load a track into the active Deck (1 or 3), press the right side button to load a track into the active Deck (2 or 4). If you keep the knob pressed down longer than 0,5 sec an actual loaded track will be ejected from the deck upon release of the knob.
48.       :hwlabel:`SHIFT` + :hwlabel:`SELECT/LOAD` knob                   Turn to browse quickly through the tracks in the library or push the knob to open folders on the left side of the library.
49.       :hwlabel:`SORT` button                                           Press and hold to activate sort functions.
50.       :hwlabel:`BACK` button                                           Press to switch between right and left side of the library.
50.       :hwlabel:`SHIFT` + :hwlabel:`BACK` button                        Press to move through frames inside the GUI.
50.       :hwlabel:`SORT` + :hwlabel:`BACK` button                         Press to sort the tracks by Beats Per Minute.
51.       :hwlabel:`L.PREP` button                                         Press to load the currently selected track to the Preview Deck.
51.       :hwlabel:`SHIFT` + :hwlabel:`L.PREP` button                      Press to start and stop playing the track in Preview Deck.
51.       :hwlabel:`SORT` + :hwlabel:`L.PREP` button                       Press to sort the tracks by their Key.
52.       :hwlabel:`FILES` button                                          Press to maximise the library. Press this button again to exit maximised library.
52.       :hwlabel:`SORT` + :hwlabel:`FILES` button                        Press to sort the tracks by Artist.
53.       :hwlabel:`PANEL` button                                          Press to open and close the FX panel inside the GUI.
53.       :hwlabel:`SORT` + :hwlabel:`PANEL` button                        Press to sort the tracks by Title.
54.       :hwlabel:`NEEDLE DROP` strip                                     Place your finger on a point along this sensor to jump to that point in the track (strip represents entire track).
54.       :hwlabel:`SHIFT` + :hwlabel:`NEEDLE DROP` strip                  Press to jump to a position while a track is currently playing.
========  ===============================================================  ===============================================================


Performance Pads
^^^^^^^^^^^^^^^^

Mode Selection
--------------

========  ===============================================================  ===============================================================
No.       Control                                                          Function
========  ===============================================================  ===============================================================
36.       :hwlabel:`CUE` button                                            Press to switch to "Hot Cue" mode.
37.       :hwlabel:`ROLL` button                                           Press to switch to "Roll" mode.
38.       :hwlabel:`SLICER` button                                         Press to switch to "Beatjump" mode.
39.       :hwlabel:`SAMPLER` button                                        Press to switch to "Sampler" mode.
========  ===============================================================  ===============================================================


Hot Cue Mode
------------

========  ===============================================================  ===============================================================
No.       Control                                                          Function
========  ===============================================================  ===============================================================
35.       Pad                                                              Set or play a :term:`hotcue`.
35.       :hwlabel:`SHIFT` + Pad                                           Press to delete an existing Hot Cue.
========  ===============================================================  ===============================================================

Roll  Mode
----------

This mode lets you repeat a number of beats while keep pushing a pad down. From the 1st to 8th performance pad the loop size is set as 1/16, 1/8, 1/4, 1/2, 1, 2, 4 and 8 beats. The :hwlabel:`SLIP` function remains active so that the track continues at the position where it had been playing forward the whole time.

Beatjump Mode
-------------

The first row buttons jump forward by 1, 2, 4 and 8 beats. The 2nd row buttons jump backward by 1, 2, 4 and 8 beats.

Sampler Mode
------------

8 samplers can be triggered from either Deck.
Add samplers to the sampler bank pushing a performance pad.
If a sampler is loaded, then another push on the pad will play the sampler from its cue point.
Push the pad again while playing will replay the sampler from cue point.

Use :hwlabel:`SHIFT` + Pad to stop a sampler while playing or eject a sampler when stopped.


FX Sections
~~~~~~~~~~~

========  ===============================================================  ===============================================================
No.       Control                                                          Function
========  ===============================================================  ===============================================================
11.       :hwlabel:`FX ASSIGN` buttons                                     Press assign :hwlabel:`FX 1` and/or :hwlabel:`FX 2` to the corresponding channel.
55.       :hwlabel:`FX ON` button                                          Press to turn the corresponding effect on or off.
55.       :hwlabel:`SHIFT` + :hwlabel:`FX ON` button                       Press to select an effect from the list that was enabled in the Mixxx Preferences FX section.
56.       :hwlabel:`FX 1`, :hwlabel:`FX 2` or :hwlabel:`FX 3` knobs        Turn to adjust the level of the corresponding effect. The :hwlabel:`FX ON` button under the knob must be lit for this knob to function.
57.       :hwlabel:`FX BEATS` encoder                                      Turn to adjust the Wet/Dry rate of the effects.
58.       :hwlabel:`FX TAP` button                                         Press to activate effects for the Master output. This can be overlapped with Channel Effects.
58.       :hwlabel:`SHIFT` + :hwlabel:`FX TAP` button                      Press to activate effects for headphones cue.
========  ===============================================================  ===============================================================

LEDs
~~~~

The Channel Volume Meters matches to the ones shown in Mixxx GUI. Only when clipping the red LED illuminates.

The Master Volume Meter is not correlated to Mixxx GUI as the controller handles that in Hardware.

Button LEDs are fully mapped for the first function. As you press and hold :hwlabel:`SHIFT` then the secondary functions have only got some flashing LEDs mapped, e.g. TAP and KEY SYNC, when activated.

Platter Ring LEDs are correlated with the :hwlabel:`VINYL` button.

  - If vinyl mode is enabled, the LED imitates a turntable platter spinning at 33.3 rpm.
  - If vinyl mode is disabled, the current track position is indicated by the Platter LEDs starting at the top.

:hwlabel:`SHIFT` + :hwlabel:`Deck` to switch Platter Ring LED Mode.

  - Mode 0 = Single "off" LED chase (all other LEDs are "on")
  - Mode 1 = Single "on" LED chase (all other LEDs are "off")

    .. hint::
        The Platter Ring LED Mode is set to "Mode 1" by default but can be changed inside the script :file:`Denon-MC7000-scripts.js`.

Known Issues
~~~~~~~~~~~~

- Some Performance Pad modes are not available (Cue Loop, Flip, Saved Loop, Slicer Loop, Velocity Sampler, Pitch).
- The Effect Units don't use Mixxx' Standard Effects Mapping
