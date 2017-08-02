.. include:: /shortcuts.rstext

.. _getting-started-mixxx:

Getting Started
***************

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
  :command:`mixxx` in Spotlight.

**GNU/Linux**
  Click the Mixxx icon in the applications menu or launcher of your desktop
  environment or perform a search for :file:`mixxx`. Alternatively type
  :command:`mixxx` into the terminal, then hit :kbd:`Return`.
  If your :term:`soundcard` is not accessible from Mixxx because it is used by
  other applications via PulseAudio, you may close and restart Mixxx using
  :command:`pasuspender mixxx`. See :ref:`appendix-command-line-options` for an
  overview of Mixxx's command line options.

.. _getting-started-sound-io:

Configuring sound input and output
==================================

Before you can start using Mixxx, you need to configure Mixxx to use your
sound hardware in :menuselection:`Preferences --> Sound Hardware`. At a
minimum, one output must be configured. You do not need to configure all inputs
and outputs.

.. seealso:: For Mixxx to perform the best it can on your system, read the
             full details about all the :ref:`preferences-sound-hardware`
             preferences.

.. seealso:: The :ref:`hardware` chapter explains different types of DJ
             hardware and how to set them up with the the input and output
             options.

.. figure:: ../_static/Mixxx-200-Preferences-Soundhardware.png
   :align: center
   :width: 80%
   :figwidth: 100%
   :alt: Mixxx Sound Hardware Preferences
   :figclass: pretty-figures

   Mixxx Sound Hardware Preferences

Output Options
--------------

Internal mixing
^^^^^^^^^^^^^^^

* **Master**: all decks, samplers, microphones, and auxiliary inputs mixed
  together
* **Headphones**: all decks, samplers, microphones, and auxiliary inputs
  assigned to :term:`pre-fader listening <PFL>`
* **Booth**: same as Master output, but has a separate gain control

External mixing
^^^^^^^^^^^^^^^

* **Decks 1-4**: the individual unmixed decks to send to an external mixer
* **Bus Left/Center/Right**: all decks, samplers, and auxiliary inputs
  assigned to each side of Mixxx's crossfader

Input Options
-------------

Internal mixing
^^^^^^^^^^^^^^^

* **Microphone 1-4**: live microphone or musical instrument inputs
* **Auxiliary 1-4**: other sound sources

External mixing
^^^^^^^^^^^^^^^
* **Record/Broadcast**: When this is configured, Mixxx will record and
  broadcast from this soundcard input instead of the internal master mix.

Either internal or external mixing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* **Vinyl Control 1-4**: timecode input from turntables or CDJs for
  manipulating decks 1-4

.. _getting-started-import-audio-files:

Importing your audio files
==========================

.. sectionauthor::
   S.Brandt <s.brandt@mixxx.org>

.. figure:: ../_static/Mixxx-200-1st-run-choose-library-directory-win.png
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Mixxx 1st run - Choose music library directory dialog
   :figclass: pretty-figures

   Mixxx running on Windows 10 - Choose music library directory dialog


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
  To enable the playback of AAC files,
  `build Mixxx from source with m4a/AAC files support <http://www.mixxx.org/wiki/doku.php/compiling_on_linux#optionalbuild_with_m4a_aac_file_support>`_.

**Import external libraries**
  If you have iTunes, Traktor, Rhythmbox, or Banshee installed, Mixxx allows you
  to access your tracks and playlists in the Mixxx library,
  see :ref:`library-3rd-party`.

**Import remote files**
  To import audio files which are not in your music library directory, drag them
  directly from an external :term:`file manager` or from the
  :ref:`Browse section<library-browse>` to the track list. Importing files
  into Mixxx does not change the location of the files on the hard disk.

  .. note :: You can not drag complete folders to the library because currently
             Mixxx can not recursively scan folders for compatible music files.

**Import playlists**
  You can import existing :file:`m3u`, :file:`pls` , :file:`m3u8`, :file:`pls`
  playlist files from products other than Mixxx, see :ref:`library-playlists`.

**Import music from CDs**
  Mixxx can not play music from Audio CDs. Convert the content to compatible
  files in good quality and add them to the Mixxx library. See
  `<https://en.wikipedia.org/wiki/Ripping>`_

.. _getting-started-analyze-library:

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

The Analyze features in detail:

* **All / New radio-buttons**: Allows you to view a list of either all tracks in
  the library or tracks added to the library within the last 7 days.
* **Select All button**: Selects all tracks in the current view.
* **Analyze button**: Starts the detection on the selected tracks.

.. seealso:: For more information, go to :ref:`configuration-bpm-detection`.
