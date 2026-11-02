.. _hercules-djcontrol-mix-ultra:

Hercules DJControl Mix Ultra
============================

.. sectionauthor::
   Aayush Kapoor <xeoneux@gmail.com>

- `Manufacturer’s product page <https://www.hercules.com/en-us/product/djcontrol-mix-ultra/>`__
- `Manufacturer’s support and downloads page <https://support.hercules.com/en/product/djcontrolmixultra-en/>`__
- `Controller Mapping Forum <https://mixxx.discourse.group/c/controller-mappings/10>`__

.. versionadded:: 2.5.0

Compatibility
-------------

The Hercules DJControl Mix Ultra is a USB MIDI class-compliant device (USB VID:PID ``06F8:B131``) and also supports Bluetooth LE MIDI.
It works out of the box on GNU/Linux, macOS, and Windows via USB without requiring proprietary drivers.

.. note::
   On GNU/Linux and Windows, connecting via USB is strongly recommended for lowest latency and plug-and-play operation. Bluetooth LE MIDI connections require an OS-level BLE-MIDI bridge daemon on Linux (e.g. PipeWire BLE-MIDI or bluez-alsa) or third-party BLE-MIDI utilities on Windows.

Sound Card Setup
----------------

The DJControl Mix Ultra is a dedicated MIDI control surface and **does not include an integrated audio interface**.

To preview tracks in your headphones and output the master mix:

- Use your computer's built-in sound card with a DJ splitter cable, or
- Use a dedicated multi-channel external USB audio interface.

.. seealso::
   The :ref:`example setups section <setup-laptop-and-external-card>` provides complete walkthroughs for configuring master and headphone audio outputs in Mixxx.

Mapping description
-------------------

Mixer
~~~~~

===============================================================  ==============================================================
Control                                                          Function
===============================================================  ==============================================================
:hwlabel:`Crossfader`                                            Fades audio between Deck 1 and Deck 2.
:hwlabel:`MASTER` knob                                           Controls the main output volume.
:hwlabel:`Volume` faders                                         Controls channel volume for Deck 1 and Deck 2.
:hwlabel:`FILTER` knob                                           Dedicated bipolar Low-Pass / High-Pass filter per deck (center = off).
:hwlabel:`HIGH` EQ knob                                          Controls treble frequencies for the deck.
:hwlabel:`MID` EQ knob                                           Controls middle frequencies for the deck.
:hwlabel:`LOW` EQ knob                                           Controls bass frequencies for the deck.
:hwlabel:`SHIFT` + :hwlabel:`HIGH` EQ                            Adjusts track pre-gain (:hwlabel:`Gain`) for the deck.
:hwlabel:`Headphone` (:hwlabel:`PFL`) buttons                    Toggles headphone cue / PFL for the deck.
:hwlabel:`SHIFT` + :hwlabel:`PFL` (Deck A)                       Toggles Headphone Master Cue (:hwlabel:`CUE MASTER`).
:hwlabel:`SHIFT` + :hwlabel:`PFL` (Deck B)                       Toggles Headphone Split Cue (:hwlabel:`SPLIT`).
:hwlabel:`ASSISTANT` (Center button)                             Toggles **AutoDJ** on/off (button LED illuminates when active).
===============================================================  ==============================================================

Browser
~~~~~~~

===============================================================  ==============================================================
Control                                                          Function
===============================================================  ==============================================================
:hwlabel:`BROWSER` knob (turn)                                   Scrolls vertically through tracks or the library tree.
:hwlabel:`BROWSER` knob (press)                                  Toggles focus between library tree, track list, and search bar.
:hwlabel:`SHIFT` + :hwlabel:`BROWSER` knob (turn)                Scrolls horizontally through the library tree (expands / collapses folders).
:hwlabel:`SHIFT` + :hwlabel:`BROWSER` knob (press)               Toggles maximized library view full-screen.
:hwlabel:`LOAD` button (Deck A / B)                              Loads the currently selected track into the deck.
:hwlabel:`LOAD` (double-press)                                   **Instant Doubles**: Clones the playing track from the opposite deck (if enabled in Preferences → Decks).
===============================================================  ==============================================================

Decks
~~~~~

===============================================================  ==============================================================
Control                                                          Function
===============================================================  ==============================================================
:hwlabel:`PLAY/PAUSE` button                                     Play or pause playback.
:hwlabel:`SHIFT` + :hwlabel:`PLAY/PAUSE`                         Cue Stutter.
:hwlabel:`CUE` button                                            Sets or returns to the temporary cue point.
:hwlabel:`SHIFT` + :hwlabel:`CUE`                                Returns to the start of the track.
:hwlabel:`SYNC` button                                           Enables :ref:`Sync Lock <sync-lock>`.
:hwlabel:`SHIFT` + :hwlabel:`SYNC`                               Sets deck as Sync leader.
:hwlabel:`VINYL` button                                          Toggles scratch mode on/off (default: on).
:hwlabel:`PITCH` fader                                           14-bit high-resolution tempo / pitch slider with soft-takeover.
Jog Wheel (top surface touch + rotate)                           Scratches the track when Vinyl mode is active.
Jog Wheel (outer ring)                                           Pitch bends the track (temporarily speeds up or slows down).
:hwlabel:`SHIFT` + Jog Wheel                                     Fast seek / scrub through the track.
===============================================================  ==============================================================

.. note::
   On unpatched stock firmware, the outer jog ring emits MIDI packets only above a slight rotational speed threshold (~1 revolution per 6 seconds). The top wheel surface and :hwlabel:`SHIFT` + ring combinations work at any crawl speed.

Performance Pads
~~~~~~~~~~~~~~~~

The DJControl Mix Ultra features 4 hardware pad mode buttons (:hwlabel:`HOTCUE`, :hwlabel:`LOOP`, :hwlabel:`FX`, :hwlabel:`SAMPLER`) and 8 performance pads per deck.

Hot Cue Mode
^^^^^^^^^^^^

Engaged by pressing the :hwlabel:`HOTCUE` mode button.

===============================================================  ==============================================================
Control                                                          Function
===============================================================  ==============================================================
Pad :hwlabel:`1` - :hwlabel:`8`                                  Set or trigger :term:`hotcue` 1 - 8.
:hwlabel:`SHIFT` + Pad :hwlabel:`1` - :hwlabel:`8`               Delete :term:`hotcue` 1 - 8.
===============================================================  ==============================================================

Loop Mode
^^^^^^^^^

Engaged by pressing the :hwlabel:`LOOP` mode button.

===============================================================  ==============================================================
Control                                                          Function
===============================================================  ==============================================================
Pad :hwlabel:`1`                                                 Toggle 1/2 beat loop.
Pad :hwlabel:`2`                                                 Toggle 1 beat loop.
Pad :hwlabel:`3`                                                 Toggle 2 beats loop.
Pad :hwlabel:`4`                                                 Toggle 4 beats loop.
Pad :hwlabel:`5`                                                 Toggle 8 beats loop.
Pad :hwlabel:`6`                                                 Toggle 16 beats loop.
Pad :hwlabel:`7`                                                 Loop In.
Pad :hwlabel:`8`                                                 Loop Out.
:hwlabel:`SHIFT` + Pad :hwlabel:`7`                              Loop Halve.
:hwlabel:`SHIFT` + Pad :hwlabel:`8`                              Loop Double.
===============================================================  ==============================================================

FX Mode
^^^^^^^

Engaged by pressing the :hwlabel:`FX` mode button.

===============================================================  ==============================================================
Control                                                          Function
===============================================================  ==============================================================
Pad :hwlabel:`1` - :hwlabel:`3`                                  Toggle Effect 1 - 3 on the deck's effect unit.
Pad :hwlabel:`4`                                                 Toggle effect unit routing for the channel.
Pad :hwlabel:`5` - :hwlabel:`7`                                  Cycle to next effect in slot 1 - 3.
Pad :hwlabel:`8`                                                 Toggle effect unit mix mode.
:hwlabel:`SHIFT` + Pad :hwlabel:`1` - :hwlabel:`3`               Cycle to previous effect in slot 1 - 3.
:hwlabel:`SHIFT` + Pad :hwlabel:`4`                              Toggle effect unit routing for the opposite deck.
===============================================================  ==============================================================

.. note::
   The effects can be applied in two ways:

   * Permanent: Press the pad to turn the effect on, press again to turn off.
   * Momentary: Press and hold the pad; the effect will remain active until the pad is released.

Sampler Mode
^^^^^^^^^^^^

Engaged by pressing the :hwlabel:`SAMPLER` mode button.

===============================================================  ==============================================================
Control                                                          Function
===============================================================  ==============================================================
Pad :hwlabel:`1` - :hwlabel:`8` (Deck A)                         Play Sampler 1 - 8 (:hwlabel:`SHIFT`: Stop / Eject).
Pad :hwlabel:`1` - :hwlabel:`8` (Deck B)                         Play Sampler 9 - 16 (:hwlabel:`SHIFT`: Stop / Eject).
===============================================================  ==============================================================
