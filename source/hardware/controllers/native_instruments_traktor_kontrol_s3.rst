.. _native-instruments-traktor-kontrol-s3:

Native Instruments Traktor Kontrol S3
=====================================

.. sectionauthor::
  Owen Williams <owilliams at mixxx.org>
  Robbert van der Helm <mail@robbertvanderhelm.nl>

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
Main          Channel 1-2
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
sync on. Refer to :ref:`Sync Lock documentation <sync-lock>`
for details.

.. hint:: There are two :hwlabel:`SHIFT` buttons, one for each side of the
          controller. Make sure you press the :hwlabel:`SHIFT` button on the
          same side as the control you want to modify.

Mixer
~~~~~

  - The :hwlabel:`GAIN` and equalizer :hwlabel:`HIGH`/:hwlabel:`MID`/:hwlabel:`LOW` knobs and the :hwlabel:`CUE` (headphones) button behave as labelled.
  - :hwlabel:`FX Enable`, buttons, FX select buttons, and the FX knobs: See Effect section below.
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
Library encoder press                       Load track selected in library to the deck or open selected tree in menu.
:hwlabel:`SHIFT` + Library encoder press    Eject track.
Small play button                           While held, plays the current track in the preview deck.  If you rotate the library encoder while you hold the :hwlabel:`PLAY` button, Mixxx will scan through the track being previewed.
Star button                                 This button is not used.
:hwlabel:`≡+` (List-plus button)            Move focus of library control between left-hand tree, search, and main list.
:hwlabel:`VIEW` button                      Expand / minimize library view.
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
By default, the buttons on the right side of the controller also correspond to Samplers 1-8.
If you edit the javascript file and set `TraktorS3.SixteenSamplers = true;`, the samplers on the right-hand deck correspond to Samplers 9-16.
By default, pressing a number button will activate a sample.
Pressing the button again will stop sample playback.

You can change this behavior by editing the javascript file to set `TraktorS3.SamplerModePressAndHold = true;`.
In this mode, the sample will play while the button is held, and stop when you let go.

In both modes, holding :hwlabel:`SHIFT` and pressing a button will eject the sample if it is not playing, and will rewind the sample back to the beginning if it was playing.

Effects
-------

This mapping has two modes for controlling the Mixer FX section. The default
mode emulates the Mixer FX behavior as designed by Native Instruments and
focuses on Mixxx's quick effect chains. The second mode is specific to Mixxx and
instead provides detailed control over Mixxx's four effect units at the cost of
being more complex to use.

Quick Effect Mode (default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This mode mimics the intended Mixer FX behavior of the S3 by using Mixxx's quick
effect chains. The idea is that the :hwlabel:`Filter` and :hwlabel:`FX 1-4`
buttons on the right hand side of the controller's mixer map to the first five
quick effect chain presets selected in :menuselection:`Options --> Effects`. The
:hwlabel:`Filter` button, which is considered to be the default state, is mapped
to the first preset in the list, and the other FX select buttons are mapped to
the next four presets. Pressing one of these buttons changes the quick effect
chain of each of the four channels to the corresponding preset, allowing you to
control different effects with the FX knobs. The :hwlabel:`FX Enable` and FX
select buttons light up to indicate which effect chains are active and on what
channel. Meanwhile, pressing and holding one of the five FX select buttons while
pressing one of four channel's :hwlabel:`FX Enable` buttons assigns a quick
effect chain preset to that channel without affecting the other channels. This
allows efficient use of the controller's limited number of effects controls.

Setup
^^^^^

To make optimal use of this mode, you may want to change the following
preferences:

..
   This relies on https://github.com/mixxxdj/mixxx/pull/11198 or a similar PR
   being merged. Since the behavior without it can be a bit confusing, a bullet
   explaining the soft takeover behavior was added instead:

   - The '*Keep superknob position*' option in :menuselection:`Options --> Effects`
     page should be enabled. Otherwise changing the quick effect chain while the
     knob is not exactly at the center position may cause the quick effect
     superknob to become stuck in soft takeover mode until you move the physical
     knob to the superknob's new position.

- The very first quick effect chain preset in the quick effect presets list on
  the same :menuselection:`Options --> Effects` page should be set to the Moog
  Filter preset or another filter preset.
- The next four quick effect chain presets should contain that exact same filter
  effect, plus another effect. Delays, reverbs, flangers, trance gates, and
  white noise are some examples of effects that would work well here.
- Switching to a new quick effect chain preset using the :hwlabel:`Filter` and
  :hwlabel:`FX 1-4` buttons will load that preset's default values. If the FX
  knob is not already in the neutral position for the preset, then the FX knob
  will be put in soft takeover mode and you will need to turn it to match the
  super knob's new position before you can start using it. This behavior differs
  from similar setups in other DJ hardware and software.

Controls
^^^^^^^^

========================================================== ===========================================================================================================================================================================
Control                                                    Description
========================================================== ===========================================================================================================================================================================
:hwlabel:`Filter`/:hwlabel:`FX 1-4`                        Change the quick effect chain on all four channels to the first, second, third, fourth, or fifth quick effect chain preset.
:hwlabel:`Filter`/:hwlabel:`FX 1-4` + :hwlabel:`FX Enable` Change only one channel's quick effect chain preset without affecting the other channels.
:hwlabel:`FX Enable`                                       Bypass the channel's quick effect chain.
FX knobs                                                   Change the channel's quick effect superknob.
========================================================== ===========================================================================================================================================================================

Multi Effect Mode
~~~~~~~~~~~~~~~~~

Because the S3 has limited effects controls, this FX setup is unusual and a little complex.
Each deck has a single effect toggle button and one knob, and on the right-hand side of the mixer there are five buttons, one for each effect chain and one for the QuickEffect.
These buttons and knobs are used in different ways depending on how they are pushed, and together allow the DJ to customize all of the effects.

There are three modes that the effect controls can be in:
1.  The initial mode is Filter Mode.
This mode is indicated when the :hwlabel:`FX ENABLE` buttons have the same colors as the individual decks.
This mode is used for adjusting QuickEffects and assigning Effect Chains to decks.
1.  The next mode is Effect Chain Edit Mode.
This mode is indicated when the :hwlabel:`FX ENABLE` buttons are all the same color as one of the effect buttons.
This mode is used for turning individual effects in a chain on and off, and adjusting each effect chain's mix knob.
1.  The last mode is Effect Focus Mode.
This mode is indicated when :hwlabel:`FX ENABLE` buttons are all the same color as one of the effects, and one of the :hwlabel:`FX SELECT` buttons is blinking.
This mode is used for tuning individual parameters in an effect and enabling or disabling effect toggle buttons.

Switching Effect Modes
^^^^^^^^^^^^^^^^^^^^^^

At any time, you can push the :hwlabel:`FILTER` :hwlabel:`FX SELECT` button to return to Filter Mode.
If you get lost, try pusing the :hwlabel:`FILTER` button to start over.

Press any :hwlabel:`FX SELECT` button to enter Effect Chain mode for that number chain.
If you press the same :hwlabel:`FX SELECT` button again, you'll return to Filter Mode.
Press a different :hwlabel:`FX SELECT` button to enter Effect Chain mode for that other chain.

Press and hold an :hwlabel:`FX SELECT` button, then press a :hwlabel:`FX ENABLE` button to enter Effect Focus mode.
The :hwlabel:`FX SELECT` button will start blinking.
From left to right, the :hwlabel:`FX ENABLE` buttons will focus on the first through fourth effects in the chain.
If you press any :hwlabel:`FX SELECT` button, you'll return to Effect Chain mode.

Soft Takeover
^^^^^^^^^^^^^

The knobs have Soft Takeover mode enabled, which means you need to turn the physical knob to match the current position of the UI knob before the value will change.
If you are wondering why it seems like the values aren't changing, you may need to rotate the knob more.

Assigning Effects
^^^^^^^^^^^^^^^^^

You can assign effect chains to individual decks in Filter Mode.
Press and hold :hwlabel:`FX ENABLE`, then press the desired :hwlabel:`FX SELECT` button or buttons.
The :hwlabel:`FX SELECT` buttons that are bright are the effect chains that are selected for that deck.

Filter Mode
^^^^^^^^^^^

In Filter Mode the FX knobs control each channel's selected quick effect. By
default this is a combined low-pass and high-pass filter, but a different effect
can be chosen from the :menuselection:`Options --> Equalizer` section or
directly from the mixer if supported by the selected Mixxx skin.

Effect Chain Edit Mode
^^^^^^^^^^^^^^^^^^^^^^

In Effect Chain Edit Mode, the :hwlabel:`FX ENABLE` buttons change color to match the selected FX button.
The lights will be dim if the effect is disabled, and bright if it is enabled.
Tap the :hwlabel:`FX ENABLE` button to enable or disable the effect.
Turn the first three knobs to adjust the meta knob for each effect.
The last filter knob adjusts the mix knob for the whole chain.
This is to prevent sudden changes in sound when navigating between modes.

Effect Focus Mode
^^^^^^^^^^^^^^^^^

In Effect Focus Mode, the :hwlabel:`FX ENABLE` buttons represent effect button parameters, while the four knobs adjust the first four parameters of the selected effect.

Mapping options
---------------

.. sectionauthor::
  Sam Whited <sam@samwhited.com>

Settings can be edited in the preference windows, under :guilabel:`Preferences`
> :guilabel:`Controllers` > :guilabel:`Traktor Kontrol S3 ...`.

.. csv-table::
   :header: "Setting", "Values", "Function"
   :widths: 30, 50, 40

   "Effect section layout", "Quick Effect, Advanced Mode", "Changes the layout of the FX section to match either the controller layout or the Mixxx standard layout."
   "Reset FX chain on startup", "Boolean", "Reset to the default effect on startup, or preserve the last selected effect."
   "Use channel colors for FX enable buttons", "Boolean", "Use the selected channel color for the FX buttons or use a different color."
   "Pitch Slider Mode", "Absolute, Relative", "Use the pitch faders in normal (absolute) mode or as relative faders that can be moved higher or lower multiple times."
   "Stop samplers when button is released", "Boolean", "Stop the sampler when the button is released instead of requiring a separate button press."
   "Enable scratch mode on start", "Boolean", "Enable or disable the jog button on startup."
   "Use deck 2 for samplers 9–16", "Boolean", "Use the deck 2 buttons for more samplers (instead of using both for samplers 1–8)."
   "Channel 1 Color", "Colors", "Set the color for the first channel buttons."
   "Channel 2 Color", "Colors", "Set the color for the second channel buttons."
   "Channel 3 Color", "Colors", "Set the color for the third channel buttons."
   "Channel 4 Color", "Colors", "Set the color for the fourth channel buttons."
