Pioneer DDJ-SX
==============

The Pioneer DDJ-SX is a 4 deck all-in-one controller that provides intuitive control of all of Mixxx’s features. The DDJ-SX mapping `reportedly works with the
DDJ-SX2 <https://mixxx.org/forums/viewtopic.php?p=37884#p37884>`__, but it does not use the new features of the DDJ-SX2 hardware.

-  `Manufacturer’s product page <https://www.pioneerdj.com/en-us/product/controller/ddj-sx/black/overview/>`__
-  `Forum thread <http://www.mixxx.org/forums/viewtopic.php?f=7&t=8310>`__
-  `Manual (multi-language) <http://docs.pioneerdj.com/Manuals/DDJ_SX_DRH1193_manual/>`__


User Options
------------

To change the mapping’s user options, you have to open the script file (*.js). At the top of the file under **USER OPTIONS** the following settings can be made:

-  **PioneerDDJSX.jogwheelSensivity**: Sets the jogwheel sensivity. 1 = default, 2 is twice as sensitive, 0.5 is half as sensitive.
-  **PioneerDDJSX.jogwheelShiftMultiplier**: Sets how much more sensitive the jogwheels get when holding [**SHIFT**]. Set it to 1 to disable jogwheel sensitivity increase when holding [**SHIFT**].
-  **PioneerDDJSX.twinkleVumeterAutodjOn**: If true, level-meter twinkles if *AutoDJ* is enabled.
-  **PioneerDDJSX.autoDJAddTop**: If true, the selected track will be added to *AutoDJ* queue-top on pressing [**ROTARY SELECTOR**], else the selected track will be added to *AutoDJ* queue-bottom.
-  **PioneerDDJSX.autoDJTickInterval**: Sets the duration of sleeping between *AutoDJ* actions if *AutoDJ* is enabled [ms].
-  **PioneerDDJSX.autoDJMaxBpmAdjustment**: Sets the maximum adjustment of BPM allowed for beats to sync if *AutoDJ* is enabled [BPM].
-  **PioneerDDJSX.autoDJShuffleAfterSkip**: If true, *AutoDJ* queue is being shuffled after skipping a track.
-  **PioneerDDJSX.jumpPreviewEnabled**: If true, by releasing [**ROTARY SELECTOR**], track in preview player jumps forward to “jumpPreviewPosition”.
-  **PioneerDDJSX.jumpPreviewPosition**: Sets the preview player absolute position, being set at releasing [**ROTARY SELECTOR**] and if “jumpPreviewEnabled” is enabled.
-  **PioneerDDJSX.samplerCueGotoAndPlay**: If true, pad press in [**SAMPLER**]-PAD-MODE repeatedly causes *sampler* to play loaded track from cue-point, else it causes to play loaded track from the
   beginning.
-  **PioneerDDJSX.autoPFL**: If true, PFL / Cue (headphone) is being activated by loading a track into certain deck.

General Functions
-----------------

Managed by Mixxx
~~~~~~~~~~~~~~~~

=============== ========== ============ =========================== ===================================================================================================================
Group           Figure     [**SHIFT**]? Button Name                 Description
=============== ========== ============ =========================== ===================================================================================================================
5 - BROWSER     2, 3, 4, 5              [**LOAD**]                  Loads the selected track into the specific deck
                2          [**SHIFT**]  [**LOAD**]                  AutoDJ - Toggle BPM sync
                3          [**SHIFT**]  [**LOAD**]                  AutoDJ - Toggle Key sync
                1                       [**ROTARY SELECTOR**]       Move UP or DOWN the specified number of locations in Library (MoveVertical function)
                1                       [**ROTARY SELECTOR PRESS**] Equivalent to double clicking the currently selected item in Library (GoToItem function)
                1          [**SHIFT**]  [**ROTARY SELECTOR**]       Move LEFT or RIGHT the specified number of locations in Library (MoveHorizontal function)
                1          [**SHIFT**]  [**ROTARY SELECTOR PRESS**] Add track from Library to AutoDJ queue at top/bottom (see user options: default = at bottom)
                6          -            [**BACK**]                  Currently focused pane changes in Library - previously focused pane will be focused (MoveFocusBackward function)
                6          [**SHIFT**]  [**BACK**]                  Maximize view of Library
                7                       [**LOAD PREPARE**]          Load selected track into PreviewDeck, jump to position (see user options) and play, else stop already playing track
3 - MIXER       1                       Crossfader                  Controls Mixxx crossfader, fades between deck 1, 3 and 2, 4
                2                       Channel fader               Controls deck volume
                2          [**SHIFT**]  Channel fader               Fader start (starts playing deck when rising deck volume)
                3                       TRIM                        Controls deck gain
                4                       EQ HIGH                     Controls deck’s equalizer/filter high frequencies
                5                       EQ MID                      Controls deck’s equalizer/filter mid frequencies
                6                       EQ LOW                      Controls deck’s equalizer/filter low frequencies
                7                       [**CUE**]                   Toggles PFL/Cue (headphones) for specific deck
                7          [**SHIFT**]  [**CUE**]                   BPM Tab function for specific deck
                9          [**SHIFT**]  [**MASTER CUE**]            Toggles split cue (headphones)
                10                      Crossfader Assign           Crossfader assignment - deck to crossfader (left (A), right (B) or center (THRU))
                14                      SAMPLER VOLUME              Controls volume of all available Sampler decks
4 - FRONT PANEL 1                       Crossfader curve            Controls Mixxx crossfader curve
1 - DECK        25                      [**PANEL SELECT**]          Show/hide Sampler decks / Effect rack
=============== ========== ============ =========================== ===================================================================================================================

Managed by the controller
~~~~~~~~~~~~~~~~~~~~~~~~~

The following functions directly affect the controller’s sound card, so adjusting these will not change anything on screen in Mixxx:

=============== ====== ============ =================== ===============================================
Group           Figure [**SHIFT**]? Button Name         Description
=============== ====== ============ =================== ===============================================
3 - MIXER       8                   MASTER LEVEL        Controls the master output volume
                9                   [**MASTER CUE**]    Toggles master cue
                13                  HEADPHONES MIX      Controls headphone’s audio source (cue, master)
                15                  BOOTH MONITOR LEVEL Controls the booth output volume
4 - FRONT PANEL 2                   INPUT SELECT        Controls deck source (PC, MIC, CD, PHONO, LINE)
=============== ====== ============ =================== ===============================================

Deck Functions
--------------

.. _managed-by-mixxx-1:

Managed by Mixxx
~~~~~~~~~~~~~~~~

+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Group     | F | [*    | Button Name         | Description                                                                                                                                           |
|           | i | *SHIF |                     |                                                                                                                                                       |
|           | g | T**]? |                     |                                                                                                                                                       |
|           | u |       |                     |                                                                                                                                                       |
|           | r |       |                     |                                                                                                                                                       |
|           | e |       |                     |                                                                                                                                                       |
+===========+===+=======+=====================+=======================================================================================================================================================+
| 1 - DECK  | 1 | -     | [**PLAY/PAUSE**]    | Toggles play/pause (hold pressed while playing: starts brake effect -> release: pause track, press while stopped: starts playback)                    |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**PLAY/PAUSE**]    | Toggles play stutter                                                                                                                                  |
|           |   | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**CUE**]           | Toggles default cue (sets cue point/ goes to cue point)                                                                                               |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | [     | [**CUE**]           | Jump to the beginning of the track and stop                                                                                                           |
|           |   | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | -     | Jog dial (Platter)  | Vinyl-Mode enabled: performs scratching when pressed and rotated, Vinyl-Mode disabled: performs pitch bend                                            |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | [     | Jog dial (Platter)  | Vinyl-Mode enabled: performs scratching considering user-options multiplier when touched and rotated, Vinyl-Mode disabled: performs pitch bend        |
|           |   | **SHI |                     | considering user-options multiplier                                                                                                                   |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | -     | Jog dial (Wheel     | Performs pitch bend when rotated                                                                                                                      |
|           |   |       | side)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | [     | Jog dial (Wheel     | Performs pitch bend when rotated considering user-options multiplier                                                                                  |
|           |   | **SHI | side)               |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 4 | -     | TEMPO               | Controls pitch/tempo ratio                                                                                                                            |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | -     | [**KEYLOCK**]       | Toggles keylock                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | [     | [**KEYLOCK**]       | Changes TEMPO slider range: Doubles the *rateRange*, starting from the value set up in the Mixxx settings, until 100% is reached. On the next press   |
|           |   | **SHI |                     | *rateRange* jumps back to its original value.                                                                                                         |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | -     | [**KEYLOCK**] (Long | Toggles pitch/tempo reset                                                                                                                             |
|           |   |       | press)              |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 6 | -     | [**NEEDLE SEARCH**] | Jumps to equivalent absolute position in track if track is stopped.                                                                                   |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 6 | [     | [**NEEDLE SEARCH**] | Jumps to equivalent absolute position in track while track is playing.                                                                                |
|           |   | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**SYNC**]          | Toggles deck sync                                                                                                                                     |
|           | 3 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**SYNC**]          | Toggles quantize function                                                                                                                             |
|           | 3 | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**AUTO LOOP**]     | Set and enable beat loop                                                                                                                              |
|           | 4 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**AUTO LOOP**]     | Activates / Deactivates current loop                                                                                                                  |
|           | 4 | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**LOOP 1/2X**]     | Halves active loop                                                                                                                                    |
|           | 5 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**LOOP 1/2X**]     | Moves active loop one beat backward (left)                                                                                                            |
|           | 5 | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**LOOP 2X**]       | Doubles active loop                                                                                                                                   |
|           | 6 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**LOOP 2X**]       | Moves active loop one beat forward (right)                                                                                                            |
|           | 6 | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**LOOP IN**]       | Toggles loop in                                                                                                                                       |
|           | 7 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**LOOP IN**]       | Activates current loop, jumps to its loop in point and stops playback.                                                                                |
|           | 7 | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**LOOP OUT**]      | Toggles loop out                                                                                                                                      |
|           | 8 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**LOOP OUT**]      | Toggles reloop / exit loop                                                                                                                            |
|           | 8 | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**VINYL**]         | Toggles vinyl (scratch) mode                                                                                                                          |
|           | 9 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**CENSOR**]        | Toggles reverse roll play                                                                                                                             |
|           | 0 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | [     | [**CENSOR**]        | Toggles reverse play                                                                                                                                  |
|           | 0 | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**SLIP**]          | Toggles slip mode                                                                                                                                     |
|           | 1 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**GRID ADJUST**]   | Hold and touch/rotate Jog dial to adjust beats faster/slower                                                                                          |
|           | 2 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | [     | [**GRID ADJUST**]   | Set/translate beat grid to current track position (adjust position with Jog dial)                                                                     |
|           | 2 | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**GRID SLIDE**]    | Hold and touch/rotate Jog dial to set/translate beat grid earlier/later                                                                               |
|           | 3 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**SHIFT**]         | Switches to shifted controls, no direct function                                                                                                      |
|           | 4 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6 -       | 1 | -     | [**PAD 1**] (HOT    | Set/activate Hot cue 1                                                                                                                                |
| PE        |   |       | CUE mode)           |                                                                                                                                                       |
| RFORMANCE |   |       |                     |                                                                                                                                                       |
| PADS      |   |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**PAD 1**] (HOT    | Clear Hot cue 1                                                                                                                                       |
|           |   | **SHI | CUE mode)           |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**PAD 2**] (HOT    | Set/activate Hot cue 2                                                                                                                                |
|           |   |       | CUE mode)           |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | [     | [**PAD 2**] (HOT    | Clear Hot cue 2                                                                                                                                       |
|           |   | **SHI | CUE mode)           |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | -     | [**PAD 3**] (HOT    | Set/activate Hot cue 3                                                                                                                                |
|           |   |       | CUE mode)           |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | [     | [**PAD 3**] (HOT    | Clear Hot cue 3                                                                                                                                       |
|           |   | **SHI | CUE mode)           |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 4 | -     | [**PAD 4**] (HOT    | Set/activate Hot cue 4                                                                                                                                |
|           |   |       | CUE mode)           |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 4 | [     | [**PAD 4**] (HOT    | Clear Hot cue 4                                                                                                                                       |
|           |   | **SHI | CUE mode)           |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | -     | [**PAD 5**] (HOT    | Set/activate Hot cue 5                                                                                                                                |
|           |   |       | CUE mode)           |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | [     | [**PAD 5**] (HOT    | Clear Hot cue 5                                                                                                                                       |
|           |   | **SHI | CUE mode)           |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 6 | -     | [**PAD 6**] (HOT    | Set/activate Hot cue 6                                                                                                                                |
|           |   |       | CUE mode)           |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 6 | [     | [**PAD 6**] (HOT    | Clear Hot cue 6                                                                                                                                       |
|           |   | **SHI | CUE mode)           |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 7 | -     | [**PAD 7**] (HOT    | Set/activate Hot cue 7                                                                                                                                |
|           |   |       | CUE mode)           |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 7 | [     | [**PAD 7**] (HOT    | Clear Hot cue 7                                                                                                                                       |
|           |   | **SHI | CUE mode)           |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 8 | -     | [**PAD 8**] (HOT    | Set/activate Hot cue 8                                                                                                                                |
|           |   |       | CUE mode)           |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 8 | [     | [**PAD 8**] (HOT    | Clear Hot cue 8                                                                                                                                       |
|           |   | **SHI | CUE mode)           |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PAD 1**] (ROLL   | Toggle Beatloop roll length index 1 (according parameter set)                                                                                         |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**PAD 2**] (ROLL   | Toggle Beatloop roll length index 2 (according parameter set)                                                                                         |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | -     | [**PAD 3**] (ROLL   | Toggle Beatloop roll length index 3 (according parameter set)                                                                                         |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 4 | -     | [**PAD 4**] (ROLL   | Toggle Beatloop roll length index 4 (according parameter set)                                                                                         |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | -     | [**PAD 5**] (ROLL   | Toggle Beatloop roll length index 5 (according parameter set)                                                                                         |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 6 | -     | [**PAD 6**] (ROLL   | Toggle Beatloop roll length index 6 (according parameter set)                                                                                         |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 7 | -     | [**PAD 7**] (ROLL   | Toggle Beatloop roll length index 7 (according parameter set)                                                                                         |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 8 | -     | [**PAD 8**] (ROLL   | Toggle Beatloop roll length index 8 (according parameter set)                                                                                         |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PAD 1**] (SLICER | Press: Jumps to beat position 1 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (continuous slice only):   |
|           |   |       | mode)               | Jumps to actual play position in the background (slip). See `#Slicer description <#Slicer%20description>`__                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**PAD 2**] (SLICER | Press: Jumps to beat position 2 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (continuous slice only):   |
|           |   |       | mode)               | Jumps to actual play position in the background (slip). See `#Slicer description <#Slicer%20description>`__                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | -     | [**PAD 3**] (SLICER | Press: Jumps to beat position 3 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (continuous slice only):   |
|           |   |       | mode)               | Jumps to actual play position in the background (slip). See `#Slicer description <#Slicer%20description>`__                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 4 | -     | [**PAD 4**] (SLICER | Press: Jumps to beat position 4 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (continuous slice only):   |
|           |   |       | mode)               | Jumps to actual play position in the background (slip). See `#Slicer description <#Slicer%20description>`__                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | -     | [**PAD 5**] (SLICER | Press: Jumps to beat position 5 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (continuous slice only):   |
|           |   |       | mode)               | Jumps to actual play position in the background (slip). See `#Slicer description <#Slicer%20description>`__                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 6 | -     | [**PAD 6**] (SLICER | Press: Jumps to beat position 6 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (continuous slice only):   |
|           |   |       | mode)               | Jumps to actual play position in the background (slip). See `#Slicer description <#Slicer%20description>`__                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 7 | -     | [**PAD 7**] (SLICER | Press: Jumps to beat position 7 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (continuous slice only):   |
|           |   |       | mode)               | Jumps to actual play position in the background (slip). See `#Slicer description <#Slicer%20description>`__                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 8 | -     | [**PAD 8**] (SLICER | Press: Jumps to beat position 8 in 8-beat-section and beat loops according quantization index (default: 1/4 beat), Release (continuous slice only):   |
|           |   |       | mode)               | Jumps to actual play position in the background (slip). See `#Slicer description <#Slicer%20description>`__                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PAD 1**]         | Sample deck index 1 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options)      |
|           |   |       | (SAMPLER mode)      | sample deck                                                                                                                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**PAD 1**]         | Sample deck index 1 (according sampler bank) - playing: stop deck, stopped: eject track                                                               |
|           |   | **SHI | (SAMPLER mode)      |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**PAD 2**]         | Sample deck index 2 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options)      |
|           |   |       | (SAMPLER mode)      | sample deck                                                                                                                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | [     | [**PAD 2**]         | Sample deck index 2 (according sampler bank) - playing: stop deck, stopped: eject track                                                               |
|           |   | **SHI | (SAMPLER mode)      |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | -     | [**PAD 3**]         | Sample deck index 3 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options)      |
|           |   |       | (SAMPLER mode)      | sample deck                                                                                                                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | [     | [**PAD 3**]         | Sample deck index 3 (according sampler bank) - playing: stop deck, stopped: eject track                                                               |
|           |   | **SHI | (SAMPLER mode)      |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 4 | -     | [**PAD 4**]         | Sample deck index 4 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options)      |
|           |   |       | (SAMPLER mode)      | sample deck                                                                                                                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 4 | [     | [**PAD 4**]         | Sample deck index 4 (according sampler bank) - playing: stop deck, stopped: eject track                                                               |
|           |   | **SHI | (SAMPLER mode)      |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | -     | [**PAD 5**]         | Sample deck index 5 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options)      |
|           |   |       | (SAMPLER mode)      | sample deck                                                                                                                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | [     | [**PAD 5**]         | Sample deck index 5 (according sampler bank) - playing: stop deck, stopped: eject track                                                               |
|           |   | **SHI | (SAMPLER mode)      |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 6 | -     | [**PAD 6**]         | Sample deck index 6 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options)      |
|           |   |       | (SAMPLER mode)      | sample deck                                                                                                                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 6 | [     | [**PAD 6**]         | Sample deck index 6 (according sampler bank) - playing: stop deck, stopped: eject track                                                               |
|           |   | **SHI | (SAMPLER mode)      |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 7 | -     | [**PAD 7**]         | Sample deck index 7 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options)      |
|           |   |       | (SAMPLER mode)      | sample deck                                                                                                                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 7 | [     | [**PAD 7**]         | Sample deck index 7 (according sampler bank) - playing: stop deck, stopped: eject track                                                               |
|           |   | **SHI | (SAMPLER mode)      |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 8 | -     | [**PAD 8**]         | Sample deck index 8 (according sampler bank) - empty: Load selected track into sample deck, track loaded: start play (default, see user options)      |
|           |   |       | (SAMPLER mode)      | sample deck                                                                                                                                           |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 8 | [     | [**PAD 8**]         | Sample deck index 8 (according sampler bank) - playing: stop deck, stopped: eject track                                                               |
|           |   | **SHI | (SAMPLER mode)      |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PAD 1**] (GROUP2 | Toggle Beatloop length index 1 (according parameter set)                                                                                              |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 2 | -     | [**PAD 2**] (GROUP2 | Toggle Beatloop length index 2 (according parameter set)                                                                                              |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 3 | -     | [**PAD 3**] (GROUP2 | Toggle Beatloop length index 3 (according parameter set)                                                                                              |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 4 | -     | [**PAD 4**] (GROUP2 | Toggle Beatloop length index 4 (according parameter set)                                                                                              |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 5 | -     | [**PAD 5**] (GROUP2 | Toggle Beatloop length index 5 (according parameter set)                                                                                              |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 6 | -     | [**PAD 6**] (GROUP2 | Toggle Beatloop length index 6 (according parameter set)                                                                                              |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 7 | -     | [**PAD 7**] (GROUP2 | Toggle Beatloop length index 7 (according parameter set)                                                                                              |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 8 | -     | [**PAD 8**] (GROUP2 | Toggle Beatloop length index 8 (according parameter set)                                                                                              |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 9 | -     | [**HOT CUE**] mode  | Switches PAD control and illumination to HOT CUE mode                                                                                                 |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**ROLL**] mode     | Switches PAD control and illumination to BEATLOOP ROLL mode                                                                                           |
|           | 0 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**ROLL**] mode     | Switches PAD control and illumination to GROUP2 (BEATLOOP) mode                                                                                       |
|           | 0 | **SHI |                     |                                                                                                                                                       |
|           |   | FT**] |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**SLICER**] mode   | Switches PAD control and illumination to SLICER mode, in SLICER mode switches between continuous slice mode and loop slice mode (see `#Slicer         |
|           | 1 |       |                     | description <#Slicer%20description>`__)                                                                                                               |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**SAMPLER**] mode  | Switches PAD control and illumination to SAMPLER mode                                                                                                 |
|           | 2 |       |                     |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**SAMPLER**] mode  | Toggles SAMPLER PADS velocity mode (velocity ~ volume)                                                                                                |
|           | 2 |       | (long press)        |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Jump *beatjump_size* beats backward                                                                                                                   |
|           | 3 |       | LEFT**] (HOT CUE    |                                                                                                                                                       |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**PARAMETER        | Increase *beatjump_size*                                                                                                                              |
|           | 3 | **SHI | LEFT**] (HOT CUE    |                                                                                                                                                       |
|           |   | FT**] | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Decrement active looproll-interval parameter set (0-3, see `#Loop/Loop-Roll parameter sets <#Loop/Loop-Roll%20parameter%20sets>`__), button LED is    |
|           | 3 |       | LEFT**] (ROLL mode) | illuminated at parameter set 2, 3                                                                                                                     |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Decrement active slicer quantization (1/8, 1/4, 1/2, 1 beat loop), button LED is illuminated at quantization 1/2, 1                                   |
|           | 3 |       | LEFT**] (SLICER     |                                                                                                                                                       |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**PARAMETER        | Decrement active slicer domain (8, 16, 32, 64 beats), button LED is illuminated at domain 32, 64                                                      |
|           | 3 | **SHI | LEFT**] (SLICER     |                                                                                                                                                       |
|           |   | FT**] | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Decrement active sampler bank (0-3), button LED is illuminated at sampler bank 2, 3. Sampler bank 0: sampler 1-8, sampler bank 1: sampler 9-16,       |
|           | 3 |       | LEFT**] (SAMPLER    | sampler bank 2: sampler 17-24, sampler bank 3: sampler 25-32                                                                                          |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Decrement active loop-interval parameter set (0-3, see `#Loop/Loop-Roll parameter sets <#Loop/Loop-Roll%20parameter%20sets>`__), button LED is        |
|           | 3 |       | LEFT**] (GROUP2     | illuminated at parameter set 2, 3                                                                                                                     |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Jump *beatjump_size* beats forward                                                                                                                    |
|           | 4 |       | RIGHT**] (HOT CUE   |                                                                                                                                                       |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**PARAMETER        | Decrease *beatjump_size*                                                                                                                              |
|           | 4 | **SHI | RIGHT**] (HOT CUE   |                                                                                                                                                       |
|           |   | FT**] | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Increment active looproll-interval parameter set (0-3, see `#Loop/Loop-Roll parameter sets <#Loop/Loop-Roll%20parameter%20sets>`__), button LED is    |
|           | 4 |       | RIGHT**] (ROLL      | illuminated at parameter set 1, 3                                                                                                                     |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Increment active slicer quantization (1/8, 1/4, 1/2, 1 beat loop), button LED is illuminated at quantization 1/4, 1                                   |
|           | 4 |       | RIGHT**] (SLICER    |                                                                                                                                                       |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | [     | [**PARAMETER        | Increment active slicer domain (8, 16, 32, 64 beats), button LED is illuminated at domain 16, 64                                                      |
|           | 4 | **SHI | RIGHT**] (SLICER    |                                                                                                                                                       |
|           |   | FT**] | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Increment active sampler bank (0-3), button LED is illuminated at sampler bank 1, 3. Sampler bank 0: sampler 1-8, sampler bank 1: sampler 9-16,       |
|           | 4 |       | RIGHT**] (SAMPLER   | sampler bank 2: sampler 17-24, sampler bank 3: sampler 25-32                                                                                          |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | 1 | -     | [**PARAMETER        | Increment active loop-interval parameter set (0-3, see `#Loop/Loop-Roll parameter sets <#Loop/Loop-Roll%20parameter%20sets>`__), button LED is        |
|           | 4 |       | RIGHT**] (GROUP2    | illuminated at parameter set 1, 3                                                                                                                     |
|           |   |       | mode)               |                                                                                                                                                       |
+-----------+---+-------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _managed-by-the-controller-1:

Managed by the controller
~~~~~~~~~~~~~~~~~~~~~~~~~

The following functions are directly controlled by the controller (Mixxx-independent):

======== ====== ============ =============== =======================================================================
Group    Figure [**SHIFT**]? Button Name     Description
======== ====== ============ =============== =======================================================================
1 - DECK 7      -            [**DECK 1**]    Switches left deck to DECK 1 control and illumination
         8      -            [**DECK 2**]    Switches right deck to DECK 2 control and illumination
         9      -            [**DECK 3**]    Switches left deck to DECK 3 control and illumination
         10     -            [**DECK 4**]    Switches right deck to DECK 4 control and illumination
         11     -            [**DUAL DECK**] Toggles left deck to dual deck control and illumination (DECK 1 and 3)
         12     -            [**DUAL DECK**] Toggles right deck to dual deck control and illumination (DECK 2 and 4)
======== ====== ============ =============== =======================================================================

Loop/Loop-Roll parameter sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By using the [**PARAMETER LEFT**] and [**PARAMETER RIGHT**] buttons in BEATLOOP ROLL (default parameter set: 2) or BEATLOOP mode (default parameter set: 0), you can change the pad-assigned loop size.
The following table shows the possible assignments (unit: beats).

======= ==== ==== ==== ==== ==== ==== ==== ====
Set No. PAD1 PAD2 PAD3 PAD4 PAD5 PAD6 PAD7 PAD8
======= ==== ==== ==== ==== ==== ==== ==== ====
0       1/4  1/2  1    2    4    8    16   32
1       1/8  1/4  1/2  1    2    4    8    16
2       1/16 1/8  1/4  1/2  1    2    4    8
3       1/32 1/16 1/8  1/4  1/2  1    2    4
======= ==== ==== ==== ==== ==== ==== ==== ====

Slicer description
~~~~~~~~~~~~~~~~~~

For a detailed explanation of the slicer mode, take a look at the controller’s `manual <http://docs.pioneerdj.com/Manuals/DDJ_SX_DRH1193_manual/>`__. A limited slicer functionality is implemented into
the controller mapping as described below.

There are two slicer modes, continuous slice and loop slice, which can be selected by pressing the [**SLICER**] mode button. If none or only one PAD (beat) is lit, continuous slice mode is active. If
you press [**SLICER**] mode button again, loop slice mode will be activated and all PADs, except one for the beat, will light up.

Starting with the first beat marked on a playing track, the track is divided into sections of 8 equal parts (not visible in waveform). If the first 8 parts are reached, the next section starts. The
PADs are assigned to one section, each time the active section changes, the PADs will be assigned to the new active section (PAD 1..8 = section part 1..8). The section size is dependent of the
selected slicer domain, changeable by pressing [**SHIFT**] + [**PARAMETER LEFT**] or [**PARAMETER RIGHT**]. The default slicer domain is 8 beats, so each part represents the part between one beat and
the following beat. Possible slicer domains are 8, 16, 32, 64 beats.

Continuous slice mode
^^^^^^^^^^^^^^^^^^^^^

The PAD lights show the active part in the active section: The active part PAD is lit, all other PAD lights are off.

Continuous slice mode moves to the next section if the end of the previous active section is reached.

.. figure:: ../../_static/controllers/pioneer_ddj_sx_slicertype1.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Pioneer DDJ SX Slicer (type 1)
   :figclass: pretty-figures

   Pioneer DDJ SX Slicer (type 1)

By pressing PAD X, the play position jumps to the beat X of the active section. If you have pressed the PAD on-beat and hold it, the play position is playing in loop. The beat loop length depends on
the selected slicer quantization (changeable by pressing [**PARAMETER LEFT**] or [**PARAMETER RIGHT**]). If you release the PAD, the playback will resume where the track would have been if the slicer
wouldn’t have been activated (slip mode).

Loop slice mode
^^^^^^^^^^^^^^^

The PAD lights show the active part in the active section: The active part PAD light is off, all other PADs are lit.

As soon as loop slice mode is activated, the active section is played in loop (not visible in waveform). If the end of the active section is reached, the play position jumps back to the beginning of
the active section.

.. figure:: ../../_static/controllers/pioneer_ddj_sx_slicertype2.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Pioneer DDJ SX Slicer (type 2)
   :figclass: pretty-figures

   Pioneer DDJ SX Slicer (type 2)


By pressing PAD X, the play position jumps to the beat X of the active section. In loop slice mode beat loop is not possible.

As soon as loop slice mode is deactivated (by pressing [**SLICER**] mode button again), the playback will resume where the track would have been if the slicer wouldn’t have been activated (slip mode).

Effect Functions
----------------

This controller mapping uses the `standard Mixxx mapping for effects sections on controllers <standard_effects_mapping>`__.

+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Group       | Figure         | [**SHIFT**]? | Button Name      | Description                                                                                                                     |
+=============+================+==============+==================+=================================================================================================================================+
| 2 - EFFECTS | 1 (L)          | -            | FX1-1            | Focused effect none: Controls EffectRack1-EffectUnit1/3-Effect1 meta, Focused effect 1..3: Controls effect parameter 1 of       |
|             |                |              |                  | focused effect in EffectRack1-EffectUnit1/3                                                                                     |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 1 (L)          | [**SHIFT**]  | FX1-1            | Controls effect selection for EffectRack1-EffectUnit1/3 effect 1                                                                |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 1 (R)          | -            | FX2-1            | Focused effect none: Controls EffectRack1-EffectUnit2/4-Effect1 meta, Focused effect 1..3: Controls effect parameter 1 of       |
|             |                |              |                  | focused effect in EffectRack1-EffectUnit2/4                                                                                     |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 1 (R)          | [**SHIFT**]  | FX2-1            | Controls effect selection for EffectRack1-EffectUnit2/4 effect 1                                                                |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 2 (L)          | -            | FX1-2            | Focused effect none: Controls EffectRack1-EffectUnit1/3-Effect2 meta, Focused effect 1..3: Controls effect parameter 2 of       |
|             |                |              |                  | focused effect in EffectRack1-EffectUnit1/3                                                                                     |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 2 (L)          | [**SHIFT**]  | FX1-2            | Controls effect selection for EffectRack1-EffectUnit1/3 effect 2                                                                |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 2 (R)          | -            | FX2-2            | Focused effect none: Controls EffectRack1-EffectUnit2/4-Effect2 meta, Focused effect 1..3: Controls effect parameter 2 of       |
|             |                |              |                  | focused effect in EffectRack1-EffectUnit2/4                                                                                     |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 2 (R)          | [**SHIFT**]  | FX2-2            | Controls effect selection for EffectRack1-EffectUnit2/4 effect 2                                                                |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 3 (L)          | -            | FX1-3            | Focused effect none: Controls EffectRack1-EffectUnit1/3-Effect3 meta, Focused effect 1..3: Controls effect parameter 3 of       |
|             |                |              |                  | focused effect in EffectRack1-EffectUnit1/3                                                                                     |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 3 (L)          | [**SHIFT**]  | FX1-3            | Controls effect selection for EffectRack1-EffectUnit1/3 effect 3                                                                |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 3 (R)          | -            | FX2-3            | Focused effect none: Controls EffectRack1-EffectUnit2/4-Effect3 meta, Focused effect 1..3: Controls effect parameter 3 of       |
|             |                |              |                  | focused effect in EffectRack1-EffectUnit2/4                                                                                     |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 3 (R)          | [**SHIFT**]  | FX2-3            | Controls effect selection for EffectRack1-EffectUnit2/4 effect 3                                                                |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 4 (L)          | -            | FX1 BEATS        | Controls EffectRack1-EffectUnit1/3 mix                                                                                          |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 4 (R)          | -            | FX2 BEATS        | Controls EffectRack1-EffectUnit2/4 mix                                                                                          |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 4 (L)          | [**SHIFT**]  | FX1 BEATS        | Controls EffectRack1-EffectUnit1/3 super1 knob                                                                                  |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 4 (R)          | [**SHIFT**]  | FX2 BEATS        | Controls EffectRack1-EffectUnit2/4 super1 knob                                                                                  |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 5 (L)          | -            | [**FX1-1 ON**]   | EffectFocusButton press and hold: focus EffectRack1-EffectUnit1/3-Effect1, else: Toggles EffectRack1-EffectUnit1/3-Effect1      |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 5 (R)          | -            | [**FX2-1 ON**]   | EffectFocusButton press and hold: focus EffectRack1-EffectUnit2/4-Effect1, else: Toggles EffectRack1-EffectUnit2/4-Effect1      |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 6 (L)          | -            | [**FX1-2 ON**]   | EffectFocusButton press and hold: focus EffectRack1-EffectUnit1/3-Effect2, else: Toggles EffectRack1-EffectUnit1/3-Effect2      |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 6 (R)          | -            | [**FX2-2 ON**]   | EffectFocusButton press and hold: focus EffectRack1-EffectUnit2/4-Effect2, else: Toggles EffectRack1-EffectUnit2/4-Effect2      |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 7 (L)          | -            | [**FX1-3 ON**]   | EffectFocusButton press and hold: focus EffectRack1-EffectUnit1/3-Effect3, else: Toggles EffectRack1-EffectUnit1/3-Effect3      |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 7 (R)          | -            | [**FX2-3 ON**]   | EffectFocusButton press and hold: focus EffectRack1-EffectUnit2/4-Effect3, else: Toggles EffectRack1-EffectUnit2/4-Effect3      |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 8 (L)          | -            | [**FX1 TAP**]    | EffectFocusButton of EffectRack1-EffectUnit1/3                                                                                  |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 8 (R)          | -            | [**FX2 TAP**]    | EffectFocusButton of EffectRack1-EffectUnit2/4                                                                                  |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 8 (L)          | [**SHIFT**]  | [**FX1 TAP**]    | Switch EffectUnit 1 <-> 3                                                                                                       |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 8 (R)          | [**SHIFT**]  | [**FX2 TAP**]    | Switch EffectUnit 2 <-> 4                                                                                                       |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 9, 10, 11, 12  | -            | [**FX1 ASSIGN**] | Assign EffectRack1-EffectUnit1/3 to specific deck                                                                               |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 13, 14, 15, 16 | -            | [**FX2 ASSIGN**] | Assign EffectRack1-EffectUnit2/4 to specific deck                                                                               |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+
|             | 17, 18, 19, 20 | -            | FILTER           | Control QuickEffectRack1 super1 knob (e.g. moog filter)                                                                         |
+-------------+----------------+--------------+------------------+---------------------------------------------------------------------------------------------------------------------------------+

Troubleshooting
---------------

If you experience any strange behavior of a button or a LED (e.g. wheel LEDs not working), make sure your controller is set up correctly to work with MIXXX. The DDJ-SX provides several settings, which
can be changed in a special *Utility-Mode*.

Utility-Mode
~~~~~~~~~~~~

-  Disconnect USB-cable.
-  Switch off [**STANDBY/ON**] the unit.
-  Hold [**SHIFT**] button and [**PLAY/PAUSE**] button at the left deck while switching on the unit [**STANDBY/ON**].
-  Now *Utility-Mode* is activated.
-  For saving and exiting *Utility-Mode*, switch off the unit again [**STANDBY/ON**].

Setting for usage of Serato DJ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| To use the DDJ-SX with MIXXX, the controller must be configured for the usage of Serato DJ. You can check/change this setting as follows:
| **Press the [KEY LOCK] button at the left deck:**

-  [**KEY LOCK**] button off: Controller is configured for using Serato DJ (default).
-  [**KEY LOCK**] button on (lit): Controller is configured for using different DJ-software.
