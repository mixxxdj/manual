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

Although the mapping provided to Traktor users by the manufacturer has a feature of extending the controller to handle 4 decks using a :hwlabel:`SHIFT` button, this particular mapping handles the basic 2 decks setup. :hwlabel:`SHIFT` button has been mapped, however it handles the rest of the functionality.

Jog Wheels
^^^^^^^^^^

Jog modes work as described in the following table:

.. table::
    :widths: 70

    ================== =============
    Jog mode           Description
    ================== =============
    *Pitch bending*    Turn the wheel to temporarily increase or decrease the speed. This is the default mode while :hwlabel:`SEARCH` and :hwlabel:`SCRATCH` buttons are disabled.
    *Scratch*          Touch the top of the wheel and turn to scratch. This mode is enabled by pressing :hwlabel:`SCRATCH`
    *Search*           Turn the wheel to quickly move through the track. This mode is enabled by pressing :hwlabel:`SEARCH`
    *Library search*   Turn the wheel to quickly browse the tracks table. This **extra mode** is enabled by pressing **any of the two** :hwlabel:`SHIFT` buttons and is indicated by flashing all jog wheel mode LEDs.
    ================== =============
