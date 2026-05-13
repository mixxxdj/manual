# Hercules DJ Control Instinct P8

![](../../_static/controllers/hardware/hercules-instinct-p8.jpg)

  - Manufacturer's product pages: [DJ Control Instinct
    P8](https://www.hercules.com/en-us/product/djcontrolinstinctp8/)
  - [Forum thread](https://mixxx.org/forums/viewtopic.php?f=7&t=9155)

## Setup

The controller is a class compliant MIDI controller

### Audio Channels

There are two outputs on the controller itself: the headphones output
with builtin volume control on the side facing you and the speakers
output.

In Mixxx the headphones output is on channels 3 and 4, so select the
"Channels 3-4" item to get stereo output. The speakers output is on
channels 1 and 2, so to get stereo output you want to select the
"Channels 1-2" item.

## Controls

  - Play, Cue, Sync, crossfader, volume faders, equalizer knobs, PFL,
    PFL+/-, Load A/B
  - work as expected
  - Shift + Play: Play/Stutter
  - Shift + Cue: Go to cue and stop
  - Shift + Sync: Pitch reset
  - (Shift+) Browser button: Move focus
  - Browser knob: Vertical movement
  - Shift + Browser knob: Master gain
  - Wheel jog: Pitch bend
  - Shift + wheel jog: Pitch change
  - Scratch: Enable scratching
  - Shift + Scratch: Toggle AutoDJ
  - Loop button: Toggle loop
  - Pads in Loop mode:
  - Pad1: Toggle 1 beat loop
  - Pad 2: Toggle 2 beat loop
  - Pad 3: Toggle 4 beat loop
  - Pad 4: Toggle 8 beat loop
  - Shift + Pad 1: Set loop in
  - Shift + Pad 2: Set loop out
  - Shift + Pad 3: Halve loop
  - Shift + Pad 4: Double loop
  - Loop knob: Halve/double loop
  - Shift + Loop knob: Move loop
  - Pads in FX mode:
  - Pad 1: Toggle effect 1
  - Pad 2: Toggle effect 2
  - Pad 3: Toggle effect 3
  - Pad 4: Toggle effect unit on channel
  - Loop knob: FX Super
  - Shift + Loop knob: FX Mix
  - Deck A Pads in FX mode: AutoDJ
  - Shift + Pad 1: Fade now
  - Shift + Pad 2: Skip next
  - Shift + Pad 3: Add to bottom
  - Deck B Pads in FX mode: Preview 1
  - Shift + Pad 1: Load track and play
  - Shift + Pad 2: Play/Stop
  - Shift + Pad 3: Fast rewind
  - Shift + Pad 4: Fast forward
  - Pads in Sample mode:
  - Pad X: Play sample X
  - Shift + Pad X: Stop sample X
  - Pads in Cue mode:
  - Pad X: Activate hotcue X
  - Shift + Pad X: Clear hotcue X

Some further comments:

  - Hercules uses shifted controls for decks C and D. However, not all
    functions may be mapped for the additional decks and the
    soft-takeover did not work well despite adding all the affected
    controls to the JavaScript code. Thus I have commented out the
    corresponding mappings.
  - The FX mode mappings deviate from Hercules documentation as
    scripting would be required.
  - The pitch reset was reassigned to Shift + Sync because the jog touch
    detection is rather sensitive and would reset inadvertently.
  - Neither normal nor scratch mode react to the wheel when a touch is
    detected. (todo)
  - After scratching the sound remains somewhat distorted until
    disabling scratch mode. (reason unknown)
  - Virtual knobs respond rather slowly to turning of the encoder knobs.

#### MIDI Map

<http://ts.hercules.com/download/sound/MIDI_Mapping/DJ_InstinctP8/DJControl_Instinct_P8_MIDI_Command_List.pdf>
