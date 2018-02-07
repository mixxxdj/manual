.. include:: /shortcuts.rstext

.. _microphones:

Using Microphones
*****************
There are three ways to use microphones with Mixxx, each with their own pros
and cons:
  * :ref:`Software monitoring<microphones-software-monitoring>`: Cheapest and 
    simplest to set up, but there is a disorienting delay, referred to as 
    "latency", between sound going into the microphone and hearing it come out 
    speakers or headphones.
  * :ref:`Direct monitoring<microphones-direct-monitoring>`: Recommended for 
    most users. This is the easiest and cheapest to set up with good sound 
    quality and without the latency issue of software monitoring.
  * :ref:`Hardware mixers<microphones-hardware-mixers>`: Most expensive option 
    to set up with high sound quality. This does not have the latency issue of 
    software monitoring.

.. warning:: USB microphones are not recommended. These devices have their own 
             soundcard built in and can only be used with software monitoring. 
             Some USB microphones have headphone jacks for direct monitoring, 
             but the music from Mixxx cannot be heard in this headphone jack. 
             Also, they can be difficult to configure at the same time as a 
             different soundcard for music output.

.. _microphones-software-monitoring:

Software monitoring
-------------------
Software monitoring can be used with the soundcard build into a computer, but
it has a big drawback. Due to the nature of digital audio, it takes time for
input from the soundcard to be available for Mixxx to process, time for Mixxx
to process the audio, and more time to send the audio back out the soundcard.
This time is referred to as "latency".

.. figure:: ../_static/software-monitor-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Microphone input with software monitoring signal path
   :figclass: pretty-figures

   Microphone input with software monitoring signal path

Mixxx can be configured to run at low latencies by choosing a smaller 
:ref:`preferences-audio-buffer`, but there is no way to completely eliminate 
latency. Thus, if you use software monitoring, you will hear the microphone 
signal out of the speakers after you make sound into the microphone. Although 
latency is measured in milliseconds, even a few milliseconds of latency can be 
disorienting and distracting to hear, whether you are using the microphone for 
spoken announcements, vocals, or playing a musical instrument.

.. _microphones-direct-monitoring:

Direct monitoring
-----------------
Direct monitoring with a :ref:`loopback input<microphones-loopback-input>` is 
the recommended way to use microphones with Mixxx for most users. To use direct 
monitoring, you need a soundcard that supports it. Most soundcards with 
microphone inputs support direct monitoring. A soundcard 
that also supports a loopback input is recommended for easier setup. Soundcards 
that come built into computers typically do not support direct monitoring.

Direct monitoring routes the audio from the soundcard's inputs directly to its
outputs to avoid the latency of sending it into the computer and back out with 
:ref:`software monitoring <microphones-software-monitoring>`. At the same time, 
the soundcard sends the input into the computer so Mixxx can
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
signal mixed into the music, set up a either a 
:ref:`loopback input<microphones-loopback-input>` or
:ref:`latency compensation <microphones-latency-compensation>`.

Because the microphones are mixed with the music by the soundcard rather 
than Mixxx, adjust the microphone volume with the input gain knob on 
your soundcard. If you adjust the microphone gain knob in Mixxx, the volume 
of the microphone relative to the music will be different in your recorded 
and broadcasted mixes compared to what you hear from your soundcard's output.

.. _microphones-loopback-input:

Loopback Input
^^^^^^^^^^^^^^
Some soundcards that support direct monitoring have a feature called
"loopback". Using direct monitoring with a soundcard that supports loopback is 
the recommended way to use microphones with Mixxx. It is the easiest to 
setup without the latency issue of
:ref:`software monitoring <microphones-software-monitoring>` and cheapest 
to set up with good sound quality.

Using direct monitoring, the microphone input is mixed with the music output 
from Mixxx by the soundcard. This avoids the latency of sending the
microphone signal into the computer and back out. The mixed signal is sent to
the speakers connected to the main output. Using the loopback feature, that
mixed signal is sent into the computer instead of the microphone signal alone,
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
input**.

Do not configure anything for the Microphone 1-4 inputs. The microphone 
controls in Mixxx will not affect your microphones because they are mixed by 
the soundcard and not sent directly to Mixxx.

.. _microphones-latency-compensation:

Latency Compensation
^^^^^^^^^^^^^^^^^^^^
When using direct monitoring without a
:ref:`loopback input <microphones-loopback-input>`, it still takes time for
Mixxx to receive the audio input from the soundcard and process it. Without 
compensating for this, the microphone inputs are out of time relative to the 
music in your recorded and broadcasted mixes even though they are aligned in 
what you hear from your soundcard's output.

.. figure:: ../_static/direct-monitor-input-latency.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Diagram explaining latency offset with direct monitoring
   :figclass: pretty-figures
   
   Diagram explaining latency offset with direct monitoring

Mixxx can compensate for this timing misalignment, but it is complicated to
set up. If you do not want to record your microphone into your mix or 
broadcast, you do not need to set this up.

To configure latency compensation, open
:guilabel:`Options -> Preferences -> Sound Hardware` and click the
:guilabel:`Input` tab. Select the soundcard input(s) for the Microphone 1-4
inputs. Make sure you select only a single mono channel for each Microphone
input instead of a stereo pair of channels (unless you have stereo
microphones set up). For the :guilabel:`Microphone Monitor Mode` option, select
**Direct monitor (recording and broadcasting only)**.

Set the :guilabel:`Microphone Latency Compensation` option to the round trip
latency. This is different from the size of the :ref:`preferences-audio-buffer`
configured in Mixxx. The round trip latency is amount of time it takes for
audio to make a complete trip from your soundcard's input, through your
computer, and back out the soundcard. Mixxx cannot calculate the round trip
latency amount because it depends on details of your soundcard's hardware, your
operating system, your soundcard's driver, and other factors in your computer's
hardware. You must use a physical cable to directly connect an output on your
soundcard to its input and use a third party program to measure the round trip
latency. These programs are recommended on each OS for measuring round trip 
latency:

* **GNU/Linux**: jack_iodelay
* **Windows**: RTL Utility
* **macOS**: Audacity?

.. figure:: ../_static/latency-measurement.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Measuring round trip latency
   :figclass: pretty-figures

   Measuring round trip latency

Copy the time measured in milliseconds by the measurement program into
the :guilabel:`Microphone Latency Compensation` option in Mixxx's Sound
Hardware Preferences. You must use the same sample rate and audio buffer size
in the measurement program as you do in Mixxx for the measurement to be
accurate.

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

.. _microphones-hardware-mixers:

Hardware Mixers
----------------
Mixxx can be used with a microphone plugged into an external hardware mixer. 
This does not have the problem with latency that happens with
:ref:`software monitoring<microphones-software-monitoring>`, but it is 
generally recommeded to use a sound card that supports
:ref:`direct monitoring<microphones-direct-monitoring>` and a
:ref:`loopback input<microphones-loopback-input>` instead. Mixers that can be 
used with Mixxx without reducing the sound quality of the music tend to be much 
more expensive than sound cards that support direct monitoring.

.. figure:: ../_static/external-mixing-with-microphone-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Using a microphone with an external mixer
   :figclass: pretty-figures

   Using a microphone with an external mixer and a stand-alone USB soundcard

Every conversion between digital and analog signals adds noise and distortion 
to the signal, which reduces the sound quality. Typically, a soundcard that 
converts the digital signals from Mixxx to analog is required to use Mixxx with 
an external mixer. To record and/or broadcast the mix, the mixer's analog 
output has to be converted back to digital by the soundcard to send it back 
to Mixxx. Alternatively, some mixers process signals digitally and have a 
built-in USB soundcard. These digital mixers can send signals back and forth to 
Mixxx without converting them to analog. Using these mixers with Mixxx will not 
reduce the sound quality of the music.

.. figure:: ../_static/external-mixing-with-microphone-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Using a microphone with an external mixer that has a built in USB 
         soundcard
   :figclass: pretty-figures

   Using a microphone with an external mixer that has a built in USB soundcard
   
To configure Mixxx for using a hardware mixer and a microphone, go to
:guilabel:`Options -> Preferences -> Sound Hardware`. In the Output 
tab, configure the :guilabel:`Deck 1-2` outputs (and :guilabel:`Deck 3-4` 
outputs if your soundcard and mixer support 4 decks) to send Mixxx's decks to 
the mixer. In the Input tab, if you want to record and/or broadcast your mix, 
configure the :guilabel:`Record/Broadcast` input to soundcard channels 
connected to the mixer's record, booth, or auxiliary output. For mixers with a 
built-in USB soundcard, refer to the mixer manufacturer's manual to find which 
channels of the mixer's soundcard send the record output back to the computer 
for the :guilabel:`Record/Broadcast` input. Do not configure anything for the
:guilabel:`Microphone 1-4` inputs.

Using a hardware mixer with a computer's built in soundcard is not recommended.
It is not possible to use the mixer to mix stereo signals with only 2
output channels. Also, soundcards built into computers tend to have bad sound
quality.

.. _microphones-dj-controllers:

DJ Controllers With Microphone Inputs
--------------------------------------
DJ controllers with microphone inputs typically mix the microphone input with 
the master output without sending it to the computer. This does not have the 
problem with latency that happens with
:ref:`software monitoring<microphones-software-monitoring>`. However, many 
cheap DJ controllers do not digitize the signal to make it available to the
computer. Refer to the controller's page on the
`Mixxx wiki <https://mixxx.org/wiki/doku.php/hardware_compatibility>`_
or the manual from the controller manufacturer for details about your 
particular controller.

If the controller does not digitize the microphone input, you cannot use 
Mixxx's microphone input to record or broadcast with the microphone using 
Mixxx's :guilabel:`Microphone 1-4` inputs. It is still possible to record and 
broadcast the microphone by connecting the booth output of the controller to a 
soundcard input and configuring this for Mixxx's :guilabel:`Record/Broadcast` 
input. If the controller does not have a booth output, a Y splitter cable can 
be used on each side of the stereo main output to connect the main output to 
both the speakers and to another soundcard's input.

.. figure:: ../_static/dj-controller-with-mic-and-splitter-cables.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Using a DJ controller with Y splitter cables to record and/or
         broadcast the mix with a microphone
   :figclass: pretty-figures

   Using a DJ controller with Y splitter cables to record and/or broadcast the 
   mix with a microphone
