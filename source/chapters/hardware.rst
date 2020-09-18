.. include:: /shortcuts.rstext

.. _hardware:

DJ Hardware
***********

.. sectionauthor::
   T.Rafreider <trafreider@mixxx.org>
   S.Brandt <s.brandt@mixxx.org>
   Be <be.0@gmx.com>
   Jan Holthuis <jholthuis@mixxx.org>

Although Mixxx can be used with just a laptop or desktop computer, fully taking
advantage of Mixxx's features requires specialized DJ hardware. Depending on
your budget and application area, your setup and requirements may vary. This
chapter provides general background information about various types of DJ
hardware.

To make DJing with Mixxx a fun experience, at least the following pieces are needed:

- speakers to play the music to the audience,
- an :ref:`audio interface <hardware-audio-interfaces>` with 4 mono/2 stereo
  output channels (or 2 mono output channels + a :ref:`DJ splitter cable
  <hardware-splitter-cables>`),
- :ref:`headphones <hardware-headphones>` for prelistening tracks while another
  track is playing on the speakers, and
- audio cables and adapters to connect the equipment to your computer.

Additionally, you might consider getting the follwing equiment:

- a :ref:`controller <hardware-controllers>`,
- :ref:`turntables <hardware-turntables>`, an audio interface with phono inputs
  and :ref:`timecode vinyl <vinyl-control-media>`,
- a laptop/controller stand,
- a surge protector to protect the equipment from voltage spikes,
- cases for laptop, controller and headphones, and
- custom fader and knob caps to customize your gear.

.. seealso:: The `Mixxx DJ Hardware Guide <https://mixxx.org/wiki/doku.php/hardware_compatibility>`_
             lists specific devices with information about their prices,
             features, and compatibility with Mixxx.

.. _hardware-controllers:

Controllers
===========
DJ controllers are devices with knobs, faders, buttons, and jog wheels to
control DJ software such as Mixxx. Controllers allow quick access to different
controls while providing tactile and visual feedback indicating the state of
each control, such as the position of a knob or whether a switch is on or off.
This allows you to focus on manipulating the music without needing to look at
your computer screen all the time. Controllers also allow using two hands to
manipulate two different controls at the same time, which is required for many
mixing techniques.

DJ controllers typically do not do any actual audio processing. Instead, they
send signals (typically :term:`MIDI` or :term:`HID` over a USB cable) to the
computer to instruct DJ software how to manipulate the audio. Many DJ
controllers include an :ref:`audio interface <hardware-audio-interfaces>` with
2 separate stereo outputs built into the device. This allows the DJ to
transport and setup only one piece of hardware in addition to a laptop. Some
devices can be used as both a controller and :ref:`hardware mixer
<hardware-mixers>`.

Mixxx can work with any :term:`MIDI` or :term:`HID` :term:`controller` as long
as there is a mapping file to tell Mixxx how to understand the controller's
signals. Mixxx comes bundled with a number of MIDI and HID mapping presets,
which are listed in the `Mixxx DJ Hardware Guide
<https://mixxx.org/wiki/doku.php/hardware_compatibility>`_ on the wiki. For
controllers that Mixxx does not yet support, you can `search the forum
<https://mixxx.org/forums/search.php?fid[]=7>`_ to see if anyone has
started a mapping. You can also start one yourself using the information in the
`Controller Mapping Documentation
<https://mixxx.org/wiki/doku.php/start#controller_mapping_documentation>`_
on the wiki.

.. seealso:: :ref:`control-midi` describes how to configure Mixxx to use
             controllers.

.. _hardware-audio-interfaces:

Audio Interfaces
================
An audio interface (also known as a "sound card", although few of them are
shaped like cards anymore) is a device that allows a computer to send output to
and receive input from audio equipment. Whether using :ref:`internal or
external mixing <intro-how-mixxx-works>`, it is recommended to use a single
audio interface with at least 4 independent output channels (2 separate stereo
pairs).

The headphone jack on most laptops is not a second audio output. Rather,
plugging headphones into the jack simply redirects the laptop's single stereo
output from its speakers to your headphones. A :ref:`splitter cable
<hardware-splitter-cables>` can be used to separate the stereo output of a
headphone jack into two separate mono outputs for headphone cueing, but it is
recommended to use a sound card with at least four mono outputs (for two stereo
pairs). Such sound cards tend to be higher quality than those built into
laptops and allow your mix to be enjoyed in stereo by your audience.

Unlike some proprietary DJ systems, Mixxx can use any audio interface and any
:term:`MIDI` or :term:`HID` controller that your :term:`OS <operating system>`
has drivers to use. If your controller has an integrated audio interface, you
may choose to use a different audio interface for higher quality audio. Mixxx
can also use multiple audio interfaces simultaneously.

Audio Interface Considerations
------------------------------
This section provides background information to help you choose an audio
interface to use with Mixxx.

Bit Depth and Sample Rate
^^^^^^^^^^^^^^^^^^^^^^^^^
Most music is published with a bit depth of 16 bits at a sample rate of 44.1
kHz because this is all that is needed to store all the detail of music in
digital form.

Bit depth determines the possible dynamic range of the signal. 16 bits is more
than enough for playing back music. While 24 bits is helpful for recording,
`it is useless for playback
<https://sonicscoop.com/2013/08/29/why-almost-everything-you-thought-you-
knew-about-bit-depth-is-probably-wrong/>`_.

Half the sample rate determines the maximum frequency that can be represented
by the signal. Humans generally can't hear frequencies above 20 kHz, so a
sampling rate of 44.1 kHz, representing a maximum frequency of 22.05 kHz, is
fine for playback. Higher sample rates like 88.2 kHz and 96 kHz can be helpful
to reduce aliasing distortion when recording, but have no benefit for playback
and make your computer work harder.

For a more thorough and technical explanation of why 16 bits at 44.1 kHz is all
that is needed for playback, read `24/192 Music Downloads Are Very Silly Indeed
<https://web.archive.org/web/20120306150922/https://people.xiph.org/~xiphmont/
demo/neil-young.html>`_.

Specifications
^^^^^^^^^^^^^^
When considering specifications, higher dynamic range, higher signal-to-noise
ratio (SNR), higher maximum output level, lower THD+N (Total Harmonic
Distortion + Noise; look for a more negative dB value or smaller percentage),
and lower crosstalk (more negative dB value) are better. Cheap audio interfaces
tend to not have these specifications published.

Connector and Cable Types
^^^^^^^^^^^^^^^^^^^^^^^^^
If you are unfamiliar with professional audio equipment, read Digital DJ Tips'
`Essential Guide to Audio Cables for DJs
<https://www.digitaldjtips.com/2011/07/the-essential-guide-to-audio-cables-for-djs>`_
to understand the different kinds of connectors on audio interfaces. It
is better to use an audio interface with balanced outputs, especially if you
will run long cables directly into an amplifier or active speakers without
going through a :ref:`hardware mixer <hardware-mixers>`. Balanced signals
reject interference and are less susceptible to ground loop hum issues (which
can be a problem when plugging unbalanced gear into separate power sources).

However, most venues have DJs plug into :ref:`hardware DJ mixers
<hardware-mixers>`, which typically only have RCA inputs (RCA cables cannot be
balanced). Most home/computer speakers and amplifiers have RCA and/or 1/8" TRS
stereo inputs. Most live sound mixers have balanced 1/4" TRS mono inputs. If
you need to interconnect balanced and unbalanced gear, refer to this `guide
from Presonus (deleted, via archive.org)
<https://web.archive.org/web/20171011070552/https://www.presonus.com/learn/technical-articles/Balanced-Unbalanced>`_
and this `guide from Rane (deleted, via archive.org)
<https://web.archive.org/web/20191224231514/rane.com/note110.html>`_.

Number of Channels
^^^^^^^^^^^^^^^^^^^
Audio interfaces sometimes have multiple connectors for a single channel,
resulting in more connectors than channels. So, not every connector can send or
receive and independent signal. For example, some audio interfaces made for
DJing have 4 output channels with 4 mono output connectors and 1 stereo
headphone connector. This does not mean that the audio interface can send out 6
different signals at the same time; rather, the signal on 2 of the mono outputs
and the stereo headphone output would be the same. Also, many controllers have
separate master and booth outputs with independent volume controls, but they
both play the same signal.

Vinyl Control and Phono Preamplifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Turntables output low voltage (phono level) signals that need to be amplified
to line level before most audio equipment can work with them. So, if you want
to use :ref:`vinyl-control`, sometimes referred to as a Digital Vinyl System
(DVS), it is best to have phono preamplifiers (one for each deck) somewhere
between your turntable and sound card to boost the turntable's phono level
signal to line level. Mixxx can amplify phono level signals in software, but it
is better to do it in hardware. The phono preamp can be in the turntable, in
the audio interface, or a stand alone device. Most audio interfaces do not have
phono preamps; these are generally found on audio interfaces specifically made
for controlling DJ software with timecode vinyl. :ref:`hardware-mixers` with
audio interfaces have phono preamps on their deck inputs, but not necessarily
on every deck input. Many higher-end all-in-one controllers also include audio
interfaces with phono preamps.

Driver Support
^^^^^^^^^^^^^^
Unlike some proprietary DJ programs, Mixxx works with any audio interface that
is compatible with your operating system — including for timecode vinyl (DVS)
use.

USB Audio Class compliant audio interfaces should work out of the box on all
operating systems supported by Mixxx. This is the case for the integrated audio
interfaces in most DJ controllers. Sound cards that aren't USB Audio Class
compliant need a driver for each OS.

.. note:: On Windows, you should install the manufacturer's drivers even for
   USB class compliant audio interfaces to be able to use the recommended ASIO
   sound API.

.. hint:: If you are considering buying a controller or audio interface, the
   easiest way to tell if it is USB class compliant before you buy it is to
   search for macOS drivers for the device on the manufacturer's website. If it
   is advertised as compatible with macOS or iOS but there are no drivers to
   download for macOS, the device is USB class compliant.

.. _hardware-mixers:

Mixers
======
Mixers are devices that combine audio signals. DJ mixers are different from
live and studio mixers because they have multiple stereo channels with phono
preamplifiers for connecting :ref:`hardware-turntables`. It is conventional to
use a DJ mixer with :ref:`vinyl-control`, but vinyl control can be used without
a hardware mixer.

Using Mixxx with a DJ mixer requires an audio interface with at least 4 mono
outputs (2 stereo pairs) to send Mixxx's decks to the mixer's stereo channels.
Some DJ mixers have a USB :ref:`audio interface <hardware-audio-interfaces>`
built into them. This lets Mixxx send unmixed audio files directly to the mixer
without needing a separate stand-alone audio interface.

Often DJs who use DJ software with internal mixing send their master output to
a hardware mixer. This can be helpful to send the mixed signal to both a main
speaker output for the audience and booth speakers for the DJ with separate
gain controls for each output. It also facilitates smooth transitions between
DJs.

However, using an external mixer with internal mixing is not necessary and
reduces the sound quality. Each piece of equipment an audio signal passes
through reduces the sound quality, so avoiding unnecessary equipment in the
signal path can provide better sound quality. Many DJ controllers provide
separate master and booth outputs with independent volume controls.
Alternatively, a sound card with at least 6 output channels can be used with
Mixxx's :guilabel:`Booth` output.

Many people confuse "analog mixers" and "hardware mixers", but these are
not the same. Many hardware mixers process audio digitally with specialized
signal processors as opposed to a general purpose CPU like those in laptop and
desktop computers.

.. seealso:: :ref:`microphones-record-broadcast-external-mixer`

.. _hardware-turntables:

Turntables
==========
Turntables are mechanical devices that play music recordings cut into vinyl
phonograph records. Before software like Mixxx was available, the art of DJing
originated with turntables and :ref:`DJ mixers <hardware-mixers>`. Special
vinyl records can be used with turntables to control the playback of digital
files in Mixxx as if the digital file was pressed onto the vinyl record.

.. seealso:: :ref:`vinyl-control`

CDJs
====
CDJs are devices that play digital audio files and have controls from
manipulating the playback of the audio. Originally CDJs played audio CDs, but
new devices typically use USB storage drives or SD cards. Some CDJs can be
plugged into a computer with a USB cable to function as a :ref:`controller
<hardware-controllers>` for Mixxx.

Microphones
===========
Microphones convert changes in sound pressure in air to changes in voltage (an
analog audio signal). Mixxx can work with any microphone that can be plugged
into your :ref:`audio interface <hardware-audio-interfaces>`.

.. seealso:: :ref:`microphones`

.. _hardware-headphones:

Headphones
==========

Being able to listen to what you will play next in headphones before your
audience hears on the main speakers or your broadcast stream is an essential
part of DJing. DJ headphones are generally better quality than typical consumer
headphones. Importantly, they are designed to have good isolation, meaning they
block outside sound. This allows the DJ to focus on the sound in the headphones
better without having to turn up the volume to drown out sound from the
monitors, PA system, and chatter. Also, DJ headphones have hinges or flexible
headbands that allow the DJ to take off one headphone cup to hear the monitor
or PA output better in one ear and compare it to the headphone output in the
other ear.

When shopping for headphones, consider how well they isolate sound and their
durability. The most frequent places that headphones break are the cable
attachment point and the headband. Look for headphones with detachable cables,
metal headbands, and other individually replaceable parts. Avoid Bluetooth
headphones because these may be unreliable and will always reduce sound
quality. Active noise canceling headphones also tend to have worse sound
quality than other headphones of a comparable price. DJ headphones with a
closed design block out a lot of sound simply by being closed.

Whether to get on-ear or over-ear headphones is a matter of personal
preference. Everyone's head is different, so headphones that are comfortable
for a friend or a reviewer may not be comfortable for you.

In-ear monitors (IEMs) isolate sound better than headphones but are more
expensive. They usually cost more than double the price of good DJ headphones
with comparable quality. They may be a sound investment for musicians who play
often in very loud environments to preserve their hearing.

.. _hardware-splitter-cables:

Splitter Cables
===============
DJ splitter cables are the cheapest way to get two separate sound outputs from
your computer.  These plug into the onboard audio interface built into computer
motherboards and split the stereo signal into two separate mono signals.
However, onboard audio interfaces are not good quality, and you lose the stereo
effect of hearing different sounds arranged in space.

Devices marketed as "headphone splitter" instead of DJ splitters duplicate one
stereo signal in two jacks.  These cannot be used for headphone cueing.  Also,
generic stereo-to-mono splitter cables or adapters typically have two mono jack
outputs.  Plugging headphones or stereo speakers into a generic stereo-to-mono
splitter will only play sound on one side of the headphones or speakers.
