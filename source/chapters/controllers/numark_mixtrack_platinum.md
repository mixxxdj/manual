# Numark Mixtrack Platinum

[[/media/undefined/mixtrackplatinum_ortho_3000x1875_web.jpg|]]

  - [Manufacturer's product
    page](https://www.numark.com/product/mixtrack-platinum)
  - [Forum
    thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=8863)
  - [Download mapping for
    Mixxx 2.1](https://www.mixxx.org/forums/viewtopic.php?f=7&t=8863&p=34041#p34041)
    

The Numark Mixtrack Platinum is a 2 channel (with 4 channel layering)
entry level DJ controller with an integrated audio interface. The stand
out feature of the Mixtrack Platinum is the LCD displays integrated into
the jog wheels. It is a USB Audio and MIDI Class compliant device and
works with Linux, macOS, and Windows.

## Audio interface

Configure Mixxx's Master output for channels 1-2 and Headphones output
for Channels 3-4.

The microphone input on this controller is not available to the computer
through the controller's audio interface. It is mixed with the master
output in hardware, so this controller's audio itnerface is not suitable
for broadcasting or recording the inputs. If you want to use the
controller for broadcasting or recording, a separate [USB audio
interface](Hardware%20Compatibility#USB%20Audio%20Interfaces) with a
microphone input is suggested.

## Configuration Options

Configuration options can be set in the mapping. You will need to edit
the values below at the very top of the JavaScript file
`Numark-Mixtrack-Platinum-scripts.js` and save changes. Allowed values
are “true” or “false” unless specified.

  - **EnableWheel:** if true, wheel/vinyl mode will be enabled by
    default (defaults to true)
  - **ShowTimeElapsed:** if true, time elapsed will be show by default
    on the displays, otherwise time remaining will be displayed
    (defaults to true)
  - **UseManualLoopAsCue:** if true, the manual loop controls will
    behave as hotcues 5-8. When enabled, the normal loop control
    behavior can be activated using shift+pad mode+mode button and pad
    mode+mode to use the hotcue behavior (defaults to false)
  - **UseAutoLoopAsCue:** if true, the auto loop controls will behave as
    hotcues 5-8. When enabled, the normal loop control behavior can be
    activated using shift+pad mode+mode button and pad mode+mode to use
    the hotcue behavior (defaults to false)
  - **UseCueAsSampler:** if true, the hotcues will control sampler slots
    5-8 when sampler mode is active. When enabled, the normal hotcue
    control behavior can be activated using shift+pad mode+sampler while
    pad mode+sampler will activate the special behavior (defaults to
    false)
  - **ShiftLoadEjects:** if true, pressing shift + load will eject a
    track (defaults to false)

## Mapping

[[/media/hardware/mixtrack_platinum_labeled.png|]]

1\. **Browse Knob:** Rotate this knob clockwise to scroll down, counter
clockwise to scroll up. Press the Knob to load tracks into the inactive
deck, expand entries in the library view, and select playlists and
crates.  
**Shift + Turn:** Page down/page up, allows you to scroll by page
instead of by item.  
**Shift + Push:** Focus next library pane, allows you to toggle between
the left and right panes.

2\. **Master Gain:** Adjusts the master volume in the software.  
**Note:** This control does not affect the microphone volume which is
summed with the final output of the Master Gain to the Master Output.
Use the Mic Gain knob to control the microphone volume.

3\. **Cue Mix:** Adjusts the software’s audio output to the headphones,
mixing between the cue (PFL) output and the master mix output.

4\. **Cue Gain:** Adjusts the volume for headphone cueing in the
software.  
**Shift+Cue Gain:** adjust the volume of the first 8 sampler banks

5\. **VU Meter:** Monitor the volume levels of the master output and
each channel. When cue/pfl is active on ANY channel, the meter shows the
mono levels each channel (left meter shows the deck on the left, right
meter for the deck on the right). Otherwise the meter shows the stereo
levels of the master output.

6\. **Load:** Press one of these buttons while a track is selected in
the library window to assign it to Deck 1 and 2 (or 3 and 4),
respectively, in the software.  
**Shift + Load:** Load the track and play (or if the ShiftLoadEjects
option is set, eject the track)

7\. **Gain Knobs:** Adjust the gain of the deck.  
**Shift + Gain:** Adjust parameter 2 of the currently focused effect on
this deck.

8\. **High EQ Knobs:** Adjust the volume of the high frequencies of the
deck.  
**Shift + High:** Adjust parameter 3 of the currently focused effect on
this deck.

9\. **Mid EQ Knobs:** Adjust the volume of the mid frequencies of the
deck.  
**Shift + Mid:** Adjust parameter 4 of the currently focused effect on
this deck.

10\. **Low EQ Knobs:** Adjust the volume of the low frequencies of the
deck.  
**Shift + Low:** Adjust parameter 5 of the currently focused effect on
this deck.

11\. **Filter:** Adjusts the amount of the filter effect. Turning the
knob left controls the low pass filter; turning it right controls the
high pass filter. The effect applied here can be configured (the Quick
Effect option in the Equalizer preferences).  
**Shift + Filter:** With no effect focused, this controls the Superknob
of the effects unit. With an effect focused, this adjusts parameter 1 of
the currently focused effect on this deck.

12\. **Cue/PFL/Headphones:** Sends pre-fader audio to the headphone
output. If any channels have the cue button active, the VU meter will
show channel output levels instead of master output levels on all decks.

13\. **Volume fader:** Adjusts the volume of the deck.

14\. **Crossfader:** Controls the blend between the two decks.

15-16. **Pitch Bend Down/Up:** Press and hold to momentarily reduce the
speed of the track.  
**Shift + Pitch Bend:** adjust the key of the playing track up or down.
Press both buttons to reset the key.  
**Pitch Bend Up + Pitch Bend Down:** toggle keylock

17\. **Pitch Fader:** Adjust the speed of the music (activate keylock to
adjust tempo without affecting pitch). Note that moving the fader down
*increases* speed, as marked by the "+" at the bottom of the fader on
the controller. This can be reversed in Mixxx's preferences under
Interface \> Speed slider direction.

18\. **Touch Strip:** Use the Touch Strip to adjust the deck’s Effect
Unit Superknob. When an effect is focused, the touch strip controls that
effect's meta knob.  
**Shift + Touch Strip:** search through a track’s timeline

19\. **Beats Knob:** Adjusts the Dry/Wet mix of the deck’s Effect Unit.

20\. **FX 1 On/Off:** Toggle FX 1 of the deck’s Effect Unit  
**Shift + FX 1:** Cycle to the next effect.  
**Hold + FX 1:** Enable this effect in instant mode, after the button is
released the effect will be disabled again.  
**Tap + FX 1:** Focus this effect to allow adjusting its metaknob with
the touch strip.

21\. **FX 2 On/Off:** Toggle FX 2 of the deck’s Effect Unit  
**Shift + FX 2:** Cycle to the next effect.  
**Hold + FX 2:** Enable this effect in instant mode, after the button is
released the effect will be disabled again.  
**Tap + FX 2:** Focus this effect to allow adjusting its metaknob with
the touch strip.

22\. **FX 3 On/Off:** Toggle FX 3 of the deck’s Effect Unit  
**Shift + FX 3:** Cycle to the next effect.  
**Hold + FX 3:** Enable this effect in instant mode, after the button is
released the effect will be disabled again.  
**Tap + FX 3:** Focus this effect to allow adjusting its metaknob with
the touch strip.

23\. **Tap BPM:** Press this button several times on beat to manually
enter a new BPM. The software will ignore the track's BPM and follow
your manually entered tempo.  
24\. **Wheel button:** If active you can use the platter/jog wheel to
grab and move the audio, scratching the track like a vinyl record.  
**Shift + Wheel:** Toggle elapsed time or time remaining on the deck's
display.

25\. **Platter/Jog Wheel:** If Wheel is enabled, touching the platter
will result in vinyl scratching, when disabled, nothing will happen and
the entire jog wheel behaves as if the side was touched.  
**Touch side:** Pitch bend (nudging) if track is playing  
**Shift + Touch platter:** Quickly scroll through the track  
**Shift + Touch side:** Beat jump  
26\. **Jog Wheel Display:** The display is fully functional with this
mapping. It will display the position of the spinner, play position,
bpm, and keylock status.

27\. **Deck Switch:** Allows switching between decks 1/3 and 2/4.

28\. **Shift:** Allows alternate options to be activated for various
controls.

29\. **Sync:** Set the BPM of this deck to match the opposite deck.
**Press:** Press once to synchronize the tempo (BPM) to that of to that
of the other track  
**Long Press:** Enable master sync. Press again to disable.  
**Shift + Sync:** Toggle quantize mode.

30\. **Cue (Transport Control):** Behavior depends on the [cue
mode](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
set in the Mixxx preferences.  
**Shift + Cue:** return the play head to the start of the track and stop
the deck.

31\. **Play/Pause:** Starts and stops playback.  
**Shift + Play/Pause:** stutter the track from the last set cue point.
If a cue point has not been set, the play head will return to the start
of the track.

32\. **Pad Mode:** Hold this button to see the currently selected pad
mode, while holding select between Manual Loop, Auto Loop, and Sampler
modes. Additionally control of hotcues 5-8 can be activated using
shift+pad mode+loop mode (either manual or auto loop). Setting either of
the **UseManualLoopAsCue** or **UseAutoLoopAsCue** options will reverse
the selection of hotcue vs loop mode when shift is held.  
**Pad Mode+Manual Loop:** set the top row of pads to manual loop control
mode (see below)  
**Pad Mode+Auto Loop:** set the top row of pads to auto loop/loop roll
control mode (see below)  
**Pad Mode+Sampler:** set the top row of pads to sampler control mode
(see below)  
**Shift+Pad Mode+Manual Loop:** set the top row of pads to control
hotcues 5-8 (see below)  
**Shift+Pad Mode+Auto Loop:** set the top row of pads to control hotcues
5-8 (see below)  
**Shift+Pad Mode+Sampler:** set the bottom row of pads to control
sampler banks 5-8 (see below)

33\. **Performance Pads:**

The top row of pads is for controlling loops and samples. To select a
mode, hold down the Pad Mode button and press one of the upper pads. An
LED under the pad section indicates the currently selected mode. See the
subsections below for details about each mode.

The bottom row of pads is used to trigger hotcue points. If a hotcue
point has not already been set for the loaded track, this control will
mark the hotcue point. If a hotcue point has already been set, this
control will jump to it.  
**Shift + Hot Cue**: Deletes the assigned hotcue point

Note: the top row can be made to control hotcues 5-8 using shift+pad
mode+loop mode (being Auto Loop or Manual Loop). This can also be made
the default using a config option (see documentation above and below).

#### Manual Loop Mode

Hold Pad Mode and press the pad marked Manual Loop (silkscreened above
the pad) to assign the upper 4 pads to the functions listed below:  

  - **Loop In** – Sets the beginning of a loop: When assigned, the Pad
    LED will light blue  
  - **Loop Out** – Sets the end point for the loop: When assigned, the
    Pad LED will light blue  
  - **On/Off** – (De)activate the loop. If a loop has not been set, this
    button will have no effect.: When assigned, the Pad LED will light
    blue  
  - **Loop x1/2** – Halve the length of the loop. Press Shift + Loop
    x1/2 to double the length of the loop. Note that this does not
    update the beatloop size shown on screen.

If Manual Loop is selected with Shift and Pad Mode held down this will
activate control of hotcues 5-8 on the upper row instead of the looping
controls. Select Manual Loop again while holding Pad Mode to restore the
default behavior. There will be no indication of which mode is selected
(beyond the LEDs on the keys themselves, which will vary depending on
loop and hotcue status). The **UseManualLoopAsCue** config option can be
set in the mapping file (see above) to swap the default "shadow" mode of
the looping controls such that hotcue control will be the default and
manual loop control with be selected when Shift is used.

#### Auto Loop Mode

Hold Pad Mode and press the pad marked Auto Loop to assign the upper 4
pads to the functions listed below:  
\* **Auto 1:** – Sets and starts playback of a 1-beat autoloop.  

  - **Auto 2:** – Sets and starts playback of a 2-beat autoloop.  
  - **Auto 3:** – Sets and starts playback of a 4-beat autoloop.  
  - **Auto 4:** – Sets and starts playback of a 8-beat autoloop.  
    \* **Shift + Auto 1:** – When held, starts a 1/16-beat loop roll.  
  - **Shift + Auto 2:** – When held, starts a 1/8-beat loop roll.  
  - **Shift + Auto 3:** – When held, starts a 1/4-beat loop roll.  
  - **Shift + Auto 4:** – When held, starts a 1/2-beat loop roll.

Note: loop rolls activate slip mode so the play position continues to
advance normally, such that when the loop is released, play continues
from the place it would have been if no loop had been activated.

If Auto Loop is selected with Shift and Pad Mode held down this will
activate control of hotcues 5-8 on the upper row instead of the looping
controls. Select Auto Loop again while holding Pad Mode to restore the
default behavior. There will be no indication of which mode is selected
(beyond the LEDs on the keys themselves, which will vary depending on
loop and hotcue status). The **UseAutoLoopAsCue** config option can be
set in the mapping file (see above) to swap the default "shadow" mode of
the looping controls such that hotcue control will be the default and
auto loop control with be selected when Shift is used.

#### Sample Mode

Hold Pad Mode and press the pad marked Sampler to enter sampler mode
(hold down shift as well to control slots 5-8 using the hotcue buttons).
A press of any of the sample buttons will load a sample if the sampler
is not loaded. Shift + sample pad will unload a sample if it is not
playing. Pressing a pad when a sample is loaded will play the sample,
pressing shift + sample pad while a sample is playing will stop it.

Use **shift+cue gain** to adjust the volume of the sampler. When
switching to the pad mode to sampler, hold down shift to control slots
5-8 using the hotcue buttons.

Note: the 8 sample slots on each deck all control the same 8 slots in
Mixxx no matter which deck the sampler is active on. This is because the
controller sends the same MIDI codes for button presses on each side, so
there is no way for Mixxx to tell whether a sampler button was pressed
on the left or right side of the controller.
