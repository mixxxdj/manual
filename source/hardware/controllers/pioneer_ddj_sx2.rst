Pioneer DDJ-SX2
===============

The Pioneer DDJ-SX2 is a 4 deck all-in-one controller that provides intuitive control of all of Mixxx’s features.

-  `Manufacturer’s product page <https://www.pioneerdj.com/en/product/dj-controllers/ddj-sx2/>`__
-  `Forum thread <https://mixxx.discourse.group/t/pioneer-ddj-sx2-mapping/33575>`__
-  `User Manual <https://support.alphatheta.com/en-US/products/4416558363289?section=23>`__
-  `MIDI Messages Manual <https://downloads.support.alphatheta.com/software_info/dj-controllers/DDJ-SX2/DDJ-SX2_List_of_MIDI_Message_E.pdf>`__

.. versionadded:: 2.6

User Options
------------

To change the mapping’s user options, go into Mixxx's Controllers Settings and change the options:

-  **PioneerDDJSX.safeScratchTimeout**: Safe Scratch Timeout (ms) (20ms is the minimum allowed)
-  **PioneerDDJSX.UseShiftToBreak**: Use :hwlabel:`Play` instead of :hwlabel:`Shift` + :hwlabel:`Play` to brake/soft start.
-  **PioneerDDJSX.SoftStartTime**: Soft Start Factor (Higher is faster) (disable with -1)
-  **PioneerDDJSX.BrakeTime**: Brake Factor (Higher is faster) (disable with -1)
-  **PioneerDDJSX.CenterRedLightsBehavior**: Bar-by-bar central red LED counter (Beat-By-Beat if disabled)
-  **PioneerDDJSX.CenterWhiteLightsBehavior**: Show track progression instead of rotation in the center white lights.
-  **PioneerDDJSX.DoNotTrickController**: Do not send Serato mode keep-alive when enabled. Note that center lights, spin alignment and slip flash will not be available.

General Functions
-----------------

====================  ===============  =============================================  =================================================================================================================================
Group                 Figure           Control                                        Description
====================  ===============  =============================================  =================================================================================================================================
5 - BROWSER           2, 3, 4, 5       :hwlabel:`LOAD`                                Loads the highlighted track from the Library into the selected deck
5 - BROWSER           2                :hwlabel:`SHIFT` + :hwlabel:`LOAD`             Sort the current library by BPM
5 - BROWSER           3                :hwlabel:`SHIFT` + :hwlabel:`LOAD`             Sort the current library by song title
5 - BROWSER           4                :hwlabel:`SHIFT` + :hwlabel:`LOAD`             Sort the current library by track number
5 - BROWSER           5                :hwlabel:`SHIFT` + :hwlabel:`LOAD`             Sort the current library by artist
5 - BROWSER           1                Rotary Selector                                Scrolls up/down through the Library list
5 - BROWSER           1                Rotary Selector (press)                        Opens or loads the selected Library item
5 - BROWSER           6                :hwlabel:`BACK`                                Moves focus to the Library’s left panel (crates, playlists, etc.)
5 - BROWSER           6                :hwlabel:`SHIFT` + :hwlabel:`BACK`             Toggles between 2 or 4 decks
5 - BROWSER           7                :hwlabel:`LOAD PREPARE`                        Preloads track metadata (BPM, Key) and displays waveform preview without loading the track
5 - BROWSER           7                :hwlabel:`SHIFT` + :hwlabel:`LOAD PREPARE`     Toggles the maximized library
3 - MIXER             1                Crossfader                                     Blends audio between decks assigned to side A and side B
3 - MIXER             2                Channel fader                                  Controls the output level of the deck
3 - MIXER             3                TRIM                                           Controls deck gain
3 - MIXER             4                EQ HIGH                                        Controls deck’s equalizer/filter high frequencies
3 - MIXER             5                EQ MID                                         Controls deck’s equalizer/filter mid frequencies
3 - MIXER             6                EQ LOW                                         Controls deck’s equalizer/filter low frequencies
3 - MIXER             7                :hwlabel:`CUE`                                 Toggles headphone pre-listen (PFL) for the deck
3 - MIXER             7                :hwlabel:`SHIFT`  :hwlabel:`CUE`               Sends BPM tap input for manual tempo detection
3 - MIXER             8                :hwlabel:`MASTER LEVEL`                        Controls the hardware master output level (independent from Mixxx)
3 - MIXER             9                :hwlabel:`MASTER CUE`                          Routes the master output signal to the headphones (independent from Mixxx)
3 - MIXER             9                :hwlabel:`SHIFT`  :hwlabel:`MASTER CUE`        Enables split-cue mode (cue in one ear, master in the other)
3 - MIXER             10               Crossfader Assign                              Crossfader assignment, deck to crossfader (left (A), right (B) or center (THRU))
3 - MIXER             13               :hwlabel:`HEADPHONES MIX`                      Controls headphone’s audio source (cue, main) (independent from Mixxx)
3 - MIXER             14               SAMPLER VOLUME                                 Controls the global output level of all sampler slots
3 - MIXER             15               :hwlabel:`BOOTH MONITOR LEVEL`                 Controls the hardware booth output level (independent from Mixxx)
4 - FRONT PANEL       1                Crossfader curve                               Adjusts the hardware crossfader response curve (smooth to sharp)
4 - FRONT PANEL       2                :hwlabel:`INPUT SELECT`                        Selects the physical input source for the deck (PC, MIC, CD, PHONO, LINE) (independent from Mixxx)
1 - DECK              25               :hwlabel:`PANEL SELECT`                        Shows or hides the Sampler panel and the Effects rack in Mixxx
====================  ===============  =============================================  =================================================================================================================================

.. note::
   The :hwlabel:`MASTER LEVEL`, :hwlabel:`MASTER CUE`, :hwlabel:`HEADPHONE MIX`, :hwlabel:`BOOTH MONITOR LEVEL` and :hwlabel:`INPUT SELECT` controls directly affect the controller’s sound card, so adjusting these will not change anything on screen in Mixxx.


Deck Functions
--------------

The controls listed here are documented in Section 1 ("Deck") of the owner's manual.

===============  =============================================  =================================================================================================================================
Figure           Control                                        Description
===============  =============================================  =================================================================================================================================
1                :hwlabel:`PLAY/PAUSE`                          Starts or stops playback at the current playhead position
1                :hwlabel:`SHIFT` + :hwlabel:`PLAY/PAUSE`       Starts or stops playback using brake/soft-start
2                :hwlabel:`CUE`                                 Sets a cue point or returns playback to the stored cue point depending on deck state
2                :hwlabel:`SHIFT` + :hwlabel:`CUE`              Instantly jumps to the beginning of the track and stops playback
3                Jog Wheel (platter)                            Vinyl mode ON: scratch when pressed and rotated. Vinyl mode OFF: performs pitch bend.
3                :hwlabel:`SHIFT` + Jog Wheel (platter)         Moves the playhead quickly through the track for fast navigation
3                Jog Wheel (side)                               Applies temporary pitch bend when rotated
3                :hwlabel:`SHIFT` + Jog Wheel (side)            Moves the playhead quickly through the track for fast navigation
4                :hwlabel:`TEMPO`                               Adjusts the deck’s playback speed (pitch/tempo)
5                :hwlabel:`KEYLOCK`                             Toggles keylock to maintain musical key when changing tempo, holding the button will reset the tempo to the default value of the track
5                :hwlabel:`SHIFT` + :hwlabel:`KEYLOCK`          Toggles between for values for the tempo range : +/-8 ; +/-16 ; +/-32 ; +/-64
6                :hwlabel:`NEEDLE SEARCH`                       Jumps to the corresponding absolute position in the track
7                :hwlabel:`DECK 1`                              Switches left deck to DECK 1 control and illumination
8                :hwlabel:`DECK 2`                              Switches right deck to DECK 2 control and illumination
9                :hwlabel:`DECK 3`                              Switches left deck to DECK 3 control and illumination
10               :hwlabel:`DECK 4`                              Switches right deck to DECK 4 control and illumination
13               :hwlabel:`SYNC`                                Toggles beat sync for the deck
13               :hwlabel:`SHIFT` + :hwlabel:`SYNC`             Toggles sync lock mode for continuous tempo alignment
14               :hwlabel:`AUTO LOOP`                           Creates and activates an automatic loop at the current play position
14               :hwlabel:`SHIFT`    :hwlabel:`AUTO LOOP`       Activates or deactivates the currently defined loop
15               :hwlabel:`LOOP 1/2X`                           Halves the length of the active loop
15               :hwlabel:`SHIFT`    :hwlabel:`LOOP 1/2X`       Moves the active loop one beat backward
16               :hwlabel:`LOOP 2X`                             Doubles the length of the active loop
15               :hwlabel:`SHIFT`    :hwlabel:`LOOP 2X`         Moves the active loop one beat forward
17               :hwlabel:`LOOP IN`                             Sets or adjusts the loop-in point
17               :hwlabel:`SHIFT`    :hwlabel:`LOOP IN`         Activates the current loop, jumps to the loop-in point, and stops playback
18               :hwlabel:`LOOP OUT`                            Sets or adjusts the loop-out point
18               :hwlabel:`SHIFT`    :hwlabel:`LOOP OUT`        Toggles reloop/exit for the active loop
19               :hwlabel:`VINYL`                               Enables or disables vinyl (scratch) mode on the jog wheel
20               :hwlabel:`CENSOR`                              Performs a temporary reverse roll while held
20               :hwlabel:`SHIFT`    :hwlabel:`CENSOR`          Toggles continuous reverse playback
21               :hwlabel:`SLIP`                                Enables slip mode, allowing temporary actions without altering track position
22               :hwlabel:`GRID ADJUST`                         Adjusts the beatgrid tempo up or down
22               :hwlabel:`SHIFT`    :hwlabel:`GRID ADJUST`     Sets/translates the beatgrid to the current play position
23               :hwlabel:`GRID SLIDE`                          Hold and touch/rotate Jog dial to set/translate beat grid earlier/later
23               :hwlabel:`SHIFT`    :hwlabel:`GRID SLIDE`      Resets the beatgrid to its previous state.
24               :hwlabel:`SHIFT`                               Enables access to secondary (shifted) controls, no direct function
===============  =============================================  =================================================================================================================================

Performance Pads
----------------

The performance pads support multiple different modes.
The controls listed here are documented in Section 6 ("Performance Pads") of the owner's manual.

===============  =============================================  =================================================================================================================================
Figure           Control                                        Description
===============  =============================================  =================================================================================================================================
9                :hwlabel:`HOT CUE` mode                        Switches pad control and illumination to :ref:`HOT CUE mode <pioneer-DDJ-SX2-hotcuemode>`
9                :hwlabel:`SHIFT` + :hwlabel:`HOT CUE` mode     Switches pad control and illumination to :ref:`HOT CUE LOOP mode <pioneer-DDJ-SX2-hotcueloopmode>`
10               :hwlabel:`ROLL` mode                           Switches pad control and illumination to :ref:`ROLL mode <pioneer-DDJ-SX2-rollmode>`
10               :hwlabel:`SHIFT` + :hwlabel:`ROLL` mode        Switches pad control and illumination to :ref:`SAVED LOOP mode <pioneer-DDJ-SX2-savedloopmode>`
11               :hwlabel:`SLICER` mode                         Switches pad control and illumination to :ref:`SLICER mode <pioneer-DDJ-SX2-slicermode>`, in SLICER mode switches between continuous slice mode and loop slice mode
11               :hwlabel:`SHIFT` + :hwlabel:`SLICER` mode      Switches pad control and illumination to :ref:`SLICER LOOP mode <pioneer-DDJ-SX2-slicerloopmode>`, in SLICER mode switches between continuous slice mode and loop slice mode
12               :hwlabel:`SAMPLER` mode                        Switches pad control and illumination to :ref:`SAMPLER mode <pioneer-DDJ-SX2-samplermode>`
12               :hwlabel:`SHIFT` + :hwlabel:`SAMPLER` mode     Switches pad control and illumination to :ref:`VELOCITY SAMPLER mode <pioneer-DDJ-SX2-velocitysamplermode>`
===============  =============================================  =================================================================================================================================


.. _pioneer-DDJ-SX2-hotcuemode:

HOT CUE Mode
~~~~~~~~~~~~

===============  =============================================  =================================================================================================================================
Figure           Control                                        Description
===============  =============================================  =================================================================================================================================
1                :hwlabel:`PAD 1`                               Sets or triggers Hot Cue 1
1                :hwlabel:`SHIFT` + :hwlabel:`PAD 1`            Clear Hot cue 1
2                :hwlabel:`PAD 2`                               Sets or triggers Hot Cue 2
2                :hwlabel:`SHIFT` + :hwlabel:`PAD 2`            Clear Hot cue 2
3                :hwlabel:`PAD 3`                               Sets or triggers Hot Cue 3
3                :hwlabel:`SHIFT` + :hwlabel:`PAD 3`            Clear Hot cue 3
4                :hwlabel:`PAD 4`                               Sets or triggers Hot Cue 4
4                :hwlabel:`SHIFT` + :hwlabel:`PAD 4`            Clear Hot cue 4
5                :hwlabel:`PAD 5`                               Sets or triggers Hot Cue 5
5                :hwlabel:`SHIFT` + :hwlabel:`PAD 5`            Clear Hot cue 5
6                :hwlabel:`PAD 6`                               Sets or triggers Hot Cue 6
6                :hwlabel:`SHIFT` + :hwlabel:`PAD 6`            Clear Hot cue 6
7                :hwlabel:`PAD 7`                               Sets or triggers Hot Cue 7
7                :hwlabel:`SHIFT` + :hwlabel:`PAD 7`            Clear Hot cue 7
8                :hwlabel:`PAD 8`                               Sets or triggers Hot Cue 8
8                :hwlabel:`SHIFT` + :hwlabel:`PAD 8`            Clear Hot cue 8
13               :hwlabel:`PARAMETER LEFT`                      No function
14               :hwlabel:`PARAMETER RIGHT`                     No function
===============  =============================================  =================================================================================================================================


.. _pioneer-DDJ-SX2-hotcueloopmode:

HOT CUE LOOP Mode
~~~~~~~~~~~~~~~~~

In this mode, hotcues will have a loop enabled and saved.

===============  =============================================  =================================================================================================================================
Figure           Control                                        Description
===============  =============================================  =================================================================================================================================
1                :hwlabel:`PAD 1`                               Set/activate Hot cue 9
1                :hwlabel:`SHIFT` + :hwlabel:`PAD 1`            Clear Hot cue 9
2                :hwlabel:`PAD 2`                               Set/activate Hot cue 10
2                :hwlabel:`SHIFT` + :hwlabel:`PAD 2`            Clear Hot cue 10
3                :hwlabel:`PAD 3`                               Set/activate Hot cue 11
3                :hwlabel:`SHIFT` + :hwlabel:`PAD 3`            Clear Hot cue 11
4                :hwlabel:`PAD 4`                               Set/activate Hot cue 12
4                :hwlabel:`SHIFT` + :hwlabel:`PAD 4`            Clear Hot cue 12
5                :hwlabel:`PAD 5`                               Set/activate Hot cue 13
5                :hwlabel:`SHIFT` + :hwlabel:`PAD 5`            Clear Hot cue 13
6                :hwlabel:`PAD 6`                               Set/activate Hot cue 14
6                :hwlabel:`SHIFT` + :hwlabel:`PAD 6`            Clear Hot cue 14
7                :hwlabel:`PAD 7`                               Set/activate Hot cue 15
7                :hwlabel:`SHIFT` + :hwlabel:`PAD 7`            Clear Hot cue 15
8                :hwlabel:`PAD 8`                               Set/activate Hot cue 16
8                :hwlabel:`SHIFT` + :hwlabel:`PAD 8`            Clear Hot cue 16
13               :hwlabel:`PARAMETER LEFT`                      No function
14               :hwlabel:`PARAMETER RIGHT`                     No function
===============  =============================================  =================================================================================================================================


.. _pioneer-DDJ-SX2-rollmode:

ROLL Mode
~~~~~~~~~

By using the :hwlabel:`PARAMETER LEFT` and :hwlabel:`PARAMETER RIGHT` buttons in ROLL mode (default parameter set: 1), you can change the pad-assigned loop size.
The following table shows the possible assignments (unit: beats).

======= ===== ===== ===== ===== ===== ===== ===== =====
Set No. Pad 1 Pad 2 Pad 3 Pad 4 Pad 5 Pad 6 Pad 7 Pad 8
======= ===== ===== ===== ===== ===== ===== ===== =====
0       1/2   1     2     4     8     16    32    64
1       1/4   1/2   1     2     4     8     16    32
2       1/8   1/4   1/2   1     2     4     8     16
3       1/16  1/8   1/4   1/2   1     2     4     8
4       1/32  1/16  1/8   1/4   1/2   1     2     4
======= ===== ===== ===== ===== ===== ===== ===== =====

===============  =============================================  =================================================================================================================================
Figure           Control                                        Description
===============  =============================================  =================================================================================================================================
1                :hwlabel:`PAD 1`                               Toggle Beatloop roll length index 1 (according parameter set)
2                :hwlabel:`PAD 2`                               Toggle Beatloop roll length index 2 (according parameter set)
3                :hwlabel:`PAD 3`                               Toggle Beatloop roll length index 3 (according parameter set)
4                :hwlabel:`PAD 4`                               Toggle Beatloop roll length index 4 (according parameter set)
5                :hwlabel:`PAD 5`                               Toggle Beatloop roll length index 5 (according parameter set)
6                :hwlabel:`PAD 6`                               Toggle Beatloop roll length index 6 (according parameter set)
7                :hwlabel:`PAD 7`                               Toggle Beatloop roll length index 7 (according parameter set)
8                :hwlabel:`PAD 8`                               Toggle Beatloop roll length index 8 (according parameter set)
13               :hwlabel:`PARAMETER LEFT`                      Decrement active looproll-interval parameter set (0-3)
14               :hwlabel:`PARAMETER RIGHT`                     Increment active looproll-interval parameter set (0-3)
===============  =============================================  =================================================================================================================================


.. _pioneer-DDJ-SX2-savedloopmode:

SAVED LOOP ROLL Mode
~~~~~~~~~~~~~~~~~~~~

This mode has pre-made loop that can be toggled.


.. _pioneer-DDJ-SX2-slicermode:

SLICER Mode
~~~~~~~~~~~

This mode is used as a beatjump, the four top pad jumps backward and the four bottom pad jumps forward.


.. _pioneer-DDJ-SX2-slicerloopmode:

SLICER LOOP Mode
~~~~~~~~~~~~~~~~

Same as SLICER mode.

.. _pioneer-DDJ-SX2-samplermode:

SAMPLER Mode
~~~~~~~~~~~~

===============  =============================================  =================================================================================================================================
Figure           Control                                        Description
===============  =============================================  =================================================================================================================================
1                :hwlabel:`PAD 1`                               Sample deck index 1 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck
1                :hwlabel:`SHIFT` + :hwlabel:`PAD 1`            Sample deck index 1 (according sampler bank) - playing: stop deck, stopped: eject track
2                :hwlabel:`PAD 2`                               Sample deck index 2 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck
2                :hwlabel:`SHIFT` + :hwlabel:`PAD 2`            Sample deck index 2 (according sampler bank) - playing: stop deck, stopped: eject track
3                :hwlabel:`PAD 3`                               Sample deck index 3 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck
3                :hwlabel:`SHIFT` + :hwlabel:`PAD 3`            Sample deck index 3 (according sampler bank) - playing: stop deck, stopped: eject track
4                :hwlabel:`PAD 4`                               Sample deck index 4 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck
4                :hwlabel:`SHIFT` + :hwlabel:`PAD 4`            Sample deck index 4 (according sampler bank) - playing: stop deck, stopped: eject track
5                :hwlabel:`PAD 5`                               Sample deck index 5 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck
5                :hwlabel:`SHIFT` + :hwlabel:`PAD 5`            Sample deck index 5 (according sampler bank) - playing: stop deck, stopped: eject track
6                :hwlabel:`PAD 6`                               Sample deck index 6 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck
6                :hwlabel:`SHIFT` + :hwlabel:`PAD 6`            Sample deck index 6 (according sampler bank) - playing: stop deck, stopped: eject track
7                :hwlabel:`PAD 7`                               Sample deck index 7 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck
7                :hwlabel:`SHIFT` + :hwlabel:`PAD 7`            Sample deck index 7 (according sampler bank) - playing: stop deck, stopped: eject track
8                :hwlabel:`PAD 8`                               Sample deck index 8 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options) sample deck
8                :hwlabel:`SHIFT` + :hwlabel:`PAD 8`            Sample deck index 8 (according sampler bank) - playing: stop deck, stopped: eject track
13               :hwlabel:`PARAMETER LEFT`                      Selects previous sampler bank (Up to 64 samples)
14               :hwlabel:`PARAMETER RIGHT`                     Selects next sampler bank (Up to 64 samples)
===============  =============================================  =================================================================================================================================

.. _pioneer-DDJ-SX2-velocitysamplermode:

VELOCITY SAMPLER Mode
~~~~~~~~~~~~~~~~~~~~~

Same as SAMPLER mode, but with Velocity on the pads.

Effect Functions
----------------

This controller mapping uses the :ref:`standard Mixxx mapping for effects sections on controllers <controller-effects-mapping>`.
The controls listed here are documented in Section 2 ("Effects") of the owner's manual.

===============  =========================================  =================================================================================================================================
Figure           Control                                    Description
===============  =========================================  =================================================================================================================================
1 (L)            :hwlabel:`FX1-1`                           Focused effect none: Controls EffectRack1-EffectUnit1/3-Effect1 meta, Focused effect 1..3: Controls effect parameter 1 of  effect in EffectRack1-EffectUnit1/3
1 (L)            :hwlabel:`SHIFT` + :hwlabel:`FX1-1`        No function
1 (R)            :hwlabel:`FX2-1`                           Focused effect none: Controls EffectRack1-EffectUnit2/4-Effect1 meta, Focused effect 1..3: Controls effect parameter 1 of focused effect in EffectRack1-EffectUnit2/4
1 (R)            :hwlabel:`SHIFT` + :hwlabel:`FX2-1`        No function
2 (L)            :hwlabel:`FX1-2`                           Focused effect none: Controls EffectRack1-EffectUnit1/3-Effect2 meta, Focused effect 1..3: Controls effect parameter 2 of focused effect in EffectRack1-EffectUnit1/3
2 (L)            :hwlabel:`SHIFT` + :hwlabel:`FX1-2`        No function
2 (R)            :hwlabel:`FX2-2`                           Focused effect none: Controls EffectRack1-EffectUnit2/4-Effect2 meta, Focused effect 1..3: Controls effect parameter 2 of focused effect in EffectRack1-EffectUnit2/4
2 (R)            :hwlabel:`SHIFT` + :hwlabel:`FX2-2`        No function
3 (L)            :hwlabel:`FX1-3`                           Focused effect none: Controls EffectRack1-EffectUnit1/3-Effect3 meta, Focused effect 1..3: Controls effect parameter 3 of focused effect in EffectRack1-EffectUnit1/3
3 (L)            :hwlabel:`SHIFT` + :hwlabel:`FX1-3`        No function
3 (R)            :hwlabel:`FX2-3`                           Focused effect none: Controls EffectRack1-EffectUnit2/4-Effect3 meta, Focused effect 1..3: Controls effect parameter 3 of focused effect in EffectRack1-EffectUnit2/4
3 (R)            :hwlabel:`SHIFT` + :hwlabel:`FX2-3`        No function
4 (L)            :hwlabel:`FX1 BEATS`                       Turn: Controls EffectRack1-EffectUnit1/3 mix. Click: Cycle through the different effects values. By default each knob controls the main value of all 3 effects, when clicking the BEATS knob, the effects knobs will now set the value for the different elements of the effects (For example, Decay/BW/Dampling for the Reverb effect)
4 (R)            :hwlabel:`FX2 BEATS`                       Turn: Controls EffectRack1-EffectUnit2/4 mix. Click: Cycle through the different effects values. By default each knob controls the main value of all 3 effects, when clicking the BEATS knob, the effects knobs will now set the value for the different elements of the effects (For example, Decay/BW/Dampling for the Reverb effect)
4 (L)            :hwlabel:`SHIFT` + :hwlabel:`FX1 BEATS`    No function
4 (R)            :hwlabel:`SHIFT` + :hwlabel:`FX2 BEATS`    No function
5 (L)            :hwlabel:`FX1-1 ON`                        Toggles EffectRack1-EffectUnit1/3-Effect1
5 (R)            :hwlabel:`FX2-1 ON`                        Toggles EffectRack1-EffectUnit2/4-Effect1
6 (L)            :hwlabel:`FX1-2 ON`                        Toggles EffectRack1-EffectUnit1/3-Effect2
6 (R)            :hwlabel:`FX2-2 ON`                        Toggles EffectRack1-EffectUnit2/4-Effect2
7 (L)            :hwlabel:`FX1-3 ON`                        Toggles EffectRack1-EffectUnit1/3-Effect3
7 (R)            :hwlabel:`FX2-3 ON`                        Toggles EffectRack1-EffectUnit2/4-Effect3
8 (L)            :hwlabel:`FX1 TAP`                         Sets whether to mix as wet/dry or wet+dry for FX1
8 (R)            :hwlabel:`FX2 TAP`                         Sets whether to mix as wet/dry or wet+dry for FX2
8 (L)            :hwlabel:`SHIFT` + :hwlabel:`FX1 TAP`      Expand or collapse the FX1 effect panel
8 (R)            :hwlabel:`SHIFT` + :hwlabel:`FX2 TAP`      Expand or collapse the FX2 effect panel
9, 10, 11, 12    :hwlabel:`FX1 ASSIGN`                      Assign EffectRack1-EffectUnit1/3 to specific deck
13, 14, 15, 16   :hwlabel:`FX2 ASSIGN`                      Assign EffectRack1-EffectUnit2/4 to specific deck
17, 18, 19, 20   :hwlabel:`FILTER`                          Control QuickEffectRack1 super1 knob (e.g. moog filter)
===============  =========================================  =================================================================================================================================

Troubleshooting
---------------

If you experience any strange behavior of a button or a LED (e.g. wheel LEDs not working), make sure your controller is set up correctly to work with Mixxx. The DDJ-SX2 provides several settings, which
can be changed in a special *Utility-Mode*. **Please look up the official manual before changing anything in Utility-Mode.**

Utility-Mode
~~~~~~~~~~~~

-  Disconnect USB-cable.
-  Switch off :hwlabel:`STANDBY/ON` the unit.
-  Hold :hwlabel:`SHIFT` button and :hwlabel:`PLAY/PAUSE` button at the left deck while switching on the unit :hwlabel:`STANDBY/ON`.
-  Now *Utility-Mode* is activated.
-  For saving and exiting *Utility-Mode*, switch off the unit again :hwlabel:`STANDBY/ON`.

Setting for usage of Serato DJ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use the DDJ-SX2 with Mixxx, the controller must be configured for the usage of Serato DJ. You can check/change this setting by pressing the :hwlabel:`KEY LOCK` button at the left deck.

-  :hwlabel:`KEY LOCK` button off: Controller is configured for using Serato DJ (default).
-  :hwlabel:`KEY LOCK` button on (lit): Controller is configured for using different DJ-software.
