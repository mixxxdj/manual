# Numark Mixtrack Pro II

[[/media/hardware/mixtrack_pro_ii_ortho-624x390.jpg|mixtrack\_pro\_ii\_ortho-624x390.jpg]]

  - [Manufacturer's product
    page](http://www.numark.com/product/mixtrack-pro-ii)
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=6833)

The Numark Mixtrack Pro II is the successor of [Numark Mixtrack
Pro](numark_mixtrack_pro) and features the same hardware with some minor
design changes.

The audio interface is recognized in Ubuntu 14.04 out of the box.

## Mapping

This mapping is integrated in Mixxx 2.1 with [this
PR](https://github.com/mixxxdj/mixxx/pull/1540). This mapping is based
on [this
mapping](https://github.com/snowyoneill/Mixxx-Numark-MixTrack-Pro-II-2016.midi).

[[/media/hardware/numarkmixtrackproii.png|numarkmixtrackproii.png]]

### 1\. Browser Knob

Rotate the knob to cycle through folders and tracks.  
**Press:** Same as Back button.

### 2\. Load

Load the track selected in the library to the deck.

### 3\. Back

Cycles between the file structure and the music library in the software.

### 4\. Shift

Allows multiple control commands to be triggered when pressed and held
first along with other buttons.

### 5\. Play/Pause

Starts and suspends playback.  
**Shift + Play/Pause:** Activates *soft start* effect if paused or
*brake* effect if playing.

### 6\. Headphone Cue

Sends pre-fader audio to the Cue Channel for headphone monitoring.

### 7\. Cue (Transport Control)

Behavior depends on the [cue
mode](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
set in the Mixxx preferences.  
**Shift + Cue:** return the play head to the start of the track.

### 8\. Platter/Jog Wheel

This capacitive, touch-sensitive jog wheel controls the audio when the
wheel is touched and moved. When the Scratch button is not active, use
the wheel to bend the pitch of the track. When the Scratch button is
active, use the wheel to grab and move the audio, "scratching" the track
as you would with a vinyl record. You can also grab the
non-touch-sensitive outer wheel to bend the pitch of the track.

### 9\. Scratch

Controls the behavior of the platters. When not active, the platter will
function as Pitch Bend. When active, the platter will have the ability
to scratch.

### 10\. Pitch Fader

Controls the tempo (speed) of the individual decks.

### 11\. Pitch Bend -

Press and hold to momentarily reduce the speed of the track.  
**Shift + Pitch Bend -:** Toggles keylock on/off.

### 12\. Pitch Bend +

Press and hold to momentarily increase the speed of the track.  
**Shift + Pitch Bend +:** Changes pitch fader range.

### 13\. Sync

Enables BPM syncing between decks.

### 14\. Effect Control

Adjusts effect metaknobs.  
**Shift + Effect Control:** Selects effect.

### 15\. Beats

Adjusts the Dry/Wet mix of the EffectUnit.  
**Shift + Beats:** Adjust the deck's QuickEffect.

### 16\. Loop In

Function of this button depends on the current Pad Mode.  
**Shift + Loop In:** Sets the current Pad Mode to "Loop Mode".  
**Loop Mode:** Press this pad to set the beginning of a loop.  
**Sample Mode:** Plays the sample assigned to Sampler 1 (left deck) or
Sampler 5 (right deck).  
**Cue Mode:** If Hotcue 1 has not already been set for the loaded track,
this control will set Hotcue 1 at current position in the track. If
Hotcue 1 has already been set, this control will jump to Hotcue 1.

### 17\. Loop Out

Function of this button depends on the current Pad Mode.  
**Shift + Loop Out:** Sets the current pad mode to “Sample Mode".  
**Loop Mode:** Set the end of a loop.  
**Sample Mode:** Plays the sample assigned to Sampler 2 (left deck) or
Sampler 6 (right deck).  
**Cue Mode:** If Hotcue 2 has not already been set for the loaded track,
this control will set Hotcue 2 at current position in the track. If
Hotcue 2 has already been set, this control will jump to Hotcue 2.

### 18\. Reloop

Function of this button depends on the current Pad Mode.  
**Shift + Reloop:** Sets the current pad mode to "Cue Mode".  
**Loop Mode:** Deactivate an active loop. If no loop is active, this
will activate the loop and start playback from its Loop In point.  
**Sample Mode:** Plays the sample assigned to Sampler 3 (left deck) or
Sampler 7 (right deck).  
**Cue Mode:** If Hotcue 3 has not already been set for the loaded track,
this control will set Hotcue 3 at current position in the track. If
Hotcue 3 has already been set, this control will jump to Hotcue 3.

### 19\. Loop x1/2

Function of this button depends on the current Pad Mode.  
**Loop Mode:** Half the loop size.  
**Shift + Loop x1/2 when in Loop Mode:** Double the loop size.  
**Sample Mode:** Plays the sample assigned to Sampler 4 (left deck) or
Sampler 8 (right deck).  
**Cue Mode:** Toggles Hotcue Delete Mode. Press this button, and then
press one of the other pads in the row to delete that Hotcue.  
**Note:** This button is lit when in Hotcue Delete Mode.

### 20\. FX 1 On/Off

Toggle the 1st effect in the unit on/off.  
**Shift + FX 1:** Sets and starts playback of a 1-beat autoloop.

### 21\. FX 2 On/Off

Toggle the 2nd effect in the unit on/off.  
**Shift + FX 2:** Sets and starts playback of a 2-beat autoloop.

### 22\. FX 3 On/Off

Toggle the 3rd effect in the unit on/off.  
**Shift + FX 3:** Sets and starts playback of a 4-beat autoloop.

### 23\. Tap

Allows manual entry of song's BPM by repeated pressing along the beats
of the track.  
**Shift + Tap:** Sets and starts playback of a 16-beat autoloop.  
**Note:** This button will blink at each detected beat in the track.

### 24\. Channel Volume

Adjusts the volume of the deck.

### 25\. Master Gain

Adjusts the volume of the master mix coming from the software.  
**Note:** This does not affect the microphone volume. Use the Mic Gain
knob to control the microphone volume.

### 26\. Crossfader

Controls the blend between the two decks.

### 27\. High EQ

Controls the treble frequencies for the deck.

### 28\. Mid EQ

Controls the mid range frequencies for the deck.

### 29\. Low EQ

Controls the bass frequencies for the deck.

### 30\. Cue Gain

Adjusts the volume for headphone cueing in the software.

### 31\. Cue Mix

Adjusts the software’s audio output to the headphones, mixing between
the cue output and the master mix output.

### 32\. Stutter

Press this button while the music is playing to jump back to the last
set cue point, creating a "stutter" effect.

## Other Community Mappings

  - <https://github.com/tompreston/Mixxx-Numark-Mixtrack-Pro-II-Mappings>
  - <https://github.com/snowyoneill/Mixxx-Numark-MixTrack-Pro-II-2016.midi>
