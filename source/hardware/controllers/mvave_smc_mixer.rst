M-Vave SMC-Mixer
================

`Manufacturer's product page <https://www.cuvave.com/productinfo/1106102.html>`_ ·
`Forum thread <https://mixxx.discourse.group/t/m-wave-sinco-smc-mixer-radio-broadcast-mapping/30366>`_

.. versionadded:: 2.5.1

Overview
--------

.. figure:: ../../_static/controllers/mvave_smc_mixer.svg
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: M-Vave SMC-Mixer
   :figclass: pretty-figures

See the tables below for controls descriptions.

Deck and EQ
-----------

On the left side of the controller each set of a fader, rotary encoder, and
buttons affect a single deck starting with 3 on the left, then 1, 2, and finally
deck 4.

..

.. csv-table::
   :header: "#", "Name", "Function"
   :widths: 5 25 70

   "Knob", ":hwlabel:`EQ` (rotate)", "Adjust selected function (defaults to channel gain)"
   "M", ":hwlabel:`TREBLE` (press)", "Toggle high filter cutoff"
   "M", ":hwlabel:`TREBLE` (long press)", "Toggle knob between gain and high filter"
   "S", ":hwlabel:`MID` (press)", "Toggle mid filter cutoff"
   "S", ":hwlabel:`MID` (long press)", "Toggle knob between gain and mid filter"
   "R", ":hwlabel:`BASS` (press)", "Toggle low filter cutoff"
   "R", ":hwlabel:`BASS` (long press)", "Toggle knob between gain and low filter"
   "□", ":hwlabel:`EFFECT` (press)", "Toggle quick effect rack"
   "□", ":hwlabel:`EFFECT` (long press)", "Toggle knob between gain and quick effect"
   "LEDs", ":hwlabel:`LED`", "Blinks when the hardware control does not match the software control and soft takeover is enabled"
   "Faders", ":hwlabel:`Channel fader`", "Adjust volume level"

Beat Grid
---------

The right hand side of the controller is mapped to controls relating to the
tempo and beat grid.
Each set of controls is mapped to one deck and follows the same order (3, 1, 2,
4) as the left side controls.
The only exception is the rotary encoders, which are mapped separately as
described below.

.. csv-table::
   :header: "#", "Name", "Function"
   :widths: 5 25 70

   "M", ":hwlabel:`SLIP`", "Toggle slip mode"
   "S", ":hwlabel:`QUANTIZE`", "Toggle quantize mode"
   "R", ":hwlabel:`KEY`", "Toggle the key lock"
   "□", ":hwlabel:`CUE`", ":term:`Headphone button` / PFL. Toggle sending channel to the cue (headphone) channel"
   "LEDs", ":hwlabel:`LED`", "Blinks when the hardware control does not match the software control and soft takeover is enabled"
   "Faders", ":hwlabel:`Tempo fader`", "Adjust track tempo"

Transports
----------

The transport buttons along the bottom affect only the currently selected deck,
with the exception of "record" which toggles recording of the mix and the
navigation buttons which always affect the library view.

.. csv-table::
   :header: "#", "Name", "Function"
   :widths: 5 25 70

   "⏵", ":hwlabel:`Play/Pause`", "Play/pause playback"
   "⏸", ":hwlabel:`CUE`", "If track is playing: stops the track and resets position to the main cue point

   If playback is stopped: sets the main cue point"
   "⏸", ":hwlabel:`CUE` (hold)", "Play the track from main cue point, release to stop playback and return to the main cue point. Playback must be initially stopped on the main cue point."
   "⏺", ":hwlabel:`RECORD`", "Toggle recording the mix"
   "⏪", ":hwlabel:`REWIND`", "Beatjump backwards"
   "⏩", ":hwlabel:`FASTFORWARD`", "Beatjump forwards"
   "«",  ":hwlabel:`DECK`", "Select deck 1"
   "«",  ":hwlabel:`DECK` (hold)", "Select deck 3"
   "»",  ":hwlabel:`DECK`", "Select deck 2"
   "»",  ":hwlabel:`DECK` (hold)", "Select deck 4"
   "▲",  ":hwlabel:`UP`", "Navigate up in selected library pane"
   "▼",  ":hwlabel:`DOWN`", "Navigate down in selected library pane"
   "◀", ":hwlabel:`LEFT` (tracks pane focused)", "Navigate to library sidebar"
   "◀", ":hwlabel:`LEFT` (sidebar focused)", "Expand/collapse selected list"
   "▶", ":hwlabel:`RIGHT` (sidebar focused)", "Navigate to library tracks view"
   "▶", ":hwlabel:`RIGHT` (tracks pane focused)", "Load track to first available deck"

.. hint::
   The actual behavior of CUE and Play/Pause buttons depends on Mixxx settings. See :ref:`interface-cue-modes` for more info.


Knobs
-----

The four right most rotary encoders are not mapped to individual decks.
Instead they control global mixer values.

.. csv-table::
   :header: "#", "Name", "Function"
   :widths: 5 25 70

   "5",  ":hwlabel:`MAIN GAIN`", "Adjust the volume level of :term:`master output`."
   "6",  ":hwlabel:`BALANCE`", "Adjust the output balance"
   "7",  ":hwlabel:`CUE GAIN`", "Adjust the headphone volume"
   "8",  ":hwlabel:`CUE MIX`", ":term:`Head/mix knob<Head/mix button>`. Adjust the dry/wet output to the headphones, mixing between the cue output and the main mix output"
