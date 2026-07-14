Native Instruments Traktor Kontrol S2 MK1
=========================================

The Native Instruments Traktor Kontrol S2 MK1 is a 2 deck all-in-one
controller with an integrated audio interface. It has a pair of balanced
1/4" TRS outputs and a pair of unbalanced RCA outputs which both output
the main mix, a 1/4" TRS headphone jack, and a 1/4" TRS microphone
input. The microphone input is not digitized and routed internally
to the outputs. The Kontrol S2 MK1 can run with only USB
bus power and an optional power supply can be connected to make the LEDs
brighter and the headphone output louder.

The Kontrol S2 MK1 can be distinguished from the Mk2 by the jog wheels.
The S2 MK1 has pressure sensitive jog wheels made of black plastic,
while the S2 MK2 has touch sensitive jog wheels made of shiny aluminium;
The Kontrol S2 MK3 does not have effects knobs at the top.

.. versionadded:: 2.3.4

Compatibility
-------------

The Kontrol S2 MK1 is a :term:`USB` audio and :term:`HID` class compliant
device. It is fully compatible with Linux, Windows, and macOS. No proprietary
driver is required on Linux or macOS. For Windows, download and install the
latest driver from `Native Instruments’ website
<https://www.native-instruments.com/en/support/downloads/drivers-other-files/>`__.

The mapping uses the hardware calibration which is necessary to detect a
jog-wheel press. A calibration might be necessary before first use. This is
possible in the Controller Manager or Traktor from Native Instruments which is
available for Windows and macOS.

Audio routing
-------------

========================  =======================
Output                    Channels
========================  =======================
:guilabel:`Master`        Channel 1 - 2
:guilabel:`Headphones`    Channel 3 - 4
========================  =======================

The microphone is routed internally and is not accessible to Mixxx.

On Windows setting the sound API to ASIO might be necessary.

Mapping
-------

Decks
~~~~~

Jog Wheels
^^^^^^^^^^

Press the top of the jog wheel and turn it to scratch. Move the jog
wheel from the edge without pressing the top to nudge the track. Hold
:hwlabel:`SHIFT` and spin the jog wheel to seek quickly.

Loop Section
^^^^^^^^^^^^

We are going to use the terminology from :ref:`loop controls
<interface-looping>` and :ref:`transport controls <interface-transport>`.

Activate loop
    To beatloop press the right encoder. To reloop hold :hwlabel:`SHIFT` and
    press the right encoder.
    Holding :hwlabel:`SHIFT` and pressing the right encoder when a will pause
    the deck and jump to the start of the loop.
    To set the loop-in marker press :hwlabel:`LOOP IN`.
    If the loop-out marker is set it will also activate the loop right away.
    To set the loop-out marker press :hwlabel:`LOOP OUT`.
    If the loop-in marker is set it will also activate the loop right away.

Deactivate loop
    To deactivate a loop press the right encoder.

Changing beatloop size
    To half or double the beatloop size turn the right encoder.
    The loop-in marker can be moved by pressing or holding :hwlabel:`LOOP IN`.
    The loop-out marker can be moved by pressing or holding :hwlabel:`LOOP OUT`.

Beatjump/Moving loop
    To beatjump by the beatjump size forward/backward turn the left encoder.
    To change the beatjump size press and turn the left encoder.
    To jump one beat forward/backward hold :hwlabel:`SHIFT` and turn the right
    encoder.

Top Pad Row
~~~~~~~~~~~

The top pad row has 3 different modes.

Hotcue mode
    This is the default mode when Mixxx starts.
    This mode is active if the :hwlabel:`SAMPLES` and the :hwlabel:`RESET`
    lights are off.
    The pads control hotcues 1-4.
    Active hotcues light up blue.
    Press an unlit button to set a new :term:`hotcue`.
    When a loop is active it will save the loop instead.
    Press a lit pad to seek to the hotcue or seek and activate the loop.
    Press a lit pad with :hwlabel:`SHIFT` to delete the hotcue or loop.
Intro & Outro cue mode
    This mode is activated by pressing the :hwlabel:`RESET` button above the
    tempo fader.
    This mode is active if the :hwlabel:`RESET` light is on.
    Pads 1 & 2 are used for the intro start & end cues and light up green.
    Pads 3 & 4 are used for the outro start & end cues and light up blue.
Sampler mode
    This mode is activated by the button under the :hwlabel:`SAMPLES` knob in
    the center of the mixer.
    This mode is active if the :hwlabel:`SAMPLES` light is on.
    Press an unlit pad to load the selected track in the library to the sampler.
    Loaded and stopped sampler pads are lit dim green.
    Press a dim green pad to play a sampler.
    A playing sampler is lit green.
    Press a lit pad with :hwlabel:`SHIFT` to stop a sampler, or if it is already
    stopped, unload the sample.
    Looping sampler pads are lit cyan.

Transport Controls
^^^^^^^^^^^^^^^^^^

The transport controls work mostly as labeled on the controller:

:hwlabel:`SYNC` button
    Press to :term:`sync` :term:`tempo`.
    Press and hold to enable sync lock.
    Press again to disable sync lock.
    Press with :hwlabel:`SHIFT` to enable sync lock without needing to hold.
:hwlabel:`CUE` button
    Behavior depends on the :ref:`cue mode set in the Mixxx preferences
    <interface-cue-modes>`.
    Press with :hwlabel:`SHIFT` to seek the beginning of the track and stop.
:hwlabel:`PLAY` button
    Play or pause the deck. Press with :hwlabel:`SHIFT` to toggle key lock.
:hwlabel:`TEMPO` fader
    Adjusts the :term:`tempo`.
:hwlabel:`SHIFT` and left encoder
    Adjusts the :term:`key`.
:hwlabel:`RESET` button
    This does not reset the tempo but rather switch between the intro/outro cues
    and the hot cues.

Mixer
~~~~~

Deck Columns
^^^^^^^^^^^^

:hwlabel:`GAIN` encoder
    Controls the Quick Effect superknob for the deck.
    With :hwlabel:`SHIFT`, controls gain.
    Press to reset the Quick Effect superknob.
    Press with :hwlabel:`SHIFT` to reset gain.
:hwlabel:`FX 1`/:hwlabel:`FX 2` buttons
    Assign the deck to effect units 1 and 2.
:hwlabel:`HI`/:hwlabel:`MID`/:hwlabel:`LOW` knobs
    Adjust the high, middle, and low frequencies.
:hwlabel:`CUE` button
    Toggle whether the deck is routed to the :term:`prefader headphone output
    <PFL>`.
    With :hwlabel:`SHIFT`, toggle quantize for the deck.
Fader
    Control the deck volume.

Center Column
^^^^^^^^^^^^^

:hwlabel:`MAIN LEVEL` knob
    Adjust the volume of the main output.
    This acts on the controller’s audio interface output in hardware, so it is
    not mapped to the main mix gain knob in Mixxx.
:hwlabel:`SAMPLES` knob
    Adjusts the gain of samplers 1-8.
:hwlabel:`SAMPLES ON A`/:hwlabel:`SAMPLES ON B` buttons
    Toggles the top pad row of the corresponding deck to control samplers.
    Press when lit to return the pads to controlling :term:`hotcues <hotcue>`.
:hwlabel:`BROWSE` encoder
    Scroll through the music library.
    Turn with :hwlabel:`SHIFT` to scroll a whole page at a time.
    Push to open/select the highlighted item.
    Push with :hwlabel:`SHIFT` to cycle through the windows (Track List,
    Sidebar, search box).
:hwlabel:`LOAD A`/:hwlabel:`LOAD B` buttons
    Load the track selected in the library to the corresponding deck.
    Press with :hwlabel:`SHIFT` to clone the other deck.
:hwlabel:`LEVEL` meters
    The meters show the levels for each deck.
Crossfader
    Crossfade between the decks.

Effects
~~~~~~~

The Kontrol S2 MK1 uses the :ref:`standard Mixxx effects
mapping <controller-effects-mapping>`.

Front panel
~~~~~~~~~~~

The cue volume knob adjusts the volume of the controller’s audio
interface in hardware, so it is not mapped to Mixxx (otherwise the gain
would be applied twice). The cue mix knob is mapped to Mixxx. The Mic
Engage button toggles talkover for Microphone Input 1 in hardware.
