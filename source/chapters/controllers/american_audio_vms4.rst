American Audio VMS4/4.1
=======================

-  `Original VMS4 <http://www.adj.com/vms4>`__
-  `VMS4.1 <http://www.adj.com/vms4-1>`__
-  `VMS4.1 (International site) <http://vms4.adjfocus.com/vms-41-digital-work-station.html>`__
-  `VMS4.1 Traktor edition <http://www.adj.com/vms4-1-traktor>`__

The original VMS4 has problems with sound quality. The microphone input
impedance is off and the output volume is low. The VMS4.1 is the same
controller, except that those hardware issues have been fixed. The
Traktor edition has different labels on some buttons & knobs, but it’s
otherwise the same hardware as the VMS4.1.

Setup
-----

.. note::
   Mixxx expects the VMS4 to be set to “Post EQ” mode for best
   sound quality. Do this by holding down the Headphone Cue button on
   Midilog 4 while powering on the unit. You only need to do this once.
   (Each time you do, it changes the mode back and forth.) Consult the
   `user manual <http://intranet.americandj.com/ItemRelatedFiles/8347/vms4.pdf>`__
   for more information.

   To check the status of this in Linux, at a
   console, issue the command ``lsusb -v|grep 'iSerial\|iProduct'`` and
   look at the serial number under the VMS4 device per the instructions in
   the user manual. As of this writing, the leading digit should be **1**.

1.  Make sure the VMS4 is off
2.  Slide the switch on the front of the VMS4 to “8 OUT”

    -  If you’re using vinyl control or aux devices (or Mixxx 1.11 &
       below) set the switch to “4 OUT” for 2-deck output and 2-deck
       input

3.  Turn on the unit (and plug in the USB cable if you haven’t yet)
4.  Start Mixxx
5.  Open Preferences
6.  Click Sound Hardware. In the right pane:

    1. Set the sample rate to **44100Hz**
    2. Set the Master output to **None**
    3. Set the Headphone output to **None**
    4. Set the Deck 1 output to the **VMS4** device and **Channel 3-4**
       (may show as “USB Audio Device” on Windows)
    5. Set the Deck 2 output to the **VMS4** device and **Channel 5-6**
    6. Set the Deck 3 output to the **VMS4** device and **Channel 1-2**
    7. Set the Deck 4 output to the **VMS4** device and **Channel 7-8**

       -  If you’re using 4 OUT mode, (for vinyl control/aux input or
          Mixxx 1.11 & below):

          1. Set the Deck 1 output to the **VMS4** device and **Channel
             1-2**
          2. Set the Deck 2 output to the **VMS4** device and **Channel
             3-4**
          3. For vinyl control, set the Vinyl Control 1 input to the
             **VMS4** device and **Channel 1-2**, connect a turntable to
             Midilog 1, and set it to Analog.
          4. For vinyl control, set the Vinyl Control 2 input to the
             **VMS4** device and **Channel 3-4**, connect a turntable to
             Midilog 4, and set it to Analog.

7.  Plug your headphones into the VMS4’s jack on the front. You will use
    the VMS4’s CUE buttons and knobs for headphone control.
8.  Still in the Preferences, expand “Controllers” on the left
9.  Select the “VMS4 MIDI” device (may show as “USB Audio Device” on
    Windows)

    -  Do not choose the the HID one. That’s for the little mouse pad
       and button area.

10. Click the Enable checkbox in the right pane
11. Click the drop-down and choose the “American Audio VMS4” preset
12. Click OK and the controller should light up. (In 1.9.x, the
    controller will light up when you load a track to a deck.)
13. Continue reading below to know how everything is mapped

Direct deck output implications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setup uses direct deck outputs because mixing takes place in the
VMS4 hardware. The down side to this is that you won’t be able to use
Mixxx features that play to Master or Cue buses like the Preview Deck or
Samplers. Using these features with a hardware + MIDI mixer like the
VMS4 is not really feasible unless you used a separate sound interface
or controlled Mixxx’s internal mixer another way.

Control
-------

This guide explains how the VMS4 is mapped by default in Mixxx.

**Easy customization:** We have provided the following customization
variables at the top of the script you can set to your liking:

1. **RateRanges**: Set the pitch slider range each time you toggle it
   with Shift+Sync.

Just open the ``midi/American-Audio-VMS4-scripts.js`` file in your
favorite text editor (Wordpad works too) and you’ll see these variables
right near the top. Edit & save, then restart Mixxx and enjoy.

Deck controls
-------------

.. note::
   There are a number of different face plates in the wild so
   these images and control descriptions may not exactly match yours. The
   locations of the controls are the key things to pay attention to.

*The controls are the same on both sides of the controller. The left
side controls Deck 1 and the right side controls Deck 2.*

-  **Sync/Range** button - Changes the BPM of this deck to match that of
   the other. When shifted, toggles the pitch slider range. (See top of
   page to customize.)
-  **Hot cue buttons** - Press to set or recall a hot cue. The buttons
   light up red when one is set.
   Hold Shift and press to access hot cues 5-8. (The buttons
   light up blue for these.) Hold Vinyl and press to delete the cue.
   (Note: there is a bug in some firmware versions that causes hot cues
   5 and 6 to be deleted simultaneously.)
   the cue.
-  **Pitch Bend +/-**
-  Momentarily speeds up or slows down the deck while the button is held
   down.
-  Hold Shift and press to adjust the key (pitch) of the song (independent of the tempo.)
-  **Loop In** - Set the in point of a loop
-  **Loop Out** - Set the out point of a loop
-  **Reloop** - Toggle a previously-set loop. Lights red when a loop is
   active.
-  **Loop/Smart** Start a 4-beat loop. Hold Shift and press to toggle
   quantization (locking to the nearest beat.)
-  **Vinyl/Keylock** - *(Does nothing on its own when un-shifted at the
   moment.)* When shifted, toggles key lock.
-  **<< Search/ /2** - Fast-rewind
   Hold Shift and press to halve the current loop length
-  **Search >>/ \*2** - Fast-forward
   Hold Shift and press to double the current loop length
-  **Touch strip**
   Scroll through the respective Library panes. (Left for the
   folders/crates list, right for the track list.)
    - Hold Shift and touch:
         - to affect the Dry/Wet knob on the respective effect unit while the deck is playing
         - for Needle drop - search through the track while the deck is stopped
-  **Wheel**
   Move the wheel while touching the top to scratch the current track like a vinyl record
   Move the wheel without touching the top (so on the sides) to perform a temporary pitch bend
-  **CUE** - Operates according to the Cue mode set in Mixxx's preferences
   Hold Shift and press to play immediately from the cue point (known as Cue+Play or CUP.)
-  **Play** - Press to toggle deck playback
   Hold Shift and press to set this deck as the master for syncing with another
-  **Pause** - Stops the deck playback

Effects section
~~~~~~~~~~~~~~~

The left side controls effect unit 1 and the right side controls effect
unit 2.

-  **Select knob**
  -  Rotate to choose the effect chain preset
  -  Press to toggle whether the effect unit is on or not
-  **Control knob**
  -  Adjusts the wet/dry ratio
  -  When Parameter is on, this becomes the Wonder Knob, adjusting all
     effect parameters at once
-  **On/Off** - Toggles the effect for the deck matching the effect unit
   number
-  **Parameter** - Toggles what the above Control knob adjusts

Sample section
~~~~~~~~~~~~~~

The left side of the controller controls Sampler 1, and the right,
Sampler 2.

-  **Select knob**
   Rotate to move the highlight in the library.
   Press to load the currently highlighted track into the sampler.
   Hold Shift and press to eject the current track from the sampler
   (when the sampler is not playing.)
-  **Volume knob** - Adjusts the volume of the sampler
-  **Play**
   Press to play the sample from the beginning. Press while playing for
   a stutter-play effect (play again from the beginning.)
   Hold Shift and press to stop playing.
-  **Rec** - *Currently does nothing*

Mixer controls
--------------

The volume sliders don’t control the ones in Mixxx because direct Deck
outputs are affected by Mixxx’s internal ones.

-  **Midilog 1** - This strip controls Deck 3/C
-  **Midilog 2** - This strip controls Deck 1/A
-  **Midilog 3** - This strip controls Deck 2/B
-  **Midilog 4** - This strip controls Deck 4/D
