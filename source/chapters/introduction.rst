Introduction to Mixxx
*********************

Mixxx allows you to perform live DJ mixes with your digital music collection.
It helps you rock the party with DJ controllers, vinyl turntables, or even just
your keyboard. It is developed by an international team of volunteers who
want to bring the joy of DJing to everyone. The project is non-profit,
open-source and community driven. Together and with your help we aim to build
the best DJ software ever created.

Mixxx has lots of features to manipulate music, but these are only tools. Mixxx
will not instantly make you a great DJ. It up to you to develop your own ways
to use these tools in creative ways. This manual will help you understand
Mixxx's features and provide hints about how to get started using them.

Some effort has been made to present the material in a way that is neither too
technical nor too dumbed-down. Take some time to look through it and you'll
find lots of hints that will enhance both your enjoyment and your productivity.

How Mixxx Works
===============
Mixxx is different from typical music player applications because it is designed
to play multiple audio files at the same time and has many features to
manipulate the playback of the audio files. This lets you creatively mix
different music together on the fly.

Additionally, you can use Mixxx to preview the next track you would like to
play in headphones before the audience hears it, also known as headphone
cueing. This helps you choose a track that is appropriate for the present
moment and that will mix well into the currently playing track(s). In order to
use headphone cueing, you need at least 2 separate audio outputs, typically
provided by a USB soundcard (also known as an “audio interface”). Mixxx can be
used in two different ways for headphone cueing:

**Internal Mixing**

  Mixxx plays multiple audio files on the computer at the same
  time, mixes them together, and sends the mixed signal to one soundcard
  output. A separate signal is sent to another soundcard output for headphone
  cueing. Often a DJ controller is used with internal mixing to provide easier
  control over Mixxx than a mouse and keyboard.

  .. figure:: ../_static/mixxx_setup_midi_integrated_sound.png
     :align: center
     :width: 75%
     :figwidth: 100%
     :alt: Using Mixxx together with a DJ controller and integrated soundcard
     :figclass: pretty-figures

     Using Mixxx together with a DJ controller for internal mixing. The
     DJ controller has an integrated soundcard that provides two separate
     stereo outputs.

**External Mixing**

  Mixxx plays multiple audio files on the computer at the same time and sends
  each track to a separate soundcard output. The soundcard's outputs are
  plugged into an external hardware mixer. The hardware mixer performs the
  actual mixing of the audio signals. On the hardware mixer, there are separate
  outputs for the mixed signal to play to the audience and for the DJ to use
  headphone cueing.

  External mixing is typically used with turntables and
  :ref:`special vinyl records<vinyl-control>` to manipulate digital music files
  as if the music was on the vinyl records. Sometimes DJs who use external
  mixing also use a small controller for Mixxx features that are not available
  on the hardware mixer.

  .. figure:: ../_static/mixxx_setup_timecode_vc.png
     :align: center
     :width: 75%
     :figwidth: 100%
     :alt: Using Mixxx together with turntables and external mixer
     :figclass: pretty-figures

     Using Mixxx together with a USB sound card, external mixer, and
     timecode vinyl for external mixing
