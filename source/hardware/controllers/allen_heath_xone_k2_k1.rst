.. _allen-heath-xone-k2:

Allen & Heath Xone:K2
=====================

The Allen & Heath Xone:K2 is a flexible controller that is mapped to
control Mixxx’s decks, effects, or both. It has an integrated 4 channel
audio interface with 2 RCA jacks and an 1/8" stereo headphone jack. The
Xone K1 is the same as the Xone K2 but without the built in audio
interface and does not come with the EVA travel case that the K2 comes
with.

-  `Manufacturer’s product page <http://www.allen-heath.com/ahproducts/xonek2/>`__
-  `Forum thread <https://mixxx.discourse.group/t/allen-heath-xone-k2/12506>`__
-  `Manufacturer’s User Guide <http://www.allen-heath.com/media/Xone+K2_UG_AP8509_2.pdf>`__
-  `Blank template diagrams <http://www.allen-heath.com/media/Xone+K2+Blank+Overlays.zip>`__

.. versionadded:: 1.11

Audio Setup
-----------

The Xone:K2 is setup in Mixxx > Preferences > Sound Hardware > Output

========== ======= =============
Output     Device  Channel
========== ======= =============
Master     XONE:K2 Channel 3 - 4
Headphones XONE:K2 Channel 1 - 2
========== ======= =============

Note: This Channel setup is the opposite of what most DJ controllers
with an integrated audio interface use. The design choice to not use
Channel 1 - 2 for Master Output is known to cause problems, when users
want to use the Xone:K2 as default system audio output as the operating
system will always use Channel 1 - 2. Thus system audio will go to the
headphones.

There are no hardware controls for the volume so they are always at max
volume. Adjusting the volume of master and headphone outputs is done by
adjusting the gain for those outputs in Mixxx using the controller
mapping.

Setup
-----

**Requirement**: The Xone K2 must have Latching Layers turned off, which
is the default. Refer to the `Xone K2
manual <https://allen-heath.com/media/Xone+K2_UG_AP8509_2.pdf>`__ page
12 for details. The K1 does not have Latching Layers.

This mapping can used with one or multiple Xone K2s/K1s. Multiple Xone
K2s/K1s can be connected to each other via X-Link with one of them
connected to the computer via USB. Alternatively, when using 2 K2s/K1s,
they can both be connected with their own USB cable and this same
mapping can be loaded for each.

The layout of the mapping depends on the configured MIDI channel of the
controller. Change the MIDI channel of the controller by pressing the
bottom right encoder (labeled “Power On Setup/Scroll/Set”) while
plugging in the controller. Scroll with the encoder to select a MIDI
channel. The letter in parentheses corresponds to the last lit button
when selecting the channel:

-  Channel 15 (O, default out of the box): two decks + two effect units
   with decks in the middle
-  Channel 14 (N): two decks + two effect units with effect units in the
   middle
-  Channel 13 (M): two decks + two effect units with decks on left
-  Channel 12 (L): two decks + two effect units with decks on right
-  Channel 11 (K): four decks ordered 3 1 2 4
-  Channel 10 (J): four decks ordered 1 2 3 4
-  Channel 9 (I): four effect units ordered 3 1 2 4
-  Channel 8 (H): four effect units ordered 1 2 3 4

Global Controls
---------------

These are available on any configuration with decks, but not the 4
effect unit layout.

-  Bottom left encoder:
-  adjust tempo of all decks with sync enabled
-  press and turn: PFL/master mix in headphones
-  shift: headphone gain
-  press with shift: toggle split cue mode
-  Bottom right encoder
-  scroll through tracks in library
-  press and release: load selected track into first stopped deck
-  press and hold: load selected track into a deck by pressing the play
   button of the deck
-  shift: master gain

Decks
-----

The bottom right button is the shift button. The bottom left button
toggles the bottom button grid between a loop layer (amber) and a hotcue
layer (red). Holding shift then holding the bottom left layer button at
the same time activates supershift mode.

-  Top encoder: jog

   -  shift: gain
   -  supershift: adjust key

-  Top encoder press: reset gain

   -  shift: master sync
   -  supershift: reset key

-  Knobs: high/mid/low equalizer knobs
-  Top button 1: headphones/PFL

   -  shift: reset tempo
   -  supershift: set beatgrid to current position

-  Top button 2: cue

   -  shift: go to beginning of track and stop
   -  supershift: keylock

-  Top button 3: play

   -  shift: reverse
   -  supershift: quantize

-  Fader: volume
-  Bottom buttons (intro/outro cue layer, amber): Intro/outro cues from
   top to bottom are ordered: - Intro start - Intro end - Outro start -
   Outro end

   -  press: jump to that cue or sets it if it is not set
   -  shift: seek forward/back. The top two (intro) buttons seek
      quickly; the bottom two (outro) seek slowly
   -  supershift: delete cue

-  Bottom buttons (hotcue layer, red): Hotcues are ordered 1-4 from top
   to bottom

   -  press: jump to that hotcue or sets it if it is not set
   -  shift: seek forward/back. The top two buttons seek quickly; the
      bottom two seek slowly
   -  supershift: delete hotcue

-  Bottom buttons (loop layer, green):
-  Bottom button 1 (red): reloop/disable loop

   -  shift: jump to to beginning of loop, stop playback, and activate
      loop
   -  supershift: set loop in point. Hold to move loop in point with
      play position.

-  Bottom button 2 (green): activate loop of selected size

   -  shift: activate rolling loop of selected size
   -  supershift: set loop out point. Hold to move loop out point with
      play position.

-  Bottom button 3 (amber): double loop size

   -  shift: beatjump forward by selected size if no loop is enabled. If
      loop is enabled, move the loop forward by the beatjump size.
   -  supershift: double beatjump size

-  Bottom button 4 (amber): halve loop size

   -  shift: beatjump backward by selected size if no loop is enabled.
      If loop is enabled, move the loop backward by the beatjump size.
   -  supershift: halve beatjump size

Effects
-------

The top part of the column uses the `Standard Effects
Mapping <https://github.com/mixxxdj/mixxx/wiki/Standard-Effects-Mapping>`_.
Pressing the top encoder acts
as the effect focus button. When no effect is focused, the buttons are
red. When holding the top encoder to choose an effect to focus, the
buttons are green. When an effect is focused, the buttons are amber.

The fader acts as the mix knob.

The bottom buttons assign the effect unit to different input channels
and light up red. On the two deck layouts, from top to bottom, they
assign the effect unit to deck 1, deck 2, master mix, and headphones. On
the four effect unit layouts, they assign the effect unit to decks 1-4
going down the column. You can look down a column to see which decks an
effect unit is assigned. You can look across a row to see which effect
units are assigned to a deck. When shift is pressed, the bottom two
buttons switch to controlling the routing buttons for the master and
headphones channels and light up amber.

The bottom encoders are not mapped in the 4 effect unit layout.

Effect unit focusing
~~~~~~~~~~~~~~~~~~~~

In addition to focusing one effect in a unit at a time with the
`Standard Effects Mapping <https://github.com/mixxxdj/mixxx/wiki/Standard-Effects-Mapping>`_, the Xone
K2/K1 has another mode for focusing a whole effect unit. This allows for
controlling the parameters of all 3 effects in the unit at a time. This
mode is only available on the 4 effect unit layouts. To access it, press
the Layer button in the bottom left. Press one of the top encoders to
choose which effect unit to focus.

In this mode, each horizontal row of knobs and buttons controls one
effect. The knobs control the parameters of the effects. Turning any of
the knobs with shift loads different effects. The button in the leftmost
column controls the enable button of the effect and turns amber when it
is on. The rest of the buttons control the button parameters of the
effect and turn green when active (not all effects have button
parameters). The faders still control the dry/wet knobs and the bottom
button grid still controls the routing buttons.

To get back to controlling all 4 effect units, press the Layer button
again. The next time Layer is pressed, the effect unit that was focused
before will be remembered (but it will not be remembered after
restarting Mixxx).

Troubleshooting
---------------

If general functionality or supershift are not working, double check
that Latch Layers is turned off and MIDI CH is selected. Refer to the
`Xone K2
manual <https://allen-heath.com/media/Xone+K2_UG_AP8509_2.pdf>`__ page
12 for details.

Known Issues
------------

There are a few known issues with the Xone K2/K1 firmware:

-  Since there is no way for Mixxx to ask the controller about the positions of
   all the knobs and faders when Mixxx starts, they are out of sync with the
   state of Mixxx until they are first moved.
-  When the USB connection is interrupted and the controller stays powered on,
   such as leaving the controller plugged into a powered USB hub and
   disconnecting the hub from the computer, the controller will not send MIDI
   input until it is powered down (unplugged) and plugged back in.

If you would like these issues to be fixed, please let `Allen & Heath
Support <https://www.allen-heath.com/support/>`__ know.
