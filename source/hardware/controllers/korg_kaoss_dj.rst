Korg Kaoss DJ controller
========================

2-deck controller with touch controlled jogwheels, built-in 4-channel soundcard and a Korg Kaoss Pad as built-in effect section (can be switched off for using software effects).

| Controller needs to be set as output device in order to wake up from standby (Stb).
| Main: Channel 1-2
| Headphone: Channel 3-4

-  `Manufacturer’s product page <http://www.korg.com/uk/products/dj/kaoss_dj/>`__
-  `Forum thread <https://mixxx.discourse.group/t/korg-kaoss-dj-midi-mapping-help/16093>`__
-  `Pull request on Github <https://github.com/mixxxdj/mixxx/pull/1509>`__

.. versionadded:: 2.1

Mapping
-------

.. figure:: ../../_static/controllers/korg_kaoss_dj.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Korg Kaoss DJ (schematic view)
   :figclass: pretty-figures

   Korg Kaoss DJ (schematic view)


+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| No. |                  Name                  |                   Function                    |                  Shifted Operation                   |
+=====+========================================+===============================================+======================================================+
| 1   | Headphone knob                         | Adjusts headphone level                       |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 2   | Balance knob                           | Adjusts balance between master level          |                                                      |
|     |                                        | and headphone monitor level                   |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 3   | Master knob                            | Adjusts master volume level                   |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 4   | Browse knob                            | Selects a song from the library               | Moves between levels                                 |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 5   | Display                                | Not used yet                                  |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 6   | Touchpad Mode Button                   | Switches the touchpad between the Controller, |                                                      |
|     |                                        | KAOSS Effect, and Sampler modes (long press   |                                                      |
|     |                                        | for blue LED)                                 |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 7   | Program/Value Knob (controller mode)   | Selects an effect (not implemented yet)       | Selects a key, selects a scale (not implemented yet) |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
|     | Program/Value Knob (Kaoss Effect mode) | Selects an effect                             | Jumps to next effect category                        |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 8   | Tap Button                             | tap to open a folder in the file-browser      | use left / right shift to set the tempo              |
|     |                                        | (double-tap to close an open folder)          | of left / right track                                |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 9   | Hold Button                            | Enables/disables the touchpad’s hold function | Scale setting mode                                   |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 10  | Touchpad (controller mode)             | Controls the effects of Mixxx.                | Controls Quick-Effect super knobs.                   |
|     |                                        | Vertical axis: mix (dry/wet) knob /           | Horizontal axis: deck 1 /                            |
|     |                                        | Horizontal axis: super knob                   | Vertical axis: deck 2                                |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
|     | Touchpad (Kaoss Effect mode)           | Controls KAOSS effect                         | Adjusts depth of KAOSS Effect                        |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
|     | Touchpad (sampler mode)                | Controls sampler function of Mixxx            |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 11  | Crossfader                             | Adjusts balance between Decks A/B             |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 12  | Touch Slider mode button               | Switches between the three touch slider modes |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 13  | Touch Slider (Normal mode)             | Left: Nudge (-) /                             | Moves to specified position in the song              |
|     |                                        | Center: Enable scratch mode  /                | (slider)                                             |
|     |                                        | Right: Nudge (+)                              |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
|     | Touch Slider (Hot Cue mode)            | Sets or moves to Hot Cue.                     | Delete Hot Cue.                                      |
|     |                                        | Left: 1 /                                     | Left: 1 /                                            |
|     |                                        | Center: 2 /                                   | Center: 2 /                                          |
|     |                                        | Right: 3                                      | Right: 3                                             |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
|     | Touch Slider (Loop mode)               | Left: Halfs Loop /                            | Left: Sets Loop In point /                           |
|     |                                        | Center: New beatloop at playback position /   | Center: Re-loop /                                    |
|     |                                        | Right: Doubles Loop                           | Right: Sets Loop Out point                           |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 14  | EQ                                     | Boosts or Cuts Hi/Mid/Lo EQ                   |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 15  | Gain knob                              | Adjusts gain                                  |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 16  | Load button                            | Loads song into selected deck A/B             | A: close selected folder in file-browser /           |
|     |                                        |                                               | B: open selected folder in file-browser              |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 17  | Fx button                              | Left: FX1 rack mix knob can be manipulated    |                                                      |
|     |                                        | when enabled /                                |                                                      |
|     |                                        | Right: FX2 rack mix knob can be manipulated   |                                                      |
|     |                                        | when enabled                                  |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 18  | Headphone cue button                   | Turns headphone monitor on/off                | Switches the function of the level meter             |
|     |                                        |                                               | between Deck A/B and the Master level                |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 19  | Touch wheel                            | Scratches (in scratch mode) or adjusts the    | Search function (in scratch mode) or moves           |
|     |                                        | pitch                                         | beatgrid                                             |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 20  | Pitch fader                            | Adjusts pitch                                 |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 21  | Level meter                            | Indicates the input level to deck A/B or the  |                                                      |
|     |                                        | master level                                  |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 22  | Shift button                           | Holding this button provides access to the    |                                                      |
|     |                                        | controllers SHIFT functions                   |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 23  | Play / pause button                    | Starts/pauses the song                        |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 24  | Sync button                            | Synchronizes tempo of Deck A and Deck B       |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 25  | Cue button                             | Sets cue point or moves to the cue point      |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| 26  | Level fader                            | Adjusts level of deck A/B                     |                                                      |
+-----+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
