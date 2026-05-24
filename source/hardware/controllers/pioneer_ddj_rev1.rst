.. _pioneer-ddj-rev1:

Pioneer DDJ-REV1
================

.. sectionauthor:: AKOI

The Pioneer DDJ-REV1 is a four-channel battle-style USB controller with an
integrated audio interface. This page documents Mixxx-specific mapping
behavior; see the manufacturer’s manual for the physical control layout.

- `Manufacturer’s product page
  <https://www.pioneerdj.com/en/product/controller/ddj-rev1/black/overview/l>`_
- `Manufacturer’s manual
  <https://www.pioneerdj.com/en/support/documents/ddj-rev1/>`_
- `MIDI message list (PDF)
  <https://www.pioneerdj.com/-/media/pioneerdj/software-info/controller/ddj-rev1/ddj-rev1_midi_message_list_e1.pdf>`_
- `Mapping forum thread
  <https://mixxx.discourse.group/t/pioneer-ddj-rev1-mapping-update-2-6/32603>`_

.. versionadded:: 2.5.0

Requirements
------------

Mixxx 2.5 or newer. Supports 2.5 and 2.6+ behavior; see
`Compatibility`_.

AKOI Mapping version **2.2+**

Firmware & drivers
------------------

**Firmware:** At the time this documentation was written there were no
required firmware updates for the Pioneer DDJ-REV1. Check the Pioneer DJ
website for updates.

**Drivers:** No dedicated driver is required for class-compliant operation.
On Windows, ASIO may require installation of the Pioneer audio driver.

Compatibility
-------------

**Controller:** This controller is a class-compliant USB MIDI and audio device,
so it can be used without any special drivers on GNU/Linux, macOS, and
Windows. However, if you wish to use the ASIO sound API under Windows, please
install the latest driver package available.

**Mixxx:** This mapping supports version-gated behavior for Mixxx 2.5 and 2.6+.

==========     ===========================================================================
Mode           Behavior
==========     ===========================================================================
**2.5:** Scratch Bank on :hwlabel:`SCRATCH Bank` pads 1–4 (samples 17–24). 
**2.6+:** Same pads on :hwlabel:`SCRATCH Bank` control stems (mute). Scratch Bank is available via :ref:`Mixxxed Mode` slot 4 when enabled. Stem/EQ options apply only when stem tracks and stem controls are available.
==========     ===========================================================================

**Priority gate:** On a stems-capable runtime, stems mode takes priority over
ScratchBank when both would conflict.

Sound card setup
----------------

This controller has a built-in 4-channel sound card with master output. MIC
input: 1/4" TR jack. Master output: RCA pin jacks. Headphones: 3.5 mm stereo
jack.

In :menuselection:`Preferences --> Sound Hardware`, configure outputs as
follows:

===============  =========== 
Output channel   Assign to
===============  =========== 
1–2              Main
3–4              Headphones
===============  =========== 

=============== =============
Input Channels  Assign to
=============== =============
1-2 (Input 1)   Microphone 1
=============== =============

Input routing
^^^^^^^^^^^^^

On the rear side is a small knob to select the microphone volume. It adjusts
the level of sound input at the microphone input terminal.

.. seealso::
   When the microphone is not in use, turn the level to the minimum available.
   The :ref:`example setups section <setup-laptop-and-external-card>` provides more details about the audio configuration in Mixxx.


Hardware controls
^^^^^^^^^^^^^^^^^

The **Mic Level** hardware control interacts directly with the integrated sound
card and is not mapped to Mixxx.

.. seealso::
   The :ref:`gain staging documentation <djing-gain-staging>` explains how to set your levels properly when using Mixxx.


Mapping description differences
-------------------------------

See the Pioneer manual for the physical control layout. The following
describes Mixxx-specific behavior.

- Automatic version detection (2.5 / 2.6+) (STEMS vs Scratch Bank pad routing).
- :hwlabel:`SHIFT` + :hwlabel:`PLAY/PAUSE` supports braking profiles (Off,
  Classic, Slow) with a default fallback when braking is disabled.
- Configurable Beat Jump, Auto Loop and Beat Roll pads use hold semantics with configurable roll sizes.
- Sampler volume gate and headphone cue logic are tuned for usability.
- ScratchBank mapping and FX buffering are refined for stability.
- 4 Sampler pad layout options are available (see `User configuration options`_).
- Sixteen samples by default (samples 1–16).
- Improvements to Library Sort.
- Scratch Feel.
- Split FX.
- STEMS v2.6+.
- Additional user configuration options.
- Configurable beat tempo ranges.
- VU meter options
- Mixxxed Mode (configurable by deck from controller). 
 - Slot 1: Auto Loop
 - Slot 2: Beat Slicer
 - Slot 3: *Coming Soon*
 - Slot 4: Scratch Bank




Controls
-------------------------------

Browse section
^^^^^^^^^^^^^^

========================  ======================================================  ===========================================================================================
No.                       Control                                                 Function
========================  ======================================================  ===========================================================================================
1                         :hwlabel:`SHIFT` + :hwlabel:`LOAD`                      Sort by user-selected configuration. Double press toggles ascending/descending.
2                         :hwlabel:`Rotary Selector PUSH`                         Push Rotary selector to cycle forward between panels in library.
2                         :hwlabel:`SHIFT` + :hwlabel:`Rotary Selector PUSH`      Hold shift + Push Rotary selector to cycle backwards between panels in library.
3                         :hwlabel:`SHIFT` + :hwlabel:`Rotary Selector`           Rotate selector while holding SHIFT to move left or right in the library or open and close the subcrates panel.
========================  ======================================================  ===========================================================================================


Deck section
^^^^^^^^^^^^

==== ========================================================= ======================================================================
No.  Control                                                   Function
==== ========================================================= ======================================================================
6    :hwlabel:`SYNC`                                           Temporary beat sync. If sync lock is active, a short press cancels the lock.
6    :hwlabel:`SHIFT` + :hwlabel:`SYNC`                        Enable sync lock.
7    :hwlabel:`SHIFT` + :hwlabel:`PLAY/PAUSE`                  Braking disabled: stutter-play. Braking enabled: uses the configured start/stop brake profile (Off / Classic / Slow).
9    :hwlabel:`JOG WHEEL` top / side Vinyl mode:               Top scratches, side bends (or waveform zoom when enabled). CDJ mode: jog uses bend behavior.
==== ========================================================= ======================================================================

Mixer section
^^^^^^^^^^^^^

==== ========================================================= ======================================================================
No.  Control                                                   Function
==== ========================================================= ======================================================================
12   :hwlabel:`(HEADPHONES) CUE`                               PFL toggle with updated head-mix handling (user configuration).
12   :hwlabel:`MASTER CUE`                                     Toggles head-mix behavior (user configuration).
13   :hwlabel:`SHIFT` + :hwlabel:`CHANNEL FADER`               Channel fader start (must be enabled in Utility mode on the controller).
15   :hwlabel:`SHIFT` + :hwlabel:`CROSSFADER`                  Crossfader start (must be enabled in Utility mode on the controller).
==== ========================================================= ======================================================================

.. note::
   Utility mode and fader-start MIDI can vary by hardware firmware. If
   fader-start does not respond after changing utility options, restart Mixxx.

Effect section
^^^^^^^^^^^^^^

==== ============================================================================ ============================================================================================
No.  Control                                                                      Function
4    :hwlabel:`LEVEL/DEPTH`                                                       Adjusts the parameter of the enabled effects for FX1 / FX2.
3    :hwlabel:`SHIFT` + :hwlabel:`FX 1`                                           Cycle to the next effect-chain preset after the currently loaded preset (descending order).
4    :hwlabel:`SHIFT` + :hwlabel:`FX 2`                                           Adjust the average BPM up by +0.01 (beat grid lines move closer together).
5    :hwlabel:`SHIFT` + :hwlabel:`FX 3`                                           Adjust the average BPM down by −0.01 (beat grid lines move farther apart).
4    :hwlabel:`FX1`, :hwlabel:`FX2`, :hwlabel:`FX3` + :hwlabel:`ROTARY SELECTOR`  Designate the effect for the selected FX button (descending order).
==== ============================================================================ ============================================================================================

Sampler section
^^^^^^^^^^^^^^^

==== ========================================================= =================================================================================================
No.  Control                                                   Function
==== ========================================================= =================================================================================================
10   :hwlabel:`SAMPLER PADS 1-8`                               Play the loaded sample, or load the selected track when empty. Follows sampler pad layout.
10   :hwlabel:`SHIFT` + :hwlabel:`SAMPLER PADS 1-8`            Stop the playing sample, or eject a stopped sample.
10   :hwlabel:`SAMPLER` + :hwlabel:`LEVEL/DEPTH`               Sampler gain for samplers 1–16 while held (sampler volume gate).
==== ========================================================= =================================================================================================


Scratch Bank section (Mixxx 2.5)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When stems priority is not active, Scratch Bank uses pads as follows:

==== ========================================================= ======================================================================
No.  Control                                                   Function
==== ========================================================= ======================================================================
10   :hwlabel:`SCRATCH MODE` pads 1–4                          Load scratch samples from samples **17–20(Deck1/3) 21-24 (Deck2/4).**
==== ========================================================= ======================================================================

.. note::
   On 2.6, Scratch Bank moved to *Mixxxed Mode* slot 4. 

Stem section (Mixxx 2.6+)
^^^^^^^^^^^^^^^^^^^^^^^^^

==== ========================================================= ======================================================================
No.  Control                                                   Function
==== ========================================================= ======================================================================
10   :hwlabel:`SCRATCH MODE pads 1–4`                          Stem mute toggles (voice / melody / bass / drums).
10   :hwlabel:`SCRATCH MODE pads 5–8`                          Stem effect toggles (voice / melody / bass / drums).
10   :hwlabel:`STEM PAD pads 1–4` + :hwlabel:`LEVEL/DEPTH`     Adjust stem volume / while held parameters while held.
10   :hwlabel:`STEM PAD pads 5–8` + :hwlabel:`LEVEL/DEPTH`     Adjust effect volume / while held.
10   :hwlabel:`STEM PAD pads 1–4` + :hwlabel:`Rotary Selector` Select stem effect chain / while held.
==== ========================================================= ======================================================================

.. figure:: ../../_static/controllers/Mixxx-250-Hardware-DDJ_REV1-stems-layout.svg
   :align: center
   :width: 350
   :alt: Stems and stem-effect positions: voice, melody, bass, drums.
   :figclass: pretty-figures

   Stems and stem-effect positions: voice, melody, bass, drums.

Beat Jump / Roll section
^^^^^^^^^^^^^^^^^^^^^^^^

==== ========================================================= ======================================================================
No.  Control                                                   Function
==== ========================================================= ======================================================================
10   Beat Jump :hwlabel:`pads 1–4`                             One-shot beat jump / back / size controls.
10   Beat Jump :hwlabel:`pad 5`                                Previous track (deck must not be playing).
10   Beat Jump :hwlabel:`pads 6 /`                             Hold-to-rewind / hold-to-fast-forward.
10   Beat Jump :hwlabel:`pad 8`                                Hold-to-censor (``reverseroll``).
11   Beat Roll :hwlabel:`pads 1–8`                             Hold loop roll with per-pad configurable roll sizes and available actions.
==== ========================================================= ======================================================================

Extra controls section
^^^^^^^^^^^^^^^^^^^^^^

==== ========================================================= ======================================================================
No.  Control                                                   Function
==== ========================================================= ======================================================================
10   Scratch Mode :hwlabel:`SHIFT` + :hwlabel:`Pad1`           AutoDJ.
10   Scratch Mode :hwlabel:`SHIFT` + :hwlabel:`Pad2`           AutoDJ fade to next.
10   Scratch Mode :hwlabel:`SHIFT` + :hwlabel:`Pad3`           Toggle Microphone.
10   Scratch Mode :hwlabel:`SHIFT` + :hwlabel:`Pad4`           Toggle Record Mix.
10   Scratch Mode :hwlabel:`SHIFT` + :hwlabel:`Pad5`           Key Match.
10   Scratch Mode :hwlabel:`SHIFT` + :hwlabel:`Pad6`           Beat Grid.
10   Scratch Mode :hwlabel:`SHIFT` + :hwlabel:`Pad7`           Pitch Up.
10   Scratch Mode :hwlabel:`SHIFT` + :hwlabel:`Pad8`           Pitch Down.
==== ========================================================= ======================================================================

*MIXXXED MODE* section
^^^^^^^^^^^^^^^^^^^^^^

==== ========================================================== ======================================================================
No.  Control                                                    Function
0    Auto Loop Mode :hwlabel:`SHIFT` + :hwlabel:`←FX2/FX3→`     Select Mixxxed mode.
1    Auto Loop Mode :hwlabel:`Mode 1:` ``Auto Loop``            Set loop length. User configuration applies.
2    Auto Loop Mode :hwlabel:`Mode 2:` ``Beat Slicer``          Segment beat into small consumable pieces. Default continuous mode. 
2    Auto Loop Mode :hwlabel:`SHIFT` + :hwlabel:`Pad7`          Update Beat Slicer domain 8/16/32/64. Loop size and slice jump size increases accordingly.
2    Auto Loop Mode :hwlabel:`SHIFT` + :hwlabel:`Pad8`          Loop Beat Slicer.

3    Auto Loop Mode :hwlabel:`Mode 3:` ``Piano (Unavailable)``  Coming soon Piano, Play Through+!

4    Auto Loop Mode :hwlabel:`Mode 4:` ``Scratch Bank``         Loads selected scratch samples to respective deck.
4    Auto Loop Mode :hwlabel:`pads 1–4`                         Load scratch samples from samples **17–20(Deck1/3) 21-24** (Deck2/4).


==== ========================================================== ======================================================================

.. note:: ``Beat Slicer`` If domain does not update and autoloop engaged, disengage auto loop. (Temp fix)*

User configuration options
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Controller settings are exposed in mapping options (XML); script defaults apply
as fallback.

.. list-table::
   :header-rows: 1
   :widths: 23 62 15
   :class: longtable

   * - Variable
     - Function
     - Default
   * - ``PioneerDDJREV1.vinylMode``
     - Per-deck startup vinyl / CDJ mode.
     - ``true``
   * - ``PioneerDDJREV1.VinylSlipAutoff``
     - Auto-enable slip on vinyl touch and auto-disable on release.
     - ``false``
   * - ``PioneerDDJREV1.nonShiftScratchFeel``
     - Scratch speed: DEFAULT / PLX / DIGITAL / AKO / STUDIO.
     - ``Default``
   * - ``PioneerDDJREV1.librarySortDefaults``
     - Sort by any available library option.
     - ``"artist"``, ``"bpm"``, ``"date added"``, ``"key"``
   * - ``PioneerDDJREV1.bigLibraryShiftPush``
     - :hwlabel:`SHIFT` + :hwlabel:`ROTARY SELECTOR PUSH` Maximize and minimize "Big Library". *Replaces library backwards panel movement. Use forward to cycle through.*
     - ``false``
   * - ``PioneerDDJREV1.beatJumpSize1`` … ``beatJumpSize8``
     - Per-pad configuration for beat jump size, includes action override.
     - ``Back/Half/Double/Forward`` … ``Prev/RWD/FWD/Censor``
   * - ``PioneerDDJREV1.autoLoopSize1`` … ``autoLoopSize8``
     - Per-pad loop sizes for auto loop mode (1/32...-64, halves/doubles).
     - ``1/16`` … ``8``
   * - ``PioneerDDJREV1.beatLoopRollsSize1`` … ``beatLoopRollsSize8``
     - Per-pad roll sizes for beat roll mode (1/32...-64, halves/doubles).
     - ``1/4`` … ``32``
   * - ``PioneerDDJREV1.sZoom``
     - Use vinyl side jog for waveform zoom.
     - ``false``
   * - ``PioneerDDJREV1.waveformZoomMode``
     - Attach waveform zoom to deck Vinyl or CDJ mode when enabled.
     - ``vinyl``
   * - ``PioneerDDJREV1.vuMeterMode``
     - VU meter routing: legacy per-deck meters, or stereo split master (left , right).
     - ``per_deck``
   * - ``PioneerDDJREV1.brakingEnabled``
     - Enable profile-based :hwlabel:`SHIFT` + :hwlabel:`PLAY` braking.
     - ``false``
   * - ``PioneerDDJREV1.brakingStartProfile``
     - Start profile for :hwlabel:`SHIFT` + :hwlabel:`PLAY`: ``off`` / ``classic`` / ``slow``.
     - ``off``
   * - ``PioneerDDJREV1.brakingStopProfile``
     - Stop profile for :hwlabel:`SHIFT` + :hwlabel:`PLAY`: ``off`` / ``classic`` / ``slow``.
     - ``off``
   * - ``PioneerDDJREV1.tempSamplerSkin``
     - Show sampler UI while using the sampler volume gate.
     - ``false``
   * - ``PioneerDDJREV1.studioPflAdjustment``
     - PFL adjustment: Off / Auto / Studio.
     - ``Auto``
   * - ``PioneerDDJREV1.splitFx``
     - :hwlabel:`LEVEL/DEPTH` routing: Off (default) controls both FX units; On routes :hwlabel:`LEVEL/DEPTH`-> FX1 vs :hwlabel:`SHIFT` + :hwlabel:`LEVEL/DEPTH`-> FX2.
     - ``false``
   * - ``PioneerDDJREV1.enableFxUnit34ShiftLock``
     - :hwlabel:`SHIFT` + :hwlabel:`LOCK ON`-> FX3/4.
     - ``false``
   * - ``PioneerDDJREV1.tempoRangeProfile``
     - :hwlabel:`Deck Select` long press cycles through preselected ranges (wraps to first step). Default [8%, 16%, 50%], Classic [6%, 10%, 16%, 25%], Alt Step Size [8%, 24%, 50%], Extreme [8%, 16%, 50%, 100%].
     - ``Default``
   * - ``PioneerDDJREV1.multiModeEnabled``
     - :hwlabel:`Shift` + :hwlabel:`←FX2/FX3→` cycles through available modes.
     - ``false``
   * - ``PioneerDDJREV1.disableStartFader``
     - :hwlabel:`Shift` + :hwlabel:`Any fader` Disables channel and crossfader start.
     - ``false``
   * - ``PioneerDDJREV1.samplePadLayout``
     - ``Standard`` / ``Banked Rows`` / ``Mirrored``/ ``Per Pad 32``.
     - ``Standard``

.. note:: ``samplePadLayout`` layouts

  - **Standard (linear):** (Deere, Tango) 
       - Left 1–8, right 9–16 (top to bottom, linear).
  - **Banked rows:** (Late Night) 
      - Top row: left 1–4, right 5–8. Bottom row: left 9–12, right 13–16.
  - **Mirrored:** Default order reversed within each row. 
      - Top 4 3 2 1, bottom 8 7 6 5; deck 2 mirror: top 12 11 10 9, bottom 16 15 14 13.
  - **Per Pad 32:** Each deck controls its own bank of 8 samplers:
       - Deck 1 → 1–8, Deck 2 → 9–16, Deck 3 → 17–24, Deck 4 → 25–32. (Top to bottom, linear).
        - Note: `Pad 32`` conflicts with ScratchBank’s current Sampler 17–24 pool (Deck 3 sampler pads overlap).


Known issues
~~~~~~~~~~~~

- Controller Utility mode may not expose all expected fader-start MIDI
  variants on the hardware (controller limitation).
- Fader-start behavior can depend on controller-side utility state and may
  require a Mixxx restart after utility changes (controller limitation).
- Classic scratch row is not used on 2.6+; Scratch Bank via Mixxxed Mode slot 4.
