Hercules DJControl Inpulse 300
==============================

-  `Manufacturer’s product page <https://web.archive.org/web/20220316132957/https://www.hercules.com/en-us/product/djcontrolinpulse300/>`__
-  `Manufacturer’s support and downloads page <https://support.hercules.com/en/product/djcontrolinpulse300-en//>`__
-  `Forum thread <https://mixxx.discourse.group/t/hercules-djcontrol-inpulse-300/17854/>`__

.. versionadded:: 2.2.4

Compatibility
-------------

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows. However, if you wish to use the :ref:`ASIO sound API <preferences-sound-api>`
under Windows, please install the latest driver package available from
the `Support
page <https://support.hercules.com/en/product/djcontrolinpulse300-en//>`__.

.. note::
   Firmware upgrade (v1.72) is required for pads to work correctly in **FX Mode**.

   When using **Firmware v1.68** and earlier, pads in FX Mode will not work as expected.

   For more details about `upgrading the
   Firmware. <https://web.archive.org/web/20250329173925/https://www.djuced.com/change-your-pad-fx-on-hercules-djcontrol-inpulse-firmware-update-guide/>`__

Sound card setup
----------------

This controller has built-in 4 channel output sound card, with MAIN
output (RCA) and HEADPHONE output (3.5mm jack).

-  Open **Preferences > Sound Hardware**
-  Select the **Output** tab
-  From the **Main** drop-down menu, select the audio interface, then
   **Channels 1-2**
-  From the **Headphones** drop-down menu, select the audio interface,
   then **Channels 3-4**
-  Click **Apply** to save the changes.

.. seealso::
   The :ref:`example setups section <setup-laptop-and-external-card>` provides more details about the audio configuration in Mixxx.

.. note::
   The **Master** and **Headphone** knobs, as well as the
   **Master** button are hardware controls and interact directly with the
   integrated sound card’s output. Although they also send MIDI messages,
   they have NOT been mapped in Mixxx, so do not expect an on-screen
   reaction when using them. This was done to prevent the knobs to adjust
   both the gain on the controller’s sound card and in Mixxx.

Mapping description
-------------------

Decks
~~~~~

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`SYNC` button                                           Toggle :ref:`Sync Lock <sync-lock>`.
:hwlabel:`SHIFT` + :hwlabel:`SYNC` button                        Set deck as Sync leader.
:hwlabel:`CUE` button                                            Specifies, plays or recalls temporary cue point.
:hwlabel:`SHIFT` + :hwlabel:`CUE` button                         Return to the beginning of the track.
Play button                                                      Play/Pause the current track.
:hwlabel:`SHIFT` + Play button                                   Cue Stutter.
:hwlabel:`VINYL` button                                          Toggle scratch mode (default: on)
Loop :hwlabel:`IN` button                                        Enable Beatloop 4 beats.
:hwlabel:`SHIFT` + Loop :hwlabel:`IN` button                     Halve the current loop size.
Loop :hwlabel:`OUT` button                                       Disable Beatloop.
:hwlabel:`SHIFT` + Loop :hwlabel:`OUT` button                    Double the current loop size.
:hwlabel:`BEATMATCH GUIDE`                                       Toggles beatmatch guide LEDs.
:hwlabel:`SLIP`                                                  Toggles splip mode.
:hwlabel:`Q`                                                     Toggles quantize.
:hwlabel:`SHIFT` + :hwlabel:`Q`                                  Adjusts beatgrid so closest beat is aligned with the current playposition.
===============================================================  ==========================================

Browser
~~~~~~~

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`BROWSER` encoder (turn)                                Move up/down list.
:hwlabel:`SHIFT` + :hwlabel:`BROWSER` encoder (turn)             Move left/right (fold/unfold) list.
:hwlabel:`BROWSER` encoder (press)                               Switch focus between list and file view.
:hwlabel:`SHIFT` + Encoder (press)                               Maximize/Minimize library view.
:hwlabel:`ASSISTANT` button                                      Toggle AutoDJ (be sure a playlist was created for AutoDJ before activating this function).
===============================================================  ==========================================

FX
~~
===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`ON` pad                                                Toggle FX 3 on/off.
:hwlabel:`SHIFT` + :hwlabel:`ON` pad (select)                    Cycle to the next effect after the currently loaded effect.
===============================================================  ==========================================

Performance Pads
~~~~~~~~~~~~~~~~

Hot Cue Mode
^^^^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1 - 8                                                        Set and trigger :term:`hotcue` 1 - 8
:hwlabel:`SHIFT` + Pad 1 - 8                                     Delete :term:`hotcue` 1 - 8.
===============================================================  ==========================================

Toneplay Mode
^^^^^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1                                                            Jump to the last used hot cue (or cue point if no hotcue is set) and play at original pitch.
Pad 2                                                            Jump to the last used hot cue/cue point and play at +1 semitones.
Pad 3                                                            Jump to the last used hot cue/cue point and play at +2 semitones.
Pad 4                                                            Jump to the last used hot cue/cue point and play at +3 semitones.
Pad 5                                                            Jump to the last used hot cue/cue point and play at -4 semitones.
Pad 6                                                            Jump to the last used hot cue/cue point and play at -3 semitones.
Pad 7                                                            Jump to the last used hot cue/cue point and play at -2 semitones.
Pad 8                                                            Jump to the last used hot cue/cue point and play at -1 semitones.
:hwlabel:`SHIFT` + Pad 1                                         Change the pitch to the original pitch (without jumping).
:hwlabel:`SHIFT` + Pad 2                                         Change the pitch to +1 semitones.
:hwlabel:`SHIFT` + Pad 3                                         Change the pitch to +2 semitones.
:hwlabel:`SHIFT` + Pad 4                                         Change the pitch to +3 semitones.
:hwlabel:`SHIFT` + Pad 5                                         Change the pitch to -4 semitones.
:hwlabel:`SHIFT` + Pad 6                                         Change the pitch to -3 semitones.
:hwlabel:`SHIFT` + Pad 7                                         Change the pitch to -2 semitones.
:hwlabel:`SHIFT` + Pad 8                                         Change the pitch to -1 semitones.
===============================================================  ==========================================

Roll Mode
^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1                                                            Activate Beatloop of 1/8 beat size.
Pad 2                                                            Activate Beatloop of 1/4 beat size.
Pad 3                                                            Activate Beatloop of 1/2 beat size.
Pad 4                                                            Activate Beatloop of 1 beat size.
Pad 5                                                            Activate Beatloop of 2 beat size.
Pad 6                                                            Activate Beatloop of 4 beat size.
Pad 7                                                            Activate Beatloop of 8 beat size.
Pad 8                                                            Activate Beatloop of 16 beat size.
===============================================================  ==========================================

FX Mode
^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1 - 3                                                        Toggle Effect 1 - 3.
Pad 5 - 7                                                        Cycle to the next effect for Effect 1 - 3.
Pad 4                                                            Toggle Effect Unit 1.
Pad 8                                                            Toggle Effect Unit 2.
:hwlabel:`Shift` + Pad 1 - 3                                     Toggle Effect 1 - 3. (Effect Unit 3 / 4 for deck A / B)
:hwlabel:`Shift` + Pad 5 - 7                                     Cycle to the next effect for Effect 1 - 3 (Effect Unit 3 / 4 for deck A / B).
:hwlabel:`Shift` + Pad 4                                         Toggle Effect Unit 3.
:hwlabel:`Shift` + Pad 8                                         Toggle Effect Unit 4.
===============================================================  ==========================================

Sampler Mode
^^^^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1 - 8 (deck A)                                               Trigger Sampler 1 - 8.
Pad 1 - 8 (deck B)                                               Trigger Sampler 9 - 16.
:hwlabel:`SHIFT` + Pad 1 - 8 (deck A)                            Stop Sampler 1 - 8.
:hwlabel:`SHIFT` + Pad 1 - 8 (deck B)                            Stop Sampler 9 - 16.
===============================================================  ==========================================

Beatjump Mode
^^^^^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1 - 2                                                        Jump backward/forward by 1 beat.
Pad 3 - 4                                                        Jump backward/forward by 2 beats.
Pad 5 - 6                                                        Jump backward/forward by 4 beats.
Pad 7 - 8                                                        Jump backward/forward by 8 beats.
===============================================================  ==========================================

Slicer/Slicer Loop Mode
^^^^^^^^^^^^^^^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Slicer                                                           Create a slicer section (overrides active loops). Removes the slicer section if one is already active.
:hwlabel:`SHIFT` + Slicer                                        Create a looped slicer section (overrides active loops). Removes the slicer section if one is already active.
Pad 1 - 8                                                        Create a loop on slicer section 1-8.
Loop :hwlabel:`IN` button                                        Enable Beatloop 4 beats (overrides active slicers).
:hwlabel:`SHIFT` + Loop :hwlabel:`IN` button                     Halve the slicer section size.
Loop :hwlabel:`OUT` button                                       Disable Beatloop or slicer section.
:hwlabel:`SHIFT` + Loop :hwlabel:`OUT` button                    Double the slicer section size.
===============================================================  ==========================================

Pressing Slicer or Slicer Loop creates a slicer section (indicated by loop markers). The length of the slicer section is dependent on loop size in the spinbox.
Pressing Slicer, Slicer Loop, or Loop Out will remove the slicer section.

The slicer section is cut into 8 equal slices. Pressing pad 1-8 will create a loop on slice 1-8. For example, if a slicer section of 8 beats is created, then each slice will be 1 beat long.
Pressing pad 1 will create a 1-beat loop on the 1st slice (1st beat). Pad 2 will loop the 2nd slice, pad 3 will loop the 3rd beat, and so on.

Pressing two pads at the same time creates a loop between two slices. For example, pressing pads 3 and 6 creates a 4 beat loop that encompasses slices 3, 4, 5, and 6.
Pressing three or more pads will create a loop between the first and last slices. For example, pressing pads 2, 5, and 7 creates a 6 beat loop that encompasses slices 2-7.

In Slicer mode, the slicer section moves throughout the track. In Slicer Loop mode, the slicer section stays in place.

For more details, look at the original Inpulse 300 manual.

Known issues
------------
- The slicer section does not move backwards with the play indicator when scratching with the jogwheel.
- Slicer will not work properly if BPM is not constant.

Controls not included in this mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Master knob (Hardware control)
-  Headphone knob (Hardware control)
-  Master buttons (Hardware control)
