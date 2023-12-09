.. _native-instruments-traktor-kontrol-z1:

Native Instruments Traktor Kontrol Z1
=====================================

Native Instruments Traktor Kontrol Z1 is a two-deck ultra-compact DJ controller with an integrated 96 kHz / 24-bit sound card. It features stereo sound output using two unbalanced RCA connectors and a standard headphone (1/8" / 3.5 mm TRS) output jack. The controller can be powered directly from the USB bus or by using an external power adapter.

- `Traktor Kontrol Z1 product page <https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-z1/>`__
- `Mixxx forum mapping thread <https://mixxx.discourse.group/t/new-mapping-for-native-instruments-traktor-kontrol-z1/28436>`__

Compatibility
~~~~~~~~~~~~~

The Kontrol Z1 is a HID and USB audio class compliant device, which makes it fully compatible with Mixxx. It requires no proprietary drivers when used on Linux or macOS.

For Windows, download and install the latest Traktor Kontrol Z1 audio driver from the `manufacturer's website <https://www.native-instruments.com/en/support/downloads/drivers-other-files/>`__.

.. warning::
   **Parallel installation of Traktor Pro software on Windows**
   
   If you have a parallel installation of Traktor Pro on Windows, a service called :file:`NIHardwareService.exe` is running in the background, which has control over the LEDs of the Z1.
   
   To make the Z1 work properly with Mixxx, you must either uninstall the Traktor Pro software, or temporarily stop this Windows service. One way to do this is to open a Windows PowerShell terminal as Administrator, and run the following command: ``Stop-Service -Name "NIHardwareService"``.

Audio hardware setup
~~~~~~~~~~~~~~~~~~~~

The Z1 has a standard 4-channel sound card. Configure the channels in Mixxx as follows:

=======================  =======================
Audio output             Channel configuration
=======================  =======================
:guilabel:`Main`         Channel 1-2
:guilabel:`Headphones`   Channel 3-4
=======================  =======================

Controller overview
~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/native_instruments_traktor_kontrol_z1.png
   :align: center
   :width: 85%
   :figwidth: 85%
   :alt: Native Instruments Traktor Kontrol Z1 (schematic view)
   :figclass: pretty-figures

   *Native Instruments Traktor Kontrol Z1 (schematic view)*

Mapping description
~~~~~~~~~~~~~~~~~~~

All knobs and buttons function in Mixxx as they are labeled and follow the manufacturer's standard mapping. Two secondary track control functions are also available using the :hwlabel:`Mode` button as a modifier. This makes the Kontrol Z1 more usable by itself without other controllers.

======  ====================================  ==================================================================================  ==============================================================
No.     Element                               Primary function                                                                    Secondary function
======  ====================================  ==================================================================================  ==============================================================
1       :hwlabel:`Main` knob                  Main output volume (hardware function - not mapped in Mixxx)
2       :hwlabel:`Cue Vol` knob               Headphone output volume (hardware function - not mapped in Mixxx)
3       :hwlabel:`Cue Mix` knob               Adjusts cue / main mix for the headphone output
4       :hwlabel:`Gain` knobs                 Adjusts pre-fader gain of the deck
5       :hwlabel:`Hi` knobs                   High frequency equalizer knob
6       :hwlabel:`Mid` knobs                  Middle frequency equalizer knob
7       :hwlabel:`Low` knobs                  Low frequency equalizer knob
8       :hwlabel:`Filter | FX` knobs          Adjusts quick effect superknob for the deck
9       :hwlabel:`Filter | FX On` buttons     Toggles selected deck quick effect on / off                                         Start / stop track playback
10      :hwlabel:`Headphone A / B` buttons    Toggles deck headphone cueing on / off                                              Seek track to cue and stop
11      :hwlabel:`Mode` button                Activates secondary functions when held down
12      :hwlabel:`Level A / B` meters         Show the current instantaneous deck volume
13      Volume faders                         Adjusts channel volume fader for the corresponding deck
14      Crossfader                            Adjusts the crossfader between both decks
======  ====================================  ==================================================================================  ==============================================================
