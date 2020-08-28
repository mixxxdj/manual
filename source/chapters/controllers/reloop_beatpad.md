# Reloop Beatpad

[[/media/hardware/reloop/reloopbeatpadtp.png|]]

  - [Manufacturer's product page](http://www.reloop.com/reloop-beatpad)
  - [Forum thread : mapping to download, users feedback, installation
    notes](http://www.mixxx.org/forums/viewtopic.php?f=7&t=7581)

The **Reloop Beatpad** is a conventional 2 channel controller that is
primarily designed to work with algoriddim‘s djay on the iOS platform
and more recently on the Android platform, but can also be used with
Mixxx by sending MIDI signals to a computer with a USB cable.


## MIXER SECTION

### Crossfader

Blends audio between left and right mixer channels.

### Volume Faders

Adjust the Volume of each channel. If [Fader
Start](#1-and-2-\(Track-select-buttons\)) is enabled the deck will stop
at the previously used Cue if the Volume Fader reaches the minimum
position and will start playing if the Volume fader moves from the
minimum position.

### 1 and 2 (Track select buttons)

  - **Load a track:** Press these buttons to load the selected track
    from the Browser to left or right deck. The LED of the button will
    be on if the deck is loaded. 
  - **Eject:** Hold the same button for more than half of a second to
    unload the same deck.
  - **Fader Start:** Hold **[SHIFT](#SHIFT)** down and then press one of
    these buttons to enable the **Fader Start** on a deck. The LED of
    the button will blink if Fader Start is enabled. If Fader Start is
    enabled the deck will stop at the previously used Cue if the Volume
    Fader reaches the minimum position and will start playing if the
    Volume fader moves from the minimum position.

### PFL (symbolized by a headphone)

  - \*\*PFL: \*\*Press these buttons to send each channel to the
    Headphones Output channel for pre-listening.
  - \*\*Slip mode: \*\*Hold **[SHIFT](#shift)** down and then press
    these buttons to activate/desactivate Slip Mode. When active, the
    playback continues muted in the background during a loop, scratch
    etc. Once disabled, the audible playback will resume where the track
    would have been.
  - **Quantize mode:** Hold **[SHIFT](#shift)** down and then press
    these buttons to activate/desactivate the Quantize mode. When
    active, it aligns Hot-cues and Loops to the next beat from the
    current position.

### Equalizer

  - **LOW:** Adjust the Low (Bass) frequencies for each mixer channel.
  - **MID:** Adjust the Mid frequencies for each mixer channel.
  - **HIGH:** Adjust the High (Treble) frequencies for each mixer
    channel.
  - **GAIN:** Adjust the Gain of each mixer channel.
  - **MASTER:** Adjust the level of the Master Output.
  - **Cue Mix (Hadphones mixing):** Adjust how the Channels and the
    Master Output blend at the Headphones Channel.
  - **Phones (Hadphones level):** Adjust the Volume Output of the
    Headphones Channel.
  - **AUX:** Adjust the Volume of the AUX Input.

The MASTER, Phones, and AUX knobs adjust the levels of the Beatpad's
sound card; they do not control the software gains in Mixxx so the
changes are not visible on screen.

### REC

  - **Record:** Use this button to start/stop recording your mixing
    session.
  - **End track warning:** Hold **[SHIFT](#SHIFT)** down and then press
    this button in order to toggle **on** or **off** the red flashing of
    the **[jog wheels](#JOGWHEEL)** when the playback reaches the end of
    the track.

### Browse Knob

Scroll through your library.

  - **Turn** to select a track in the song list.
  - **Push** to load the selected track into first stop deck.
  - **[SHIFT](#shift)+Turn** to select a folder or subfolder in the left
    item list sidebar.
  - **[SHIFT](#shift)+Push** to open/close folders and subfolders in the
    left item list sidebar.

## DECK CONTROLS SECTION

### SHIFT

Press and hold one of those buttons to access secondary functions of
other controls on the Beatpad. The secondary functions can be accessed
while the **SHIFT** button is held down. If the **SHIFT LOCK** switch on
the back side of the Reloop Beatpad is on, the secondary functions can
be accessed after the button **SHIFT** button is released and until the
**SHIFT** is pressed again.

### PLAY/PAUSE

  - **Play/pause:** Press to play/pause the track. If there was no track
    loaded into the deck and a track is selected in the library, it is
    loaded and starts playing.
  - **Censor:** Hold **[SHIFT](#shift)** down and then press this button
    to play the track in reverse. When released the track will continue
    to play from the position it would have been if the button was never
    pressed. In other words, it enables reverse and slip mode while
    held.

### JUMP

  - **While playing, or stopped:** If the Cue point is set, seeks the
    player to it and starts playback.
  - **Brake:** Hold **[SHIFT](#shift)** down and then press this button
    to stop the track with a gradual brake. If the **JUMP** button is
    released before the track has completely stopped, the track is then
    played back to its regular speed.
  - **Spinback:** see the **[Instant FX](#Instant-fx)** usage.

### SET

  - **While playing:** Seeks the track to the cue-point and stops.
  - **While stopped:** Sets the cue point (Pioneer/Mixxx mode) OR
    preview from it (Denon mode).  
    If the Cue point is already set at the current position of the
    track, hold this button to play the track and release it to return
    to the Cue point and pause it. To continue playback without
    returning to the Cue Point, press and hold the **SET** Button, then
    press and hold the **[Play/Pause](#Play/Pause)** Button and then
    release both buttons.
  - **Hint:** Change the default cue mode in Preferences -\> Interface.
    The Pioneer mode is the more consistent with the Reloop Beatpad. 
  - **Key lock:** Hold **[SHIFT](#shift)** down and then press this
    button to enable/disable the Key-lock.

### SYNC

  - **Press once** to synchronize the tempo (BPM) and phase to that of
    the other track.
  - **Press twice quickly** to play the track immediatly, synchronized
    to the tempo (BPM) and to the phase of the other track, if the track
    was paused.
  - **Sync Lock:** Hold for at least half of a second to enable **sync
    lock** for this deck. Decks with sync locked will all play at the
    same tempo, and decks that also have **quantize** enabled (wich is
    enabled by default by the mapping) will always have their beats
    lined up.  
    **Note :** the **quantize** mode is not mapped on the controller but
    can be enabled/desabled from Mixxx.

### JOGWHEEL

Touch sensitive platters for scratching (Scratch mode/iCut mode),
bending (Scratch mode/CD mode) or Seek mode.  
The jogwheel offers multi-color leds, which will show the playing marker
(Scratch mode), the song progress bar (in Seek mode), and other colored
combinations depending on the applied effect, loop, loop roll or Filter.
If no track is loaded, the jogwheel displays a red cross. At the end of
a track, the jogwheel is flashing red faster and faster until it reaches
the end of the track (full steady red).  
You can toggle on/off this behavior with
**[SHIFT](#shift)+[REC](#rec)**.

#### Scratch mode

Toggle with the **JOG SCRATCH** button.  
Use the jogwheel to scratch and the outer ring to bend (like in [CD
mode](#CD-mode)).

  - **iCut mode:** Hold **[SHIFT](#shift)** down and scratch to scratch
    in "automagic" scratch mode. When the jog wheel is turned back, the
    crossfader is closed. When the jog wheel is turned forward, the
    crossfader opens. (Note that the Algoriddim djay mapping actually
    closes/opens the crossfader quickly without taking into account the
    direction of the wheel, contrary to what the Beatpad's Quick Start
    guide says.)  

#### Seek mode

Toggle with the **JOG SEEK** button.  
Use the jogwheel to navigate through the track.

#### CD mode

Deactivate both the **[Scratch mode](#Scratch-mode)** and the **[Seek
mode](#Seek-mode)** to enable this mode.  
Use the jogwheel to temporarily bend the pitch of the track (which only
affects the tempo with keylock on).

### PITCH BEND

  - **Pitch bend:** Use these buttons temporary slow-down/speed up the
    tempo of the track.  
    Once the buttons are released the track will continue to play at the
    tempo designated by the pitch fader.
  - \*\*Beat Jump: \*\*Hold **[SHIFT](#shift)** down and then use these
    buttons to jump 1 beat backwards or forward.

### PITCH

Controls the track's pitch. With keylock on, this only changes the
tempo. The red LED indicates that the pitch fader of the unit is on zero
(center) position.

## LOOPS SECTION

(see also **[Bounce Loop (Roll) mode](#Bounce-Loop-\(Roll\)-mode)**
section)

  - **Loop size:** Turn the encoder to select the number of beats for a
    loop. Turn it counterclockwise to half the size of the loop and
    clockwise to double it.
  - **Loop move:** Hold **[SHIFT](#shift)** down and then use the
    encoder to move the triggered loop forward or backwards by 1 beat.
  - **Activate/deactivate:** (Acts exactly like the **[LOOP](#loop)**
    Button)
  - **Regular loop mode:** Push (and release) the encoder to trigger a
    loop of the selected size
  - **Roll loop mode:** Press (and hold down) to trigger a momentary
    rolling loop of the selected size. While the encoder is held down,
    the track will keep moving forward as if it was not looping, so when
    the encoder is released, it will jump forward to where the track
    would have been if the rolling loop was never enabled. In other
    words, this is a regular loop in **[slip
    mode](#PFL-\(symbolized-by-a-headphone\))** (see
    **[PFL](#PFL-\(symbolized-by-a-headphone\))** section).
  - **Toggle loop mode:** Hold **[SHIFT](#shift)** down and then push
    the encoder to toggle between Regular and Roll Loop mode.

## EFFECTS SECTION

(see also **[Instant FX mode](#Instant-FX-mode)** and **[Sampler
mode](#Sampler-mode)** sections)

#### FX ON

Push (and release) this button to trigger the selected effect chain for
the corresponding deck (toggle function).

#### FX SELECT

  - **Select:** Use this encoder to select an effect for the current
    selected rack. 
  - **Temporary effect:** Push and hold the encoder to temporarily apply
    the effect of the current selected rack for the corresponding deck
    (while pressed).
  - **Quick Effect:** Hold **[SHIFT](#​shift)** down and then push the
    encoder Activate or Kill the **Quick Effect**. You can change the
    Quick effect assigned in Mixxx, via Options -\> Settings-\>​
    Equalizers -\> Quick Effect.

#### FX PARAM

  - **SUPER:** Use this knob to control the **SUPER** parameter of the
    effect for the current selected rack.
  - **MIX:** Hold **[SHIFT](#​shift)** down and then use this knob to
    control the **MIX** parameter of the effect for the current selected
    rack.

#### FILTER

  - **Quick Effect:** Use this knob to apply the Quick effect (by
    default, this is Filter, but you can change it) to the deck. In
    middle position no effect is applied for filter.
  - **Key:** Hold SHIFT down and use this knob to adjust the key (pitch)
    of the track without changing the tempo. In middle position the
    track will have its original key.

## PADS SECTION

The 4 Performance Pads offer 4 different modes, depending on the 4 PAD
MODE buttons just above.

### HotCues mode

#### CUE

Press the **CUE** mode button to set the PADs to HOT CUE mode.

#### Pads

  - **Press** each one of the 4 pads to assign a Hot Cue Point (1 to 4)
    or returns the track to that Hot Cue Point. When a Hot Cue Button is
    unlit, you can assign a Hot Cue Point by pressing it at the desired
    point in your track. Once it is assigned, the Hot Cue Button will
    light up blue.
  - **[SHIFT](#SHIFT)+Press** to delete its assigned Hot Cue Point.

### Bounce Loop (Roll) mode

#### BOUNCE LOOP

Press the **BOUNCE LOOP** mode button to set the PADs to Loop Roll mode.

#### Pads

Press (and keep down) any of the 4 pads to trigger a momentary **[Loop
Roll](#Good-to-know-for-beginners)** of a different size (in beats) as
per the table.

|                       |      |     |     |    |
| --------------------- | ---- | --- | --- | -- |
|                       | Pads |     |     |    |
| :::                   | 1    | 2   | 3   | 4  |
| Press                 | 1/8  | 1/4 | 1/2 | 1  |
| [SHIFT](#shift)+Press | 2    | 4   | 8   | 16 |

Once the PAD is released the track will continue to play from the
position it would have been if the Loop Roll was never triggered. The
size of the applied Loop Roll can be adjusted with the **[LOOP
SIZE](#LOOP-SIZE)** encoder as well. Pads change the "selected loop
size" introduced in **[LOOP SIZE](#LOOP-SIZE)** and **[LOOP](#LOOP)**
sections.

### Instant FX mode

#### Instant FX

  - **Press** this button to set the PADs to Effects mode.
  - **Spinback:** Hold **[SHIFT](#shift)** down and then press this
    button down in order to stop the track with a backward brake effect.
    If the **[Instant FX](#Instant-fx)** button is released before the
    track has completely stopped, the track is then played back to its
    regular speed, in the forward direction.
  - **Brake :** see **[JUMP](#jump)** button usage

#### Pads

  - **Instant FX:** Press (and keep down) any of the 4 pads to apply
    momentarily the effect of the corresponding effect rack. The
    parameters of these effects can be adjusted from the **[FX
    PARAM](#FX-PARAM)** knob.
  - **Current effect rack selection:** Hold **[SHIFT](#shift)** down and
    then press any of the 4 pads to select the current effect rack for
    this deck that will be used for effect selection or for the
    corresponding effect to be triggered later on (see **[EFFECTS
    SECTION](#EFFECTS-SECTION)**).  
    this can also be done with a visual feedback in **[Sampler
    mode](#Sampler-mode)** 

### Sampler mode

**Note:** On account of the Reloop Beatpad limitations (bug ?), lights
will not show on in Sampler mode when the controller is in
**[SHIFT](#shift)** mode.

Press the SAMPLER mode button to set the PADs to cycle between 4 sub
modes:

``` 
 - **Sampler mode** (orange LEDs): each pad triggers a sample from the selected Sampler bank. The PADs wich are lit indicate which samples are loaded and ready to use. While a sample is playing, the corresponding PAD changes its color to pink.
 - **Sampler bank selection mode** (pink LED): each pad selects 1 of the 4 sampler banks. The PAD wich is lit indicates wich bank is active.
 - **Loop mode** status and selection (magenta LEDs): press any pad to toggle between **[[#LOOPS-SECTION|regular loop mode]]** and **[[#LOOPS-SECTION|roll loop mode]]**.\\ **Regular loop mode** is symbolized by the left PAD lit, representing the loop), and all the others switched off. **Roll loop mode** is symbolized by both the left (representing the loop) and the right PADs lit (symbolizing the position after the loop where the track will continue to play when the loop will be triggered off).
 - **Effect rack selection** mode (purple LED): each pads selects 1 of the 4 effect racks. The PAD which is lit indicates which effect rack is active (see **[[#EFFECTS-SECTION|EFFECTS SECTION]]**).
```

## TIPS & TRICKS Guide

(work in progress) This section exposes several issues wih the Reloop
Beatpad and ways, when it's possible, to correct them


### Grounding problem

If your controller randomly freezes or your iPad or Android tablet acts
weirdly (screen flashing, bad sound), [make a home made, grounded power
cable](http://support.reloopdj.com/beatpad/otg-cable-missing-in-my-box-any-otg/).

### Controller not detected by Windows

If you see a yellow exclamation point (\!) in the Windows Device Manager
indicating that the drivers did not start, unplug the power cable from
your laptop then unplug/replug the USB cable from your controller. If
that does not work, restart your laptop without the power cable plugged
in.

### No sound with your Android tablet or smartphone

Unfortunately, Android does not have good support for low latency audio
or USB sound cards. OS support for USB audio was only recently added to
Android version 5.0 (Lollipop). Prior to Android 5.0, some applications
provided their own driver for USB sound cards. On any version of
Android, to use USB sound cards like the one in the Beatpad, the device
has to support USB On-The-Go (OTG) and you need to use an OTG adapter
cable to plug in your device. Not all Android devices support OTG. See
[here](http://support.reloopdj.com/beatpad/android-device-compatibility-list/)
for compatibility information about various Android devices.

If you have trouble using your Beatpad's sound card with Android, you
could also use a [DJ splitter
cable](hardware%20compatibility#splitter%20cable) with the onboard sound
card on your smartphone or tablet.

### Freeze/crash/abnormal behavior with your Android tablet/smartphone

It may be that your Android device does not provide enough power through
the USB cable. If so, use a powered USB hub between your Android device
and your Beatpad. The connections would be:

`Android tablet/phone --- OTG cable --- powered USB hub --- USB cable
--- Beatpad`

If that does not work, you may have a [\#grounding
problem](#grounding%20problem).
