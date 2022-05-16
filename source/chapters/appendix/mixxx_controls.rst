.. include:: /shortcuts.rstext

.. _appendix-mixxxcontrols:

Mixxx Controls
==============

Nearly every knob, button, or fader you see in Mixxx's interface is
controllable via Mixxx's "control" system. The control system allows
skins, :term:`MIDI` controllers, :term:`HID` controllers and keyboards
to control Mixxx via a single interface.

A control is identified by a "group" (which is used for grouping
associated controls) and a "key" (the name of the individual control).

For example, the volume fader for Deck 1 is identified by the group
:mixxx:cogroupref:`[Channel1] <[ChannelN]>` and key :mixxx:coref:`volume <[Channel1],volume>`.
Similarly, the volume fader for Sampler 1 is identified by the group
:mixxx:cogroupref:`[Sampler1] <[SamplerN]>` and key :mixxx:coref:`volume <[Sampler1],volume>`.

The group is used to collect all the controls that affect one component
of Mixxx into one collection. Some groups have a high overlap of
controls in common (e.g. samplers, decks, and the preview deck all share
the same control keys).

In addition to controlling Mixxx, the control system can be used to
inspect Mixxx's state. For example, the sample rate of the track loaded
in Deck 1 can be accessed via the :mixxx:coref:`[Channel1],track_samplerate`
control. You can read the :mixxx:coref:`[Channel3],play` control to determine
whether Deck 3 is playing.

The default value range is 0.0 to 1.0, unless otherwise noted. Binary means
that it is either 'ON' (non-zero) or 'OFF' (zero).

.. hint:: Discovering Controls used in Skins

   You can view the control connected to any part of a skin by running
   Mixxx with the ``--developer`` command line option and hovering your mouse
   cursor over part of the skin. If no tooltip appears, enable tooltips for
   the Library and Skin in :menuselection:`Options --> Preferences --> Interface`.

.. hint:: Changing any control from the GUI in Developer Mode

   When running Mixxx in Developer Mode (with the ``--developer`` command
   line option), you can view and manually set the state of any control in
   Mixxx by going to :menuselection:`Developer --> Developer Tools`.

.. seealso:: See :ref:`controlindex` for a full list.


.. _appendix-mixxxcontrols-controlpotmeter:

ControlPotMeter controls
~~~~~~~~~~~~~~~~~~~~~~~~

The following extensions add some features to ``ControlPotMeter`` controls
(volume, :term:`crossfader`, ...). Use in conjunction with ``[ChannelN]``,
``[SamplerN]``, ``[Master]``, ... groups.

================== ============================================================
Control Suffix     Description, example
================== ============================================================
``_up``            Increases the value, e.g. :mixxx:coref:`[ChannelN],rate_perm_up` sets the speed one step higher (4 % default)
``_down``          Decreases the value, sets the speed one step lower (4 % default)
``_up_small``      Increases the value by smaller step, sets the speed one small step higher (1 % default)
``_down_small``    Decreases the value by smaller step, sets the speed one small step lower (1 % default)
``_set_one``       Sets the value to 1.0, sets the channel volume to full
``_set_minus_one`` Sets the value to -1.0, sets the channel volume to zero
``_set_default``   Input: sets the control to its default, return to default waveform zoom level
``_set_default``   Output: set to 1.0 if the control is at its default, light up the pitch fader center indicator
``_set_zero``      Sets the value to 0.0, put the crossfader in the middle again
``_toggle``        Sets the value to 0.0 if the value was > 0.0, and to 1.0 if the value was 0.0, will cut off/on a track while you're playing
``_minus_toggle``  Sets the value to -1.0 if the value was > -1.0, and to 1.0 if the value was -1.0, can tilt the crossfader from left to right
================== ============================================================

These controls can be used in JavaScript files like this:

.. code-block:: javascript

   // This won't work:
   engine.setValue(group, "pitch_up_small", 1.0);

   // Use this instead:
   script.triggerControl(group, "pitch_up_small", 50);

To use ``*_toggle`` the respective shortcut for scripts is:

.. code-block:: javascript

   script.toggleControl(group, "keylock_toggle", 100);


The ``[Master]`` group
~~~~~~~~~~~~~~~~~~~~~~

The :mixxx:cogroupref:`[Master]` group generally corresponds to controls that affect the mixing engine.
This will bear some similarity to what you will find on a DJ mixer (e.g. :term:`crossfader` controls, headphone cueing controls, etc.).

.. mixxx:control:: [Master],audio_latency_usage

   Reflects fraction of :term:`latency`, given by the audio buffer size, spend for audio processing inside Mixxx. At value near 25 % there is a high risk of buffer underflows

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0 .. 25 %
   :feedback: latency meter

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],audio_latency_overload

   Indicates a buffer under or over-flow. Resets after 500 ms

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Overload indicator

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],audio_latency_overload_count

   Counts buffer over and under-flows. Max one per 500 ms

   :range: 0 .. n
   :feedback: Counter in hardware preferences

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],balance

   Adjusts the left/right channel balance on the Master output.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: -1.0..1.0
   :feedback: Center Balance knob


.. mixxx:control:: [Master],booth_enabled

   Indicates whether a Booth output is configured in the :ref:`Sound Hardware Preferences <preferences-sound-hardware>`.

   :range: binary
   :feedback: Booth gain knob shown or hidden

   .. versionadded:: 2.1.0


.. mixxx:control:: [Master],booth_gain

   Adjusts the gain of the Booth output.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0.0...1.0...5.0
   :feedback: Booth gain knob

   .. versionadded:: 2.1.0


.. mixxx:control:: [Master],crossfader

   Adjusts the :term:`crossfader` between players/decks (-1.0 is all the way left).

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: -1.0..1.0
   :feedback: Crossfader slider


.. mixxx:control:: [Master],crossfader_down

   Moves the :term:`crossfader` left by 1/10th.

   :range: binary
   :feedback: Crossfader slider


.. mixxx:control:: [Master],crossfader_down_small

   Moves the :term:`crossfader` left by 1/100th.

   :range: binary
   :feedback: Crossfader slider

   .. versionadded:: 1.10.0


.. mixxx:control:: [Master],crossfader_up

   Moves the :term:`crossfader` right by 1/10th.

   :range: binary
   :feedback: Crossfader slider


.. mixxx:control:: [Master],crossfader_up_small

   Moves the :term:`crossfader` right by 1/100th.

   :range: binary
   :feedback: Crossfader slider

   .. versionadded:: 1.10.0


.. mixxx:control:: [Master],duckStrength

   Microphone ducking strength

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0.0..1.0
   :feedback: Strength knob

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],enabled

   Indicator that the master mix is processed.

   :range: binary
   :feedback: None

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],gain

   Adjusts the gain for the master output as well as recording and broadcasting signal.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0.0..1.0..5.0
   :feedback: Master volume knob

   .. versionadded:: 2.0.0



.. mixxx:control:: [Master],headEnabled

   Indicator that the headphone mix is processed.

   :range: binary
   :feedback: None

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],headGain

   Adjusts the headphone output gain.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0.0..1.0..5.0
   :feedback: Headphone volume knob

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],headMix

   Adjusts the cue/main mix in the headphone output.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Pre/Main knob


.. mixxx:control:: [Master],headSplit

   Splits headphone stereo cueing into right (master mono) and left (:term:`PFL` mono).

   :range: binary
   :feedback: Split Cue button

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],latency

   :term:`Latency <latency>` setting (sound buffer size) in milliseconds (default 64).

   :range: >=0 (absolute value)
   :feedback: Latency slider in the prefs


.. mixxx:control:: [Master],maximize_library

   Toggle maximized view of library.

   :range: binary
   :feedback: Toggle maximized view of library

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],num_decks

   The number of decks currently enabled.

   :range: integer
   :feedback: None

   .. versionadded:: 1.9.0


.. mixxx:control:: [Master],num_effectsavailable

   The number of available effects that can be selected in an effect slot.

   :range: integer, read-only
   :feedback: None

   .. versionadded:: 2.1.0


.. mixxx:control:: [Master],num_samplers

   The number of samplers currently enabled.

   :range: integer
   :feedback: None

   .. versionadded:: 1.9.0


.. mixxx:control:: [Master],num_preview_decks

   The number of preview decks currently enabled.

   :range: integer
   :feedback: None

   .. versionadded:: 1.11.0


.. mixxx:control:: [Master],PeakIndicator

   Indicates when the signal is clipping (too loud for the hardware and is being distorted) (composite).

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Clip light (mono)


.. mixxx:control:: [Master],PeakIndicatorL

   Indicates when the signal is clipping (too loud for the hardware and is being distorted) for the left channel.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Clip light (left)


.. mixxx:control:: [Master],PeakIndicatorR

   Indicates when the signal is clipping (too loud for the hardware and is being distorted) for the right channel.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Clip light (right)


.. mixxx:control:: [Master],samplerate

   The current output sample rate (default: 44100 Hz).

   :range: absolute value (in Hz)
   :feedback: None


.. mixxx:control:: [Master],talkoverDucking

   Toggle microphone ducking mode (OFF, AUTO, MANUAL)

   :range: FIXME
   :feedback: Ducking mode button

   .. versionadded:: 2.0.0


.. mixxx:control:: [Master],VuMeter

   Outputs the current instantaneous master volume (composite).

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Master meter (mono)


.. mixxx:control:: [Master],VuMeterL

   Outputs the current instantaneous master volume for the left channel.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Master meter L


.. mixxx:control:: [Master],VuMeterR

   Outputs the current instantaneous master volume for the right channel.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Master meter R


.. mixxx:control:: [Master],headVolume

    Adjust headphone volume.

    :range: 0.0..1.0..5.0
    :feedback: Headphone Gain knob

    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[Master],headGain` instead.


.. mixxx:control:: [Master],volume

    Adjust master volume.

    :range: 0.0..1.0..5.0
    :feedback: Master Gain knob

    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[Master],gain` instead.

.. _appendix-mixxxcontrols-decks:

Decks, Preview Decks and Samplers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each deck in Mixxx corresponds to a :mixxx:cogroupref:`[ChannelN]` group.
Whenever you see :mixxx:cogroupref:`[ChannelN]`, think "Deck N".
N can range from 1 to the number of active decks in Mixxx.

Preview decks and Sample decks ("samplers") in Mixxx are identical to regular decks, they simply have a different purpose (previewing tracks or playing samples, respectively).
Any control listed above for :mixxx:cogroupref:`[ChannelN]` will work for a samplers and preview decks, just replace :mixxx:cogroupref:`[ChannelN]` with :mixxx:cogroupref:`[PreviewDeckN]` or :mixxx:cogroupref:`[SamplerN]`.

.. seealso:: There are some :ref:`additional global controls for samplers <appendix-mixxxcontrols-samplers>`.

.. mixxx:control:: [ChannelN],back
                   [PreviewDeckN],back
                   [SamplerN],back

   Fast rewind (REW)

   :range: binary
   :feedback: << button


.. mixxx:control:: [ChannelN],beat_active
                   [PreviewDeckN],beat_active
                   [SamplerN],beat_active

   Indicates whether the player is currently positioned within 50 milliseconds of a beat or not.
   This can be used to make controller LEDs blink on every beat.

   :range: binary
   :feedback: None

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],beat_closest
                   [PreviewDeckN],beat_closest
                   [SamplerN],beat_closest


   Its value is set to the sample position of the closest beat of the active beat and is used for updating the beat LEDs.
   :range: -1, 0.0, real-valued
   :feedback: None

.. mixxx:control:: [ChannelN],beat_distance
                   [PreviewDeckN],beat_distance
                   [SamplerN],beat_distance

   Outputs the relative position of the play marker in the section between the the previous and next beat marker.
   :range: 0.0 - 1.0, real-valued
   :feedback: None


.. mixxx:control:: [ChannelN],beatjump
                   [PreviewDeckN],beatjump
                   [SamplerN],beatjump

   Jump forward by :mixxx:coref:`beatjump_size <[ChannelN],beatjump_size>` (positive) or backward by :mixxx:coref:`beatjump_size <[ChannelN],beatjump_size>` (negative). If a loop is active, the loop is moved by :mixxx:coref:`beatjump_size <[ChannelN],beatjump_size>`.

   :range: real number, -1, 0, 1
   :feedback: Player jumps forward or backward by X beats.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],beatjump_size
                   [PreviewDeckN],beatjump_size
                   [SamplerN],beatjump_size

   Set the number of beats to jump with :mixxx:coref:`beatjump_forward <[ChannelN],beatjump_forward>`/:mixxx:coref:`beatjump_backward <[ChannelN],beatjump_backward>`.

   :range: positive real number
   :feedback: Beatjump size spinbox

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],beatjump_forward
                   [PreviewDeckN],beatjump_forward
                   [SamplerN],beatjump_forward

   Jump forward by :mixxx:coref:`beatjump_size <[ChannelN],beatjump_size>`. If a loop is active, the loop is moved forward by X beats.

   :range: binary
   :feedback: Player jumps forward by :mixxx:coref:`beatjump_size <[ChannelN],beatjump_size>`.

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],beatjump_backward
                   [PreviewDeckN],beatjump_backward
                   [SamplerN],beatjump_backward

   Jump backward by :mixxx:coref:`beatjump_size <[ChannelN],beatjump_size>`. If a loop is active, the loop is moved backward by X beats.

   :range: binary
   :feedback: Player jumps backward by :mixxx:coref:`beatjump_size <[ChannelN],beatjump_size>`.

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],beatjump_X_forward
                   [PreviewDeckN],beatjump_X_forward
                   [SamplerN],beatjump_X_forward

   Jump forward by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64. If a loop is active, the loop is moved forward by X betas.

   :range: binary
   :feedback: Player jumps forward by X beats.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],beatjump_X_backward
                   [PreviewDeckN],beatjump_X_backward
                   [SamplerN],beatjump_X_backward

   Jump backward by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64. If a loop is active, the loop is moved backward by X beats.

   :range: binary
   :feedback: Player jumps backward by X beats.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],beatloop_activate
                   [PreviewDeckN],beatloop_activate
                   [SamplerN],beatloop_activate

   Set a loop that is :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>` beats long and enables the loop

   :range: binary
   :feedback: A loop is shown over :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>` beats

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],beatloop_X_activate
                   [PreviewDeckN],beatloop_X_activate
                   [SamplerN],beatloop_X_activate

   Activates a loop over X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64

   :range: binary
   :feedback: A loop is shown over X beats.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],beatloop_size
                   [PreviewDeckN],beatloop_size
                   [SamplerN],beatloop_size

   Set the length of the loop in beats that will get set with :mixxx:coref:`beatloop_activate <[ChannelN],beatloop_activate>` and :mixxx:coref:`beatlooproll_activate <[ChannelN],beatlooproll_activate>`.
   Changing this will resize an existing loop if the length of the loop matches :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>`.

   :range: positive real number
   :feedback: Beatloop size spinbox and possibly loop section on waveform

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],beatloop_X_toggle
                   [PreviewDeckN],beatloop_X_toggle
                   [SamplerN],beatloop_X_toggle

   Toggles a loop over X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64

   :range: binary
   :feedback: A loop is shown over X beats.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],beatloop_X_enabled
                   [PreviewDeckN],beatloop_X_enabled
                   [SamplerN],beatloop_X_enabled

   1 if beatloop X is enabled, 0 if not.

   :range: binary
   :feedback: Beatloop X button in skin is lit.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],beatlooproll_activate
                   [PreviewDeckN],beatlooproll_activate
                   [SamplerN],beatlooproll_activate

   Activates a rolling loop over :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>` beats. Once disabled, playback will resume where the track would have been if it had not entered the loop.

   :range: binary
   :feedback: A loop overlay is shown over :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>` beats on waveform.

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],beatlooproll_X_activate
                   [PreviewDeckN],beatlooproll_X_activate
                   [SamplerN],beatlooproll_X_activate

   Activates a rolling loop over X beats. Once disabled, playback will resume where the track would have been if it had not entered the loop. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64

   :range: binary
   :feedback: Beatloop X button in skin is lit. A loop overlay is shown over X beats on waveform.

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],beats_adjust_faster
                   [PreviewDeckN],beats_adjust_faster
                   [SamplerN],beats_adjust_faster

   Adjust the average :term:`BPM` up by +0.01

   :range: binary
   :feedback: The :term:`beatgrid` lines move closer to each other.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],beats_adjust_slower
                   [PreviewDeckN],beats_adjust_slower
                   [SamplerN],beats_adjust_slower

   Adjust the average :term:`BPM` down by -0.01.

   :range: binary
   :feedback: The :term:`beatgrid` lines move further apart from each other.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],beats_translate_curpos
                   [PreviewDeckN],beats_translate_curpos
                   [SamplerN],beats_translate_curpos

   Adjust :term:`beatgrid` so closest beat is aligned with the current playposition.

   :range: binary
   :feedback: The beatgrid moves to align with current playposition.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],beats_translate_match_alignment
                   [PreviewDeckN],beats_translate_match_alignment
                   [SamplerN],beats_translate_match_alignment

   Adjust :term:`beatgrid` to match another playing deck.

   :range: binary
   :feedback: Instead of :term:`syncing <sync>` the beatgrid to the current playposition, sync the beatgrid so the nearest beat lines up with the other track's nearest beat.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],beats_translate_earlier
                   [PreviewDeckN],beats_translate_earlier
                   [SamplerN],beats_translate_earlier

   Move :term:`beatgrid` to an earlier position.

   :range: binary
   :feedback: The beatgrid moves left by a small amount.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],beats_translate_later
                   [PreviewDeckN],beats_translate_later
                   [SamplerN],beats_translate_later

   Move :term:`beatgrid` to a later position.

   :range: binary
   :feedback: The beatgrid moves right by a small amount.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],beatsync
                   [PreviewDeckN],beatsync
                   [SamplerN],beatsync

  :term:`Syncs <sync>` the :term:`tempo` and phase (depending on quantize) to that of the other track (if :term:`BPM` is detected on both).

   :range: binary
   :feedback: The :guilabel:`Sync` button flashes and the :term:`tempo` slider snaps to the appropriate value.

   .. versionchanged:: 1.10.0


.. mixxx:control:: [ChannelN],beatsync_phase
                   [PreviewDeckN],beatsync_phase
                   [SamplerN],beatsync_phase

   :term:`Syncs <sync>` the :term:`phase` to that of the other track (if :term:`BPM` is detected on both).

   :range: binary
   :feedback: The :guilabel:`Sync` button flashes and the :term:`tempo` slider snap to the appropriate value.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],beatsync_tempo
                   [PreviewDeckN],beatsync_tempo
                   [SamplerN],beatsync_tempo

   :term:`Syncs <sync>` the :term:`tempo` to that of the other track (if :term:`BPM` is detected on both).

   :range: binary
   :feedback: The :guilabel:`Sync` button flashes and the :term:`tempo` slider snaps to the appropriate value.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],bpm
                   [PreviewDeckN],bpm
                   [SamplerN],bpm

   Reflects the perceived (rate-adjusted) :term:`BPM` of the loaded file.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: real-valued
   :feedback: :term:`BPM` value display

   .. versionchanged:: 1.10.0


.. mixxx:control:: [ChannelN],bpm_tap
                   [PreviewDeckN],bpm_tap
                   [SamplerN],bpm_tap

   When tapped repeatedly, adjusts the :term:`BPM` of the track on the deck (not the tempo slider!) to match the taps.

   .. note:: If you want to change the :term:`rate` of the deck use `script.bpm.tapButton(deck) <https://github.com/mixxxdj/mixxx/wiki/midi%20scripting#user-content-helper-functions>`_ in your controller mapping instead.

   :range: binary
   :feedback: :term:`BPM` value display (playback speed doesn't change)

   .. versionadded:: 1.9.2


.. mixxx:control:: [ChannelN],CloneFromDeck
                   [PreviewDeckN],CloneFromDeck
                   [SamplerN],CloneFromDeck

   Clone the given deck number, copying the play state, position, rate, and key. If 0 or a negative number is given, Mixxx will attempt to select the first playing deck as the source for the clone.

   :range: integer between 1 and :mixxx:coref:`[Master],num_decks` (inclusive)
   :feedback: The channel will start playing at the rate and position of the source deck.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],CloneFromSampler
                   [PreviewDeckN],CloneFromSampler
                   [SamplerN],CloneFromSampler

   Clone the given sampler number, copying the play state, position, rate, and key.

   :range: integer between 1 and :mixxx:coref:`[Master],num_samplers` (inclusive)
   :feedback: The channel will start playing at the rate and position of the source deck.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],cue_cdj
                   [PreviewDeckN],cue_cdj
                   [SamplerN],cue_cdj

   Represents a :guilabel:`Cue` button that is always in :term:`CDJ` mode.

   :range: binary
   :feedback: None

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],cue_clear
                   [PreviewDeckN],cue_clear
                   [SamplerN],cue_clear

   Deletes the already set cue point and sets :mixxx:coref:`[ChannelN],cue_point` to -1.

   :range: binary
   :feedback: None


.. mixxx:control:: [ChannelN],cue_goto
                   [PreviewDeckN],cue_goto
                   [SamplerN],cue_goto

   If the cue point is set, recalls the cue point.

   :range: binary
   :feedback: Player may change position


.. mixxx:control:: [ChannelN],cue_default
                   [PreviewDeckN],cue_default
                   [SamplerN],cue_default

   In :term:`CDJ` mode, when playing, returns to the :term:`cue point` and pauses. If stopped, sets a cue point at the current location. If stopped and at a cue point, plays from that point until released (set to 0.)

   :range: binary
   :feedback: :guilabel:`Cue` button


.. mixxx:control:: [ChannelN],cue_gotoandplay
                   [PreviewDeckN],cue_gotoandplay
                   [SamplerN],cue_gotoandplay

   If the :term:`cue point` is set, seeks the player to it and starts playback.

   :range: binary
   :feedback: Player may change position and start playing.

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],cue_gotoandstop
                   [PreviewDeckN],cue_gotoandstop
                   [SamplerN],cue_gotoandstop

   If the :term:`cue point` is set, seeks the player to it and stops.

   :range: binary
   :feedback: Player may change position.

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],cue_indicator
                   [PreviewDeckN],cue_indicator
                   [SamplerN],cue_indicator

   Indicates the blinking pattern of the :guilabel:`CUE` button (i.e. 1.0 if the button is illuminated, 0.0 otherwise), depending on the chosen :mixxx:coref:`cue mode <[ChannelN],cue_mode>`.

   :range: binary
   :feedback: :guilabel:`Cue` button

   .. versionadded:: 2.0.0

.. mixxx:control:: [ChannelN],cue_mode
                   [PreviewDeckN],cue_mode
                   [SamplerN],cue_mode

   Represents the currently chosen :ref:`cue mode <interface-cue-modes>`.

   :range:
      ===== =============================
      Value compatible hardware
      ===== =============================
      0.0   Mixxx mode (default)
      1.0   Pioneer mode
      2.0   Denon mode
      3.0   Numark mode
      4.0   Mixxx mode (no blinking)
      5.0   CUP (Cue + Play) mode
      ===== =============================



   :feedback: None


.. mixxx:control:: [ChannelN],cue_play
                   [PreviewDeckN],cue_play
                   [SamplerN],cue_play

   Go to :term:`cue point` and play after release (CUP button behavior). If stopped, sets a cue point at the current location.

   :range: binary
   :feedback: None

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],cue_point
                   [PreviewDeckN],cue_point
                   [SamplerN],cue_point

   The current position of the :term:`cue point` in samples.

   :range: absolute value
   :feedback: Cue point marker


.. mixxx:control:: [ChannelN],cue_preview
                   [PreviewDeckN],cue_preview
                   [SamplerN],cue_preview

   Plays from the current :term:`cue point`.

   :range: binary
   :feedback: :guilabel:`Cue` button lights and waveform moves


.. mixxx:control:: [ChannelN],cue_set
                   [PreviewDeckN],cue_set
                   [SamplerN],cue_set

   Sets a :term:`cue point` at the current location.

   :range: binary
   :feedback: :term:`Cue <cue>` mark appears on the waveform


.. mixxx:control:: [ChannelN],cue_simple
                   [PreviewDeckN],cue_simple
                   [SamplerN],cue_simple

   If the player is not playing, set the :term:`cue point` at the current location otherwise seek to the cue point.

   :range: binary
   :feedback: :guilabel:`Cue` button


.. mixxx:control:: [ChannelN],duration
                   [PreviewDeckN],duration
                   [SamplerN],duration

   Outputs the length of the current song in seconds

   :range: absolute value
   :feedback: None


.. mixxx:control:: [ChannelN],eject
                   [PreviewDeckN],eject
                   [SamplerN],eject

   Eject currently loaded track

   :range: binary
   :feedback: Eject button is lit. Be sure to set back to 0 with scripts so the button does not stay lit.

   .. versionadded:: 1.9.0


.. mixxx:control:: [ChannelN],end
                   [PreviewDeckN],end
                   [SamplerN],end

   Jump to end of track

   :range: binary
   :feedback: Track jumps to end


.. mixxx:control:: [ChannelN],end_of_track
                   [PreviewDeckN],end_of_track
                   [SamplerN],end_of_track

   Switches to 1 if the play position is within the end range defined in :menuselection:`Preferences --> Waveforms --> End of track warning`.

   :range: binary, read-only
   :feedback: Waveform and Overview widgets show a flashing border


.. mixxx:control:: [ChannelN],file_bpm
                   [PreviewDeckN],file_bpm
                   [SamplerN],file_bpm

   The detected :term:`BPM` of the loaded track.

   :range: positive value, read-only
   :feedback: None


.. mixxx:control:: [ChannelN],file_key
                   [PreviewDeckN],file_key
                   [SamplerN],file_key

   The detected key of the loaded track.

   :range: ?, read-only
   :feedback: None

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],fwd
                   [PreviewDeckN],fwd
                   [SamplerN],fwd

   Fast forward (FF)

   :range: binary
   :feedback: > button


.. mixxx:control:: [ChannelN],hotcue_X_activate
                   [PreviewDeckN],hotcue_X_activate
                   [SamplerN],hotcue_X_activate

   If :term:`hotcue` X is not set, this sets a hotcue at the current play position and saves it to hotcue slot X.

   If hotcue X is set, the player seeks to hotcue X's position.
   Setting the control to 1 when the track is currently not playing (i.e. :mixxx:coref:`play <[ChannelN],play>` is set to 0) will start hotcue previewing.
   After resetting the control to 0, playback will usually be stopped and the player will seek to the hotcue position.
   If :mixxx:coref:`play <[ChannelN],play>` is set to 1 while previewing is active, the playback will continue and no seek occurs.

   :range: binary
   :feedback: Player may change position. Hotcue X marker may change on waveform.

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],hotcue_X_clear
                   [PreviewDeckN],hotcue_X_clear
                   [SamplerN],hotcue_X_clear

   If :term:`hotcue` X is set, clears its hotcue status.

   :range: binary
   :feedback: Hotcue X marker changes on waveform.

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],hotcue_X_color
                   [PreviewDeckN],hotcue_X_color
                   [SamplerN],hotcue_X_color

   Color of :term:`hotcue` X or -1 if the hotcue is not set.

   :range: 3-Byte :term:`RGB` color code (or -1)
   :feedback: Color of Hotcue X button and waveform marker changes.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],hotcue_X_enabled
                   [PreviewDeckN],hotcue_X_enabled
                   [SamplerN],hotcue_X_enabled

   Indicates if :term:`hotcue` slot X is set. The value is 1 if the hotcue is set (position is not -1), 0 otherwise.

   :range: binary, read-only

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],hotcue_X_goto
                   [PreviewDeckN],hotcue_X_goto
                   [SamplerN],hotcue_X_goto

   If :term:`hotcue` X is set, seeks the player to hotcue X's position.

   :range: binary
   :feedback: Player may change position.

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],hotcue_X_gotoandplay
                   [PreviewDeckN],hotcue_X_gotoandplay
                   [SamplerN],hotcue_X_gotoandplay

   If :term:`hotcue` X is set, seeks the player to hotcue X's position and starts playback.

   :range: binary
   :feedback: Player may change position.

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],hotcue_X_gotoandstop
                   [PreviewDeckN],hotcue_X_gotoandstop
                   [SamplerN],hotcue_X_gotoandstop

   If :term:`hotcue` X is set, seeks the player to hotcue X's position and stops.

   :range: binary
   :feedback: Player may change position.

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],hotcue_X_position
                   [PreviewDeckN],hotcue_X_position
                   [SamplerN],hotcue_X_position

   The position of :term:`hotcue` X in samples, -1 if not set.

   :range: positive integer
   :feedback: Hotcue X marker changes on waveform.

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],hotcue_X_set
                   [PreviewDeckN],hotcue_X_set
                   [SamplerN],hotcue_X_set

   Set :term:`hotcue` X to the current play position. If hotcue X was previously set, clears its hotcue status.

   :range: binary
   :feedback: Hotcue X marker changes on waveform.

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],hotcue_focus
                   [PreviewDeckN],hotcue_focus
                   [SamplerN],hotcue_focus

   Contains the number of the most recently used :term:`hotcue` (or -1 if no hotcue was used).

   :range: positive integer (or -1)
   :feedback: None

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],hotcue_focus_color_prev
                   [PreviewDeckN],hotcue_focus_color_prev
                   [SamplerN],hotcue_focus_color_prev

   If there is a focused :term:`hotcue`, sets its color to the previous color in the palette.

   :range: binary
   :feedback: Color of focused hotcue button and waveform marker changes.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],hotcue_focus_color_next
                   [PreviewDeckN],hotcue_focus_color_next
                   [SamplerN],hotcue_focus_color_next

   If there is a focused :term:`hotcue`, sets its color to the next color in the palette.

   :range: binary
   :feedback: Color of focused hotcue button and waveform marker changes.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_end_activate
                   [PreviewDeckN],intro_end_activate
                   [SamplerN],intro_end_activate

   If the intro end cue is set, seeks the player to the intro end position. If the intro end is not set, sets the intro end to the current play position.

   :range: binary
   :feedback: Player may change position. Intro end marker may change on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_end_clear
                   [PreviewDeckN],intro_end_clear
                   [SamplerN],intro_end_clear

   If the intro end cue is set, clears its status.

   :range: binary
   :feedback: Intro end marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_end_enabled
                   [PreviewDeckN],intro_end_enabled
                   [SamplerN],intro_end_enabled

   1 if intro end cue is set, (position is not -1), 0 otherwise.

   :range: binary, read-only
   :feedback: Intro end button lights up.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_end_position
                   [PreviewDeckN],intro_end_position
                   [SamplerN],intro_end_position

   The position of the intro end in samples, -1 if not set.

   :range: positive integer
   :feedback: Intro end marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_end_set
                   [PreviewDeckN],intro_end_set
                   [SamplerN],intro_end_set

   Set intro end to the current play position. If intro end was previously set, it is moved to the new position.

   :range: binary
   :feedback: Intro end marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_start_activate
                   [PreviewDeckN],intro_start_activate
                   [SamplerN],intro_start_activate

   If the intro start cue is set, seeks the player to the intro start position. If the intro start is not set, sets the intro start to the current play position.

   :range: binary
   :feedback: Player may change position. Intro start marker may change on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_start_clear
                   [PreviewDeckN],intro_start_clear
                   [SamplerN],intro_start_clear

   If the intro start cue is set, clears its status.

   :range: binary
   :feedback: Intro start marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_start_enabled
                   [PreviewDeckN],intro_start_enabled
                   [SamplerN],intro_start_enabled

   1 if intro start cue is set, (position is not -1), 0 otherwise.

   :range: binary, read-only
   :feedback: Intro start button lights up.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_start_position
                   [PreviewDeckN],intro_start_position
                   [SamplerN],intro_start_position

   The position of the intro start in samples, -1 if not set.

   :range: positive integer
   :feedback: Intro start marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],intro_start_set
                   [PreviewDeckN],intro_start_set
                   [SamplerN],intro_start_set

   Set intro start to the current play position. If intro start was previously set, it is moved to the new position.

   :range: binary
   :feedback: Intro start marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],key
                   [PreviewDeckN],key
                   [SamplerN],key

   Current key of the track

   :range:
     =====  =======  ========  ===========
     Value  OpenKey  Lancelot  Traditional
     =====  =======  ========  ===========
     1      1d       8b        C
     2      8d       3b        D♭
     3      3d       10b       D
     4      10d      5b        E♭
     5      5d       12b       E
     6      12d      7b        F
     7      7d       2b        F♯/G♭
     8      2d       9b        G
     9      9d       4b        A♭
     10     4d       11b       A
     11     11d      6b        B♭
     12     6d       1b        B
     13     10m      5a        Cm
     14     5m       12a       C♯m
     15     12m      7a        Dm
     16     7m       2a        D♯m/E♭m
     17     2m       9a        Em
     18     9m       4a        Fm
     19     4m       11a       F♯m
     20     11m      6a        Gm
     21     6m       1a        G♯m
     22     1m       8a        Am
     23     8m       3a        B♭m
     24     3m       10a       Bm
     =====  =======  ========  ===========

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],keylock
                   [PreviewDeckN],keylock
                   [SamplerN],keylock

   Enable key-lock for the specified deck (rate changes only affect tempo, not key)

   :range: binary
   :feedback: key-lock button activates

   .. versionadded:: 1.9.0


.. mixxx:control:: [ChannelN],LoadSelectedTrack
                   [PreviewDeckN],LoadSelectedTrack
                   [SamplerN],LoadSelectedTrack

   Loads the currently highlighted track into the deck

   :range: binary
   :feedback: Track name & waveform change


.. mixxx:control:: [ChannelN],LoadSelectedTrackAndPlay
                   [PreviewDeckN],LoadSelectedTrackAndPlay
                   [SamplerN],LoadSelectedTrackAndPlay

   Loads the currently highlighted track into the deck and starts playing

   :range: binary
   :feedback: Track name & waveform change & Play/pause button

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],local_bpm
                   [PreviewDeckN],local_bpm
                   [SamplerN],local_bpm

   Reflects the average bpm around the current play position of the loaded file.

   :range: positive value
   :feedback: None


.. mixxx:control:: [ChannelN],loop_double
                   [PreviewDeckN],loop_double
                   [SamplerN],loop_double

   Doubles :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>`. If :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>` equals the size of the loop, the loop is resized.

   :range: binary
   :feedback: Beatloop size spinbox changes

   .. versionadded:: 1.10.0
   .. versionchanged:: 2.1.0


.. mixxx:control:: [ChannelN],loop_enabled
                   [PreviewDeckN],loop_enabled
                   [SamplerN],loop_enabled

   Indicates whether or not a loop is enabled.

   :range: binary, read-only
   :feedback: Loop in waveform is active.

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],loop_end_position
                   [PreviewDeckN],loop_end_position
                   [SamplerN],loop_end_position

   The player loop-out position in samples, -1 if not set.

   :range: positive integer
   :feedback: Loop-out marker shows on waveform.

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],loop_halve
                   [PreviewDeckN],loop_halve
                   [SamplerN],loop_halve

   Halves :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>`. If :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>` equals the size of the loop, the loop is resized.

   :range: binary
   :feedback: Beatloop size spinbox changes

   .. versionadded:: 1.10.0
   .. versionchanged:: 2.1.0


.. mixxx:control:: [ChannelN],loop_in
                   [PreviewDeckN],loop_in
                   [SamplerN],loop_in

   If loop is disabled, sets the player loop in position to the current play position. If loop is enabled, press and hold to move loop in position to the current play position. If quantize is enabled, :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>` will be updated to reflect the new loop size.

   :range: binary
   :feedback: Loop-in marker changes on waveform.

   .. versionadded:: 1.8.0
   .. versionchanged:: 2.1.0


.. mixxx:control:: [ChannelN],loop_in_goto
                   [PreviewDeckN],loop_in_goto
                   [SamplerN],loop_in_goto

   Seek to the loop in point.

   :range: binary
   :feedback: Waveform position jumps

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],loop_out
                   [PreviewDeckN],loop_out
                   [SamplerN],loop_out

   If loop is disabled, sets the player loop out position to the current play position. If loop is enabled, press and hold to move loop out position to the current play position. If quantize is enabled, :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>` will be updated to reflect the new loop size.

   :range: binary
   :feedback: Loop-out marker changes on waveform.

   .. versionadded:: 1.8.0
   .. versionchanged:: 2.1.0


.. mixxx:control:: [ChannelN],loop_out_goto
                   [PreviewDeckN],loop_out_goto
                   [SamplerN],loop_out_goto

   Seek to the loop out point.

   :range: binary
   :feedback: Waveform position jumps

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],loop_move
                   [PreviewDeckN],loop_move
                   [SamplerN],loop_move

   Move loop forward by X beats (positive) or backward by X beats (negative).

   :range: real number
   :feedback: Loop moves forward or backward by X beats.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],loop_move_X_forward
                   [PreviewDeckN],loop_move_X_forward
                   [SamplerN],loop_move_X_forward

   Moves the loop in and out points forward by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64

   :range: binary
   :feedback: Loop moves forward by X beats.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],loop_move_X_backward
                   [PreviewDeckN],loop_move_X_backward
                   [SamplerN],loop_move_X_backward

   Loop moves by X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64

   :range: binary
   :feedback: Loop moves backward by X beats.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],loop_scale
                   [PreviewDeckN],loop_scale
                   [SamplerN],loop_scale

   Scale the loop length by the value scale is set to by moving the end marker. :mixxx:coref:`beatloop_size <[ChannelN],beatloop_size>` is not updated to reflect the change.

   :range: 0.0 - infinity
   :feedback: Loop length is scaled by given amount on waveform.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],loop_start_position
                   [PreviewDeckN],loop_start_position
                   [SamplerN],loop_start_position

   The player loop-in position in samples, -1 if not set.

   :range: positive integer
   :feedback: Loop-in marker changes on waveform.

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],orientation
                   [PreviewDeckN],orientation
                   [SamplerN],orientation

   Set channel orientation for the :term:`crossfader`.

   :range:
      ===== ===================================
      Value Meaning
      ===== ===================================
      0     Left side of crossfader
      1     Center (not affected by crossfader)
      2     Right side of crossfader
      ===== ===================================
   :feedback: None

   .. versionadded:: 1.9.0


.. mixxx:control:: [ChannelN],orientation_center
                   [PreviewDeckN],orientation_center
                   [SamplerN],orientation_center
                   [AuxiliaryN],orientation_center

   Assign channel to the center of the :term:`crossfader`.


.. mixxx:control:: [ChannelN],orientation_left
                   [PreviewDeckN],orientation_left
                   [SamplerN],orientation_left
                   [AuxiliaryN],orientation_left

   Assign channel to the left side of the :term:`crossfader`.


.. mixxx:control:: [ChannelN],orientation_right
                   [PreviewDeckN],orientation_right
                   [SamplerN],orientation_right
                   [AuxiliaryN],orientation_right

   Assign channel to the right side of the :term:`crossfader`.


.. mixxx:control:: [ChannelN],outro_end_activate
                   [PreviewDeckN],outro_end_activate
                   [SamplerN],outro_end_activate

   If the outro end cue is set, seeks the player to the outro end position. If the outro end is not set, sets the outro end to the current play position.

   :range: binary
   :feedback: Player may change position. Outro end marker may change on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],outro_end_clear
                   [PreviewDeckN],outro_end_clear
                   [SamplerN],outro_end_clear

   If the outro end cue is set, clears its status.

   :range: binary
   :feedback: Outro end marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],outro_end_enabled
                   [PreviewDeckN],outro_end_enabled
                   [SamplerN],outro_end_enabled

   1 if outro end cue is set, (position is not -1), 0 otherwise.

   :range: binary, read-only
   :feedback: Outro end button lights up.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],outro_end_position
                   [PreviewDeckN],outro_end_position
                   [SamplerN],outro_end_position

   The position of the outro end in samples, -1 if not set.

   :range: positive integer
   :feedback: Outro end marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],outro_end_set
                   [PreviewDeckN],outro_end_set
                   [SamplerN],outro_end_set

   Set outro end to the current play position. If outro end was previously set, it is moved to the new position.

   :range: binary
   :feedback: Outro end marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],outro_start_activate
                   [PreviewDeckN],outro_start_activate
                   [SamplerN],outro_start_activate

   If the outro start cue is set, seeks the player to the outro start position. If the outro start is not set, sets the outro start to the current play position.

   :range: binary
   :feedback: Player may change position. Outro start marker may change on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],outro_start_clear
                   [PreviewDeckN],outro_start_clear
                   [SamplerN],outro_start_clear

   If the outro start cue is set, clears its status.

   :range: binary
   :feedback: Outro start marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],outro_start_enabled
                   [PreviewDeckN],outro_start_enabled
                   [SamplerN],outro_start_enabled

   1 if outro start cue is set, (position is not -1), 0 otherwise.

   :range: binary, read-only
   :feedback: Outro start button lights up.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],outro_start_position
                   [PreviewDeckN],outro_start_position
                   [SamplerN],outro_start_position

   The position of the outro start in samples, -1 if not set.

   :range: positive integer
   :feedback: Outro start marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],outro_start_set
                   [PreviewDeckN],outro_start_set
                   [SamplerN],outro_start_set

   Set outro start to the current play position. If outro start was previously set, it is moved to the new position.

   :range: binary
   :feedback: Outro start marker changes on waveform.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],passthrough
                   [PreviewDeckN],passthrough
                   [SamplerN],passthrough

   Connects the vinyl control input for vinyl control on that deck to the channel output. Allows to mix external media into DJ sets.

   :range: binary
   :feedback: Passthrough label in the :term:`waveform overview` and passthrough button

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],PeakIndicator
                   [PreviewDeckN],PeakIndicator
                   [SamplerN],PeakIndicator

   Indicates when the signal is clipping (too loud for the hardware and is being distorted)

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Clip light

.. mixxx:control:: [ChannelN],PeakIndicatorL
                   [PreviewDeckN],PeakIndicatorL
                   [SamplerN],PeakIndicatorL

   Indicates when the signal is clipping (too loud for the hardware and is being distorted) for the left channel

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Clip light (left)

   .. versionadded:: 2.0.0

.. mixxx:control:: [ChannelN],PeakIndicatorR
                   [PreviewDeckN],PeakIndicatorR
                   [SamplerN],PeakIndicatorR


   Indicates when the signal is clipping (too loud for the hardware and is being distorted) for the right channel

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Clip light (right)

   .. versionadded:: 2.0.0

.. mixxx:control:: [ChannelN],pfl
                   [PreviewDeckN],pfl
                   [SamplerN],pfl

   Toggles :term:`headphone cueing (PFL) <PFL>`.

   :range: binary
   :feedback: Headphone button


.. mixxx:control:: [ChannelN],pitch
                   [PreviewDeckN],pitch
                   [SamplerN],pitch

   The total adjustment to the track's pitch, including changes from the rate slider if keylock is off as well as :mixxx:coref:`pitch_adjust <[ChannelN],pitch_adjust>`.

   .. note:: Do not map this to knobs or sliders on controllers; map :mixxx:coref:`pitch_adjust <[ChannelN],pitch_adjust>` instead.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: -6.0..6.0 semitones
   :feedback: Key display

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],pitch_up
                   [PreviewDeckN],pitch_up
                   [SamplerN],pitch_up

   Changes the track pitch up one half step, independent of the tempo.

   :range: binary
   :feedback: Key display

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],pitch_down
                   [PreviewDeckN],pitch_down
                   [SamplerN],pitch_down

   Changes the track pitch down one half step, independent of the tempo.

   :range: binary
   :feedback: Key display

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],pitch_adjust
                   [PreviewDeckN],pitch_adjust
                   [SamplerN],pitch_adjust

   Adjusts the pitch in addition to the :term:`tempo` slider pitch and keylock. It is reset after loading a new track.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: -3.0..3.0 semitones
   :feedback: Key display

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],play
                   [PreviewDeckN],play
                   [SamplerN],play

   Toggles playing or pausing the track.

   The value is set to 1 when the track is playing or when previewing from cue points and when the play command is adopted and track will be played after loading.

   :range: binary
   :feedback: Play/pause button


.. mixxx:control:: [ChannelN],play_indicator
                   [PreviewDeckN],play_indicator
                   [SamplerN],play_indicator

   Provides information to be bound with the a Play/Pause button e.g blinking when play is possible

   :range: binary, read-only
   :feedback: Play/pause button

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],play_latched
                   [PreviewDeckN],play_latched
                   [SamplerN],play_latched

   This is set to 1 when the track is playing, but not when previewing (see :mixxx:coref:`play <[ChannelN],play>`).

   :range: binary, read-only
   :feedback: Play/pause button

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],play_stutter
                   [PreviewDeckN],play_stutter
                   [SamplerN],play_stutter

   A play button without pause. Pushing while playing, starts play at :term:`cue point` again (Stutter).

   :range: binary
   :feedback: Play/Stutter button

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],playposition
                   [PreviewDeckN],playposition
                   [SamplerN],playposition

   Sets the absolute position in the track.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: -0.14 to 1.14 (0 = beginning -> Midi 14, 1 = end -> Midi 114)
   :feedback: Waveform


.. mixxx:control:: [ChannelN],pregain
                   [PreviewDeckN],pregain
                   [SamplerN],pregain

   Adjusts the pre-fader gain of the track (to avoid clipping)

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0.0..1.0..4.0
   :feedback: GAIN knob


.. mixxx:control:: [ChannelN],quantize
                   [PreviewDeckN],quantize
                   [SamplerN],quantize

   Aligns Hot-cues and Loop In & Out to the next beat from the current position.

   :range: binary
   :feedback: Hot-cues or Loop In/Out markers

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],rate
                   [PreviewDeckN],rate
                   [SamplerN],rate

   Speed control

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: -1.0..1.0
   :feedback: Speed slider


.. mixxx:control:: [ChannelN],rate_dir
                   [PreviewDeckN],rate_dir
                   [SamplerN],rate_dir

   Indicates orientation of speed slider.

   :range: -1 or 1


.. mixxx:control:: [ChannelN],rate_perm_down
                   [PreviewDeckN],rate_perm_down
                   [SamplerN],rate_perm_down

   Sets the speed one step lower (4 % default) lower

   :range: binary
   :feedback: Perm down button & Speed slider


.. mixxx:control:: [ChannelN],rate_perm_down_small
                   [PreviewDeckN],rate_perm_down_small
                   [SamplerN],rate_perm_down_small

   Sets the speed one small step lower (1 % default)

   :range: binary
   :feedback: Perm down button & Speed slider


.. mixxx:control:: [ChannelN],rate_perm_up
                   [PreviewDeckN],rate_perm_up
                   [SamplerN],rate_perm_up

   Sets the speed one step higher (4 % default)

   :range: binary
   :feedback: Perm up button & Speed slider


.. mixxx:control:: [ChannelN],rate_perm_up_small
                   [PreviewDeckN],rate_perm_up_small
                   [SamplerN],rate_perm_up_small

   Sets the speed one small step higher (1 % default)

   :range: binary
   :feedback: Perm up button & Speed slider


.. mixxx:control:: [ChannelN],rate_temp_down
                   [PreviewDeckN],rate_temp_down
                   [SamplerN],rate_temp_down

   Holds the speed one step lower while active

   :range: binary
   :feedback: Temp down button & Speed slider


.. mixxx:control:: [ChannelN],rate_temp_down_small
                   [PreviewDeckN],rate_temp_down_small
                   [SamplerN],rate_temp_down_small

   Holds the speed one small step lower while active

   :range: binary
   :feedback: Temp down button & Speed slider


.. mixxx:control:: [ChannelN],rate_temp_up
                   [PreviewDeckN],rate_temp_up
                   [SamplerN],rate_temp_up

   Holds the speed one step higher while active

   :range: binary
   :feedback: Temp up button & Speed slider


.. mixxx:control:: [ChannelN],rate_temp_up_small
                   [PreviewDeckN],rate_temp_up_small
                   [SamplerN],rate_temp_up_small

   Holds the speed one small step higher while active

   :range: binary
   :feedback: Temp up button & Speed slider


.. mixxx:control:: [ChannelN],rateRange
                   [PreviewDeckN],rateRange
                   [SamplerN],rateRange

   Sets the range of the Speed slider (0.08 = 8%)

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0.0..4.0
   :feedback: none, until you move the Speed slider


.. mixxx:control:: [ChannelN],rateSearch
                   [PreviewDeckN],rateSearch
                   [SamplerN],rateSearch

   Seeks forward (positive values) or backward (negative values) at a speed determined by the value

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: -300..300
   :feedback: Deck seeks


.. mixxx:control:: [ChannelN],rateEngine
                   [PreviewDeckN],rateEngine
                   [SamplerN],rateEngine

   Actual rate (used in visuals, not for control)


.. mixxx:control:: [ChannelN],reloop_andstop
                   [PreviewDeckN],reloop_andstop
                   [SamplerN],reloop_andstop

   Activate current loop, jump to its loop in point, and stop playback.

   :range: binary
   :feedback: Loop range in waveform activates or deactivates and play position moves to loop in point.

   .. versionadded:: 2.1.0

.. mixxx:control:: [ChannelN],reloop_toggle
                   [PreviewDeckN],reloop_toggle
                   [SamplerN],reloop_toggle

   Toggles the current loop on or off. If the loop is ahead of the current play position, the track will keep playing normally until it reaches the loop.

   :range: binary
   :feedback: Loop range in waveform activates or deactivates.

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],repeat
                   [PreviewDeckN],repeat
                   [SamplerN],repeat

   Enable repeat-mode for the specified deck

   :range: binary
   :feedback: when track finishes, song loops to beginning

   .. versionadded:: 1.9.0


.. mixxx:control:: [ChannelN],reset_key
                   [PreviewDeckN],reset_key
                   [SamplerN],reset_key

   Resets the key to the original track key.

   :range: binary

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],reverse
                   [PreviewDeckN],reverse
                   [SamplerN],reverse

   Toggles playing the track backwards

   :range: binary
   :feedback: REV button


.. mixxx:control:: [ChannelN],reverseroll
                   [PreviewDeckN],reverseroll
                   [SamplerN],reverseroll

   Enables reverse and slip mode while held (Censor)

   :range: binary
   :feedback: REV button

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],scratch2
                   [PreviewDeckN],scratch2
                   [SamplerN],scratch2

   Affects absolute play speed & direction whether currently playing or not when :mixxx:coref:`[ChannelN],scratch2_enabled` is active. (multiplicative). Use JavaScript ``engine.scratch`` functions to manipulate in controller mappings.

   :range: -3.0..3.0
   :feedback: Waveform

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],scratch2_enabled
                   [PreviewDeckN],scratch2_enabled
                   [SamplerN],scratch2_enabled

   Takes over play speed & direction for :mixxx:coref:`[ChannelN],scratch2`.

   :range: binary
   :feedback: Waveform

   .. versionadded:: 1.8.0


.. mixxx:control:: [ChannelN],slip_enabled
                   [PreviewDeckN],slip_enabled
                   [SamplerN],slip_enabled

   Toggles slip mode. When active, the playback continues muted in the background during a loop, scratch etc. Once disabled, the audible playback will resume where the track would have been.

   :range: binary
   :feedback: Slip mode button

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],stars_up
                   [PreviewDeckN],stars_up
                   [SamplerN],stars_up

   Increase the rating of the currently loaded track (if the skin has star widgets in the decks section).

   :range: binary
   :feedback: Star count is increased in the deck's star widget and in the library table.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],stars_down
                   [PreviewDeckN],stars_down
                   [SamplerN],stars_down

   Decrease the rating of the currently loaded track (if the skin has star widgets in the decks section).

   :range: binary
   :feedback: Star count is decreased in the deck's star widget and in the library table.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],start
                   [PreviewDeckN],start
                   [SamplerN],start

   Jump to start of track

   :range: binary
   :feedback: Track jumps to start


.. mixxx:control:: [ChannelN],start_play
                   [PreviewDeckN],start_play
                   [SamplerN],start_play

   Start playback from the beginning of the deck.

   :range: binary
   :feedback: Deck plays from beginning

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],start_stop
                   [PreviewDeckN],start_stop
                   [SamplerN],start_stop

   Seeks a player to the start and then stops it.

   :range: binary
   :feedback: Deck stops at the beginning.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],stop
                   [PreviewDeckN],stop
                   [SamplerN],stop

   Stops a player.

   :range: binary
   :feedback: Pause Button. Deck pauses at the current position.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],sync_enabled
                   [PreviewDeckN],sync_enabled
                   [SamplerN],sync_enabled

   Syncs the :term:`tempo` and :term:`phase` (depending on quantize) to that of the other track (if :term:`BPM` is detected on both). Click and hold for at least one second activates sync lock on that deck.

   :range: binary
   :feedback: If enabled, the :guilabel:`Sync` button stays lit and :term:`tempo` slider snap to the appropriate value. Slider adjustments are linked on all decks that have :term:`sync lock` enabled.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],sync_master
                   [PreviewDeckN],sync_master
                   [SamplerN],sync_master

   Sets deck as leader clock.

   :range: binary
   :feedback: If enabled, the :guilabel:`Sync` button stays lit and :term:`tempo` slider snap to the appropriate value. Slider adjustments are linked on all decks that have :term:`sync lock` enabled.

   .. versionadded:: 2.0.0
   .. versionchanged:: 2.3.0
      This button just enables :term:`sync lock` mode (similar to :mixxx:coref:`[ChannelN],sync_enabled`), it does not actually guarantee the deck will be the sync leader. This will be fixed in a future version.


.. mixxx:control:: [ChannelN],sync_mode
                   [PreviewDeckN],sync_mode
                   [SamplerN],sync_mode

   .. versionadded:: 2.0.0

   :range:
      ===== =============================
      Value Meaning
      ===== =============================
      0     :term:`Sync lock <sync lock>` disabled for that deck
      1     Deck is sync follower
      2     Deck is sync leader
      ===== =============================

.. mixxx:control:: [ChannelN],sync_key
                   [PreviewDeckN],sync_key
                   [SamplerN],sync_key

   :feedback: Key value widget

   Match musical key.

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],track_color
                   [PreviewDeckN],track_color
                   [SamplerN],track_color

   Color of the currently loaded track or -1 if no track is loaded or the track has no color.

   :range: 3-Byte :term:`RGB` color code (or -1)
   :feedback: Track color changes in the library view.

   .. versionadded:: 2.3.0


.. mixxx:control:: [ChannelN],track_loaded
                   [PreviewDeckN],track_loaded
                   [SamplerN],track_loaded

   Whether a track is loaded in the specified deck

   :range: binary, read-only
   :feedback: Waveform and track metadata shown in deck

   .. versionadded:: 2.1.0


.. mixxx:control:: [ChannelN],track_samplerate
                   [PreviewDeckN],track_samplerate
                   [SamplerN],track_samplerate

   Sample rate of the track loaded on the specified deck

   :range: absolute value, read-only
   :feedback: None

   .. versionadded:: 1.9.0


.. mixxx:control:: [ChannelN],track_samples
                   [PreviewDeckN],track_samples
                   [SamplerN],track_samples

   Number of sound samples in the track loaded on the specified deck

   :range: absolute value, read-only
   :feedback: None


.. mixxx:control:: [ChannelN],volume
                   [PreviewDeckN],volume
                   [SamplerN],volume


   Adjusts the channel volume fader

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Deck volume fader


.. mixxx:control:: [ChannelN],mute
                   [PreviewDeckN],mute
                   [SamplerN],mute

   Mutes the channel

   :range: binary
   :feedback: Mute button

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],vinylcontrol_enabled
                   [PreviewDeckN],vinylcontrol_enabled
                   [SamplerN],vinylcontrol_enabled

   Toggles whether a deck is being controlled by digital vinyl.

   :range: binary
   :feedback: When enabled, a vinyl indication should appear onscreen indicating green for enabled.

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],vinylcontrol_cueing
                   [PreviewDeckN],vinylcontrol_cueing
                   [SamplerN],vinylcontrol_cueing

   Determines how :term:`cue points <cue point>` are treated in vinyl control relative mode.

   :range:
      ===== =============================
      Value Meaning
      ===== =============================
      0     Cue points ignored
      1     One Cue - If needle is dropped after the :term:`cue point`, track will seek to that cue point
      2     Hot Cue - Track will seek to nearest previous :term:`hotcue`
      ===== =============================

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],vinylcontrol_mode
                   [PreviewDeckN],vinylcontrol_mode
                   [SamplerN],vinylcontrol_mode

   Determines how vinyl control interprets needle information.

   :range:
      ===== =====================================================================================
      Value Meaning
      ===== =====================================================================================
      0     Absolute Mode (track position equals needle position and speed)
      1     Relative Mode (track :term:`tempo` equals needle speed regardless of needle position)
      2     Constant Mode (track :term:`tempo` equals last known-steady tempo regardless of needle input
      ===== =====================================================================================

      See :ref:`Control Mode <vinyl-control-modes>` for details.

   :feedback: 3-way button indicates status

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],vinylcontrol_status
                   [PreviewDeckN],vinylcontrol_status
                   [SamplerN],vinylcontrol_status

   Provides visual feedback with regards to vinyl control status.

   :range: 0.0-3.0, read-only
   :feedback: Off for control disabled, green for control enabled, blinking yellow for when the needle reaches the end of the record, and red for needle skip detected

   .. versionadded:: 1.10.0


.. mixxx:control:: [ChannelN],visual_bpm
                   [PreviewDeckN],visual_bpm
                   [SamplerN],visual_bpm

   :term:`BPM` to display in the :term:`GUI` (updated more slowly than the actual BPM).

   :range: ?
   :feedback: :term:`BPM` value widget

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],visual_key
                   [PreviewDeckN],visual_key
                   [SamplerN],visual_key

   Current musical key after pitch shifting to display in the :term:`GUI` using the notation selected in the preferences

   :range: ?
   :feedback: Key value widget

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],visual_key_distance
                   [PreviewDeckN],visual_key_distance
                   [SamplerN],visual_key_distance

   The distance to the nearest key measured in cents

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: -0.5..0.5
   :feedback: Key value widget

   .. versionadded:: 2.0.0


.. mixxx:control:: [ChannelN],VuMeter
                   [PreviewDeckN],VuMeter
                   [SamplerN],VuMeter

   Outputs the current instantaneous deck volume

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Deck VU meter


.. mixxx:control:: [ChannelN],VuMeterL
                   [PreviewDeckN],VuMeterL
                   [SamplerN],VuMeterL

   Outputs the current instantaneous deck volume for the left channel

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Deck VU meter L


.. mixxx:control:: [ChannelN],VuMeterR
                   [PreviewDeckN],VuMeterR
                   [SamplerN],VuMeterR

   Outputs the current instantaneous deck volume for the right channel

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Deck VU meter R


.. mixxx:control:: [ChannelN],waveform_zoom
                   [PreviewDeckN],waveform_zoom
                   [SamplerN],waveform_zoom

   Zooms the waveform to look ahead or back as needed.

   :range: 1.0 - 10.0
   :feedback: Waveform zoom buttons

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],waveform_zoom_up
                   [PreviewDeckN],waveform_zoom_up
                   [SamplerN],waveform_zoom_up

   Waveform Zoom Out

   :range: ?
   :feedback: Waveform zoom buttons

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],waveform_zoom_down
                   [PreviewDeckN],waveform_zoom_down
                   [SamplerN],waveform_zoom_down

   Waveform Zoom In

   :range: ?
   :feedback: Waveform zoom buttons

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],waveform_zoom_set_default
                   [PreviewDeckN],waveform_zoom_set_default
                   [SamplerN],waveform_zoom_set_default

   Return to default waveform zoom level

   :range: ?
   :feedback: Waveform zoom buttons

   .. versionadded:: 1.11.0


.. mixxx:control:: [ChannelN],wheel
                   [PreviewDeckN],wheel
                   [SamplerN],wheel

   Affects relative playback speed and direction persistently (additive offset & must manually be undone).

   :range: -3.0..3.0
   :feedback: Waveform


Deprecated controls
+++++++++++++++++++

These controls have been deprecated, new controller mappings should use the alternatives.

.. mixxx:control:: [ChannelN],beatloop
                   [PreviewDeckN],beatloop
                   [SamplerN],beatloop

    Setup a loop over the set number of beats.

    :range: positive real number
    :feedback: A loop is shown over the set number of beats.

    .. deprecated:: 2.1.0
       Use :mixxx:coref:`[ChannelN],beatloop_size` and `[ChannelN],beatloop_toggle` instead.


.. mixxx:control:: [ChannelN],reloop_exit
                   [PreviewDeckN],reloop_exit
                   [SamplerN],reloop_exit

    Toggles the current loop on or off. If the loop is ahead of the current play position, the track will keep playing normally until it reaches the loop.

    :range: binary
    :feedback: Loop range in waveform activates or deactivates.

    .. deprecated:: 2.1.0
       Use :mixxx:coref:`[ChannelN],reloop_toggle` instead.


.. mixxx:control:: [ChannelN],jog
                   [PreviewDeckN],jog
                   [SamplerN],jog

    Affects relative playback speed and direction for short instances (additive & is automatically reset to 0).

    :range: -3.0..3.0
    :feedback: waveform

    .. deprecated:: ??
       Use the JavaScript ``engine.scratch`` functions instead.


.. mixxx:control:: [ChannelN],scratch
                   [PreviewDeckN],scratch
                   [SamplerN],scratch

    Affects playback speed and direction ([differently whether currently playing or not](https://bugs.launchpad.net/mixxx/+bug/530281)) (multiplicative).

    :range: -3.0..3.0
    :feedback: Waveform

    .. deprecated:: ??
       Use the JavaScript ``engine.scratch`` functions instead.


.. mixxx:control:: [ChannelN],filter
                   [PreviewDeckN],filter
                   [SamplerN],filter

    Toggles the filter effect.

    :range: binary
    :feedback: Filter button

    .. versionadded:: 2.0.0
    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[QuickEffectRack1_[ChannelN]_Effect1],enabled <[QuickEffectRack1_[ChannelI]_Effect1],enabled>` instead.


.. mixxx:control:: [ChannelN],filterDepth
                   [PreviewDeckN],filterDepth
                   [SamplerN],filterDepth

    Adjusts the intensity of the filter effect.

    :range: default
    :feedback: Filter depth knob

    .. versionadded:: 2.0.0
    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[QuickEffectRack1_[ChannelN]],super1 <[QuickEffectRack1_[ChannelI]],super1>` instead.


.. mixxx:control:: [ChannelN],filterLow
                   [PreviewDeckN],filterLow
                   [SamplerN],filterLow

    Adjusts the gain of the low :term:`EQ` filter.

    :range: 0.0..1.0..4.0
    :feedback: Low EQ knob

    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[EqualizerRack1_[ChannelN]_Effect1],parameter1 <[EqualizerRack1_[ChannelI]_Effect1],parameterK>` instead.


.. mixxx:control:: [ChannelN],filterLowKill
                   [PreviewDeckN],filterLowKill
                   [SamplerN],filterLowKill

    Holds the gain of the low :term:`EQ` to -inf while active

    :range: binary
    :feedback: Low EQ :term:`kill switch`

    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[EqualizerRack1_[ChannelI]_Effect1],button_parameter1 <[EqualizerRack1_[ChannelI]_Effect1],button_parameterK>` instead.


.. mixxx:control:: [ChannelN],filterMid
                   [PreviewDeckN],filterMid
                   [SamplerN],filterMid

    Adjusts the gain of the mid :term:`EQ` filter..

    :range: 0.0..1.0..4.0
    :feedback: Mid EQ knob

    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[EqualizerRack1_[ChannelI]_Effect1],parameter2 <[EqualizerRack1_[ChannelI]_Effect1],parameterK>` instead.


.. mixxx:control:: [ChannelN],filterMidKill
                   [PreviewDeckN],filterMidKill
                   [SamplerN],filterMidKill

    Holds the gain of the mid :term:`EQ` to -inf while active.

    :range: binary
    :feedback: Mid EQ :term:`kill switch`

    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[EqualizerRack1_[ChannelI]_Effect1],button_parameter2 <[EqualizerRack1_[ChannelI]_Effect1],button_parameterK>` instead.


.. mixxx:control:: [ChannelN],filterHigh
                   [PreviewDeckN],filterHigh
                   [SamplerN],filterHigh

    Adjusts the gain of the high :term:`EQ` filter.

    :range: 0.0..1.0..4.0
    :feedback: High EQ knob

    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[EqualizerRack1_[ChannelI]_Effect1],parameter3 <[EqualizerRack1_[ChannelI]_Effect1],parameterK>` instead.


.. mixxx:control:: [ChannelN],filterHighKill
                   [PreviewDeckN],filterHighKill
                   [SamplerN],filterHighKill

    Holds the gain of the high :term:`EQ` to -inf while active.

    :range: binary
    :feedback: High EQ :term:`kill switch`

    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[EqualizerRack1_[ChannelI]_Effect1],button_parameter3 <[EqualizerRack1_[ChannelI]_Effect1],button_parameterK>` instead.


.. mixxx:control:: [ChannelN],beatloop_X
                   [PreviewDeckN],beatloop_X
                   [SamplerN],beatloop_X

    Setup a loop over X beats. A control exists for X = 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64

    :range: toggle
    :feedback: A loop is shown over X beats.

    .. versionadded:: 1.10.0
    .. deprecated:: 2.0.0
       Use :mixxx:coref:`[ChannelN],beatloop_X_activate` instead.

.. _appendix-mixxxcontrols-samplers:

Global Sampler controls
+++++++++++++++++++++++

These controls can be used to control all samplers.

.. mixxx:control:: [Samplers],show_samplers

   :range: binary
   :feedback: Shows Sampler bank(s)

.. mixxx:control:: [Sampler],SaveSamplerBank

   Save sampler configuration. Make currently loaded tracks in samplers instantly available at a later point.

   :range: binary
   :feedback: Opens file dialog. Configuration file can be named and saved.

   .. versionadded: 2.0.0


.. mixxx:control:: [Sampler],LoadSamplerBank

   Load saved sampler configuration file and add tracks to the available samplers.

   :range: binary
   :feedback: Opens file dialog. Select configuration file.

   .. versionadded: 2.0.0


.. _appendix-mixxxcontrols-aux:

Microphones and Auxiliary Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In contrast to :ref:`decks, preview decks and samplers <appendix-mixxxcontrols-decks>`, microphones and auxiliary channels are input channels.
You can map audio interface's inputs to mixxx's auxiliary input channels and connect external audio source to it (cellphone, mp3 player).
Then you can use your :term:`MIDI` controller to control its volume and some other parameters (orientation, gain, :term:`volume`), apply effects and use the prelisten function.

.. note:: Although the first auxiliary group is named :mixxx:cogroupref:`[Auxiliary1]`, the group for the first microphone is just called :mixxx:cogroupref:`[Microphone] <[MicrophoneN]>`, not :mixxx:cogroupref:`[Microphone1] <[MicrophoneN]>`.

.. mixxx:control:: [MicrophoneN],enabled
                   [AuxiliaryN],enabled

   1 if a channel input is enabled, 0 if not.

   :range: binary
   :feedback: Microphone is enabled.

   .. versionadded:: 1.10.0
   .. deprecated:: 2.0.0
      Use :mixxx:coref:`[MicrophoneN],input_configured` instead.


.. mixxx:control:: [MicrophoneN],input_configured
                   [AuxiliaryN],input_configured

   1 if there is input is configured for this channel, 0 if not.

   :range: binary, read-only
   :feedback: Configured channel in the sound preferences.


.. mixxx:control:: [MicrophoneN],master
                   [AuxiliaryN],master

   Hold value at 1 to mix channel input into the master output.
   For :mixxx:cogroupref:`[MicrophoneN]` use :mixxx:coref:`[MicrophoneN],talkover` instead.
   Note that :mixxx:cogroupref:`[AuxiliaryN]` also take :mixxx:coref:`[AuxiliaryN],orientation` into account.

   :range: binary
   :feedback: Auxiliary: Play button
              Microphone: N/A


.. mixxx:control:: [AuxiliaryN],orientation

   Set channel orientation for the :term:`crossfader`.

   :range:
      ===== ===================================
      Value Meaning
      ===== ===================================
      0     Left side of crossfader
      1     Center (not affected by crossfader)
      2     Right side of crossfader
      ===== ===================================
   :feedback: None

   .. versionadded:: 1.10.0

.. mixxx:control:: [MicrophoneN],orientation

   .. versionadded:: 1.10.0
   .. deprecated:: 1.10.0

      The control is not processed in the Mixer, which is also why there are no orientation controls for Microphones in the GUI.


.. mixxx:control:: [MicrophoneN],PeakIndicator
                   [AuxiliaryN],PeakIndicator

   Indicates when the signal is clipping (too loud for the hardware and is being distorted)

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Microphone Clip light

   .. versionadded:: 1.10.0


.. mixxx:control:: [MicrophoneN],PeakIndicatorL
                   [AuxiliaryN],PeakIndicatorL

   Indicates when the signal is clipping (too loud for the hardware and is being distorted) for the left channel

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Clip light (left)

   .. versionadded:: 2.0.0

.. mixxx:control:: [MicrophoneN],PeakIndicatorR
                   [AuxiliaryN],PeakIndicatorR


   Indicates when the signal is clipping (too loud for the hardware and is being distorted) for the right channel

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: binary
   :feedback: Clip light (right)

   .. versionadded:: 2.0.0

.. mixxx:control:: [MicrophoneN],pfl
                   [AuxiliaryN],pfl

   Toggles :term:`headphone cueing (PFL) <PFL>`.

   :range: binary
   :feedback: Headphone button


.. mixxx:control:: [MicrophoneN],talkover
                   [AuxiliaryN],talkover

   Hold value at 1 to mix channel input into the master output.
   For :mixxx:cogroupref:`[AuxiliaryN]` use :mixxx:coref:`[AuxiliaryN],master` instead.
   Note that :mixxx:cogroupref:`[AuxiliaryN]` also take :mixxx:coref:`[AuxiliaryN],orientation` into account.

   :range: binary
   :feedback: Microphone: Talk button
              Auxiliary: N/A

   .. versionadded:: 1.10.0


.. mixxx:control:: [MicrophoneN],volume
                   [AuxiliaryN],volume

   Adjusts the channel volume fader

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Microphone volume fader changes

   .. versionadded:: 1.10.0


.. mixxx:control:: [MicrophoneN],pregain
                   [AuxiliaryN],pregain

   Adjusts the gain of the input

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0.0..1.0..4.0
   :feedback: Microphone gain knob


.. mixxx:control:: [MicrophoneN],mute
                   [AuxiliaryN],mute

   Mutes the channel

   :range: binary
   :feedback: Mute button

   .. versionadded:: 2.0.0


.. mixxx:control:: [MicrophoneN],VuMeter
                   [AuxiliaryN],VuMeter

   Outputs the current instantaneous channel volume

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Microphone VU meter changes

   .. versionadded:: 1.10.0


.. mixxx:control:: [MicrophoneN],VuMeterL
                   [AuxiliaryN],VuMeterL

   Outputs the current instantaneous deck volume for the left channel

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Deck VU meter L

   .. versionadded:: 2.0.0


.. mixxx:control:: [MicrophoneN],VuMeterR
                   [AuxiliaryN],VuMeterR

   Outputs the current instantaneous deck volume for the right channel

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: default
   :feedback: Deck VU meter R

   .. versionadded:: 2.0.0


The ``[VinylControl]`` group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :mixxx:cogroupref:`[VinylControl]` group can toggle the :ref:`vinyl control feature <vinyl-control>`.

.. mixxx:control:: [VinylControl],Toggle

   Moves control by a vinyl control signal from one deck to another if using the single deck vinyl control (VC) feature.

   :range: binary
   :feedback: If VC isn't enabled on any decks, enable it on the first one we're receiving samples for. If VC is enabled on a single (exclusive) deck, and another deck is setup to receive samples, disable it on the former deck and enable it on the next eligible deck (ordered by deck number). If VC is enabled on multiple decks, don't do anything.

   .. versionadded:: 1.10.0


.. mixxx:control:: [VinylControl],show_vinylcontrol

   Toggle the vinyl control section in skins.

   :range: binary
   :feedback: Vinyl controls are shown

   .. versionadded:: 1.10.0


.. mixxx:control:: [VinylControl],gain

   Allows to amplify the "phono" level of attached turntables to "line" level.
   This is equivalent to setting the :ref:`turntable boost <vinyl-control-config-gain>` in :menuselection:`Options --> Preferences --> Vinyl Control`

   :range: binary
   :feedback: position of Boost slider in :menuselection:`Options --> Preferences --> Vinyl Control` (is not updated while viewing this Preferences page)

   .. versionadded:: 1.10.0

The ``[Recording]`` controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The controls in the :mixxx:cogroupref:`[Recording]` group can be used to query and control the :ref:`recording of your mix <djing-recording-your-mix>`.

.. mixxx:control:: [Recording],toggle_recording

   Turns recording on or off.

   :range: binary
   :feedback: Recording icon


.. mixxx:control:: [Recording],status

   Indicates whether Mixxx is currently recording.

   :range:
      ===== ====================
      Value Meaning
      ===== ====================
      0     Recording Stopped
      1     Initialize Recording
      2     Recording Active
      ===== ====================
   :feedback: Recording icon


AutoDJ controls
~~~~~~~~~~~~~~~

The :mixxx:cogroupref:`[AutoDJ]` controls allow interacting with :ref:`AutoDJ <library-auto-dj>`.

.. mixxx:control:: [AutoDJ],enabled

   Turns Auto DJ on or off.

   :range: binary
   :feedback: AutoDJ button

   .. versionadded:: 1.11.0


.. mixxx:control:: [AutoDJ],shuffle_playlist

   Shuffles the content of the Auto DJ playlist.

   :range: binary
   :feedback: Order of tracks in the AutoDJ playlist changes.

   .. versionadded:: 1.11.0


.. mixxx:control:: [AutoDJ],skip_next

   Skips the next track in the Auto DJ playlist.

   :range: binary
   :feedback: Skipped track is removed from the AutoDJ playlist.

   .. versionadded:: 1.11.0


.. mixxx:control:: [AutoDJ],fade_now

   Triggers the transition to the next track.

   :range: binary
   :feedback: Crossfader slider moves to the other side.

   .. versionadded:: 1.11.0


The ``[Library]`` controls
~~~~~~~~~~~~~~~~~~~~~~~~~~

The controls in the :mixxx:cogroupref:`[Library]` group can be used to navigate the :ref:`library <library-interface>`.
Note that :mixxx:coref:`[Library],MoveUp` and other Move and Scroll controls emulate keypresses and therefore require the Mixxx window to be focused.

.. mixxx:control:: [Library],MoveUp

   Equivalent to pressing the :kbd:`Up` key on the keyboard

   :range: Binary
   :feedback: Currently selected item changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],MoveDown

   Equivalent to pressing the :kbd:`Down` key on the keyboard

   :range: Binary
   :feedback: Currently selected item changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],MoveVertical

   Move the specified number of locations up or down. Intended to be mapped to an encoder knob.

   :range: Relative (positive values move down, negative values move up)
   :feedback: Currently selected item changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],ScrollUp

   Equivalent to pressing the :kbd:`PageUp` key on the keyboard

   :range: Binary
   :feedback: Currently selected item changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],ScrollDown

   Equivalent to pressing the :kbd:`PageDown` key on the keyboard

   :range: Binary
   :feedback: Currently selected item changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],ScrollVertical

   Scroll the specified number of pages up or down. Intended to be mapped to an encoder knob.

   :range: Relative (positive values move down, negative values move up)
   :feedback: Currently selected item changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],MoveLeft

   Equivalent to pressing the :kbd:`Left` key on the keyboard

   :range: Binary
   :feedback: Currently selected item changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],MoveRight

   Equivalent to pressing the :kbd:`Right` key on the keyboard

   :range: Binary
   :feedback: Currently selected item changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],MoveHorizontal

   Move the specified number of locations left or right. Intended to be mapped to an encoder knob.

   :range: Relative (positive values move right, negative values move left)
   :feedback: Currently selected item changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],MoveFocusForward

   Equivalent to pressing the :kbd:`Tab` key on the keyboard

   :range: Binary
   :feedback: Currently focused pane changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],MoveFocusBackward

   Equivalent to pressing the :kbd:`Shift` + :kbd:`Tab` key on the keyboard

   :range: Binary
   :feedback: Currently focused pane changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],MoveFocus

   Move focus the specified number of panes forward or backwards. Intended to be mapped to an encoder knob.

   :range: Relative (positive values move forward, negative values move backward)
   :feedback: Currently focused pane changes

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],GoToItem

   Triggers different actions, depending on which interface element currently has keyboard focus:

   ========================  =============================================================================================================
   **Search bar**
   ---------------------------------------------------------------------------------------------------------------------------------------
   text box                  moves focus to tracks table
   ------------------------  -------------------------------------------------------------------------------------------------------------
   Clear button              clears search text
   ------------------------  -------------------------------------------------------------------------------------------------------------
   **Sidebar**
   ---------------------------------------------------------------------------------------------------------------------------------------
   collapsed node            expands the item (except Tracks and Auto DJ)
   ------------------------  -------------------------------------------------------------------------------------------------------------
   leaf node                 moves focus to tracks table
   ------------------------  -------------------------------------------------------------------------------------------------------------
   **Tracks table**          Performs the action selected in :menuselection:`Preferences --> Library --> Track Double-Click Action` (default is "Load selected track"). Also see :menuselection:`Preferences --> Decks --> Playing track protection`
   ------------------------  -------------------------------------------------------------------------------------------------------------
   **Dialogs / popups**      presses :kbd:`Enter`. Note: the :mixxx:coref:`Move.. <[Library],MoveUp>` controls allow to move button focus.
   ========================  =============================================================================================================

   :range: Binary
   :feedback: Context dependent

   .. versionadded:: 2.1.0


.. mixxx:control:: [Library],AutoDjAddBottom
                   [Playlist],AutoDjAddBottom

   Add selected track(s) to Auto DJ Queue (bottom).

   :range: Binary
   :feedback: Append track(s) to Auto DJ playlist

   .. versionadded:: 2.0.0


.. mixxx:control:: [Library],AutoDjAddTop
                   [Playlist],AutoDjAddTop

   Add selected track(s) to Auto DJ Queue (top).

   :range: Binary
   :feedback: Prepend track(s) to Auto DJ playlist

   .. versionadded:: 2.0.0


.. mixxx:control:: [Library],show_coverart

   Toggle the Cover Art in Library

   :range: Binary


.. mixxx:control:: [Library],font_size_increment

   Increase the size of the library font. If the row height is smaller than the font-size the larger of the two is used.

   :range: Binary
   :feedback: Library view

   .. versionadded:: 2.0.0


.. mixxx:control:: [Library],font_size_decrement

   Decrease the size of the library font

   .. versionadded:: 2.0.0

   :range: Binary
   :feedback: Library view


.. mixxx:control:: [Library],font_size_knob

   Increase or decrease the size of the library font

   .. versionadded:: 2.0.0

   :range: Relative
   :feedback: Library view


.. mixxx:control:: [Library],sort_column


   Indicates the sorting column the track table

   :range:
     ===== ================== ============ ======== ===== ======
     Value Description        Library      Playlist Crate Browse
     ===== ================== ============ ======== ===== ======
     1     Artist             X            X        X     X
     2     Title              X            X        X     X
     3     Album              X            X        X     X
     4     Albumartist        X            X        X     X
     5     Year               X            X        X     X
     6     Genre              X            X        X     X
     7     Composer           X            X        X     X
     8     Grouping           X            X        X     X
     9     Tracknumber        X            X        X     X
     10    Filetype           X            X        X     X
     11    Native Location    X            X        X     X
     12    Comment            X            X        X     X
     13    Duration           X            X        X     X
     14    Bitrate            X            X        X     X
     15    BPM                X            X        X     X
     16    ReplayGain         X            X        X     X
     17    Datetime Added     X            X        X     X
     18    Times Played       X            X        X     X
     19    Rating             X            X        X     X
     20    Key                X            X        X     X
     21    Preview            X            X        X     X
     22    Coverart           X            X        X
     23    Position                        X
     24    Playlist ID                     X
     25    Location                        X
     26    Filename                                       X
     27    File Modified Time                             X
     28    File Creation Time                             X
     29    Sample Rate
     30    Track Color        X            X        X
     ===== ================== ============ ======== ===== ======

   :feedback: Sorting indicator in the column headers of the track table

   .. versionadded:: 2.3.0


.. mixxx:control:: [Library],sort_column_toggle

   Equivalent to clicking on column headers. A new value sets :mixxx:coref:`[Library],sort_column` to that value and :mixxx:coref:`[Library],sort_order` to 0, setting the same value again will toggle :mixxx:coref:`[Library],sort_order`.

   :range: Same as for :mixxx:coref:`[Library],sort_column` or value 0 for sorting according the current column with the cursor on it
   :feedback: Sorting indicator in the column headers of the track table

   .. versionadded:: 2.3.0


.. mixxx:control:: [Library],sort_order

   Indicate the sort order of the track tables.

   :range: Binary (0 for ascending, 1 for descending)
   :feedback: Sorting indicator in the column headers of the track table

   .. versionadded:: 2.3.0


.. mixxx:control:: [Library],track_color_prev

   Set color of selected track to previous color in palette.

   :range: Binary
   :feedback: Track color changes in the library view.

   .. versionadded:: 2.3.0


.. mixxx:control:: [Library],track_color_next

   Set color of selected track to next color in palette.

   :range: Binary
   :feedback: Track color changes in the library view.

   .. versionadded:: 2.3.0

The ``[Shoutcast]`` controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mixxx:control:: [Shoutcast],enabled

   Shows if live Internet broadcasting is enabled.

   :range: ?
   :feedback: shoutcast only supports mp3 format as field


.. mixxx:control:: [Shoutcast],status

   This control displays whether broadcasting connection to Shoutcast server was successfully established.

   :range: binary
   :feedback: None


The ``[Playlist]`` controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:mixxx:cogroupref:`[Playlist]` controls allow navigating the sidebar and tracks table directly without considering
the currently focused widget. This is helpful when another application's window is focused.
This group is going to be deprecated at some point, with its controls added to ``[Library]`` above.

.. seealso::
   See `bug \#1772184 <https://bugs.launchpad.net/mixxx/+bug/1772184>`__ for the current status.


.. mixxx:control:: [Playlist],SelectPlaylist

   Scrolls the given number of items (view, playlist, crate, etc.) in the side pane (can be negative for reverse direction).

   :range: relative value
   :feedback: Library sidebar highlight


.. mixxx:control:: [Playlist],SelectTrackKnob

   Scrolls the given number of tracks in the track table (can be negative for reverse direction).

   :range: relative value
   :feedback: Library track table highlight


.. mixxx:control:: [Playlist],LoadSelectedIntoFirstStopped
    :range: binary
    :feedback: Waveform view

    Loads the currently highlighted song into the first stopped deck

    .. deprecated:: 2.1.0
       Use :mixxx:coref:`[Library],GoToItem` instead.


.. mixxx:control:: [Playlist],SelectNextPlaylist
    :range: binary
    :feedback: Library sidebar

    Switches to the next view (Library, Queue, etc.)

    .. deprecated:: 2.1.0
       Use :mixxx:coref:`[Library],MoveDown` instead.


.. mixxx:control:: [Playlist],SelectPrevPlaylist

    :range: binary
    :feedback: Library sidebar

   Switches to the previous view (Library, Queue, etc.)

    .. deprecated:: 2.1.0
       Use :mixxx:coref:`[Library],MoveUp` instead.


.. mixxx:control:: [Playlist],ToggleSelectedSidebarItem
    :range: binary
    :feedback: Library sidebar

    Toggles (expands/collapses) the currently selected sidebar item.

    .. versionadded:: 1.11.0
    .. deprecated:: 2.1.0
       Use :mixxx:coref:`[Library],GoToItem` instead.


.. mixxx:control:: [Playlist],SelectNextTrack
    :range: binary
    :feedback: Library track table highlight

    Scrolls to the next track in the track table.

    .. deprecated:: 2.1.0
       Use :mixxx:coref:`[Library],MoveDown` instead.


.. mixxx:control:: [Playlist],SelectPrevTrack
    :range: binary
    :feedback: Library track table highlight

    Scrolls to the previous track in the track table.

    .. deprecated:: 2.1.0
       Use :mixxx:coref:`[Library],MoveUp` instead.



The ``[Controls]`` controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :mixxx:cogroupref:`[Controls]` group contains controls that didn't fit in any other group.

.. mixxx:control:: [Controls],touch_shift

   Once enabled, all touch tab events are interpreted as right click. This control has been added to provide touchscreen compatibility in 2.0 and might be replaced by a general modifier solution in the future.

   :range: binary
   :feedback: All Widgets

   .. versionadded:: 2.0.0


.. mixxx:control:: [Controls],AutoHotcueColors

   If enabled, colors will be assigned to newly created :term:`hotcues <hotcue>` automatically.

   :range: binary
   :feedback: None

   .. versionadded:: 2.3.0

.. mixxx:control:: [Controls],ShowDurationRemaining

   Represents the current state of the remaining time duration display of the loaded track.

   :range:
      ===== ===========================================================================
      Value Meaning
      ===== ===========================================================================
      0     currently showing elapsed time, sets to remaining time
      1     currently showing remaining time , sets to elapsed time
      2     currently showing both (that means we are showing remaining, set to elapsed
      ===== ===========================================================================
   :feedback: None

.. _appendix-mixxxcontrols-effects:

The Effects Framework
~~~~~~~~~~~~~~~~~~~~~

In the list below,

 *  EffectRack1 leaves room for future expansion to multiple EffectRacks.
 *  N ranges from 1 to ``[EffectRack1],num_effectunits``, inclusive.
 *  M ranges from 1 to ``[EffectRack1_EffectUnitN],num_effectslots``, inclusive. (For a given value of N)
 *  K ranges from 1 to ``[EffectRack1_EffectUnitN_EffectM],num_parameters``, inclusive.  (For given values of N and M)
 *  I ranges from 1 to ``[Master],num_decks``, inclusive.
 *  J ranges from 1 to ``[Master],num_samplers``, inclusive.

.. versionadded:: 2.0.0

Linking Values
++++++++++++++

Effect parameters can be linked to the effect's metaknob.
This linkage can be user-controlled by changing the ``link_type`` and the ``link_inverse`` control of the parameter.
The default link type is loaded from the effect parameter's manifest's ``linkHint`` property.

=================  =============  ============================================
Link Type          Integer Value  Interpretation
=================  =============  ============================================
None               0              Not controlled by the metaknob
Linked             1              Controlled by the metaknob as it is
Linked Left        2              Controlled by the left side of the metaknob
Linked Right       3              Controlled by the right side of the metaknob
Linked Left Right  4              Controlled by both sides of the metaknob
=================  =============  ============================================

============  =============  ==============================
Link Inverse  Integer Value  Interpretation
============  =============  ==============================
Normal        0              Linked in equal relation
Inverse       1              Linked in an inverse relation.
============  =============  ==============================


EQs and Filters
+++++++++++++++

:term:`Equalizers <EQ>` and filters are special effects units.
The EQs are controlled by :mixxx:cogroupref:`[EqualizerRack1_[ChannelI]_Effect1]` and the filter knob is controlled by :mixxx:coref:`[QuickEffectRack1_[ChannelI]],super1` and :mixxx:coref:`[QuickEffectRack1_[ChannelI]_Effect1],enabled`.
Users can choose between several options for the effects loaded in these racks in the Equalizers section of the Preferences window.


Controls
++++++++

.. mixxx:control:: [EffectRack1],show

   Show the Effect Rack

   :range: binary


.. mixxx:control:: [EffectRack1],num_effectunits
                   [EqualizerRack1],num_effectunits
                   [QuickEffectRack1],num_effectunits

   The number of EffectUnits in this rack

   :range: integer, read-only


.. mixxx:control:: [EffectRack1],clear
                   [EqualizerRack1],clear
                   [QuickEffectRack1],clear

   Clear the Effect Rack

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN],chain_selector
                   [EqualizerRack1_[ChannelI]],chain_selector
                   [QuickEffectRack1_[ChannelI]],chain_selector

   Select EffectChain preset. \> 0 goes one forward; \< 0 goes one backward.

   :range: +1/-1


.. mixxx:control:: [EffectRack1_EffectUnitN],clear
                   [EqualizerRack1_[ChannelI]],clear
                   [QuickEffectRack1_[ChannelI]],clear

   Clear the currently loaded EffectChain in this EffectUnit.

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN],enabled
                   [EqualizerRack1_[ChannelI]],enabled
                   [QuickEffectRack1_[ChannelI]],enabled

   If true, the EffectChain in this EffectUnit will be processed. Meant to allow the user a quick toggle for the effect unit.

   :range: binary, default true


.. mixxx:control:: [EffectRack1_EffectUnitN],focused_effect
                   [EqualizerRack1_[ChannelI]],focused_effect
                   [QuickEffectRack1_[ChannelI]],focused_effect

   0 indicates no effect is focused; \> 0 indicates the index of the focused effect. Focusing an effect only does something if a controller mapping changes how it behaves when an effect is focused.

   :range: 0..num_effects


.. mixxx:control:: [EffectRack1_EffectUnitN],group_[ChannelI]_enable
                   [EqualizerRack1_[ChannelI]],group_[ChannelI]_enable
                   [QuickEffectRack1_[ChannelI]],group_[ChannelI]_enable

   Whether or not this EffectChain applies to Deck I

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN],group_[Headphone]_enable

   Whether or not this EffectChain applies to the Headphone output

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN],group_[Master]_enable

   Whether or not this EffectChain applies to the Master output

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN],group_[SamplerJ]_enable

   Whether or not this EffectChain applies to Sampler J

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN],loaded
                   [EqualizerRack1_[ChannelI]],loaded
                   [QuickEffectRack1_[ChannelI]],loaded

   Whether an EffectChain is loaded into the EffectUnit

   :range: binary, read-only


.. mixxx:control:: [EffectRack1_EffectUnitN],mix
                   [EqualizerRack1_[ChannelI]],mix
                   [QuickEffectRack1_[ChannelI]],mix

   The dry/wet mixing ratio for this EffectChain with the EngineChannels it is mixed with

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0.0..1.0


.. mixxx:control:: [EffectRack1_EffectUnitN],next_chain
                   [EqualizerRack1_[ChannelI]],next_chain
                   [QuickEffectRack1_[ChannelI]],next_chain

   Cycle to the next EffectChain preset after the currently loaded preset.

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN],num_effects
                   [EqualizerRack1_[ChannelI]],num_effects
                   [QuickEffectRack1_[ChannelI]],num_effects

   The number of Effects that this EffectChain has

   :range: integer, read-only


.. mixxx:control:: [EffectRack1_EffectUnitN],num_effectslots
                   [EqualizerRack1_[ChannelI]],num_effectslots
                   [QuickEffectRack1_[ChannelI]],num_effectslots

   The number of effect slots available in this EffectUnit.

   :range: integer, read-only


.. mixxx:control:: [EffectRack1_EffectUnitN],prev_chain
                   [EqualizerRack1_[ChannelI]],prev_chain
                   [QuickEffectRack1_[ChannelI]],prev_chain

   Cycle to the previous EffectChain preset before the currently loaded preset.

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN],show_focus
                   [EqualizerRack1_[ChannelI]],show_focus
                   [QuickEffectRack1_[ChannelI]],show_focus

   Whether to show focus buttons and draw a border around the focused effect in skins. This should not be manipulated by skins; it should only be changed by controller mappings.

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN],show_parameters
                   [EqualizerRack1_[ChannelI]],show_parameters
                   [QuickEffectRack1_[ChannelI]],show_parameters

   :range: binary

   Whether to show all the parameters of each effect in skins or only show metaknobs.


.. mixxx:control:: [EffectRack1_EffectUnitN],super1
                   [EqualizerRack1_[ChannelI]],super1
                   [QuickEffectRack1_[ChannelI]],super1

   The EffectChain superknob. Moves the metaknobs for each effect in the chain.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0.0..1.0


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],clear
                   [EqualizerRack1_[ChannelI]_Effect1],clear
                   [QuickEffectRack1_[ChannelI]_Effect1],clear

   Clear the currently loaded Effect in this Effect slot from the EffectUnit.

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],effect_selector
                   [EqualizerRack1_[ChannelI]_Effect1],effect_selector
                   [QuickEffectRack1_[ChannelI]_Effect1],effect_selector

   Select Effect -- \>0 goes one forward, \<0 goes one backward.

   :range: +1/-1


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],enabled
                   [EqualizerRack1_[ChannelI]_Effect1],enabled
                   [QuickEffectRack1_[ChannelI]_Effect1],enabled

   If true, the effect in this slot will be processed. Meant to allow the user a quick toggle for this effect.

   :range: binary, default true


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],loaded
                   [EqualizerRack1_[ChannelI]_Effect1],loaded
                   [QuickEffectRack1_[ChannelI]_Effect1],loaded

   Whether an Effect is loaded into this EffectSlot

   :range: binary, read-only


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],next_effect
                   [EqualizerRack1_[ChannelI]_Effect1],next_effect
                   [QuickEffectRack1_[ChannelI]_Effect1],next_effect

   Cycle to the next effect after the currently loaded effect.

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],num_parameters
                   [EqualizerRack1_[ChannelI]_Effect1],num_parameters
                   [QuickEffectRack1_[ChannelI]_Effect1],num_parameters

   The number of parameters the currently loaded effect has.

   :range: integer, read-only,  0 if no effect is loaded


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],num_parameterslots
                   [EqualizerRack1_[ChannelI]_Effect1],num_parameterslots
                   [QuickEffectRack1_[ChannelI]_Effect1],num_parameterslots

   The number of parameter slots available.

   :range: integer, read-only


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],num_button_parameters
                   [EqualizerRack1_[ChannelI]_Effect1],num_button_parameters
                   [QuickEffectRack1_[ChannelI]_Effect1],num_button_parameters

   The number of button parameters the currently loaded effect has.

   :range: integer, read-only, 0 if no effect is loaded


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],num_button_parameterslots
                   [EqualizerRack1_[ChannelI]_Effect1],num_button_parameterslots
                   [QuickEffectRack1_[ChannelI]_Effect1],num_button_parameterslots

   The number of button parameter slots available.

   :range: integer, read-only


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],meta
                   [EqualizerRack1_[ChannelI]_Effect1],meta
                   [QuickEffectRack1_[ChannelI]_Effect1],meta

   Controls the parameters that are linked to the metaknob.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: 0..1


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],prev_effect
                   [EqualizerRack1_[ChannelI]_Effect1],prev_effect
                   [QuickEffectRack1_[ChannelI]_Effect1],prev_effect

   Cycle to the previous effect before the currently loaded effect.

   :range: binary


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],parameterK
                   [EqualizerRack1_[ChannelI]_Effect1],parameterK
                   [QuickEffectRack1_[ChannelI]_Effect1],parameterK

   The scaled value of the Kth parameter.
   See the `Parameter Values <https://github.com/mixxxdj/mixxx/wiki/Effects-Framework#user-content-parameter-values>`__ section for more information.

   This is a :ref:`ControlPotMeter control <appendix-mixxxcontrols-controlpotmeter>`.

   :range: double


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],parameterK_link_inverse
                   [EqualizerRack1_[ChannelI]_Effect1],parameterK_link_inverse
                   [QuickEffectRack1_[ChannelI]_Effect1],parameterK_link_inverse

   The link direction of the Kth parameter to the effect's metaknob.

   :range: bool


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],parameterK_link_type
                   [EqualizerRack1_[ChannelI]_Effect1],parameterK_link_type
                   [QuickEffectRack1_[ChannelI]_Effect1],parameterK_link_type

   The link type of the Kth parameter to the effects's metaknob.

   :range: enum


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],parameterK_loaded
                   [EqualizerRack1_[ChannelI]_Effect1],parameterK_loaded
                   [QuickEffectRack1_[ChannelI]_Effect1],parameterK_loaded

   Whether or not the Kth parameter slot has an effect parameter loaded into it.

   :range: binary, read-only


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],parameterK_type
                   [EqualizerRack1_[ChannelI]_Effect1],parameterK_type
                   [QuickEffectRack1_[ChannelI]_Effect1],parameterK_type

   The type of the Kth parameter value. See the Parameter Value Types table.

   :range: integer, read-only


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],button_parameterK
                   [EqualizerRack1_[ChannelI]_Effect1],button_parameterK
                   [QuickEffectRack1_[ChannelI]_Effect1],button_parameterK

   The value of the Kth parameter. See the Parameter Values section for more information.

   :range: double


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],button_parameterK_loaded
                   [EqualizerRack1_[ChannelI]_Effect1],button_parameterK_loaded
                   [QuickEffectRack1_[ChannelI]_Effect1],button_parameterK_loaded

   Whether or not the Kth parameter slot has an effect parameter loaded into it.

   :range: binary, read-only


.. mixxx:control:: [EffectRack1_EffectUnitN_EffectM],button_parameterK_type
                   [EqualizerRack1_[ChannelI]_Effect1],button_parameterK_type
                   [QuickEffectRack1_[ChannelI]_Effect1],button_parameterK_type

   The type of the Kth parameter value. See the Parameter Value Types table.

   :range: integer, read-only


Removed controls
~~~~~~~~~~~~~~~~

These controls have been removed from Mixxx. Skins and controller mappings that attempt to use them will not work correctly.

.. mixxx:control:: [ChannelN],flanger
    :range: binary
    :feedback: Flanger button

    Toggles the flanger effect.

    .. deprecated:: 2.0.0
       This control has been **removed** without a direct replacement. Use the :ref:`effects framework <appendix-mixxxcontrols-effects>` instead.


.. mixxx:control:: [ChannelN],Hercules1
                   [ChannelN],Hercules2
                   [ChannelN],Hercules3
                   [ChannelN],Hercules4

    .. deprecated:: ??
       This control has been **removed**.


.. mixxx:control:: [ChannelN],NextTask

    .. deprecated:: ??
       This control has been **removed**.


.. mixxx:control:: [ChannelN],NextTrack

    .. deprecated:: ??
       This control has been **removed**.


.. mixxx:control:: [ChannelN],PrevTask

    .. deprecated:: ??
       This control has been **removed**.


.. mixxx:control:: [ChannelN],PrevTrack

    .. deprecated:: ??
       This control has been **removed**.


.. mixxx:control:: [ChannelN],transform

    .. deprecated:: ??
       This control has been **removed**.


.. mixxx:control:: [Flanger],lfoDepth
    :range: default
    :feedback: Depth knob

    Adjusts the intensity of the flange effect

    .. deprecated:: 2.0.0
       This control has been **removed** without a direct replacement. Use the :ref:`effects framework <appendix-mixxxcontrols-effects>` instead.


.. mixxx:control:: [Flanger],lfoDelay
    :range: 50..10000
    :feedback: Delay knob

    Adjusts the phase delay of the flange effect in microseconds

    .. deprecated:: 2.0.0
       This control has been **removed** without a direct replacement. Use the :ref:`effects framework <appendix-mixxxcontrols-effects>` instead.


.. mixxx:control:: [Flanger],lfoPeriod
    :range: 50000..2000000
    :feedback: LFO knob

    Adjusts the wavelength of the flange effect in microseconds

    .. deprecated:: 2.0.0
       This control has been **removed** without a direct replacement. Use the :ref:`effects framework <appendix-mixxxcontrols-effects>` instead.
