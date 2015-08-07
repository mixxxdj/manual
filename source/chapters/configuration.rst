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

+----------------------------------------+--------------+
| OS / Audio API                         | Quality      |
+========================================+==============+
| Windows / WMME                         | Poor         |
+----------------------------------------+--------------+
| Windows / DirectSound                  | Poor         |
+----------------------------------------+--------------+
| Windows / WASAPI                       | Good         |
+----------------------------------------+--------------+
| Windows / ASIO                         | Good         |
+----------------------------------------+--------------+
| Windows / WDDKMS                       | Good         |
+----------------------------------------+--------------+
| Mac OS X / CoreAudio                   | Good         |
+----------------------------------------+--------------+
| GNU Linux / OSS                        | OK           |
+----------------------------------------+--------------+
| GNU Linux / ALSA                       | Good         |
+----------------------------------------+--------------+
| GNU Linux / JACK (Advanced)            | Good         |
+----------------------------------------+--------------+

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

.. warning:: On GNU/Linux do *not* use the ``pulse`` device with the ALSA Audio
             API. This is an emulation layer for ALSA provided by PulseAudio and
             results in very poor performance. 
