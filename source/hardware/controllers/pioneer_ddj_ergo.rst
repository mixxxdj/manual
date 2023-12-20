Pioneer DDJ-ERGO
================

The Pioneer DDJ-ERGO is a 4 deck USB :term:`MIDI` controller with a built in soundcard. The current mapping for Mixxx allows it to control 2 decks and video controls are not supported. The mapping was created as close as possible as the original mapping.

-  `Manufacturer’s product page <https://www.pioneerdj.com/en/product/controller/archive/ddj-ergo/black/overview/>`__
-  `Forum thread <https://mixxx.discourse.group/t/pioneer-ergo-mapping/28643>`__
-  `GitHub pull request <https://github.com/mixxxdj/mixxx/pull/12456>`__

.. versionadded:: 2.4

Drivers
-------

Windows
~~~~~~~

Windows 10, Windows 8.1 and Windows 7 are supported. You can download the latest drivers and firmware from http://www.pioneerdj.com/en/support/software/ddj-ergo.

Mac OS X & Linux
~~~~~~~~~~~~~~~~

You don’t need any drivers on Mac OS X and Linux.

The controller supports Mac OS X 10.14 and up.

Usage
-----

Audio configuration
~~~~~~~~~~~~~~~~~~~

Configure channels 1-2 for main output and channels 3-4 for headphones. An input is provided and shared between Mic and Aux. This input is mixed in software and needs to be configured with channels 1-2.

Library browsing
~~~~~~~~~~~~~~~~

The controls for library browsing can be found in the center top of the controller.

=========================== ===================================================================================================================================================
Control                     Function
=========================== ===================================================================================================================================================
Rotary knob                 Track selection
Load buttons                Loads currently highlighted track to the corresponding deck
Pushing rotary knob         Switch between directories and files
Shift + rotary knob         Sidebar section open and close directories
Shift + pushing rotary knob toggle expanding library section
=========================== ===================================================================================================================================================

Switching between decks
~~~~~~~~~~~~~~~~~~~~~~~

Click the dedicated buttons on the top of the controller, labeled with A-B-C-D. Currently only decks A and B are mapped.

Volume, equalizers & filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Between the decks the usual faders, crossfader and EQ knobs can be found. A filter knob is also available.

Knobs are available for the master and headphones level. These are functional and interact directly with Mixxx.

Jogwheels, tempo & vinyl mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a deck is paused, the jogwheel allows you to browse through a track. If you want to browse faster, hold shift while using the jogwheel.

When a deck is playing, using the jogwheel allows you to temporarily change the tempo of the playing track.

The tempo slider allows changing the tempo of each deck. This normally changes the pitch of a track, you can make the pitch stay constant by pressing the “key lock / tempo range” button.

Vinyl mode makes the jogwheels emulate the way turntables work. Vinyl mode can be toggled by pressing the “vinyl / pulse mode” button. Touching the outer plastic ring of the jogwheel will make it behave as
with vinyl mode off. Touching the disc simulates touching the vinyl record, so just putting your hand on it will stop the “vinyl”. You can scratch in a similar way as with turntables in vinyl
mode.

Hot Cues and Samplers
~~~~~~~~~~~~~~~~~~~~~

Over the jogwheels there are sections allowing to control hot cues and samples.

============================== ===================================================================================================================================================
Control                        Function
============================== ===================================================================================================================================================
Hot Cue 1-4                    Set hot cue on first push, go to hot cue and play on next pushes
Samplers                       Play/stop sample
Shift + Hot Cue 1-4            Delete hot cue
Shift + Samplers               Go to start and play sample
Sample Vol Knob Rotate         Adjust volume of the last sample played
Sample Vol Knob Push           Play/stop last sample played
Shift + Sample Vol Knob Rotate Select sample to control with the knob
Shift + Sample Vol Knob Push   View/hide samplers
============================== ===================================================================================================================================================

FX - FX1/FX2
~~~~~~~~~~~~

Over the samplers there are sections allowing to control effects.

============================== ===================================================================================================================================================
Control                        Function
============================== ===================================================================================================================================================
FX 1-2                         Toggle on/off effects in slots 1 or 2 accordingly
FX ON                          Turn on/off selected effect
FX1/2 1-3 buttons              Select which effect slot to manipulate
Control                        Select effect in corresponding slot
FX1/2 1 knob                   Manipulate meta knob for the selected effect slot
FX1/2 2-3 knobs                Not mapped
============================== ===================================================================================================================================================

Pulse Mode
~~~~~~~~~~

Pulse Mode can be activated by holding shift + “vinyl / pulse mode” button.
This mode displays blue lights on the jogwheel. Its intensity depends on how aligned the beats of both tracks are.
