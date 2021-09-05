.. _behringer-ddm4000:

Behringer Digital Pro Mixer DDM4000
===================================

.. figure:: ../../_static/controllers/behringer_ddm4000_page1_mixer.svg
   :align: center
   :width: 90%
   :figwidth: 100%
   :alt: Behringer DDM4000 (schematic view)
   :figclass: pretty-figures

   Behringer DDM4000 (schematic view)

The DDM4000 is a 5-Channel Digital DJ Mixer with Sampler, 4 FX Sections, BPM Counters and MIDI
support. Each of the following sections can be configured separately to be used either for audio
or as MIDI controller:

* Channel 1-4
* Microphone Channel
* Crossfader
* Sampler

The mixer contains no digital interfaces for audio or microphones.

* `Manufacturer's product page <https://www.behringer.com/behringer/product?modelCode=P0167>`_
* `User Manual <https://mediadl.musictribe.com/media/sys_master/h1f/h4d/8849404887070.pdf>`_
* `Forum thread <https://mixxx.discourse.group/t/ddm4000-controller-mapping/20045>`_

.. versionadded:: 2.3

Compatibility
-------------

This controller contains a :term:`MIDI` interface with 5-pin DIN jacks In/Out/Thru. If your
soundcard does not offer DIN jacks, a separate USB/MIDI interface is required to use it
on GNU/Linux, Mac OS X, and Windows.

Setup
-----
Configure the affected mixer sections as MIDI controller:

#. Long press the :hwlabel:`CONSOLE SETUP` knob
#. Select ``MIDI SETTINGS`` by turning and pressing the :hwlabel:`CONSOLE SETUP` knob
#. Enable MIDI for the following sections:
   * Microphone
   * Crossfader
   * Sampler
   * Channel 1
   * Channel 4
#. Press the :hwlabel:`ESC` button to exit MIDI Setup
#. To make the change persistent, save the settings in a user preset.
   See the controller manual for details.

Controller Mapping
------------------

A schematic drawing with the control numbers that are used here can be found on the specified page in the User Manual in the Links section.

.. _behringer-ddm4000-stereochannels:

Stereo channels 1 – 4 (p. 6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/behringer_ddm4000_page6_stereo_channels.svg
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Behringer DDM4000 (stereo channels section)
   :figclass: pretty-figures

   Stereo channels strips

Stereo channels 2 & 3
^^^^^^^^^^^^^^^^^^^^^

The inner channels 2 & 3 contain default controls for Deck 1 & 2:

* Channel 2 controls Deck 1.
* Channel 3 controls Deck 2.

+-----+---------------------------------------------------------+-------------------------------------------------------------------------+
| No. | Control                                                 | Function                                                                |
+=====+=========================================================+=========================================================================+
|  4  | :hwlabel:`HIGH` / :hwlabel:`MID` / :hwlabel:`LOW` knobs | Adjust high/mid/low-frequencies.                                        |
+-----+---------------------------------------------------------+-------------------------------------------------------------------------+
|  6  | :hwlabel:`P1` / :hwlabel:`P2` / :hwlabel:`P3` buttons   | Toggle the kill function for high/mid/low-frequencies.                  |
+-----+---------------------------------------------------------+-------------------------------------------------------------------------+
|  7  | :hwlabel:`PFL` button                                   | Toggle headphone pre-fader listening.                                   |
+-----+---------------------------------------------------------+-------------------------------------------------------------------------+
|  8  | Channel faders                                          | Adjust the output volume.                                               |
+-----+---------------------------------------------------------+-------------------------------------------------------------------------+
| 10  | :hwlabel:`CF ASSIGN` button                             | Assign the channel to either side of the crossfader.                    |
+-----+---------------------------------------------------------+-------------------------------------------------------------------------+

Stereo channels 1 & 4
^^^^^^^^^^^^^^^^^^^^^

The outer channels 1 & 4 contain effect controls for Deck 1 & 2:

* Channel 1 controls Deck 1.
* Channel 4 controls Deck 2.

+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| No. | Control                                               | Function                                                                |
+=====+=======================================================+=========================================================================+
|  4  | :hwlabel:`LOW` knob                                   | - Rotate: Increases or decreases the size of the current loop in beats. |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
|  4  | :hwlabel:`MID` knob                                   | - Rotate: Moves the current loop left or right.                         |
|     |                                                       | - Shift + Rotate: Ignore the movement, do nothing.                      |
|     |                                                       |   This allows to continue moving the loop after the knob has reached    |
|     |                                                       |   the end of its physical range.                                        |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
|  4  | :hwlabel:`HIGH` knob                                  | - Rotate: Increases or decreases the number of beats to move the loop.  |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
|  5  | :hwlabel:`MODE` button                                | - Press: Toggle shift.                                                  |
|     |                                                       |                                                                         |
|     |                                                       | Shift changes the behaviour of controls as described on this page, and  |
|     |                                                       | additionally the behaviour of the Effect Units. See                     |
|     |                                                       | `Standard Effects Mapping                                               |
|     |                                                       | <https://github.com/mixxxdj/mixxx/wiki/Standard%20Effects%20Mapping>`_  |
|     |                                                       | for details.                                                            |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
|  6  | :hwlabel:`P3` button                                  | - Press: Toggle a rolling loop while pressed. Playback continues where  |
|     |                                                       |   the track would have been if it had not been temporarily reversed.    |
|     |                                                       | - Shift + Press: Toggle a loop that ends at the current play position.  |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
|  6  | :hwlabel:`P2` button                                  | - Press: Toggle rolling reverse playback while pressed. Playback        |
|     |                                                       |   continues where the track would have been if it had not been          |
|     |                                                       |   temporarily reversed.                                                 |
|     |                                                       | - Shift + Press: Toggle reverse playback.                               |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
|  6  | :hwlabel:`P1` button                                  | - Press: Toggle Echo Roll effect.                                       |
|     |                                                       | - Shift + Press: Toggle vinyl control mode.                             |
|     |                                                       |                                                                         |
|     |                                                       | The Echo Roll effect enables echo and filter while muting the channel.  |
|     |                                                       |                                                                         |
|     |                                                       | .. note:: Requirement: Effect Unit 1 holds Echo in Slot 1 and Filter in |
|     |                                                       |   Slot 2.                                                               |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
|  7  | :hwlabel:`PFL` button                                 | - Press: Reset the key.                                                 |
|     |                                                       | - Shift + Press: Toggle Keylock.                                        |
|     |                                                       | - LED: Show Keylock state.                                              |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
|  8  | Channel faders                                        | - Press: Adjust the key.                                                |
|     |                                                       |                                                                         |
|     |                                                       | Raising the fader raises the key, lowering the fader lowers the key.    |
|     |                                                       | When the fader position does not match the deck's key, movement is      |
|     |                                                       | ignored until the center position is crossed (soft-takeover).           |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 10  | :hwlabel:`CF ASSIGN` button                           | - Press: Toggle assignment of Effect Unit 1 or 2.                       |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+


.. _behringer-ddm4000-microphonechannel:

Microphone (p. 6)
~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/behringer_ddm4000_page6_microphone_channel.svg
   :align: center
   :width: 35%
   :figwidth: 100%
   :alt: Behringer DDM4000 (microphone channel section)
   :figclass: pretty-figures

   Microphone channel

The MIC section controls Effect Unit 1. See
`Standard Effects Mapping <https://github.com/mixxxdj/mixxx/wiki/Standard%20Effects%20Mapping>`_
for details.

+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| No. | Control                                               | Function                                                                |
+=====+=======================================================+=========================================================================+
| 14  | :hwlabel:`HIGH` knob                                  | - Rotate: Control the parameter of effect 1.                            |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 14  | :hwlabel:`MID` knob                                   | - Rotate: Control the parameter of effect 2.                            |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 14  | :hwlabel:`LOW` knob                                   | - Rotate: Control the parameter of effect 3.                            |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 15  | :hwlabel:`ON/OFF` button                              | - Press: Toggle Effect Unit 1.                                          |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 16  | :hwlabel:`MIC SETUP` button                           | - Press: Toggle effect focus mode.                                      |
|     |                                                       | - Shift + Press: Toggle Effect Unit.                                    |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 17  | :hwlabel:`XMC ON` button                              | - Press: Toggle effect 1.                                               |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 18  | :hwlabel:`MIC FX ON` button                           | - Press: Toggle effect 2.                                               |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 19  | :hwlabel:`TALK ON` button                             | - Press: Toggle effect 3.                                               |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+

.. _behringer-ddm4000-crossfader:

Crossfader section (p. 7)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/behringer_ddm4000_page7_crossfader.svg
   :align: center
   :width: 90%
   :figwidth: 100%
   :alt: Behringer DDM4000 (crossfader section)
   :figclass: pretty-figures

   Crossfader section

The EQ buttons in this section control deck effects:

* Side A (Left) controls Deck 1.
* Side B (Right) controls Deck 2.

+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| No. | Control                                               | Function                                                                |
+=====+=======================================================+=========================================================================+
| 20  | Crossfader                                            | Fade between the signals that are assigned to its two sides A and B.    |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 21  | :hwlabel:`CF ON` button                               | Toggle crossfader function. When disabled, the crossfader control in    |
|     |                                                       | the Mixxx user interface is hidden.                                     |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 22  | :hwlabel:`LOW` button                                 | - Press: Toggle a rolling loop while pressed. Playback continues where  |
|     |                                                       |   the track would have been if it had not been temporarily reversed.    |
|     |                                                       | - Shift + Press: Toggle a loop that ends at the current play position.  |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 22  | :hwlabel:`MID` button                                 | - Press: Toggle rolling reverse playback while pressed. Playback        |
|     |                                                       |   continues where the track would have been if it had not been          |
|     |                                                       |   temporarily reversed.                                                 |
|     |                                                       | - Shift + Press: Toggle reverse playback.                               |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 22  | :hwlabel:`HIGH` button                                | - Press: Toggle Echo Roll effect.                                       |
|     |                                                       | - Shift + Press: Toggle vinyl control mode.                             |
|     |                                                       |                                                                         |
|     |                                                       | The Echo Roll effect enables echo and filter while muting the channel.  |
|     |                                                       |                                                                         |
|     |                                                       | .. note:: Requirement: Effect Unit 1 holds Echo in Slot 1 and Filter in |
|     |                                                       |   Slot 2.                                                               |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 23  | :hwlabel:`FULL FREQ` button                           | - Press: Toggle shift.                                                  |
|     |                                                       |                                                                         |
|     |                                                       | Shift changes the behaviour of controls as described on this page, and  |
|     |                                                       | additionally the behaviour of the Effect Units. See                     |
|     |                                                       | `Standard Effects Mapping                                               |
|     |                                                       | <https://github.com/mixxxdj/mixxx/wiki/Standard%20Effects%20Mapping>`_  |
|     |                                                       | for details.                                                            |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 24  | :hwlabel:`CURVE` knob                                 | Adjust the response of the crossfader.                                  |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 25  | :hwlabel:`REVERSE HOLD` button                        | Toggle a permanent reverse of the crossfader sides A and B.             |
|     |                                                       | This means that A and B are interchanged.                               |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 26  | :hwlabel:`REVERSE TAP` button                         | Toggle a momentary reverse of the crossfader sides A and B. This means  |
|     |                                                       | that A and B are interchanged as long as the TAP push button is held    |
|     |                                                       | down.                                                                   |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+

.. _behringer-ddm4000-sampler:

Sampler (p. 8)
~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/behringer_ddm4000_page8_sampler.svg
   :align: center
   :width: 35%
   :figwidth: 100%
   :alt: Behringer DDM4000 (sampler)
   :figclass: pretty-figures

   Sampler section

.. note:: The Dry/Wet button does not control the sampler but Effect Unit 1.

+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| No. | Control                                               | Function                                                                |
+=====+=======================================================+=========================================================================+
| 55  | :hwlabel:`VOLUME/MIX` knob                            | - Rotate: Adjusts the mixing of the dry (input) signal with the wet     |
|     |                                                       |   (output) signal of Effect Unit 1.                                     |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 57  | :hwlabel:`PFL` button                                 | - Press: Toggle headphone pre-fader listening for sampler 1.            |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 58  | :hwlabel:`SAMPLE LENGTH` buttons                      | - Press: Adjust the beatloop size of sampler 1.                         |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 61  | :hwlabel:`MODE` buttons for bank 1/2                  | - Press: Select the playback type for the selected sampler (Reverse or  |
|     |                                                       |   Loop). A short press toggles the Reverse function, a long press       |
|     |                                                       |   toggles the Loop function.                                            |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 62  | :hwlabel:`PLAY/OUT` buttons for bank 1/2              | - Press: Start or stop playback for the selected sampler. When the Loop |
|     |                                                       |   function is disabled, the sample is only played back while the button |
|     |                                                       |   is pressed.                                                           |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 63  | :hwlabel:`SMP FX ON` button                           | - Press: Toggle Effect Unit 1 for sampler 1.                            |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
| 65  | :hwlabel:`CF ASSIGN` button                           | - Press: Assign sampler 1 to either side of the crossfader.             |
+-----+-------------------------------------------------------+-------------------------------------------------------------------------+
