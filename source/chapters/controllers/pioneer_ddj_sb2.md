# Pioneer DDJ-SB2

[[/media/hardware/pioneer-ddj-sb2_1.jpg|]]

``` 
 *[[http://www.pioneerdj.com/en/product/controller/ddj-sb2/black/overview/|Manufacturer's product page]]
 *[[http://mixxx.org/forums/viewtopic.php?f=7&t=7509&p=26782#p26782|Forum thread]]
 *[[https://github.com/dg3nec/mixxx/tree/DDJ-SB2/res/controllers]]
```

The Pioneer DDJ-SB2 is an all-in-one USB MIDI controller with a built in
sound card. It has controls for 2 decks that can be toggled between
decks to play with 4 decks. It is compatible with Mixxx since version
2.0.

The sound card has 2 RCA jacks for the main output. There are two
headphone jacks, one small (1/8") and one large (1/4") connector (each
jack plays the same channels, they cannot be used for independent
signals). There is a 1/4" microphone input with an adjustable gain knob.
The microphone input is mixed directly with the main RCA outputs in
hardware. It is not available to the computer, so cannot record or
broadcast with the microphone input on the controller. You could use the
controller with a separate [USB Sound
Card](Hardware%20Compatibility#USB%20Sound%20Cards) that has a
microphone input for that purpose. The microphone preamplifier is very
noisy, so it is recommended to keep the microphone gain knob all the way
down when not using a microphone, otherwise there will be noise added to
the main RCA outputs.

## Compatibility

### Windows

Pioneer has a
[driver](https://www.pioneerdj.com/en/support/software/ddj-sb2/#drivers)
for Windows versions 7 and newer. Select the ASIO sound API in Mixxx's
Sound Hardware Preferences.

### Mac OS X & Linux

The DDJ-SB2 is a USB class compliant MIDI and audio device, so it works
with Mac OS X and Linux without any special drivers.

## User Options

There are some user configurable options for this mapping. To change the
options, open the .js file in your [controller mapping file
locations\#user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder)
for your Pioneer DDJ-SB2 with a text editor such as KWrite or GEdit on
GNU/Linux, Notepad on Windows, or TextEdit on Mac OS X.

  - **blinkingSync**: If true the sync button blinks with the beat, if
    false led is lit when sync is enabled.
  - **invertVinylSlipButton**: If true, the vinyl button activates slip.
    Vinyl mode is then activated by using shift. Allows toggling slip
    faster, but is counterintuitive.
  - **jogwheelSensivity**: Sets the jogwheels sensivity. 1 is default, 2
    is twice as sensitive, 0.5 is half as sensitive.
  - **jogwheelShiftMultiplier**: Sets how much more sensitive the
    jogwheels get when holding shift. Set to 1 to disable jogwheel
    sensitivity increase when holding shift.
  - **speedRateToNormalTime**: Time per step (in ms) for pitch speed
    fade to normal
  - **showVumeterMaster**: If true Level-Meter shows VU-Master left &
    right. If false shows level of channel: 1/3 2/4 (depending active
    deck)
  - **cutVumeter**: Cut's Level-Meter low and expand upper. Fore
    example, at 0.5 only signals greater 50% show on the meter, expanded
    to full range
  - **twinkleVumeterAutodjOn**: If true VU-Level twinkle if AutoDJ is
    ON.
  - **jumpPreviewEnabled**: If true, when releasing the browser knob,
    the preview deck jumps forward to "position". 
  - **jumpPreviewPosition**: The place in the track to jump to, on a
    scale from 0 (beginning of track) to 1 (end of track).

## Usage

### Library browsing

The controls for library browsing can be found in the center top of the
controller.

| Control                                  | Function                                                           |
| ---------------------------------------- | ------------------------------------------------------------------ |
| Rotary knob                              | Track selection                                                    |
| Load buttons                             | Loads currently highlighted track to the corresponding deck        |
| Pushing rotary knob                      | Loads currently highlighted track to the preview deck and plays it |
| Pushing rotary knob again without rotate | Stop the preview deck                                              |
| Shift + rotary knob                      | Library section selection (scroll through left pane of library)    |
| Shift + pushing rotary knob              | Toggle expanding library section                                   |

Pushing the rotary knob to start playing a track in the preview deck
then releasing it jumps forward in the preview deck. This behavior can
be disabled in the mapping's user options and the place in the track it
jumps to can also be configured.

Addition functions not belonging to library:

  - Shift & load left -\> toggle effects view in/out
  - Shift & load right -\> toggle sampler view in/out

### Switching between decks

Press the deck button. It lights when deck 3-4 is active.

### Volume, equalizers & filters

Between the decks the usual faders, crossfader and EQ knobs can be
found. A filter knob is also available.

Knobs are available for the master and headphones level. These control
the controller's built in sound card; they do not control the software
gains in Mixxx, so moving them does not move the master and headphone
gain knobs on screen.

The filter fade button changes the crossfader from fading the volumes
between decks to using filters to fade between decks.

The TRIM knob controls the deck's gain.

### Jogwheels, tempo & vinyl mode

When a deck is paused, the jogwheel allows you to browse through a
track. If you want to browse faster, hold shift while using the
jogwheel.

When a deck is playing, using the jogwheel allows you to temporarily
change the tempo of the playing track. Again, holding shift exaggerates
this effect.

The tempo slider allows changing the tempo of each deck. This normally
changes the pitch of a track, but you can make the pitch stay constant
by pressing the "key lock / tempo range" button. Additionally, with
shift, the "key lock / tempo range" will fade the tempo slowly to 0. The
fading speed can be customized with the speedRateToNormalTime mapping
option.

Vinyl mode makes the jogwheels emulate the way turntables work. Vinyl
mode can be toggled by pressing the "vinyl / slip" button. Touching the
outer plastic ring of the jogwheel will temporarily change the tempo
like when vinyl mode is off. Touching the metal disc simulates touching
the vinyl record, so just putting your hand on it will stop the "vinyl".
You can scratch in a similar way as with turntables in vinyl mode.

### Slip mode

By pressing shift + "vinyl / slip" you can toggle slip mode. When
entering slip mode, Mixxx remembers what point exactly of the track
should be playing even if, for example, you scratch or make a loop. When
you press shift + slip again, Mixxx will jump back to that point.

### Pads - lower row

The play and cue pads should be self-explaining. The sync pad toggles
master sync for a deck, which tries to beatmatch the deck with the
others, and also syncs the tempo between them, even when the tempo of
one deck is changed. Refer to the Mixxx manual for how to use master
sync.

Additional functions can be accessed by holding shift

| Control      | Function                                                                                                               |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Shift + play | Plays the track in reverse and enables slipping (see slip mode)                                                        |
| Shift + cue  | Brakes the track as if the power of the motor on a turntable was turned off                                            |
| Shift + sync | Enables quantize mode (this makes most actions, e.g. pressing play or setting the cue point, fall to the nearest beat) |

### Pads - hot cue mode

In hot cue mode the upper row of pads control the hotcues. Pressing a
pad that is not lit sets a hotcue. Pressing a pad that is lit makes the
track jump and play from that hotcue. Pressing a pad while holding shift
deletes that hotcue.

You can control a set of 4 more hotcues by pressing shift + hot cue. The
hot cue button will start blinking. The pads will behave in the same
way, but controlling hotcues 5 to 8.

### Pads - auto loop mode

Pressing the pads in auto loop mode will make loops of a specific length
measured in beats.

| Control       | Function                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------- |
| Pad 1         | set a loop of the selected number of beats                                                                      |
| Pad 2         | halve the selected loop length                                                                                  |
| Pad 3         | double the selected loop length                                                                                 |
| Pad 4         | reloop (reactivate a pre-existing loop)                                                                         |
| Shift + pad 1 | set a rolling loop of the selected number of beats                                                              |
| Shift + pad 2 | beatjump backwards by the beatjump size, or move the loop backwards by the beatjump size if the loop is enabled |
| Shift + pad 3 | beatjump forwards by the beatjump size, or move the loop forwards by the beatjump size if the loop is enabled   |
| Shift + pad 4 | enable loop, jump to loop in marker, and stop playback                                                          |

### Pads - manual loop mode

This mode allows you to set loops different from the fixed lengths of
beats in auto loop mode.

| Control       | Function                    |
| ------------- | --------------------------- |
| Pad 1         | Set loop in                 |
| Pad 2         | Set loop out                |
| Pad 3         | Toggles loop                |
| Pad 4         | Halve loop length           |
| Shift + pad 4 | Double loop length          |
| Shift + pad 1 | Move loop one beat backward |
| Shift + pad 2 | Move loop one beat forward  |

### Pads - sampler mode

In sampler mode the sampler can be controlled. To load a file into a
sampler, first press the sampler button while holding shift, so that the
sampler button starts blinking. Now pressing a pad will load the
currently highlighted track on the library into the corresponding
sampler. Pressing a pad while holding shift will eject the sample.

To play samples, press the sampler button without holding shift (it
should not blink). Pressing a pad will start playing the corresponding
sample, pressing a pad while holding shift will stop it.

### Pads - loop roll (shift + auto loop)

By pressing the auto loop button while holding shift (it should start
blinking) you can make loop rolls. This mode combines auto loops with
slip mode. The pads will start a loop in the current position with a
determinate beat length while simultaneously enabling slip mode, so that
when releasing the pad the track will continue playing as if the loop
never happened.

| Control       | Function              |
| ------------- | --------------------- |
| Pad 1         | 1/16th beat loop roll |
| Pad 2         | 1/8th beat loop roll  |
| Pad 3         | 1/4th beat loop roll  |
| Pad 4         | 1/2 beat loop roll    |
| Shift + pad 1 | 1 beat loop roll      |
| Shift + pad 2 | 2 beat loop roll      |
| Shift + pad 3 | 4 beat loop roll      |
| Shift + pad 4 | 8 beat loop roll      |

### Pads - kill (shift + manual loop)

By pressing the manual loop button while holding shift (it should start
blinking) you can make the pads behave as EQ kill switches.

| Control | Function  |
| ------- | --------- |
| Pad 1   | Kill low  |
| Pad 2   | Kill mid  |
| Pad 3   | Kill high |
| Pad 4   | Mute      |

### Effects

The knob controls the dry/wet knob of the whole effect chain when no
effect is focused. When an effect is focused, the knob controls the
metaknob of the focused effect. Focus an effect by pressing one of the
effect buttons. To switch the controller's knob back to manipulating the
dry/wet knob, unfocus by pressing the button of the focused effect
again.

Press and hold an effect button to toggle the enable switch for that
effect. The enable switches for each effect are not shown on the
controller's LEDs, so you need to look at the screen to check whether an
effect is on. All effects are off when Mixxx starts.

Use shift and the mixer knobs to control the parameters of the focused
effect. The trim knob controls parameter 1, the equalizer knobs control
parameters 2-4, and the filter knob controls parameter 5.

The DDJ-SB2 does not have enough buttons to control assigning effect
units to different decks. You may want to set up a [custom keyboard
mapping](https://mixxx.org/manual/latest/chapters/advanced_topics.html#making-a-custom-keyboard-mapping)
to have easy access to those switches. Otherwise, you can use your mouse
to click the buttons on screen.

### Auto DJ

Start/stop Auto DJ: Shift + DECK 4. If enabled in the user options
enabled, the level meter LEDs twinkle.

Skip Track: Shift + DECK 3

### Channel fader start

By moving a channel fader up from the very bottom while holding shift
when a deck is paused, the deck will start playing. Moving the fader
back to the bottom without releasing shift stops the deck and moves it
back to its original position.
