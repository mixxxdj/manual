Hercules DJControl MIX
==============================

-  `Manufacturer’s product page <https://www.hercules.com/en-us/product/djcontrol-mix/>`__
-  `Manufacturer’s support and downloads page <https://support.hercules.com/en/product/djcontrolmix-en/>`__
-  `Forum thread <https://mixxx.discourse.group/t/hercules-contrl-mix-mapping/26581>`__

.. versionadded:: 2.3

Compatibility
-------------

This controller is a class compliant USB MIDI, so it can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows.

.. note::
In order to use this mapping, the DJControl MIX must be physically connected to the computer through USB. It was not conceived to use the controller connected via Bluetooth.

Sound card setup
----------------

This device does not have a built in audio interface.

Please refer to :ref:`the user
manual <controllers-without-an-integrated-audio-interface>`for more details about the audio configuration in Mixxx.

Mapping description
-------------------

Decks
~~~~~

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`SYNC` button                                           Toggle :ref:`Sync Lock <master-sync>`.
:hwlabel:`SHIFT` + :hwlabel:`SYNC` button                        Set deck as Sync leader.
:hwlabel:`CUE` button                                            Specifies, plays or recalls temporary cue point.
:hwlabel:`SHIFT` + :hwlabel:`CUE` button                         Return to the beginning of the track.
Play button                                                      Play/Pause the current track.
:hwlabel:`SHIFT` + Play button                                   Cue Stutter.
:hwlabel:`VINYL` button                                          Toggle scratch mode (default: on)
:hwlabel:`TEMPO` 												 Controls pitch/tempo ratio
===============================================================  ==========================================

Mixer
~~~~~~~

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`Crossfader` 				                             Fades between deck 1 and 2
:hwlabel:`MASTER` 				                             	 Controls the master output volume
:hwlabel:`HEADPHONE` knob				                         Controls the headphone output volume
:hwlabel:`Headphone` buttons				                     Toggles PFL/Cue (headphones) for specific deck
:hwlabel:`SHIFT` + :hwlabel:`CUE MASTER`						 Toggles between headphone’s audio source (Cue / Master)
:hwlabel:`SHIFT` + :hwlabel:`SPLIT ON/OFF` 						 Toggles split cue (headphones)
:hwlabel:`Volume` 				                             	 Controls deck volume
:hwlabel:`Filter/Bass` knob				                         Controls deck’s filter/ equalizer low frequencies
:hwlabel:`Filter/Bass` button				                     Toggles knob control between Filter/Bass
===============================================================  ==========================================


Performance Pads
~~~~~~~~~~~~~~~~

Hot Cue Mode
^^^^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`Pad 1 - 4`                                             Set and trigger :term:`hotcue` 1 - 4
:hwlabel:`SHIFT` + :hwlabel: `Pad 1 - 4`                         Delete :term:`hotcue` 1 - 4.
===============================================================  ==========================================

Loop Mode
^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`Pad 1`                                                 Activate Beatloop of 1/2 beat size.
:hwlabel:`Pad 2`                                                 Activate Beatloop of 1 beat size.
:hwlabel:`Pad 3`                                                 Activate Beatloop of 2 beat size.
:hwlabel:`Pad 4`                                                 Activate Beatloop of 4 beat size.

===============================================================  ==========================================

FX Mode
^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`Pad 1 - 3`                                             Toggle Effect 1 - 3.
:hwlabel:`SHIFT` + :hwlabel: `Pad 1 - 3`						 Select Next available Effect
:hwlabel:`Pad 4` (Deck A)                                        Toggle Effect Unit 1.
:hwlabel:`Pad 4` (Deck B)                                        Toggle Effect Unit 2.
===============================================================  ==========================================

.. note::
The effects can be applied in two ways:
- Permanent = Press pad to turn effect On, press again to turn Off.
- Momentary = Press and Hold. The effect will be On until the pad is released.


Sampler Mode
^^^^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`Pad 1 - 4` (Deck A)                                    Trigger Sampler 1 - 4.
:hwlabel:`Pad 1 - 4` (Deck B)                                    Trigger Sampler 5 - 8.
===============================================================  ==========================================
