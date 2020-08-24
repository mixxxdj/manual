# Hercules DJ Console RMX 2

[[/media/hardware/Hercules-DJ-Console-RMX-2.png|Hercules-DJ-Console-RMX-2.png]]

  - [Manufacturer's product
    page](http://www.hercules.com/us/DJ-Music/bdd/p/193/djconsole-rmx-2/)
  - [Manual / Midi
    commands](https://support.hercules.com/de/product/djconsolermx2-de)
  - [Forum thread](http://mixxx.org/forums/viewtopic.php?f=7&t=11860)
  - [Previous forum
    thread](http://mixxx.org/forums/viewtopic.php?f=7&t=4541)

This all-in-one DJ controller features a built in 4 channel sound card
with balanced XLR master outputs and a balanced microphone input. It is
a USB class compliant MIDI and audio device (unlike older Hercules
controllers).

## User Options

To change the mapping's user options, you have to open the script file
(\*.js). At the top of the file under **USER OPTIONS** the following
settings can be made:

  - **DJCRMX2.jogwheelSensivity**: Sets the jogwheel sensivity. 1 =
    default, 2 is twice as sensitive, 0.5 is half as sensitive.
  - **DJCRMX2.jogwheelShiftMultiplier**: Sets how much more sensitive
    the jogwheels get when holding \[**SHIFT**\]. Set it to 1 to disable
    jogwheel sensitivity increase when holding \[**SHIFT**\].
  - **DJCRMX2.twinkleVumeterAutodjOn**: If true, level-meter twinkles if
    *AutoDJ* is enabled.
  - **DJCRMX2.autoPFL**: If true, PFL / Cue (headphone) is being
    activated by loading a track into certain deck.
  - **DJCRMX2.vuMeterOutputMaster**: If true, deck vu meters show master
    output (L = Deck A, R = Deck B). If false, deck vu meter shows deck
    output (mono).
  - **DJCRMX2.showHideSamplersEffectsOnPadMode**: If true, *Samplers*
    and *EffectRack* get shown or hidden in dependance of Pad-Mode.

## General Functions

[[/media/hardware/hercules-djconsole-rmx-2.png|]]

### Managed by Mixxx

| Figure     | \[**SHIFT**\]? | Long-press? | Control Name        | Description                                              |
| ---------- | -------------- | ----------- | ------------------- | -------------------------------------------------------- |
| 11         | ✘              | ✘           | \[**MAIN VOLUME**\] | Controls *Master* volume                                 |
| 13         | ✘              | ✘           | \[**VINYL**\]       | Split headcue                                            |
| 13         | ✔              | ✘           | \[**VINYL**\]       | Maximize library                                         |
| 20         | ✘              | ✘           | \[**CROSS FADER**\] | Controls crossfader                                      |
| 21         | ✘              | ✘           | \[**CUE TO MIX**\]  | Controls mix in headphones between PFL and master signal |
| 7          | ✘              | ✘           | \[**MIC ON/OFF**\]  | Toggle microphone on/off and talkover on/off             |
| 15 (Right) | ✘              | ✘           | \[**FILES**\]       | Go To Item in Library                                    |
| 15 (Right) | ✔              | ✘           | \[**FILES**\]       | Add to bottom of Auto DJ playlist                        |
| 15 (Left)  | ✘              | ✘           | \[**FOLDERS**\]     | Move focus backward in Library                           |
| 15 (Left)  | ✔              | ✘           | \[**FOLDERS**\]     | Toggle Auto DJ                                           |
| 15 (Up)    | ✘              | ✘           | \[**UP**\]          | Move vertically up in Library                            |
| 15 (Up)    | ✘              | ✔           | \[**UP**\]          | Scroll vertically up in Library                          |
| 15 (Down)  | ✘              | ✘           | \[**DOWN**\]        | Move vertically down in Library                          |
| 15 (Down)  | ✘              | ✔           | \[**DOWN**\]        | Scroll vertically down in Library                        |

### Managed by the controller

The following functions directly affect the controller's sound card, so
adjusting these will not change anything on screen in Mixxx:

| Figure | \[**SHIFT**\]? | Long-press? | Control Name              | Description                           |
| ------ | -------------- | ----------- | ------------------------- | ------------------------------------- |
| 22     | ✘              | ✘           | \[**HEADPHONES VOLUME**\] | Controls the headphones output volume |
| 6      | ✘              | ✘           | \[**MIC VOLUME**\]        | Controls the microphone volume (gain) |

## Deck Functions

| Figure    | \[**SHIFT**\]? | Long-press? | Control Name                | Description                                                                                                                                  |
| --------- | -------------- | ----------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 (-)     | ✘              | ✘           | \[**PITCH BEND MINUS**\]    | Pitch bend down                                                                                                                              |
| 3 (-)     | ✔              | ✘           | \[**PITCH BEND MINUS**\]    | Decrement (halve) pitch range                                                                                                                |
| 3 (+)     | ✘              | ✘           | \[**PITCH BEND PLUS**\]     | Pitch bend up                                                                                                                                |
| 3 (+)     | ✔              | ✘           | \[**PITCH BEND PLUS**\]     | Increment (double) pitch range                                                                                                               |
| 2 (Left)  | ✘              | ✘           | \[**REWIND**\]              | Fast backward in loaded track                                                                                                                |
| 2 (Left)  | ✔              | ✘           | \[**REWIND**\]              | *Spinback* effect                                                                                                                            |
| 2 (Right) | ✘              | ✘           | \[**REWIND**\]              | Fast forward in loaded track                                                                                                                 |
| 2 (Right) | ✔              | ✘           | \[**REWIND**\]              | *Brake* effect                                                                                                                               |
| 9         | ✘              | ✘           | \[**SOURCE**\]              | Toggle pass thru                                                                                                                             |
| 17        | ✘              | ✘           | \[**PREVIEW**\]             | Toggle pfl                                                                                                                                   |
| 17        | ✔              | ✘           | \[**PREVIEW**\]             | Toggle keylock                                                                                                                               |
| 30        | ✘              | ✘           | \[**PLAY**\]                | *PlayButton* behavior of [components](components_js) lib                                                                                     |
| 30        | ✔              | ✘           | \[**PLAY**\]                | *PlayButton* behavior of [components](components_js) lib                                                                                     |
| 29        | ✘              | ✘           | \[**CUE**\]                 | *CueButton* behavior of [components](components_js) lib                                                                                      |
| 29        | ✔              | ✘           | \[**CUE**\]                 | *CueButton* behavior of [components](components_js) lib                                                                                      |
| 28        | ✘              | ✘           | \[**SYNC**\]                | *SyncButton* behavior of [components](components_js) lib                                                                                     |
| 28        | ✔              | ✘           | \[**SYNC**\]                | *SyncButton* behavior of [components](components_js) lib                                                                                     |
| 16        | ✘              | ✘           | \[**LOAD**\]                | Load selected track                                                                                                                          |
| 16        | ✔              | ✘           | \[**LOAD**\]                | Eject track                                                                                                                                  |
| 8         | ✘              | ✘           | \[**LOOP MODE**\] encoder   | Adjust beatloop size                                                                                                                         |
| 8         | ✔              | ✘           | \[**LOOP MODE**\] encoder   | Move loop forward/backward                                                                                                                   |
| 8         | ✘              | ✘           | \[**FX MODE**\] encoder     | EffectUnit's mix knob, in *EffectFocusMode* in combination with *ParameterEditMode* - Controls effect's parameters                           |
| 8         | ✔              | ✘           | \[**FX MODE**\] encoder     | EffectUnit's super knob                                                                                                                      |
| 8         | ✘              | ✘           | \[**SAMPLE MODE**\] encoder | Switch between 4 sampler banks (each of 4 samplers)                                                                                          |
| 8         | ✘              | ✘           | \[**CUE MODE**\] encoder    | Adjust key of loaded track                                                                                                                   |
| 24-1      | ✘              | ✘           | \[**LOOP PAD 1**\]          | Toggles beatloop over beatloop size                                                                                                          |
| 24-2      | ✘              | ✘           | \[**LOOP PAD 2**\]          | Toggles beatloop over 2 beats                                                                                                                |
| 24-3      | ✘              | ✘           | \[**LOOP PAD 3**\]          | Toggles beatloop over 4 beats                                                                                                                |
| 24-4      | ✘              | ✘           | \[**LOOP PAD 4**\]          | Toggles beatloop over 8 beats                                                                                                                |
| 24-1      | ✔              | ✘           | \[**LOOP PAD 1**\]          | Toggles beatlooproll over 1/16 beats                                                                                                         |
| 24-2      | ✔              | ✘           | \[**LOOP PAD 2**\]          | Toggles beatlooproll over 1/8 beats                                                                                                          |
| 24-3      | ✔              | ✘           | \[**LOOP PAD 3**\]          | Toggles beatlooproll over 1/4 beats                                                                                                          |
| 24-4      | ✔              | ✘           | \[**LOOP PAD 4**\]          | Toggles beatlooproll over 1/2 beats                                                                                                          |
| 24-1      | ✘              | ✘           | \[**FX PAD 1**\]            | Enables effect 1, in *EffectFocusMode* toggles effect button parameter 1, in *ParameterEditMode* gives encoder control of effect parameter 1 |
| 24-2      | ✘              | ✘           | \[**FX PAD 2**\]            | Enables effect 2, in *EffectFocusMode* toggles effect button parameter 2, in *ParameterEditMode* gives encoder control of effect parameter 2 |
| 24-3      | ✘              | ✘           | \[**FX PAD 3**\]            | Enables effect 3, in *EffectFocusMode* toggles effect button parameter 3, in *ParameterEditMode* gives encoder control of effect parameter 3 |
| 24-4      | ✘              | ✘           | \[**FX PAD 4**\]            | Shows/hides focus of EffectUnit                                                                                                              |
| 24-1      | ✘              | ✔           | \[**FX PAD 1**\]            | In *EffectFocusMode* enables *ParameterEditMode* and gives encoder control of effect parameter 1                                             |
| 24-2      | ✘              | ✔           | \[**FX PAD 2**\]            | In *EffectFocusMode* enables *ParameterEditMode* and gives encoder control of effect parameter 2                                             |
| 24-3      | ✘              | ✔           | \[**FX PAD 3**\]            | In *EffectFocusMode* enables *ParameterEditMode* and gives encoder control of effect parameter 3                                             |
| 24-4      | ✘              | ✔           | \[**FX PAD 4**\]            | Enables *EffectFocusMode* (+ press \[**FX PAD 1..3**\] to focus an effect)                                                                   |
| 24-1      | ✔              | ✘           | \[**FX PAD 1**\]            | Enables effect 1 of EffectUnit and controls meta its meta knob by velocity                                                                   |
| 24-2      | ✔              | ✘           | \[**FX PAD 2**\]            | Enables effect 2 of EffectUnit and controls meta its meta knob by velocity                                                                   |
| 24-3      | ✔              | ✘           | \[**FX PAD 3**\]            | Enables effect 3 of EffectUnit and controls meta its meta knob by velocity                                                                   |
| 24-4      | ✔              | ✘           | \[**FX PAD 4**\]            | Cycle through *effectUnit* numbers array                                                                                                     |
| 24-1      | ✘              | ✘           | \[**SAMPLE PAD 1**\]        | Load selected track into Sampler (Index 1) if empty, else go to cue point and play - velocity (volume) controlled                            |
| 24-2      | ✘              | ✘           | \[**SAMPLE PAD 2**\]        | Load selected track into Sampler (Index 2) if empty, else go to cue point and play - velocity (volume) controlled                            |
| 24-3      | ✘              | ✘           | \[**SAMPLE PAD 3**\]        | Load selected track into Sampler (Index 3) if empty, else go to cue point and play - velocity (volume) controlled                            |
| 24-4      | ✘              | ✘           | \[**SAMPLE PAD 4**\]        | Load selected track into Sampler (Index 4) if empty, else go to cue point and play - velocity (volume) controlled                            |
| 24-1      | ✔              | ✘           | \[**SAMPLE PAD 1**\]        | Stop Sampler (Index 1) if playing, else eject loaded track                                                                                   |
| 24-2      | ✔              | ✘           | \[**SAMPLE PAD 2**\]        | Stop Sampler (Index 2) if playing, else eject loaded track                                                                                   |
| 24-3      | ✔              | ✘           | \[**SAMPLE PAD 3**\]        | Stop Sampler (Index 3) if playing, else eject loaded track                                                                                   |
| 24-4      | ✔              | ✘           | \[**SAMPLE PAD 4**\]        | Stop Sampler (Index 4) if playing, else eject loaded track                                                                                   |
| 24-1      | ✘              | ✘           | \[**CUE PAD 1**\]           | Hotcue 1 *HotcueButton* behavior of [components](components_js) lib                                                                          |
| 24-2      | ✘              | ✘           | \[**CUE PAD 2**\]           | Hotcue 2 *HotcueButton* behavior of [components](components_js) lib                                                                          |
| 24-3      | ✘              | ✘           | \[**CUE PAD 3**\]           | Hotcue 3 *HotcueButton* behavior of [components](components_js) lib                                                                          |
| 24-4      | ✘              | ✘           | \[**CUE PAD 4**\]           | Hotcue 4 *HotcueButton* behavior of [components](components_js) lib                                                                          |
| 24-1      | ✔              | ✘           | \[**CUE PAD 1**\]           | Hotcue 1 *HotcueButton* behavior of [components](components_js) lib                                                                          |
| 24-2      | ✔              | ✘           | \[**CUE PAD 2**\]           | Hotcue 2 *HotcueButton* behavior of [components](components_js) lib                                                                          |
| 24-3      | ✔              | ✘           | \[**CUE PAD 3**\]           | Hotcue 3 *HotcueButton* behavior of [components](components_js) lib                                                                          |
| 24-4      | ✔              | ✘           | \[**CUE PAD 4**\]           | Hotcue 4 *HotcueButton* behavior of [components](components_js) lib                                                                          |
| 1         | ✘              | ✘           | \[**JOG WHEEL**\]           | Jog/Scratch loaded track                                                                                                                     |
| 1         | ✔              | ✘           | \[**JOG WHEEL**\]           | Jog/Scratch loaded track using *DJCRMX2.jogwheelShiftMultiplier* option                                                                      |
| 10        | ✘              | ✘           | \[**GAIN**\]                | Controls pregain                                                                                                                             |
| 18/19     | ✘              | ✘           | \[**VOLUME FADER**\]        | Controls volume                                                                                                                              |
| 4         | ✘              | ✘           | \[**PITCH FADER**\]         | Controls rate (speed control)                                                                                                                |
| 12        | ✘              | ✘           | \[**KILL TREBLE**\]         | High frequencies kill                                                                                                                        |
| 12        | ✘              | ✘           | \[**KILL MEDIUM**\]         | Middle frequencies kill                                                                                                                      |
| 12        | ✘              | ✘           | \[**KILL BASS**\]           | Low frequencies kill                                                                                                                         |
| 14        | ✘              | ✘           | \[**TREBLE**\]              | High frequencies control                                                                                                                     |
| 14        | ✘              | ✘           | \[**MEDIUM**\]              | Middle frequencies control                                                                                                                   |
| 14        | ✘              | ✘           | \[**BASS**\]                | Low frequencies control                                                                                                                      |
| 14        | ✔              | ✘           | \[**BASS**\]                | Filter (QuickEffectRack) control                                                                                                             |
