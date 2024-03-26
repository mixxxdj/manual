.. include:: /shortcuts.rstext

Library
=======

.. _configuration-import:

Changing music directories
--------------------------

You can manually add, relink, and remove Mixxx music directories in
:menuselection:`Preferences --> Library`.

**Add a new music directory**
  Mixxx handles multiple music library folders. Click :guilabel:`Add` to
  browse to a directory where your music is stored. Mixxx will watch this
  directory and its subdirectories for new tracks.

  If you add a directory that is already in your library, or you are currently
  :ref:`rescanning your library <library-tracks>`, the operation is canceled.

  Directories can also be added from the :ref:`Computer <library-computer>`
  sidebar item inside the library.

**Relink an existing music directory**
  If an existing music directory is moved or renamed, Mixxx doesn't know where to
  find the audio files in it. The tracks will still show in library but they can't
  be loaded on decks and the tracks will become missing after the library is rescanned.

  To relink the music directory, go to :menuselection:`Preferences --> Library`,
  click :guilabel:`Relink` to select the music directory in its new location. This will
  re-establish the links to the audio files in the Mixxx library.

  Click :menuselection:`Library --> Rescan Library`, this will update the tracks and
  cause them to show up again in the library, check the location column in the library
  and you should see that it now points to the new music directory.

  The playlists, crates, history and all track data like cue points, rating, comments etc.
  are preserved after relinking the library, the tracks are also not re-analyzed as the cached
  analysis is reused. You can confirm this by checking the :term:`Key <key>` and :term:`BPM <BPM>`
  columns to see if there is a key and BPM for every track.

.. note:: It is recommended to take a backup of your Mixxx configuration files before moving or renaming music directories used in Mixxx.
          For locations in each supported :term:`OS <operating system>` as well as detailed descriptions of all settings files, go to :ref:`appendix-settings-files`.

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
