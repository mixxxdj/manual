# Native Instruments Traktor Kontrol S4 MK2

[[/media/native_instrument_traktor_s4-mkii-1.jpg|native\_instrument\_traktor\_s4-mkii-1.jpg]]

  - [Manufacturer's product
    page](https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s4/)
  - [DJTechTools
    review](http://djtechtools.com/2013/10/22/review-traktor-kontrol-s4-mk2-and-s2-mk2/)
  - [Digital DJ Tips
    review](http://www.digitaldjtips.com/2013/10/review-video-traktor-kontrol-s4-mk2/)
  - [DJWORX
    review](https://djworx.com/review-ni-traktor-kontrol-s4-mk2-dj-controller/)

The Kontrol S4 MK2 is a 4 deck all-in-one controller with a sturdy build
quality and integrated sound card. The MK2 has substantial improvements
over the S4 MK1, including large multicolor buttons. The MK1 is not
supported and cannot be supported because it uses a proprietary
communication protocol exclusive to Traktor. The MK2 uses the standard
HID protocol (also used by keyboards & mice) to send and receive signals
from a computer, so it can work with Mixxx. The easiest way to tell the
MK1 apart from the MK2 is the appearance of the jog wheel. On the MK1,
the top of the jog wheel is black plastic; on the MK2, the top of the
jog wheel is shiny aluminum.

The Kontrol S4 Mk2 can run from USB bus power. Using the separate power
supply increases the brightness of the LEDs, which is helpful for using
it in daylight, and increases the volume of the headphone output.

## Compatibility

### Controller

The Kontrol S4 MK2 is a USB class compliant audio, HID, and MIDI device,
so it is compatible with Mixxx without any proprietary drivers on
GNU/Linux and Mac OS X. On Windows, it is recommended to install the
[driver from Native
Instruments](https://www.native-instruments.com/en/support/downloads/drivers-other-files/)
and select the ASIO sound API in the Sound Hardware section of Mixxx's
Preferences.

With the S4 plugged in, a MIDI device is listed as an available
controller in Mixxx's Preferences. That is the MIDI input/output ports
on the back of the S4 for connecting external MIDI gear; no mapping for
the S4 will appear in the menu for the MIDI device. The controller uses
HID for the knobs, buttons, and other components on the device, so the
mapping can only be loaded when you select the HID device on the left
side of Mixxx's Preferences.

### Timecode vinyl

The phono inputs on the S4 can be used with turntables for timecode
vinyl control of Mixxx. Unlike Traktor, there is no additional software
to install to use timecode with the S4; the free version of Mixxx is the
full version. However, note that Mixxx is not compatible with Traktor
Scratch Mk2 timecode; refer to the [Mixxx
manual](http://mixxx.org/manual/latest/chapters/vinyl_control.html#supported-timecode-media)
for a list of supported types of timecode.

## Mapping description

Note that Mixxx doesn't have the concept of a single "master" deck for
sync. Instead, push and hold the sync button to "lock" sync on for all
decks you want to remain in sync. Or you can push Shift + Sync to lock
sync on. Refer to [the Mixxx
manual](http://www.mixxx.org/manual/2.0/chapters/djing_with_mixxx.html#master-sync)
for details.

Mixxx does not have remix decks, so the four remix slot buttons control
the samplers. There are some more bonus actions that can be accessed by
holding shift and pressing certain buttons.

### Mixer

  - Gain, effects routing, equalizer high/mid/low, and cue (headphones)
    behave as labelled.
  - Filter: controls QuickEffect superknob. This controls the Filter
    effect by default, but a different effect can be chosen in the
    Equalizer section of Mixxs's Preferences.
  - Snap: toggles library fullscreen
  - Loop record: toggles whether Mixxx is recording your set
  - Shift + Gain: up/down will move the beatgrid

The Master Volume knob on the S4 controls the volume of the S4's master
output in hardware, so it does not affect the software master gain knob
in Mixxx. Peak display is only generated from software, however. So if
you see or hear clipping, lower the gain of the playing decks; adjusting
the master volume knob on the S4 will not help.

### Decks

  - Load: load track selected in library to the deck.
  - Load + shift: eject track
  - Small buttons with play icons: play a sampler from its cue point. If
    no track is loaded in the sampler, the track selected in the library
    will be loaded.
  - Small buttons with play icons + shift: If sampler is playing, stop
    it. If sampler is not playing, the loaded eject track from the
    sampler.
  - 1-4 numbered buttons: set/activate hotcue
  - 1-4 numbered buttons + shift: clear hotcue
  - Wheel nudge + shift: fast search through track when not playing

#### Looping

  - right encoder turn: double/halve loop size. The loop size is shown
    on the controller. A dot on the right indicates a fractional loop
    size. Two dots indicates a loop size larger than 99 beats.
  - right encoder press: activate loop of set size from current position
  - right encoder turn + shift: adjust key
  - right encoder press + shift: reset key

<!-- end list -->

  - left encoder turn: beatjump forward/backward by beatjump size (shown
    on screen but not on controller), or move the loop by beatjump size
    if there is a loop enabled
  - left encoder press: re-enable a loop that has been set previously.
    Pressing this before a loop will keep playing until the loop is
    entered.
  - left encoder turn + shift: adjust beatjump size
  - left encoder press + shift: jump to loop in point, activate loop,
    and stop playback. This is helpful for preparing to mix a track in
    with a loop.

<!-- end list -->

  - In button: set loop in point manually. Hold pressed while moving the
    jog wheel to finely adjust the loop in point.
  - Out button: set loop out point manually. Hold pressed while moving
    the jog wheel to finely adjust the loop out point.

### Effects

The knob on the left of each effect unit controls the mix (dry/wet) knob
for all 3 effects in the unit. The other knobs control the metaknobs of
the effects. The buttons below the metaknobs control the effect enable
buttons. When pressed with shift, they cycle through the available
effects. The button below the mix knob toggles whether the effect
parameters are showing on screen. This will be expanded in a future
update to implement the [Standard Effects
Mapping](Standard%20Effects%20Mapping).

The buttons at the top of each mixer column control which decks are
routed to which effects units.

### Mapping options

If you choose, you can edit the controller script and change the Remix
Slot buttons to perform loop rolls instead. Also by default, Shift + CUE
rewinds the track to the beginning but you can change this to a Reverse
Roll (or "Censor") effect instead.

Making these changes is still a little awkward and we will be making
controller preferences easier to change in the future. For now you'll
have to make a small change to the mapping script file. Don't worry, the
actual edit only involves replacing a single word in a text file.

1.  Open Mixxx Preferences and select the Kontrol S4 in the side list.
2.  You should see a series of tabs at the top of the preferences
    window, one of which is "Scripts". Select that tab.
3.  Select "Traktor-Kontrol-S4-MK2-hid-scripts.js". 
4.  Click "Open Selected File."
5.  Either the file should open in an editor, or you should see a file
    browser window with that file selected. If you see a file browser,
    right click the file and select an option to edit it.
6.  At the top of the file will be short instructions explaining what to
    do.
