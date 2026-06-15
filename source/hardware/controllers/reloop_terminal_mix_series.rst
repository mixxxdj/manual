.. _reloop-terminal-mix-series:

Reloop Terminal Mix 2/4
=======================

- `Terminal Mix 2 product page <http://web.archive.org/web/20190916160609/http://www.reloop.com/reloop-terminal-mix-2>`__
- `Terminal Mix 4 product page <https://web.archive.org/web/20190916134709/http://www.reloop.com/reloop-terminal-mix-4>`__

The Reloop Terminal Mix 2 and Terminal Mix 4 use the same mapping in Mixxx.

.. versionadded:: 1.11

Sound hardware
--------------

The Reloop Terminal Mix 2 and Terminal Mix 4 have integrated multichannel sound cards.
Usually, the TerminalMix runs very well with USB power only.
If you experience issues especially when powering both main and booth outputs at high levels you should use the additional power supply (6v/1.5A).
The official manual from Reloop states not to operate the unit at temperatures below 5°C/41°F as it might damage A/D converters and other components.
However, the audio output may already start crackling if the temperature drops below 10°C.

Inputs
~~~~~~

Both TerminalMix 2 and 4 have a microphone and a switchable line/phono input that can be routed into Mixxx.
The Microphone jack is at the front side of the controller, the RCA line jacks are at the back next to the line/phono switch.
For both inputs there is a gain knob and a switch on the controller’s front side that toggles between routing the signal to the computer (:hwlabel:`SW`) or mixing it directly with the main output (:hwlabel:`MST`).
:hwlabel:`MST` allows to play music from external sources without any software, for example while setting up Mixxx software.
Switch to :hwlabel:`SW` if you want to use the line signal for vinyl control or AUX input, or if you want to record the microphone input with Mixxx, broadcast it, or put on effects.

Outputs
~~~~~~~

At the front, there are two headphone jacks (1/8" and 1/4“), both affected by the hard-wired :hwlabel:`TONE` knob.
At the back, there are unbalanced outputs for booth and main (RCA), as well as a balanced main output (1/4”).
The output level of both main outputs, booth and headphone outputs are all controlled by respective hard-wired knobs in the center column which can’t be mapped to software.


.. _reloop-terminal-mix-series-maintenance:

Controller hardware / Maintenance
---------------------------------

The jog wheels’ touch sensitivity can be adjusted separately.
Refer to the `official manual <http://www.reloop.com/media/custom/upload/Reloop-TM4_Factory+JogReset.pdf>`__ for instructions.

When used in dusty environment for a while you might find the MIDI LED flickering although you didn’t touch any of the controls.
This is mostly due to dust/fuzz particles in the ‘comb’ at the jog wheels’ underside that is distracting the IR light barriers that detect platter movement.
Remove the particles with a vacuum cleaner, or blow into the gap between wheel and housing.

After a few years of heavy usage the buttons and sliders may start to wear out.
Then, buttons need to be pressed harder or in a different manner than what was working before, and sliders may send false values when they are actually in the ‘off zone’.
Luckily, the buttons are standard parts and relatively easy to replace, and the sliders’ conductive surface can be cleaned with Q-tips and alcohol.


.. _reloop-terminal-mix-series-options:

Mapping options
---------------

The mapping the following customization variable at the top of the script
you can set to your liking:

- ``pitchRanges``: Set the pitch slider range each time you toggle it.

Just open the :file:`Reloop Terminal Mix 2-4.js` file in your favorite
text editor and you’ll see these variables right near the top. Edit and save and
Mixxx will automatically reload the mapping.


Deck controls
-------------

*The controls are the same on both sides of the controller. The left side
controls Deck 1 or 3 and the right side controls Deck 2 or 4.*

- :hwlabel:`RANGE` button - Toggles the pitch slider range. See :ref:`Mapping Options <reloop-terminal-mix-series-options>`.
- :hwlabel:`KEYLOCK*` button - Toggles key lock.

FX Controls
~~~~~~~~~~~

This mapping uses the :ref:`Standard Effects Mapping <controller-effects-mapping>` to control the FX units.

.. note::
  These knobs and buttons don’t switch to decks 3 and 4.

- :hwlabel:`FX1/2/3` knobs

  - control the Meta knob of each effect
  - focused effect: control the first three knob parameters of the focused effect

- :hwlabel:`ON` buttons

  - Press: toggle the effects
  - Press + hold: temporarily toggle an effect
  - focused effect: control the first three button parameters of the focused effect

- :hwlabel:`BEATS` encoder

  - Turn: adjust the Wet/Dry knob of the effect unit
  - Press repeatedly: adjust the BPM (not the pitch/speed!) of the loaded track
  - :hwlabel:`SHIFT` + Press: move the nearest beat marker to the current play position

- :hwlabel:`TAP` button

  - LED flashes on each beat
  - Press + hold, then press any ON button to focus the respective effect
  - :hwlabel:`SHIFT` + Press: switch between FX units 1/3 (left FX section) and 2/4 (right FX section)

Loop Controls
~~~~~~~~~~~~~

- :hwlabel:`LENGTH` knob

  - Turn: double or halve the current *loop size* (beats) visible in loop size spinbox in each skin.
  - Press: set and activate a loop of *loop size*

- :hwlabel:`SHIFT` + Press: re-activate the previous loop

  - play position behind loop-out: jump to loop-in point and play loop from there
  - play position before loop: activate loop, keep playing and enter loop when play position crosses loop-in marker

- :hwlabel:`IN` / :hwlabel:`1/2x` button

  - Press: set the loop in point, flashes when a loop is active
  - Press + hold: drags the loop in point of an active loop

- :hwlabel:`OUT` / :hwlabel:`2x` button

  - Press: set the loop out point, flashes when a loop is active
  - Press + hold: drags the loop out point of an active loop

- :hwlabel:`MOVE` knob

  - Press + turn: adjust the //beatjump size// visible in beatjump spinbox in each skin
  - Turn with no active loop: jump back or forth in the track by beatjump size
  - Turn with active loop + Quantize OFF: move the loop position by 1/8 beat per detent (helpful to correct the loop in point in case it's set slightly too early or too late)
  - Turn with active loop + Quantize ON: move the loop position by one beat per detent (helpful to correct the loop in point in case it snapped to the wrong beat marker)
  - :hwlabel:`SHIFT` + turn with active loop: shift the loop back or forth by beatjump size

Hot cues / Sampler buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Hot cue buttons :hwlabel:`1-4`

  - LED: lit if a hot cue is set
  - Press: set or recall a hot cue
  - Press + hold when deck is stopped: play from hot cue as long as button is pressed. Press Play to continue playing after releasing hot cue button
  - Press + hold when deck is playing: jump to hot cue and play from there
  - :hwlabel:`SHIFT` + press: delete the hot cue

- :hwlabel:`▶ 1-4` Sampler buttons
- LED: lit when a sample is loaded to the corresponding sampler, flashes when that sampler is playing.
- Press: play the sample from the beginning
- :hwlabel:`SHIFT` + Press: stop the sample
- :hwlabel:`✂ (scissors)` button - Switches hot cues 5-8 and samplers 5-8

Wheel & Vinyl button
~~~~~~~~~~~~~~~~~~~~

- :hwlabel:`Vinyl/Search` button
- Press + release: toggle scratching with the wheel (LED On)
- Hold down + turn the wheel: seek through the track
- :hwlabel:`Wheel`
- Vinyl mode ON

  - Touch the top black area + turn: scratch the current track like a vinyl record
  - Touch gray rim only + turn: perform a temporary pitch bend

- Vinyl mode OFF

  - Touch wheel anywhere + turn: perform a temporary pitch bend

Transport buttons
~~~~~~~~~~~~~~~~~

- :hwlabel:`▶◀ (Sync)` - Synchronizes the tempo and beat phase of this deck to that of the other.
- :hwlabel:`CUP` (Cue-Play) Start playback from the cue point (also known as stutter play)
- :hwlabel:`Q` (Cue)

  - LED: lit or flashes when play position is at cue point, depending on the :ref:`cue mode <interface-cue-modes>`.
  - Press: Set or recall the main cue point on the track
  - Press + hold: play from Cue point. Release stops playback

- :hwlabel:`▶||` (Play/Pause) Toggle playback of the track
- :hwlabel:`SHIFT` + :hwlabel:`▶◀` (left deck) / :hwlabel:`SHIFT` +  :hwlabel:`▶||` (right deck)

  - initiate the brake effect for the respective deck: track slows down to full stop.

- Touch wheel, Vinyl mode ON: track speed jumps back to normal (considering the pitch slider) and playback continues as soon as the wheel is released. Open the :file:`controllers/Reloop Terminal Mix 2-4.js` file and look for ``TerminalMix.brake`` to adjust parameters.
- :hwlabel:`3` / :hwlabel:`4` button - When lit all deck buttons (except FX controls) control deck 3 (deck 4 respectively).

Mixer controls
--------------

Channel strips
~~~~~~~~~~~~~~

*The below controls adjust the specified parameter of the respective virtual
deck.*

- :hwlabel:`GAIN` knob - Adjusts the pre-fader gain
- :hwlabel:`HIGH`/:hwlabel:`MID`/:hwlabel:`LOW` EQ knobs - Adjust the volume of the respective frequency range
- :hwlabel:`FILTER` knob - Adjust the QuickEffect Meta knob (default: filter)
- :hwlabel:`Headphone` button - Toggles hearing the deck in the headphone output
- :hwlabel:`1` / :hwlabel:`2` / :hwlabel:`3` / :hwlabel:`4`

  - Press: load the currently highlighted song into that deck.
  - :hwlabel:`SHIFT` + press: toggle fader-start (on the channel fader and cross-fader when applicable.) The button flashes when fader-start is enabled on that deck.

- Channel slider - Adjust the output volume

*The below controls are not deck-specific.*

- :hwlabel:`MASTER` knob - Adjust the main output volume of the internal sound card. *(Hard-wired knob, does not send MIDI messages)*
- :hwlabel:`BOOTH` knob - Adjust the booth output volume of the internal sound card. *(Hard-wired knob, does not send MIDI messages)*
- :hwlabel:`PHONES` knob - Adjust the headphone output volume of the internal sound card. *(Hard-wired knob, does not send MIDI messages)*
- :hwlabel:`CUE MIX` knob - Adjust how much of the headphone bus vs the main output you hear in the headphones.
- :hwlabel:`SAMPLER VOLUME` knob - Adjusts the volume of all of the samplers at once.
- :hwlabel:`CRATES` button - Does nothing at the moment. (Mixxx’s library doesn’t yet support direct panel selection.) Use the MIDI Learning Wizard to assign an action.*
- :hwlabel:`VIEW` button - Does nothing at the moment. Use the MIDI Learning Wizard to assign an action.* - :hwlabel:`PREP` button - *Does nothing at the moment. Use the MIDI Learning Wizard to assign an action.*
- :hwlabel:`BACK` button

  - Press: move the highlight in the active library panel to the right
  - :hwlabel:`SHIFT` + Press: move the highlight to the left

- :hwlabel:`TRAX knob`

  - Turn: move the highlight up/down by one line
  - :hwlabel:`SHIFT` + turn: move the highlight one page up/down
  - Press while Tree panel has focus: expand an item if possible. If item can’t be expanded further, it is selected and and highlight is shifted rightwarde to the respective tracks table.
  - Press while tracks table has focus: perform the Track Load Action specified in :menuselection:`Preferences --> Library` (default: load track to next empty deck)

- :hwlabel:`Volume Level Meter`

  - LEDs display the hardware (!) volume of the main output (2 blue LEDs at the top indicate clipping)
  - *Attention:* the main volume might already clip in Mixxx before the hardware LEDs light up. You can adjust the hardware main volume knob and target loudness in :menuselection:`Preferences --> Normalization --> ReplayGain` to keep enough headroom for the main volume in Mixxx and make the lower blue LEDs light up when the main volume clips in Mixxx

- :hwlabel:`POWER` LED (red)
- :hwlabel:`MIDI` LED (blue)

  - Flashes when a MIDI messages was sent
  - When it flashes although no control is touched, it’s probably due to dust in the jogwheels (See :ref:`Controller Hardware / Maintenance <reloop-terminal-mix-series-maintenance>`)

- :hwlabel:`Shift Lock` switch at the back side

  - :hwlabel:`ON`: press :hwlabel:`SHIFT` buttons once to switch to secondary button/knob actions
  - :hwlabel:`OFF`: press & hold :hwlabel:`SHIFT` buttons to switch to secondary button/knob actions

Cross-fader section
~~~~~~~~~~~~~~~~~~~

Move the cross-fader to smoothly fade between the decks assigned to either side.

Deck assign switches (Terminal Mix 4 only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the four switches on the front of the unit to choose on which side of the
cross fader that deck will be heard. (Note that the fader-start functionality
correctly follows this assignment.) If “thru” is selected, the cross-fader
will not affect the audio from that deck and it will always be heard.

Curve adjust
^^^^^^^^^^^^

Use the knob to adjust the curve from a smooth fade to a fast cut.

*The remaining controls on the front of the unit adjust hardware parameters and
are not MIDI-mappable.*
