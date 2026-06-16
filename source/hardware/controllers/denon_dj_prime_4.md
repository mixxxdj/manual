# Denon DJ Prime 4

![Photo of Prime 4](https://d1jtxvnvoxswj8.cloudfront.net/wysiwyg/denondj/catalog/prime-4/DenonDJ-img-Prime4TopIntro.jpg)

The Denon DJ Prime 4 is a powerful, 4-Deck, standalone DJ unit with a lot of powerful features:
* Built-in sound card
* Small drive bay for holding a large in-house music library
* 8 velocity-sensitive performance pads on each deck with different performance modes
* Large, touch-capacitive jog wheels
* 4 USB ports for multiple devices with different DJ libraries
* Online integration with SoundCloud, Tidal, Beatport, Beatsource, and Dropbox
* Plug-and-play integration with Serato DJ and Virtual DJ
* Computer Mode for sending and receiving MIDI signals to other software for custom mappings

[Mixxx Forum Thread](https://mixxx.discourse.group/t/denon-prime-4-mapping/22404/2) | [Manufacturer's Product Page](https://www.denondj.com/prime-4-prime4xus)

## Drivers & Firmware

To download firmware updates and/or the Windows driver for the Prime 4:
* Go to <https://www.denondj.com/downloads/>
* Click "STANDALONE DJ SYSTEMS"
* Click "PRIME 4"
* Download necessary files and follow on-screen instructions where necessary

## Mixxx Mapping Progress

A mapping for the Denon DJ Prime 4 is currently under development on [this GitHub fork](https://github.com/whanake-music/mixxx/tree/prime4_mapping).

### File Locations

Both mapping files can be found at `~/mixxx/res/controllers/Denon Prime 4.midi.xml` and `~/mixxx/res/controllers/Denon-Prime-4-scripts.js`, assuming the repo has been cloned to `~/mixxx`.

### Current Implementations

Currently, the EQ, Gain, Headphone Mix and Library scroll knobs work as expected, as does the Master Gain knob on the top right of the unit. I am slowly getting to grips with using Components JS for the buttons on each Deck and FX section, and so far the Cue and Play/Stop buttons on the left deck work, but with no LED feedback at present.
