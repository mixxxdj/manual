.. include:: /shortcuts.rstext

.. _appendix-settings-files:

The Mixxx Settings Directory
============================

.. sectionauthor::
   ronso0 <ronso0@mixxx.org>

The Mixxx settings directory contains all user data and settings of your Mixxx installation. If you want to make a backup of your library and all preferences copy the entire directory to a safe place.

Location
--------

You can navigate to the settings directory location manually as described below. Since Mixxx 2.3 you can also open this directory in your file browser from within Mixxx: go to :menuselection:`Preferences --> Library`, scroll to the bottom of the page and click on :guilabel:`Open Mixxx Settings Directory`.

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
 | For distribution packages, or Mixxx installed from source:
 | ``~/.mixxx/``
 | This resolves to ``/home/<your-username>/.mixxx``
 |
 | For Flatpak:
 | ``~/.var/app/org.mixxx.Mixxx/.mixxx``

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

BackUp
------

**preferences**
    To avoid users accidentally changing the BackUp settings, these settings
	were not included in the preferences.
	The BackUp settings need to be adjusted in the mixxx.cfg.

**default**
    By default, Mixxx makes a BackUp once a day at startup.
	[BackUp]

    By default, five BackUps are saved.

**settings**
    [BackUp]
    BackUpEnabled 1
    BackUpFrequency daily
    KeepXBUs 5
    LastBackUp *

    In the mixxx.cfg is a part [BackUp] containing the settings.
    BackUpEnabled 1
    The default '1' enables the backupsystem while 0 disables it.

    BackUpFrequency daily
    The default 'daily' sets the frequency to 1 BackUp a day,
    'always' sets the frequency to 'a BackUp on every startup'

    KeepXBUs 5
    with the default setting of '5', five BackUps are kept, if you have already
    5 BackUps the oldest will be deleted before Mixxx creates a new one.
    You can change this value to change the number of kept BackUps.
    Setting KeepXBUs to '0' will prevent Mixxx from deleting old BackUps,
    in this case all BackUps will be kept.

    The LastBackup field keeps the date (YYYYMMDD) of the last backup, used to determinate
    the need of creating a new BackUp if the frequency is set to daily.
	
**location**
    On Windows the BackUps are created in the folder in your Documents directory 
    -> <username>/Documents/Mixxx-BackUps
    On MacOS the BackUps are created in the container of Mixxx 
    -> /Users/>username>/Library/Containers/org.mixxx.mixxx/Data/Documents/Mixxx-BackUps/
    On Linux the BackUps are created in your home/Documents folder
    -> /home//Documents/Mixxx-BackUps/

**BackUps on upgrade**
   When Mixxx is upgraded to a new version a BackUp named 'Upgrade Version xxx' 
   will be created in a subfolder 'Upgrade' in the Mixxx-BackUps folder.
   These backups will not be automatically deleted.
