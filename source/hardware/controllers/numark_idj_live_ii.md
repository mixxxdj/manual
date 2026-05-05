(numark-idj-live-ii)=

# Numark iDJ Live II

![Numark iDJ Live II](https://www.numark.com/images/sized/images/product_large/iDJLiveII_ortho_web_lg-624x390.jpg)


:::{sectionauthor} Nathan Korth <nkorth@nkorth.com>
:::
The Numark iDJ Live II is a budget MIDI controller similar to the {ref}`Discover DJ <ion-discover-dj>`. It does not have a built in sound card, so a {ref}`splitter cable
<hardware-splitter-cables>` or a {ref}`separate audio interface <hardware-audio-interfaces>` is required to use headphones with it.

-  [Manufacturer's product page](https://www.numark.com/product/idj-live-ii)

:::{versionadded} 2.3.0
:::
## Compatibility


This controller is USB {term}`MIDI` class compliant, so it is plug-and-play on all platforms without having to install any special drivers.

## Button mapping


Most of the mapping is self-explanatory and matches up to labels in the Mixxx {term}`GUI`.
The mapping script only handles the jog wheels and scratch button, so you can remap everything else using the learning wizard if you'd like.

### Play/Cue/Sync buttons


Despite their appearance, the cue buttons don't seem to have LEDs. Only the play and sync buttons do.

The "SET" buttons set the cue point and the arrow buttons jump to the cue point. They do not change behavior depending on whether the track is playing or paused.

By default, the sync LEDs only light up when pressed or locked. To make them flash with the beat, go to "Output mappings" in the controller settings. Look for these rows, and replace "sync_enabled" with "beat_active":

| Channel | Opcode  | Control | On Value | Off Value | Action                     | Min | Max |
| ------- | ------- | ------- | -------- | --------- | -------------------------- | --- | --- |
| 1       | Note On | 0x40    | 0x7F     | 0x00      | [Channel1],sync_enabled | 0.5 | 1   |
| 1       | Note On | 0x47    | 0x7F     | 0x00      | [Channel2],sync_enabled | 0.5 | 1   |

### Jog wheels and scratch button


The scratch button in the middle changes the mode of the jog wheels. When the scratch LED is off, you can use the wheels to adjust the pitch of a playing track, or to quickly search through a paused
track. The search mode moves exactly 32 beats for each revolution of the jog wheel.

### Browse knob


The browse knob scrolls through your library, and the 1 and 2 buttons below it load a track into the corresponding deck. Pressing down on the Browse knob toggles fullscreen library view.
