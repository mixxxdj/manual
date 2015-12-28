.. include:: /shortcuts.rstext

.. _configuration-mixxx:

Mixxx Setup
***********

.. _configuration-open:

Opening Mixxx
=============
|logo| Once you've :ref:`installed Mixxx <installing-mixxx>`, start by opening
Mixxx and importing your music to the Mixxx library.

**Windows**
  Double-click the Mixxx icon on the Desktop. Alternatively, browse your Windows
  start menu and click the Mixxx icon, or perform a search for
  :file:`Mixxx.exe`.

**Mac OSX**
  Double-click the Mixxx icon in the :file:`Applications` folder. Alternatively,
  drag the Mixxx icon to the dock and double-click it there or search for
  "Mixxx" in Spotlight.

**GNU/Linux**
  Simply type :command:`mixxx` into the terminal, then hit :kbd:`Return`. With
  some distributions like Ubuntu you can also double-click the Mixxx icon in the
  launcher. Alternatively, perform a search for :file:`mixxx`.

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
inputs and outputs to be used.

* **Sound API**: Depending on your :term:`Operating System`, select the :term:`API`
  that Mixxx uses to deliver audio to your audio device. Your choice can
  drastically affect how well Mixxx performs on your computer.

* **Sample Rate**: Allows you to manually select the sample rate for the audio
  input. The sample rate value should be set to the sample rate of your audio
  interface. By default, Mixxx tries the system default first, which is most
  likely 44.1 kHz. Otherwise, Mixxx will pick a different default.

* **Audio buffer**: Also known as latency, this is the lag time in milliseconds
  that it takes for Mixxx to process your input. Lower latency means Mixxx
  will be more responsive but on slower computers and cheaper sound cards it
  might cause glitches.

* **Buffer Underflow Count**: Underflows (data is not available when needed)
  indicate that some of the subsystems in Mixxx can't keep up with real-time
  deadlines imposed by the current audio buffer size. This is useful to
  tune the latency settings. If the counter increases, then increase your audio
  buffer size, decrease the sample rate setting or change the sound API
  setting if available.

.. _configuration-mixer-mode:

Audio Outputs
=============

Mixxx's mixing engine can be used in two ways:

**Internal Mixer Mode**
  In this mode, Mixxx performs the mixing of the decks, microphone, and samplers
  in software and outputs them to a single output. To enable internal mixer mode,
  assign a valid audio output to the :guilabel:`Master` output in
  :menuselection:`Preferences --> Sound Hardware --> Output`.

  Internal mode is used in the following configurations:

  * :ref:`setup-laptop-only`
  * :ref:`setup-laptop-and-external-card`
  * :ref:`setup-controller-and-external-card`

**External Mixer Mode**
  In this mode, Mixxx outputs the audio from each deck to a separate soundcard
  output. This allows you to route the deck outputs through a hardware mixer.
  To enable external mixer mode, select a valid audio output
  for the :guilabel:`Deck` outputs in
  :menuselection:`Preferences --> Sound Hardware --> Output`.

  External mode is used in the following configuration:

  * :ref:`setup-vinyl-control`

Headphone Output
----------------

In both internal and external mixer mode, you can choose a headphone output for
:term:`pre-fader listening <PFL>` or :term:`headphone cueing <cueing>` in
:menuselection:`Preferences --> Sound Hardware --> Output --> Headphone`. This
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
keyboard/mouse or a controller. An audio buffer below 10 ms is recommended
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

+-----------------------------+------------+
| OS / Audio API              | Quality    |
+=============================+============+
| Windows / ASIO              | Good       |
+-----------------------------+------------+
| Windows / WDM-KS            | Good       |
+-----------------------------+------------+
| Windows / WASAPI            | Acceptable |
+-----------------------------+------------+
| Windows / DirectSound       | Poor       |
+-----------------------------+------------+
| Windows / MME               | Poor       |
+-----------------------------+------------+
| Mac OS X / CoreAudio        | Good       |
+-----------------------------+------------+
| GNU Linux / ALSA            | Good       |
+-----------------------------+------------+
| GNU Linux / JACK (Advanced) | Good       |
+-----------------------------+------------+
| GNU Linux / OSS             | Acceptable |
+-----------------------------+------------+

For low latency on Windows, it is best to use an ASIO driver that bypassses
the sound processing of the Windows kernel. If there is no such ASIO driver
available for your soundcard, use the WDM-KS API. There is generally no
advantage to using ASIO4ALL <http://asio4all.com>_, a wrapper around the
WDM-KS API.

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

If the PulseAudio plugin for alsalibs is installed on GNU/Linux, you can
choose the virtual device ``pulse``. This allows Mixxx to share the default
system sound card with other media players. This only works if you start
Mixxx without pasuspender, which you can do by running "mixxx" from a console
rather than clicking the launcher icon in a menu or on your desktop. Since the
sound stream is routed from ALSA to Pulse and back to ALSA, this adds an
additional latency of ~2 x the selected audio buffer size.

Equalizer Preferences
=====================

.. sectionauthor::
   Daniel Schürmann <daschuer@mixxx.org>

.. figure:: ../_static/Mixxx-111-Preferences-Equalizer(TODO).png
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
  displayed. Unchecking "Only allow EQ knobs to control EQ specific effects"
  allows you to select any other effect.

* **Quick Effect**: Here you can select the effect that is controlled by the
  dedicated filter knob in each deck. By default only built-in filter effects are
  selected for all decks, but that can be changed as above.

* **High/Low Shelf EQ**: This slider sets the crossover frequencies of the mixing
  EQ. It controls which frequency range is affected by the low, mid, and high
  channel EQ knobs. By default the low knob controls the bass and sub bass
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

cut: the frequency response (curve form) at the cross over frequency.

roll-off: The steepness of the EQ bands.

linear phase: No phase distortion, all frequencies are processed with the same group delay.

minimum phase: A natural phase distortion, the group delay changes by the frequency.

bit perfect: Whether the EQ leaves the original samples untouched when the EQ is at unity.

CPU usage: Processing time needed to calculate the EQ output.

.. _configuration-import:

Importing your audio files
==========================

.. sectionauthor::
   S.Brandt <s.brandt@mixxx.org>

.. figure:: ../_static/Mixxx-111-1st-run-choose-library-directory-win.png
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Mixxx 1st run - Choose music library directory dialog
   :figclass: pretty-figures

   Mixxx running on Windows 8 - Choose music library directory dialog


**Setup the music library**
  The first time you run Mixxx, you are asked to select a directory where your
  music is stored. By default, the dialog points to a location where music files
  are typically held, but you can select any location on your computer.

  Click :guilabel:`Select Folder` and Mixxx will scan your music library.
  Depending on the size of your library this could take some time. All the
  supported music files Mixxx detects will be listed in the :ref:`library-root`.

  If you want to refresh your library (for example because you added or moved
  files), you can do this with :menuselection:`Library --> Rescan Library` in
  the menu. If you want to rescan at every launch, select
  :menuselection:`Preferences --> Library --> Rescan on startup`.

  .. warning :: On Windows 7 and 8 the import dialog points to your Windows
                “Music“ Library, a special-purpose virtual folder. You can
                **not** use these virtual folders. Select a regular folder
                instead, usually “My Music“, like pictured above.

**Compatible files**

  .. versionadded:: 2.0
     Support for the Opus audio format.

  Mixxx supports a variety of audio file formats: :term:`Wave <WAV>` (wav),
  :term:`Aiff <AIFF>` (aiff, aif), :term:`MP3` (mp3), :term:`Ogg Vorbis` (ogg),
  :term:`FLAC` (flac), :term:`Opus` (opus), and :term:`AAC` (aac, m4a) if
  supported by your :term:`OS <Operating System>`. :term:`DRM` protected files,
  such as m4p files purchased in the iTunes Store, are not supported.

  AAC (M4A) is supported on Windows Vista and Mac OS X 10.5 onwards. The
  `Platform Update Supplement <http://support.microsoft.com/kb/2117917>`_
  is required for Windows Vista.

  On Linux, AAC playback is disabled by default due to licensing restrictions.
  To enable the playback of AAC files, `build Mixxx from source with m4a/AAC
  files support <http://www.mixxx.org/wiki/doku.php/compiling_on_linux#build_with_m4a_aac_file_support>`_.

**Import external libraries**
  If you have iTunes, Traktor, Rhythmbox, or Banshee installed, Mixxx allows you
  to access your tracks and playlists in the Mixxx library,
  see :ref:`library-3rd-party`.

**Import remote files**
  To import audio files which are not in your music library directory, drag them
  directly from an external :term:`file manager` or from the :ref:`Browse section
  <library-browse>` to the track list. Importing files into Mixxx does not
  change the location of the files on the hard disk.

  .. note :: You can not drag complete folders to the library because currently
             Mixxx can not recursively scan folders for compatible music files.

**Import playlists**
  You can import existing :file:`m3u`, :file:`pls` , :file:`m3u8`, :file:`pls`
  playlist files from products other than Mixxx, see :ref:`library-playlists`.

**Import music from CDs**
  Mixxx can not play music from Audio CDs. Convert the content to compatible
  files in good quality and add them to the Mixxx library. See
  `<https://en.wikipedia.org/wiki/Ripping>`_

.. _configuration-changing-music-directories:

Changing music directories
==========================

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

.. _configuration-removing-tracks:

Removing tracks from the library
================================

Removing tracks from the Mixxx library will **not** physically delete them from
your drive. However it does delete extra metadata Mixxx might have (such as
hotcues and the beatgrids), and removes links to playlists or crates.

#. Click the :guilabel:`Library` item in the sidebar.
#. Find and select the tracks you want to remove, perform a right-click on them
   and select :guilabel:`Hide from Library` from the context menu.
#. Expand the :guilabel:`Library` item in the sidebar and click on the
   :guilabel:`Hidden tracks` sub-item. All tracks that were set to be hidden
   from the library will appear here.
#. Select the tracks you want to remove, or use the :guilabel:`Select All`
   button.
#. To confirm you want to permanently remove these tracks from the library,
   click :guilabel:`Purge`.

.. hint:: If you later decide to add some of the deleted tracks back, import
          them to the Mixxx library again, see :ref:`configuration-import`.

.. _configuration-bpm-detection:

BPM and Beat Detection Preferences
==================================

.. sectionauthor::
   T.Rafreider <trafreider@mixxx.org>
   S.Brandt <s.brandt@mixxx.org>

.. TODO:: Update this section to explain the differences between the beatgrid
          and beatmap options.

Mixxx uses an ultra-precise BPM and beat detector. Manual adjustments
are redundant in many cases because Mixxx knows where the beats are.

Analyzer Settings
-----------------

BPM and beat detection is a complex operation. Depending on your computer and
the track's bitrate and duration this may take some time. By default Mixxx
analyzes the complete track. To accelerate beat detection on slower computers, a
“Fast Analysis” option is available. If enabled, the BPM is computed by
analyzing the first minute of the track. In most cases this does not affect the
beat detection negatively because most of today's dance music is written in a
4/4 signature with a fixed tempo.

.. figure:: ../_static/Mixxx-111-Preferences-Beatdetection.png
   :align: center
   :width: 75%
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

Key Detection Preferences
=========================

Mixxx comes with a high precision musical key detector to help you make smooth
mixes by ensuring that your tracks are musically compatible.

Analyzer Settings
-----------------

Key detection is a complex operation. Depending on your computer and the track's
bitrate and duration this may take some time. By default Mixxx analyzes the
complete track. To accelerate key detection on slower computers, a “Fast
Analysis” option is available. If enabled, the key is computed by analyzing the
first minute of the track.

.. figure:: ../_static/Mixxx-112-Preferences-Keydetection.png
   :align: center
   :width: 75%
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

.. _configuration-analyze:

Analyze your library
====================

.. sectionauthor::
   RJ Ryan <rryan@mixxx.org>
   S.Brandt <s.brandt@mixxx.org>

|ic_lib_prepare| Mixxx automatically analyzes tracks the first time you load
them in a deck, nevertheless it is recommended that you analyze them before
playing live to ensure the beatgrids are correct. Furthermore, track
analysis takes considerable CPU power and might cause skips in the audio ---
things you surely don't need while performing.

Once you have configured your music directories and your BPM and key detection
settings, press :guilabel:`OK` on the Preferences window. Go to the Analyze
view on the left side panel of the library. This allows you to run
:term:`beatgrid`, :term:`key`, and :term:`ReplayGain` detection on tracks in
advance. While analyzing, the progress in percentage and total queue length are
shown.

.. versionadded:: 2.0
   Drag and drop tracks from the library or external file managers onto the
   analysis view to instantly analyze these files. The title changes to
   :guilabel:`Analyze (x/y)` where x is the number of tracks that have been
   analyzed so far and y is the total number of tracks originally in the queue.

.. versionchanged:: 2.0
   Does not generate waveforms to save disk space.

The Analyze features in detail:

* **All / New radio-buttons**: Allows you to view a list of either all tracks in
  the library or tracks added to the library within the last 7 days.
* **Select All button**: Selects all tracks in the current view.
* **Analyze button**: Starts the detection on the selected tracks.

.. seealso:: For more information, go to :ref:`configuration-bpm-detection`.
