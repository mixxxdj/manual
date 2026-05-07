# Behringer CMD MM-1 Advanced Mapping

This is my Advanced mapping for the Behringer CMD MM-1. Its main focus
was not to make a complete mapping for the whole CMD series (see this
mapping: [Behringer CMD MM-1](behringer_cmd_mm-1)), but instead to add
the features that the mapping for the Novation Launchpad MK2 is missing
[Mixxx mapping for Novation Launchpad
🦄](novation_launchpad_mapping_by_szdavid92). This mapping can of
course also by itself.

Thanks to Mevsme for the 3D-Model of the controller.

![](../../_static/controllers/hardware/behringer/behringercmdmm1overview.png)

### The concept

##### Modifiers

Similar to the mentioned Launchpad Mapping, this mapping features two
modifiers: \[*SHIFT*\] and \[**CTRL**\] These allow each button to have
up to four functionalities. They behave like the normal shift and
control keys on your PC-Keyboard. Most of the features can be explained
via the renderings where the functionalities are marked by the
formatting of the Text (\[*SHIFT*\] and \[**CTRL**\]).

##### Channels

Each Channel can be put into Deck- and FX-Mode, as well as reassigned to
a different Deck/FxUnit on the fly or via a variable at the top of the
script. This makes it possible for people that only use two decks to use
the other channels for controlling an EffectUnit instead of wasting the
unused controls.

##### Reassigning Channelmode and -number

Both can be changed when in ***thirdMode***: Pressing the cue-button
toggles between Deck- and Fx-Mode. The Channelnumber is assigned with
the \[1\]&\[2\] buttons.

\<nerd speech\> They are mapped in a sort of two bit encoded system
\</nerd speech\>

If you have no Idea what that is these are the combos and the
corresponding number:

  - \[ \] & \[ \] = Channel 1
  - \[x\] & \[ \] = Channel 2
  - \[ \] & \[x\] = Channel 3
  - \[x\] & \[x\] = Channel 4

So you can change between channel 1&3 by pressing the \[1\] button, and
channel 2&4 by pressing the \[2\] button.

### Global variables

There are four global variables at the top of the script:

  - channelNumber: The standard channelnumber of the CMD MM-1 is 5 but
    it can differ. If that's the case you can change it here
  - invertColor: Swaps the colors which suits certain skins more
  - defaultChannelSequence: Defines how the channels are mapped by
    default.
  - channelMode: Defines if a channel is in Deck- or FxMode by default.
  - standardKnobBehavior: Defines the default mapping of the knobs.

### The top row

![](../../_static/controllers/hardware/behringer/behringercmdmm1-toprowlabeled.png)

The Out 1 knob controls the Master balance and the Out 2 knob controls
the Master gain.

You can see the L/R buttons besides the encoder as Shift and Ctrl
buttons.

The encoder in the middle is able to browse the library and jump on the
preview deck (16 steps) while holding shift. When pressing the encoder,
the selected/highlighted track in the library gets loaded into the
preview deck. The preview deck can be played/paused when holding shift
while pressing the encoder down.

The Cue Vol/Mix knobs have no alternative functionality.

### Knob unit

![](../../_static/controllers/hardware/behringer/behringercmdmm1-knoboptionslabeled.png)

The Knobs have three different mappings which can be cycled while in
operation. (more on that later) The first one is the standard
\[High,Mid,Low,Quickeffect\]-Combo. The second one shifts everything up
and is mapped to \[Gain,High,Mid,Low\] which some people might prefer.
The third one controls the EffectUnits \[Meta1,Meta2,Meta3,Mix\]. The
Effectunit is based on the channel/deck number, so the channel that
controls the knobs/buttons/faders of channel 1 also controls the knobs
of EffectUnit1, Channel 2 controls EffectUnit2, etc.

#### FxMode-Knobs

![](../../_static/controllers/hardware/behringer/channelstriplabeled-min.png)

The Knobs in FxMode overwrite the assigned mapping and are mapped as
\[Effect1Meta,Effect2Meta,Effect3Meta,Super\] but the fader is also
mapped to the mix of the EffectUnit. The Buttons are documented in their
own section.

### MiddleButton/exShift ;-)

![](../../_static/controllers/hardware/behringer/behringercmdmm1-knobslabeled.png)

Normal: toggle maximize library, Shift: recenter Crossfader Ctrl: Cycle
Knob assignment (swaps the mapping of the knobs as mentioned earlier.
Third: Reassing Channel Sequence (resets mapping back do the global
defaults (look at global vars))

### Buttons

##### DECKMODE

![](../../_static/controllers/hardware/behringer/buttons_orientationlabeled-min.png)

\[1\]&\[2\] Buttons:

  - Normal: Change Crossfader side (Orientation)
  - Shift: Toggle Fx1&2 for desired Channel
  - Ctrl: Toggle Fx3&4 for desired Channel
  - Third: Change ChannelNumber/Assignment

\[CUE\] Buttons:

  - Normal: Pre-Fader-Listening
  - Shift: Load selected Track to Deck
  - Ctrl: Enable Fx-PFL for Unit according to channel number.
  - Third: Change Channelmode

##### FXMODE

![](../../_static/controllers/hardware/behringer/buttonsofflabeledfxmode-min.png)

\[1\]&\[2\] Buttons:

  - Normal: Toggle Channel1&2 for desired FxUnit
  - Shift: Toggle Channel3&4 for desired FxUnit
  - Ctrl: Toggle Effect 1&2 in desired FxUnit
  - Third: Change ChannelNumber/Assignment

\[CUE\] Buttons:

  - Normal: Pre-Fader-Listening for FxUnit
  - Shift: assign to master
  - Ctrl: Toggle Effect 3 for desired FxUnit
  - Third: Change Channelmode

### Faders

![](../../_static/controllers/hardware/behringer/behringercmdmm1-fadeslabeled.png)

DeckMode:

  - Normal: Volume Fader
  - Shift: Rate-/BPM-Faders

FxMode:

  - EffectUnit Mix

### Troubleshooting

#### Controller does not light up

The issue is probably the Midi-Channel of your MM-1. Behringer has a
tool that allows every controller in the CMD-series to change its
midi-channel. So your controller is probably set to the wrong channel.
The easiest way to fix this is to use Behringers tool and set it do
MIDI-CHANNEL 5 (THIS IS IMPORTANT).
<https://musicgroup-prod.mindtouch.us/04_BEHRINGER/CMD-_How_Do_I_Change_MIDI_Channel_On_My_CMD_Controller%3F>
If you can't do that for some reason, you have to find out the channel
your MM-1 is sending on at the time. Once you know that you should go
change the line where it says "var CHANNELNUMBER = 5;" of the file
"Behringer-CMD-MM-1-Advanced-scripts.js" in the folder with the mappings
so there is the number of your channel instead of the 5. (IMPORTANT: NO
PARENTHESES). The you have to find the file "Behringer
CMD-MM-1-Advanced.midi.xml" in the same folder and replace the 4 at the
end of 0x94, 0x84 and 0xB4 with your CHANNEL-NUMBER MINUS 1. Restart mix
and then it should work.
