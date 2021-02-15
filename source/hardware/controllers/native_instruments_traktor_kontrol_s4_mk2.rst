Native Instruments Traktor Kontrol S4 MK2
=========================================

The Kontrol S4 MK2 is a 4 deck all-in-one controller with a sturdy build quality and integrated sound card.
The MK2 has substantial improvements over the S4 MK1, including large multicolor buttons.
The MK1 is not supported and cannot be supported because it uses a proprietary communication protocol exclusive to Traktor.
The MK2 uses the standard :term:`HID` protocol (also used by keyboards & mice) to send and receive signals from a computer, so it can work with Mixxx.
The easiest way to tell the MK1 apart from the MK2 is the appearance of the jog wheel.
On the MK1, the top of the jog wheel is black plastic; on the MK2, the top of the jog wheel is shiny aluminum.

The Kontrol S4 Mk2 can run from :term:`USB` power.
Using the separate power supply increases the brightness of the LEDs, which is helpful for using it in daylight, and increases the volume of the headphone output.

-  `Manufacturer’s product page <https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s4/>`__

.. versionadded:: 2.1

Compatibility
-------------

Controller
~~~~~~~~~~

The Kontrol S4 MK2 is a USB class compliant audio, :term:`HID` and :term:`MIDI` device, so it is compatible with Mixxx without any proprietary drivers on GNU/Linux and MacOS.
On Windows, it is recommended to install the `driver from Native Instruments <https://www.native-instruments.com/en/support/downloads/drivers-other-files/>`__ and select the :ref:`ASIO sound API in the preferences <preferences-sound-api>`.

With the S4 plugged in, a MIDI device is listed as an available controller in Mixxx’s Preferences.
That is the MIDI input/output ports on the back of the S4 for connecting external MIDI gear; no mapping for the S4 will appear in the menu for the MIDI device.
The controller uses HID for the knobs, buttons, and other components on the device, so the mapping can only be loaded when you select the HID device on the left side of Mixxx’s Preferences.

Timecode vinyl
~~~~~~~~~~~~~~

The phono inputs on the S4 can be used with turntables for timecode vinyl control of Mixxx.

.. seealso::
   Read the :ref:`Vinyl Control section <vinyl-control>` for details.

Mapping Description
-------------------

Push and hold the :hwlabel:`SYNC` button to “lock” sync on for all decks you want to remain in sync.
Push :hwlabel:`SHIFT` + :hwlabel:`SYNC` to enable :ref:`Sync Lock <master-sync>` for details.

Mixxx does not have remix decks, so the four remix slot buttons control the samplers.
There are some more bonus actions that can be accessed by holding :hwlabel:`SHIFT` and pressing certain buttons.

Mixer
~~~~~

==================================================  =========================================================================
Control                                             Description
==================================================  =========================================================================
:hwlabel:`FILTER` knob                              Controls QuickEffect superknob. This controls the Filter effect by default, but a different effect can be chosen in the Equalizer section of Mixxs’s Preferences.
:hwlabel:`SNAP`                                     Toggles library fullscreen
:hwlabel:`LOOP RECORD`                              Toggles recording
:hwlabel:`LOOP RECORDER PLAY`                       Hold down and press :hwlabel:`FLUX` button on a deck to enable autoslip mode on that deck.
:hwlabel:`SHIFT` + :hwlabel:`Gain`                  Up/down will move the beatgrid
:hwlabel:`LOOP RECORDER PLAY` + :hwlabel:`GAIN`      Increase / decrease the BPM of the track by 0.5. Press the encoder to round the track the nearest whole BPM. Best done to fix tracks with the wrong BPM with the pitch fader at 0.
:hwlabel:`BROWSE` encoder                           Up/down will browse in the focused library pane. Pressing acts like a double click on the mouse.
==================================================  =========================================================================

:hwlabel:`GAIN`, effects routing, equalizer high/mid/low, and :hwlabel:`CUE` (headphones) behave as labeled.

The Master Volume knob on the S4 controls the volume of the S4’s master output in hardware, so it does not affect the software master gain knob in Mixxx.
Peak display is only generated from software, however.
So if you see or hear clipping, lower the gain of the playing decks; adjusting the master volume knob on the S4 will not help.

Decks
~~~~~

===================================================  =========================================================================
Control                                              Description
===================================================  =========================================================================
:hwlabel:`LOAD`                                      Load track selected in library to the deck.
:hwlabel:`SHIFT` + :hwlabel:`LOAD`                   Eject track
Small buttons with preview icons                     Play a sampler from its cue point. If no track is loaded in the sampler, the track selected in the library will be loaded.
:hwlabel:`SHIFT` + small buttons with preview icons  If sampler is playing, stop it. If sampler is not playing, the loaded track is ejected from the sampler.
:hwlabel:`1-4` numbered buttons                      Set/activate :term:`hotcue`
:hwlabel:`SHIFT` + :hwlabel:`1-4` numbered buttons   Clear hotcue
:hwlabel:`SHIFT` + Wheel nudge                       Fast search through track when not playing
:hwlabel:`FLUX` button                               Enable slip mode (if shift is held down this decreases the range of the BPM slider, if :hwlabel:`LOOP RECORDER PLAY` is held down enter autoslip mode)
:hwlabel:`RESET` button                              Reset key (if shift is held down increase the range of the BPM slider

===================================================  =========================================================================

Looping
^^^^^^^

==================================================  =========================================================================
Control                                             Description
==================================================  =========================================================================
Right Encoder (turn)                                Double/halve loop size. The loop size is shown on the controller. A dot on the right indicates a fractional loop size. Two dots indicates a loop size larger than 99 beats.
Right Encoder (press)                               Activate loop of set size from current position
:hwlabel:`SHIFT` + Right Encoder (turn)             Adjust key
:hwlabel:`SHIFT` + Right Encoder (press)            Reset key
Left Encoder (turn)                                 Beatjump forward/backward by beatjump size (shown on screen but not on controller), or move the loop by beatjump size if there is a loop enabled
Left Encoder (press)                                Re-enable a loop that has been set previously. Pressing this before a loop will keep playing until the loop is entered.
:hwlabel:`SHIFT` + Left Encoder (turn)              Adjust beatjump size
:hwlabel:`SHIFT` + Left Encoder (press)             Jump to loop in point, activate loop, and stop playback. This is helpful for preparing to mix a track in with a loop.
:hwlabel:`IN` button                                Set loop in point manually. Hold pressed while moving the jog wheel to finely adjust the loop in point.
:hwlabel:`OUT` button                               Set loop out point manually. Hold pressed while moving the jog wheel to finely adjust the loop out point.
==================================================  =========================================================================

Effects
~~~~~~~

The knob on the left of each effect unit controls the mix (dry/wet) knob for all 3 effects in the unit.
The other knobs control the metaknobs of the effects.
The buttons below the metaknobs control the effect enable buttons.
When pressed with shift, they cycle through the available effects.
The button below the mix knob toggles whether the effect parameters are showing on screen.
This will be expanded in a future update to implement the `Standard Effects Mapping <https://github.com/mixxxdj/mixxx/wiki/Standard-Effects-Mapping>`__.

The buttons at the top of each mixer column control which decks are routed to which effects units.

Mapping extras
~~~~~~~~~~~~~~~
Autoslip mode: Holding down :hwlabel:`LOOP RECORDER PLAY` and pressing the :hwlabel:`FLUX` on a deck will enable autoslip mode on that deck. Autoslip turns on slip mode automatically before doing certain actions and turns it off after the actions is finished. It works for beat loops, hot cues, and scratching (warning, can have weird effects when scratching).


Mapping options
~~~~~~~~~~~~~~~

If you choose, you can edit the controller script and change the Remix Slot buttons to perform loop rolls instead.
Also by default, :hwlabel:`SHIFT` + :hwlabel:`CUE` rewinds the track to the beginning but you can change this to a Reverse Roll (or “Censor”) effect instead.

Making these changes is still a little awkward and we will be making controller preferences easier to change in the future.
For now you’ll have to make a small change to the mapping script file. Don’t worry, the actual edit only involves replacing a single word in a text file.

1. Open Mixxx Preferences and select the Kontrol S4 in the side list.
2. Select :file:`Traktor-Kontrol-S4-MK2-hid-scripts.js`.
3. Click :guilabel:`Open Selected File`.
4. Either the file should open in an editor, or you should see a file browser window with that file selected. If you see a file browser, right click the file and select an option to edit it.
5. At the top of the file will be short instructions explaining what to do.
