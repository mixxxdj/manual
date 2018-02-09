.. include:: /shortcuts.rstext

.. _microphones:

Using Microphones
*****************
There are three ways to use microphones with Mixxx, each with their own pros
and cons:

  * :ref:`Software monitoring<microphones-software-monitoring>`: Cheapest and 
    simplest to set up, but you cannot hear yourself without a disorienting 
    delay, referred to as "latency".
  * :ref:`Direct monitoring<microphones-direct-monitoring>`: Recommended for 
    most users. This is the cheapest to set up with good sound quality and 
    without the latency of software monitoring.
  * :ref:`Hardware mixers<microphones-hardware-mixers>`: Most expensive option 
    to set up with high sound quality. This does not have the latency of 
    software monitoring.

.. warning:: USB microphones are not recommended. These devices have their own 
             audio interface built in and can only be used with software 
             monitoring. Some USB microphones have headphone jacks for direct 
             monitoring, but the music from Mixxx cannot be heard in this 
             headphone jack. Also, they can be difficult to configure at the 
             same time as a different audio interface for music output.

.. _microphones-software-monitoring:

Software monitoring
-------------------
Software monitoring can be used with the built-in microphone on a laptop or 
with a headset plugged into the built-in audio interface on a computer. 
However, there is a delay between the time you make sound into the microphone 
and hear it in the Master output. Due to the nature of digital audio, it takes 
time for input from the audio interface to be available for Mixxx to process, 
time for Mixxx to process the audio, and more time to send the audio back out 
the audio interface. This time is referred to as "latency".

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

.. hint:: If you would prefer to not hear the microphone input mixed with 
          Mixxx's output, you can set the :guilabel:`Microphone Monitor Mode` 
          option to :guilabel:`Direct monitor (recording and broadcasting 
          only)`. This will still mix the microphone input with your 
          recorded and broadcasted mixes, but it will not mix the microphone 
          with the Master output. Don't forget to press the :guilabel:`Talk` 
          button when using the microphone if you use this option.

.. _microphones-direct-monitoring:

Direct monitoring
-----------------
Direct monitoring with a :ref:`loopback input<microphones-loopback-input>` is 
the recommended way to use microphones with Mixxx for most users. Except for 
audio interfaces built into computers, most audio interfaces with microphone 
inputs support direct monitoring. However, not all audio interfaces that 
support direct monitoring also have a loopback input feature.

Direct monitoring routes the audio from the audio interface's inputs directly to 
its outputs to avoid the latency of sending it into the computer and back out 
with :ref:`software monitoring <microphones-software-monitoring>`. At the same 
time, the audio interface sends the input into the computer so Mixxx can record 
and broadcast it.

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
Some audio interfaces that support :ref:`direct monitoring 
<microphones-direct-monitoring>` have a loopback input feature. This adds 
Mixxx's output to the microphone input that the audio interface sends to the 
computer. Configuring Mixxx to record and/or broadcast a loopback input is 
easier to set up than configuring :ref:`latency compensation 
<microphones-latency-compensation>`.

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
#. Select the audio interface for the :guilabel:`Record/Broadcast input`. Do 
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
When using :ref:`direct monitoring <microphones-direct-monitoring>`, it still 
takes time for Mixxx to receive the audio input from the audio interface and 
process it. Without compensating for this latency or using a :ref:`loopback 
input <microphones-loopback-input>`, the microphone inputs are out of time 
relative to the music in your recorded and broadcasted mixes even though they 
are aligned in what you hear from your audio interface's output.

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
<microphones-activate-direct-monitoring>` without configuring 
latency compensation.

To configure latency compensation:

#. Open :menuselection:`Preferences --> Sound Hardware`.
#. Click the :guilabel:`Input` tab.
#. Select the audio interface input(s) for the :guilabel:`Microphone 1-4` 
   inputs. Select a single mono channel for each Microphone input instead of a 
   stereo pair of channels (unless you have stereo microphones set up).
#. For the :guilabel:`Microphone Monitor Mode` option, select :guilabel:`Direct 
   monitor (recording and broadcasting only)`.
#. :ref:`Measure the round trip latency 
   <microphones-measure-round-trip-latency>` and enter that time in 
   milliseconds for the :guilabel:`Microphone Latency Compensation` option.
#. Click the :guilabel:`Apply` button.
#. Click the :guilabel:`OK` button.
#. :ref:`Activate direct monitoring on your audio interface. 
   <microphones-activate-direct-monitoring>`
#. Click the :guilabel:`Mics` button in the main Mixxx window to show the 
   microphone controls.
#. Click the :guilabel:`Talk` button when you are using the microphone. 
   Mixxx will not record or broadcast your microphone if the 
   :guilabel:`Talk` button is not active. However, you will still hear the 
   microphone in your main output because the microphone is mixed by your    
   audio interface, not Mixxx. You may leave the :guilabel:`Talk` button on to 
   ensure you do not forget it, but this will record and broadcast background 
   noise when you are not actively using the microphone.
#. Adjust the microphone volume with the input gain knob on your audio 
   interface. Do not adjust the microphone gain in Mixxx or the relative volume 
   of the mics and music will be different in your recorded and broadcasted 
   mixes compared to what you hear out your audio interface.

.. _microphones-measure-round-trip-latency:

Measuring round trip latency
"""""""""""""""""""""""""""""

The round trip latency is different from the size of the 
:ref:`preferences-audio-buffer` configured in Mixxx. It is the amount of time it 
takes for audio to make a complete trip from your audio interface's input, 
through your computer, and back out the audio interface. Mixxx cannot calculate 
the round trip latency because it depends on details of your audio interface's 
hardware, your operating system, your audio interface's driver, and other 
factors in your computer's hardware. You must use a physical cable to directly 
connect an output on your audio interface to its input and use a third party 
program to measure the round trip latency. These programs are recommended on 
each OS for measuring round trip latency:

* **GNU/Linux**: `jack_iodelay <https://www.linuxmusicians.com/viewtopic.php?t=8022>`_
* **Windows**: `RTL Utility  <http://www.oblique-audio.com/free/rtlutility>`_
* **macOS**: `Audacity <https://manual.audacityteam.org/man/latency_test.html>`_

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
remeasure your round trip latency to have your microphone inputs aligned in your 
recorded and broadcasted mixes.

.. warning:: Make sure direct monitoring is not :ref:`activated on your 
             audio interface <microphones-activate-direct-monitoring>` while you 
             are measuring the round trip latency or you will not get an 
             accurate measurement.
             
Copy the round trip latency time in milliseconds into the :guilabel:`Microphone 
Latency Compensation` option in the :guilabel:`Sound Hardware` section of 
Mixxx's Preferences. Refer to the :ref:`Latency Compensation 
<microphones-latency-compensation>` section above for more detailed setup 
instructions.

.. _microphones-activate-direct-monitoring:

Activating direct monitoring and loopback on the audio interface
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

To hear mono microphone inputs on both sides of the main stereo output with 
direct monitoring, you typically need to toggle a switch on the device.

To activate loopback input, there may be a switch on the device.

Soundcards with lots of inputs and outputs often have a proprietary
program provided by the manufacturer that is installed automatically with the
driver instead of knobs and switches on the hardware to control direct
monitoring, loopback, stereo/mono switches, and other audio interface features. 
On GNU/Linux, you might be able to access these controls with alsamixer.

Refer to the section below for details about using microphones with
:ref:`DJ controllers <microphones-dj-controllers>`.

.. _microphones-hardware-mixers:

Hardware Mixers
----------------
Mixxx can be used with a microphone plugged into an external hardware mixer. 
This does not have the problem with latency that happens with
:ref:`software monitoring <microphones-software-monitoring>`, but it is 
generally recommeded to use an audio interface that supports
:ref:`direct monitoring <microphones-direct-monitoring>` and a
:ref:`loopback input <microphones-loopback-input>` instead unless you are 
using :ref:`vinyl control <vinyl-control>`. Mixers that can be 
used with Mixxx without reducing the sound quality of the music tend to be much 
more expensive than audio interfaces that support direct monitoring.

.. figure:: ../_static/external-mixing-with-microphone-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Using a microphone with an external mixer
   :figclass: pretty-figures

   Using a microphone with an external DJ mixer and a stand-alone USB audio 
   interface

Every conversion between digital and analog signals adds noise and distortion 
to the signal, which reduces the sound quality. Typically, an audio interface 
that converts the digital signals from Mixxx to analog is required to use Mixxx 
with an external mixer. To record and/or broadcast the mix, the mixer's analog 
output has to be converted back to digital by the audio interface to send it 
back to Mixxx.

Alternatively, some mixers process signals digitally and have a 
built-in USB audio interface. These digital mixers can send signals back and 
forth to Mixxx without converting them to analog. Using these mixers with Mixxx 
will not reduce the sound quality of the music.

.. figure:: ../_static/external-mixing-with-microphone-signal-path.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Using a microphone with an external mixer that has a built in USB 
         audio interface
   :figclass: pretty-figures

   Using a microphone with an external mixer that has a built in USB audio 
   interface
   
To configure Mixxx for using a hardware mixer and a microphone:

#. Open :menuselection:`Options -> Preferences -> Sound Hardware`.
#. In the :guilabel:`Output` tab, configure the :guilabel:`Deck 1-2` outputs 
   (and :guilabel:`Deck 3-4` outputs if your audio interface and mixer support 
   4 decks). If you do not want to record or broadcast your mix, no further 
   setup is required.
#. Click the :guilabel:`Input` tab.
#. Configure the :guilabel:`Record/Broadcast` input to audio interface channels 
   connected to the mixer's record, booth, or auxiliary output. For mixers with 
   a built-in USB audio interface, refer to the mixer manufacturer's manual to 
   find which channels of the mixer's audio interface send the record output.

Do not configure anything for the :guilabel:`Microphone 1-4` inputs when using 
an external mixer.

Using a hardware mixer with a computer's built in audio interface is not 
recommended. It is not possible to use the mixer to mix stereo signals with 
only 2 output channels. Also, audio interfaces built into computers tend to 
have bad sound quality.

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
broadcast the microphone by connecting the booth output of the controller to an 
audio interface input and configuring this for Mixxx's 
:guilabel:`Record/Broadcast` input. If the controller does not have a booth 
output, a Y splitter cable can be used on each side of the stereo main output to 
connect the main output to both the speakers and to another audio interface's 
input.

.. figure:: ../_static/dj-controller-with-mic-and-splitter-cables.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Using a DJ controller with Y splitter cables to record and/or
         broadcast the mix with a microphone
   :figclass: pretty-figures

   Using a DJ controller with Y splitter cables to record and/or broadcast the 
   mix with a microphone
