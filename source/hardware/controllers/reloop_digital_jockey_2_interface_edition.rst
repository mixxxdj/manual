.. _reloop_digital_jockey_2_interface_edition:

Reloop Digital Jockey 2 Interface Edition
=========================================

The *Reloop Digital Jockey 2 Interface Edition* is a 2 deck USB MIDI controller designed to work with Traktor software. Compared to *Controller Edition* the *Interface Edition* is additionally equipped with a high quality 4-channel USB audio interface and touch-sensitive jog wheels. The microphone input is available to the computer for recording and broadcasting. The controller can be powered only from the USB bus, however the included external power supply can serve as the power source too. Using a separate power supply has no impact on the output level or LED brightness.

-  `Manufacturer’s product page <https://www.reloop.com/reloop-digital-jockey-2-ie>`__
-  `Forum thread <https://mixxx.discourse.group/t/reloop-digital-jockey-2-mapping-by-dj-ak/23971>`__

.. versionadded:: 2.3

Compatibility
-------------

The device should work out of the box on Windows, macOS and GNU/Linux.
For Windows, Reloop offers an ASIO driver on the product page linked above.

Mixxx Sound Hardware Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. table::
    :widths: 100 100

    ========================  =======================
    Output                    Channels
    ========================  =======================
    :guilabel:`Master`        Channel 1 - 2
    :guilabel:`Headphones`    Channel 3 - 4
    ========================  =======================

Mapping
-------

The mapping is straightforward and follows the layout of the controller. The deviations are documented below.

Decks
~~~~~

This mapping handles 2 decks setup.

.. note::
  Pressing :hwlabel:`SHIFT` does not enable decks C and D control.

CUP button
^^^^^^^^^^

- :hwlabel:`CUP` is mapped to :mixxx:coref:`[ChannelN],cue_play` (usual CUP button behavior)
- :hwlabel:`SHIFT` + :hwlabel:`CUP`  is mapped to :mixxx:coref:`[ChannelN],cue_gotoandplay`

Jog Wheels
^^^^^^^^^^

Jog modes work as described in the following table:

.. table::
    :widths: 70

    ================== =============
    Jog mode           Description
    ================== =============
    *Pitch bending*    Turn the wheel to temporarily increase or decrease the speed. This is the default mode while :hwlabel:`SEARCH` and :hwlabel:`SCRATCH` buttons are disabled.
    *Scratch*          Touch the top of the wheel and turn to scratch. This mode is enabled by pressing :hwlabel:`SCRATCH`.
    *Search*           Turn the wheel to quickly move through the track. This mode is enabled by pressing :hwlabel:`SEARCH`.
    *FX dry/wet*       Turn the wheel for smooth control of the FX unit's dry/wet parameter. This mode is enabled by pressing :hwlabel:`FX DRY/WET`.
    *Library search*   Turn the wheel to quickly browse the tracks table or folder tree. This **extra mode** is enabled by pressing any of the two :hwlabel:`SHIFT` buttons and is indicated by flashing all jog mode LEDs.
    ================== =============

Library
~~~~~~~

The library can be controlled as follows:

- pressing :hwlabel:`TRAX` toggles maximized view of the library
- pressing :hwlabel:`SHIFT` + :hwlabel:`TRAX` moves focus between the sidebar and tracks table (equivalent to pressing :hwlabel:`TAB` key on the keyboard)
- turning the :hwlabel:`TRAX` knob changes currently selected item
- turning the :hwlabel:`TRAX` knob with :hwlabel:`SHIFT` scrolls the items (equivalent to :hwlabel:`PageUp`/:hwlabel:`PageDown` on keyboard)
- pressing :hwlabel:`SHIFT` + any of the four pitch bend buttons (:hwlabel:`CLOSE/OPEN FOLDER` label) invokes action for :mixxx:coref:`[Library],GoToItem`
- turning any jog wheel with :hwlabel:`SHIFT` enables smooth and fast browsing (see `Jog Wheels`_)


FX Controls
~~~~~~~~~~~

This mapping uses the `Standard Effects Mapping <https://github.com/mixxxdj/mixxx/wiki/Standard-Effects-Mapping>`__ to control the FX units.

Quick Effects
^^^^^^^^^^^^^

The :hwlabel:`FILTER` knob (:hwlabel:`SHIFT` + :hwlabel:`HIGH` knob) is mapped to *Quick Effect*.

- pressing :hwlabel:`SHIFT` + :hwlabel:`HIGH` knob toggles *Quick Effect* (enable/disable)
- turning :hwlabel:`HIGH` knob with :hwlabel:`SHIFT` moves the metaknobs for the *Quick Effect*

.. note::
  *Key* and *Pan* effects are not mapped.
