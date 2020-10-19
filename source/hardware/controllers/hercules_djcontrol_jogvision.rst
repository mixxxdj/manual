Hercules DJControl Jogvision
============================

-  `Manufacturer's product page <https://www.hercules.com/en-us/product/djcontroljogvision-2old/>`__
-  `Manufacturer's support and downloads page <https://support.hercules.com/en/product/djcontroljogvision-en/>`__
-  `Forum thread <https://www.mixxx.org/forums/viewtopic.php?f=7&t=12580>`__
  
Whether you’re just getting started DJing or you’ve already refined your skills, you can let your creativity run wild.
Enjoy excellent precision and comfort to create your mixes using the circular displays on the jog wheels to guide your movements and perfect your scratches,
and have fun with the amazing contactless AIR Control sensor.
Your adventure starts right here and now. It’s your turn\!

Compatibility
-------------

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows. For Windows, please install the latest driver package available from
the `Support
page <https://support.hercules.com/es/product/djcontroljogvision-es/>`__.

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

All controls *act as labeled*, but there are some **additional** functionalities that have been added:

- MODE+Loop ON                  : set a loop_in mark (with curently defined loop_size), activate it, and enable slip mode  
- MODE+Loop X 1/2 / X 2         : do a 'beatjump_size' beats beatjump backward/forward  
- MODE+Loop Size Knob           : decrease/increase pitch (only key, not tempo!)  
- MODE+JogWheel plate (playing) : scratch with 'Slip' ON (deactivate 'Slip' when plate is released)  
- MODE+JogWheel plate (stopped) : move song position backward/forward faster by 'quickMoveFactor' factor  
- MODE+Browser Knob Turn        : move library selected position in groups of 'quickBrowseFactor' elements forward/backward  
- MODE+LOAD A|B                 : toggle 'quantize' for deck where MODE key is pressed  
- SHIFT+LOAD A|B                : eject track from deck where SHIFT key is pressed  
- SHIFT+Browser Knob Press      : activate (double-click) currently selected item in browser  
- SHIFT+Loop Size Knob          : move existing loop forward/backward  
- SHIFT+JogWheelTouch           : do a 'backspin' with 'spinBackBrakeFactor' and 'spinBackInitialSpeed' factors  
- SHIFT+MultiFX                 : set beatgrid to current position  
- SHIFT+Air control Filter      : do the reverse than standard, that is, high-pass filter  
