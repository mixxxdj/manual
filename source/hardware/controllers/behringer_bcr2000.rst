.. _behringer-b-control-bcr2000:

Behringer BCR2000
=================

.. figure:: ../../_static/controllers/behringer_bcr2000.svg
   :align: center
   :width: 90%
   :figwidth: 100%
   :alt: Behringer BCR2000 (schematic view)
   :figclass: pretty-figures

   Behringer BCR2000 (schematic view)

- `Manufacturer's product page <https://www.behringer.com/behringer/product?modelCode=P0245>`_
- `Forum thread <https://mixxx.discourse.group/t/behringer-b-control-bcr2000/20287>`_

The B-CONTROL BCR2000 is a general-purpose :term:`USB` :term:`MIDI` controller containing 20
buttons, 24 rotary encoders and 8 push encoders. Every control is backed by LEDs that show the
current value. As a pure MIDI controller it contains no interfaces for audio or microphones.

The controller can be be configured extensively.
It offers 32 presets that may be programmed by the user.

.. versionadded:: 2.3

Compatibility
-------------

This controller is a class compliant USB MIDI and audio device, so it can be used without any
special drivers on GNU/Linux, Mac OS X, and Windows.

Setup
-----
Controller Preset
^^^^^^^^^^^^^^^^^
The default mapping works out-of-the-box for the factory settings of controller preset 1.

If you don't want to use this preset, you can choose one of the following options:

#. Load the dump file ``bcr_Only_Controllers.syx`` via Sysex to any other preset slot and update
   the preset number in the ``init`` function in the file ``Behringer-BCR2000-scripts.js``.
   The dump file and instructions how to install it in the controller is available on the
   manufacturer's webpage.
#. Factory reset the controller.

Button Behaviour
^^^^^^^^^^^^^^^^
It is recommended, but not required, to change the button behaviour from *Toggle On* (default)
to *Toggle Off*. Both behaviours send an ``On`` message on button press, but the action to
send an ``Off`` message is different: *Toggle Off* responds to a button release while *Toggle On*
ignores the release and requires a second press. To change the behaviour:

#. Hold :hwlabel:`EDIT`, press a button, then release both
#. Turn the :hwlabel:`MODE` encoder until the display shows ``toFF``
#. Press the :hwlabel:`EXIT` button

To make the change persistent, press *Store* twice. See the controller manual for details.

Mapping Description
-------------------
The BCR2000 is a general purpose controller that allows different mappings.

The file ``Behringer-BCR2000-scripts.js`` contains a default mapping which works
out-of-the-box for a factory-reset controller, but may be customized freely according to your needs.

The controls are divided into five parts:

- Top left area (4 push encoders + 4 buttons): loop, reverse & pitch controls for Deck 1
- Top right area (4 push encoders + 4 buttons): loop, reverse & pitch controls for Deck 2
- Middle left area (4 buttons + 4 encoders): controls for Effect Unit 1
- Middle right area (4 buttons + 4 encoders): controls for Effect Unit 2
- Bottom right area (4 buttons): controls for assignment of effect units to decks

.. figure:: ../../_static/controllers/behringer_bcr2000_overlay.svg
  :width: 600

+-------------------------------------------------------+-----------------------------------------------------------------------------+
| Control                                               | Description                                                                 |
+------------------+---------------+--------------------+                                                                             |
| Location         | Affects       | Hardware control   |                                                                             |
+==================+===============+====================+=============================================================================+
| Push Encoder Row | Deck 1        | Encoder 1          | - Rotate: Manipulates the key of the track in semitones.                    |
|                  |               | (:hwlabel:`TYPE`)  | - Push: Resets the key to the original track key.                           |
|                  +---------------+--------------------+                                                                             |
|                  | Deck 2        | Encoder 5          |                                                                             |
|                  |               | (:hwlabel:`VAL 2`) |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Deck 1        | Encoder 2          | - Rotate: Increases or decreases the size of the current loop in beats.     |
|                  |               | (:hwlabel:`CH`)    |                                                                             |
|                  +---------------+--------------------+                                                                             |
|                  | Deck 2        | Encoder 6          |                                                                             |
|                  |               | (:hwlabel:`VAL 2`) |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Deck 1        | Encoder 3          | - Rotate: Moves the current loop left or right.                             |
|                  |               | (:hwlabel:`PAR`)   |                                                                             |
|                  +---------------+--------------------+                                                                             |
|                  | Deck 2        | Encoder 7          |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Deck 1        | Encoder 4          | - Rotate: Increases or decreases the number of beats to move the loop.      |
|                  |               | (:hwlabel:`VAL 1`) |                                                                             |
|                  +---------------+--------------------+                                                                             |
|                  | Deck 2        | Encoder 8          |                                                                             |
+------------------+---------------+--------------------+-----------------------------------------------------------------------------+
| Button Row 1     | Deck 1        | Button 1           | - Press: Toggles keylock.                                                   |
|                  +---------------+--------------------+ - Shift + Press: Toggles vinyl control mode.                                |
|                  | Deck 2        | Button 5           |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Deck 1        | Button 2           | - Press: Toggles a loop that ends at the current play position.             |
|                  +---------------+--------------------+ - Shift + Press: Toggles a rolling loop. Playback will resume where         |
|                  | Deck 2        | Button 6           |   the track would have been if it had not entered the loop.                 |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Deck 1        | Button 3           | - Press: Toggles reverse playback.                                          |
|                  +---------------+--------------------+ - Shift + Press: Toggles rolling reverse playback. Playback continues       |
|                  | Deck 2        | Button 7           |   where the track would have been if it had not been temporarily reversed.  |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | All controls  | Button 4           | - Press: Toggles shift.                                                     |
|                  +---------------+--------------------+   Shift changes the behaviour of controls as described in this table, and   |
|                  | All controls  | Button 8           |   additionally the behaviour of the effect units. See                       |
|                  |               |                    |   `Standard Effects Mapping                                                 |
|                  |               |                    |   <https://github.com/mixxxdj/mixxx/wiki/Standard%20Effects%20Mapping>`_    |
|                  |               |                    |   for details.                                                              |
|                  |               |                    |                                                                             |
|                  |               |                    | .. note:: Both Shift buttons have the same effect, they are not             |
|                  |               |                    |   deck-specific. This design decision was made to keep the layout symmetric |
|                  |               |                    |   so that you don't have to press a button on the left side when you're     |
|                  |               |                    |   working on the right side.                                                |
+------------------+---------------+--------------------+-----------------------------------------------------------------------------+
| Button Row 2     | Effect Unit 1 | Button 1           | - Press: Toggles effect focus mode.                                         |
|                  +---------------+--------------------+ - Shift + Press: Toggles effect unit.                                       |
|                  | Effect Unit 2 | Button 5           |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Effect Unit 1 | Button 2           | - Press: Toggles parameter button 1.                                        |
|                  +---------------+--------------------+                                                                             |
|                  | Effect Unit 2 | Button 6           |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Effect Unit 1 | Button 3           | - Press: Toggles parameter button 2.                                        |
|                  +---------------+--------------------+                                                                             |
|                  | Effect Unit 2 | Button 7           |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Effect Unit 1 | Button 4           | - Press: Toggles parameter button 3.                                        |
|                  +---------------+--------------------+                                                                             |
|                  | Effect Unit 2 | Button 8           |                                                                             |
+------------------+---------------+--------------------+-----------------------------------------------------------------------------+
| Encoder Row 1    | Effect Unit 1 | Encoder 1          | - Rotate: Adjusts the mixing of the dry (input) signal with the wet         |
|                  +---------------+--------------------+   (output) signal of the effect unit.                                       |
|                  | Effect Unit 2 | Encoder 5          |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Effect Unit 1 | Encoder 2          | - Rotate: Controls the parameter of effect 1.                               |
|                  +---------------+--------------------+                                                                             |
|                  | Effect Unit 2 | Encoder 6          |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Effect Unit 1 | Encoder 3          | - Rotate: Controls the parameter of effect 2.                               |
|                  +---------------+--------------------+                                                                             |
|                  | Effect Unit 2 | Encoder 7          |                                                                             |
+                  +---------------+--------------------+-----------------------------------------------------------------------------+
|                  | Effect Unit 1 | Encoder 4          | - Rotate: Controls the parameter of effect 3.                               |
|                  +---------------+--------------------+                                                                             |
|                  | Effect Unit 2 | Encoder 8          |                                                                             |
+------------------+---------------+--------------------+-----------------------------------------------------------------------------+
| Button Box Row 1 | Deck 1        | Left Button        | - Press: Toggles assignment of Effect Unit 1.                               |
|                  +---------------+--------------------+                                                                             |
|                  | Deck 2        | Right Button       |                                                                             |
+------------------+---------------+--------------------+-----------------------------------------------------------------------------+
| Button Box Row 2 | Deck 1        | Left Button        | - Press: Toggles assignment of Effect Unit 2.                               |
|                  +---------------+--------------------+                                                                             |
|                  | Deck 2        | Right Button       |                                                                             |
+------------------+---------------+--------------------+-----------------------------------------------------------------------------+

Overlay
^^^^^^^
Overlay to print on cardboard or paper for lamination:

- :download:`PDF, DIN A4<../../_static/controllers/behringer_bcr2000_overlay_a4.pdf>`
- :download:`PDF, DIN A3<../../_static/controllers/behringer_bcr2000_overlay_a3.pdf>`
- :download:`ODG<../../_static/controllers/behringer_bcr2000_overlay.odg>` (LibreOffice)
- :download:`SVG<../../_static/controllers/behringer_bcr2000_overlay_a3_unlabeled.svg>` (without labels)
