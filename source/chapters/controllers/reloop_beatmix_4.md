# Reloop Beatmix 4

[[/media/reloop-beatmix-4.jpg|]]

  - [Manufacturer's product
    page](http://www.reloop.com/reloop-beatmix-4)
  - [Forum thread : mapping to download, users feedback, installation
    notes](http://www.mixxx.org/forums/viewtopic.php?f=7&t=8428)

The **Reloop Beatmix 4** is a performance-oriented 4-channel pad
controller with integrated soundcard. **Beatmix 4** offers an
ergonomically designed 4-channel mixer layout, optimized for the club
allowing you to work intuitively: Dedicated equalizer and gain dials,
high-quality line-faders, an extremely smooth-running crossfader, 16
multi-colour drum pads, as well as two extensive FX units are the
foundation for your creativity.

This controller is a midi and audio class compliant device so it is
compatible as-is with Linux, MacOS and Windows. However, on windows, the
manufacturer ship an ASIO low-latency driver that can be found on the
[Manufacturer's product page](http://www.reloop.com/reloop-beatmix-4).

The MIC input is hardware-mixed and is not digitized so Mixxx can not
have any control on the mic and you can not use ducking in Mixxx.

The master volume and head volume knobs directly control hardware and
don't change Mixxx controls. So be sure to adjust Mixxx controls to the
desired level using the mouse or keayboard.


## Mixer Section

[[/media/reloop-beatmix4_mixer-section.png|]]

  1. **MASTER** Controls the master volume to your main sound system.  This controls the built in sound card and has no effect on the master gain knob in Mixxx.
  2. **PHONES** Controls your headphones volume. This controls the built in sound card and has no effect on the headphone gain knob in Mixxx.
  3. **CUE MIX** Mixes the headphones CUE signal between your selected channel and the master output.
  4. **TRAX SELECT** Use the trax select encoder to navigate through your song library. See [below](#Trax-selector-and-Back-button) for details.
  5. **TRACK LOAD** Press 1-4 to load tracks on either channel. Long press 1-4 to eject the selected deck. These buttons are lit when a track is loaded into the associated deck.
  6. **FADER-START** Press SHIFT + track load 1-4 to enable and launch a track using your linefader. (hardware function)
  6. **CUE** Pre-listen the selected channel in your headphones.  This buttons lights-up when activated
  7. **BACK** push back button to switch Trax action between playlists (sidebar), tracks and Preview Deck. See [below](#Trax-selector-and-Back-button) for more explanation.
  8. **SAMPLER VOLUME** Controls the volume of all samplers.  *Tip*: you can replace the fader cap of this fader with a [custom colored fader cap](custom%20caps) to make it visually stand out from the channel volume faders.
  9. **LINE FADERS** Controls your channel volume.
  10. **CROSSFADER** Enables you to fade between your decks.
  11. **GAIN** Adjust the gain for each deck.
  12. **EQ** Tweak the high, mid or low frequencies when mixing your track.
  13. **DECK** Press the deck button to swap between decks 1 & 3 on the left and 2 & 4 on the right.

## Trax selector and Back button

[[/media/reloop-beatmix4_trax-selector.png|]]

The trax selector let you navigate through your library (playlist and
tracks) as well as preview tracks.

The trax selector has three modes:

  - **Track mode** (default): turning the trax selector will select
    tracks (one by one), turning with shift will select tracks faster
    (10 by 10). Pressing the "Back" button will switch to Playlist mode
    and pushing the trax selector will load the selected track into the
    preview deck, start playing and switch to Preview mode.
  - **Playlist mode**: turning the trax selector will select sidebar
    item (one by one), turning with shift will select sidebar item
    faster (10 by 10). Pressing the trax selector will expand/collapse
    the selected sidebar item and pressing the "Back" button will return
    to Track mode.
  - **Preview mode**: turning the trax selector let you navigate through
    the track loaded in the PreviewDeck (faster with shift), pushing the
    trax selector play/pause the preview deck and pushing the back
    button return to Track mode.

## Transport Section

[[/media/reloop-beatmix4_transport-section.png|]]

**PLAY/PAUSE** Press to launch and pause your track.

**SHIFT + PLAY/PAUSE** This reverses the direction of the track playing.

**CUE** Cue sets a temporary CUE point. It is set by pausing the track
and pressing the CUE button. Whilst the track is playing, press CUE to
return to that point, where it will pause.

**SHIFT+ CUE** Takes you back to the start of your track.

**CUP** Pressing CUP takes you directly to your CUE point, starting
playback instantly. If no CUE point is set, it will jump to the
beginning of the track.

**SHIFT + CUP** Changes the pitch range, cycling through 8%, 10%, 12%
and 16%

**SYNC** Syncs the BPM and phase to that of the other track (if BPM is
detected on both).

**SHIFT + SYNC** Turn on master sync, keeping sync enabled

## Jog wheel and pitch slider

[[/media/Reloop-Beatmix4_JogWheel.png|]]
[[/media/reloop-beatmix4_pitchslider.png|]]

Touch and move the jog wheel to scratch (either deck playing or not).

When playing, use the side of the wheel, without touching the metallic
platter, to temporarily bend the pitch (speed up/slow down playback).

When the deck is not playing, using the side of the wheel let you quick
search through your track.

Hold SHIFT and turn the jog wheel to quick search through your track

(shift ignores touch sensitive platter so holding shift and turning
jogwheel is the same as using the side of the jogwheel).

When a deck is playing, jog led will turn around at 33.3RPM. When track
time left is below 30 seconds, jog leds will blink slowly, and when
track time remaining is below 15 seconds, jog leds will blink quickly.
These delays can be changed by editing the two variables at the
beginning of the JS file and eventually set to -1 to disable jog led
blink.

The pitch slider let you adjust pitch.

Pitch +/- buttons let you temporarily adjust the the speed one step
higher/lower. These buttons, when used with shift, let you [control
effects](#Effects-Section).

## Effects Section

[[/media/reloop-beatmix4_fx-section.png|]]

The effect section let you control the first two EffectUnits. There are
two different effect modes mapped:

  - Multi Effect mode (the default), where you can load up to three
    effects in each EffectUnit and control then with the superKnob
  - Single Effect mode, where you can load a single effect in the
    EffectUnit and control the first 6 parameters

|                    |                               |                     |
| ------------------ | ----------------------------- | ------------------- |
|                    | Multi Effect mode             | Single Effect mode  |
| FX1                | Turn left to disable effect 1 | Effect parameter 1  |
| FX2                | Turn left to disable effect 2 | Effect parameter 2  |
| FX3                | Turn left to disable effect 3 | Effect parameter 3  |
| Shift + FX1        | select effect 1               | Effect parameter 4  |
| Shift + FX2        | select effect 2               | Effect parameter 5  |
| Shift + FX3        | select effect 3               | Effect parameter 6  |
| Beats turn         | SuperKnob                     | dry/wet knob        |
| Beats push         | EffectUnit enable/disable     |                     |
| Shift + Beats turn | dry/wet knob                  | Select Effect Chain |
| Shift + Beats push | Eject Effect Chain            |                     |

You can choose which deck you want to apply EffectUnit 1 and 2 by
pressing Shift + Pitchbend- / Shift + Pitchbend+ on that deck (short
press).

To switch from Single Effect mode to Multi Effect mode, hold down shift
and press Pitchbend- for more than a second to switch to "Single Effect
mode" or Pitchbend+ for more than a second to switch to "Multi Effect
mode". The corresponding led will blink three times, indicating which
mode you switched to.

## Pad Section

[[/media/reloop-beatmix_pad-section.png|]]

### Mode A - Cue points and Loops

**Top Row 4 Pads - CUE Points**  
Press an unlit pad to set a new CUE point. If it is already set, jump to
this CUE point.

**Top Row 4 Pads - SHIFT + PAD**  
Deletes CUE points.

**Lower Row 4 Pads - LOOP**  
Press the pad to activate a loop. Loop length (in beats) is respectively
1, 2, 4 and 8 beats.

**Lower Row 4 Pads + SHIFT - LOOP ADJUST**  
Drum Pad 1 - Sets a loop length. Push to define loop start, release to
define loop end.  
Drum Pad 2 - Shortens (half) the LOOP.  
Drum Pad 3 - Lengthens (double) the LOOP.  
Drum Pad 4 - Replays the LOOP.

### Mode B - Samplers

Mode B let you control 8 samplers. Top row is for sampler 1-4 and bottom
row is for sampler 5-8, each sampler controlled by a pad button.

Press an unlit pad to load the track selected in the library to that
sampler. Pads are red when the sampler is loaded but not playing and
purple when playing.

Press a red pad to play the sample from its cue point. Press a purple
pad to jump back to the sample's cue point.

Press a purple pad with shift to stop a playing sample. Press a red pad
with shift to eject a sample.

### Split mode

Split mode is activated by pressing mode A and mode B buttons
simultaneously. The two leds A and B are lit together. In this mode, to
top row is configured in mode A, and the bottom row if configured as the
top row of mode B.

So in this mode, you can control 4 cue points and 4 samplers.
