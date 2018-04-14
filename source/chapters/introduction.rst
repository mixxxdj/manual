.. _intro:

Introduction to Mixxx
*********************

Mixxx enables you to perform live DJ mixes with your digital music collection.
It helps you rock the party with DJ controllers, vinyl turntables, or even just
your keyboard. It is developed by an international team of volunteers who want
to bring the joy of DJing to everyone. The project is non-profit, open-source
and community driven. Together, we aim to build the best DJ software ever
created. We hope you will join us!

.. _intro-how-mixxx-works:

How Mixxx Works
===============
Mixxx is different from typical music player applications because it plays
multiple audio files at the same time and has many features to
manipulate the playback of the audio files. This lets you creatively mix
different tracks together on the fly.

You can use Mixxx to preview the next track in headphones before the audience
hears it, also known as headphone cueing. This helps you choose a track that
is appropriate for the present moment and that will mix well into the
currently playing track(s). To use headphone cueing, you need at least 2
separate audio outputs, typically provided by a USB audio interface (also known
as a “sound card”, although most of them are not shaped like cards anymore).
Mixxx can be used in two different ways for headphone cueing:

**Internal Mixing**

  Mixxx plays multiple audio files on the computer at the same
  time, mixes them together, and sends the mixed signal to one audio interface
  output. A separate signal is sent to another audio interface output
  for headphone cueing. Often a DJ controller is used with internal mixing to
  provide easier control over Mixxx than a mouse and keyboard.

  .. figure:: ../_static/mixxx_setup_midi_integrated_audio_interface.png
     :align: center
     :width: 75%
     :figwidth: 100%
     :alt: Using Mixxx together with a DJ controller and integrated audio
           interface
     :figclass: pretty-figures

     Using Mixxx together with a DJ controller for internal mixing. The
     DJ controller has an integrated audio interface that provides two separate
     stereo outputs.

**External Mixing**

  In this kind of setup, Mixxx plays multiple audio files on the computer at
  the same time and sends each track to a separate audio interface output. The
  audio interface's outputs are plugged into an external hardware mixer. The
  hardware mixer performs the actual mixing of the audio signals. On the
  hardware mixer, there are separate outputs for the mixed signal to play to
  the audience and for the DJ to use headphone cueing. External mixing is
  typically used with turntables and :ref:`special vinyl
  records<vinyl-control>` to manipulate digital music files as if the music was
  on the vinyl records.

  .. figure:: ../_static/mixxx_setup_timecode_vc.png
     :align: center
     :width: 75%
     :figwidth: 100%
     :alt: Using Mixxx together with turntables and external mixer
     :figclass: pretty-figures

     Using Mixxx together with a USB audio interface, external mixer, and
     timecode vinyl for external mixing
>>>>>>> upstream/manual-2.1.x
