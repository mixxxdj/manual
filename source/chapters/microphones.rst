.. include:: /shortcuts.rstext

.. _microphones:

Using Microphones
*****************
Mixxx can work with any microphone that can be plugged into your :ref:`audio
interface <hardware-audio-interfaces>`. There are three ways to use microphones
with Mixxx, each with their own pros and cons:

  * :ref:`microphones-software-monitoring`: Cheapest and simplest to set up,
    but you cannot hear yourself without a disorienting delay, referred to as
    "latency".
  * :ref:`microphones-direct-monitoring`: Recommended for most users. This is
    the cheapest to set up with good sound quality and without the latency of
    software monitoring.
  * :ref:`microphones-hardware-mixers`: Most expensive option to set up with
    high sound quality. This does not have the latency of software monitoring.

.. warning:: USB microphones are not recommended. These devices have their own
             audio interface built in and can only be used with software
             monitoring. Some USB microphones have headphone jacks for direct
             monitoring, but the music from Mixxx cannot be heard in this
             headphone jack. Also, they can be difficult to configure at the
             same time as a different audio interface for music output.

.. seealso:: The `Mixxx DJ Hardware Guide
             <https://mixxx.org/wiki/doku.php/hardware_compatibility>`_ lists
             specific audio interfaces with information about their prices,
             features, and suitability for use with microphones.

.. _microphones-software-monitoring:

Software Monitoring
-------------------
Software monitoring can be used with the built-in microphone on a laptop or
with a headset plugged into the built-in audio interface on a computer.
However, there is a delay between the time you make sound into the microphone
and hear it in the Master output. Due to the nature of digital audio, it takes
time for input from the audio interface to be available for Mixxx to process,
time for Mixxx to process the audio, and more time to send the audio back out
the audio interface. This time is referred to as "latency".

.. TODO: Uncomment when this diagram is added.
  .. figure:: ../_static/software-monitor-signal-path.png
     :align: center
     :width: 80%
     :figwidth: 100%
     :alt: Microphone input with software monitoring signal path
     :figclass: pretty-figures

     Microphone input with software monitoring signal path

Mixxx can be configured to run at low latencies by choosing a smaller
:ref:`preferences-audio-buffer`, but there is no way to completely eliminate
latency. Although latency is measured in milliseconds, even a few milliseconds
of latency can be disorienting and distracting to hear, whether you are using
the microphone for spoken announcements, vocals, or playing a musical
instrument.

To use software monitoring:

#. Open :menuselection:`Preferences --> Sound Hardware`.
#. Select the :guilabel:`Input` tab.
#. For :guilabel:`Microphone 1`, select the audio interface that your
   microphone is plugged into.
#. Click the :guilabel:`Apply` button.
#. Click the :guilabel:`OK` button.
#. Click the :guilabel:`Mics` button in the main Mixxx window to show the
   microphone controls.
#. Click the :guilabel:`Talk` button when you are using the microphone.

.. hint:: If you would prefer to not hear the microphone input, you can set the
          :guilabel:`Microphone Monitor Mode` option to :guilabel:`Direct
          monitor (recording and broadcasting only)`. This will still mix the
          microphone input with your recorded and broadcasted mixes, but it
          will not mix the microphone with the Master output. Don't forget to
          press the :guilabel:`Talk` button when using the microphone if you
          use this option.

.. _microphones-direct-monitoring:

Direct Monitoring
-----------------
An audio interface with direct monitoring and a
:ref:`microphones-loopback-input` is the recommended way to use microphones with
Mixxx for most users. Except for audio interfaces built into computers, most
audio interfaces with microphone inputs support direct monitoring. However, not
all audio interfaces that support direct monitoring also have a loopback input.

Direct monitoring routes the audio from the audio interface's inputs directly
its outputs. This avoids the latency of sending it into the computer and back
out with :ref:`microphones-software-monitoring`. At the same time, the audio
interface sends the input into the computer so Mixxx can record and broadcast
it.

.. TODO: Uncomment when this diagram is added.
  .. figure:: ../_static/direct-monitor-signal-path.png
     :align: center
     :width: 80%
     :figwidth: 100%
     :alt: Microphone input with direct monitoring signal path
     :figclass: pretty-figures

     Microphone input with direct monitoring signal path

.. _microphones-loopback-input:

Loopback Input
^^^^^^^^^^^^^^
Some audio interfaces that support :ref:`microphones-direct-monitoring` have a
loopback input feature. They add Mixxx's output to the microphone signal before
sending it to the computer. This makes it easier to set up Mixxx with direct
monitoring than configuring :ref:`microphones-latency-compensation`.

.. TODO: Uncomment when this diagram is added.
  .. figure:: ../_static/direct-monitor-loopback-signal-path.png
     :align: center
     :width: 80%
     :figwidth: 100%
     :alt: Microphone input with direct monitoring signal path
     :figclass: pretty-figures

     Microphone input with direct monitoring signal path

To configure Mixxx with a loopback input:

#. Open :menuselection:`Preferences --> Sound Hardware`.
#. Click the :guilabel:`Input` tab.
#. Select the audio interface for the :guilabel:`Record/Broadcast` input. Do
   not configure anything for the :guilabel:`Microphone 1-4` inputs.
#. Click the :guilabel:`Apply` button.
#. Click the :guilabel:`OK` button.
#. :ref:`Activate direct monitoring and loopback on your audio interface.
   <microphones-activate-direct-monitoring>`
#. Adjust the microphone volume with the input gain knob on your audio
   interface.

The microphone controls in Mixxx will not affect your microphones because they
are mixed by the audio interface and not sent directly to Mixxx.

.. _microphones-latency-compensation:

Latency Compensation
^^^^^^^^^^^^^^^^^^^^
When using :ref:`microphones-direct-monitoring`, you will hear the microphone
mixed with the music from Mixxx without any noticable latency. However, it still
takes time for Mixxx to receive the microphone signal and process it. Without
compensating for this latency or using a :ref:`microphones-loopback-input`, the
microphone inputs will be out of time relative to the music in your recorded
and broadcasted mixes.

.. TODO: Uncomment when this diagram is added.
  .. figure:: ../_static/direct-monitor-input-latency.png
     :align: center
     :width: 80%
     :figwidth: 100%
     :alt: Diagram explaining latency offset with direct monitoring
     :figclass: pretty-figures

     Diagram explaining latency offset with direct monitoring

Mixxx can compensate for this timing misalignment, but it is complicated to set
up. If you do not want to record your microphone into your mix or broadcast,
you can :ref:`activate direct monitoring on your audio interface
<microphones-activate-direct-monitoring>` without configuring latency
compensation.

.. _microphones-measure-round-trip-latency:

Measuring Round Trip Latency
"""""""""""""""""""""""""""""
To configure Mixxx to compensate for input latency while using direct
monitoring, first you must measure the round trip latency of your setup. The
round trip latency is different from the size of the
:ref:`preferences-audio-buffer` configured in Mixxx. It is the amount of time
it takes for audio to make a complete trip from your audio interface's input,
through your computer, and back out the audio interface.

Mixxx cannot calculate the round trip latency because it depends on details of
your audio interface's hardware, your operating system, your audio interface's
driver, and other factors in your computer's hardware. The round trip latency
can only be found by measuring it. To do this, use a physical cable to connect
the audio interface's output to its input. Then, use a third party program to
measure the round trip latency. These programs are recommended on each OS:

* **GNU/Linux**:
  `jack_iodelay <https://www.linuxmusicians.com/viewtopic.php?t=8022>`_
* **Windows**: `RTL Utility  <http://www.oblique-audio.com/free/rtlutility>`_
* **macOS**: `Audacity <https://manual.audacityteam.org/man/latency_test.html>`_

.. TODO: Uncomment when this diagram is added.
  .. figure:: ../_static/latency-measurement.png
     :align: center
     :width: 80%
     :figwidth: 100%
     :alt: Measuring round trip latency
     :figclass: pretty-figures

     Measuring round trip latency

You must use the same sample rate and audio buffer size in the measurement
program as you do in Mixxx for the measurement to be accurate. If you decide to
change the sample rate or buffer size you use with Mixxx, you will need to
remeasure your round trip latency to have your microphone inputs aligned in
your recorded and broadcasted mixes.

.. warning:: Make sure direct monitoring is *not* :ref:`activated on your
             audio interface <microphones-activate-direct-monitoring>` while
             you are measuring the round trip latency or you will not get an
             accurate measurement.

.. _microphones-configure-latency-compensation:

Configuring Latency Compensation
""""""""""""""""""""""""""""""""
#. Before opening Mixxx, :ref:`measure the round trip latency
   <microphones-measure-round-trip-latency>`.
#. Open Mixxx.
#. Open :menuselection:`Preferences --> Sound Hardware`.
#. Click the :guilabel:`Input` tab.
#. Select the audio interface input(s) for the :guilabel:`Microphone 1-4`
   inputs. Select a single mono channel for each Microphone input unless you
   are using stereo microphones.
#. For the :guilabel:`Microphone Monitor Mode` option, select :guilabel:`Direct
   monitor (recording and broadcasting only)`.
#. Enter the measured round trip latency in millseceonds for the
   :guilabel:`Microphone Latency Compensation` option.
#. Click the :guilabel:`Apply` button.
#. Click the :guilabel:`OK` button.
#. :ref:`Activate direct monitoring on your audio interface.
   <microphones-activate-direct-monitoring>`
#. Click the :guilabel:`Mics` button in the main Mixxx window to show the
   microphone controls.
#. Click the :guilabel:`Talk` button when you are using the microphone.
#. Adjust the microphone volume with the input gain knob on your audio
   interface. Do not adjust the microphone gain in Mixxx. If you do, the
   relative volume of the mics and music will be different in your recorded
   and broadcasted mixes compared to what you hear out of your audio interface.

Mixxx will not record or broadcast your microphone if the :guilabel:`Talk`
button is not active. However, you will still hear the microphone in your main
output because the microphone is mixed by your audio interface, not Mixxx. You
may leave the :guilabel:`Talk` button on to ensure you do not forget it, but
this will record and broadcast background noise when you are not actively using
the microphone. If your microphone has an on/off switch on it, you may leave
the :guilabel:`Talk` button enabled in Mixxx and use the switch on the
microphone to avoid adding background noise to your mix. Alternatively, you can
adjust the input gain on your audio interface throughout your mix.

.. _microphones-activate-direct-monitoring:

Activating Direct Monitoring And Loopback On The Audio Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
General tips for activating direct monitoring and loopback are described below.
However, every audio interface is different, so refer to the audio interface
manual from the manufacturer for more details.

On stand-alone audio interfaces, there is often a knob on the device that
controls direct monitoring. This knob crossfades the audio interface's output
between the signal from the computer and the directly monitored inputs. If your
audio interface has a knob like this, set the knob to the center.
Alternatively, some audio interfaces have a switch to toggle direct monitoring
instead of a knob.

To hear mono microphone inputs on both sides of the stereo output with
direct monitoring, you typically need to toggle a switch on the device.

If the audio interface supports :ref:`microphones-loopback-input`, that may
be activated by a switch on the device.

Audio interfaces with lots of inputs and outputs often have a control panel
program provided by the manufacturer that is installed automatically with the
driver. This may be used instead of knobs and switches on the hardware to
control direct monitoring, loopback, stereo/mono switches, and other audio
interface features. On GNU/Linux, you might be able to access these controls
with :command:`alsamixer`.

Refer to the section below for details about :ref:`microphones-dj-controllers`.

.. _microphones-hardware-mixers:

Hardware Mixers
----------------
Mixxx can be used with a microphone plugged into an external hardware mixer.
This does not have the problem with latency that happens
with :ref:`microphones-software-monitoring`. However, it is generally
recommeded to use an audio interface that supports
:ref:`microphones-direct-monitoring` and a :ref:`microphones-loopback-input`
instead of an external mixer. If you are using :ref:`vinyl-control` and a
microphone, you may need an external mixer.

Mixxx can send each deck to separate stereo channels on an external mixer by
using the :guilabel:`Deck 1-4` outputs. This requires an audio interface with
at least 4 output channels (2 stereo pairs). Audio interfaces built into
computers only have one stereo output and they do not have high sound quality.
Thus, another audio interface is recommended. Audio interfaces with at least 4
output channels typically have microphone inputs and support
:ref:`microphones-direct-monitoring`, so there is no need for the external
mixer.

However, audio interfaces with phono preamplifiers for :ref:`vinyl-control` do
not have microphone inputs. If you want to use vinyl control with a microphone,
it is recommended to plug the microphone into a DJ mixer.

.. warning:: Some mixers that are not designed for DJing have a built-in USB
             audio interface. However, the audio interfaces in these mixers
             typically send only 2 channels (one stereo pair) to the mixer, so
             they are not recommended.

.. _microphones-record-broadcast-external-mixer:

Recording And Broadcasting With An External Hardware Mixer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To record or broadcast with an external hardware mixer, the output of the mixer
needs to be connected to the input of an audio interface. Most DJ mixers have
an extra output for this which may be labeled "record", "session", "auxiliary",
or "booth". Some audio interfaces for vinyl control have enough input channels
to receive the output of the mixer and timecode from two turntables. If yours
does not, you may use the input of the audio interface built into your
computer, but these do not have high sound quality.

.. TODO: Uncomment when this diagram is added.
  .. figure:: ../_static/external-mixing-with-microphone-signal-path.png
     :align: center
     :width: 80%
     :figwidth: 100%
     :alt: Using a microphone with an external mixer
     :figclass: pretty-figures

     Using a microphone with an external DJ mixer and a stand-alone USB audio
     interface

Alternatively, some DJ mixers have a built-in USB audio interface. These
have inputs with phono preamplifiers for vinyl control and usually can send
the record output back to the computer without a separate audio interface. Many
(but not all) of these mixers are digital mixers, so they can send signals back
and forth to Mixxx without converting them to analog. This results in higher
sound quality for your recorded and broadcasted mixes compared to using a
separate audio interface with an external mixer.

.. TODO: Uncomment when this diagram is added.
  .. figure:: ../_static/external-mixing-with-microphone-signal-path.png
     :align: center
     :width: 80%
     :figwidth: 100%
     :alt: Using a microphone with an external mixer that has a built in USB
           audio interface
     :figclass: pretty-figures

     Using a microphone with an external mixer that has a built in USB audio
     interface

To configure Mixxx for using a hardware mixer for recording and/or broadcasting:

#. Open :menuselection:`Preferences --> Sound Hardware`.
#. In the :guilabel:`Output` tab, select the audio interface for the
   :guilabel:`Deck 1-2` outputs (and :guilabel:`Deck 3-4` outputs if your audio
   interface and mixer support 4 decks).
#. Click the :guilabel:`Input` tab.
#. For the :guilabel:`Record/Broadcast` input, select the audio interface
   connected to the mixer's output. For mixers with a built-in USB audio
   interface, refer to the mixer manufacturer's manual to find which channels of
   the mixer's audio interface send the record output.
#. If you are using vinyl control, select the audio interface connected to the
   turntables for the :guilabel:`Vinyl Control 1-4` inputs.
#. Click the :guilabel:`Apply` button.
#. Click the :guilabel:`OK` button.

Do not configure anything for the :guilabel:`Microphone 1-4` inputs when using
an external mixer. The microphone controls in Mixxx will not affect your
microphones because the microphone is mixed by the external mixer.

DJ mixers typically do not supply phantom power required for condenser
microphones. Stand-alone audio interfaces typically do supply phantom power.

.. _microphones-dj-controllers:

DJ Controllers With Microphone Inputs
--------------------------------------
DJ controllers with microphone inputs typically mix the microphone input with
the master output without sending it to the computer. This does not have the
problem with latency that happens with
:ref:`microphones-software-monitoring`. However, many cheap DJ controllers do
not digitize the signal to make it available to the computer. Refer to the
controller's page on the `Mixxx wiki
<https://mixxx.org/wiki/doku.php/hardware_compatibility>`_ or the manual from
the controller manufacturer for details about your particular controller.

If the controller does not digitize the microphone input, you cannot use
Mixxx's microphone input to record or broadcast with the microphone using
Mixxx's :guilabel:`Microphone 1-4` inputs. It is still possible to record and
broadcast the microphone by connecting the booth output of the controller to an
audio interface input and configuring this for Mixxx's
:guilabel:`Record/Broadcast` input. If the controller does not have a booth
output, a Y splitter cable can be used on each side of the stereo main output to
connect the main output to both the speakers and to another audio interface's
input.

.. TODO: Uncomment when this diagram is added.
  .. figure:: ../_static/dj-controller-with-mic-and-splitter-cables.png
     :align: center
     :width: 80%
     :figwidth: 100%
     :alt: Using a DJ controller with Y splitter cables to record and/or
           broadcast the mix with a microphone
     :figclass: pretty-figures

     Using a DJ controller with Y splitter cables to record and/or broadcast the
     mix with a microphone

DJ controllers typically do not supply phantom power required for condenser
microphones. Stand-alone audio interfaces typically do supply phantom power.
