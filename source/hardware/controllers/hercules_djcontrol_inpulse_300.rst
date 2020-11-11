Hercules DJControl Inpulse 300
==============================

-  `Manufacturer’s product page <https://www.hercules.com/en-us/product/djcontrolinpulse300//>`__
-  `Manufacturer’s support and downloads page <https://support.hercules.com/en/product/djcontrolinpulse300-en//>`__
-  `Forum thread <https://mixxx.discourse.group/t/hercules-djcontrol-inpulse-300/17854/>`__

.. versionadded:: 2.2.4

Compatibility
-------------

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows. However, if you wish to use the `ASIO sound
API <https://mixxx.org/manual/latest/en/chapters/preferences.html?highlight=asio#windows>`__
under Windows, please install the latest driver package available from
the `Support
page <https://support.hercules.com/en/product/djcontrolinpulse300-en//>`__.

Sound card setup
----------------

This controller has built-in 4 channel output sound card, with MASTER
output (RCA) and HEADPHONE output (3.5mm jack).

-  Open **Preferences > Sound Hardware**
-  Select the **Output** tab
-  From the **Master** drop-down menu, select the audio interface, then
   **Channels 1-2**
-  From the **Headphones** drop-down menu, select the audio interface,
   then **Channels 3-4**
-  Click **Apply** to save the changes.

Please refer to `the user
manual <https://mixxx.org/manual/latest/en/chapters/example_setups.html#laptop-and-external-usb-audio-interface>`__
for more details about the audio configuration in Mixxx.

.. note::
   The **Master** and **Headphone** knobs, as well as the
   **Master** button are hardware controls and interact directly with the
   integrated sound card’s output. Although they also send MIDI messages,
   they have NOT been mapped in Mixxx, so do not expect an on-screen
   reaction when using them. This was done to prevent the knobs to adjust
   both the gain on the controller’s sound card and in Mixxx.

Mapping description
~~~~~~~~~~~~~~~~~~~

Save both MIDI and script files to your `user controller mapping
folder <https://github.com/mixxxdj/mixxx/wiki/controller%20mapping%20file%20locations#user-content-user%20controller%20mapping%20folder>`__,
then load the preset as described in `the user
manual <https://mixxx.org/manual/latest/en/chapters/controlling_mixxx.html#using-midi-hid-controllers>`__

Controls not included in this mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Master knob (Hardware control)
-  Headphone knob (Hardware control)
-  Master buttons (Hardware control)
-  Beatmatch guide (Hardware control)
-  PADS: Slicer/Slicer Loop
-  PADS: Toneplay
-  PADS: FX

.. note::
   When using **Firmware v1.68** and earlier, each FX pad will
   send multiple and different Note and CC messages. As these could not all
   be used properly with Mixxx current effect framework, the pads have not
   been assigned in this mapping. \* However, after applying **Firmware
   v1.72**, each FX pad now sends a simple Note On/Note Off (as is the case
   in every other Pad mode). This would make it easier to use the pads to
   control effect and the mapping might be modified eventually to take
   advantage of this possibility.

   For more details about `updating the
   Firmware. <https://www.djuced.com/change-your-pad-fx-on-hercules-djcontrol-inpulse-firmware-update-guide>`__

**Decks:**

Sync = Sync lock SHIFT + SYNC = Sync master.

Cue = Cue point SHIFT + CUE = Return to beginning of loaded song.

Play = Play/Pause SHIFT + Play = Cue Stutter.

Vinyl = Scratch On/Off (Default: ON) Q = Keylock Beat Align LED = Track
end warning (Make sure **Beatmatch Guide** is **On** for this to work)
Loop In = Beatloop 4 beats SHIFT + Loop In = Loop Halve. Loop Out =
Beatloop Off SHIFT + Loop Out = Loop Double.

**Browser:**

Encoder = Move up/down list Encoder button = Switch focus between List
and file view SHIFT + Encoder button = Maximize/Minimize browser view
Assistant = AutoDJ On/Off

**FX:**

FX On = FX 3 On/off SHIFT + FX On = FX 3 Select (next effect)

**PADS - Hot Cue:**

Set and trigger Hot Cue 1-4 SHIFT + Pad = Delete Hot Cue 1-4.

**PADS - Roll:**

Pad 1-4 = Beatloop 1 / 2 / 4 / 8 beats

**PADS - Sample:**

Trigger Sampler 1-4 (Deck A) Trigger Sampler 5-8 (Deck B)

**PADS - Beatjump:**

Pad 1-2: Beatjump Backward/Forward 1 beat Pad 3-4: Beatjump
Backward/Forward 2 beat Pad 5-6: Beatjump Backward/Forward 4 beat Pad
7-8: Beatjump Backward/Forward 8 beat
