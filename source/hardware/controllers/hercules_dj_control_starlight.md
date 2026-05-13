![](../../_static/controllers/hardware/hercules_dj/djcstarlight.png)

\* [Manufacturer's product
page](https://www.hercules.com/en-us/product/djcontrolstarlight/)
\* [Manufacturer's support and downloads
page](https://support.hercules.com/en/product/djcontrolstarlight-en/)
\* [Forum
thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=12570)

Ultra-compact, ultra-light, ultra-practical and ultra-unique with its
lights, the DJControl Starlight packs all the features needed to mix and
scratch. With its built-in audio interface, the DJControl Starlight
offers pre-listening in the headphones so you can then play your mix on
speakers, which is perfect for learning or creating new mixes. The
system is so comprehensive for its size that it boasts all the essential
features such as bass equalization/filter knobs for smooth transitions
or touch-sensitive jog wheels for easy scratching. The added bonus: the
bright and powerful RGB backlighting.

## Compatibility

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows. However, if you wish to use the [ASIO sound
API](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api)
under Windows, please install the latest driver package available from
the [Support
page](https://support.hercules.com/en/product/djcontrolstarlight-en//).

## Sound card setup

This controller has built-in 4 channel output sound card, with MASTER
output and HEADPHONE output (both 3.5mm jack).

\* Open **Preferences \> Sound Hardware**
\* Select the **Output** tab
\* From the **Master** drop-down menu, select the audio interface, then
**Channels 1-2**
\* From the **Headphones** drop-down menu, select the audio interface,
then **Channels 3-4**
\* Click **Apply** to save the changes.

Please refer to [the user
manual](https://mixxx.org/manual/latest/en/chapters/example_setups.html#laptop-and-external-usb-audio-interface)
for more details about the audio configuration in Mixxx.

##### Please note:

The **Master** and **Headphone** knobs are hardware controls and
interact directly with the integrated sound card's output. Although they
also send MIDI messages, they have NOT been mapped in Mixxx, so do not
expect an on-screen reaction when using them. This was done to prevent
the knobs to adjust both the gain on the controller's sound card and in
Mixxx.

Please refer to [the user
manual](https://mixxx.org/manual/latest/en/chapters/djing_with_mixxx.html#djing-gain-staging)
in order to learn how to set your levels properly when using Mixxx.

### Mapping description

Save both MIDI and script files to your [controller mapping file
locations\#user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder),
then load the preset as described in [the user
manual](https://mixxx.org/manual/latest/en/chapters/controlling_mixxx.html#using-midi-hid-controllers)

**Decks:**

Sync = Sync lock
SHIFT + SYNC = Sync master.

Cue = Cue point
SHIFT + CUE = Return to beginning of loaded song.

Play = Play/Pause
SHIFT + Play = Cue Stutter.



Vinyl = Scratch On/Off (Default: ON)

When Vinyl is on, turning a jog wheel scratches that deck. When Vinyl is
off, turning a jog wheel bends the pitch of the track.


**PADS - Hot Cue:**

Set and trigger Hot Cue 1-4
SHIFT + Pad = Delete Hot Cue 1-4.

**PADS - Loop:**

Beatloop 1/2 / 1 / 2 / 4 beats

**PADS - FX Mode:**

FX 1-3 on/off
SHIFT + Pad = FX 1-3 Select
PAD 4 = FX Rack 1/2 On/Off (Deck A/B respectively)

**PADS - Sample:**

Trigger Sampler 1-4 (Deck A)
Trigger Sampler 5-8 (Deck B)

**Base LED:**

Link to VU Meter for light show effect on each deck respectively.

Other controls as labeled.
