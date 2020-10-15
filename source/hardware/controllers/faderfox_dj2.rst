FaderFox DJ2
============

-  `Manufacturer’s product page <http://www.faderfox.de/dj2.html>`__

.. versionadded:: 1.6

Setting up the controller
-------------------------

In order for this mapping to work, you will need to use these settings.
First, enter *System Mode* by pressing the two black buttons in the top
right encoder section. There is a vertical *System* label next to these
two buttons. The orange *Sys/Mon* LED in the center bottom should be on
and not blinking.

You can now modify various settings by pressing each of the 4 black
buttons of the encoder section. There are two possible settings for each
function, *On* or *Off*, depending which of the corresponding LED is
lit. There is also a brief explanation of these settings on a gray
sticker in the back of the controller.

-  The top left button controls the *Auto Switch* function. If the
   *Seek/Scratch* green LED, is on, the function is off. If the
   *List/load* red LED is on, the function is on. If the *Auto Switch*
   function is on, the encoder will switch to *Seek/Scratch* after
   pressing the encoder to load a track. This function is up to the
   user’s preference and will not affect the mapping.
-  **The bottom left button must be set to the Gain green LED for this
   mapping to work**. If set to the red *Pitch* LED, the transport
   buttons will have different CC numbers. This is useful if you own a
   second controller which already has transport functions.
-  **The top right button must be set to the Seek/Scratch green LED.**
   If set to the *List/Load* red LED, the *Auto Play* function will be
   on, meaning that loading a track from the *List/load* encoder will
   trigger playback. You don’t want this function on since it will
   conflict with the play button of the transport section which would
   have the same CC number.
-  **The bottom right button must be set to the Gain green LED.** If set
   to the red LED, the joystick will have different CC numbers, and its
   mapping won’t work properly.
-  If the green *FX1* LED is on, the controller’s will use MIDI channel
   1, and channel 16 if the *FX2* LED is on. This is useful if you want
   to control four decks using two FaderFox DJ2 controllers. If you use
   only one controller, leave this setting to *FX1*. To change the
   setting, press the *Shift* button and the lower left black button of
   the encoder section for channel 1, or the lower right black button of
   the encoder section for channel 16.

*Important* : changes to your settings won’t be saved if you just turn
off the controller on *System Mode*. To save the settings, exit *System
Mode* by pressing again the two black buttons of the left encoder
section.

Encoders Section
----------------

The two encoders on top of the controller control various parameters.
They can of course be turned but also act as push buttons. You can
select which function is used for each of the encoders by pushing the
black buttons of the encoders section. LEDs indicate which function is
currently selected.

-  *List/Load* (top red LED is on) lets you browse your playlist. Push
   the left encoder to load the highlighted track into Deck A or the
   right encoder for Deck B.
-  *Seek/Scratch* (top green LED is on) acts as a jogwheel. Turn the
   left encoder for Deck A or the right encoder for Deck B. Pushing the
   encoder on that setting will activate *Sync* on that deck.
-  *Gain* (bottom green LED is on) controls the gain of the channel.
   Pushing the encoder on that setting will mute the track.
-  *Pitch* (bottom red LED is on) controls the tempo of the deck.
   Unfortunately there is no MIDI CC number emitted when pushing the
   encoder on that position.

Joystick
--------

The joystick can be set to control either the first or the second unit
of the effect rack. To control the first effect unit, press *Shift* +
the lower black button of the left encoder section (*FX1* green LED is
on). To control the second effect unit, press *Shift* + the lower black
button of the right encoder section (*FX2* green LED is on).

The horizontal axis of the joystick controls the *Mix* knob of the
effect unit. The vertical axis control the *Super Knob* of the unit.

Mixer Section
-------------

-  Using the knobs and faders should be straightforward as the controls
   follow the labels printed on the controller.
-  The *Cue Mix* knob controls the headphone mix. The *Cue A* and *Cue
   B* are used to pre-listen the selected deck.
-  The green *FX ctrl* buttons are used to activate a desired effect
   unit on the selected deck.
-  the left green button enables effect unit 1 on that deck
-  the right green button enables effect unit 2 on that deck
-  *Shift* + left green button enables effect unit 3 on that deck
-  *Shift* + right green button enables fx unit 4 on that deck
-  The *Kill* button controls Low Kill and *Shift + Kill* controls High
   Kill. To use Mid Kill, press *Shift* + *Cue A* (Deck A) or *Shift* +
   *Cue B* (Deck B)

Transport Section
-----------------

The left transport section controls Deck A transport functions, and the
right transport section those of Deck B.

-  The top left gray button (labeled with a pause symbol) of each
   section controls the *Align beatgrid to current playposition*
   function. *Shift* + this button controls the *Quantize* function.
-  The top right gray button (without any label) controls the *Keylock*.
   *Shift* + this button controls the *Reverse* function.
-  The bottom left gray button (Play/pause label) controls *Play*.
   *Shift* + this button will make the playback jump one beat backward
   on this deck.
-  The bottom right gray button (play label) controls *Cue* (depending
   on the settings in Mixxx’s preferences). *Shift* + this button will
   make the playback jump one beat forward on this deck.
-  The top blue button holds down the speed (temporary pitch bend) and
   the bottom blue button holds the speed up according to the labels on
   the controller. Pressing *Shift* + these blue buttons will act
   similarly but with a smaller pitch bending.
