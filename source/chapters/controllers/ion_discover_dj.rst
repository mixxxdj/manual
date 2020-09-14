ION Discover DJ
===============

The ION Discover DJ is a cheap budget MIDI controller meant to “discover DJ-ing” for people with a potential interest. It does not have a built in sound card, so a `splitter
cable <hardware%20compatibility#splitter%20cables>`__ or `separate sound card <hardware%20compatibility#USB%20sound%20cards>`__ is required to use headphones with it.

-  `Manufacturer’s product page <http://www.ionaudio.com/products/details/discover-dj>`__
-  `Forum thread <https://mixxx.discourse.group/t/ion-discover-dj-controller-possible-future-support/10284>`__

Compatibility
-------------

This controller is USB MIDI class compliant, so it is plug-and-play on all platforms without having to install any special drivers. The manufacturer’s page only mentions Windows and Mac but it’s
confirmed working on Linux as well.

Library browsing
----------------

The controls for library browsing are in the center of the controller.

====================== =========================================================================================
Control                Function
====================== =========================================================================================
Rotary encoder         Track selection
Load buttons           Loads currently highlighted track to the corresponding deck (only if no audio is playing)
Pushing rotary encoder Maximizes/minimizes the library
====================== =========================================================================================

Jog wheels
----------

The button in the center can be used to switch the jog wheels between search and scratch mode. In search mode, the jog wheels can be used to seek to different parts of a song when paused. When that
deck is playing, the jog wheels can be pushed/pulled to speed up/slow down the playback. This is useful for beatmatching.

Pressing the center button will put the jog wheels in scratch mode, which means that the deck in Mixxx will follow the absolute movement of the jog wheels. In this mode the Scratch button is lit.

Equalizers
----------

This controller only has a 2-band equalizer but Mixxx uses a 3-band EQ. Therefore, the volume knob has been mapped to the low EQ, the bass knob has been mapped to the mid EQ, and the treble knob has
been mapped to the high EQ. For controlling the volume of the decks, use the crossfader.

Other buttons
-------------

The pitch buttons will control the tempo which also controls the pitch, except when keylock is on (padlock icon on screen).

========== ================================================================== ================================
Button     Function                                                           Light
========== ================================================================== ================================
Sync       Matches the BPM of that deck to the song playing in the other deck Blinks according to the beatgrid
Rev        While held the deck plays in reverse                               only lights when pressed
CUE        Attached to the cue control in mixxx                               follows cue button on screen
play/pause Play/pause the deck                                                follows play button on screen
========== ================================================================== ================================

The behavior of the cue and play buttons can be configured `in Mixxx’s preferences <http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes>`__.
