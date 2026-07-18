.. _native-instruments-traktor-mx2:

Native Instruments Traktor MX2
==============================

The MX2 is a two-channel controller with an integrated sound card. It has two integrated stereo outputs (line and 1/8" / 3.5 mm TRS), headphone outputs (1/8" / 3.5 mm TRS) and microphone
inputs (1/4" / 6.3 mm TRS). The MX2 uses the standard HID protocol to send and receive signals from a computer, so it can work with Mixxx.

- `Manufacturer’s product page <https://www.native-instruments.com/de/products/traktor/dj-controllers/traktor-mx2/>`__
- `Mapping forum thread <https://mixxx.discourse.group/t/native-instruments-traktor-mx2/33225>`__

.. versionadded:: 2.6.0

Mixxx Sound Hardware Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Main output: channels 1-2
-  Headphone output: channels 3-4

Controller Preferences
~~~~~~~~~~~~~~~~~~~~~~

- **Use Pattern Mode for Samplers**: Allows the Pattern mode to take control of Mixxx's sampler decks instead of remaining unused.

Mixxx Mapping
~~~~~~~~~~~~~

The Mixxx mapping for the MX2 is designed to mirror Native Instruments' original layout as closely as possible, while replacing some Traktor only features with Mixxx's ones like Patterns (Traktor) → Samplers (Mixxx). For a reference to the original Traktor layout, you can consult `section 4 of their manual <https://www.native-instruments.com/fileadmin/ni_media/downloads/manuals/traktor/Traktor_MX2_user_guide-en.pdf>`__.

Please refer to the sections below for the exact mapping of all elements:

- `Effect Units`_
- `Overview`_
- `Channel Controls (1-30)`_
- `Multi-Function Controls`_
- `Mixer Controls (31-38)`_

Effect Units
++++++++++++

The effect units support cycling through four distinct modes by pressing :kbd:`SHIFT` + Misc (leftmost button in the FX section): **Group Mode**, **Single 1**, **Single 2**, and **Single 3**.

- **Group Mode**: Controls three independent effects. The three effect buttons toggle their respective effects on or off. The three effect parameter knobs control the 'meta' parameter for the effects.
- **Single Mode (1, 2, or 3)**: Focuses the controller on one specific effect slot. The Misc button acts as an on/off toggle for the focused effect. It lights up in red (Single 1), blue (Single 2), or green (Single 3) to clearly indicate the active slot. The three effect buttons control the first, second, and third button parameters of the focused effect, respectively. The three parameter knobs control the first, second, and third parameters of the focused effect, respectively.

In all modes, :kbd:`SHIFT` + Effect Button cycles the selected effect in the button's effect slot. The `Mix` knob (leftmost) controls the 'dry/wet' parameter for the whole unit.

Overview
++++++++

.. figure:: ../../_static/controllers/native_instruments_traktor_mx2.svg
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Native Instruments Traktor MX2 (schematic view)
   :figclass: pretty-figures

   Native Instruments Traktor MX2 (schematic view)


Channel Controls (1-30)
+++++++++++++++++++++++

+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| Element            | Primary function                                                                                                            | Secondary function (+ SHIFT)                        |
+====================+=============================================================================================================================+=====================================================+
| **1**. FX Main knob| *See Multi-Function Controls table below*                                                                                   |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **2**. FX Param    | *See Multi-Function Controls table below*                                                                                   |                                                     |
| knob               |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **3**. FX Toggle   | *See Multi-Function Controls table below*                                                                                   |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **4**. Preparation | Add selected track to AutoDJ queue (bottom)                                                                                 | Add selected track to AutoDJ queue (top)            |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **5**. Browse knob | *See Multi-Function Controls table below*                                                                                   |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **6**. Preview     | | Load selected track into preview deck, or play/pause if already loaded                                                    |                                                     |
| button             |                                                                                                                             |                                                     |
|                    | Buttons are linked: preview on channels 1 & 2 control the same preview deck                                                 |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **7**. List view   | Toggle maximizing the library                                                                                               |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **8**. FLX button  | Enable and disable slip mode                                                                                                |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **9**. REV button  | Reverse play while held                                                                                                     | Reverse play + slip mode while held                 |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **10**. Turntable  | Set jog wheel to **Turntable Mode**                                                                                         |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **11**. Jog button | Set jog wheel to **Jog Mode**                                                                                               |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **12**. Jog wheel  | **Turntable Mode**: Control scratching when touched from the top (bend the pitch when touched from the side)                |                                                     |
|                    |                                                                                                                             |                                                     |
|                    | **Jog Mode**: Temporarily bend the pitch                                                                                    |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **Shift** button   | Activates secondary functions when pressed                                                                                  |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **14**. Sync button| Sync the BPM and phase (depending on quantize). Press longer to activate sync lock on that deck                             | Sync the phase to that of the other track           |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **15**. Sync master| Set the deck as sync leader                                                                                                 |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **16**. Move knob  | *See Multi-Function Controls table below*                                                                                   |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **17**. Keylock    | *See Multi-Function Controls table below*                                                                                   |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **18**. Loop knob  | *See Multi-Function Controls table below*                                                                                   |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **CUE** button     | CUE default                                                                                                                 | If the CUE point is set, jump to it and stop        |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **Play** button    | Toggle playing                                                                                                              | Seek the player to the start and then stop it       |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **Hotcues**        | Activate **Hotcue Mode** (for the number buttons)                                                                           |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **Stems**          | Activate **Stems Mode** (for the number buttons)                                                                            |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **Patterns**       | Activate **Sampler Mode** (if enabled in Controller Preferences) (for the number buttons)                                   |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **Loops**          | Activate **Loops Mode** (for the number buttons)                                                                            |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **19**. Number     | *See Multi-Function Controls table below*                                                                                   |                                                     |
| buttons 1-4        |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **20**. Number     | *See Multi-Function Controls table below*                                                                                   |                                                     |
| buttons 5-8        |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **21**. Tempo fader| Adjust tempo and (if not keylocked) speed                                                                                   |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **22**. Pre-Gain   | Adjust the pre-fader gain of the deck                                                                                       |                                                     |
| knob               |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **23**. FX select  | Select whether FX1 / FX2 should be applied to the deck                                                                      |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **24**. HI knob    | High frequency filter                                                                                                       |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **25**. MID knob   | Middle frequency filter                                                                                                     |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **26**. LOW knob   | Low frequency filter                                                                                                        |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **27**. GFX        | Quick effect (**35**, **36**) 'meta' parameter knob for the deck                                                            |                                                     |
| parameter knob     |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **28**. GFX toggle | Toggle whether GFX (**35**, **36**) should be applied to the deck. Hold while pressing **35** or **36** to enable the effect|                                                     |
| button             | only on this channel                                                                                                        |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **29**. Headphone  | Toggle headphone cueing                                                                                                     |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **30**. Volume     | Adjust the channel volume fader for the corresponding deck                                                                  |                                                     |
| fader              |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+



Multi-Function Controls
++++++++++++++++++++++++

+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| Element            | Primary function                                                                                                            | Secondary function (+ SHIFT)                        |
+====================+=============================================================================================================================+=====================================================+
| **1**. FX Main knob| **All modes**: Control the 'dry/wet' parameter of FX1 / FX2                                                                 |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **2**. FX Param    | **Group Mode**: Control the 'meta' parameter of effects 1-3 in FX1 / FX2                                                    |                                                     |
| knob               |                                                                                                                             |                                                     |
|                    | **Single Mode (1-3)**: Control the 1st, 2nd, and 3rd parameters of the focused effect, respectively                         |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **3**. FX Toggle   | **Group Mode**: Toggle effects 1-3 in FX1 / FX2                                                                             | **All modes**: Cycle through effects                |
| button             |                                                                                                                             |                                                     |
|                    | **Single Mode (1-3)**: Control the 1st, 2nd, and 3rd button parameters of the focused effect, respectively                  |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **X** Misc button  | **Group Mode**: (No primary function)                                                                                       | **All modes**: Cycle through effect unit modes      |
| (leftmost in FX)   |                                                                                                                             | (Group → Single 1 → Single 2 → Single 3 → Group)    |
|                    | **Single Mode (1-3)**: Toggle the focused effect on/off                                                                     |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **5**. Browse knob | **Default**: Scroll in tracks table                                                                                         | Scroll in tree view                                 |
| **turn**           | **Preview playing**: Seek through preview                                                                                   |                                                     |
|                    | **Sampler Mode** (Hold pads 5-8): Change pregain of sampler                                                                 |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **5**. Browse knob | **Hovering Track**: Load selected track into deck                                                                           |                                                     |
| **press**          | **Hovering Library**: Expand / Collapse hovered item                                                                        | Go to tracks table of currently hovered item        |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **16**. Move knob  | **Default**: Beatjump backwards/forwards                                                                                    | Halve or double beatjump size                       |
| **turn**           |                                                                                                                             |                                                     |
|                    | **Stems Mode** (Hold pads 5-8): Control volume of stem                                                                      |                                                     |
|                    |                                                                                                                             |                                                     |
|                    | **Sampler Mode** (Hold pads 5-8): Seek through sampler track                                                                |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **16**. Move knob  | **Default**: Activate a rolling loop of the defined number of beats. Once disabled, playback will resume where the track    | Activate current loop, jump to its loop in point,   |
| **press**          | would have been if it had not entered the loop                                                                              | and stop playback                                   |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **17**. Keylock    | **Default**: Enable keylock for the deck. Toggle loop knob **18** to **Pitch Mode** while being held                        |                                                     |
| button             |                                                                                                                             |                                                     |
|                    | **Sampler Mode** (Hold pads 5-8): Toggle sampler keylock                                                                    |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **18**. Loop knob  | **Default**: Halve or double loop size                                                                                      |                                                     |
| **turn**           |                                                                                                                             |                                                     |
|                    | **Pitch Mode**: Change pitch of the track                                                                                   |                                                     |
|                    |                                                                                                                             |                                                     |
|                    | **Stems Mode** (Hold pads 5-8): Control the 'meta' parameter of the stems' effect                                           | Cycle through effects                               |
|                    |                                                                                                                             |                                                     |
|                    | **Sampler Mode** (Hold pads 5-8): Change rate (speed, pitch depending on keylock) of sampler                                |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **18**. Loop knob  | **Default**: Set a loop of the defined number of beats and enable the loop                                                  | Toggle the current loop on or off                   |
| **press**          |                                                                                                                             |                                                     |
|                    | **Sampler Mode** (Hold pads 5-8): Toggle sampler repeat                                                                     |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **19**. Number     | **Hotcue Mode**: If hotcue is set, seek the player to hotcue position. Otherwise set hotcue at current position             | Clear the hotcue                                    |
| buttons 1-4        |                                                                                                                             |                                                     |
|                    | **Stems Mode**: Toggle mute stem 1-4                                                                                        |                                                     |
|                    |                                                                                                                             |                                                     |
|                    | **Sampler Mode**: Toggle the playback state of the sampler (sampler 1-4 on channel 1, sampler 5-8 on channel 2)             |                                                     |
|                    |                                                                                                                             |                                                     |
|                    | **Loops Mode**: Enable a rolling loop of 1/16, 1/8, 1/4, 1/2 beats while being held                                         | Enable default loop instead                         |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **20**. Number     | **Hotcue Mode**: like **19**                                                                                                | like **19**                                         |
| buttons 5-8        |                                                                                                                             |                                                     |
|                    | **Stems Mode**: Hold to use stems modifier functions (see **16**, **18**)                                                   |                                                     |
|                    |                                                                                                                             |                                                     |
|                    | **Sampler Mode**: Hold to use sampler modifier functions (see **5**, **16**, **17**, **18**)                                |                                                     |
|                    | (sampler 1-4 on channel 1, sampler 5-8 on channel 2)                                                                        |                                                     |
|                    |                                                                                                                             |                                                     |
|                    | **Loops Mode**: Enable a rolling loop of 1, 2, 4, 8 beats while being held                                                  | Enable a default loop instead                       |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+

Mixer Controls (31-38)
+++++++++++++++++++++++

+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| Element            | Primary function                                                                                                            | Secondary function (+ SHIFT)                        |
+====================+=============================================================================================================================+=====================================================+
| **31**. Gain knob  | *Unmapped* (adjusts the hardware gain)                                                                                      |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **32**. VuMeter    | Show the current instantaneous deck volume                                                                                  |                                                     |
| LEDs               |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **33**. Headphone  | Adjust the cue/main mix in the headphone output                                                                             |                                                     |
| mix knob           |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **34**. Headphone  | Adjust the headphone output gain                                                                                            |                                                     |
| gain knob          |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **35**. Effect     | | Load preset from the Quick Effect presets list on both decks. The first 8 presets from the list can be selected           |                                                     |
| buttons (GFX)      | | Press the button once to get the first preset, press twice for the second preset                                          |                                                     |
|                    | | Press once (Press twice):                                                                                                 |                                                     |
|                    | | 1 (5)  2 (6)                                                                                                              |                                                     |
|                    | | 3 (7)  4 (8)                                                                                                              |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **36**. Filter     | Load the 'Filter' effect preset                                                                                             |                                                     |
| effect button (GFX)|                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **37**. Microphone | Toggle microphone talkover, long press for permanent activation                                                             |                                                     |
| button             |                                                                                                                             |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
| **38**. Crossfader | Adjust the crossfader between both decks                                                                                    |                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
