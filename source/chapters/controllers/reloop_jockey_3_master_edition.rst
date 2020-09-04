Reloop Jockey 3 Master Edition
==============================

The Reloop Jockey 3 Master Edition is a 2 Channel Controller with the option to
control 4 Channels. It has a built-in sound card with 6 channels in and 4
channels out. It features both balanced 1/4" and unbalanced RCA master outputs
plus RCA booth outputs with an independent volume control. It can also be used
as a stand-alone mixer, or used to mix an analog source with music files in
Mixxx. This device requires a power adapter in addition to the USB cable. This
device is not USB MIDI class compliant. Its signals are translated to MIDI by
special drivers on Windows and macOS. *There is no driver available for Linux.*

-  `Mixxx Forum Thread <http://mixxx.org/forums/viewtopic.php?f=7&t=5418>`__
-  `Manufacturer’s product page <http://www.reloop.com/reloop-jockey-3-me>`__
-  `Manufacturer’s manual <http://www.reloop.com/media/catalog/product/pdf/2/2/4/224649_Reloop_IM.pdf>`__
-  `Review from Digitaldjtips.com <http://www.digitaldjtips.com/2011/05/review-video-reloop-jockey-iii-me-controller/2/>`__

Setup
-----

The Mixxx mapping uses the same settings as Reloop’s Traktor mapping. Leave the
MIDI channels as the default 1-4. If you have problems with the jogwheels, set
the jogwheel resolution to 2048. (Please read the manual of this Controller
section **5.1** and **5.1.2**)

Set the Input 1 and Input 2 switches on the front side of the Jockey 3 ME to SW.

Mixxx Sound Hardware Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Master output: channels 1-2
-  Headphone output: channels 3-4
-  Auxiliary or vinyl input 1: channels 1-2
-  Auxiliary or vinyl input 2: channels 3-4
-  Microphone input: channels 5-6

Mapping Description
-------------------

Mixer Section
~~~~~~~~~~~~~

-  **Trax encoder**: scroll through library. With shift, scroll through sections
   on the left side of the library. Push to toggle big library.
-  **Load button**: load selected track into active deck
-  **Deck switches**: select between controlling deck 1/3 or analog input 1 on
   the left; select between controlling deck 2/4 or analog input 2 on the right.
   Note that the analog inputs are only affected by the mixer controls but not
   the other deck controls.
-  **Gain**: set `deck
   gain <http://mixxx.org/manual/latest/chapters/user_interface.html#equalizers-and-gain-knobs>`__
-  **High/mid/low**: adjust EQ for high/mid/low frequencies
-  **Master/booth/phones**: control the Jockey 3 ME’s sound card. These knobs do
   not send MIDI messages or adjust values in Mixxx, so turning them will not
   change anything on screen. Use these but not the software knobs on screen in
   Mixxx (see `the Mixxx
   manual <http://mixxx.org/manual/latest/chapters/user_interface.html#interface-gain-knob>`__
   for an explanation).
-  **Headphones**: play deck on headphone output
-  **Cuemix**: Fade between PFL and master output on headphones
-  **Vertical faders**: deck volume
-  **Level meter LEDs**: show the level of the deck
-  **Crossfader**: fade between decks
-  **Crossfader curve** (front side of controller): Adjust crossfader curve
   between fade and cut.

Transport Section
~~~~~~~~~~~~~~~~~

-  **Play/pause**: play/pause or, with shift, toggle keylock
-  **Cue**: behavior depends on `cue mode set in Mixxx
   preferences <http://mixxx.org/manual/latest/chapters/user_interface.html#interface-cue-modes>`__.
   With shift, it does not work as labeled; it toggles quantize.
-  **Cup**: Like Cue, but it plays only after releasing the button.
-  **Sync**: toggle master sync. With shift, it does not work as labeled; it
   toggles microphone talkover.

Jogwheels
~~~~~~~~~

Set the jog wheel mode by pressing one of the 4 buttons beside the jog wheel,
below the trash and 5-8 buttons.

-  **Off**: By default, all mode buttons are off. In this default mode, moving
   the jogwheel temporarily bends the pitch, regardless of whether it is moved
   from the top or the side.
-  **Scratch**: Move the wheel from the top to scratch. Touch the outside rubber
   ring to temporarily bend the pitch.
-  **Pitch bend**: Move the wheel to control the SuperKnob on EffectUnit of this
   Deck. FIXME (Maybe a Touch Control?)
-  **Search**: Search position in file quickly. Touch stops the Deck.
-  **Trax**: Not Mapped. FIXME (No Plans)

Hotcue Section
~~~~~~~~~~~~~~

Press an unlit hotcue button to set that hotcue at the current position. Press a
lit hotcue button to jump to that hotcue. To delete a hotcue, hold the Trash
button while pressing a hotcue. To toggle between hotcues 1-4 and 5-8, press the
5-8 button.

Loop Section
~~~~~~~~~~~~

-  **Length encoder**: Press to activate a 4 beat loop. Double or half the beats
   of the loop by turning
-  **Move encoder**: Move a track 4 Beats forward or backward. Push, hold and
   Turn it to halve or double the value of 4 Beats.
-  **Loop button**: Turn on/off a Loop that is set from Length encoder. With
   shift, sets the start position of a loop.
-  **Reloop button**: Repeat the entire file. With shift, sets the end position
   of a loop.

Other controls
~~~~~~~~~~~~~~

-  **Filter**: turn to apply a highpass or lowpass filter. On Deck A, press
   Shift and turn Filter to adjust the Gain of the Microphone
-  **Pan**: On Deck A, turn to fade between the left and right speakers on the
   master output. (Balance)
-  **< Beat**: Beatjump by one beat back. With shift, moves the beatgrid lines
   further from each other (lower BPM by 0.01)
-  **Beat >**: Beatjump by one beat forward. With shift, moves beatgrid lines
   closer to each other (raise BPM by 0.01)
-  **Pitch fader**: adjust playback rate of deck (with keylock, only adjusts
   tempo and not pitch)
-  **+/-**: Pitch temporarily faster or slower.
-  **FX 1**: Shift - (Minus) does not function as labeled. It aligns the
   beatgrid with the current play position.

Effect Section
~~~~~~~~~~~~~~

The effect section controls the effect chain with the same number as the deck
selected by the deck switch, although any effect chain can be applied to any
deck.

-  **Dry/wet**: adjust how much the effect is applied. With shift, turn to
   select different effect chain presets
-  **FX Param**: adjust effect parameters 1-3 for the first effect in the chain.
-  **Press FX Param 1-3 + Shift**: edit how effect parameters are linked to the
   superknob. The effect selected corresponds to the number of the FX Param
   encoder pressed. For example, pressing FX Param 2 with shift on deck 3 edits
   Effect2 of the EffectRack3. Each encoder press with shift changes what is
   being edited:

   -  Select which effect parameter to edit
   -  Select a [[effects framework#linking values|superknob link type between 0
      and 4]] for the parameter selected on the first press
   -  Select whether the [[effects framework#linking values|superknob link is
      inverted]] for the parameter selected on the first press
   -  Close superknob link editing mode

-  **FX on**: enable/disable effect chain
-  **FX B1/2/3**: enable/disable effect 1/2/3 on this chain
-  **Preset 1-4** (shift+effect buttons): apply effect chain to that deck number
