.. include:: /shortcuts.rstext

.. _preferences-sound-hardware:

Sound Hardware
==============

.. figure:: ../../_static/Mixxx-200-Preferences-Soundhardware.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Mixxx Sound Hardware Preferences
   :figclass: pretty-figures

   Mixxx Sound Hardware Preferences

To achieve the best performance with Mixxx it is essential to configure your
*audio buffer*, *sample rate*, and *audio API*. These three factors largely
determine Mixxx's responsiveness and reliability. The optimal settings
will vary based on your computer and hardware quality.

For information about the different input and output options, refer to
:ref:`getting-started-sound-io`. The :ref:`hardware` chapter explains different
types of DJ hardware and how to set them up with the input and output
options. If you are using a microphone, refer to the :ref:`microphones` chapter.

.. _preferences-audio-buffer:

Audio Buffer
------------

The audio buffer is the amount of audio in milliseconds that Mixxx processes at
a time. This is a major factor that determines the latency between changing
controls in Mixxx such as moving the :term:`crossfader` or pressing the play button and
hearing the audio change. For example, with an audio buffer of 23 ms, it will
take approximately 23 milliseconds for Mixxx to stop the audio after you toggle
the play button. The actual latency will be longer depending on a variety of
factors.

The audio buffer setting determines how quickly your :term:`operating system`
expects Mixxx to react. A smaller audio buffer means Mixxx will be more
responsive, but requires a faster CPU and quality audio interface. Setting your
audio buffer too small may be too much for your computer and audio interface to
handle. In this situation, Mixxx playback will be choppy and very clearly
distorted as your system will not be able to keep up with how frequently Mixxx
is trying to process audio. It is recommended to set your audio buffer as
small as your system can handle reliably without glitches. Experiment with
different audio buffer sizes to find what works for your system.

An audio buffer between 23-64 ms is acceptable if you are using Mixxx with a
keyboard/mouse or a controller. An audio buffer below 10 ms is recommended
when vinyl control is used because Mixxx will feel unresponsive otherwise.

The `Adjusting Audio Latency <https://github.com/mixxxdj/mixxx/wiki/Adjusting-Audio-Latency>`_
page on the Mixxx Wiki has tips for different operating systems
that may help you use a smaller audio buffer reliably.

.. warning:: Your system may glitch only occasionally if you have your audio
             buffer set a little too low. This will happen at unpredictable
             times and you may not notice if you are only doing brief tests of
             each audio buffer size. When you think you have found a good
             buffer size for your system, play with Mixxx for at least a half
             hour before performing to ensure no glitches happen.

.. _preferences-sample-rate:

Sample Rate
-----------

The sample rate setting in Mixxx controls how many samples (chunks of audio)
per second are produced by Mixxx. This determines the maximum frequency in
Mixxx's signal, which is half the sample rate. Humans can only hear up to 20
kHz, so there is generally no need to use more than a 44.1 kHz (44100 Hz)
sample rate for playback. Most music is published with a 44100 Hz sample rate,
and playing music in a different sample rate than the audio file slightly
reduces sound quality.

.. warning:: A sample rate of 96 kHz gives your computer less than half the time
             to as to do the same processing. Increasing the sample
             rate will increase CPU usage and likely raise the minimum audio
             buffer size you can use reliably.


.. _preferences-sound-api:

Sound API
---------

The Sound :term:`API` that Mixxx uses is the method by which Mixxx talks to your
:term:`operating system` in order to deliver audio to your audio interface. Your
choice of Sound API can drastically affect Mixxx's performance on your
computer. **Therefore it is important to take care to choose the best Sound API
available to you.**

Windows
^^^^^^^
The following Sound APIs are available on Windows:

  * **ASIO**: Good
  * **WDM-KS**: Good
  * **WASAPI**: Acceptable
  * **DirectSound**: Poor
  * **MME**: Poor

It is best to use the ASIO Sound API that bypassses the sound processing of the
Windows kernel. Using ASIO requires a driver for your audio interface from
the manufacturer. Check the manufacturer's website to see if a driver download
is available. Soundcards designed for musicians almost always have an ASIO
driver available, but audio interfaces built into computers and very cheap
audio interfaces typically do not have an ASIO driver. If there is no ASIO
driver available for your audio interface, use the WDM-KS API. There is
generally no advantage to using `ASIO4ALL <http://www.asio4all.org>`_, a wrapper
around the WDM-KS API.

GNU/Linux
^^^^^^^^^
The following Sound APIs are available on GNU/Linux:

  * **ALSA**: Good
  * **JACK**: Good
  * **OSS**: Acceptable

ALSA is the simplest sound API to configure. Using ALSA will prevent any other
programs from using the audio interface(s) that Mixxx is using.

JACK allows you to route audio between JACK-compatible applications in flexible
ways and output sound from multiple programs at the same time. However, JACK can
be complicated to set up. Unless you will be connecting Mixxx to other
JACK-compatible applications, JACK offers no advantages over ALSA. To use JACK,
start the JACK daemon *before* running Mixxx. Otherwise JACK will not appear as
a Sound API in the preferences.

Most modern GNU/Linux distributions use PulseAudio by default. When
launched from a GUI menu entry or icon, Mixxx suspends PulseAudio while it is
running so that Mixxx can use ALSA directly. Like JACK, PulseAudio allows
multiple programs to access one audio interface, but PulseAudio and JACK have
opposite design goals. PulseAudio is designed to make ordinary computer usage
such as watching videos online and listening to music easy whereas JACK is
designed for demanding low latency audio programs like Mixxx. It can be
difficult to setup JACK and PulseAudio to work well together. So, unless you
already use JACK, it is easiest to let Mixxx suspend PulseAudio and use ALSA.

If the PulseAudio plugin for alsalibs is installed on GNU/Linux, you can
choose the virtual device ``pulse``. This allows Mixxx to share the default
system audio interface with other media players. This only works if you start
Mixxx without pasuspender, which you can do by running :command:`mixxx` from a
console rather than clicking the launcher icon in a menu or on your desktop.
Since the sound stream is routed from ALSA to Pulse and back to ALSA, this adds
an additional latency of ~2 x the selected audio buffer size.

OSS is an Sound API that predates ALSA. Few modern audio interfaces have OSS
drivers.

macOS
^^^^^
CoreAudio is the only Sound API on macOS.

Other Sound Hardware options
----------------------------
* **Multi-Soundcard Synchronization**: Mixxx is able to use two or more
  :term:`audio interface <audio interface>` at a time, each with its own clock. When multiple
  audio interfaces are in use, the Mixxx engine is driven by the Master
  audio interface. Here you can select the synchronization used for the other
  audio interfaces to avoid buffer overflows or underflows.

* **Keylock/Pitch-Bending Engine**: This allows you to select the engine used
  for independent tempo and pitch changes (e.g. :term:`key lock`). Use
  :menuselection:`Soundtouch` on lower power machines (such as netbooks) or if
  you experience buffer underflows while using :term:`key lock`.

* **Master Mix**: You may disable the master mix to reduce Mixxx's CPU usage if
  you do not use the Master output, recording or live broadcasting.

* **Master Output Mode**: In Mono mode, the left and right channel are combined
  into a mono signal which is passed to both channels of your master audio
  interface. This is useful for setups where the audience cannot hear your mix
  in stereo because of speaker placement or playing in a space with lots of
  reverberation.

* **Buffer Underflow Count**: Underflows (data is not available when needed)
  indicate that some of the subsystems in Mixxx can't keep up with real-time
  deadlines imposed by the current audio buffer size. This is useful to tune the
  latency settings. If the counter increases, then increase your audio buffer
  size, decrease the sample rate setting or change the sound API setting if
  available.

Output and Input Devices
------------------------

In the usual, basic 'Digital DJ' setup (:ref:`setup-controller-and-external-card`
or :ref:`setup-laptop-and-external-card`) all that needs to be configured are
the Master and Headphones outputs. Though, there are many more output and
input channels available for more complex setups, for example with external
mixers, vinyl control or for broadcasting.

All outputs are usually sent to a channel pair (stereo), though they can
also be sent to one channel only (mono mixdown), for example if you're short
on output channels, like when you need to use one stereo output for both master
and headphones (see :ref:`setup-laptop-with-splitter`).

Inputs can be mono or stereo (matching plugged sources, of course), except vinyl
control inputs which require stereo to capture the entire control signal.

Outputs
^^^^^^^

* **Master** (Main): The mix of all audible channels, e.g. main decks, all
  samplers, enabled microphones and auxiliary inputs.

* **Headphones**: All channels for which :term:`pfl` is enabled, as well as the
  preview deck.

* **Booth**: Basically the same output as Main to be routed to a separate output,
  for example for the speakers in the DJ booth, external recording device,
  loopback device for video recordings etc.

* **Left Bus**: All decks, samplers and auxiliaries that are assigned to the left
  side of the :term:`crossfader`.

* **Center Bus**: All decks, samplers and auxiliaries that are assigned to the
  center of the :term:`crossfader`.

* **Right Bus**: All decks, samplers and auxiliaries that are assigned to the right
  side of the :term:`crossfader`.

* **Deck 1-4**: Separate outputs for each of the main decks.

Inputs
^^^^^^

* **Vinyl Control 1-4**: Inputs to be used for :ref:`vinyl control and passthrough <vinyl-control>`.
  Note that one input can be selected for multiple decks.

* **Microphone 1-4**: ref:`Microphone <microphones>` inputs.

* **Auxiliary 1-4**: Auxiliary inputs.
  .. TODO: link to Aux chapter when it's been added.

* **Record/Broadcast**: The input used for the Mixxx-internal :ref:`recording <djing-recording-your-mix>` and :ref:`broadcasting <live-broadcasting>`.
  Note that when setting this input your recording and broadcast stream will
  not be identical to the main output.
