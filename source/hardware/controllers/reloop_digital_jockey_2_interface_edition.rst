.. _reloop_digital_jockey_2_interface_edition:

Reloop Digital Jockey 2 Interface Edition
=========================================

The *Reloop Digital Jockey 2 Interface Edition* is a 2 deck USB MIDI controller designed to work with Traktor software. Compared to *Controller Edition* the *Interface Edition* is additionally equipped with a high quality 4-channel USB audio interface and touch-sensitive jog wheels. The microphone input is available to the computer for recording and broadcasting. The controller can be powered only from the USB bus, however the included external power supply can serve as the power source too. Using a separate power supply has no impact on the output level or LED brightness.

-  `Manufacturer’s product page <https://www.reloop.com/reloop-digital-jockey-2-ie>`__
-  `Forum thread <https://mixxx.discourse.group/t/reloop-digital-jockey-2-mapping-by-dj-ak/23971>`__

.. versionadded:: 2.3

Compatibility
-------------

The mapping for *Reloop Digital Jockey 2 Interface Edition* has originally been developed under Debian 8 Jessie with *Mixxx v2.1*. Lately the mapping has been moved to *Mixxx v2.3* and tested under Kubuntu 20.04. No special device drivers are required for GNU/Linux systems.

Windows build has not been tested.

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

Although the mapping provided to Traktor users by the manufacturer has a feature of extending the controller to handle 4 decks using a :hwlabel:`SHIFT` button, this particular mapping handles the basic 2 decks setup. :hwlabel:`SHIFT` button has been mapped, however it handles the rest of the functionality.

Jog Wheels
^^^^^^^^^^

Jog modes work as described in the following table:

.. table::
    :widths: 70

    ================== =============
    Jog mode           Description
    ================== =============
    *Pitch bending*    By default the jogs work in this mode. In contrast to the manufacturer mapping, you do not have to press :hwlabel:`SEARCH` and :hwlabel:`SCRATCH` buttons to enable this mode. This is more convenient.
    *Scratch*          The mode is enabled by pressing :hwlabel:`SCRATCH`
    *Search*           The mode is enabled by pressing :hwlabel:`SEARCH`
    *Library search*   This is an **extra mode** that has been introduced by this mapping. This mode is enabled by pressing **any of the two** :hwlabel:`SHIFT` buttons and is indicated by flashing all jog wheel mode LEDs. While in this mode, turn **any** jog to browse the library. This is also an enhancement to the manufacturer's mapping.
    ================== =============
