.. _configuring-mixxx:

Configuring Mixxx
*****************

Sound Hardware Preferences
==========================

.. figure:: ../_static/Mixxx-111-Preferences-Soundhardware.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Mixxx Sound Hardware Preferences
   :figclass: pretty-figures

   Mixxx Sound Hardware Preferences

:menuselection:`Preferences --> Sound Hardware` allows you to select the audio
in- and outputs to be used.

* **Sound API**: Depending your :term:`Operating System`, select the :term:`API`
  that Mixxx uses to deliver audio to your audio device. Your choice can
  drastically affect how smooth Mixxx performs on your computer.

* **Sample Rate**: Allows you to manually select the sample rate for the audio input.
  The sample rate value should be set to the sample rate of your audio interface.
  By default, Mixxx tries the system default first, which is most likely 44.1
  kHz. Otherwise, Mixxx will pick a different default.

* **Audio buffer**: Also known as latency, this is the lag time in milliseconds
  that it takes for Mixxx to process your input. Lower latency means Mixxx
  will be more responsive but on slower computers and cheaper sound cards it
  might cause glitches.

* **Buffer Underflow Count**: Underflows (no data is available when needed)
  indicate that some of the subsystems in Mixxx can't keep up with
  real-time deadlines. This is useful to tune the latency settings. If the
  counter increases, then increase your audio buffer setting, decrease the
  sample rate setting or change the sound API setting if available.

.. _configuring-mixer-mode:

Audio Outputs
=============

Mixxx's mixing engine can be used two ways:

**Internal Mixer Mode**
  In this mode, Mixxx performs the mixing of the decks, microphone, and samplers
  in software and outputs them to a single output. To enable internal mixer mode
  assign a valid audio output to the :guilabel:`Master` output in
  :menuselection:`Preferences --> Sound Hardware --> Output`.

  Internal mode is used in the following configurations:

  * :ref:`setup-laptop-only`
  * :ref:`setup-laptop-and-external-card`
  * :ref:`setup-controller-and-external-card`

**External Mixer Mode**
  In this mode, Mixxx outputs the audio from each deck to a separate soundcard
  output. This allows you to route the deck outputs through a hardware mixer.
  Similarly, to enable external mixer mode, simply select a valid audio output
  for the :guilabel:`Deck` outputs in
  :menuselection:`Preferences --> Sound Hardware --> Output`.

  External mode is used in the following configuration:

  * :ref:`setup-vinyl-control`

Headphone Output
----------------

In both internal and external mixer mode, you can choose a headphone output for
:term:`pre-fader listening <PFL>` or :term:`headphone cueing <cueing>` in
:menuselection:`Preferences --> Sound Hardware --> Output --> Microphone`. This
allows you to listen and synchronize the track you will play next in your
headphones before your audience hears the track. See also :ref:`interface-pfl`.

.. _configuration-latency-samplerate-audioapi:

Latency, Sample Rate, and Audio API
===================================

To achieve the best performance with Mixxx it is essential to configure your
*audio buffer*, *sample rate*, and *audio API*. These three factors largely
determine Mixxx's responsiveness and audio quality and the optimal settings
will vary based on your computer and hardware quality.

.. _configuration-latency:

Audio Buffer
------------

The audio buffer, also known as latency, is the lag time in milliseconds that
it takes for Mixxx to process your input (turning knobs, sliding the
crossfader, etc.). For example, with an audio buffer of 36 ms, it
will take approximately 36 milliseconds for Mixxx to stop the audio after you
toggle the play button. Additionally, the audio buffer setting determines how
quickly your :term:`Operating System` expects Mixxx to react. A smaller audio
buffer means Mixxx will be more responsive. On the other hand,
setting your audio buffer too low may be too much for your computer and sound
card to handle. In this situation, Mixxx playback will be choppy and very
clearly distorted as your computer will not be able to keep up with how
frequently Mixxx is processing audio.

An audio buffer between 36-64 ms is acceptable if you are using Mixxx with a
keyboard/mouse or a MIDI controller. An audio buffer below 10 ms is recommended
when vinyl control is used because Mixxx will feel unresponsive otherwise.

Keep in mind that *lower latencies require better soundcards and faster CPUs*
and that zero latency DJ software is a myth (although Mixxx is capable of
sub-1ms operation).

Sample Rate
-----------

The sample rate setting in Mixxx controls how many samples per second are
produced by Mixxx. This determines the maximum frequency in Mixxx's signal,
which is half the sample rate. Humans can only hear up to 20 kHz, so there
is generally no need to use more than a 44.1 kHz (44100 Hz) sample rate
for playback. Most music is published with a 44100 Hz sample rate.

.. warning:: A sample rate of 96kHz takes Mixxx over twice as long to compute.
             Keep in mind that increasing the sample rate will increase CPU
             usage and likely raise the minimum audio buffer size you can
             use.

Audio API
---------

The Audio :term:`API` that Mixxx uses is the method by which Mixxx talks to your
:term:`Operating System` in order to deliver audio to your soundcard. Your
choice of Audio API can drastically affect Mixxx's performance on your
computer. **Therefore it is important to take care to choose the best Audio API
available to you.** Refer to the following table of Audio APIs to see what the
best choice is for your operating system.

+-----------------------------+---------+
| OS / Audio API              | Quality |
+=============================+=========+
| Windows / WMME              | Poor    |
+-----------------------------+---------+
| Windows / DirectSound       | Poor    |
+-----------------------------+---------+
| Windows / WASAPI            | Good    |
+-----------------------------+---------+
| Windows / ASIO              | Good    |
+-----------------------------+---------+
| Windows / WDDKMS            | Good    |
+-----------------------------+---------+
| Mac OS X / CoreAudio        | Good    |
+-----------------------------+---------+
| GNU Linux / OSS             | OK      |
+-----------------------------+---------+
| GNU Linux / ALSA            | Good    |
+-----------------------------+---------+
| GNU Linux / JACK (Advanced) | Good    |
+-----------------------------+---------+

On Windows, if an ASIO driver is not available for your operating system, you
can try installing `ASIO4ALL <http://asio4all.com>`_, a low-latency audio driver
for WDM audio devices.

On GNU/Linux, ALSA is the simplest sound API to configure. Using ALSA will
prevent any other programs from using the sound card(s) that Mixxx is using.

JACK allows you to route audio between JACK-compatible applications in flexible
ways and output sound from multiple programs at the same time. However, JACK can
be complicated to set up. To use JACK, start the JACK daemon *before* running
Mixxx. Otherwise JACK will not appear as a Sound API in the preferences.

Most modern GNU/Linux distributions use PulseAudio by default. When
launched from a GUI menu entry or icon, Mixxx suspends PulseAudio while it is
running so that Mixxx can use ALSA directly. Like JACK, PulseAudio allows
multiple programs to access one sound card, but PulseAudio and JACK have
opposite design goals. PulseAudio is designed to make ordinary computer usage
such as watching videos online and listening to music easy whereas JACK is
designed for demanding low latency audio programs like Mixxx. It can be
difficult to setup JACK and PulseAudio to work well together. So, unless you
already use JACK, it is easiest to let Mixxx suspend PulseAudio and use ALSA.

If the PulseAudio plugin for alsalibs is installed on GNU/Linux, you can 
choose the virtual device ``pulse``. This allows Mixxx to share the default 
system sound card with other media players. This does only work if you start 
mixxx without pasuspender. Since the sound stream is routed from ALSA to Pulse 
and back to ALSA, this adds an additional latency of ~2 x the selected audio 
buffer.  
 
Equalizer Preferences
=====================

.. figure:: ../_static/Mixxx-111-Preferences-Equalizer(TODO).png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Equalizer Preferences
   :figclass: pretty-figures

   Equalizer Preferences

:menuselection:`Preferences --> Equalizer` allows you to setup the equalizers.

* **Equalizer Rack**: The Equalizer Rack is a special Effect Rack that is
  connected to the deck's equalizer and filter controls.

  In this section you can select the equalizers and quick effects that are used
  with the decks.

* **Equalizer Plugin**: Here you can select the effect that is used as mixing
  EQ in each deck. By default only built-in equalizers are displayed.  If you uncheck
  "Only allow EQ knobs to control EQ specific effects" you can select any other
  effect.


  If you want different settings for each deck, you may uncheck "Use the same
  EQ filter for all decks"

* **Quick Effect**: Here you can select the effect that is controlled by the
  dedicated filter knob in each deck. By default only built-in filter effects are
  selected for all decks, but that can be changed as above.

* **High/Low Shelf EQ**: This slider sets the crossover frequencies of the mixing 
  EQ. It controls which frequency range is affected by the three Channel EQ
  knobs Low, Mid and High. By default the low knob controls the bass and sub bass 
  range up to 246 Hz. The mid knob controls the mid range up to 2,5 kHz. 
  The remaining teble range is controlled by the high knob.   

* **Master EQ**: This section allows you to setup an EQ that effects only the
  master output. 


Mixing Equalizers
-----------------

Mixxx offers three types of mixing equalizers with full kill feature. They are 
actually isolators, adopted from analog cross over networks. Each EQ is 
combination of a high shelf filter, a band pass filter, and a low shelf filter, 
offering its own individual sound, so try them out.


The Bessel EQs with Lipshitz and Vanderkooy Mix do not alter audio samples when
all knobs are at center. Once you adjust the knobs it activates and requires more
CPU time.

The Linkwitz-Riley EQ always applies a minimum, natural sounding phase shift.
The amount of CPU time does not change when you adjust the EQ knobs.

The following table compares some technical parameters:

+----------------+--------+------------+-------------+-------------+-----------+
| Type           | cut    | roll-off   | phase shift | bit perfect | CPU usage |
+================+========+============+=============+=============+===========+
| Bessel4 LV-Mix | soft   | -24 db/Oct | linear      | yes         | low       |
+----------------+--------+------------+-------------+-------------+-----------+
| Bessel8 LV-Mix | medium | -48 db/Oct | linear      | yes         | medium    |
+----------------+--------+------------+-------------+-------------+-----------+
| Linkwitz-Riley | sharp  | -48 db/Oct | minimum     | no          | high      |
+----------------+--------+------------+-------------+-------------+-----------+

cut: the frequency response (curve form) at the cross over frequency

roll-off: The steepness of the EQ bands

linear phase: No phase distortion, all frequencies are processed with the same group delay

minimum phase: A natural phase distortion, the group delay changes by the frequency

bit perfect: Whether the EQ changes leaves the original samples untouched when the EQ is at unity

CPU usage: Processing time, needed to calculate the EQ output 
