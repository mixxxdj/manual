.. include:: /shortcuts.rstext

.. _preferences:

Preferences
***********
Mixxx has many options to customize in
:menuselection:`Options --> Preferences`.

.. _preferences-sound-hardware:

Sound Hardware
==============

.. figure:: ../_static/Mixxx-200-Preferences-Soundhardware.png
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

If you are using a microphone, it is important to configure the
:ref:`preferences-mic-monitor-mode`.

For information about the different input and output options, refer to
:ref:`getting-started-sound-io`. The :ref:`hardware` chapter explains different
types of DJ hardware and how to set them up with the the input and output
options.

.. _preferences-audio-buffer:

Audio Buffer
------------

The audio buffer is the amount of audio in milliseconds that Mixxx processes at
a time. This is a major factor that determines the latency between changing
controls in Mixxx such as moving the crossfader or pressing the play button and
hearing the audio change. For example, with an audio buffer of 23 ms, it will
take approximately 23 milliseconds for Mixxx to stop the audio after you toggle
the play button. The actual latency will be longer depending on a variety of
factors.

The audio buffer setting determines how quickly your :term:`Operating System`
expects Mixxx to react. A smaller audio buffer means Mixxx will be more
responsive, but requires a faster CPU and quality sound card. Setting your
audio buffer too small may be too much for your computer and sound card to
handle. In this situation, Mixxx playback will be choppy and very clearly
distorted as your system will not be able to keep up with how frequently Mixxx
is trying to processing audio. It is recommended to set your audio buffer as
small as your system can handle reliably without glitches. Experiment with
different audio buffer sizes to find what works for your system.

An audio buffer between 23-64 ms is acceptable if you are using Mixxx with a
keyboard/mouse or a controller. An audio buffer below 10 ms is recommended
when vinyl control is used because Mixxx will feel unresponsive otherwise.

The `Adjusting Audio Latency <https://mixxx.org/wiki/doku.php/adjusting_audio_latency>`_
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
:term:`Operating System` in order to deliver audio to your soundcard. Your
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
Windows kernel. Using ASIO requires a driver for your soundcard from
the manufacturer. Check the manufacturer's website to see if a driver download
is available. Soundcards designed for musicians almost always have an ASIO
driver available, but soundcards built into computers and very cheap soundcards
typically do not have an ASIO driver. If there is no ASIO driver available for
your soundcard, use the WDM-KS API. There is generally no advantage to using
`ASIO4ALL <http://asio4all.com>`_, a wrapper around the WDM-KS API.

GNU/Linux
^^^^^^^^^
The following Sound APIs are available on GNU/Linux:

  * **ALSA**: Good
  * **JACK**: Good
  * **OSS**: Acceptable

ALSA is the simplest sound API to configure. Using ALSA will prevent any other
programs from using the soundcard(s) that Mixxx is using.

JACK allows you to route audio between JACK-compatible applications in flexible
ways and output sound from multiple programs at the same time. However, JACK can
be complicated to set up. Unless you will be connecting Mixxx to other
JACK-compatible applications, JACK offers no advantages over ALSA. To use JACK,
start the JACK daemon *before* running Mixxx. Otherwise JACK will not appear as
a Sound API in the preferences.

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
system sound card with other media players. This only works if you start
Mixxx without pasuspender, which you can do by running :command:`mixxx` from a
console rather than clicking the launcher icon in a menu or on your desktop.
Since the sound stream is routed from ALSA to Pulse and back to ALSA, this adds
an additional latency of ~2 x the selected audio buffer size.

OSS is an Sound API that predates ALSA. Few modern soundcards have OSS drivers.

macOS
^^^^^
CoreAudio is the only Sound API on macOS.

.. _preferences-mic-monitor-mode:

Microphone Monitor Mode and Latency Compensation
------------------------------------------------

The Microphone Monitor Mode option presents three options for routing the
microphone inputs:

* **Master output only**: The microphones are mixed with the master output. If
  the Booth output is configured, the microphones are excluded from it. This
  can be helpful to prevent feedback in a loud DJ booth.
* **Master and booth outputs**: The microphones are mixed with both the
  master and booth outputs.
* **Direct monitor (recording and broadcasting only)**: The microphones
  are recorded and broadcasted, but are not mixed with the Master or Booth
  outputs. This is meant to be used with a soundcard configured to directly
  monitor the microphone inputs. If you do not activate direct monitoring on
  your soundcard with this option, you will not hear the microphone input.

The :guilabel:`Master output only` and :guilabel:`Master and booth outputs`
options are referred to as *software monitoring* because the microphone signal
is mixed with the music by Mixxx. Due to the nature of digital audio, it takes
time for input from the soundcard to be available for Mixxx to process, time
for Mixxx to process the audio, and more time to send the audio back out the
soundcard. This time is referred to as "latency". Mixxx can be configured to
run at low latencies by choosing a smaller :ref:`preferences-audio-buffer`, but
there is no way to completely eliminate latency. Thus, if you use software
monitoring, you will hear the microphone signal out of the speakers after you
make sound into the microphone. Although latency is measured in milliseconds,
even a few milliseconds can be disorienting and distracting, whether you are
using the microphone for spoken announcements, vocals, or playing a musical
instrument.

.. figure:: ../_static/software-monitor-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Microphone input with software monitoring signal path
   :figclass: pretty-figures

   Microphone input with software monitoring signal path

To work around this issue, most soundcards with microphone inputs have a
feature called :term:`direct monitoring`. Soundcard manufacturers
often refer to this feature as "zero latency monitoring" (although truly zero
latency is physically impossible, the latency is so small it cannot be heard).
Soundcards built into computers typically do not support direct monitoring.

Direct monitoring routes the audio from the soundcard's inputs directly to its
outputs to avoid the latency of sending it into the computer and back out. At
the same time, the soundcard sends the input into the computer so Mixxx can
record and broadcast it. The tradeoff is that you hear Mixxx's effects on the
microphone inputs in real time because the audio you hear is mixed by the
soundcard, not Mixxx.

.. figure:: ../_static/direct-monitor-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Microphone input with direct monitoring signal path
   :figclass: pretty-figures

   Microphone input with direct monitoring signal path

.. warning:: USB microphones are not recommended for use with Mixxx. Some
             USB microphones have headphone jacks for direct monitoring, but
             this directly monitored signal only includes the microphone signal
             without the music from Mixxx. These microphones have their own
             soundcard built in, which often creates complications when
             configuring it at the same time as a different soundcard for
             output.

.. warning:: If you adjust the microphone gain knob in Mixxx while using direct
             monitoring, the relative volume of your microphone input to the
             music will be different in your recorded and broadcasted signal
             compared to what you hear from your speakers. Only adjust the
             microphone volume with the input gain control on your soundcard
             with direct monitoring. Refer to :ref:`djing-gain-staging` for how
             to set your gain controls properly.

.. _preferences-direct-monitoring:

Activating Direct Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
General tips for activating direct monitoring are described below. However,
every soundcard is different, so refer to the soundcard manual from the
manufacturer for more details.

Stand-alone Soundcards
""""""""""""""""""""""
On stand-alone soundcards, there is often a knob on the device that crossfades
the soundcard's output between the signal from the computer and the directly
monitored inputs. If your soundcard has a knob like this, set the knob to
the center. Also, you will need to configure your soundcard to route the mono
microphone inputs to both sides of the main stereo output. This is typically
controlled by a button or switch on the device.

Soundcards with lots of inputs and outputs often have a proprietary
program provided by the manufacturer that is installed automatically with the
driver instead of knobs and switches on the hardware to control direct
monitoring and other soundcard features. On GNU/Linux, you might be able to
access these controls with alsamixer.

DJ Controllers
""""""""""""""
DJ controllers with microphone inputs typically have direct monitoring
of microphone inputs hardwired or switched on by default.

Many cheap DJ controllers hardwire microphone inputs directly to the master
output without digitizing the signal to make it available to the computer. If
this is the case, you cannot use Mixxx's microphone input to record or
broadcast with your microphone using Mixxx's Microphone input. It is still
possible to record and broadcast your microphone by using a splitter cable on
your controller's master output and sending one of the split signals to a
different soundcard's input while listening to the other split signal through
speakers. In this case, the other soundcard's input would be configured as
Mixxx's :guilabel:`Record/Broadcast` input.

Refer to your controller's manual and its page on the Mixxx wiki for details
about setting up your specific controller's microphone inputs with Mixxx.

Microphone Latency Compensation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When using direct monitoring, it still takes time for Mixxx to receive the
audio input and process it. Without compensating for this, the microphone
inputs are out of time relative to the music in your recorded and broadcasted
mixes even though they are aligned in the soundcard's output signal.

Mixxx can align the microphones with the music in your recorded and broadcasted
mixes if you configure the :guilabel:`Microphone Latency Compensation` option.
If you do not want to record or broadcast your microphone input, you do not
need to set this up. Set this option to the amount of time it
takes for audio to make a complete trip from your soundcard's input, through
your computer, and back out the soundcard, also known as the round trip latency.
Mixxx cannot calculate the round trip latency amount because it depends on
details of your soundcard's hardware, your operating system, your soundcard's
driver, and other factors in your computer's hardware. You must use a physical
cable to directly connect an output on your soundcard to its input and use a
third party program to measure the round trip latency. These programs are
recommended on each OS:

* **GNU/Linux**: jack_iodelay
* **Windows**: RTL Utility
* **macOS**: Audacity?

Copy the time measured in milliseconds by the measurement program into
the :guilabel:`Microphone Latency Compensation` option in Mixxx's Sound
Hardware Preferences. You must use the same sample rate and audio buffer size
in the measurement program as you do in Mixxx for the measurement to be
accurate.

.. figure:: ../_static/latency-measurement.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Measuring round trip latency
   :figclass: pretty-figures

   Measuring round trip latency

.. hint:: Some soundcards, both standalone soundcards and soundcards
          integrated into DJ controllers, have a loopback feature. This sends
          the mix of the directly monitored inputs and the output from the
          computer back to the computer instead of just sending the microphone
          input to the computer. If your soundcard supports this, you can
          configure the soundcard's loopback input as Mixxx's Record/Broadcast
          input instead of the Microphone inputs and do not need to measure
          your round trip latency.

.. warning:: The round trip latency varies unpredictably for each combination
             of sample rate, audio buffer size, soundcard, computer, and
             :term:`OS`. If you decide to change the sample rate or buffer size
             you use with Mixxx, you will need to remeasure your round trip
             latency to have your microphone inputs aligned in your recorded
             and broadcasted mixes.

External Mixers
^^^^^^^^^^^^^^^
Another way to work around the latency issue is to send the output of Mixxx to
a soundcard output, connect the soundcard output to a hardware's mixer input,
plug the microphone into another input on the hardware mixer, connect the
hardware mixer's output to an input on your soundcard, and configure that
soundcard input for Mixxx's :guilabel:`Record/Broadcast` input. Other software
for radio and Internet broadcasting does not support latency compensation for
microphone inputs and only works with this kind of setup.

However, this setup is not recommended unless the mixer is a digital mixer and
has an integrated USB soundcard. Every conversion between digital and analog
signals adds noise and distortion to the signal, which reduces the sound
quality. This type of setup is especially not recommended when using a
computer's built in soundcard because it is not possible to use the mixer to mix
stereo signals with only 2 output channels. Also, sound cards built into
computers tend to have bad sound quality. Instead, it is recommended use a
soundcard capable of direct monitoring.

Other Sound Hardware options
----------------------------
* **Multi-Soundcard Synchronization**: Mixxx is able to use two or more
  :term:`soundcards` at a time, each with its own clock. When multiple
  soundcards are in use, the Mixxx engine is driven by the Master
  soundcard. Here you can select the synchronization used for the other
  soundcards to avoid buffer overflows or underflows.

* **Keylock/Pitch-Bending Engine**: This allows you to select the engine used
  for independent tempo and pitch changes (e.g. :term:`keylock`). Use
  :menuselection:`Soundtouch` on lower power machines (such as netbooks) or if
  you experience buffer underflows while using :term:`keylock`.

* **Master Mix**: You may disable the master mix to reduce Mixxx's CPU usage if
  you do not use the Master output, recording or live broadcasting.

* **Master Output Mode**: In Mono mode, the left and right channel are combined
  into a mono signal which is passed to both channels of your master sound card.
  This is useful for setups where the audience cannot hear your mix in stereo
  because of speaker placement or playing in a space with lots of reverberation.

* **Buffer Underflow Count**: Underflows (data is not available when needed)
  indicate that some of the subsystems in Mixxx can't keep up with real-time
  deadlines imposed by the current audio buffer size. This is useful to tune the
  latency settings. If the counter increases, then increase your audio buffer
  size, decrease the sample rate setting or change the sound API setting if
  available.

Library
=======

.. _configuration-import:

Changing music directories
--------------------------

.. versionadded:: 2.0
   Handles multiple music library folders and adds an option to move them to
   another location without data loss.

You can manually add, relink, and remove Mixxx music directories in
:menuselection:`Preferences --> Library`.

**Add a new music directory**
  Mixxx handles multiple music library folders. Click :guilabel:`Add` to
  browse to a directory where your music is stored. Mixxx will watch this
  directory and its subdirectories for new tracks.

  If you add a directory that is already in your library, or you are currently
  :ref:`rescanning your library <library-root>`, the operation is canceled.

  Directories can also be added from the :ref:`Browse <library-browse>` sidebar
  item inside the library.

**Relink a existing music directory**
  If an existing music directory is moved, Mixxx doesn't know where to find the
  audio files in it. Click :guilabel:`Relink` to select the music directory
  in its new location. This will re-establish the links to the audio files in
  the Mixxx library.

**Remove a music directory**
  Click :guilabel:`Remove`, and Mixxx will no longer watch a directory and
  its subdirectories for new tracks, and asks what would you like to do with the
  tracks from these directories.

  * Select :guilabel:`Hide Tracks` to hide all tracks from this directory and
    subdirectories.
  * Select :guilabel:`Delete Track Metadata` to delete all metadata for these
    tracks from Mixxx permanently
  * Select :guilabel:`Leave Tracks Unchanged` to leave the tracks unchanged in
    your library.

  Hiding tracks saves their metadata in case you re-add them in the future.

  Metadata means all track details (artist, title, playcount, etc.) as well as
  beatgrids, hotcues, and loops. This choice only affects the Mixxx library.
  No files on disk will be changed or deleted.

.. hint:: When changing music directories, you might want to run a library
          rescan afterwards. Select :menuselection:`Library --> Rescan Library`
          in the menu.

.. _configuration-bpm-detection:

Beat Detection
==============

.. sectionauthor::
   T.Rafreider <trafreider@mixxx.org>
   S.Brandt <s.brandt@mixxx.org>

.. TODO:: Update this section to explain the differences between the beatgrid
          and beatmap options.

Mixxx uses an ultra-precise BPM and beat detector. Manual adjustments
are redundant in many cases because Mixxx knows where the beats are.

BPM and beat detection is a complex operation. Depending on your computer and
the track's bitrate and duration this may take some time. By default Mixxx
analyzes the complete track. To accelerate beat detection on slower computers, a
“Fast Analysis” option is available. If enabled, the BPM is computed by
analyzing the first minute of the track. In most cases this does not affect the
beat detection negatively because most of today's dance music is written in a
4/4 signature with a fixed tempo.

.. figure:: ../_static/Mixxx-200-Preferences-Beatdetection.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Mixxx preferences - BPM settings
   :figclass: pretty-figures

   Mixxx preferences - BPM settings

The table below summarizes the beat detection settings:

+---------------------------------------+--------------------------------------+
| Option                                | Description                          |
+=======================================+======================================+
| Enable Fast Analysis                  | If enabled, BPM will be detected by  |
|                                       | only using the first minute of audio.|
+---------------------------------------+--------------------------------------+
| Assume constant tempo                 | If enabled, Mixxx assumes that the   |
|                                       | distances between the beats are      |
|                                       | constant. If disabled, the raw beat  |
|                                       | grid obtained by the analyzer is     |
|                                       | presented. The latter is appropriate |
|                                       | for tracks with variable tempo.      |
+---------------------------------------+--------------------------------------+
| Enable Offset Correction              | Prevents beat markers from being     |
|                                       | placed incorrectly.                  |
+---------------------------------------+--------------------------------------+
| Re-analyze beats when settings        | If enabled, Mixxx over-writes old    |
| change or beat detection data is      | beat grids from prior versions.      |
| outdated                              | Moreover, it will re-analyze the BPM |
|                                       | if your beat detection preferences   |
|                                       | change or BPM data from 3rd party    |
|                                       | programs are present.                |
+---------------------------------------+--------------------------------------+

Correcting Beat Grids
---------------------

There may be situations where BPM and beat detection do not result in a proper
beat grid.

Typically, the detected BPM is correct but the analyzer has failed to detect the
location of the first beat. Consequently, the beat markers are shifted, i.e.
the beat markers are a fixed distance from the true beat. To adjust the
beat grid, cue the track before a real beat and click the :guilabel:`Beat-grid
Adjust` button in the :ref:`interface-button-grid`.

If the detected BPM is not accurate, the corresponding beat grid will also be
inaccurate. A deviation of 0.02 BPM units from the correct BPM will cause
beatgrid alignment issues on long tracks (e.g. a club mix). If this happens,
your beatgrid may look aligned for the few minutes but you will notice a slight
drift as the song goes on. Finding the correct BPM is easy in many cases - just
follow the note below.

.. note:: If the detected BPM value is not sufficiently accurate but very close
          to an integer value, try to set the BPM value manually to the integer.

.. _configuration-key-detection:

Key Detection
=============

Mixxx comes with a high precision musical key detector to help you make smooth
mixes by ensuring that your tracks are musically compatible.

Analyzer Settings
-----------------

Key detection is a complex operation. Depending on your computer and the track's
bitrate and duration this may take some time. By default Mixxx analyzes the
complete track. To accelerate key detection on slower computers, a “Fast
Analysis” option is available. If enabled, the key is computed by analyzing the
first minute of the track.

.. figure:: ../_static/Mixxx-200-Preferences-Keydetection.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Mixxx preferences - Key settings
   :figclass: pretty-figures

   Mixxx preferences - Key settings

The table below summarizes the Key detection settings:

+---------------------------------------+--------------------------------------+
| Option                                | Description                          |
+=======================================+======================================+
| Enable Fast Analysis                  | If enabled, the key will be detected |
|                                       | by using only the first minute of    |
|                                       | audio.                               |
+---------------------------------------+--------------------------------------+
| Re-analyze key when settings          | If enabled, Mixxx will re-analyse    |
| change or Key detection data is       | tracks if you select a different key |
| outdated                              | detection plugin or the key was      |
|                                       | generated by a program other than    |
|                                       | Mixxx.                               |
+---------------------------------------+--------------------------------------+
| Key Notation                          | Change the way keys are displayed    |
|                                       | in the library.                      |
+---------------------------------------+--------------------------------------+

.. _preferences-equalizers:

Equalizers
==========

.. sectionauthor::
   Daniel Schürmann <daschuer@mixxx.org>

.. figure:: ../_static/Mixxx-200-Preferences-Equalizer.png
    :align: center
    :width: 80%
    :figwidth: 100%
    :alt: Equalizer Preferences
    :figclass: pretty-figures

    Equalizer Preferences

:menuselection:`Preferences --> Equalizer` allows you to setup the equalizers.

* **Equalizer Rack**: The Equalizer Rack is a special effect rack that is
  connected to the deck's equalizer and filter controls.

  In this section you can select the equalizers and quick effects that are used
  with the decks.

* **Equalizer Plugin**: Here you can select the effect that is used as the
  mixing EQ in each deck. By default only built-in equalizers are
  displayed. Unchecking :menuselection:`Only allow EQ knobs to control EQ
  specific effects` allows you to select any other effect.

* **Quick Effect**: Here you can select the effect that is controlled by the
  dedicated filter knob in each deck. By default only built-in filter effects
  are selected for all decks, but that can be changed as above.

* **High/Low Shelf EQ**: This slider sets the crossover frequencies of the
  mixing EQ. It controls which frequency range is affected by the low, mid, and
  high channel EQ knobs. By default the low knob controls the bass and sub bass
  range up to 246 Hz. The mid knob controls the mid range up to 2.5 kHz.
  The remaining treble range is controlled by the high knob.

* **Master EQ**: This section allows you to setup an EQ that affects the master
  output.


Mixing Equalizers
-----------------

Mixxx offers three types of mixing equalizers with a full kill option. These
equalizers are "isolators", adapted from analog crossover networks. Each EQ is
combination of a high shelf filter, a band pass filter, and a low shelf filter.
Each EQ type has a unique sound, so try them out to find out which one you
prefer.

The Bessel EQs with Lipshitz and Vanderkooy Mix (LV-Mix) do not alter the sound
or take any processing time when their knobs are in the center position. They
activate once you adjust an EQ knob.

The Linkwitz-Riley EQ on the other hand always applies a minimum, natural
sounding phase shift to the sound. Their processing time does not change when
you adjust the EQ knobs.

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

 * cut: the frequency response (curve form) at the cross over frequency.
 * roll-off: The steepness of the EQ bands.
 * linear phase: No phase distortion, all frequencies are processed with the
   same group delay.
 * minimum phase: A natural phase distortion, the group delay changes by the
   frequency.
 * bit perfect: Whether the EQ leaves the original samples untouched when the EQ
   is at unity.
 * CPU usage: Processing time needed to calculate the EQ output.
