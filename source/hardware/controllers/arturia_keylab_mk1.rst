Arturia KeyLab Mk 1
===================

`Manufacturer's product page <https://www.arturia.com/keylab88/resources>`_ ·
`Forum thread <https://mixxx.discourse.group/t/arturia-keylab-mk1/31080>`_

.. versionadded:: 2.5.1

Overview
--------

.. figure:: ../../_static/controllers/arturia_keylab88.svg
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Arturia KeyLab 88
   :figclass: pretty-figures

The Arturia KeyLab 88 (retroactively called the "Mark 1") is a full size piano
keyboard that includes various encoders, faders, buttons, and velocity sensitive
touch pads.
It also includes a two-line dot-matrix display.

.. note:: Arturia also made 61 and 25 key versions of this keyboard.
   This mapping has only been tested with the full size version and it is
   unknown whether it works for the smaller versions.

Menu Controls
-------------

On the left side of the controller is an unlabeled section of controls
surrounding the screen and the KeyLab logo.
These global controls are used to select the deck, and to perform various tasks
using the built-in menu which will be displayed on the screen.

.. csv-table::
   :header: "Control", "Label", "Function"
   :widths: 20 25 55

   "Knob", ":hwlabel:`Volume`", "Main output gain"
   "Menu Nav", ":hwlabel:`Param` (rotate)", "Scroll between menu items on the display"
   "Menu Nav", ":hwlabel:`Param` (press)", "Enter into the selected submenu"
   "Menu Action", ":hwlabel:`Value` (rotate)", "Select value of active menu item"
   "Menu Action", ":hwlabel:`Value` (press)", "Toggle or activate selected menu item"
   "Deck 1/3", ":hwlabel:`Sound` (short press)", "Select deck 1"
   "Deck 1/3", ":hwlabel:`Sound` (long press)", "Select deck 3"
   "Deck 2/4", ":hwlabel:`Multi` (short press)", "Select deck 2"
   "Deck 2/4", ":hwlabel:`Multi` (long press)", "Select deck 4"

The on screen menu contains the following options:

.. _main-menu:

Main Menu
^^^^^^^^^

.. csv-table::
   :header: "Label", "Action", "Function"
   :widths: 20 10 70

   "Key", "Rotate", "Change the key of the selected deck"
   "Key", "Press", "Reset the key of the selected deck to the detected key"
   "Beatloop", "Rotate", "Change the length of a loop"
   "Beatloop", "Press", "Activate or deactivate the last loop"
   "Library", "—", "Open the :ref:`library-menu`"
   "Skin", "—", "Open the :ref:`skin-menu`"
   "FX1", "—", "Open one of the :ref:`fx-menus`"
   "FX2", "—", "Open one of the :ref:`fx-menus`"
   "FX3", "—", "Open one of the :ref:`fx-menus`"
   "FX4", "—", "Open one of the :ref:`fx-menus`"

.. _library-menu:

Library Menu
^^^^^^^^^^^^

The library submenu contains options for navigating and selecting items in the
library view.

.. note:: Currently Mixxx must be focused for the library navigation options to
   have any effect. This is an open issue that will be addressed in a future
   version of Mixxx.

.. csv-table::
   :header: "Label", "Action", "Function"
   :widths: 20 10 70

   "Search", "Rotate", "Select previous library searches"
   "Search", "Press", "Clear the current search"
   "Focus", "Rotate", "Change the focused pane in the library view"
   "Scroll", "Rotate", "Move vertically in the selected pane"
   "Scroll", "Press", "Perform the default action for the selected item (configurable for tracks, open drop downs, etc.)"
   "Sort", "Rotate", "Select sort order column"
   "Sort", "Press", "Toggle the sort order between ascending and descending"
   "Maximize", "Press", "Maximize the library view, shrinking the decks and other UI elements"
   "Font Size", "Rotate", "Change the font size"
   "Back", "Press", "Go back to the :ref:`main-menu`"

.. _skin-menu:

Skin Menu
^^^^^^^^^

The skin submenu contains options for configuring and changing the Mixxx UI.

.. csv-table::
   :header: "Label", "Action", "Function"
   :widths: 20 10 70

   "Effect Rack", "Press", "Show or hide the effect racks"
   "Coverart", "Press", "Show or hide the album coverart"
   "Samplers", "Press", "Show or hide the samplers"
   "Vinyl Control", "Press", "Show or hide the vinyl controls"
   "Back", "Press", "Go back to the :ref:`main-menu`"

.. _fx-menus:

FX Menus
^^^^^^^^

There are four FX menus for controlling individual effect racks.
Each one has the following options:

.. csv-table::
   :header: "Label", "Action", "Function"
   :widths: 20 10 70

   "FX Preset", "Rotate", "Select one of the effect rack presets"
   "FX Preset", "Press", "Enable or disable the given effect rack for the selected deck"
   "FX Focus", "Rotate", "Change the currently focused effect in the UI"
   "FX Focus", "Press", "Show or hide the focus indicator on the given effect rack"
   "Back", "Press", "Go back to the :ref:`main-menu`"

Main Controls
-------------

To the right of the KeyLab logo are the main bank of controls
labeled, simply, :hwlabel:`Controls`.
Currently Mixxx only uses the first bank, so the :hwlabel:`Bank 1` button should
be illuminated, otherwise the other controls in this section may not work.

.. csv-table::
   :header: "Control", "Label", "Function"
   :widths: 20 10 70

   "Gain Knob", ":hwlabel:`P1`", "Deck gain"
   "High Knob", ":hwlabel:`P2`", "EQ highs"
   "Mid Knob", ":hwlabel:`P3`", "EQ mids"
   "Low Knob", ":hwlabel:`P4`", "EQ lows"
   "Effect Knob", ":hwlabel:`P5`", "Quick effect rack"
   "D3 Fader", ":hwlabel:`F1`", "Deck 3 volume"
   "D1 Fader", ":hwlabel:`F2`", "Deck 1 volume"
   "D2 Fader", ":hwlabel:`F3`", "Deck 2 volume"
   "D4 Fader", ":hwlabel:`F4`", "Deck 4 volume"
   "D3 Fader", ":hwlabel:`F5`", "Deck 3 tempo"
   "D1 Fader", ":hwlabel:`F6`", "Deck 1 tempo"
   "D2 Fader", ":hwlabel:`F7`", "Deck 2 tempo"
   "D4 Fader", ":hwlabel:`F8`", "Deck 4 tempo"
   "X-Fader", ":hwlabel:`F9`", "Crossfader"

Snapshots
---------

Below the main controls are a collection of 10 physical buttons labeled
:hwlabel:`Snapshots`.

.. csv-table::
   :header: "Control", "Label", "Function"
   :widths: 30 5 65

   "Intro/Outro + Hotcues", ":hwlabel:`1`", "Configure first four drum pads to be the intro and outro markers and the remaining pads to be hotcues."
   "Hotcues", ":hwlabel:`2`", "Configure all 16 drum pads to be hotcues."
   "Samplers", ":hwlabel:`3`", "Configure all 16 drum pads to be velocity sensitive samplers."


Transports
----------

To the right of the snapshot buttons are a collection of buttons labeled
:hwlabel:`Transports`.
Each of these is bound to the currently selected deck except for the record
button.

.. csv-table::
   :header: "Function", "Name", "Function"
   :widths: 5 25 70

   "Rewind", ":hwlabel:`⏪`", "Beatjump backwards"
   "Fastforward", ":hwlabel:`⏩`", "Beatjump forwards"
   "Cue", ":hwlabel:`⏹`", "If track is playing: stops the track and resets position to the main cue point

   If playback is stopped: sets the main cue point"
   "Cue", ":hwlabel:`⏹` (hold)", "Play the track from main cue point, release to stop playback and return to the main cue point. Playback must be initially stopped on the main cue point."
   "Play/Pause", ":hwlabel:`⏯`", "Play/pause playback"
   "Record", ":hwlabel:`⏺`", "Toggle recording the mix"
   "Loop",  ":hwlabel:`🔁`", "Toggle the previous beatloop"

.. hint::
   The actual behavior of CUE and Play/Pause buttons depends on Mixxx settings. See :ref:`interface-cue-modes` for more info.

Drum Pads
---------

To the right of the main controls are a collection of 16 drum pads that are
individually labeled Pad 16 (top right) through Pad 1 (bottom left).
In Mixxx we invert the numbers so that eg. Pad 13 in the top left maps to
Sampler 1.
If the pad is not illuminated, pressing it will load the currently selected
track into the given sampler.
If it is illuminated, pressing it will cause the sampler to play and the pad to
blink for the duration of the playback.
The pads are velocity sensitive and the harder they are hit the louder the
volume of the sampler.

Mapping Options
---------------

Several options are available for configuring the controller in the Mixxx
settings:

.. csv-table::
   :header: "Setting", "Values", "Default", "Description"
   :widths: 20 20 10 50

   "Soft Takeover", "On/Off", "On", "Enable or disable soft takeover mode for all encoders."
   "Disable Pads", "On/Off", "Off", "Disables the pads so they can be used with with an external synth."
   "Output Delay", "Duration (ms)", "100", "The number of milliseconds to wait before setting output LEDs or writing to the screen. The controller sometimes sets LEDs by itself, meaning they no longer match the value expected by Mixxx. If you notice LEDs being set to the expected setting, then flickering to an unexpected setting, increase this number."
