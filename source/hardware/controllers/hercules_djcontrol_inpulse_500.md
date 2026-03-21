![](https://aws1.discourse-cdn.com/free1/uploads/mixxx/original/2X/e/e3ee08e8d4b5ed1cd8d49e694720ae56a70720bc.png)

\* [Manufacturer's product
page](https://www.hercules.com/en-us/product/djcontrol-inpulse-500/)
\* [Manufacturer's support and downloads
page](https://support.hercules.com/en/product/djcontrolinpulse500-en//)
\* [Forum
thread](https://mixxx.discourse.group/t/hercules-djcontrol-inpulse-500/19739/)

## Compatibility

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows.
However, if you wish to use the [ASIO sound
API](https://mixxx.org/manual/latest/en/chapters/preferences.html?highlight=asio#windows)
under Windows, please install the latest driver package available from
the [Support
page](https://support.hercules.com/en/product/djcontrolinpulse500-en//).

## Sound card setup

This controller has built-in 4 channel output sound card, with MASTER
output (RCA) and HEADPHONE output (3.5mm jack).

\* Open **Preferences \> Sound Hardware**
\* Select the **Output** tab
\* From the **Master** drop-down menu, select the audio interface, then
**Channels 1-2**
\* From the **Headphones** drop-down menu, select the audio interface,
then **Channels 3-4**
\* Click **Apply** to save the changes.

Please refer to [the user
manual](https://mixxx.org/manual/latest/en/chapters/example_setups.html#laptop-and-external-usb-audio-interface)
for more details about the audio configuration in Mixxx as well as to [learn how to set your levels properly when using Mixxx](https://mixxx.org/manual/latest/en/chapters/djing_with_mixxx.html#djing-gain-staging)

### Mapping description

***
Save both [MIDI](https://mixxx.discourse.group/uploads/short-url/iM3HIi1t8Rk2UzyvVzt7ihr4W9J.xml) and [script](https://mixxx.discourse.group/uploads/short-url/kSoIcpk36f5XXAqin2wuNNKwmC7.js) files to your [user controller mapping
folder](https://github.com/mixxxdj/mixxx/wiki/controller%20mapping%20file%20locations#user%20controller%20mapping%20folder),
then load the preset as described in [the user
manual](https://mixxx.org/manual/latest/en/chapters/controlling_mixxx.html#using-midi-hid-controllers)

#### Please note:
The following are hardware controls and interact directly with the integrated soundcard's input and output.

##### Master
- Master Vol
- Master Headphone button
##### Headphones
- Headphone mix knob
- Headphone Volume
##### Mic
- Mic Vol
- High
- Low
##### Aux
- Aux Vol
- Aux Filter

Although they also send MIDI messages, they have NOT been mapped in Mixxx, so do not expect an on-screen reaction when using them.
This was done to prevent the knobs to adjust both the parameters on the controller's sound card and in Mixxx.

##### Other controls not included in this mapping:

* PADS mode 5-8

* Filter/FX buttons


***

**Decks:**

Sync = Sync lock
_SHIFT_ + SYNC = Sync master.

Cue = Cue point
_SHIFT_ + CUE = Return to beginning of loaded song.

Play = Play/Pause
_SHIFT_ + Play = Cue Stutter.


Vinyl = Scratch On/Off (Default: ON)

Slip = Slip Mode
Quant. = Keylock

Beat Align LED = Track end warning (Make sure **Beatmatch Guide** is
**On** for this to work)

Loop In = Beatloop 4 beats.
_SHIFT_ + Loop In = Loop Halve.
Loop Out = Beatloop Off.
_SHIFT_ + Loop Out = Loop Double.

LOOP Encoder = Loop Halve / Loop Double.

Encoder button = Beatloop On/Off (according to length selected).

**Browser:**

Encoder = Move up/down list.

Encoder button = Switch focus between List and file view .

_SHIFT_ + Encoder button = Maximize/Minimize browser view.

Assistant = AutoDJ On/Off.



**PADS - Hot Cue:**

Set and trigger Hot Cue 1-8.
_SHIFT_ + Pad = Delete Hot Cue 1-8.

Pad colors are set to match Mixxx color code (relatively....). This is a work is progress :-)

**PADS - Loop:**

Beatloop 1/8 to 16 beats


**PADS - Slicer = Beatjump:**

Pad 1-2: Beatjump Backward/Forward 1 beat
Pad 3-4: Beatjump Backward/Forward 2 beat
Pad 5-6: Beatjump Backward/Forward 4 beat
Pad 7-8: Beatjump Backward/Forward 8 beat

**PADS - Sampler:**

Same for both decks:

Trigger Sampler 1-4 (Upper row - Dark blue)
Trigger Sampler 5-8 (Lower row - Cyan)
