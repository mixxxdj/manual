# Behringer CMD MM-1

[[/media/hardware/behringer/behringercmdmm1overview.png|]]

  - [Forum
    thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=9276)

The Behringer CMD MM-1 is a flexible controller that controls 4 decks by
default. The mapping can be easily configured to control any combination
of decks and effect units. The [Behringer CMD DC-1](behringer_cmd_dc-1)
and [Behringer CMD DV-1](behringer_cmd_dv-1) are designed to be used
together with the CMD MM-1, but the CMD MM-1 can be used alone or with
other controllers (especially the [Novation
Launchpad](novation_launchpad_mapping_by_szdavid92))

## Mapping description

### Architecture

The controller has four strips of channels, each of which can be
configured to control a different Deck or even an EffectUnit. These
options can be changed during runtime via the Buttons in the of the
***ThirdLayer***. You can find more about how to use this at the end of
this document.

### Mapping options

There are a few user configurable options available for you to
customize. You can change these by opening the
`Behringer-CMD-MM-1-scripts.js` file in your [controller mapping file
locations\#user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder)
with your text editor of choice (such as Notepad, TextEdit, Kate, or
gEdit) and editing the lines at the very top of the file.

  - channelNumber: change this if your [\#controller does not light
    up](#controller%20does%20not%20light%20up)
  - invertColor: Swaps the colors which suits certain skins more
  - defaultChannelSequence: Defines how the channels are mapped when
    Mixxx starts
  - channelMode: Defines if a channel is in Deck or FX Mode when Mixxx
    starts
  - faderMode: Defines how the faders behave in FX Mode by default
  - standardKnobBehavior: Defines the mapping of the knobs when Mixxx
    starts
  - navEncoderScale: the factor of speedup when using the encoder with a
    modifier 

### Top row

[[/media/hardware/behringer/behringercmdmm1-toprowlabeled.png|]]

The top left knobs control the Master balance and Master gain. The top
right knobs control the headphone gain and cue mix (PFL/master mix in
Headphones output).

You can see the L/R buttons besides the encoder as \[*SHIFT*\] and
\[**CTRL**\] buttons. These allow each button to have up to four
functionalities. They behave like the Shift and Control keys on a
computer keyboard.

### Knobs

The Knobs have three different modes which can be cycled while in
operation. The knobs in each mode, from top to bottom, control:

1.  Deck: High, Mid, Low, QuickEffect (filter by default)
2.  Deck: Gain, High, Mid, Low
3.  Effect Unit: Meta 1, Meta 2, Meta 3, Mix

The Effect Unit number is the same as the channel/deck number, so the
channel that controls the knobs/buttons/faders of deck 1 also controls
the knobs of EffectUnit1, Channel 2 controls EffectUnit2, and so on.

#### FX Mode

The Knobs in FxMode overwrite the assigned mapping and are mapped as
\[Effect 1 Meta, Effect 2 Meta, Effect 3 Meta, Super\] and the fader is
also mapped to the mix of the EffectUnit. The buttons are documented in
their own section.

### Middle button

  - Normal: recenter Crossfader
  - Shift: Cycle Knob assignment (swaps the mapping of the knobs as
    mentioned earlier)

### Buttons

#### Deck Mode

\[1\]&\[2\] Buttons:

  - Normal: Change Crossfader side (Orientation)
  - Shift: Toggle Fx1&2 for desired Channel
  - Ctrl: Toggle Fx3&4 for desired Channel
  - Third: Change ChannelNumber/Assignment

\[CUE\] Buttons:

  - Normal: Pre-Fader-Listening
  - Shift: Load selected Track to Deck
  - Ctrl: enable Sync for the Deck.
  - Third: Change Channelmode

#### FX Mode

[[/media/hardware/behringer/buttonsofflabeledfxmode-min.png|]]

\[1\]&\[2\] Buttons:

  - Normal: Toggle Effect 1&2 in desired FxUnit
  - Shift: Toggle Channel1&2 for desired FxUnit
  - Ctrl: Toggle Channel3&4 for desired FxUnit
  - Third: Change ChannelNumber/Assignment

\[CUE\] Buttons:

  - Normal: Toggle Effect 3 for desired FxUnit
  - Shift: Pre-Fader-Listening for FxUnit
  - Ctrl: change mix\_mode of Unit
  - Third: Change Channelmode

### Faders

DeckMode:

  - Normal: Volume Fader

FxMode:

  - EffectUnit Mix (dry/wet)
  - Third: Reconfigure Fader to control Rate/BPM/Pitch of the Channel as
    if it was in Deckmode

### Reassigning channel mode and number

The channel modes and numbers can be set by changing the [\#mapping
options](#mapping%20options) at the top of the script. They can also be
changed while using the controller when in ***thirdMode***. Pressing the
cue- button toggles between Deck and FX Mode. The Channel number is
assigned with the \[1\]&\[2\] buttons.

They are mapped in a sort of two bit encoded system:

  - \[ \] & \[ \] = Channel 1
  - \[x\] & \[ \] = Channel 2
  - \[ \] & \[x\] = Channel 3
  - \[x\] & \[x\] = Channel 4

So you can change between channel 1&3 by pressing the \[1\] button, and
channel 2&4 by pressing the \[2\] button.

You can change the Channel mode (Deck/Fx) via the Cue Button. (Note:
there is a rare issue where you have to change the Channel mode after
the assignment for it to work. So it is suggested that you always change
the assignment first).

## Troubleshooting

### Controller does not light up

The issue is probably the MIDI channel of your MM-1. Behringer had a
tool that can set the controller to a different MIDI channel, however
this is no longer available for download from Behringer's website. So
you will have to modify the controller mapping to use the MIDI channel
that your controller is set to. Refer to [MIDI Crash
Course](midi_crash_course#sniffing_your_controller_with_mixxx) for how
to see incoming MIDI messages from your controller.

**NOTE:** The Behringer Website is currently (07.04.2018) undergoing
some maintenance which is why the productpage and the channelswitcher
utility is currently unavailable. After Emailing the support, they
provided a link to the
[Channelswitcher](https://music--c.ap7.content.force.com/servlet/servlet.EmailAttachmentDownload?q=%2FwSnKlUyyB%2BzbQSKctPoiJvsTfYczcfDzIqBxz2ocDse1VdWx4S8NXjyHKhbFfsBbxCe3uhNzEnFic%2FsTkPPxg%3D%3D)
([Mirror](https://mega.nz/#!4zhjxQKQ!A_HJjx40YzyHdoV1nPdPmWL83nmUGspssKNdxyf00Tc))
and a
[manual](https://music--c.ap7.content.force.com/servlet/servlet.EmailAttachmentDownload?q=%2FwSnKlUyyB%2BzbQSKctPoiBsPNgXKYtUs%2FOnHuE8nfl3EFaYPHCHQaat%2B50yN3fR%2FIe3k9mnNj%2FSe5xTcwwM23g%3D%3D)
([Mirror](https://mega.nz/#!JzITlC4a!GOeJb-wVjwp6gYnhSXvWeTZ02QcYlSo2tqTPSHZWeds))
for the whole CMD line up.

Once you know the MIDI channel of your controller, open the file
`Behringer-CMD-MM-1-scripts.js` file in your [controller mapping file
locations\#user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder)
with your text editor of choice (such as Notepad, TextEdit, Kate, or
gEdit) and replace the number `5` in the line where it says `var
CHANNELNUMBER = 5;`. Then, open the file `Behringer CMD-MM-1.midi.xml`
in the same folder and replace the 4 at the end of 0x94, 0x84 and 0xB4
with your CHANNEL-NUMBER MINUS 1. Restart Mixxx, reload the mapping in
Mixxx's preferences, and then it should work.
