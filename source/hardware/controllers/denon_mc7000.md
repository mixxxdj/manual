### The full mapping documentation has been moved to the [Mixxx User Manual](https://manual.mixxx.org/2.3/en/hardware/controllers/denon_mc7000.html) since Mixxx v 2.3.
I gonna maintain additional information here inside the Wiki for people who wanna get more information, alternative mappings or help to improve the functionality.

### Content of this page:

* [How to get mappings that are not included with Mixxx](#how-to-get-additional-mappings)
* [Change Log](#change-log)
* [Under investigation / development](#under-investigation--development)
* [Wish List](#wish-list)
* [Contact, DJ Web Sites and Tutorials](#contact-dj-web-sites-and-tutorials)

### How to get additional mappings

For MIXXX 2.2.4 and following the mapping will be included in the
Software. You don't need to download.

If you like to add a mapping manually for any other version then read on...

The version for MIXXX 2.2.2 or MIXXX 2.2.3 is on GitHub. You need both
files so please just right click each of the links and "save link as".

  - [Denon MC7000 Mapping \*.xml
    file](https://github.com/mixxxdj/mixxx/raw/2.2/res/controllers/Denon-MC7000.midi.xml)
  - [Denon MC7000 Mapping \*.js
    file](https://github.com/mixxxdj/mixxx/raw/2.2/res/controllers/Denon-MC7000-scripts.js)

I am continuously working on fine tuning the mapping - see below section [Under investigation / development](#under-investigation--development)

For testing you can find the latest development mapping here:
  - [Denon MC7000 Mapping \*.xml
    file](https://github.com/toszlanyi/mixxx/raw/Denon_MC7000_mapping/res/controllers/Denon-MC7000.midi.xml)
  - [Denon MC7000 Mapping \*.js
    file](https://github.com/toszlanyi/mixxx/raw/Denon_MC7000_mapping/res/controllers/Denon-MC7000-scripts.js)

Read further [where to place the mapping
files](https://github.com/mixxxdj/mixxx/wiki/controller_mapping_file_locations)
for your system.

**You need to activate the mapping in Preferences -\> Controller -\>
chose the MC7000 mapping.**

### Change Log

**Release for Mixxx 2.3**
  - added Library sort function for Artist, Title, BPM, Key
  - added Softtakeover for Pitch faders
  - combine Censor/Reverse with Slip Mode
  - use Shift + Key Select/Reset Knob for Waveform Zoom/Reset
  - add Search through track using Shift + Jog Wheel
  - use Parameter buttons to add or delete stars
  - use Shift + Parameter to cycle track color in library
  - use library select knob to eject track
  - add slicer LEDs for beat count as an "experimental" feature
  - code improvements to send LED Midi signals only when needed
  - some more minor code cleaning and improvements

**Release for Mixxx 2.2.4**
  - initial release with most functions working
  - secondary PAD functions need to be implemented yet

### Under investigation / development
  - several SLIP mode improvements. With activated SLIP mode it will be switched off automatically and therefore jump to the original time position inside the track after:
    - scratching
    - after Hot Cue jump
    - after backspin
  - changed (simplified) jog calculations
  - changed scratch parameters
  - stop to play current sampler when a new one is triggered
  - Rate Range change now considers start point from Mixxx preferences for changing range up and down

### Wish List

All additional wishes will be listed here (help appreciated):

  - let Platter Ring LEDs flash during the last minute (or other time
    period) of a track
  - colored Hot Cue
  - Secondary PAD functions

### Contact, DJ Web Sites and Tutorials

If you like to contact me then please visit [the
Forum](https://mixxx.discourse.group/t/denon-mc7000-mapping/18235) or contact
me on [Facebook](http://www.facebook.com/OsZ.DJ/).

To listen sets made with this MC7000 using MIXXX please visit
me on [Mixcloud](http://www.mixcloud.com/DJ_OsZ/uploads/). You can also find me on [YouTube](https://www.youtube.com/channel/UClBxBvYLTkjcAeTga1g3h0A) providing Techno sets and Mixxx tutorials.

Listen 24/7 to Techno shows (recorded and live) directly on our website
[Techno Connection](https://www.technoconnection.com/radio-links-and-chat), at [Radio
Garden](https://radio.garden/listen/techno-connection/oosngiMz) or with the Android app [MüzikoOo](https://play.google.com/store/apps/details?id=com.dndmix.muzikooo)
