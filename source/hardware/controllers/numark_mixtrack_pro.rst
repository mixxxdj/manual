.. _numark-mixtrack-pro:

Numark Mixtrack Pro
===================

The **Numark Mixtrack Pro** is functionally identical to the :ref:`Numark Mixtrack <numark-mixtrack>`, but includes a built-in USB audio interface.

This model has been discontinued and was succeeded by the :ref:`Numark Mixtrack Pro 3 <numark-mixtrack-pro-3>`.

-  `Manufacturer’s product page <http://www.numark.com/product/mixtrackpro>`__
-  `Mixxx forum thread <https://mixxx.discourse.group/t/numark-mixtrack-pro-by-vespadj/32635>`__

.. versionadded:: 1.8.2
.. versionchanged:: 2.5.x

Overview
--------

The Mixtrack Pro combines traditional two-deck controls with an integrated sound card for main and headphone outputs.

It is compatible with Mixxx and supports plug-and-play operation on most systems.

.. _audio-interface:

Audio Interface
---------------

-  :hwlabel:`OUTPUT 1` (RCA):** Main mix output to speakers or amplifier.
-  :hwlabel:`OUTPUT 2` (RCA):** Cue channel for headphone monitoring.
-  :hwlabel:`HEADPHONES` (1/4”):** Mirrors the cue channel.
-  :hwlabel:`MIC THROUGH` (1/4”):** Mic input directly mixed into the master output (not routed to the computer).

Typical configuration in Mixxx:

-  Channels **1–2**: Master output (stereo)
-  Channels **3–4**: Headphones (cue/PFL) (stereo)

Mapping Description
-------------------

.. figure:: ../../_static/controllers/numark_mixtrack_pro.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Numark Mixtrack Pro (schematic view)
   :figclass: pretty-figures

   Numark Mixtrack Pro (schematic view)

1.  :hwlabel:`USB`: Sends and receives control information between the controller and the computer.

2.  :hwlabel:`TREBLE`: Adjusts the high-frequency range of the channel.

3.  :hwlabel:`MID`: Adjusts the mid-frequency range.

    *Advanced alternative mapping available at* :ref:`mapping-settings`.

4.  :hwlabel:`BASS`: Adjusts the low-frequency range.

5.  :hwlabel:`CUE` *(round button)*: "PFL". Sends pre-fader audio to the cue channel for headphone monitoring.

    *Advanced alternative mapping available at* :ref:`mapping-settings`.

6.  :hwlabel:`CUE GAIN`: Adjusts the cue channel volume.

7.  :hwlabel:`CUE MIX`: Blends cue and master signals in the headphone output.

    Turn fully left to hear only the cue signal; fully right to hear only the master mix.

8.  :hwlabel:`BROWSE`: Turn and press. Turn the knob to scroll through tracks in the library.

    - In File mode (see 9), press to load the highlighted track into the first stopped deck.
    - In Folder mode (see 9), scroll library, press to unfold item.

9.  :hwlabel:`BACK`: Toggles the browse knob between folder navigation and track list modes (indicated by the FOLDER or FILE LEDs).

10. :hwlabel:`LOAD A` / :hwlabel:`LOAD B`: Loads the selected track into Deck 1 (A) or Deck 2 (B).

| *May be works only if the deck is stopped depending by* :menuselection:`Preferences --> Deck --> Loading a track, when deck is playing`.
|  Resets rate/pitch to 0% on load (regardless of slider position).*

11. :hwlabel:`A GAIN` / :hwlabel:`B GAIN` fader: Adjusts the channel volume.

12. :hwlabel:`MASTER GAIN` fader: Controls the overall output volume.

13. **CROSSFADER:** Blends audio between Decks 1 and 2.

14. **JOG WHEEL:**

    - While stopped: scrubs through the track.
    - With :hwlabel:`SCRATCH` mode on: the top surface scratches (supports backspin); the edge nudges rate.
    - With :hwlabel:`SCRATCH` mode off: nudges rate while playing.

    *Advanced alternative mapping available at* :ref:`mapping-settings`.

15. :hwlabel:`SCRATCH`: Toggles Scratch Mode (LED on when active).

16. :hwlabel:`PLAY / PAUSE`: Starts or pauses playback.

    LED on = playing; LED off = stopped.

    *Advanced alternative mapping available at* :ref:`mapping-settings`.

17. :hwlabel:`STUTTER`: Repositions the BeatGrid for better synchronization.

    *LED blinks at each beat of the grid.*

18. :hwlabel:`CUE` *(rectangular button)*:

    - When paused: sets the cue point.
    - When playing: returns to the cue point and pauses.

    Hold to play from the cue point temporarily; releasing returns to the cue point.

    If :hwlabel:`PLAY` is pressed before releasing, playback continues.

    *LED blinks on beats during the last 30 seconds of the track.*

    *Avoid setting cue points too close to the end of the track.*

19. :hwlabel:`SYNC`: Matches tempo and phase to the other deck.

    *If the other deck is stopped, only tempo is synced (not phase).*

    *LED acts as peak indicator.*

    :hwlabel:`SHIFT` *(24) +* :hwlabel:`SYNC` *: resets pitch to 0%.*

20. **RATE FADER:** Controls playback speed.

    LED lights near 0%.

    *Soft-takeover prevents sudden jumps when hardware/software values differ.*

21. :hwlabel:`PITCH BEND` **(– / +)**: Operation depends on :ref:`mapping-settings`.

22. :hwlabel:`KEYLOCK`: preserve key (pitch) on playback speed changes.

23. **HOT CUE BUTTONS (1-3):**

    Printed as :hwlabel:`EQ KILL`: :hwlabel:`BASS`,  :hwlabel:`MID`,  :hwlabel:`TREBLE`.

    - Unlit: press to assign a hot cue at the current position.
    - Lit: press to jump to the stored cue point.

    :hwlabel:`SHIFT` *(24) + HOTCUE: clears the hot cue.*

24. :hwlabel:`SHIFT`: also printed as :hwlabel:`DELETE`, :hwlabel:`VIEW`, :hwlabel:`TICK`.

    - Enables secondary button functions (LED on).
    - Deactivates automatically after one use.

    Combinations:

    - :hwlabel:`SHIFT` + **HOTCUE:** clears Hotcue.
    - :hwlabel:`SHIFT` + :hwlabel:`MANUAL` **:** toggles Quantize ON/OFF.
    - :hwlabel:`SHIFT` + :hwlabel:`RELOOP` **:** clears active loop (`loop_remove`).
    - :hwlabel:`SHIFT` + :hwlabel:`SYNC` **:** resets pitch to 0%.

    *Advanced Alternative Mapping is avaible at* :ref:`mapping-settings`.

25. :hwlabel:`EFFECT`: Toggle current FX on the current channel.

    *Advanced Alternative Mapping is avaible at* :ref:`mapping-settings`.

26. **EFFECT** :hwlabel:`SELECT`: Turn to scroll through enabled effects, in Mixxx :menuselection:`Preferences --> Effects --> Visible effects`, and load on-the-fly.

    - Press to reset to default the *Quick Effect Super knob*.
    - On the left deck: press, hold, and turn to adjust the *Waveform Zoom*.

27. **LEFT EFFECT** :hwlabel:`CONTROL`: Adjusts the MetaKnob.

    **RIGHT EFFECT** :hwlabel:`CONTROL`: Adjusts Mix (dry/wet) knob for FX.

28. **MODE:** Switches between :hwlabel:`AUTO` Loop and :hwlabel:`MANUAL` Loop modes.

    **Auto Loop Mode (LED off):**

    - :hwlabel:`1/2`: creates a 1-beat loop or halves loop length.
    - :hwlabel:`1 BAR`: creates a 4-beat loop or exits the loop.
    - :hwlabel:`2X`: doubles loop length or reloop (exit with *OUT* button).

    **Manual Mode (LED on):**

    :hwlabel:`SHIFT` *(24) + MODE: toggles Quantize (recommended for manual looping).*

    - :hwlabel:`IN`: sets loop start point.
    - :hwlabel:`OUT`: sets loop end point and activates loop.
    - :hwlabel:`RELOOP`: reactivates last loop or exits current *manual* loop.

    *Panic or clear:* :hwlabel:`SHIFT` *(24) +* :hwlabel:`RELOOP`: clears loop (`loop_remove`).

    *Advanced alternative mapping available at* :ref:`mapping-settings`.

29. :hwlabel:`OUTPUT 1`: See :ref:`audio-interface`.
30. :hwlabel:`OUTPUT 2`: See :ref:`audio-interface`.
31. :hwlabel:`HEADPHONES`: See :ref:`audio-interface`.
32. :hwlabel:`MIC GAIN`: Controls the microphone level sent to the main mix.
33. :hwlabel:`MIC THROUGH`: See :ref:`audio-interface`.

.. _mapping-settings:

Mapping Settings
----------------

Check in Mixxx: :menuselection:`Preferences --> Controllers --> MixTrack Pro --> Mapping Settings`.

The following advanced or alternative mappings are available:

-  **Play/Pause performs Brake and Soft Start when “SCRATCH LED” is on.**
   *Requires Mixxx ≥ 2.6.*

-  **Edit Loop by Touch-Wheel:** If Scratch LED is off and a loop is active, touching the wheel top, then rotate forward for starting the editing of Loop-IN or rotate backward for Loop-OUT point.

-  **PITCH BEND buttons:** follow options available.

    - Rate temp up/down: fine temporarily adjusts playback speed (press and hold).
    - Beat jump *(Default)*: beat jump, value by Mixxx. Hold + Wheel for fast moving on track.
    - Pitch-Key up/down: changes key of track.

-  **Quick Effect Super knob on MID knob:** Enables the Quick-Effect super knob (Filter by default) on the MID knob when this modifier is active.

   Options:

    -  None (disabled)
    -  CUE (PFL) *(default)*
    -  SHIFT (VIEW / TICK / DELETE)
    -  EFFECT

-  **Scratch Sensibility:** *default* 600.

Known Problems
--------------

-  The pitch faders on the controller have a very short run, making high-range (+/–10%) adjustments less precise. A ±8% range is recommended.
-  Knobs and sliders may need to be moved after Mixxx startup to synchronize hardware and software positions.

Compatibility
-------------

-  Works on Windows, macOS, and Linux.
-  USB Audio Class compliant (no driver required on macOS or Linux).
-  Tested with Mixxx 2.5, 2.6 and later.

Credits
-------

- 2010 - `Matteo <https://mixxx.discourse.group/u/matteo>`__, :ref:`Numark Mixtrack <numark-mixtrack>` Mapping Script Functions
- 2011 - James Ralston
- 2011 - `Darío José Freije <https://www.dariofreije.com/>`__
.. codespell:ignore Patten
- 2024 - `Josh Patten <https://github.com/joshpatten>`__ with `PR 12948 <https://github.com/mixxxdj/mixxx/pull/12948>`__
- 2025 - `Vespadj <https://mixxx.discourse.group/u/vespadj>`__
