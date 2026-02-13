.. _reloop-beatmix-4:

Reloop Beatmix 4
================

The Reloop Beatmix 4 MK2 is a performance-oriented 4-channel pad controller with integrated soundcard.
It offers an ergonomically designed 4-channel mixer layout, optimized for the club allowing you to work intuitively:
Dedicated equalizer and gain dials, high-quality line-faders, an extremely smooth-running crossfader, 16 multi-colour drum pads, as well as two extensive FX units are the foundation for your creativity.

-  `Manufacturer’s product page <http://www.reloop.com/reloop-beatmix-4-mk2>`__
-  `Forum thread <https://mixxx.discourse.group/t/reloop-beatmix-2-4-mapping/16049>`__

.. versionadded:: 2.1

Audio
-----

This controller is a MIDI and audio class compliant device so it is compatible as-is with Linux, MacOS and Windows.
On windows, the manufacturer ships an :term:`ASIO` low-latency driver that can be found on the `Manufacturer’s product page <http://www.reloop.com/reloop-beatmix-4>`__.

The :hwlabel:`MIC` input is hardware-mixed and is not digitized so Mixxx can not have any control on the mic and you can not use ducking in Mixxx.
The :hwlabel:`MASTER` volume and :hwlabel:`PHONES` volume knobs directly control hardware and don’t change Mixxx controls.

Mixer Section
-------------

=============================================  =========================================================================
Control                                        Description
=============================================  =========================================================================
:hwlabel:`MASTER`                              Controls the main volume to your main sound system. This controls the built in sound card and has no effect on the main gain knob in Mixxx.
:hwlabel:`PHONES`                              Controls your headphones volume. This controls the built in sound card and has no effect on the headphone gain knob in Mixxx.
:hwlabel:`CUE MIX`                             Mixes the headphones CUE signal between your selected channel and the main output.
:hwlabel:`TRAX SELECT`                         Use the :ref:`Trax selector <reloop-beatmix-4-traxselector>` to navigate through your song library.
:hwlabel:`TRACK LOAD` (short press)            Load tracks on either channel. These buttons are lit when a track is loaded into the associated deck.
:hwlabel:`TRACK LOAD` (long press)             Eject the selected deck.
:hwlabel:`SHIFT`:hwlabel:`TRACK LOAD`          Enable and launch a track using your linefader (:hwlabel:`FADER-START`, hardware function)
:hwlabel:`CUE`                                 Pre-listen the selected channel in your headphones. This buttons lights-up when activated
:hwlabel:`BACK`                                Switch :ref:`Trax action <reloop-beatmix-4-traxselector>` between playlists (sidebar), tracks and Preview Deck.
:hwlabel:`SAMPLER VOLUME`                      Controls the volume of all samplers.
:hwlabel:`LINE FADERS`                         Controls your channel volume.
:hwlabel:`CROSSFADER`                          Enables you to fade between your decks.
:hwlabel:`GAIN`                                Adjust the gain for each deck.
:hwlabel:`EQ`                                  Tweak the high, mid or low frequencies when mixing your track.
:hwlabel:`DECK`                                Press the deck button to swap between decks 1 & 3 on the left and 2 & 4 on the right.
=============================================  =========================================================================

.. hint::
   You can replace the fader cap of the :hwlabel:`SAMPLER VOLUME` fader with a custom colored fader cap to make it visually stand out from the channel volume faders.

.. _reloop-beatmix-4-traxselector:

Trax selector and Back button
-----------------------------

The trax selector let you navigate through your library (playlist and tracks) as well as preview tracks.

The trax selector has three modes:

Track mode (default)
    Turning the trax selector will select tracks (one by one), turning with shift will select tracks faster (10 by 10).
    Pressing the :hwlabel:`Back` button will switch to Playlist mode and pushing the trax selector will load the selected track into the preview deck, start playing and switch to Preview mode.
Playlist mode
    Turning the trax selector will select sidebar item (one by one), turning with shift will select sidebar item faster (10 by 10).
    Pressing the trax selector will expand/collapse the selected sidebar item and pressing the :hwlabel:`Back` button will return to Track mode.
Preview mode
    Turning the trax selector let you navigate through the track loaded in the PreviewDeck (faster with shift), pushing the trax selector will play/pause the preview deck and pushing the :hwlabel:`back` button return to Track mode.

Transport Section
-----------------

=============================================  =========================================================================
Control                                        Description
=============================================  =========================================================================
:hwlabel:`PLAY/PAUSE`                          Press to launch and pause your track.
:hwlabel:`SHIFT` + :hwlabel:`PLAY/PAUSE`       Reverses the direction of the track playing.
:hwlabel:`CUE`                                 Sets a temporary :term:`cue point`. It is set by pausing the track and pressing the :hwlabel:`CUE` button. While the track is playing, press the button to return to that point, where it will pause.
:hwlabel:`SHIFT` + :hwlabel:`CUE`              Takes you back to the start of your track.
:hwlabel:`CUP`                                 Takes you directly to your cue point and starts playback instantly. If no cue point is set, it will jump to the beginning of the track.
:hwlabel:`SHIFT` + :hwlabel:`CUP`              Changes the pitch range, cycling through 8%, 10%, 12% and 16%
:hwlabel:`SYNC`                                Syncs the BPM and phase to that of the other track (if :term:`BPM` is detected on both).
:hwlabel:`SHIFT` + :hwlabel:`SYNC`             Turn on sync lock, keeping sync enabled
=============================================  =========================================================================


Jog wheel and pitch slider
--------------------------

Touch and move the jog wheel to scratch (either deck playing or not).

When playing, use the side of the wheel, without touching the metallic platter, to temporarily bend the pitch (speed up/slow down playback).
When the deck is not playing, using the side of the wheel let you quick search through your track.

Hold :hwlabel:`SHIFT` and turn the jog wheel to quick search through your track.
:hwlabel:`SHIFT` ignores touch sensitive platter so holding it and turning jogwheel is the same as using the side of the jog wheel.

When a deck is playing, jog led will turn around at 33.3 RPM.
When track time left is below 30 seconds, jog leds will blink slowly, and when track time remaining is below 15 seconds, jog leds will blink quickly.
These delays can be changed by editing the two variables at the beginning of the JavaScript file and eventually set to -1 to disable jog led blink.

The pitch slider let you adjust pitch.

:hwlabel:`PITCH +/-` buttons let you temporarily adjust the the speed one step higher/lower.
These buttons, when used with shift, let you :ref:`control effects <reloop-beatmix-4-effects>`.


.. _reloop-beatmix-4-effects:

Effects Section
---------------

The effect section let you control the first two EffectUnits.
There are two different effect modes mapped:

-  Multi Effect mode (the default), where you can load up to three effects in each EffectUnit and control then with the super knob
-  Single Effect mode, where you can load a single effect in the Effect Unit and control the first 6 parameters

==========================================  =============================  ===================
Control                                     Multi Effect mode              Single Effect mode
==========================================  =============================  ===================
:hwlabel:`FX1`                              Turn left to disable effect 1  Effect parameter 1
:hwlabel:`FX2`                              Turn left to disable effect 2  Effect parameter 2
:hwlabel:`FX3`                              Turn left to disable effect 3  Effect parameter 3
:hwlabel:`SHIFT` + :hwlabel:`FX1`           select effect 1                Effect parameter 4
:hwlabel:`SHIFT` + :hwlabel:`FX2`           select effect 2                Effect parameter 5
:hwlabel:`SHIFT` + :hwlabel:`FX3`           select effect 3                Effect parameter 6
:hwlabel:`BEATS` (turn)                     SuperKnob                      dry/wet knob
:hwlabel:`BEATS` (push)                     Toggle Effect Unit
:hwlabel:`SHIFT` + :hwlabel:`Beats` (turn)  Dry/Wet knob                   Select Effect Chain
:hwlabel:`SHIFT` + :hwlabel:`Beats` (push)  Eject Effect Chain
==========================================  =============================  ===================

You can choose which deck you want to apply EffectUnit 1 and 2 by pressing :hwlabel:`SHIFT` + :hwlabel:`PITCHBEND -` / :hwlabel:`SHIFT` + :hwlabel:`PITCHBEND +` on that deck (short press).

To switch from Single Effect mode to Multi Effect mode, hold down :hwlabel:`SHIFT` and press :hwlabel:`PITCHBEND -` for more than a second to switch to “Single Effect mode” or :hwlabel:`PITCHBEND +` for more than a second to switch to “Multi Effect mode”.
The corresponding led will blink three times, indicating which mode you switched to.

Pad Section
-----------

Mode A - Cue points and Loops
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============================================  =========================================================================
Control                                        Description
=============================================  =========================================================================
Pads 1-4 (top row)                             Press an unlit pad to set a new :term:`cue point`. If it is already set, jump to this cue point.
:hwlabel:`SHIFT` + Pads 1-4 (top row)          Deletes cue points.
Pads 5-8 (bottom row)                          Press the pad to activate a loop. Loop length (in beats) is respectively 1, 2, 4 and 8 beats.
:hwlabel:`SHIFT` + Pads 5 (bottom row)         Sets a loop length. Push to define loop start, release to define loop end.
:hwlabel:`SHIFT` + Pads 6 (bottom row)         Shortens (half) the loop.
:hwlabel:`SHIFT` + Pads 7 (bottom row)         Lengthens (double) the loop.
:hwlabel:`SHIFT` + Pads 8 (bottom row)         Replays the loop.
=============================================  =========================================================================

Mode B - Samplers
~~~~~~~~~~~~~~~~~

Mode B let you control 8 samplers.
Top row is for sampler 1-4 and bottom row is for sampler 5-8, each sampler controlled by a pad button.

Press an unlit pad to load the track selected in the library to that sampler.
Pads are red when the sampler is loaded but not playing and purple when playing.

Press a red pad to play the sample from its cue point.
Press a purple pad to jump back to the sample’s cue point.

Press a purple pad with shift to stop a playing sample.
Press a red pad with shift to eject a sample.

Split mode
~~~~~~~~~~

Split mode is activated by pressing mode A and mode B buttons simultaneously.
The two leds A and B are lit together. In this mode, to top row is configured in mode A, and the bottom row if configured as the top row of mode B.

So in this mode, you can control 4 cue points and 4 samplers.
