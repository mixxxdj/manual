.. _yaeltex-minimixxx:

Yaeltex MiniMixxx
=================

.. sectionauthor::
  Owen Williams <owilliams at mixxx.org>

The Yaeltex MiniMixxx is a compact, 2-deck DJ controller designed exclusively
for Mixxx. Unlike most small form-factor DJ controllers which sacrifice
important functions, the MiniMixxx provides access to all of the critical parts
of DJing: full size EQ and quick FX knobs, pitch sliders, channel faders and
track gain, playback controls including sync nudging, looping, an FX bank, 4
hotcues per deck, 8 samplers, sync lock, keylock, library navigation, and master
output settings. Button mode layers are intelligently laid out and road-tested
for maximum flexibility during performance, with bold RGB colors indicating
current modes. The visualization of channel volume and virtual record spinning
indicators makes the MiniMixxx an eye-catching wonder in the DJ booth.

The MiniMixxx can run on USB bus power. Using a separate power supply increases
the brightness of the LEDs. The MiniMixxx does not have a built-in sound card.

.. versionadded:: 2.4.0

Compatibility
-------------

Setup
~~~~~~~~~~

The MiniMixxx is a USB class compliant MIDI device.  To work correctly with this
mapping, you need to load the custom Yaeltex layout file onto your controller:

1. Download the :download:`MiniMixxx Layout Configuration<../../_static/controllers/MiniMixxx.ytx>`.
1. Go to `Yaeltex Kilowhat <https://kilowhat.yaeltex.com/>`_ configuration site.
1. Select your controller and click "Load From Desktop"
1. Select the downloaded layout file.
1. Click Send to Device.

Inside Mixxx, open the preferences and select the Yaeltex Minimixxx from the list of controller presets.

Mapping description
-------------------

Mixer
~~~~~

The primary mixer knobs and sliders are single-purpose. This includes:

========  ==================================================  ==========================================
No.       Control                                             Function
========  ==================================================  ==========================================
1         :hwlabel:`Hi`                                       High frequency EQ Adjustment
2         :hwlabel:`Mid`                                      Midrange EQ Adjustment
3         :hwlabel:`Low`                                      Low frequency EQ Adjustment
4         :hwlabel:`FX`                                       Turn to engage Quick FX for each channel.
5         :hwlabel:`Level`                                    Slide to adjust channel level
6         :hwlabel:`Pitch`                                    Slide to adjust deck speed. When :hwlabel:`SHIFT` is held, has no effect. When :hwlabel:`KEYLOCK` is held, adjusts musical pitch.
========  ==================================================  ==========================================

Buttons Overview
~~~~~~~~~~~~~~~~

Almost all the other controls on the MiniMixxx have more than one function. It
helps to understand how the buttons are divided

.. csv-table::
   :header: "Deck 1", "", "", "Deck 2", "", "", "Layer Buttons", ""
   :widths: 1 1 1 1 1 1 1 1

   ":hwlabel:`1`", ":hwlabel:`2`", ":hwlabel:`3`", ":hwlabel:`4`", ":hwlabel:`5`", ":hwlabel:`6`", ":hwlabel:`7`", ":hwlabel:`8`"
   ":hwlabel:`9`", ":hwlabel:`10`", ":hwlabel:`11`", ":hwlabel:`12`", ":hwlabel:`13`", ":hwlabel:`14`", ":hwlabel:`15`", ":hwlabel:`16`"

There are 16 buttons arranged in three blocks.  The buttons are numbered 1-16,
starting in the upper left across the top row, and then counting the bottom row.
So the upper left button is 1, the upper right button is 8, the lower left
button is 9, the lower right button is 16.


  - Deck 1 uses the leftmost 6 buttons in a 3x2 grid.

  - Deck 2 uses the next block of 6 buttons.

  - The last 4 buttons enable certain layers and modes. These are buttons
    :hwlabel:`7`, :hwlabel:`8`, :hwlabel:`15`, and :hwlabel:`16`.

  - Button :hwlabel:`16` in the lower right is always the :hwlabel:`SHIFT` button.

  - The upper left button of each track block (number :hwlabel:`1` and
    :hwlabel:`4`) are always :hwlabel:`CUE` buttons for track 1 and 2, respectively.

  - The lower left button of each track block (number :hwlabel:`9` and
    :hwlabel:`12`) are always :hwlabel:`PLAY` buttons for track 1 and 2.

  - Each deck has a small grid of 4 buttons to the right of the :hwlabel:`PLAY`
    and :hwlabel:`CUE` buttons for that deck.  These are buttons :hwlabel:`2`,
    :hwlabel:`3`, :hwlabel:`10`, :hwlabel:`11`; and :hwlabel:`5`, :hwlabel:`6`,
    :hwlabel:`13`, :hwlabel:`14`.

Constant buttons:

.. csv-table::
   :header: "Deck 1", "", "", "Deck 2", "", "", "Layer Buttons", ""
   :widths: 1 1 1 1 1 1 1 1

   ":hwlabel:`CUE`", "", "", ":hwlabel:`CUE`", "", "", "", ""
   ":hwlabel:`PLAY`", "", "", ":hwlabel:`PLAY`", "", "", "", ":hwlabel:`SHIFT`"

Default Layer
~~~~~~~~~~~~~

Because the MiniMixxx is so compact, most controls have more than one function
depending on what Layer is selected. The Default Layer will be active when the
controller starts up.

.. csv-table::
   :header: "Encoder 1", "Encoder 2", "Encoder 3", "Encoder 4"
   :widths: 1 1 1 1
   :align: center

   ":hwlabel:`JOG 1`", ":hwlabel:`PREGAIN 1`", ":hwlabel:`PREGAIN 2`", ":hwlabel:`JOG 2`"

.. Spacer

.. csv-table::
   :header: "Deck 1", "", "", "Deck 2", "", "", "Layer Buttons", ""
   :widths: 1 1 2 1 1 2 1 1

   ":hwlabel:`CUE`", ":hwlabel:`KEYLOCK`", ":hwlabel:`FX`", ":hwlabel:`CUE`", ":hwlabel:`KEYLOCK`", ":hwlabel:`FX`", ":hwlabel:`HOTCUES-1` / :hwlabel:`FX`", ":hwlabel:`HOTCUES-2` / :hwlabel:`SAMPLERS`"
   ":hwlabel:`PLAY`", ":hwlabel:`SYNC`", ":hwlabel:`LOOP`", ":hwlabel:`PLAY`", ":hwlabel:`SYNC`", ":hwlabel:`LOOP`", ":hwlabel:`LIBRARY` / :hwlabel:`MAIN GAIN`", ":hwlabel:`SHIFT`"

The Default Layer is active when the controller starts, and represents the
default actions for each button.  Some buttons activate other layers.  When a
layer is selected, pushing another layer button will enable that layer instead.
Or, press the currently-activated layer button to disable it.

In the Default Layer, the encoders above the Pitch sliders will have an animated
spinning indicator, and the encoders above the Level sliders will show an
animated VU meter for each deck.

===============================  ========  =====================================
Button                           Category  Function
===============================  ========  =====================================
:hwlabel:`2`                     Deck 1    :hwlabel:`KEYLOCK`. Tapping this button toggles keylock. Press and hold this button and move the :hwlabel:`PITCH` slider to adjust musical key without changing track speed.
:hwlabel:`3`                     Deck 1    Toggles :hwlabel:`FX` Unit 1 for each deck.
:hwlabel:`10`                    Deck 1    :hwlabel:`SYNC`.  Tap to perform a one-off beatsync. Press and hold to enable Sync Lock.
:hwlabel:`11`                    Deck 1    Enables the :hwlabel:`LOOP` layer for each individual deck.
..
:hwlabel:`8`                     Deck 2    Enables the :hwlabel:`HOTCUE` layer for each deck.
:hwlabel:`5`                     Deck 2    :hwlabel:`KEYLOCK`. Tapping this button toggles keylock. Press and hold this button and move the :hwlabel:`PITCH` slider to adjust musical key without changing track speed.
:hwlabel:`6`                     Deck 2    Toggles :hwlabel:`FX` Unit 1 for each deck.
:hwlabel:`13`                    Deck 2    :hwlabel:`SYNC`.  Tap to perform a one-off beatsync. Press and hold to enable Sync Lock.
..
:hwlabel:`7`                     Deck 1    Enables the :hwlabel:`HOTCUE` layer for Deck 1.
:hwlabel:`8`                     Deck 2    Enables the :hwlabel:`HOTCUE` layer for Deck 2.
:hwlabel:`15`                    Layer     Enables the :hwlabel:`LIBRARY` layer. Hold :hwlabel:`SHIFT` and press to enable the :hwlabel:`MAIN GAIN` layer.
:hwlabel:`16`                    Layer     :hwlabel:`SHIFT`
===============================  ========  =====================================

==================  ================  ========================  ========================================
Encoder             Category          Action                    Function
==================  ================  ========================  ========================================
Encoder 1           Deck 1 Jog        Spin                      Jog forward and back, or nudge faster or slower if the track is playing.
..                  ..                :hwlabel:`SHIFT` + Spin   Seek forward a large distance in the track.
..                  ..                Press                     Creates a loop if not in a loop, or reloop toggle if the playhead is in the loop.
..                  ..                :hwlabel:`SHIFT` + Press  Does a beatloop roll.
Encoder 2           Deck 1 Pregain    Spin                      Adjust track pregain.
..                  ..                Press                     Toggle pfl.
..                  ..                :hwlabel:`SHIFT` + Press  Reset track pregain.
Encoder 3           Deck 2 Pregain    Spin                      Adjust track pregain.
..                  ..                Press                     Toggle pfl.
..                  ..                :hwlabel:`SHIFT` + Press  Reset track pregain.
Encoder 4           Deck 2 Jog        Spin                      Jog forward and back, or nudge faster or slower if the track is playing.
..                  ..                :hwlabel:`SHIFT` + Spin   Seek forward a large distance in the track.
..                  ..                Press                     Creates a loop if not in a loop, or reloop toggle if the playhead is in the loop.
..                  ..                :hwlabel:`SHIFT` + Press  Does a beatloop roll.
==================  ================  ========================  ========================================

If the track is clipping, the LED ring will flash bright red.

Loop Layers
~~~~~~~~~~~

.. csv-table::
   :header: "Encoder 1", "Encoder 2", "Encoder 3", "Encoder 4"
   :widths: 1 1 1 1
   :align: center

   ":hwlabel:`LOOP 1`", ":hwlabel:`BEATJUMP 1`", ":hwlabel:`LOOP 2`", ":hwlabel:`BEATJUMP 2`"

The :hwlabel:`LOOP` layer can be activated separately per-deck. When active, the
two encoders for the activated deck will turn green.

In the table below, the Left encoder for Deck 1 is above its pitch slider, Deck
2's is above its level slider. The Left encoders control loops, and the Right
encoders control beatjumping.

=============  ========================  ========================================
Encoder        Action                    Function
=============  ========================  ========================================
Left Encoder   Spin                      Adjusts loop size.
..             :hwlabel:`SHIFT` + Spin   Moves the loop by the Beatjump amount.
..             Press                     Creates a loop if not in a loop, or reloop toggle if the playhead is in the loop.
..             :hwlabel:`SHIFT` + Press  Reloop toggle.
Right Encoder  Spin                      Adjust beatjump size.
..             :hwlabel:`SHIFT` + Spin   Jump the playhead forward / backward.
..             Press                     Activate a beatloop roll.
..             :hwlabel:`SHIFT` + Press  Reloop and stop.
=============  ========================  ========================================

Hotcue Layers
~~~~~~~~~~~~~

.. csv-table::
   :header: "Deck 1", "", "", "Deck 2", "", "", "Layer Buttons", ""
   :widths: 1 1 2 1 1 2 1 1

   ":hwlabel:`CUE`", ":hwlabel:`HOTCUE 1`", ":hwlabel:`HOTCUE 2`", ":hwlabel:`CUE`", ":hwlabel:`HOTCUE 1`", ":hwlabel:`HOTCUE 2`", ":hwlabel:`HOTCUES-1` / :hwlabel:`FX`", ":hwlabel:`HOTCUES-2` / :hwlabel:`SAMPLERS`"
   ":hwlabel:`PLAY`", ":hwlabel:`HOTCUE 3`", ":hwlabel:`HOTCUE 4`", ":hwlabel:`PLAY`", ":hwlabel:`HOTCUE 3`", ":hwlabel:`HOTCUE 4`", ":hwlabel:`LIBRARY` / :hwlabel:`MAIN GAIN`", ":hwlabel:`SHIFT`"


The :hwlabel:`HOTCUE` layers are also activated separately per deck.  When
activated, the four buttons to the right of :hwlabel:`PLAY` and :hwlabel:`CUE`
for each deck become hotcue buttons. Pressing the hotcue button activates the
hotcue.  Hold :hwlabel:`SHIFT` and press to clear the hotcue.

Sampler Layer
~~~~~~~~~~~~~

.. csv-table::
   :header: "Deck 1", "", "", "Deck 2", "", "", "Layer Buttons", ""
   :widths: 1 1 2 1 1 2 1 1

   ":hwlabel:`CUE`", ":hwlabel:`SAMPLE 1`", ":hwlabel:`SAMPLE 2`", ":hwlabel:`CUE`", ":hwlabel:`SAMPLE 3`", ":hwlabel:`SAMPLE 4`", ":hwlabel:`HOTCUES-1` / :hwlabel:`FX`", ":hwlabel:`HOTCUES-2` / :hwlabel:`SAMPLERS`"
   ":hwlabel:`PLAY`", ":hwlabel:`SAMPLE 5`", ":hwlabel:`SAMPLE 6`", ":hwlabel:`PLAY`", ":hwlabel:`SAMPLE 7`", ":hwlabel:`SAMPLE 8`", ":hwlabel:`LIBRARY` / :hwlabel:`MAIN GAIN`", ":hwlabel:`SHIFT`"


When activated, all 8 buttons next to both sets of :hwlabel:`PLAY` and :hwlabel:`CUE`
buttons become sampler buttons.  Press any button to activate that sample.  Hold
:hwlabel:`SHIFT` and press to eject the sample.

FX Layer
~~~~~~~~

.. csv-table::
   :header: "Encoder 1", "Encoder 2", "Encoder 3", "Encoder 4"
   :widths: 1 1 1 1
   :align: center

   ":hwlabel:`FX META 1`", ":hwlabel:`FX META 2`", ":hwlabel:`FX META 3`", ":hwlabel:`FX SUPER`"


When FX layer is activated, the four encoders control Effect Unit 1. The left
three encoders adjust the :hwlabel:`META` knobs for the three effects in the
unit, and the rightmost encoder controls the :hwlabel:`SUPER` knob for the whole
unit. In FX mode, the encoders turn blue.

Pressing an encoder enables or disables the effect. Pressing the rightmost
encoder toggles the whole unit.

Library Layer
~~~~~~~~~~~~~

.. csv-table::
   :header: "Encoder 1", "Encoder 2", "Encoder 3", "Encoder 4"
   :widths: 1 1 1 1
   :align: center

   ":hwlabel:`VERTICAL FOCUS`", ":hwlabel:`SELECT 1`", ":hwlabel:`SELECT 2`", ":hwlabel:`HORIZONTAL FOCUS`"


When the Library layer is activated, the four encoders enable browsing of the
library. In Library mode, the encoders turn purple.

==================  ================  ========================  ========================================
Encoder             Category          Action                    Function
==================  ================  ========================  ========================================
Encoder 1           Library Focus     Spin                      Move library focus forward / backward.
..                  ..                :hwlabel:`SHIFT` + Spin   Seek forward a large distance in the track in Deck 1. This is useful for previewing tracks without leaving the library layer.
..                  ..                Press                     Activates "Go To Item", which opens or closes the tree view in the side panel.
Encoders 2 and 3    Scroll            Spin                      Scrolls up and down.
..                  ..                :hwlabel:`SHIFT` + Spin   Scrolls horizontally.
..                  ..                Press                     Load the selected track in either Deck 1 or 2, depending which knob you're using.
..                  ..                :hwlabel:`SHIFT` + Press  Ejects the currently loaded track.
Encoder 4           Horizontal Focus  Spin                      Scrolls horizontally.
..                  ..                :hwlabel:`SHIFT` + Spin   Seek forward a large distance in the track in Deck 2. This is useful for previewing tracks without leaving the library layer.
..                  ..                Press                     Activates "Go To Item", which opens or closes the tree view in the side panel.
==================  ================  ========================  ========================================

Main Gain Layer
~~~~~~~~~~~~~~~

.. csv-table::
   :header: "Encoder 1", "Encoder 2", "Encoder 3", "Encoder 4"
   :widths: 1 1 1 1
   :align: center

   ":hwlabel:`MAIN BALANCE`", ":hwlabel:`MAIN GAIN`", ":hwlabel:`HEAD GAIN`", ":hwlabel:`HEAD MIX`"


The main gain layer is useful for adjusting main and headphone output levels.
When active, the encoders turn light green and light yellow.

==================  ================  ========================  ========================================
Encoder             Category          Action                    Function
==================  ================  ========================  ========================================
Encoder 1           Main Balance      Spin                      Adjusts main balance.
..                  ..                Press                     Resets main balance.
Encoder 2           Main Gain         Spin                      Adjusts main gain.
..                  ..                :hwlabel:`SHIFT` + Spin   Adjusts booth gain.
..                  ..                Press                     Resets main gain.
..                  ..                :hwlabel:`SHIFT` + Press  Resets booth gain.
Encoder 3           Headphone Gain    Spin                      Adjusts headphone gain.
..                  ..                Press                     Resets headphone gain.
Encoder 4           Headphone Mix     Spin                      Adjusts headphone mix.
..                  ..                Press                     Resets headphone mix.
==================  ================  ========================  ========================================
