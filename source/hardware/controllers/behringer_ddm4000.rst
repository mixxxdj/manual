Behringer Digital Pro Mixer DDM4000
===================================

- `Manufacturer's product page <https://www.behringer.com/behringer/product?modelCode=P0167>`_
- `Forum thread <https://mixxx.discourse.group/t/ddm4000-controller-mapping/20045>`_

The DDM4000 is a 5-Channel Digital DJ Mixer with Sampler, 4 FX Sections, BPM Counters and MIDI
support. Each of the following sections can be configured separately to be used either for audio
or as MIDI controller:

- Channel 1-4 
- Microphone Channel
- Crossfader
- Sampler

The mixer contains no digital interfaces for audio or microphones.

.. versionadded:: 2.3

Compatibility
-------------

This controller contains a :term:`MIDI` interface with 5-pin DIN jacks In/Out/Thru. If your
soundcard does not offer DIN jacks, a separate USB/MIDI interface is required to use it
on GNU/Linux, Mac OS X, and Windows.

Setup
-----
Configure at least 1 mixer section as MIDI controller:

#. Long press the :hwlabel:`CONSOLE SETUP` knob
#. Select ``MIDI SETTINGS`` by turning and pressing the :hwlabel:`CONSOLE SETUP` knob
#. Select the sections that you want to use as MIDI controller
#. Press the :hwlabel:`ESC` button to exit MIDI Setup
#. To make the change persistent, save the settings in a user preset.
   See the controller manual for details.

Mapping Description
-------------------

Most controls behave just as you would expect:

Channel 1-4
- Volume
- Crossfader Assign
- PFL
- EQ Knobs
- EQ Buttons: Kill Switches

Microphone
- On/Off
- Talkover

Crossfader
- Crossfader

Sampler
- Volume
- PFL
- Play
- Mode: Toggles Loop
- Crossfader Assign
