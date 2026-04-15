# Numark Party Mix


[Manufacturer's product page](https://www.numark.com/product/party-mix) · [Manufacturer's user manual](http://www.numark.com/images/product_downloads/Party_Mix_-_User_Guide_-_v1.1.pdf) · [Forum thread](https://mixxx.discourse.group/t/numark-party-mix-midi-mapping/16712)

:::{versionadded} 2.3.4
:::
## Overview


```{figure-md}
:align: center

<img src="../../_static/controllers/numark_party_mix.svg" alt="Numark Party Mix" class="pretty-figures" width="100%">

Numark Party Mix
```
See the tables below for controls descriptions.

## Center


| # | Name | Function |
| --- | --- | --- |
| 1 | {hwlabel}`BROWSE` (rotate) | Browse library |
| 1 | {hwlabel}`BROWSE` (press+rotate) | switch between Library and Sidebar |
| 1 | {hwlabel}`BROWSE` (press) | Equivalent to double clicking the currently selected item in Library (see :mixxx{coref}`GoToItem<[Library],GoToItem>` control) |
| 2 | {hwlabel}`LOAD` 1 and 2 | load currently selected track to Deck 1 or 2 |
| 3 | {hwlabel}`MASTER GAIN` | Adjust the volume level of {term}`master output`. |
| 4 | {hwlabel}`CUE MIX` | {term}`Head/mix knob<Head/mix button>`. Adjust the cue/main mix in the headphone output. |
| 5 | {hwlabel}`CUE GAIN` | Adjust the headphone volume |
| 10 | {hwlabel}`Crossfader` | Controls the mix between the two decks. See {ref}`interface-crossfader` |


## Deck


Each of those controls exists in both {term}`decks<deck>` and affects only the corresponding deck.

| # | Name | Function |
| --- | --- | --- |
| 6 | {hwlabel}`GAIN` | Adjust the pre-fader, pre-EQ audio level |
| 7 | {hwlabel}`TREBLE` | Adjust high frequencies |
| 8 | {hwlabel}`BASS` | Adjust low frequencies |
| 9 | {hwlabel}`Channel fader` | Adjust volume level |
| 11 | {hwlabel}`CUE` | {term}`Headphone button`. Toggle sending channel to the cue (headphone) channel |
| 12 | {hwlabel}`Jog wheel` | If scratch mode is enabled (see the {hwlabel}`SCRATCH` button below): scratch<br><br>If scratch mode is disabled: pitch bend<br><br>The behavior of the jog wheel can be fine-tuned, see the {ref}`Adjustable values<numark_party_mix_adjustable>` section. |
| 13 | {hwlabel}`SCRATCH` | Toggle scratch mode. Disabled by default. |
| 14 | {hwlabel}`Pitch fader` | Adjust the speed of the track |
| 15 | {hwlabel}`SYNC` | If sync lock is disabled: set BPM to the other deck's BPM<br><br>If sync lock is enabled: disable sync lock |
| 15 | {hwlabel}`SYNC` (hold, then release) | Enable {term}`sync lock` |
| 16 | {hwlabel}`CUE` | If track is playing: stops the track and resets position to the main cue point<br><br>If playback is stopped: sets the main cue point |
| 16 | {hwlabel}`CUE` (hold) | Play the track from main cue point, release to stop playback and return to the main cue point. Playback must be initially stopped on the main cue point. |
| 17 | {hwlabel}`Play/Pause` | Play/pause playback |
| 18 | {hwlabel}`PADS 1-4` | Pads 1-4 function depends on selected mode |
| 19 | {hwlabel}`PAD MODE` | Select mode of {hwlabel}`PADS 1-4` |
| 20 | {hwlabel}`MODE LEDs` | The 4 pads in each deck have multiple functions, depending on the selected *pad mode*. Default pad mode is *hotcues*. Current mode is selected by pressing {hwlabel}`PAD MODE`. The LED for currently active pad mode is lit up (or all 3 LEDs for effect mode). |


:::{hint}
The actual behavior of CUE and Play/Pause buttons depends on Mixxx settings. See {ref}`interface-cue-modes` for more info.

:::
## Pads


| # | Name | Function |
| --- | --- | --- |
| 18 | {hwlabel}`CUE Mode` | set hotcue if not set. If set, go to hotcue position and start playback.<br><br>Pad lights indicate if a particular hotcue is set or not. |
| 18 | {hwlabel}`LOOP Mode` | activate auto-loop.<br><br>Default auto-loop sizes are: 4, 8, 16, 32. Loop sizes can be adjusted, see the {ref}`Adjustable values<numark_party_mix_adjustable>` section. |
| 18 | {hwlabel}`SAMPLER Mode` | button for 4 Samples for each Deck 1-4 and 5-8 (toggle play from start and stop). |
| 18 | {hwlabel}`EFFECT Mode` | Pad 1-3 activates effect during press Deck1 of EffectUnit1, Deck2 of EffectUnit2.<br><br>Pad 4 switches mix mode. Pad light on indicates Dry/Wet mode. Pad Light off indicates Dry+Wet mode. |


(numark_party_mix_adjustable)=

## Adjustable values


There are a few configurable values at the top of the script ({file}`Numark-Party-Mix.scripts.js`).

| Variable | Default value | Description |
| --- | --- | --- |
| ``jogScratchSensitivity`` | '340' | 'Scratching sensitivity' |
| ``jogScratchAlpha`` | '1/8' | 'For controlling the alpha-beta filter used in scratching' |
| ``jogScratchBeta`` | '1/8/32' | 'For controlling the alpha-beta filter used in scratching' |
| ``jogPitchSensitivity`` | '10' | 'Jog wheel (pitch bend) sensitivity during play' |
| ``jogSearchSensitivity`` | '1/2' | 'Jog wheel (scrub) sensitivity during pause' |
| ``autoLoopSizes`` | '[ "4", "8", "16", "32"]' | 'Loop sizes for the auto-loop pad mode | each value corresponds to one of the pads.' |


:::{hint}
See [here](https://github.com/mixxxdj/mixxx/wiki/Midi-Scripting#user-content-scratching-and-jog-wheels) for more info about constants used in scratching.
:::
## Alternative Mappings

I am working on alternative mappings for this controller here: [Numark Party Mix Mappings](https://github.com/olafklingt/mixxx_numark_partymix)
