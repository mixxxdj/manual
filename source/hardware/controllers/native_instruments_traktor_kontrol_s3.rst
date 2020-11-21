Native Instruments Traktor Kontrol S3
=====================================

.. sectionauthor::
  Owen Williams <owilliams at mixxx.org>

.. versionadded:: 2.3.0

The Kontrol S3 is an introductory 4 deck controller with good build
quality and integrated sound card. This is the first controller released
with the "S3" name.

The Kontrol S3 can run from USB bus power. Using the separate power
supply increases the brightness of the LEDs, which is helpful for using
it in daylight, and increases the volume of the headphone output.

  - `Manufacturer's product
    page <https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s3/>`__

Compatibility
-------------

Controller
~~~~~~~~~~

The Kontrol S3 is a USB class compliant audio and :term:`HID` device,
so it is compatible with Mixxx without any proprietary drivers on
GNU/Linux and Mac OS X. On Windows, it is recommended to install the
`driver from Native
Instruments <https://www.native-instruments.com/en/support/downloads/drivers-other-files/#traktorkontrols3>`__
and select the ASIO sound API in the Sound Hardware section of Mixxx's
Preferences.

With the S3 plugged in, the device is listed as an available
controller in Mixxx's Preferences. The controller uses
HID for the knobs, buttons, and other components on the device, so the
mapping can only be loaded when you select the HID device on the left
side of Mixxx's Preferences.

Mapping description
-------------------

Note that Mixxx doesn't have the concept of a single "leader" deck for
sync. Instead, push and hold the :hwlabel:`SYNC` button to "lock" sync on for all
decks you want to remain in sync. Or you can push :hwlabel:`SHIFT` + :hwlabel:`SYNC` to lock
sync on. Refer to :ref:`Sync Lock documentation <master-sync>`
for details.

.. hint:: There are two :hwlabel:`SHIFT` buttons, one for each side of the
          controller. Make sure you press the :hwlabel:`SHIFT` button on the
          same side as the control you want to modify.

Mixer
~~~~~

  - The :hwlabel:`GAIN` and equalizer :hwlabel:`HIGH`/:hwlabel:`MID`/:hwlabel:`LOW` knobs and the :hwlabel:`CUE` (headphones) button behave as labelled.
  - :hwlabel:`FX Enable` buttons: See Effect section below.
  - The :hwlabel:`FILTER` knob controls the Quick Effect superknob. By default, this uses a high-/low-pass filter, but a different effect can be chosen in the :ref:`Equalizer section of Mixxx' Preferences <preferences-equalizers>`.
  - :hwlabel:`EXT`: The :hwlabel:`EXT` button changes the fourth channel pregain (knob), pfl, and volume (slider) adjustments to operate with the Microphone input.  The microphone does not respond to EQ or effects.
  - :hwlabel:`SHIFT` + :hwlabel:`EXT`: Switches input from Mic to Line and back again.

The Main Volume knob on the S3 controls the volume of the S3's main
output in hardware, so it does not affect the software main output gain knob
in Mixxx by default. You can hold :hwlabel:`SHIFT` and turn the knob to adjust Mixxx'
main output gain.  Note that this will still also adjust the hardware gain, so
after you release :hwlabel:`SHIFT` you'll need to adjust the knob again.

Peak display is only generated from software. So if
you see clipping indicated, lower the gain of the playing decks or use :hwlabel:`SHIFT` + Main Volume knob.

Decks
~~~~~

==========================================  ===========================================================================================================================================================================
Control
==========================================  ===========================================================================================================================================================================
Library knob press                          Load track selected in library to the deck.
:hwlabel:`SHIFT` + Library knob press       Eject track.
Small play button                           While held, plays the current track in the preview deck.  If you rotate the library knob while you hold the :hwlabel:`PLAY` button, Mixxx will scan through the track being previewed.
Star button                                 This button is not used.
List-plus button                            Adds the current track to the Auto DJ list.
:hwlabel:`VIEW` button                      Move focus of library control between left-hand tree and main list.
==========================================  ===========================================================================================================================================================================

Transport Mode Buttons
~~~~~~~~~~~~~~~~~~~~~~

=================================  ==========================================================
Control
=================================  ==========================================================
:hwlabel:`REV`                     Activates a reverse-roll (aka "censor") effect.
:hwlabel:`SHIFT` + :hwlabel:`REV`  Turns on reverse playback mode.
:hwlabel:`GRID`                    Turns on Quantize mode.
:hwlabel:`FLUX`                    Turns on Slip mode.
:hwlabel:`JOG`                     Hold to use the wheels to quickly scroll through the track
=================================  ==========================================================

Looping
~~~~~~~

======================================   ================================================
Control
======================================   ================================================
Right Encoder Turn                       Double/halve loop size.
Right Encoder Press                      Activate loop of set size from current position.
:hwlabel:`SHIFT` + Right Encoder Press   Toggles the existing loop on and off.
Left Encoder Turn                        Beatjump forward/backward.
:hwlabel:`SHIFT` + Left Encoder Turn     Adjust beatjump size.
Left Encoder Press                       Activates beatloop roll.
:hwlabel:`SHIFT` + Left Encoder Press    Activates a loop and then stops.
======================================   ================================================

Rate / Keylock
~~~~~~~~~~~~~~

There are two ways the rate sliders can be mapped: Absolute, and Relative.  Absolute mode is the default. In this mode, the position of the pitch slider matches the on-screen pitch slider position.  If the sliders are misaligned, Mixxx engages "soft takeover mode" -- Mixxx won't update the value of the slider until the controller matches the GUI. In Relative mode, moving the slider always adjusts the value of the pitch slider, even if they don't match.

  - Absolute Mode:

     - :hwlabel:`KEYLOCK`: Press to toggle keylock mode.
     - :hwlabel:`SYNC`: Press to beatsync, or press and hold to activate Sync Lock Mode.
     - Pitch slider: Adjusts playback speed.
     - :hwlabel:`SHIFT` + Pitch slider: Adjusts musical key
  - Relative Mode:

     - :hwlabel:`KEYLOCK`: Press to toggle keylock mode.
     - :hwlabel:`SYNC`: Press to beatsync, or press and hold to activate Sync Lock Mode.
     - Pitch slider: Adjusts playback speed.
     - Keylock + Pitch Slider: adjusts musical key
     - :hwlabel:`SHIFT` + Pitch Slider: Allows the user to move the slider without any effect.

Effects
~~~~~~~

The FX setup is unusual on this controller.  Each deck has a single toggle button for effects, and on the right-hand side of the mixer there are five buttons that determine which effects are applied to every channel that has effects on.  This means it is not possible to use the controller to select one effect for one deck, and another effect for another.  You can still make these choices in the Mixxx UI, however.

When the :hwlabel:`FILTER ENABLE` button is off, the knob still controls the default Quick Effect, even if that button is not lit in the FX section. When the :hwlabel:`FILTER ENABLE` button is on, the Quick Effect is only enabled if the Filter :hwlabel:`FX SELECT` button is on.  This means the Quick Effect is available on channels that don't have any other effects active.

When turning Filter Enable off, Mixxx will use soft takeover so the QuickEffect doesn't suddenly activate.

Mapping options
~~~~~~~~~~~~~~~

There are two user-friendly customizations possible on the S3:

  1. Toggle between Absolute and Relative pitch slider mode.
  2. Customize the colors for decks A, B, C, and D.

To make these changes, you need to edit to the mapping script file.

1.  Open Mixxx Preferences and select the Kontrol S3 in the side list.
2.  There will be a box labeled Preset Info, and that box will have a section
    labeled :guilabel:`Script Files`.
3.  Select :file:`Traktor-Kontrol-S3-hid-scripts.js`.
4.  Either the file should open in an editor, or you should see a file
    browser window with that file selected. If you see a file browser,
    right click the file and select an option to edit it.
5.  At the top of the file will be short instructions explaining how to edit
    the file.

Changes you make will take effect as soon as you save the file.
