Numark NS4FX
============

-  `Manufacturer’s product page <https://www.numark.com/product/ns4fx>`__
-  `Forum thread <https://mixxx.discourse.group/t/numark-ns4-fx-mapping-repository/32767>`__

The Numark NS4FX is a 4 channel (with channel layering) DJ controller with an integrated audio interface.
The stand out feature of the Mixtrack Platinum is the LCD displays integrated into the jog wheels.
It is a USB Audio and MIDI Class compliant device and works with Linux, macOS, and Windows.

.. versionadded:: 1.0

Audio interface
---------------

Configure Mixxx’s main output for channels 1-2 and Headphones output for Channels 3-4.

The microphone input on this controller is not available to the computer through the controller’s audio interface.
It is mixed with the main output in hardware, so this controller’s audio interface is not suitable for broadcasting or recording the inputs.
If you want to use the controller for broadcasting or recording, a separate :ref:`audio interface <hardware-audio-interfaces>` with a microphone input is suggested.

Configuration Options
---------------------

You can set configuration options in the Mixxx controller preferences.

-  **EnableWheel:** if true, wheel/vinyl mode will be enabled by default (defaults to true)
-  **ShowTimeElapsed:** if true, time elapsed will be show by default on the displays, otherwise time remaining will be displayed (defaults to true)
-  **UseManualLoopAsCue:** if true, the manual loop controls will behave as hotcues 5-8. When enabled, the normal loop control behavior can be activated using shift+pad mode+mode button and pad
   mode+mode to use the hotcue behavior (defaults to false)
-  **UseAutoLoopAsCue:** if true, the auto loop controls will behave as hotcues 5-8. When enabled, the normal loop control behavior can be activated using shift+pad mode+mode button and pad mode+mode
   to use the hotcue behavior (defaults to false)
-  **UseCueAsSampler:** if true, the hotcues will control sampler slots 5-8 when sampler mode is active. When enabled, the normal hotcue control behavior can be activated using shift+pad mode+sampler
   while pad mode+sampler will activate the special behavior (defaults to false)
-  **Shift+Load ejects track** if true, pressing SHIFT + load will eject a track (defaults to false)

Mapping
-------

.. figure:: ../../_static/controllers/numark_ns4fx.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Numark NS4FX (schematic view)
   :figclass: pretty-figures

   Numark NS4FX (schematic view)

   1. **Browse Knob:** Rotate this knob clockwise to scroll down, counter clockwise to scroll up.
      Press the Knob to load tracks into the inactive deck, expand entries in the library view, and select playlists and crates.
      **Shift + Turn:** Page down/page up, allows you to scroll by page instead of by item.
      **Shift + Push:** Focus next library pane, allows you to toggle between the left and right panes.

   2. **Load:** Press one of these buttons while a track is selected in the library window to assign it to the active deck.
      **Shift + Load:** Load the track and play. If the 'Shift+Load ejects track' option is set, eject the track)

   3. **Level:** Adjusts the pre-fader, pre-EQ audio level of the corresponding channel.

   4. **Treble EQ:** Controls the treble frequencies for the individual channels.

   5. **Mid EQ:** Controls the mid-range frequencies for the individual channels.

   6. **Bass EQ:** Controls the bass frequencies for the individual channels.

   7. **Filter:** Adjusts the amount of the filter effect.
      Turning the knob left and right will produce a low-pass filter and high-pass filter, respectively.

   8. **Headphone Cue:** Sends pre-fader audio to the cue channel for headphone monitoring.

   9. **Channel Fader:** Adjusts the volume of the individual channels in the software.

   10. **Main Output LEDs:** Displays the audio level going to the Main Output.

   11. **Crossfader:** Controls the blend between the two decks.

   12. **Cue Gain:** Adjusts the volume for headphone cueing.

   13. **Cue Mix:**; Adjusts the audio output to the headphones, mixing between the cue output and the master mix output.

   14. **FX Wet/Dry Knob:** Turn this knob to adjust the wet/dry mix of the effects.

   15. **Beats Multiplier:** As Mixxx does not have a single BEATS knob, you can use it to control effect units superknobs.

   16. **Tap BPM:** Press this button 4 or more times to manually enter a new BPM.
       The software will ignore the track's BPM and follow your manually entered tempo.

       Press SHIFT and this button to reset the tempo to the track’s default BPM.

   17. **Software FX:** Press one or more of these buttons to select active software effects.

   18. **FX On / Off / Hold:** Push up on the toggle switch to latch (lock) the FX in the 'on' position.
       Push down on the toggle switch to turn the FX on momentarily.
       When the toggle switch is in the middle position, the FX will be off.

   19. **Layer:** Press this button to select which layer in the software is controlled by that hardware deck.
       Deck A can control Layer 1 or 3 while Deck B can control Layer 2 or 4.

   20. **Platter/Jog Wheel:** This capacitive, touch-sensitive jog wheel controls the audio when the wheel is touched and moved.
       When the Scratch button is not active, use the jog wheel to bend the pitch of the track.
       When the Scratch button is active, use the jog wheel to grab and move the audio, "scratching" the track as you would with a vinyl record.
       You can also grab the non-touch-sensitive outer wheel to bend the pitch of the track.

       Press Shift and move the wheel to quickly search through the track audio.

   21. **Display:** Use this screen to view information about the current track.
       See the TODO DISPLAY for more information.

   22. **Shift:** Allows multiple control commands to be triggered when pressed first along with other buttons.

   23. **Scratch:** Press this button to turn on the scratch feature for the jog wheel.

   24. **Pitch Fader:** Adjust the speed of the music. Moving towards the "+" will speed the music up, while moving towards the "–" will slow it down.

   25. **Pitch Bend Down:** Press and hold to momentarily reduce the speed of the track.
       **Shift + Pitch Bend Down:** Adjust the key of the playing track down.
       **Pitch Bend Up + Pitch Bend Down:** Toggle keylock.

   26. **Pitch Bend Up:** Press and hold to momentarily increase the speed of the track.
       **Shift + Pitch Bend Up:** Adjust the key of the playing track up.
       **Pitch Bend Up + Pitch Bend Down:** Toggle keylock.

   27. **Sync:** Set the BPM of this deck to match the opposite deck.
       **Press:** Press once to synchronize the tempo (BPM) to that of to that of the other track
       **Long Press:** Enable :ref:`Sync Lock <sync-lock>`. Press again to disable.
       **Shift + Sync:** Toggle quantize mode.

   28. **Cue (Transport Control):** Behavior depends on the :ref:`cue mode <interface-cue-modes>` set in the Mixxx preferences.
       **Shift + Cue:** return the play head to the start of the track and stop the deck.

   29. **Play/Pause:** Starts and suspends playback.

   30. **Performance Pads:** These pads have different functions on each deck depending on the current pad mode.
       See TODO Performance Pad Modes to learn how to use the pads in each mode.

       With Mixxx, the bottom row of pads is used to trigger Stutter, Start, Search Backward and Search Forward:

         * Stutter: Repeats or "stutters" the sample when the pad is repeatedly tapped from the last cue position.
         * Start: Jumps to the beginning of the current track.
         * Search Backward: Searches backward through the current track.
         * Search Forward: Searches forward through the current track.

         TIP: the bottom four pads can also be used for the selected pad mode.

   31. **Cue mode:** Press this button to enter Cue mode.

   32. **Auto Loop:** Press this button to enter Auto Loop mode.

   33. **Fader Cuts:** Press this button to enter Fader Cuts mode.

   34. **Sampler:** Press this button to enter Sampler mode.

   35. **Loop On/Off:** Press this button to activate auto loop on/off. Hold Shift and press this button to trigger a reloop.

   36. **Loop 1/2:** Press this button when a loop is active to decrease the loop size by half. Hold Shift and press this button to set the Loop In point.

   37. **Loop x2:** Press this button when a loop is active to double the loop size. Hold Shift and press this button to set the Loop Out point.

   38. **Mic 1/Line Switch:** Flip this switch to the appropriate position, depending on the device connected to the Mic 1 Input.
       If you are using a microphone connected to the Mic 1 Input, set the switch to Mic 1.
       If you are using a device such as a CD player or sampler connected to the AUX input, set the switch to Line.
   39. **Mic 1/Line Level:** Turn this knob to adjust the level for the Mic 1 Input or Aux Input.
   40. **Mic 1/Line Tone:** Turn this knob to adjust the tone of the Mic 1 Input or Aux Input.
       Turn left to increase the Low frequency tone, or turn right to increase the High frequency tone.
   41. **Booth Volume:** Turn this knob to adjust the output volume of the Booth Output mix.
   42. **Main Volume:** Turn this knob to adjust the output volume of the Main Output mix.


Performance Pads:
=================

The top row of pads is for controlling loops and samples. To select a mode, hold down the Pad Mode button and press one of the upper pads. An LED under the pad section indicates the currently selected
mode. See the subsections below for details about each mode.

| The bottom row of pads is used to trigger hotcue points. If a hotcue point has not already been set for the loaded track, this control will mark the hotcue point. If a hotcue point has already been
  set, this control will jump to it.
| **Shift + Hot Cue**: Deletes the assigned hotcue point

Note: the top row can be made to control hotcues 5-8 using shift+pad mode+loop mode (being Auto Loop or Manual Loop). This can also be made the default using a config option (see documentation above
and below).

Manual Loop Mode
^^^^^^^^^^^^^^^^

Hold Pad Mode and press the pad marked Manual Loop (silkscreened above the pad) to assign the upper 4 pads to the functions listed below:

-  **Loop In** – Sets the beginning of a loop: When assigned, the Pad LED will light blue
-  **Loop Out** – Sets the end point for the loop: When assigned, the Pad LED will light blue
-  **On/Off** – (De)activate the loop. If a loop has not been set, this button will have no effect.: When assigned, the Pad LED will light blue
-  **Loop x1/2** – Halve the length of the loop. Press SHIFT + Loop x1/2 to double the length of the loop. Note that this does not update the beatloop size shown on screen.

If Manual Loop is selected with SHIFT and Pad Mode held down this will activate control of hotcues 5-8 on the upper row instead of the looping controls. Select Manual Loop again while holding Pad Mode
to restore the default behavior. There will be no indication of which mode is selected (beyond the LEDs on the keys themselves, which will vary depending on loop and hotcue status). The
**UseManualLoopAsCue** config option can be set in the mapping file (see above) to swap the default “shadow” mode of the looping controls such that hotcue control will be the default and manual loop
control with be selected when SHIFT is used.

Auto Loop Mode
^^^^^^^^^^^^^^

| Hold Pad Mode and press the pad marked Auto Loop to assign the upper 4 pads to the functions listed below:
| \* **Auto 1:** – Sets and starts playback of a 1-beat autoloop.

-  **Auto 2:** – Sets and starts playback of a 2-beat autoloop.
-  **Auto 3:** – Sets and starts playback of a 4-beat autoloop.
-  **Auto 4:** – Sets and starts playback of a 8-beat autoloop.
   \* **Shift + Auto 1:** – When held, starts a 1/16-beat loop roll.
-  **Shift + Auto 2:** – When held, starts a 1/8-beat loop roll.
-  **Shift + Auto 3:** – When held, starts a 1/4-beat loop roll.
-  **Shift + Auto 4:** – When held, starts a 1/2-beat loop roll.

Note: loop rolls activate slip mode so the play position continues to advance normally, such that when the loop is released, play continues from the place it would have been if no loop had been
activated.

If Auto Loop is selected with SHIFT and Pad Mode held down this will activate control of hotcues 5-8 on the upper row instead of the looping controls. Select Auto Loop again while holding Pad Mode to
restore the default behavior. There will be no indication of which mode is selected (beyond the LEDs on the keys themselves, which will vary depending on loop and hotcue status). The
**UseAutoLoopAsCue** config option can be set in the mapping file (see above) to swap the default “shadow” mode of the looping controls such that hotcue control will be the default and auto loop
control with be selected when SHIFT is used.

Sample Mode
^^^^^^^^^^^

Hold Pad Mode and press the pad marked Sampler to enter sampler mode (hold down SHIFT as well to control slots 5-8 using the hotcue buttons). A press of any of the sample buttons will load a sample if
the sampler is not loaded. SHIFT + sample pad will unload a sample if it is not playing. Pressing a pad when a sample is loaded will play the sample, pressing SHIFT + sample pad while a sample is
playing will stop it.

Use **shift+cue gain** to adjust the volume of the sampler. When switching to the pad mode to sampler, hold down SHIFT to control slots 5-8 using the hotcue buttons.

Note: the 8 sample slots on each deck all control the same 8 slots in Mixxx no matter which deck the sampler is active on. This is because the controller sends the same MIDI codes for button presses
on each side, so there is no way for Mixxx to tell whether a sampler button was pressed on the left or right side of the controller.
