Native Instruments Traktor Kontrol S2 MK2
=========================================

The Native Instruments Traktor Kontrol S2 MK2 is a 2 deck all-in-one
controller with an integrated audio interface. It has a pair of balanced
1/4" TRS outputs and a pair of unbalanced RCA outputs which both output
the main mix, a 1/4" TRS headphone jack, and a 1/4" TRS microphone
input. The microphone input is digitized and available to the computer
for recording and broadcasting. The Kontrol S2 MK2 can run with only USB
bus power and an optional power supply can be connected to make the LEDs
brighter and the headphone output louder.

The Kontrol S2 MK2 can be distinguished from the Mk1 by the jog wheels.
The top of the jog wheels on the MK2 are shiny aluminum; the top of the
jog wheels on the Mk1 are black. The Kontrol S2 Mk3 does not have
effects knobs at the top.

Compatibility
-------------

The Kontrol S2 MK2 is a USB audio and HID class compliant device. It is
fully compatible with Linux, Windows, and macOS. No proprietary driver
is required on Linux or macOS. For Windows, download and install the
latest driver from `Native Instruments’
website <https://www.native-instruments.com/en/support/downloads/drivers-other-files/>`__.

Audio routing
-------------

========== ====================== =============
Output     Device                 Channels
========== ====================== =============
Master     Traktor Kontrol S2 MK2 Channel 1 - 2
Headphones Traktor Kontrol S2 MK2 Channel 3 - 4
========== ====================== =============

============ ====================== =============
Input        Device                 Channels
============ ====================== =============
Microphone 1 Traktor Kontrol S2 MK2 Channel 1 - 2
============ ====================== =============

Do *not* configure the Record/Broadcast input in Mixxx.

Mapping
-------

Decks
~~~~~

Jog wheels
^^^^^^^^^^

Touch the top of the jog wheel and turn it to scratch. Move the jog
wheel from the edge without touching the top to nudge the track. Hold
shift and spin the jog wheel to seek quickly.

Loop section
^^^^^^^^^^^^

The encoders work differently in Mixxx than in Traktor: - **Left
encoder**: Turning jumps forward/backwards by the beatjump size. If a
loop is enabled, turning moves the loop by the beatjump size. Push and
turn to adjust the beatjump size. Turning with shift adjusts the musical
key. Pushing with shift resets the key to the track’s default. - **Right
encoder**: Turning halves/doubles the loop size. Turning with shift
beatjumps by 1 beat forward/backward, or if a loop is enabled, moves the
loop 1 beat forward/backward. Pushing (de)activates a loop. Pushing with
shift reactivates a disabled loop, or if a loop is enabled, jumps to the
loop in point and stops the deck. - **In & Out buttons**: Manually set
the loop in and out points. Press and hold while moving the jog wheel to
adjust the loop in or out point.

Top pad row
~~~~~~~~~~~

The top pad row has 3 different modes. - **Hotcue mode**: This is the
default mode when Mixxx starts. The pads control hotcues 1-4. The color
of the hotcues is shown on the pads. Press an unlit button to set a new
hotcue. Press a lit pad to seek to the hotcue. Press a lit pad with
shift to delete the hotcue. - **Intro & Outro cue mode**: This mode is
activated by pressing the flux button above the tempo fader. Pads 1 & 2
are used for the intro start & end cues and light up green. Pads 3 & 4
are used for the outro start & end cues and light up red. - **Sampler
mode**: This mode is activated by the button under the Remix knob in the
center of the mixer. Press an unlit pad to load the selected track in
the library to the sampler. Loaded and stopped sampler pads are lit
white. Press a white pad play a sampler. A playing sampler is lit
magenta. Press a lit pad with shift to stop a sampler, or if it is
already stopped, unload the sample.

Transport pad row
^^^^^^^^^^^^^^^^^

The bottom pad row works as labelled on the controller: - **Sync**:
Press to sync tempo. Press and hold to enable sync lock. Press again to
disable sync lock. Press with shift to enable sync lock without needing
to hold. - **Cue**: Behavior depends on the `cue mode set in the Mixxx
preferences <https://mixxx.org/manual/latest/en/chapters/user_interface.html#using-cue-modes>`__.
Press with shift to seek the beginning of the track and stop. -
**Play**: Play or pause the deck. Press with shift to toggle keylock.

Tempo fader
^^^^^^^^^^^

Adjusts the tempo.

Flux button
^^^^^^^^^^^

Mixxx `does not yet have a very useful flux/slip
mode <https://bugs.launchpad.net/mixxx/+bug/1475303>`__, so instead this
button toggles the top pad row to the intro/outro cues. Press the button
when it is lit to return the top pad row to hotcue mode.

When slip mode is implemented in Mixxx in the future, this could be
changed so shift + flux button activates intro & outro mode for the
pads.

Mixer
~~~~~

Deck columns
^^^^^^^^^^^^

-  **Top encoder**: Controls the QuickEffect superknob for the deck.
   With shift, controls gain. Press to reset the QuickEffect superknob.
   Press with shift to reset gain. Press and turn to change the effect
   chain preset loaded to the QuickEffect chain (new in Mixxx 2.4).
-  **FX routing buttons**: Assign the deck to effects units 1 and 2.
-  **EQ knobs**: Adjust the high, middle, and low frequencies.
-  **Cue button**: Toggle whether the deck is routed to the prefader
   headphone output. With shift, toggle quantize for the deck.
-  **Fader**: Control the deck volume

Center column
^^^^^^^^^^^^^

-  **Main volume knob**: Adjust the volume of the main output. This acts
   on the controller’s audio interface output in hardware, so it is not
   mapped to the main mix gain knob in Mixxx (otherwise the gain would
   be applied twice).
-  **Remix knob**: Adjusts the gain of samplers 1-8.
-  **Remix buttons**: Toggles the top pad row of the corresponding deck
   to control samplers. Press when lit to return the pads to controlling
   hotcues.
-  **Browse encoder**: Scroll through the music library. Push to
   maximize the library browser on screen. Turn with shift to scroll 5
   rows at a time.
-  **Load buttons**: Load the track selected in the library to the
   corresponding deck. Press with shift to unload a track.
-  **Meters**: The meters show the levels for each deck.
-  **Crossfader**: Crossfade between the decks.

Effects
~~~~~~~

The Kontrol S2 MK2 uses the `standard Mixxx effects
mapping <https://github.com/mixxxdj/mixxx/wiki/standard-effects-mapping>`__.

Front panel
~~~~~~~~~~~

The cue volume knob adjusts the volume of the controller’s audio
interface in hardware, so it is not mapped to Mixxx (otherwise the gain
would be applied twice). The cue mix knob is mapped to Mixxx. The Mic
Engage button toggles talkover for Microphone Input 1 in Mixxx.
