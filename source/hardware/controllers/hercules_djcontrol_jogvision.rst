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
   The **Master** and **Headphone** knobs, as well as the
   **Master** button are hardware controls and interact directly with the
   integrated sound card’s output.
   
Mapping configuration
~~~~~~~~~~~~~~~~~~~~~

Edit the :file:`Hercules_DJControl_Jogvision-scripts.js`, and change the ``CFG.(user|fine)`` variables to fit your needs:  

.. list-table:: *USER Variables* (you may freely modify them)
   :widths: 25 25 25 50
   :header-rows: 1

   * - VARIABLE NAME
     - DEFAULT VALUE
     - AVAILABLE VALUES
     - DESCRIPTION
   * - beatDetection
     - normal
     - normal\|follow
     - (follow=song position is more accurate with beat position, but beat detection is much less accurate)
   * - initUpdateEffects
     - 0.8
     - \[0..1\]
     - (if value > 0, set some effects values at startup with given float value)
   * - beatHelper
     - 1
     - 0\|1
     - (0=disabled; 1=use outer jog leg to indicate where to slide the pitch controller; see also 'CFG.fine.beatHelpSensitivity' variable)
   * - beatActiveMode
     - follow
     - normal\|reverse\|blink\|follow\|fill\|bounce\|alternate\|off\|on
     - defines how the beats leds will lite

.. list-table:: *FINE TUNNING Variables* (you may modify them, but not too far from the default values...)
   :widths: 25 25 25 50
   :header-rows: 1

   * - VARIABLE NAME
     - DEFAULT VALUE
     - AVAILABLE VALUES
     - DESCRIPTION
   * - beatHelpSensitivity
     - 0.5
     - \[0..1)
     - Max distance (float) in BPMs to be considered as a match (in use if CFG.user.beatHelper=1): the lower, the more sensitive. Values equal or bigger than 1 are reset to 0.9 and a warning is printed
   * - quickMoveFactor
     - 0.002
     - \[0..1\]
     - the smaller (float), the slower MODE+JogWheel will move 'playposition' (when such channel is NOT playing)
   * - quickBrowseFactor
     - 10
     - \[0..inf\]
     - the bigger, the faster MODE+Browser jog will move the cursor position in the library up/down
   * - spinBackBrakeFactor
     - 100
     - (0..5000\]
     - the bigger, the softer the brake will be applied (0 = immediate stop; >=5000 = it will take almost forever to stop)
   * - spinBackInitialSpeed
     - 6
     - (0..200\]
     - the bigger, the stronger will be the "back" impulse (1 = no spinbak, but stop and start sloooowly)
   * - mixGainFactor
     - 0.1
     - (0..1)
     - (float) the bigger, the faster the Pregain or Mix level will be updated

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
