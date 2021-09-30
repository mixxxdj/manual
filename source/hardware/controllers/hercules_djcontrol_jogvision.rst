.. _hercules-djcontrol-jogvision:

Hercules DJControl Jogvision
============================

-  `Manufacturer's product page <https://www.hercules.com/en/product/djcontroljogvision/>`__
-  `Manufacturer's support and downloads page <https://support.hercules.com/en/product/djcontroljogvision-en/>`__
-  `Forum thread <https://mixxx.discourse.group/t/hercules-djcontrol-jogvision/17839>`__

Whether you’re just getting started DJing or you’ve already refined your skills, you can let your creativity run wild.
Enjoy excellent precision and comfort to create your mixes using the circular displays on the jog wheels to guide your movements and perfect your scratches,
and have fun with the amazing contactless AIR Control sensor.
Your adventure starts right here and now. It’s your turn\!

Compatibility
-------------

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows. For Windows, please install the latest driver package available from
the manufacturer's product page.

Sound card setup
----------------

This controller has built-in 4 channel output sound card, with:

================  ===================
Channel           Port
================  ===================
Master Output     RCA and 3.5mm jack
Booth Output      RCA and 3.5mm jack
Headphone Output  6.35mm and 3.5mm jack
Microphone Input  6.35mm jack
Auxiliary Input   3.5mm jack
================  ===================

- Open :menuselection:`Preferences --> Sound Hardware`
- Select the :guilabel:`Output` tab
- From the :guilabel:`Master` drop-down menu, select the audio interface, then :guilabel:`Channels 1-2`
- From the :guilabel:`Headphones` drop-down menu, select the audio interface, then :guilabel:`Channels 3-4`
- Click :guilabel:`Apply` to save the changes.

Please refer to the user manual for more details about the audio configuration in Mixxx.

.. note::
   The :hwlabel:`MASTER` and :hwlabel:`HEADPHONE` knobs, as well as the
   :hwlabel:`MASTER` button are hardware controls and interact directly with the
   integrated sound card’s output.

Mapping configuration
~~~~~~~~~~~~~~~~~~~~~

Edit the :file:`Hercules_DJControl_Jogvision-scripts.js`, and change the ``CFG.(user|fine)`` variables to fit your needs:

.. hint::
   This controller mapping can be customized by editing the corresponding Javascript file and editing the configuration options at the top of the file.

All controls act as labeled, but there are some additional functionalities that have been added:

=========================================================  =============================================================
Control                                                    Description
=========================================================  =============================================================
:hwlabel:`MODE` + :hwlabel:`LOOP ON`                       Set a loop_in mark (with currently defined loop_size), activate it, and enable slip mode
:hwlabel:`MODE` + :hwlabel:`LOOP X½` / :hwlabel:`LOOP X2`  Do a beatjump backward/forward
:hwlabel:`MODE` + :hwlabel:`LOOP SIZE` knob                Decrease/Increase pitch (only key, not tempo!)
:hwlabel:`MODE` + Jog Wheel plate (playing)                Scratch with 'Slip' on (deactivate 'Slip' when plate is released)
:hwlabel:`MODE` + Jog Wheel plate (stopped)                Move song position backward/forward faster
:hwlabel:`MODE` + :hwlabel:`BROWSER` knob turn             Move library's selected position multiple elements forward/backward
:hwlabel:`MODE` + :hwlabel:`LOAD` buttons                  Toggle 'quantize' for deck where :hwlabel:`MODE` button is pressed
:hwlabel:`SHIFT` + :hwlabel:`LOAD` buttons                 Eject track from deck where :hwlabel:`SHIFT` key is pressed
:hwlabel:`SHIFT` + :hwlabel:`BROWSER` knob press           Activate (double-click) currently selected item in browser
:hwlabel:`SHIFT` + :hwlabel:`LOOP SIZE` knob               Move existing loop forward/backward
:hwlabel:`SHIFT` + Jog Wheel touch                         Do a backspin
:hwlabel:`SHIFT` + :hwlabel:`MULTI FX`                     Set beatgrid to current position
:hwlabel:`SHIFT` + :hwlabel:`AIR CONTROL` Filter           Do the reverse than standard, that is, high-pass filter
=========================================================  =============================================================
