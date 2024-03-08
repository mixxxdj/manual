.. _hercules-djcontrol-inpulse-200:

Hercules DJControl Inpulse 200
==============================

-  `Manufacturer’s product page <https://web.archive.org/web/20220316132959/https://www.hercules.com/en-us/product/djcontrolinpulse200/>`__
-  `Manufacturer’s support and downloads page <https://support.hercules.com/en/product/djcontrolinpulse200-en//>`__
-  `Forum thread <https://mixxx.discourse.group/t/hercules-djcontrol-inpulse-200/17849>`__

.. versionadded:: 2.3.0

Compatibility
-------------

This controller is a class compliant USB MIDI and audio device, so it can be used without any special drivers on GNU/Linux, Mac OS X, and Windows. However, if you wish to use the `ASIO sound API <https://mixxx.org/manual/latest/chapters/preferences/sound_hardware.html?highlight=asio#windows>`__ under Windows, please install the latest driver package available from the `Support page <https://support.hercules.com/en/product/djcontrolinpulse200-en//>`__.

Sound Card Setup
----------------

This controller has built-in 4 channel output sound card, with :hwlabel:`MASTER` output (RCA) and :hwlabel:`HEADPHONE` output (3.5mm jack).

1. Open :guilabel:`Preferences > Sound Hardware`
2. Select the :guilabel:`Output` tab
3. From the :guilabel:`Main` drop-down menu, select the audio interface, then :guilabel:`Channels 1 - 2`
4. From the :guilabel:`Headphones` drop-down menu, select the audio interface, then :guilabel:`Channels 3 - 4`
5. Click :guilabel:`Apply` to save the changes.

.. seealso::
   The :ref:`example setups section <setup-laptop-and-external-card>` provides more details about the audio configuration in Mixxx.

.. note::
   The :hwlabel:`MASTER` and :hwlabel:`HEADPHONE` knobs, as well as the
   :hwlabel:`MASTER` button are hardware controls and interact directly with the
   integrated sound card’s output. Although they also send MIDI messages,
   they have NOT been mapped in Mixxx, so do not expect an on-screen
   reaction when using them. This was done to prevent the knobs to adjust
   both the gain on the controller’s sound card and in Mixxx.

Mapping description
-------------------

All controls not mentioned behave as labeled.

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
Loop :hwlabel:`IN` button                                        Enable Beatloop.
:hwlabel:`SHIFT` + Loop :hwlabel:`IN` button                     Halve the current loop size.
Loop :hwlabel:`OUT` button                                       Disable Beatloop.
:hwlabel:`SHIFT` + Loop :hwlabel:`OUT` button                    Double the current loop size.
Beat Align LED                                                   Track end warning (make sure :hwlabel:`BEATMATCH GUIDE` is on for this to work)
===============================================================  ==========================================

Browser
~~~~~~~

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`BROWSER` turn                                          Move up/down list.
:hwlabel:`SHIFT` + :hwlabel:`BROWSER` turn                       Scroll up/down list.
:hwlabel:`BROWSER` press                                         Switch focus between list and file view.
:hwlabel:`SHIFT` + :hwlabel:`BROWSER` press                      Maximize/Minimize library view.
:hwlabel:`ASSISTANT` button                                      Toggle AutoDJ (playlist must be set).
===============================================================  ==========================================

Performance Pads
~~~~~~~~~~~~~~~~

Hot Cue Mode
^^^^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1 - 4                                                        Set and trigger :term:`hotcue` 1 - 4
:hwlabel:`SHIFT` + Pad 1 - 4                                     Delete :term:`hotcue` 1 - 4.
===============================================================  ==========================================

Roll Mode
^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1                                                            Set Beatloop of 1 beat size.
Pad 2                                                            Set Beatloop of 2 beat size.
Pad 3                                                            Set Beatloop of 4 beat size.
Pad 4                                                            Set Beatloop of 8 beat size.
===============================================================  ==========================================

FX Mode
^^^^^^^

When using **Firmware v1.68 and earlier**, each FX pad will send multiple and different Note and CC messages.
As these could not all be used properly with Mixxx current effect framework, a simplified configuration was assigned using the pad in :hwlabel:`SHIFT` mode for convenience.

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
:hwlabel:`SHIFT` + Pad 1 - 3                                     Toggle Effect 1 - 3.
:hwlabel:`SHIFT` + Pad 4 (deck A)                                Toggle Effect Rack 1.
:hwlabel:`SHIFT` + Pad 4 (deck B)                                Toggle Effect Rack 2.
===============================================================  ==========================================

However, after applying **Firmware v1.72**, each FX pad now sends a simple Note On/Note Off (as is the case in every other Pad mode).
This makes it easier to use the pads to control effect and the latest mapping take advantage of this possibility by removing the use of the :hwlabel:`SHIFT` button.

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1 - 3                                                        Toggle Effect 1 - 3.
Pad 4 (deck A)                                                   Toggle Effect Rack 1.
Pad 4 (deck B)                                                   Toggle Effect Rack 2.
===============================================================  ==========================================

.. seealso::
   Read the update guide for more details about `updating the firmware <https://www.djuced.com/change-your-pad-fx-on-hercules-djcontrol-inpulse-firmware-update-guide>`__.

Sampler Mode
^^^^^^^^^^^^

===============================================================  ==========================================
Control                                                          Function
===============================================================  ==========================================
Pad 1 - 4 (deck A)                                               Trigger Sampler 1 - 4.
Pad 1 - 4 (deck B)                                               Trigger Sampler 5 - 8.
===============================================================  ==========================================

Unmapped Controls
~~~~~~~~~~~~~~~~~

The following controls are not mapped because they are controlled by the hardware.

-  :hwlabel:`MASTER` knob
-  :hwlabel:`HEADPHONE` knob
-  :hwlabel:`MASTER` buttons
-  :hwlabel:`BEATMATCH` guide
