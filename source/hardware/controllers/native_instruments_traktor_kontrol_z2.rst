Native Instruments Traktor Kontrol Z2
=====================================

.. sectionauthor::
   Jörg Wartenberg


The Native Instruments Traktor Kontrol Z2 is a 2+2 channel USB :term:`HID` mixer/controller with an integrated audio interface.
It has two full channels and two further channels with limited controls
The Traktor Z2 is intended for a DVS systems and is provided with Traktor Scratch MK2 :term:`timecode` Vinyls and CDs.

-  `Manufacturer’s product page <https://www.native-instruments.com/en/products/traktor/dj-mixer/traktor-kontrol-z2/>`__
-  `Virtual DJ Hardware Page <https://www.virtualdj.com/manuals/hardware/ni/z2.html>`__
-  `Traktor Kontrol Z2 Manual (ZIP-file) <https://www.native-instruments.com/fileadmin/ni_media/downloads/manuals/TRAKTOR_KONTROL_Z2_Manual_All_Languages_12_2014.zip>`__
-  `Driver/Firmware-Updates Download Page <https://www.native-instruments.com/en/support/downloads/drivers-other-files/>`__

.. versionadded:: 2.4.0

Drivers
-------

You can download the latest Windows & MacOS drivers and firmware from the `manufacturer’s website <https://www.native-instruments.com/en/support/downloads/drivers-other-files/>`__.
Since the Traktor Kontrol Z2 is a USB class compliant HID and audio device, the device is plug-and-play on Linux.

.. warning::
   **Parallel installation of Traktor software on Windows**
   If you have a parallel installation of Traktor on Windows, there will be a :file:`NIHardwareService.exe` process that takes control of the Traktor Kontrol Z2's LEDs.
   To make the them work reliable with Mixxx, you either need to uninstall the Traktor software, or stop the process by opening the task manager, selecting :guilabel:`Show processes from all users` and kill the :file:`NIHardwareService.exe` process.

Audio Setup
-----------

The mapping relies on the following channel assignments:

===================== ================
Output Channels       Assigned to
===================== ================
1-2                   Master
3-4                   Headphones
===================== ================

===================== ================
Input Channels        Assigned to
===================== ================
1-2 (Mic/Aux)         Microphone 1
3-4 (CH 1 Line/Phono) Vinyl Control 1
5-6 (CH 2 Line/Phono) Vinyl Control 2
7-8 (Recording)       Record/Broadcast
===================== ================

The microphone and auxiliary inputs are mixed with each other in the hardware together in input channels 1-2, so Mixxx can record and broadcast them.

The knobs for :hwlabel:`MASTER`, :hwlabel:`BOOTH`, :hwlabel:`HP VOLUME` are controlling the hardware mixer of the built-in audio interface.
Hence, turning the knobs will not change values in the Mixxx :term:`GUI` and you’ll need to set the Mixxx knobs to their default values when using the controller:

- Set the master/booth/headphones levels to 100% (knob center position)
- Set cue/master mixing to cue-only (leftmost position)

.. note::
   You should assign the :guilabel:`Vinyl Control` input channels even if you do not intend to use timecode vinyl.

Controls
--------

Mixer mode (Computer Internal vs. Direct mixer hardware)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Traktor Z2 allows not only mixing using the mixer hardware directly, but also mixing internal in the software of the connected computer.

Unique to the Traktor Z2 is, that the mixer mode can be switched per channel. This allows the user to connect another computer and starting Mixxx, while playing a track from an analog source in direct mode, and than blend over seamless to another channel in Internal mixing mode controlled by Mixxx.

The mixing mode of ChA and ChB is controlled by the two Traktor buttons on top:

======================================  ==================  ======================================  ====================================================
Traktor button state                    Traktor button LED  Action                                  Behavior

======================================  ==================  ======================================  ====================================================
Direct hardware mixing                  Off                 Press button to toggle                  Only Gain, EQ, Filter and Fader of channel operation (works without computer)
Computer Internal mixing (Passthrough)  Dimmed              :hwlabel:`SHIFT` hold + Traktor button  Mixxx mixes the signal, but the channel is set to Passthrough <vinyl-control-mode-and-cueing-controls>. Similar to direct mode, but allows the use of features like software effects.
Computer Internal mixing                Bright              Press button to toggle                  Mixxx plays the track and mixes the signal internally.
======================================  ==================  ======================================  ====================================================

.. note::
   Note, the selection of the mixing mode is a hardware function overruling the software. Only if all channels are switched to computer Internal mixing, you've all features of Mixxx available!

Shift button states
~~~~~~~~~~~~~~~~~~~

==============================  ================  ====================================================
Shift button state              Shift button LED  Action
==============================  ================  ====================================================
Unshifted                       Off
Shift hold                      Bright            Press and hold :hwlabel:`SHIFT`
Shift locked                    Dimmed            Short click on :hwlabel:`SHIFT` to toggle lock state
==============================  ================  ====================================================

Browse Section
~~~~~~~~~~~~~~

   Native Instruments Traktor Kontrol Z2 (Browse section)

========  =============================================================  ==========================================
No.       Control                                                        Function
========  =============================================================  ==========================================
1         :hwlabel:`LOAD/DUPLICATE A` (left) button                      Load song into deck A.
2         :hwlabel:`LOAD/DUPLICATE B` (right) button                     Load song into deck B.
3         :hwlabel:`SHIFT` + :hwlabel:`LOAD/DUPLICATE A` (left) button   Duplicate track and play position from deck B to A
4         :hwlabel:`SHIFT` + :hwlabel:`LOAD/DUPLICATE B` (right) button  Duplicate track and play position from deck A to B
5         Rotary Selector                                                Turn to move tracklist cursor up/down. Press to toggle the selected item.
6         :hwlabel:`SHIFT` + Rotary Selector                             Turn to move sidebar cursor left right/down.
========  =============================================================  ==========================================
