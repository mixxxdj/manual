# Numark Mixtrack (Pro) 3

[[/media/hardware/numark-mixtrack-pro-3.jpg|numark-mixtrack-pro-3.jpg]]

  - [Manufacturer's product
    page](http://www.numark.com/product/mixtrack-pro-3)
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=7286)
  - [Download mapping for
    Mixxx 2.0](http://mixxx.org/forums/viewtopic.php?f=7&t=7286&p=30932#p30932)
    (mapping is included in Mixxx 2.1)

The Numark Mixtrack 3 and Numark Mixtrack Pro 3 are the same controller
except that the Pro version has an integrated 4 channel output sound
card and costs $50 more. If you use the non-Pro version, you would need
a [splitter cable](hardware%20compatibility#splitter%20cables) or
[separate audio interface](hardware%20compatibility#audio%20interfaces1)
to be able to preview tracks in headphones.

The microphone input on the Pro version is not available to the computer
through the controller's sound card. It is mixed with the master output
in hardware, so this controller's sound card is not suitable for
broadcasting or recording the inputs. If you want to use the controller
for broadcasting or recording, getting the non-Pro version with a
separate [USB audio
interface](Hardware%20Compatibility#USB%20Audio%20Interfaces) with a
microphone input is suggested.

## Configuration options

Configuration options can be set in the mapping. You will need to edit
the values below at the very top of the JavaScript file
“Numark-Mixtrack-3-scripts.js” and save changes. Allowed values are
“**true**” or “**false**” unless specified.

  - **TrackEndWarning**: whether the Wheel button flashes near the end
    of a track
  - **iCutEnabled**: whether to enable iCut with the jog wheel. See
    [\#platter/jog wheel](#platter/jog%20wheel) section for details
  - **fastSeekEnabled**: whether to enable fast seeking with the jog
    wheel. See [\#platter/jog wheel](#platter/jog%20wheel) section for
    details
  - **smartPFL**: When the Load button is used, the Cue/PFL button is
    automatically activated on the deck being loaded and deactivated on
    the other deck
  - **beatlooprollActivate**: Use beatlooproll (slip mode loop) instead
    of beatloop command when using pads in Autoloop mode
  - **DarkMetalSkin**: Specify if Dark Metal skin is used for your
    installation. This is required in order for Expand Library feature
    to work properly. 
  - **FXMode**: Select FX Mode based on skin used:
    * value "**1**": (Deere skin): Each deck is assigned its own Effect Unit with 3 effects per deck (e.g. Deck 1 = Effect Unit 1, Deck 2 = Effect Unit 2, etc...\\
    * value "**2**": (other skins): FX button 1 = Effect Unit 1, Effect 1, FX Button 2 = Effect Unit 2, Effect 1,  FX button 3 = Effect Unit 3, Effect 1. Effect settings are shared by each deck.\\
  - **PitchBendOnWheelOff**: allow nudge with wheel when wheel is not active. 
  - **noPlayOnSyncDoublePress**: Specify if Play is disabled on Sync button Double Press. 
  - **ShiftFilterFX4**: Specify Shift+Filter control behavior - FX parameter 4 (true) or Channel Gain (false)

## Mapping Description

[[/media/numarkmixtrackpro3mapping.gif|]]

### 1\. Browser Knob

Rotate this knob to cycle through tracks in main library window. Press
the Knob to expand library view.  
**Shift + Turn:** allows selecting Play Lists and side navigation bar
items.  
**Shift + Push:** opens / closes selected side navigation bar item.

### 2\. Master Gain

Adjusts the master volume in the software.  
**Note**: This control does not affect the microphone volume which is
summed with the final output of the Master Gain to the Master Output.
Use the Mic Gain knob to control the microphone volume.

### 3\. Cue Mix

Adjusts the software’s audio output to the headphones, mixing between
the cue (PFL) output and the master mix output.

### 4\. Cue Gain

Adjusts the volume for headphone cueing in the software.

### 5\. Load

Press one of these buttons while a track is selected in the library
window to assign it to Deck 1 and 2, respectively, in the software.  
**Shift + Load:** Activates Fader Start mode for the corresponding (PFL
Button is then blinking). Fader start guide: In fader start mode, not
only you can press the play/pause button to play/pause the track, but if
you move up the level fader (the volume fader if you prefer) of the
deck, the track will be played and if you close it to zero, the track
will be paused.  
**Configurable option:**  
If the [smartPFL option](#configuration-options) is set to true, the
Cue/PFL button is automatically activated on the deck being loaded and
deactivated on the other deck.

### 6\. High EQ Knobs

Adjust High frequencies of the deck  
**Shift + High :** Adjust FX 1, parameter 1 of the Effect Unit assigned
to the deck  
**Padmode + high :** Adjust FX 2, parameter 1 of the Effect Unit
assigned to the deck  
**Tap + high :** Adjust FX 2, parameter 1 of the Effect Unit assigned to
the deck

### 7\. Mid EQ Knobs

Adjust Mid frequencies of the deck  
**Shift + Mid:** Adjust FX 1, parameter 2 of the Effect Unit assigned to
the deck  
**Padmode + Mid:** Adjust FX 2, parameter 2 of the Effect Unit assigned
to the deck  
**Tap + Mid:** Adjust FX 3, parameter 2 of the Effect Unit assigned to
the deck  

### 8 Low EQ Knobs

Adjust Low frequencies of the deck  
**Shift + Mid:** Adjust FX 1, parameter 3 of the Effect Unit assigned to
the deck  
**Padmode + Mid:** Adjust FX 2, parameter 3 of the Effect Unit assigned
to the deck  
**Tap + Mid:** Adjust FX 3 parameter 3 of the Effect Unit assigned to
the deck

### 9\. Filter

Adjusts the amount of the filter effect. Turning the knob left controls
the low pass filter; turning it right controls the high pass filter.  
**Shift + Filter:** Adjust FX 1, parameter 4 of the Effect Unit assigned
to the deck  
**Padmode + Filter:** Adjust FX 2, parameter 4 of the Effect Unit
assigned to the deck  
**Tap + Filter:** Adjust FX 3, parameter 4 of the Effect Unit assigned
to the deck

### 10\. Cue/PFL/Headphones

Sends pre-fader audio to the headphone output  
**SHIFT + press:** toggle slip mode  
**SHIFT + double press**: toggle quantize mode

### 11\. Volume fader

Adjusts the volume of the deck

### 12\. Crossfader

Controls the blend between the two decks

### 13-14. Pitch Bend Down/Up

Press and hold to momentarily reduce the speed of the track.  
**Shift+Pitch Bend Down/Up:** Jump 1 beat backward/forward

### 15\. Pitch Fader

Adjust the speed of the music (activate keylock to adjust tempo without
affecting pitch). Note that moving the fader down *increases* speed, as
marked by the "+" at the bottom of the fader on the controller. This can
be reversed in Mixxx's preferences under Interface \> Speed slider
direction

### 16\. Touch Strip

Use the Touch Strip to adjust the deck’s Effect Unit Superknob. If
Effects are assigned to Instant FX , they will be enabled instantly on
touch, and disabled on finger lift.  
**Shift + Touch Strip:** search through a track’s timeline

### 17\. Beats Multiplier

Adjusts the Dry/Wet mix of the deck’s Effect Unit  
**Shift + Beats:** Moves the beat grid left (turn counterclockwise) or
right (turn clockwise) **Padmode + Beats:** Adjust Sampler Volume. Left
beat knob will adjusts Samplers 1-4; Right knob will adjusts Samplers
5-8

### 18\. FX 1 On/Off

Enables FX 1 of the deck’s Effect Unit (Deck 1 = Unit 1, Deck 2 = Unit
2, Deck 3 = Unit 3, Deck 4 = Unit 4)  
**Shift + FX 1:** Select from the list of available effects for the
respective effect.  
**Padmode + FX 1:** Activates Brake effect  
**Tap + FX 1:** Assign / unassign FX 1 to Instant FX. When assigned to
Instant FX, the FX is instantly activated by touching the Strip and
stopped when finger is lifted.

### 19\. FX 2 On/Off

Enables FX 2 of the deck’s Effect Unit (Deck 1 = Unit 1, Deck 2 = Unit
2, Deck 3 = Unit 3, Deck 4 = Unit 4)  
**Shift + FX 2:** Select from the list of available effects for the
respective effect.  
**Padmode + FX 2:** Activates Spinback effect  
**Tap + FX 2:** Assign / unassign FX 1 to Instant FX. When assigned to
Instant FX, the FX is instantly activated by touching the Strip and
stopped when finger is lifted.

### 20\. FX 3 On/Off

Enables FX 3 of the deck’s Effect Unit (Deck 1 = Unit 1, Deck 2 = Unit
2, Deck 3 = Unit 3, Deck 4 = Unit 4)  
**Shift + FX 3:** Select from the list of available effects for the
respective effect.  
**Tap + FX 3:** Assign / unassign FX 1 to Instant FX. When assigned to
Instant FX, the FX is instantly activated by touching the Strip and
stopped when finger is lifted.

### 21\. Tap BPM

Press this 8 or more times on beat to manually enter a new BPM. The
software will ignore the track's BPM and follow your manually entered
tempo.  
**Shift + Tap:** Toggles deck between deck 1-3 (left side) or deck 2-4
(right side). TAP LED will be RED when deck 3 is active (Left Tap) or
deck 4 is active (Right Tap)

### 22\. Wheel button

Activate this button to use the platter/jog wheel to grab and move the
audio, scratching the track like a vinyl record.

### 23\. Platter/Jog Wheel

**Touch side:** Pitch bend (nudging) if track is playing (Wheel On
(always) & Wheel Off - if [PitchBendOnWheelOff](#configuration-options)
configuration option is true) and / track positioning (Wheel On)  
**Wheel On + Touch platter:** scratching: touch the platter and move
it  
**Shift + Wheel On + Touch platter**: iCut mode: simulates a scratch
routine with the jog wheel. When the jog wheel is turned back, the
crossfader closes; when the jog wheel is turned forward the crossfader
will open. As a visual reference, TAP LED and Wheel button LED will be
ON.  
**Wheel Button Off + Touch platter**: If track is not playing, allows
positionning the track  
**Shift + Wheel Off + Touch platter**: fast seek through track

**Configuration Options:** The [iCutEnabled](#configuration-options) and
[fastSeekEnabled](#configuration-options) options can be used to turn
off iCut and fast seeking. These options may be helpful to avoid
accidentally using these features when touching the platter with shift
lock on.

### 24\. Shift

Allows multiple control commands to be triggered when pressed first
along with other buttons  
**Single Press** : Temporary SHIFT  
**Double press** (like a double click): SHIFT Lock enabled (TAP LED will
remain ON if Shift Lock is enabled)  
**Press and release**: toggle off SHIFT Lock if enabled

### 25\. Pad Mode

This is used to change the operation mode of the [top 4 performance
pads](#29.-Performance-Pads). Pressing this button will light the pad
indicating the currently active mode (Manual Loop, Auto Loop or
Sampler).

### 26\. Sync

Enables BPM syncing between decks.  
**Short Press:** Press once to synchronize the tempo (BPM) to that of to
that of the other track  
**Double Press:** press twice QUICKLY to play the track immediately
synchronized to the tempo (BPM) and to the phase of the other track, if
the track was paused  
**Long Press** (Sync Lock): Hold for at least half of a second to enable
sync lock for this deck. Decks with sync locked will all play at the
same tempo, and decks that also have quantize enabled will always have
their beats lined up. If the Sync Lock was previously activated, it just
deactivates it regardless of the Short press/Double Press  
**Shift + Sync:** Toggle Key Lock

**Configuration Options:** The
[noPlayOnSyncDoublePress](#configuration-options) option can be used to
turn off Play on Sync Double Press.

### 27\. Cue (Transport Control)

Behavior depends on the [cue
mode](http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes)
set in the Mixxx preferences.  
**Shift + Cue:** return the play head to the start of the track.

### 28\. Play/Pause

Starts and suspends playback. If no track is loaded, loads the selected
track (if any) and play.  
**Shift + Play/Pause:** stutter the track from the last set cue point.
If a cue point has not been set, the play head will return to the start
of the track.

### 29\. Performance Pads

The top row of pads is for controlling loops and samples. To select a
mode, hold down the Pad Mode button and press one of the upper pads. An
LED under the pad section indicates the currently selected mode. See the
subsections below for details about each mode.

The bottom row of pads is used to trigger hotcue points. If a hotcue
point has not already been set for the loaded track, this control will
mark the hotcue point. If a hotcue point has already been set, this
control will jump to it.  
**Shift + Hot Cue**: Deletes the assigned hotcue point

#### Manual Loop Mode

Hold Pad Mode and press the pad marked Manual Loop (silkscreened above
the pad) to assign the lower 4 pads to the functions listed below:  

  - **Loop In** – Sets the beginning of a loop: When assigned, the Pad
    LED will light blue  
  - **Loop Out** – Sets the end point for the loop: When assigned, the
    Pad LED will light blue  
  - **On/Off** – (De)activate the loop. If a loop has not been set, this
    button will have no effect.: When assigned, the Pad LED will light
    blue  
  - **Loop x1/2** – Halve the length of the loop. Press Shift + Loop
    x1/2 to double the length of the loop.  

#### Auto Loop Mode

Hold Pad Mode and press the pad marked Autoloop to assign the lower 4
pads to the functions listed below: When assigned, the respective Pad
LED will blink Yellow  
\* **Auto 1** – Sets and starts playback of a 2-beat autoloop.  

  - **Auto 2** – Sets and starts playback of a 4-beat autoloop.  
  - **Auto 3** – Sets and starts playback of a 8-beat autoloop.  
  - **Auto 4** – Sets and starts playback of a 16-beat autoloop.  
    \* **Shift + Auto 1** – Sets and starts playback of a 1/8-beat
    autoloop.  
  - **Shift + Auto 2** – Sets and starts playback of a 1/4-beat
    autoloop.  
  - **Shift + Auto 3** – Sets and starts playback of a 1/2-beat
    autoloop.  
  - **Shift + Auto 4** – Sets and starts playback of a 1-beat
    autoloop.  

If the pad is held down more than .5 second (Long Press), the Autoloop
will be disabled once pad is released. On Short Press, the pad will
behave as a normal button (ON on first press, OFF on second press)

#### Sample Mode

Hold Pad Mode and press the pad marked Sampler to assign the lower 4
pads to the functions listed below. When assigned, the respective Pad
LED will blink Purple  
Shift + Sample X will play loaded sample, but with Sampler unit Sync
disabled  

  - **Deck 1 - Sample 1** – Plays the sample assigned to Sample Pad 1
    with the unit Sync activated.  
  - **Deck 1 - Sample 2** – Plays the sample assigned to Sample Pad 2
    with the unit Sync activated.  
  - **Deck 1 - Sample 3** – Plays the sample assigned to Sample Pad 3
    with the unit Sync activated.  
  - **Deck 1 - Sample 4** – Plays the sample assigned to Sample Pad 4
    with the unit Sync activated.  
  - **Deck 2 - Sample 1** – Plays the sample assigned to Sample Pad 5
    with the unit Sync activated.  
  - **Deck 2 - Sample 2** – Plays the sample assigned to Sample Pad 6
    with the unit Sync activated.  
    \* **Deck 2 - Sample 3** – Plays the sample assigned to Sample Pad 7
    with the unit Sync activated.  
    \* **Deck 2 - Sample 4** – Plays the sample assigned to Sample Pad 8
    with the unit Sync activated.  

If the pad is held down more than .5 second (Long Press), the sampler
will be disabled once pad is released. On Short Press, the pad will
behave as a normal button (ON on first press, OFF on second press)

### 30\. Master Output LEDs

Displays the audio level going to the Master Output.

## Changes in Mixxx 2.1

This set of changes is implemented in development versions of Mixxx 2.1
available from the [build
server](http://downloads.mixxx.org/builds/master/release/).

#### Configuration options

Some configuration options that exist in 2.0 are no longer available in
2.1. Version 2.1 supports the following options:


#### Effects

  - Focus effect with **FX button**
  - Toggle effect with **Tap + FX button**
  - Move mapping of InstantFX to **Padmode + FX button**
  - **Shift + High** controls parameter 1 of focused effect
  - **Shift + Mid** controls parameter 2 of focused effect
  - **Shift + Low** controls parameter 3 of focused effect
  - **Shift + Filter** controls parameter 4 of focused effect

If no effects are focused, the super knob of the effect rack is
controlled by the touch strip. If an effect is focused, the touch strip
controls the meta knob of the focused effect. If any effects are added
to InstantFX, they are turned on when the touch strip is activated, and
off when it is not. While active, the meta knobs associated with effects
with InstantFX enabled are controlled by the touch strip.

#### Sampler changes

  - Load sample by selecting track and pressing **Sample X**
  - Pressing sample button when sample is already playing goes back to
    cue and plays
  - Shift + sample to stop sample
  - Eject sample by **Tap + Sample X**

#### Beat jump

  - Adjust beatjump amount with **Shift + Beats knob**
  - Beatjump with **Shift + Pitch Bend +/-**. If loop is activated, move
    loop by beatjump amount instead.

#### Manual Loop Mode

  - Starting with
    [commit 2c129ea0af838543b987d55538b903e115f08ba5](https://github.com/mixxxdj/mixxx/commit/2c129ea0af838543b987d55538b903e115f08ba5),
    the Loop x1/2 button is disabled unless the corresponding deck is
    set to be quantized

#### Others

  - Move slip mode to **Shift + Wheel**
  - Move quantize toggle to **Shift + PFL** (single press)
  - Move beat grid alignment to **Tap + Beats knob**
