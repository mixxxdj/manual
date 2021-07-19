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
The top of the jog wheels on the Mk1 are black; The top of the jog wheels
on the MK2 are shiny aluminum; The Kontrol S2 Mk3 does not have
effects knobs at the top.

.. versionadded:: 2.3.1

Compatibility
-------------

The Kontrol S2 MK1 is a USB audio and HID class compliant device. It is
fully compatible with Linux, Windows, and macOS. No proprietary driver
is required on Linux or macOS. For Windows, download and install the
latest driver from `Native Instruments’
website <https://www.native-instruments.com/en/support/downloads/drivers-other-files/>`__.

Audio routing
-------------

========================  =======================
Output                    Channels
========================  =======================
:guilabel:`Master`        Channel 1 - 2
:guilabel:`Headphones`    Channel 3 - 4
========================  =======================

The microphone is routed internally and is not accessible to Mixxx.

Mapping
-------

Decks
~~~~~

Jog Wheels
^^^^^^^^^^

Touch the top of the jog wheel and turn it to scratch. Move the jog
wheel from the edge without touching the top to nudge the track. Hold
:hwlabel:`SHIFT` and spin the jog wheel to seek quickly.

Loop Section
^^^^^^^^^^^^

The encoders work differently in Mixxx than in Traktor:

Left encoder
    Turning jumps forward/backwards by the beatjump size.
    If a loop is enabled, turning moves the loop by the beatjump size.
    Push and turn to adjust the beatjump size.
    Turning with :hwlabel:`SHIFT` adjusts the musical key.
    Pushing with :hwlabel:`SHIFT` resets the key to the track’s default.
Right encoder
    Turning halves/doubles the loop size.
    Turning with :hwlabel:`SHIFT` beatjumps by 1 beat forward/backward, or if a loop is enabled, moves the loop 1 beat forward/backward.
    Pushing (de)activates a loop. Pushing with :hwlabel:`SHIFT` reactivates a disabled loop, or if a loop is enabled, jumps to the loop in point and stops the deck.
:hwlabel:`LOOP IN`/:hwlabel:`LOOP OUT` buttons
    Manually set the loop in and out points.
    Press and hold while moving the jog wheel to adjust the loop in or out point.

Top Pad Row
~~~~~~~~~~~

The top pad row has 3 different modes.

Hotcue mode
    This is the default mode when Mixxx starts.
    The pads control hotcues 1-4.
    Active hotcues light up blue.
    Press an unlit button to set a new :term:`hotcue`.
    Press a lit pad to seek to the hotcue.
    Press a lit pad with :hwlabel:`SHIFT` to delete the hotcue.
Intro & Outro cue mode
    This mode is activated by pressing the :hwlabel:`RESET` button above the tempo fader.
    Pads 1 & 2 are used for the intro start & end cues and light up green.
    Pads 3 & 4 are used for the outro start & end cues and light up blue.
Sampler mode
    This mode is activated by the button under the Sampler knob in the center of the mixer.
    Press an unlit pad to load the selected track in the library to the sampler.
    Loaded and stopped sampler pads are lit dimm green.
    Press a dimm green pad to play a sampler.
    A playing sampler is lit green.
    Press a lit pad with :hwlabel:`SHIFT` to stop a sampler, or if it is already stopped, unload the
    sample.
    Looping sampler pads are lit cyan.

Transport Controls
^^^^^^^^^^^^^^^^^^

The transport controls work mostly as labelled on the controller:

:hwlabel:`SYNC` button
    Press to :term:`sync` :term:`tempo`.
    Press and hold to enable sync lock.
    Press again to disable sync lock.
    Press with :hwlabel:`SHIFT` to enable sync lock without needing to hold.
:hwlabel:`CUE` button
    Behavior depends on the :ref:`cue mode set in the Mixxx preferences <interface-cue-modes>`.
    Press with :hwlabel:`SHIFT` to seek the beginning of the track and stop.
:hwlabel:`PLAY` button
    Play or pause the deck. Press with :hwlabel:`SHIFT` to toggle key lock.
:hwlabel:`TEMPO` fader
    Adjusts the :term:`tempo`.
:hwlabel:`RESET` button
    Mixxx `does not yet have a very useful flux/slip
    mode <https://bugs.launchpad.net/mixxx/+bug/1475303>`__, so instead this
    button toggles the top pad row to the intro/outro cues. Press the button
    when it is lit to return the top pad row to hotcue mode.

    When slip mode is implemented in Mixxx in the future, this could be
    changed so :hwlabel:`SHIFT` + :hwlabel:`RESET` button activates intro & outro mode for the
    pads.

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
    Toggle whether the deck is routed to the :term:`prefader headphone output <PFL>`.
    With :hwlabel:`SHIFT`, toggle quantize for the deck.
Fader
    Control the deck volume.

Center Column
^^^^^^^^^^^^^

:hwlabel:`MAIN LEVEL` knob
    Adjust the volume of the main output.
    This acts on the controller’s audio interface output in hardware,
    so it is not mapped to the main mix gain knob in Mixxx (otherwise the gain would be applied twice).
:hwlabel:`SAMPLES` knob
    Adjusts the gain of samplers 1-8.
:hwlabel:`SAMPLES ON A`/:hwlabel:`SAMPLES ON B` buttons
    Toggles the top pad row of the corresponding deck to control samplers.
    Press when lit to return the pads to controlling :term:`hotcues <hotcue>`.
:hwlabel:`BROWSE` encoder
    Scroll through the music library.
    Push to maximize the library browser on screen.
    Turn with :hwlabel:`SHIFT` to scroll 5 rows at a time.
:hwlabel:`LOAD A`/:hwlabel:`LOAD B` buttons
    Load the track selected in the library to the corresponding deck.
    Press with :hwlabel:`SHIFT` to unload a track.
:hwlabel:`LEVEL` meters
    The meters show the levels for each deck.
Crossfader
    Crossfade between the decks.

Effects
~~~~~~~

The Kontrol S2 MK1 uses the `standard Mixxx effects
mapping <https://github.com/mixxxdj/mixxx/wiki/standard-effects-mapping>`__.

Front panel
~~~~~~~~~~~

The cue volume knob adjusts the volume of the controller’s audio
interface in hardware, so it is not mapped to Mixxx (otherwise the gain
would be applied twice). The cue mix knob is mapped to Mixxx. The Mic
Engage button toggles talkover for Microphone Input 1 in hardware.
