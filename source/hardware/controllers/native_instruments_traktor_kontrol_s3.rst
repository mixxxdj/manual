.. _native-instruments-traktor-kontrol-s3:

Native Instruments Traktor Kontrol S3
=====================================

.. sectionauthor::
  Owen Williams <owilliams at mixxx.org>

The Kontrol S3 is an introductory 4 deck controller with good build
quality and integrated sound card. This is the first controller released
with the "S3" name.

The Kontrol S3 can run from USB bus power. Using the separate power
supply increases the brightness of the LEDs, which is helpful for using
it in daylight, and increases the volume of the headphone output.

  - `Manufacturer's product
    page <https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s3/>`__

.. versionadded:: 2.3.0

Compatibility
-------------

Controller
~~~~~~~~~~

The Kontrol S3 is a USB class compliant audio and :term:`HID` device,
so it is compatible with Mixxx without any proprietary drivers on
GNU/Linux and macOS. On Windows, it is recommended to install the
`driver from Native
Instruments <https://www.native-instruments.com/en/support/downloads/drivers-other-files/#traktorkontrols3>`__
and select the ASIO :ref:`sound API <preferences-sound-api>` in the :ref:`Sound Hardware section of Mixxx's Preferences <preferences-sound-hardware>`.

With the S3 plugged in, the device is listed as an available
controller in Mixxx's Preferences. The controller uses
HID for the knobs, buttons, and other components on the device, so the
mapping can only be loaded when you select the HID device on the left
side of Mixxx's Preferences.

Audio Hardware setup
--------------------

The S3 has a standard 4 channel sound card.  You should configure the channels
as follows:

============  =====================
Audio Output  Channel Configuration
============  =====================
Master        Channel 1-2
Headphones    Channel 3-4
============  =====================

Audio Inputs
~~~~~~~~~~~~
The S3 has two sets of inputs, but only one can be active at a time. There is
a set of line-level RCA inputs on the back of the controller, and a combo
XLR / 1¼" mic jack on the front.  Use :hwlabel:`SHIFT` + :hwlabel:`EXT` to switch
between these inputs.

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
  - :hwlabel:`SHIFT` + :hwlabel:`EXT`: Switches input sensitivity for the input connectors from Mic to Line and back again.

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
Control                                     Description
==========================================  ===========================================================================================================================================================================
Library encoder press                       Load track selected in library to the deck.
:hwlabel:`SHIFT` + Library encoder press    Eject track.
Small play button                           While held, plays the current track in the preview deck.  If you rotate the library encoder while you hold the :hwlabel:`PLAY` button, Mixxx will scan through the track being previewed.
Star button                                 This button is not used.
List-plus button                            Adds the current track to the Auto DJ list.
:hwlabel:`VIEW` button                      Move focus of library control between left-hand tree and main list.
==========================================  ===========================================================================================================================================================================

Transport Mode Buttons
~~~~~~~~~~~~~~~~~~~~~~

=================================  ==========================================================
Control                            Description
=================================  ==========================================================
:hwlabel:`REV`                     Activates a reverse-roll (aka "censor") effect.
:hwlabel:`SHIFT` + :hwlabel:`REV`  Turns on reverse playback mode.
:hwlabel:`GRID`                    Turns on Quantize mode.
:hwlabel:`FLUX`                    Turns on Slip mode.
:hwlabel:`JOG`                     When on, touching the jog wheels enables Scratch mode.
:hwlabel:`SHIFT` + Wheels          Hold to use the wheels to quickly scroll through the track.
=================================  ==========================================================

Deck Select Buttons
~~~~~~~~~~~~~~~~~~~~~~

Pressing a Deck Select button will activate that deck.

Press and hold one Deck Select button, then tap a second Deck Select button to clone the track loaded in the first deck to the second.

Looping
~~~~~~~

======================================   ================================================
Control                                  Description
======================================   ================================================
Right Encoder Turn                       Double/halve loop size.
:hwlabel:`SHIFT` + Right Encoder Turn    Move loop forward/backward by the beatjump size.
Right Encoder Press                      Activate loop of set size from current position, or disable active loop
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

     - :hwlabel:`KEYLOCK`: Press to toggle keylock mode (toggles when releasing the button).
     - :hwlabel:`SYNC`: Press to beatsync, or press and hold to activate Sync Lock Mode.
     - Pitch slider: Adjusts playback speed.
     - Keylock + Pitch Slider: adjusts musical key
     - :hwlabel:`SHIFT` + Pitch Slider: Allows the user to move the slider without any effect.

Button Pads
~~~~~~~~~~~

The grid of 8 buttons have two possible trigger modes: Hotcues, and Samplers.

In Hotcues mode, pressing the number button will set the hotcue if none exists, and activate it if one does.
If you hold :hwlabel:`SHIFT` and press a button, it will clear that hotcue.

In Samplers mode, the buttons on the left side of the controller correspond to Samplers 1-8.
The buttons on the right side of the controller correspond to Samplers 9-16.
By default, pressing a number button will activate a sample.
Pressing the button again will stop sample playback.

You can change this behavior by editing the javascript file to set `TraktorS3.SamplerModePressAndHold = true;`.
In this mode, the sample will play while the button is held, and stop when you let go.

In both modes, holding :hwlabel:`SHIFT` and pressing a button will eject the sample if it is not playing, and will rewind the sample back to the beginning if it was playing.

Effects
-------

Because the S3 has limited effects controls, the FX setup is unusual and a little complex.
Each deck has a single effect toggle button and one knob, and on the right-hand side of the mixer there are five buttons, one for each effect chain and one for the QuickEffect.
These buttons and knobs are used in different ways depending on how they are pushed, and together allow the DJ to customize all of the effects.

There are three modes that the effect controls can be in:
1.  The initial mode is Filter Mode.
This mode is indicated when the :hwlabel:`FILTER ENABLE` buttons have the same colors as the individual decks.
This mode is used for adjusting QuickEffects and assigning Effect Chains to decks.
1.  The next mode is Effect Chain Edit Mode.
This mode is indicated when the :hwlabel:`FILTER ENABLE` buttons are all the same color as one of the effect buttons.
This mode is used for turning individual effects in a chain on and off, and adjusting each effect chain's mix knob.
1.  The last mode is Effect Focus Mode.
This mode is indicated when :hwlabel:`FILTER ENABLE` buttons are all the same color as one of the effects, and one of the :hwlabel:`FX SELECT` buttons is blinking.
This mode is used for tuning individual parameters in an effect and enabling or disabling effect toggle buttons.

Switching Effect Modes
~~~~~~~~~~~~~~~~~~~~~~

At any time, you can push the :hwlabel:`FILTER` :hwlabel:`FX SELECT` button to return to Filter Mode.
If you get lost, try pusing the :hwlabel:`FILTER` button to start over.

Press any :hwlabel:`FX SELECT` button to enter Effect Chain mode for that number chain.
If you press the same :hwlabel:`FX SELECT` button again, you'll return to Filter Mode.
Press a different :hwlabel:`FX SELECT` button to enter Effect Chain mode for that other chain.

Press and hold an :hwlabel:`FX SELECT` button, then press a :hwlabel:`FILTER ENABLE` button to enter Effect Focus mode.
The :hwlabel:`FX SELECT` button will start blinking.
From left to right, the :hwlabel:`FILTER ENABLE` buttons will focus on the first through fourth effects in the chain.
If you press any :hwlabel:`FX SELECT` button, you'll return to Effect Chain mode.

Soft Takeover
~~~~~~~~~~~~~

The knobs have Soft Takeover mode enabled, which means you need to turn the physical knob to match the current position of the UI knob before the value will change.
If you are wondering why it seems like the values aren't changing, you may need to rotate the knob more.

Assigning Effects
~~~~~~~~~~~~~~~~~

You can assign effect chains to individual decks in Filter Mode.
Press and hold :hwlabel:`FILTER ENABLE`, then press the desired :hwlabel:`FX SELECT` button or buttons.
The :hwlabel:`FX SELECT` buttons that are bright are the effect chains that are selected for that deck.

Effect Chain Edit Mode
~~~~~~~~~~~~~~~~~~~~~~

In Effect Chain Edit Mode, the :hwlabel:`FILTER ENABLE` buttons change color to match the selected FX button.
The lights will be dim if the effect is disabled, and bright if it is enabled.
Tap the :hwlabel:`FILTER ENABLE` button to enable or disable the effect.
Turn the first three knobs to adjust the meta knob for each effect.
The last filter knob adjusts the mix knob for the whole chain.
This is to prevent sudden changes in sound when navigating between modes.

Effect Focus Mode
~~~~~~~~~~~~~~~~~

In Effect Focus Mode, the :hwlabel:`FILTER ENABLE` buttons represent effect button parameters, while the four knobs adjust the first four parameters of the selected effect.

Mapping options
---------------

There are two user-friendly customizations possible on the S3:

  1. Toggle between Absolute and Relative pitch slider mode.
  2. Customize the colors for decks A, B, C, and D.
  3. Change the Sampler playback mode.
  4. Whether wheel touch scratching is on by default.

To make these changes, you need to edit to the mapping script file.

1.  Open Mixxx Preferences and select the Kontrol S3 in the side list.
2.  There will be a box labeled :guilabel:`Mapping Info`, and that box will have a section
    labeled :guilabel:`Mapping Files`.
3.  Select :file:`Traktor-Kontrol-S3-hid-scripts.js`.
4.  Either the file should open in an editor, or you should see a file
    browser window with that file selected. If you see a file browser,
    right click the file and select an option to edit it.
5.  At the top of the file will be short instructions explaining how to edit
    the file.

Changes you make will take effect as soon as you save the file.
