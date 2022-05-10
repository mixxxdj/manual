.. include:: /shortcuts.rstext

.. _appendix-settings-files:

The Mixxx Settings Directory
============================

.. sectionauthor::
   ronso0 <ronso0@mixxx.org>

The Mixxx settings directory contains all user data and settings of your Mixxx installation. If you want to make a backup of your library and all preferences copy the entire directory to a safe place.

Location
--------

.. hint:: On Windows, the :file:`AppData` folder is hidden, as well as all files and
          directories beginning with a dot '.' on Linux. So if you have not already,
          you will need to set your file manager to show hidden files and folders.

**Windows**
 | ``%LOCALAPPDATA%\Mixxx``
 | Copy this and paste it into the location bar of a Computer or Folder window.
 | ``%LOCALAPPDATA%`` is then resolved to ``C:\Users\<your-username>\AppData\Local``
 |
 | Use ``%USERPROFILE%\Local Settings\Application Data\Mixxx`` if you want to migrate your settings from XP or earlier.

**macOS**
 | Mixxx 2.3: ``~/Library/Containers/org.mixxx.mixxx/Data/Library/Application Support/Mixxx``
 | Mixxx 2.2 and earlier: ``~/Library/Application Support/Mixxx``

**Linux**
 | ``~/.mixxx/``
 | This resolves to ``/home/<your-username>/.mixxx``

Content
-------

**analysis**
    This contains all waveform analysis data. This is used to compose a track's
    scrolling waveform and track overview. If not existent, this data will be
    recreated each time a track is loaded into a Mixxx deck. Thus it does not
    belong to the essential data that needs to be backed up.

**broadcast_profiles**
    All broadcast profiles you have configured.

**controllers**
    All controller mappings you stored. This can be downloaded and :ref:`self-built
    mappings <advanced-controller>`, as well as built-in mappings that you modified in
    :guilabel:`Preferences` > :guilabel:`Controllers` > :guilabel:`YourController`
    manually or with the MIDI Wizard.

**effects.xml**
    The current configuration of the 4 effect units, incl. the state of all controls.

**mixxx.cfg**
    Everything you configured in the Preferences, deck settings, skin settings,
    AutoDJ configuration, effect routing etc.

**mixxx.log[.NN]**
    Log files of the last few Mixxx sessions, with ``mixxx.log`` being the most recent one,
    followed by ``mixxx.log.1`` etc.

**mixxxdb.sqlite**
    The Mixxx library database. All track locations, all track metadata, saved cues,
    loops, colors, playlists, crates, ...

**samplers.xml**
    Stores tracks currently loaded to sample decks.

**sandbox.cfg**
    This is used under macOS to track which files Mixxx will have access to

**soundconfig.xml**
    Sound device configuration from Preferences > Sound Hardware
