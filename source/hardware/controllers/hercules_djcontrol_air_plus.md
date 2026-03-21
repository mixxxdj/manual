![](../../_static/controllers/hardware/hercules_dj/hdjcontrol_airplus.png)

\* [Manufacturer's page](https://www.hercules.com/en-us/dj/)
\* [Manufacturer's support and downloads
page](https://support.hercules.com/en/product/djcontrolairplus-en//)
\* [Forum
thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=9403)

## Compatibility

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows. However, if you wish to use the [ASIO sound
API](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api)
under Windows, please install the latest driver package available from
the [Support
page](https://support.hercules.com/en/product/djcontrolinpulse300-en//).

## Sound card setup

This controller has built-in 4 channel output sound card, with MASTER
output (RCA and 3.5mm jack) and HEADPHONE output (6.35mm and 3.5mm
jack).

\* Open **Preferences \> Sound Hardware**
\* Select the **Output** tab
\* From the **Master** drop-down menu, select the audio interface, then
**Channels 1-2**
\* From the **Headphones** drop-down menu, select the audio interface,
then **Channels 3-4**
\* Click **Apply** to save the changes.

Please refer to the user manual for more details about the[audio
configuration in
Mixxx](https://mixxx.org/manual/latest/en/chapters/example_setups.html#laptop-and-external-usb-audio-interface)
and [learning how to set your levels
properly](https://mixxx.org/manual/latest/en/chapters/djing_with_mixxx.html#djing-gain-staging).

### Mapping description

Save both MIDI and script files to your [controller mapping file
locations\#user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder),
then load the preset as described in [the user
manual](https://mixxx.org/manual/latest/en/chapters/controlling_mixxx.html#using-midi-hid-controllers)

NOTE: As it is not being used in the mapping , I'd recommend disabling
the Proximity sensor (**AIR control**) in the DJControl AIR+ control
panel in order to prevent unnecessary MIDI data being sent to Mixxx
![](../../_static/controllers/hardware/hercules_dj/air_sensor_off.png)

**Decks:**

**Vinyl** = Scratch On/Off (Default: ON)

**Gain** knob = Filter

**CUE/MIX:**
Cue Button = Switch monitor cue level to max.
Mix Button = Switch monitor cue mix to 50%.


Mic Button = Activate microphone input (in hardware).
Rec Button = Maximize/minimize library
Magic Button = AutoDJ On/Off


**PADS - Hot Cue:**

Set and trigger Hot Cue 1-4
SHIFT + Pad = Delete Hot Cue 1-4.

**PADS - Sample:**

Trigger Sampler 1-4 (Deck A)
Trigger Sampler 5-8 (Deck B)

**BANK 1 - FX Mode:**

Button 1-3 = FX 1-3 on/off
Button 4 = FX Rack 1/2 On/Off (Deck A/B respectively)

**BANK 2 - Loop Mode:**

Button 1-4 = Beatloop 1/2 / 1 / 2 / 4 beats



Other controls as labeled.
