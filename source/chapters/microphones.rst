.. include:: /shortcuts.rstext

.. _microphones:

Using Microphones
*****************
There are three ways to use microphones with Mixxx, each with their own pros
and cons:
  * Software monitoring: cheapest and simplest to set up, but there is a
    disorienting delay, referred to as "latency", between sound going into the
    microphone and hearing it come out speakers or headphones
  * Direct monitoring: avoids the latency of software monitoring but requires a
    soundcard capable of direct monitoring and can be complicated to set
    up. Recommended for most users.
  * External mixing: most expensive option to set up with high sound quality

.. warning:: USB microphones are not recommended because they cannot be used
             with direct monitoring with Mixxx. Some USB microphones
             have headphone jacks for direct monitoring, but the music
             output from Mixxx cannot be heard together with the microphone
             input in the headphone jack. Also, these microphones have their
             own soundcard built in, which often creates complications when
             configuring it at the same time as a different soundcard for
             output.

.. _microphones-software-monitoring:

Software monitoring
-------------------
Software monitoring can be used with the soundcard build into a computer, but
it has a big drawback. Due to the nature of digital audio, it takes time for
input from the soundcard to be available for Mixxx to process, time for Mixxx
to process the audio, and more time to send the audio back out the soundcard.
This time is referred to as "latency". Mixxx can be configured to run at low
latencies by choosing a smaller :ref:`preferences-audio-buffer`, but there is no
way to completely eliminate latency. Thus, if you use software monitoring, you
will hear the microphone signal out of the speakers after you make sound into
the microphone. Although latency is measured in milliseconds, even a few
milliseconds can be disorienting and distracting, whether you are using the
microphone for spoken announcements, vocals, or playing a musical instrument.

.. figure:: ../_static/software-monitor-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Microphone input with software monitoring signal path
   :figclass: pretty-figures

   Microphone input with software monitoring signal path

.. _microphones-direct-monitoring:

Direct monitoring
-----------------
To work around the issue of latency with
:ref:`software monitoring <microphones-software-monitoring>`, most soundcards
with microphone inputs have a feature called "direct monitoring".
Soundcard manufacturers often refer to this feature as "zero latency monitoring"
(although truly zero latency is physically impossible, the latency
is so small it cannot be heard). Soundcards built into computers typically do
not support direct monitoring.

Direct monitoring routes the audio from the soundcard's inputs directly to its
outputs to avoid the latency of sending it into the computer and back out. At
the same time, the soundcard sends the input into the computer so Mixxx can
record and broadcast it.

.. figure:: ../_static/direct-monitor-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Microphone input with direct monitoring signal path
   :figclass: pretty-figures

   Microphone input with direct monitoring signal path

To setup direct monitoring, it must be
:ref:`activated on your soundcard <microphones-activating-direct-monitoring-on-soundcard>`.
If you are not recording or broadcasting the microphone with the music, no
further setup is needed. To record and/or broadcast with the microphone
signal mixed into the music, setting up a either a
:ref:`loopback input <microphones-loopback-input>` or
:ref:`latency compensation <microphones-latency-compensation>` is required.

.. _microphones-loopback-input:

Loopback Input
^^^^^^^^^^^^^^
Some soundcards that support direct monitoring have a feature called
"loopback". Using a soundcard with this feature is the recommended way
to use microphones with Mixxx because it is the easiest and cheapest to setup
without the latency issue of
:ref:`software monitoring <microphones-software-monitoring>` and with good
sound quality.

Using direct monitoring, the soundcard mixes the microphone input with the
music output from Mixxx in hardware. This avoids the latency of sending the
microphone signal into the computer and back out. The mixed signal is sent to
the speakers connected to the main output. Using the loopback feature, that
mixed signal is sent to the computer instead of the microphone signal alone,
typically using input channels 1-2.

.. figure:: ../_static/direct-monitor-loopback-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Microphone input with direct monitoring signal path
   :figclass: pretty-figures

   Microphone input with direct monitoring signal path

To configure Mixxx with a loopback input, open
:guilabel:`Options -> Preferences -> Sound Hardware`, click the
:guilabel:`Input` tab, and select the soundcard for the **Record/Broadcast
input**. Do not configure anything for the Microphone 1-4 inputs. The
microphone controls in Mixxx will not affect your microphones because they are
mixed in hardware by the soundcard and not sent directly to Mixxx. Use the gain
knobs on the soundcard to control the volume of the microphones.

.. _microphones_latency_compensation:

Latency Compensation
^^^^^^^^^^^^^^^^^^^^
When using direct monitoring without a
:ref:`loopback input <microphones-loopback-input>`, it still takes time for
Mixxx to receive the audio input and process it. Without compensating for this,
the microphone inputs are out of time relative to the music in your recorded
and broadcasted mixes even though they are aligned in the soundcard's output
signal.

Mixxx can compensate for this timing misalignment, but it is complicated to
set up. If you do not want to record or broadcast your microphone input, you do
not need to set this up. To configure this, open
:guilabel:`Options -> Preferences -> Sound Hardware`. For the
:guilabel:`Microphone Monitor Mode` option, select **Direct monitor (recording
and broadcasting only)**.

Set the
:guilabel:`Microphone Latency Compensation` option to the amount of time it
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

If you adjust the microphone gain knob in Mixxx while using direct monitoring,
the relative volume of your microphone input to the music will be different in
your recorded and broadcasted signal compared to what you hear from your
speakers. Only adjust the microphone volume with the input gain control on your
soundcard with direct monitoring.

.. figure:: ../_static/latency-measurement.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Measuring round trip latency
   :figclass: pretty-figures

   Measuring round trip latency

.. warning:: The round trip latency varies unpredictably for each
             combination of sample rate, audio buffer size, soundcard, computer,
             and :term:`OS`. If you decide to change the sample rate or buffer
             size you use with Mixxx, you will need to remeasure your round trip
             latency to have your microphone inputs aligned in your recorded
             and broadcasted mixes.

.. _microphones-activating-direct-monitoring-on-soundcard:

Activating direct monitoring on the soundcard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
General tips for activating direct monitoring are described below. However,
every soundcard is different, so refer to the soundcard manual from the
manufacturer for more details.

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

Refer to the section below for details about using microphones with
:ref:`DJ controllers <microphones-dj-controllers>`.

.. _microphones-external-mixing:

External mixing
---------------
Another way to work around the latency issue with software monitoring is to
send the output of Mixxx to a hardware mixer, plug a microphone into the
hardware mixer, and send the output of the hardware mixer back to Mixxx. To do
this, connect the output of the mixer to a soundcard input and configure that
soundcard input for Mixxx's Record/Broadcast input in
:guilabel:`Options -> Preferences -> Sound Hardware`. Other software for radio
and Internet broadcasting does not support latency compensation for microphone
inputs and only works with this kind of setup. This is generally not
recommended because mixers that can do this without decreasing the sound
quality of the music are much more expensive than soundcards with
microphone inputs that support
:ref:`direct monitoring <microphones-direct-monitoring>`.

Every conversion between digital and analog signals adds noise and distortion
to the signal, which reduces the sound quality. So, if you want to use an
external mixer with a microphone input, it is recommended to use a digital
mixer with a built in USB soundcard.

Using a hardware mixer with a computer's built in soundcard is not recommended.
It is not possible to use the mixer to mix stereo signals with only 2
output channels. Also, sound cards built into computers tend to have bad sound
quality.

.. figure:: ../_static/external-mixing-with-microphone-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Using a microphone with an external mixer
   :figclass: pretty-figures

   Using a microphone with an external mixer

.. _microphones-dj-controllers:

DJ Controllers
--------------
DJ controllers with microphone inputs typically have
:ref:`direct monitoring <microphones-direct-monitoring>` of microphone inputs
hardwired or switched on by default. Some DJ controllers also have a
:ref:`loopback input <microphones-loopback-input>` for easier setup, which may
need to be configured in the soundcard control panel provided by the
manufacturer with the driver. Refer to the controller's manual and its page on
the Mixxx wiki for details about setting up the specific controller's
microphone inputs with Mixxx.

Many cheap DJ controllers hardwire microphone inputs directly to the
master output without digitizing the signal to make it available to the
computer. If this is the case, you cannot use Mixxx's microphone input to
record or broadcast with the microphone using Mixxx's Microphone input. It is
still possible to record and broadcast the microphone by connecting the booth
output of the controller to a soundcard input and configuring this for Mixxx's
:guilabel:`Record/Broadcast` input. If the controller does not have a booth
output, a Y splitter cable can be used on each side of the stereo main output
to connect the main output to both the speakers and to another soundcard's
input.

.. figure:: ../_static/dj-controller-with-mic-and-splitter-cables.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Using a DJ controller with Y splitter cables to record and/or
         broadcast the mix with a microphone
   :figclass: pretty-figures

    Using a DJ controller with Y splitter cables to record and/or
    broadcast the mix with a microphone
