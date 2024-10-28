Stanton DJC.4
=============

-  `Manufacturer’s product page <https://web.archive.org/web/20220909115203/https://www.stantondj.com/stanton-controllers-systems/djc4.html>`__
-  `Manual / Midi commands <https://web.archive.org/web/20211008132713/https://www.stantondj.com/pdf/products/controllers/djc4/DJC.4ManualV1.1.pdf>`__
-  `Forum thread <https://mixxx.discourse.group/t/mapping-for-stanton-djc-4/14074>`__

.. versionadded:: 2.2.4

Compatibility
-------------

This controller is a class compliant USB MIDI and audio device, so it can be used without any special drivers on GNU/Linux, Mac OS X, and Windows.
However, if you wish to use the :ref:`ASIO sound API <preferences-sound-api>` under Windows, please install the latest driver package available from the `Product page <https://web.archive.org/web/20220909115203/https://www.stantondj.com/stanton-controllers-systems/djc4.html>`__.

Sound card setup
----------------

This controller has a built-in 4 channel sound card, with MASTER output (RCA and balanced 6.3 mm TRS) and HEADPHONE output (6.3 and 3.5mm jack).

=============== ========================
Output Channels Assign to
=============== ========================
1-2             Main
3-4             Headphones
=============== ========================

=============== ========================
Input Channels  Assign to
=============== ========================
1-2 (Input 1)   Vinyl Control 1 or Aux 1
3-4 (Input 2)   Vinyl Control 2 or Aux 2
=============== ========================

Above the **Gain** knobs are switches to select which input should be sent to the PC. For input 1 this can be Aux (3.5 mm TRS) or Line/Phono 1/2 (RCA) and for input 2 this can be microphone (6.3 mm
TRS on front) or Line/Phono 3/4 (RCA).

Input 1 routing
^^^^^^^^^^^^^^^

On the rear side is a small switch to select if Input 1 is routed to the PC or directly to the main output (through). It is therefore possible to include the microphone into a recording/stream or to
exclude it.

.. seealso::
   The :ref:`example setups section <setup-laptop-and-external-card>` provides more details about the audio configuration in Mixxx.

Hardware controls
^^^^^^^^^^^^^^^^^

The **Master** and **Mic Level** are hardware controls and interact directly with the integrated sound card and are not mapped to Mixxx.

.. seealso::
   The :ref:`gain staging documentation <djing-gain-staging>` explains how to set your levels properly when using Mixxx.

Mapping description
-------------------

The knobs for :hwlabel:`MASTER LEVEL`, :hwlabel:`MIC LEVEL` and the :hwlabel:`MIC ON/OFF` switch are controlling the hardware mixer of the built-in audio interface.
Hence, turning the knobs will not change values in the Mixxx :term:`GUI` and you’ll need to set the Mixxx knobs to their default values when using the controller.

Controls
^^^^^^^^

Center section
~~~~~~~~~~~~~~

========================  ======================================================  ===========================================================================================
No.                       Control                                                 Function
========================  ======================================================  ===========================================================================================
1                         :hwlabel:`SAMPLER VOLUME` knob                          Change the volume of all eight samplers at the same time. If the SAMPLER VOLUME is at zero hide the sampler bank.
2                         :hwlabel:`BROWSER` Rotary encoder                       Turn to move tracklist/sidebar cursor up/down. Press to toggle between sidebar and tracklist.
2                         :hwlabel:`SHIFT` + :hwlabel:`BROWSER` Rotary encoder    Turn to move tracklist/sidebar cursor page wise up/down. Press to (Un-)Maximizes the library view.
3                         :hwlabel:`LOAD` buttons                                 Load song into active deck (Depending on Deck select).
3                         :hwlabel:`SHIFT` + :hwlabel:`LOAD` buttons              Open/close a tree view. Equivalent to pressing the LEFT/RIGHT key on the keyboard
5                         :hwlabel:`SHIFT` + :hwlabel:` L SCRATCH` button         Conxtextaul Go To item  - see https://manual.mixxx.org/2.3/en/chapters/appendix/                                                                                                                                                mixxx_controls.html#control-[Library]-GoToItem
========================  ======================================================  ===========================================================================================

Mixer section
~~~~~~~~~~~~~

========================  ======================================================  ===========================================================================================
No.                       Control                                                 Function
========================  ======================================================  ===========================================================================================
1                         :hwlabel:`GAIN` knobs                                   Adjust the deck gain (prefader)
2                         :hwlabel:`HI`, :hwlabel:`MID`, :hwlabel:`LOW` knobs     Adjust the high/mid/low-frequency regions of the song. Press to kill this frequency region.
3                         :hwlabel:`SHIFT` + :hwlabel:`LOW` knob                  QuickEffect superknob (filter by default). Press to (de-)activate QuickEffect.
4                         Channel :hwlabel:`CUE` buttons                          Toggle PFL for each channel.
5                         Channel faders                                          Adjust the output level for each channel.
6                         Cross fader                                             Fades between left and right deck.
7                         Level indicator                                         Indicate the output level of main.
8                         :hwlabel:`CROSSFADER CURVE` (front side of controller)  Adjust crossfader curve between fade and cut.
9                         :hwlabel:`HEADPHONES MIX` (front side of controller)    Adjusts the cue/main mix in the headphone output.
10                        :hwlabel:`HEADPHONES LEVEL` (front side of controller)  Adjusts the headphone output gain.
========================  ======================================================  ===========================================================================================

Deck section
~~~~~~~~~~~~

========================  ======================================================  ===========================================================================================
No.                       Control                                                 Function
========================  ======================================================  ===========================================================================================
1                         Jog dial (top surface)                                  Perform scratch operation if Scratch is enabled.
1                         Jog dial (outer edge)                                   Rotate to lower/raise playback speed if Scratch is enabled (and pitch if key lock is off).
1                         :hwlabel:`SHIFT` + Jog dial (top surface)               Search fast through the playback location.
2                         :hwlabel:`SCRATCH` button                               En-/Disable scratch function
3                         :hwlabel:`SHIFT` button                                 Hold down to access other functions.
4                         :hwlabel:`SYNC` button                                  Match tempo and phase of other deck.
4                         :hwlabel:`SHIFT` + :hwlabel:`SYNC` button               Plays the track reverse as long as pressed.
4                         :hwlabel:`TAP` button (tap repeatedly)                  Set tempo by tapping on each beat.
5                         :hwlabel:`CUE` button                                   Specifies, plays or recalls temporary cue point.
5                         :hwlabel:`SHIFT` + :hwlabel:`CUE` button                Jumps to the cue point and stops.
6                         :hwlabel:`PLAY/PAUSE` button                            Plays or pause the song.
11                        :hwlabel:`DECK` select buttons                          Switches the deck (left: decks 1 and 3, right: decks 2 and 4)
12                        :hwlabel:`KEY` LOCK                                     Toggle key lock.
12                        :hwlabel:`SHIFT` + :hwlabel:`KEY LOCK`                  Toggle beats quantization.
13                        Tempo slider                                            Adjust song playback speed (and pitch if key lock if off).
14                        :hwlabel:`PITCH BEND +`                                 Holds the speed one step (4 % default) higher while pushed.
15                        :hwlabel:`PITCH BEND -`                                 Holds the speed one step (4 % default) lower while pushed.
14, 15                    :hwlabel:`SHIFT` + :hwlabel:`PITCH BEND`                *Not mapped.*
16                        :hwlabel:`HOT CUE`                                      Set (if empty) or Play Hot Cue Point.
16                        :hwlabel:`SHIFT` + :hwlabel:`HOT CUE`                   Unset/Delete Hot Cue Point
========================  ======================================================  ===========================================================================================

Loop section
~~~~~~~~~~~~

========================  ======================================================  ===========================================================================================
No.                       Control                                                 Function
========================  ======================================================  ===========================================================================================
1                         :hwlabel:`IN`                                           If loop is disabled, sets the player loop in position to the current play position. If loop is enabled, press and hold to move loop in position to the current play position.
1                         SHIFT + IN                                              Seek to the loop in point.
2                         :hwlabel:`OUT`                                          If loop is disabled, sets the player loop out position to the current play position. If loop is enabled, press and hold to move loop out position to the current play position.
2                         SHIFT + OUT                                             Seek to the loop out point.
3                         :hwlabel:`ON`                                           Toggles the current loop on or off. If the loop is ahead of the current play position, the track will keep playing normally until it reaches the loop.
3                         SHIFT + ON                                              Activate current loop, jump to its loop in point, and stop playback.
4                         :hwlabel:`DELETE`                                       Not mapped.
5                         LOOP LENGTH /                                           Halves beatloop size.
6                         LOOP LENGTH X                                           Doubles beatloop size.
7                         BEAT MULTIPLIER encoder                                 Turn to move the loop left or right by 1 beat per click.
7                         BEAT MULTIPLIER button                                  Sets a loop using the current beatloop size long and enable the loop.
7                         SHIFT + BEAT MULTIPLIER button                          Activates a rolling loop using the current beatloop size.
========================  ======================================================  ===========================================================================================

Sampler section
~~~~~~~~~~~~~~~

========================  ======================================================  ===========================================================================================
No.                       Control                                                 Function
========================  ======================================================  ===========================================================================================
1                         :hwlabel:`SAMPLER 1-4` (left deck)                      Controls Samplers 1-4 (independent of deck selection)
2                         :hwlabel:`SAMPLER 1-4` (right deck)                     Controls Samplers 5-8 (independent of deck selection)
========================  ======================================================  ===========================================================================================


Effect section
~~~~~~~~~~~~~~

========================  ======================================================  ===========================================================================================
No.                       Control                                                 Function
========================  ======================================================  ===========================================================================================
1                         :hwlabel:`ON`                                           Toggle FX 1 for decks 1/3 (both on the left) and FX 2 for decks 2/4 (both on the right).
2-5                       *Various*                                               See :ref:`Standard Effects Mapping <controller-effects-mapping>`.
========================  ======================================================  ===========================================================================================

Tweakables
^^^^^^^^^^

At the top of the file file:`Stanton-DJC-4-scripts.js` there are a few customizable options to change the default mapping.

=====================  ==========================================================================================  =========
Variable               Function                                                                                    Default
=====================  ==========================================================================================  =========
``autoShowFourDecks``  If a track gets loaded into deck 3 or 4, automatically show four decks in Mixxx             ``false``
``showMasterVu``       If set to false, show channel VU meter instead of Main L/R                                  ``true``
``dryWetAdjustValue``  Amount the dryWetKnob changes the value for each increment                                  0.05
=====================  ==========================================================================================  =========

Known Issues
^^^^^^^^^^^^

The following controls are currently not mapped:

-  Loop Delete button (no matching function in Mixxx)
-  X-Fader Link button
-  Smart Fade button
-  Smart button (Shift + Scratch)
-  Video button (Shift + Smart Fade)
-  FX Ctrl 1/2 fader (Shift + Channel fader)
-  TX/FX Select rotary encoder
-  TX/FX Action rotary encoder button
