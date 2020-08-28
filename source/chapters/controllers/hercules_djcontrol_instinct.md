# Hercules DJ Control Instinct (S)

[[/media/hardware/Hercules-DJ-Control-Instinct.png|Hercules-DJ-Control-Instinct.png]]
[[/media/hardware/instincts.jpg|instincts.jpg]]

  - Manufacturer's product pages: [DJ Control Instinct
    S](http://www.hercules.com/us/leisure-controllers/bdd/p/248/djcontrol-instinct-s-series/)
    and [DJ Control
    Instinct](http://www.hercules.com/us/DJ-Music/bdd/p/187/djcontrol-instinct/)
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=3907)

This is the cheapest all-in-one controller with an integrated sound
card. The DJ Control Instinct S is functionally identical to the DJ
Control Instinct, but has a brushed stainless finish.

## Setup

The controller is a class compliant MIDI controller, so you should be
able to just plug it in and it should be recognized in Mixxx. No need
for drivers.

Make sure to select the correct preset for the controller and enable it.

### Audio Channels

There are two outputs on the controller itself: the headphones output
with builtin volume control on the side facing you and the speakers
output.

In Mixxx the headphones output is on channels 3 and 4, so select the
"Channels 3-4" item to get stereo output. The speakers output is on
channels 1 and 2, so to get stereo output you want to select the
"Channels 1-2" item.

## Controls

[[/media/hardware/hercules_dj_control_instinct.svg|]] *Image by Hercules from
<http://ts.hercules.com/download/sound/manuals/DJ_Instinct/Poster/Poster_DJCInstinct_UK.pdf>.
Click on the image for a bigger version.*

1.  Jog Wheel for the deck on the side of the wheel
2.  Action buttons for the deck on the side of the controls, depending
    on the mode they do the following:

<!-- end list -->

  - Hot Cue:

<!-- end list -->

``` 
    * **1:** Set and play (by holding it) from Hot Cue 1
    * **2:** Set and play (by holding it) from Hot Cue 2
    * **3:** Reset Hot Cue 1
    * **4:** Reset Hot Cue 2
* Loop
    * **1:** Set Loop start
    * **2:** Set loop end
    * **3:** Shrink loop (halves it)
    * **4:** Exit loop
* Effect
    * **1:** Toggle Effect 1
    * **2:** Toggle Effect 2
    * **3:** Toggle Effect 3
    * **4:** Toggle Effect 4
* Sample
    * **1:** Play Sample 1
    * **2:** Play Sample 2
    * **3:** Play Sample 3
    * **4:** Play Sample 4 
- Mode status display. The current mode is glowing or if none is on, Hot Cues are enabled
- Headphone volume controls
- No direct use, used as a button to add a second layer of controls
- Switch the current mode for both decks
- Knobs to adjust the EQ of the deck they are on. Top knob adjusts highs, middle knob the mids and bottom know the lows.
- Buttons to browse your library. The up and down button go up and down in the current playlist, The folder/left button goes up in the playlist list and the Files/right button goes down in the playlist list.
- Load the currently selected track to the respective deck (A is the left deck, B is the right deck)
- Listen to this deck unmixed on the headphones
- Deck volume adjusts the output volume of the respective deck
- Crossfader
- Temporary pitch shift. Pressing the Vinyl button increases the shift.
- Adjust tempo. Pressing both buttons together resets to the original tempo. Pressing the Vinyl button takes the steps bigger.
- Fast forward and backward buttons for the respective decks
- Sync tempo of this deck to the tempo of the other deck
- If pressed while paused sets the cue and when held plays from the cue, when pressed during playback jumps to the cue.
- Play and pause playback of the respective decks
```

#### MIDI Map

<https://docs.google.com/spreadsheets/d/1lNR5fh5pesNiECW_U8hI9UGamxqB5SG3x-9UddwpeHw/edit?usp=sharing>

### Mapping / Control files DJ Control Instinct S

Standard DJ Control Instinct doesn't work with the "Instinct S" variant.
This mapping works best: (download raw files):
<https://github.com/nikmartin/hercules-mixxx-mapping/tree/master/controllers>
