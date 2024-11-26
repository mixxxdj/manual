.. This is a generated file. Do not edit it manually, because it is updated
   automatically via tools/update_changelog.py.

.. include:: /shortcuts.rstext

.. _appendix-changelog:


Changelog
=========

.. _v2-4-2:

`2.4.2 <https://github.com/mixxxdj/mixxx/milestone/43?closed=1>`__ (2024-11-26)
----------------------------------------------------------------------------------

Controller Mappings
^^^^^^^^^^^^^^^^^^^


* Denon MC7000: Fix star up/down logic by only handling button down events `#13588 <https://github.com/mixxxdj/mixxx/pull/13588>`__
* Intech TEK2: Add initial mapping `#13521 <https://github.com/mixxxdj/mixxx/pull/13521>`__
* Korg Kaoss DJ: Update script `#12683 <https://github.com/mixxxdj/mixxx/pull/12683>`__
* MIDI for light: Fix unsound timer handling `#13117 <https://github.com/mixxxdj/mixxx/pull/13117>`__
* Novation Dicer: Remove flanger mapping with quickeffect toggle
  `#13196 <https://github.com/mixxxdj/mixxx/pull/13196>`__
  `#13134 <https://github.com/mixxxdj/mixxx/issues/13134>`__
* Novation Launchpad X: Fix detection on macOS
  `#13691 <https://github.com/mixxxdj/mixxx/pull/13691>`__
  `#13633 <https://github.com/mixxxdj/mixxx/issues/13633>`__
* Numark PartyMix: Fix EQ (script binding) display name `#13255 <https://github.com/mixxxdj/mixxx/pull/13255>`__
* Numark Scratch: Add initial mapping
  `#4834 <https://github.com/mixxxdj/mixxx/pull/4834>`__
  `#13375 <https://github.com/mixxxdj/mixxx/pull/13375>`__
* Pioneer DDJ-400 and DDJ-FLX4: Remove tap beat mapping to resolve conflict with toggle quantize and fix shift + play
  `#13815 <https://github.com/mixxxdj/mixxx/pull/13815>`__
  `#13813 <https://github.com/mixxxdj/mixxx/issues/13813>`__
  `#13857 <https://github.com/mixxxdj/mixxx/pull/13857>`__
* Reloop Beatmix 2/4: Fix eject button and jog LED being lit on track unload
  `#13601 <https://github.com/mixxxdj/mixxx/pull/13601>`__
  `#13605 <https://github.com/mixxxdj/mixxx/pull/13605>`__
* Reloop Mixage MK1, MK2, Controller Edition: Add initial mapping `#12296 <https://github.com/mixxxdj/mixxx/pull/12296>`__
* Sony SIXAXIS: Fix mapping `#13319 <https://github.com/mixxxdj/mixxx/pull/13319>`__

Fixes
^^^^^


* Handle not supported files when dragging to waveforms and spinnies
  `#13208 <https://github.com/mixxxdj/mixxx/pull/13208>`__
  `#13271 <https://github.com/mixxxdj/mixxx/pull/13271>`__
  `#13275 <https://github.com/mixxxdj/mixxx/pull/13275>`__
* Fix Sqlite 3.45 builds by using only single quotes for SQL strings
  `#13247 <https://github.com/mixxxdj/mixxx/pull/13247>`__
  `#13257 <https://github.com/mixxxdj/mixxx/pull/13257>`__
* LateNight: Use default colors for sampler overviews (like main decks) `#13274 <https://github.com/mixxxdj/mixxx/pull/13274>`__
* Library: Allow to drop files to decks with unsupported or no file extensions
  `#13209 <https://github.com/mixxxdj/mixxx/pull/13209>`__
  `#13204 <https://github.com/mixxxdj/mixxx/issues/13204>`__
* Update build environment with libdjinterop 0.21.0 `#13288 <https://github.com/mixxxdj/mixxx/pull/13288>`__
* Move to GitHub workflow runner macos-12
  `#13296 <https://github.com/mixxxdj/mixxx/pull/13296>`__
  `#13248 <https://github.com/mixxxdj/mixxx/issues/13248>`__
* Recording: with empty config, save default split size immediately
  `#13304 <https://github.com/mixxxdj/mixxx/pull/13304>`__
* Allow to drop files with supported MIME type regardless off the file extensions
  `#13209 <https://github.com/mixxxdj/mixxx/pull/13209>`__
  `#13204 <https://github.com/mixxxdj/mixxx/issues/13204>`__
* Add support for Ubuntu Oracular Oriole and remove Lunar Lobster
  `#13348 <https://github.com/mixxxdj/mixxx/pull/13348>`__
* Recordbox: Fix string decoding issues
  `#13293 <https://github.com/mixxxdj/mixxx/pull/13293>`__
  `#13291 <https://github.com/mixxxdj/mixxx/issues/13291>`__
* Mixer preferences: Don't update EQs/QuickEffects while applying `#13333 <https://github.com/mixxxdj/mixxx/pull/13333>`__
* Hardware preferences: Fix UX when applying config with missing/busy devices
  `#13312 <https://github.com/mixxxdj/mixxx/pull/13312>`__
* Fix minor 64 bit CPU performance issue `#13355 <https://github.com/mixxxdj/mixxx/pull/13355>`__
* Fix clicks at loop-out when looping into lead-in `#13294 <https://github.com/mixxxdj/mixxx/pull/13294>`__
* Fix wrong pitch value on startup, caused by ``components.Pot``
  `#11814 <https://github.com/mixxxdj/mixxx/issues/11814>`__
  `#13463 <https://github.com/mixxxdj/mixxx/pull/13463>`__
* Engine Prime: Fix build-failure `#13397 <https://github.com/mixxxdj/mixxx/pull/13397>`__
* Engine Prime: Friendlier error message if export fails `#13524 <https://github.com/mixxxdj/mixxx/pull/13524>`__
* macOs: Fix Keyboard shortcuts by not catching num key modifier
  `#13481 <https://github.com/mixxxdj/mixxx/pull/13481>`__
  `#13305 <https://github.com/mixxxdj/mixxx/issues/13305>`__
* Skins: fix time display to allow AM/PM
  `#13430 <https://github.com/mixxxdj/mixxx/pull/13430>`__
  `#13421 <https://github.com/mixxxdj/mixxx/issues/13421>`__
* Fix detection last sound if track does not end with silence.
  `#13545 <https://github.com/mixxxdj/mixxx/pull/13545>`__
  `#13449 <https://github.com/mixxxdj/mixxx/issues/13449>`__
* Remove false positive critical warning related to library columns
  `#13165 <https://github.com/mixxxdj/mixxx/pull/13165>`__
  `#13164 <https://github.com/mixxxdj/mixxx/issues/13164>`__
* Fix reading metadata for files with wrong extensions
  `#13218 <https://github.com/mixxxdj/mixxx/pull/13218>`__
  `#13205 <https://github.com/mixxxdj/mixxx/issues/13205>`__
* History: remove purged tracks, auto-remove empty playlists
  `#13579 <https://github.com/mixxxdj/mixxx/pull/13579>`__
  `#13578 <https://github.com/mixxxdj/mixxx/issues/13578>`__
* Synchronize AutoDJ next deck with top track in queue
  `#12909 <https://github.com/mixxxdj/mixxx/pull/12909>`__
  `#8956 <https://github.com/mixxxdj/mixxx/issues/8956>`__
* Playlists: Update play duration and bold state in sidebar when dragging tracks into the playlist table
  `#13591 <https://github.com/mixxxdj/mixxx/pull/13591>`__
  `#13590 <https://github.com/mixxxdj/mixxx/issues/13590>`__
  `#13575 <https://github.com/mixxxdj/mixxx/pull/13575>`__
* Playlists: Keep correct track selection (# position) when sorting
  `#13103 <https://github.com/mixxxdj/mixxx/pull/13103>`__
* Track file export: Various fixes
  `#13610 <https://github.com/mixxxdj/mixxx/pull/13610>`__
* Controller engine: Unify/improve logging, expand error dialog's Details box
  `#13626 <https://github.com/mixxxdj/mixxx/pull/13626>`__
* Fix quantization in the effect engine (metronome effect)
  `#13636 <https://github.com/mixxxdj/mixxx/pull/13636>`__
  `#13733 <https://github.com/mixxxdj/mixxx/pull/13733>`__
* Musicbrainz: Improved messages
  `#13672 <https://github.com/mixxxdj/mixxx/pull/13672>`__
  `#13673 <https://github.com/mixxxdj/mixxx/pull/13673>`__
* Fix ReplayGain detection in case of short tracks
  `#13680 <https://github.com/mixxxdj/mixxx/pull/13680>`__
  `#13676 <https://github.com/mixxxdj/mixxx/issues/13676>`__
  `#13702 <https://github.com/mixxxdj/mixxx/issues/13702>`__
  `#13703 <https://github.com/mixxxdj/mixxx/pull/13703>`__
* Track menu: Avoid crash and UX issues with track nullptr
  `#13685 <https://github.com/mixxxdj/mixxx/pull/13685>`__
* Disable Properties shortcut in Computer feature views
  `#13698 <https://github.com/mixxxdj/mixxx/pull/13698>`__
* Overview waveform: Add tooltip info about left-click dragging
  `#13739 <https://github.com/mixxxdj/mixxx/pull/13739>`__
* Make ``hotcue_focus_color_next``\ /\ ``_prev`` COs ``ControlPushButton``\ s to allow direct mappings
  `#13764 <https://github.com/mixxxdj/mixxx/pull/13764>`__
* Scaled svg cache to speed up drawing in hidpi mode `#13679 <https://github.com/mixxxdj/mixxx/pull/13679>`__
* Update to libdjinterop 0.22.1 for Enigine Prime 4.0.1 support `#13790 <https://github.com/mixxxdj/mixxx/pull/13790>`__
* HID: Avoid repeated error messages from hid_write()/hid_read() in case of errors
  `#13692 <https://github.com/mixxxdj/mixxx/pull/13692>`__
  `#13660 <https://github.com/mixxxdj/mixxx/issues/13660>`__
* Fix unnecessary painting with covers in library `#13715 <https://github.com/mixxxdj/mixxx/pull/13715>`__
* Fix check for unrelated decks playing when starting Auto DJ
  `#13762 <https://github.com/mixxxdj/mixxx/pull/13762>`__
  `#13734 <https://github.com/mixxxdj/mixxx/issues/13734>`__
* Fix read before m_bufferInt during scratching
  `#13917 <https://github.com/mixxxdj/mixxx/pull/13917>`__
  `#13916 <https://github.com/mixxxdj/mixxx/issues/13916>`__
* Fix waveform EQ High&Mid visualization
  `#13923 <https://github.com/mixxxdj/mixxx/pull/13923>`__
  `#13922 <https://github.com/mixxxdj/mixxx/issues/13922>`__

.. _v2-4-1:

`2.4.1 <https://github.com/mixxxdj/mixxx/milestone/41?closed=1>`__ (2024-05-08)
----------------------------------------------------------------------------------

Controller Mappings
^^^^^^^^^^^^^^^^^^^


* Behringer DDM4000 & BCR2000: Fix exception in JS code `#12969 <https://github.com/mixxxdj/mixxx/pull/12969>`__
* Denon DJ MC6000MK2: Fix mapping of filter knob/button `#13166 <https://github.com/mixxxdj/mixxx/pull/13166>`__
* Denon DJ MC7000: Fix redundant argument and migrate to ``hotcue_x_status``
  `#13113 <https://github.com/mixxxdj/mixxx/pull/13113>`__
  `#13121 <https://github.com/mixxxdj/mixxx/pull/13121>`__
* Hercules Inpulse 200: Configure shift-browser knob to scroll the library (quick) `#12932 <https://github.com/mixxxdj/mixxx/pull/12932>`__
* Nintendo Wii Remote: Fix hid script regarding addOutput `#12973 <https://github.com/mixxxdj/mixxx/pull/12973>`__
* Pioneer CDJ: Fix hid script regarding addOutput `#12973 <https://github.com/mixxxdj/mixxx/pull/12973>`__
* Pioneer DDJ-FLX4: Add waveform zoom and other mapping improvements
  `#12896 <https://github.com/mixxxdj/mixxx/pull/12896>`__
  `#12842 <https://github.com/mixxxdj/mixxx/pull/12842>`__
* Traktor Kontrol F1: Fixes for hid-parser and related script `#12876 <https://github.com/mixxxdj/mixxx/pull/12876>`__
* Traktor S2 Mk1: fix warnings `#13145 <https://github.com/mixxxdj/mixxx/pull/13145>`__
* Traktor S3: Fix mapping crash on macOS `#12840 <https://github.com/mixxxdj/mixxx/pull/12840>`__
* Controller I/O table: sort action column by display string `#13039 <https://github.com/mixxxdj/mixxx/pull/13039>`__

Target Support
^^^^^^^^^^^^^^


* Fix various minor build issues
  `#12853 <https://github.com/mixxxdj/mixxx/pull/12853>`__
  `#12847 <https://github.com/mixxxdj/mixxx/pull/12847>`__
  `#12822 <https://github.com/mixxxdj/mixxx/pull/12822>`__
  `#12892 <https://github.com/mixxxdj/mixxx/pull/12892>`__
  `#13079 <https://github.com/mixxxdj/mixxx/pull/13079>`__
  `#12989 <https://github.com/mixxxdj/mixxx/pull/12989>`__
* CMakeLists: Always prefer OpenGL framework on macOS
  `#13080 <https://github.com/mixxxdj/mixxx/pull/13080>`__
* Use capitalized Mixxx in Windows installer and start menu
  `#13178 <https://github.com/mixxxdj/mixxx/pull/13178>`__

Skins
^^^^^


* Deere: make sampler rows persist `#12928 <https://github.com/mixxxdj/mixxx/pull/12928>`__
* Tango: Remove unneeded waveform Singleton `#12938 <https://github.com/mixxxdj/mixxx/pull/12938>`__
* Tango 64: fix Main VU meter
* Prevent possible crash in customs skins using parallel waveforms
  `#13043 <https://github.com/mixxxdj/mixxx/pull/13043>`__
  `#12580 <https://github.com/mixxxdj/mixxx/issues/12580>`__
  `#13136 <https://github.com/mixxxdj/mixxx/pull/13136>`__
* Slider tooltip: consider orientation for up/down shortcut tooltips + add support for WKnobComposed `#13088 <https://github.com/mixxxdj/mixxx/pull/13088>`__
* Tooltips: update 'hotcue' with saved loop features `#12875 <https://github.com/mixxxdj/mixxx/pull/12875>`__
* Animate long press latching of sync button
  `#12990 <https://github.com/mixxxdj/mixxx/pull/12990>`__
  `#13212 <https://github.com/mixxxdj/mixxx/pull/13212>`__
* Polish fx chain controls `#12805 <https://github.com/mixxxdj/mixxx/pull/12805>`__
* Waveforms: draw loop gradient at the correct position
  `#13061 <https://github.com/mixxxdj/mixxx/pull/13061>`__
  `#13060 <https://github.com/mixxxdj/mixxx/issues/13060>`__
* Waveform / spinnies: don't take keyboard focus on click
  `#13174 <https://github.com/mixxxdj/mixxx/pull/13174>`__
  `#13211 <https://github.com/mixxxdj/mixxx/pull/13211>`__

Library
^^^^^^^


* Sidebar: show track count and duration of History playlists
  `#12811 <https://github.com/mixxxdj/mixxx/pull/12811>`__
  `#13020 <https://github.com/mixxxdj/mixxx/pull/13020>`__
  `#13019 <https://github.com/mixxxdj/mixxx/issues/13019>`__
  `#12788 <https://github.com/mixxxdj/mixxx/issues/12788>`__
  `#12880 <https://github.com/mixxxdj/mixxx/issues/12880>`__
  `#12882 <https://github.com/mixxxdj/mixxx/pull/12882>`__
* Computer feature: update removable devices on Linux `#12893 <https://github.com/mixxxdj/mixxx/pull/12893>`__ `#12891 <https://github.com/mixxxdj/mixxx/issues/12891>`__
* Playlists: Prevent removing tracks from locked playlists `#12927 <https://github.com/mixxxdj/mixxx/pull/12927>`__
* History feature: Fix removing deleted tracks after export
  `#13016 <https://github.com/mixxxdj/mixxx/pull/13016>`__
  `#13000 <https://github.com/mixxxdj/mixxx/issues/13000>`__
* BPM display uses decimal separator of selected locale `#13067 <https://github.com/mixxxdj/mixxx/pull/13067>`__ `#13051 <https://github.com/mixxxdj/mixxx/issues/13051>`__
* Fix relink directory when migrate between Linux/macOS and Windows `#12878 <https://github.com/mixxxdj/mixxx/pull/12878>`__
* Allow adding new directories while watched directories are missing
  `#12937 <https://github.com/mixxxdj/mixxx/pull/12937>`__
  `#10481 <https://github.com/mixxxdj/mixxx/issues/10481>`__
* Require a minimum movement before initiating the drag&drop of tracks
  `#13135 <https://github.com/mixxxdj/mixxx/pull/13135>`__
  `#12902 <https://github.com/mixxxdj/mixxx/issues/12902>`__
  `#12979 <https://github.com/mixxxdj/mixxx/pull/12979>`__
* iTunes/Serato/Traktor/Rhythmbox: Print error if library file could not be opened
  `#13012 <https://github.com/mixxxdj/mixxx/pull/13012>`__
* Playlists: improve table update after deleting (purging) track files
  `#13127 <https://github.com/mixxxdj/mixxx/pull/13127>`__
* Fix Color column width issue `#12852 <https://github.com/mixxxdj/mixxx/pull/12852>`__
* Tracks: select track row when clicking the preview button (only when starting preview)
  `#12791 <https://github.com/mixxxdj/mixxx/pull/12791>`__
* Library track menu: show Hide action also in Playlist & Crates `#11901 <https://github.com/mixxxdj/mixxx/pull/11901>`__
* iTunes: Obtain FileAccess before accessing iTunes XML `#13013 <https://github.com/mixxxdj/mixxx/pull/13013>`__

Miscellaneous
^^^^^^^^^^^^^


* Remove unnecessary unpolish operation of the style, before polish the new style `#12445 <https://github.com/mixxxdj/mixxx/pull/12445>`__
* Developer Tools: Initially sort controls by group name, ascending `#12884 <https://github.com/mixxxdj/mixxx/pull/12884>`__
* Waveforms: Fix scratching crossing loop boundaries `#13007 <https://github.com/mixxxdj/mixxx/pull/13007>`__
* Prohibit un-replace when deck is playing `#13023 <https://github.com/mixxxdj/mixxx/pull/13023>`__ `#12906 <https://github.com/mixxxdj/mixxx/issues/12906>`__
* Track Properties dialog: Prevent wiping metadata when applying twice quickly
  `#12965 <https://github.com/mixxxdj/mixxx/pull/12965>`__
  `#12963 <https://github.com/mixxxdj/mixxx/issues/12963>`__
* AutoDJ: Fix button state after error message about playing deck 3/4
  `#12976 <https://github.com/mixxxdj/mixxx/pull/12976>`__
  `#12975 <https://github.com/mixxxdj/mixxx/issues/12975>`__
* Tagfetcher: Cache fetched covers
  `#12301 <https://github.com/mixxxdj/mixxx/pull/12301>`__
  `#11084 <https://github.com/mixxxdj/mixxx/issues/11084>`__
* Avoid beats iterator being one off and DEBUG_ASSERT in Beats::iteratorFrom
  `#13150 <https://github.com/mixxxdj/mixxx/pull/13150>`__
  `#13149 <https://github.com/mixxxdj/mixxx/issues/13149>`__
* Show hint if resource path in CMakeCache.txt does not exist
  `#12929 <https://github.com/mixxxdj/mixxx/pull/12929>`__
* Always calculate the auto value for colorful console output `#13153 <https://github.com/mixxxdj/mixxx/pull/13153>`__
* Fix FLAC recording on macOS and Windows
  `#10880 <https://github.com/mixxxdj/mixxx/issues/10880>`__
  `#13154 <https://github.com/mixxxdj/mixxx/pull/13154>`__
* LV Mix EQ: Fix pops when enabling in effect rack
  `#13055 <https://github.com/mixxxdj/mixxx/issues/13055>`__
  `#13073 <https://github.com/mixxxdj/mixxx/pull/13073>`__
* Fix hid addOutput

.. _v2-4-0:

`2.4.0 <https://github.com/mixxxdj/mixxx/milestone/15?closed=1>`__ (2024-02-16)
----------------------------------------------------------------------------------

Music Library: Tracks Table & Track Menu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* Remember track selection when switching library features, fix initial selection etc.
  `#4177 <https://github.com/mixxxdj/mixxx/pull/4177>`__
  `#4536 <https://github.com/mixxxdj/mixxx/pull/4536>`__
  `#12321 <https://github.com/mixxxdj/mixxx/pull/12321>`__
  `#12064 <https://github.com/mixxxdj/mixxx/issues/12064>`__
  `#11196 <https://github.com/mixxxdj/mixxx/pull/11196>`__
  `#11130 <https://github.com/mixxxdj/mixxx/pull/11130>`__
* Add new library column that shows the last time a track was played
  `#3140 <https://github.com/mixxxdj/mixxx/pull/3140>`__
  `#3457 <https://github.com/mixxxdj/mixxx/pull/3457>`__
  `#3494 <https://github.com/mixxxdj/mixxx/pull/3494>`__
  `#3596 <https://github.com/mixxxdj/mixxx/pull/3596>`__
  `#3740 <https://github.com/mixxxdj/mixxx/pull/3740>`__
* Add keyboard shortcut Ctrl+Enter to open track properties `#4347 <https://github.com/mixxxdj/mixxx/pull/4347>`__
* Home/End keys jump to first/last row `#4850 <https://github.com/mixxxdj/mixxx/pull/4850>`__
* Wrap selection around at the bottom/top, only if Shift is not pressed
  `#11090 <https://github.com/mixxxdj/mixxx/pull/11090>`__
  `#11100 <https://github.com/mixxxdj/mixxx/pull/11100>`__
  `#12391 <https://github.com/mixxxdj/mixxx/pull/12391>`__
* Allow to hide/remove tracks from the library by pressing the Delete key
  `#4330 <https://github.com/mixxxdj/mixxx/pull/4330>`__
  `#7176 <https://github.com/mixxxdj/mixxx/issues/7176>`__
  `#9793 <https://github.com/mixxxdj/mixxx/issues/9793>`__
  `#9837 <https://github.com/mixxxdj/mixxx/issues/9837>`__
  `#10537 <https://github.com/mixxxdj/mixxx/issues/10537>`__
  `#11239 <https://github.com/mixxxdj/mixxx/pull/11239>`__
  `#4577 <https://github.com/mixxxdj/mixxx/pull/4577>`__
  `#10577 <https://github.com/mixxxdj/mixxx/issues/10577>`__
  `#11171 <https://github.com/mixxxdj/mixxx/pull/11171>`__
  `#10761 <https://github.com/mixxxdj/mixxx/issues/10761>`__
* Fix Recording table refresh issues `#4648 <https://github.com/mixxxdj/mixxx/pull/4648>`__
* Show time in addition to the date in the timestamp column
  `#4900 <https://github.com/mixxxdj/mixxx/pull/4900>`__
  `#10726 <https://github.com/mixxxdj/mixxx/issues/10726>`__
  `#11020 <https://github.com/mixxxdj/mixxx/pull/11020>`__
* Show only the date in Date Added / Last Played columns. Move the time of day to tooltips `#3945 <https://github.com/mixxxdj/mixxx/pull/3945>`__
* Right-align BPM, duration & bitrate values `#11634 <https://github.com/mixxxdj/mixxx/pull/11634>`__ `#11668 <https://github.com/mixxxdj/mixxx/pull/11668>`__ `#11657 <https://github.com/mixxxdj/mixxx/issues/11657>`__
* Remove parenthesis from play counter display `#11357 <https://github.com/mixxxdj/mixxx/pull/11357>`__
* Refocus library, after editing skin controls `#11767 <https://github.com/mixxxdj/mixxx/pull/11767>`__
* Fix performance with large playlists `#11851 <https://github.com/mixxxdj/mixxx/pull/11851>`__ `#11724 <https://github.com/mixxxdj/mixxx/issues/11724>`__
* Add multi-line editor delegate for comment column `#11752 <https://github.com/mixxxdj/mixxx/pull/11752>`__
* Keep current item visible when the view shrinks vertically `#11273 <https://github.com/mixxxdj/mixxx/pull/11273>`__
* macOS scrollbar: Make sure last track is shown in library `#11669 <https://github.com/mixxxdj/mixxx/pull/11669>`__ `#9495 <https://github.com/mixxxdj/mixxx/issues/9495>`__
* Add action to select loaded track in library `#4740 <https://github.com/mixxxdj/mixxx/pull/4740>`__
* Add menu for Analyze and Reanalyze
  `#4806 <https://github.com/mixxxdj/mixxx/pull/4806>`__
  `#11873 <https://github.com/mixxxdj/mixxx/pull/11873>`__
  `#11872 <https://github.com/mixxxdj/mixxx/issues/11872>`__
* Add support for overriding analysis settings about variable/constant BPM on a per-track basis `#10931 <https://github.com/mixxxdj/mixxx/pull/10931>`__
* Add menu for looking up track metadata at Discogs, SoundCloud and LastFM `#4772 <https://github.com/mixxxdj/mixxx/pull/4772>`__ `#4836 <https://github.com/mixxxdj/mixxx/pull/4836>`__
* Add "Delete Track Files" action, does "Move to Trash" with Qt >= 5.15
  `#4560 <https://github.com/mixxxdj/mixxx/pull/4560>`__
  `#4831 <https://github.com/mixxxdj/mixxx/pull/4831>`__
  `#10763 <https://github.com/mixxxdj/mixxx/issues/10763>`__
  `#11580 <https://github.com/mixxxdj/mixxx/pull/11580>`__
  `#11577 <https://github.com/mixxxdj/mixxx/issues/11577>`__
  `#11583 <https://github.com/mixxxdj/mixxx/pull/11583>`__
  `#3212 <https://github.com/mixxxdj/mixxx/pull/3212>`__
  `#11842 <https://github.com/mixxxdj/mixxx/pull/11842>`__
* Allow to clear the comment field
  `#4722 <https://github.com/mixxxdj/mixxx/pull/4722>`__
  `#10615 <https://github.com/mixxxdj/mixxx/issues/10615>`__
* Allow to reset loops and also via "[ChannelN], loop_remove" control object
  `#4802 <https://github.com/mixxxdj/mixxx/pull/4802>`__
  `#10748 <https://github.com/mixxxdj/mixxx/issues/10748>`__
  `#12392 <https://github.com/mixxxdj/mixxx/pull/12392>`__
  `#12521 <https://github.com/mixxxdj/mixxx/pull/12521>`__
* Add 'Update ReplayGain' decks' to track menus `#4031 <https://github.com/mixxxdj/mixxx/pull/4031>`__ `#4719 <https://github.com/mixxxdj/mixxx/pull/4719>`__
* Restore "Remove from playlist" in History `#11591 <https://github.com/mixxxdj/mixxx/pull/11591>`__ `#10974 <https://github.com/mixxxdj/mixxx/issues/10974>`__
* Enable Lock BPM action if any selected track BPM is unlocked `#12385 <https://github.com/mixxxdj/mixxx/pull/12385>`__
* Order BPM action by factor, show peview (for single track) `#12701 <https://github.com/mixxxdj/mixxx/pull/12701>`__ `#10128 <https://github.com/mixxxdj/mixxx/issues/10128>`__
* Provide the same features in all deck track menus `#12214 <https://github.com/mixxxdj/mixxx/pull/12214>`__
* Track table header: Keep menu open after toggling a checkbox `#12218 <https://github.com/mixxxdj/mixxx/pull/12218>`__

Music Library: Sidebar & Searchbar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* Add F2 and Del/Backspace shortcuts for renaming & deleting playlists and crates
  `#11172 <https://github.com/mixxxdj/mixxx/pull/11172>`__
  `#11235 <https://github.com/mixxxdj/mixxx/pull/11235>`__
  `#4697 <https://github.com/mixxxdj/mixxx/pull/4697>`__
  `#4700 <https://github.com/mixxxdj/mixxx/pull/4700>`__
  `#10294 <https://github.com/mixxxdj/mixxx/issues/10294>`__
* Improve presentation of the History library tree
  `#2996 <https://github.com/mixxxdj/mixxx/pull/2996>`__
  `#4298 <https://github.com/mixxxdj/mixxx/pull/4298>`__
  `#10533 <https://github.com/mixxxdj/mixxx/issues/10533>`__
* History: Fix sidebar context menu actions
  `#4384 <https://github.com/mixxxdj/mixxx/pull/4384>`__
  `#4297 <https://github.com/mixxxdj/mixxx/pull/4297>`__
  `#10529 <https://github.com/mixxxdj/mixxx/issues/10529>`__
* History: Add cleanup options
  `#4726 <https://github.com/mixxxdj/mixxx/pull/4726>`__
  `#9259 <https://github.com/mixxxdj/mixxx/issues/9259>`__
  `#10714 <https://github.com/mixxxdj/mixxx/issues/10714>`__
* History: Fix update of play count after removing tracks
  `#12258 <https://github.com/mixxxdj/mixxx/pull/12258>`__
  `#12046 <https://github.com/mixxxdj/mixxx/issues/12046>`__
  `#12256 <https://github.com/mixxxdj/mixxx/issues/12256>`__
* Improve UX with right-click and selection after add, rename, delete, duplicate etc.
  `#11208 <https://github.com/mixxxdj/mixxx/pull/11208>`__
  `#4193 <https://github.com/mixxxdj/mixxx/pull/4193>`__
  `#10488 <https://github.com/mixxxdj/mixxx/issues/10488>`__
  `#11574 <https://github.com/mixxxdj/mixxx/pull/11574>`__
  `#11208 <https://github.com/mixxxdj/mixxx/pull/11208>`__
  `#11712 <https://github.com/mixxxdj/mixxx/pull/11712>`__
* Map Left Arrow Key to jump to parent node and activates it
  `#4253 <https://github.com/mixxxdj/mixxx/pull/4253>`__
* Crates: only store or activate sibling crate if it's valid
  `#11770 <https://github.com/mixxxdj/mixxx/pull/11770>`__
  `#11769 <https://github.com/mixxxdj/mixxx/issues/11769>`__
* Add recent searches to a drop down menu of the search box
  `#3171 <https://github.com/mixxxdj/mixxx/pull/3171>`__
  `#3262 <https://github.com/mixxxdj/mixxx/pull/3262>`__
  `#4505 <https://github.com/mixxxdj/mixxx/pull/4505>`__
* Save search queries across restarts
  `#4458 <https://github.com/mixxxdj/mixxx/pull/4458>`__
  `#10517 <https://github.com/mixxxdj/mixxx/issues/10517>`__
  `#10561 <https://github.com/mixxxdj/mixxx/issues/10561>`__
  `#4571 <https://github.com/mixxxdj/mixxx/pull/4571>`__
* Enable search in Browse & Recording views `#11014 <https://github.com/mixxxdj/mixxx/pull/11014>`__ `#11012 <https://github.com/mixxxdj/mixxx/issues/11012>`__ `#4382 <https://github.com/mixxxdj/mixxx/pull/4382>`__
* Update Clear button when search is disabled `#4447 <https://github.com/mixxxdj/mixxx/pull/4447>`__
* Fix reset to default of search timeout in preferences `#4504 <https://github.com/mixxxdj/mixxx/pull/4504>`__ `#10589 <https://github.com/mixxxdj/mixxx/issues/10589>`__
* Ctrl+F in focused search box selects the entire search string `#4515 <https://github.com/mixxxdj/mixxx/pull/4515>`__
* Improve keypress handling, fix glitch in popup, strip whitespaces `#4658 <https://github.com/mixxxdj/mixxx/pull/4658>`__
* Enter jumps to track table if search query was transmitted `#4844 <https://github.com/mixxxdj/mixxx/pull/4844>`__
  Push completion entry to top, to make up/down behave naturally
* Remove ESC shortcut in favour of new ``[Library],focused_widget`` `#4571 <https://github.com/mixxxdj/mixxx/pull/4571>`__
  `#11030 <https://github.com/mixxxdj/mixxx/pull/11030>`__
  `#10975 <https://github.com/mixxxdj/mixxx/issues/10975>`__
* Restore previous search term when switching between playlists and crates
  `#11129 <https://github.com/mixxxdj/mixxx/pull/11129>`__
  `#11015 <https://github.com/mixxxdj/mixxx/issues/11015>`__
  `#11477 <https://github.com/mixxxdj/mixxx/pull/11477>`__
  `#11476 <https://github.com/mixxxdj/mixxx/issues/11476>`__
* Add options to disable auto-completion and history `#10942 <https://github.com/mixxxdj/mixxx/pull/10942>`__ `#10634 <https://github.com/mixxxdj/mixxx/issues/10634>`__
* Require Enter or Right key to search for auto completed strings
  `#11207 <https://github.com/mixxxdj/mixxx/pull/11207>`__
  `#11289 <https://github.com/mixxxdj/mixxx/pull/11289>`__
  `#11287 <https://github.com/mixxxdj/mixxx/issues/11287>`__
* Allow to use := and quotes to find exact matches `#12063 <https://github.com/mixxxdj/mixxx/pull/12063>`__ `#10699 <https://github.com/mixxxdj/mixxx/issues/10699>`__

Music Library: Backend & Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* Add new "[AutoDJ],add_random_track" to make this feature accessible from controllers `#3076 <https://github.com/mixxxdj/mixxx/pull/3076>`__
* Don't store or update metadata of missing tracks in the Mixxx database to prevent inconsistencies with file tags `#3811 <https://github.com/mixxxdj/mixxx/pull/3811>`__
* Update library schema to 37 for synchronizing file modified time with track source on metadata import/export
  `#3978 <https://github.com/mixxxdj/mixxx/pull/3978>`__
  `#4012 <https://github.com/mixxxdj/mixxx/pull/4012>`__
* Track Metadata: Fix synchronization (import/export) of file tags
  `#4628 <https://github.com/mixxxdj/mixxx/pull/4628>`__
  `#4631 <https://github.com/mixxxdj/mixxx/pull/4631>`__
  `#4847 <https://github.com/mixxxdj/mixxx/pull/4847>`__ `#10782 <https://bugs.launchpad.net/bugs/1981106>`__
* Track Metadata: Do not overwrite unchanged multi-valued fields `#12613 <https://github.com/mixxxdj/mixxx/pull/12613>`__ `#12587 <https://github.com/mixxxdj/mixxx/issues/12587>`__
* Optionally reset metadata on reimport if file tags are missing, enabled by "[Library] ResetMissingTagMetadataOnImport 1"). `#4873 <https://github.com/mixxxdj/mixxx/pull/4873>`__
* Logging: Suppress expected and harmless schema migration errors `#4248 <https://github.com/mixxxdj/mixxx/pull/4248>`__
* Fix handling of undefined BPM values
  `#4062 <https://github.com/mixxxdj/mixxx/pull/4062>`__
  `#4063 <https://github.com/mixxxdj/mixxx/pull/4063>`__
  `#4100 <https://github.com/mixxxdj/mixxx/pull/4100>`__
  `#4154 <https://github.com/mixxxdj/mixxx/pull/4154>`__
  `#4165 <https://github.com/mixxxdj/mixxx/pull/4165>`__
  `#4168 <https://github.com/mixxxdj/mixxx/pull/4168>`__
* Automatic analyze and optimize database `#4199 <https://github.com/mixxxdj/mixxx/pull/4199>`__
* Re-import and update metadata after files have been modified when loading tracks `#4218 <https://github.com/mixxxdj/mixxx/pull/4218>`__
* Re-enable shortcuts after editing controls
  `#4360 <https://github.com/mixxxdj/mixxx/pull/4360>`__
  `#10184 <https://github.com/mixxxdj/mixxx/issues/10184>`__
  `#10523 <https://github.com/mixxxdj/mixxx/issues/10523>`__
* Allow to remove a track form the disk `#3212 <https://github.com/mixxxdj/mixxx/pull/3212>`__ `#4639 <https://github.com/mixxxdj/mixxx/pull/4639>`__
* Fix accasional resetting of played counter in database `#4578 <https://github.com/mixxxdj/mixxx/pull/4578>`__ `#10617 <https://github.com/mixxxdj/mixxx/issues/10617>`__
* Experimental: Fix writing of undefined MusicBrainz Recording ID `#4694 <https://github.com/mixxxdj/mixxx/pull/4694>`__
* Traktor library: fix importing track key `#4701 <https://github.com/mixxxdj/mixxx/pull/4701>`__
* Fix exporting m3u files with tracks and special characters by using the URL format `#4752 <https://github.com/mixxxdj/mixxx/pull/4752>`__
* Library Scanner: Sort files before adding them `#10919 <https://github.com/mixxxdj/mixxx/pull/10919>`__
* Library Scanner: Fix track relocation query `#12462 <https://github.com/mixxxdj/mixxx/pull/12462>`__
* MenuBar: Add shortcut for rescanning library `#11136 <https://github.com/mixxxdj/mixxx/pull/11136>`__
* Playlists: simplify import function, add whitespace before the # suffix `#12246 <https://github.com/mixxxdj/mixxx/pull/12246>`__
* Destroy PlayerInfo after EngineRecord is stopped to fix a debug assertion `#12341 <https://github.com/mixxxdj/mixxx/pull/12341>`__ `#12242 <https://github.com/mixxxdj/mixxx/issues/12242>`__
* iTunes: Modularize importer and use ``iTunesLibrary`` on macOS for compatibility with ``Music.app``
  `#11353 <https://github.com/mixxxdj/mixxx/pull/11353>`__
  `#11256 <https://github.com/mixxxdj/mixxx/issues/11256>`__
  `#11446 <https://github.com/mixxxdj/mixxx/pull/11446>`__
  `#11444 <https://github.com/mixxxdj/mixxx/pull/11444>`__
  `#11503 <https://github.com/mixxxdj/mixxx/pull/11503>`__
  `#11500 <https://github.com/mixxxdj/mixxx/pull/11500>`__
  `#11509 <https://github.com/mixxxdj/mixxx/pull/11509>`__
* iTunes: Fix sporadic crash during unit tests due to a not initialized reference. `#11666 <https://github.com/mixxxdj/mixxx/pull/11666>`__
* iTunes: Permit duplicate playlist names by identifying playlists by id (rather than name) `#11794 <https://github.com/mixxxdj/mixxx/pull/11794>`__
* iTunes: Re-enable test and add ``composer``\ , ``playCount``\ , ``lastPlayedAt`` and ``dateAdded`` to model `#11948 <https://github.com/mixxxdj/mixxx/pull/11948>`__
* Fix setting the wrong default cue color `#11554 <https://github.com/mixxxdj/mixxx/pull/11554>`__ `#11260 <https://github.com/mixxxdj/mixxx/issues/11260>`__
* Ensure that tracks with an invalid BPM are re-analyzed `#2776 <https://github.com/mixxxdj/mixxx/pull/2776>`__
* Add support for exporting crates, playlists and the library to Engine Prime and Denon standalone controllers
  `#2753 <https://github.com/mixxxdj/mixxx/pull/2753>`__
  `#2932 <https://github.com/mixxxdj/mixxx/pull/2932>`__
  `#3102 <https://github.com/mixxxdj/mixxx/pull/3102>`__
  `#3155 <https://github.com/mixxxdj/mixxx/pull/3155>`__
  `#3621 <https://github.com/mixxxdj/mixxx/pull/3621>`__
  `#3776 <https://github.com/mixxxdj/mixxx/pull/3776>`__
  `#3787 <https://github.com/mixxxdj/mixxx/pull/3787>`__
  `#3797 <https://github.com/mixxxdj/mixxx/pull/3797>`__
  `#3798 <https://github.com/mixxxdj/mixxx/pull/3798>`__
  `#4025 <https://github.com/mixxxdj/mixxx/pull/4025>`__
  `#4087 <https://github.com/mixxxdj/mixxx/pull/4087>`__
  `#4102 <https://github.com/mixxxdj/mixxx/pull/4102>`__
  `#4143 <https://github.com/mixxxdj/mixxx/pull/4143>`__
  `#4463 <https://github.com/mixxxdj/mixxx/pull/4463>`__
  `#11815 <https://github.com/mixxxdj/mixxx/pull/11815>`__
  `#12309 <https://github.com/mixxxdj/mixxx/pull/12309>`__
  `#12005 <https://github.com/mixxxdj/mixxx/pull/12005>`__
  `#11816 <https://github.com/mixxxdj/mixxx/pull/11816>`__
  `#11720 <https://github.com/mixxxdj/mixxx/pull/11720>`__
  `#11834 <https://github.com/mixxxdj/mixxx/pull/11834>`__
  `#12452 <https://github.com/mixxxdj/mixxx/pull/12452>`__
  `#11979 <https://github.com/mixxxdj/mixxx/pull/11979>`__
* Rekordbox: Save all loops and correct AAC timing offset for CoreAudio `#2779 <https://github.com/mixxxdj/mixxx/pull/2779>`__
* Rekordbox: Fix missing playlists due to invalid child ID `#10955 <https://github.com/mixxxdj/mixxx/pull/10955>`__
* Rekordbox: Fix unhandled exception when parsing corrupt PDB files
  `#10452 <https://github.com/mixxxdj/mixxx/issues/10452>`__
  `#4040 <https://github.com/mixxxdj/mixxx/pull/4040>`__
* Improve log messages during schema migration `#2979 <https://github.com/mixxxdj/mixxx/pull/2979>`__
* Search related tracks in collection
  `#3181 <https://github.com/mixxxdj/mixxx/pull/3181>`__
  `#3213 <https://github.com/mixxxdj/mixxx/pull/3213>`__
  `#2796 <https://github.com/mixxxdj/mixxx/pull/2796>`__
  `#4207 <https://github.com/mixxxdj/mixxx/pull/4207>`__

Sync
^^^^


* Add support for setting an explicit leader for sync lock
  `#2768 <https://github.com/mixxxdj/mixxx/pull/2768>`__
  `#3099 <https://github.com/mixxxdj/mixxx/pull/3099>`__
  `#3695 <https://github.com/mixxxdj/mixxx/pull/3695>`__
  `#3734 <https://github.com/mixxxdj/mixxx/pull/3734>`__
  `#3698 <https://github.com/mixxxdj/mixxx/pull/3698>`__
  `#3864 <https://github.com/mixxxdj/mixxx/pull/3864>`__
  `#3867 <https://github.com/mixxxdj/mixxx/pull/3867>`__
  `#3921 <https://github.com/mixxxdj/mixxx/pull/3921>`__
  `#4119 <https://github.com/mixxxdj/mixxx/pull/4119>`__
  `#4135 <https://github.com/mixxxdj/mixxx/pull/4135>`__
  `#4149 <https://github.com/mixxxdj/mixxx/pull/4149>`__
  `#4276 <https://github.com/mixxxdj/mixxx/pull/4276>`__
  `#3944 <https://github.com/mixxxdj/mixxx/pull/3944>`__
  `#11828 <https://github.com/mixxxdj/mixxx/pull/11828>`__
  `#11831 <https://github.com/mixxxdj/mixxx/pull/11831>`__
  `#11829 <https://github.com/mixxxdj/mixxx/issues/11829>`__
  `#12431 <https://github.com/mixxxdj/mixxx/pull/12431>`__
  `#11788 <https://github.com/mixxxdj/mixxx/issues/11788>`__
  `#12234 <https://github.com/mixxxdj/mixxx/pull/12234>`__
  `#12499 <https://github.com/mixxxdj/mixxx/pull/12499>`__
* Fix pitch issue with dynamic tracks and sync while cloning tracks
  `#12515 <https://github.com/mixxxdj/mixxx/pull/12515>`__
* Fix issue with half/double BPM calculation when using sync
  `#3899 <https://github.com/mixxxdj/mixxx/pull/3899>`__
  `#3706 <https://github.com/mixxxdj/mixxx/pull/3706>`__
* Sync Lock: Don't seek phase when disabling sync `#4169 <https://github.com/mixxxdj/mixxx/pull/4169>`__
* Sync Lock: Fix issues with single-playing syncables
  `#4155 <https://github.com/mixxxdj/mixxx/pull/4155>`__
  `#4389 <https://github.com/mixxxdj/mixxx/pull/4389>`__
* Re-sync to leader after scratching `#4005 <https://github.com/mixxxdj/mixxx/pull/4005>`__
* Fix audio artifacts when fading from or to zero `#4363 <https://github.com/mixxxdj/mixxx/pull/4363>`__
* EngineBuffer: Fix assert when new track is loaded during playback with sync `#4682 <https://github.com/mixxxdj/mixxx/pull/4682>`__

Audio Codecs
^^^^^^^^^^^^


* Add support for m4v files `#4088 <https://github.com/mixxxdj/mixxx/pull/4088>`__
* Fix recovering from FAAD2 decoding issues `#2850 <https://github.com/mixxxdj/mixxx/pull/2850>`__
* MP3: Log recoverable errors as info instead of warning `#4365 <https://github.com/mixxxdj/mixxx/pull/4365>`__
* MP3: Garbage detection fix `#12464 <https://github.com/mixxxdj/mixxx/pull/12464>`__
* MP3: Improve decoding precision on Windows `#11911 <https://github.com/mixxxdj/mixxx/pull/11911>`__ `#11888 <https://github.com/mixxxdj/mixxx/issues/11888>`__
* AAC encoder: Fix a memory leak `#4386 <https://github.com/mixxxdj/mixxx/pull/4386>`__ `#4408 <https://github.com/mixxxdj/mixxx/pull/4408>`__
* Improve robustness of file type detection by considering the actual MIME type of the content. `#7970 <https://github.com/mixxxdj/mixxx/issues/7970>`__ `#4356 <https://github.com/mixxxdj/mixxx/pull/4356>`__ `#4357 <https://github.com/mixxxdj/mixxx/pull/4357>`__
* Fix file type detection when file has wrong file extension by determining the MIME type from content
  `#4602 <https://github.com/mixxxdj/mixxx/pull/4602>`__
  `#4600 <https://github.com/mixxxdj/mixxx/pull/4600>`__
  `#4615 <https://github.com/mixxxdj/mixxx/pull/4615>`__
  `#7970 <https://github.com/mixxxdj/mixxx/issues/7970>`__
  `#10624 <https://github.com/mixxxdj/mixxx/issues/10624>`__
  `#4683 <https://github.com/mixxxdj/mixxx/pull/4683>`__
  `#10669 <https://github.com/mixxxdj/mixxx/issues/10669>`__
* Fix type detection of AIFF files `#4364 <https://github.com/mixxxdj/mixxx/pull/4364>`__
* Fix synchronization time stamps of ModPlug files `#4826 <https://github.com/mixxxdj/mixxx/pull/4826>`__ `#10758 <https://github.com/mixxxdj/mixxx/issues/10758>`__
* ID3v2 parsing: Improve log warnings `#4610 <https://github.com/mixxxdj/mixxx/pull/4610>`__
* ID3v2 parsing: Fix inconsistent import of comment field `#11249 <https://github.com/mixxxdj/mixxx/pull/11249>`__
* Enable Modpug and Wavpack Support on macOS  `#11182 <https://github.com/mixxxdj/mixxx/pull/11182>`__ `#11119 <https://github.com/mixxxdj/mixxx/issues/11119>`__
* Fix missing file name in file metadata error message `#11965 <https://github.com/mixxxdj/mixxx/pull/11965>`__ `#11964 <https://github.com/mixxxdj/mixxx/issues/11964>`__
* Verify the "first sound" of as an analysis sanity check
  `#4773 <https://github.com/mixxxdj/mixxx/pull/4773>`__
  `#11887 <https://github.com/mixxxdj/mixxx/pull/11887>`__
  `#11946 <https://github.com/mixxxdj/mixxx/pull/11946>`__
  `#11940 <https://github.com/mixxxdj/mixxx/issues/11940>`__
* Fix zeros in the first m4a chunk on Linux `#11879 <https://github.com/mixxxdj/mixxx/pull/11879>`__
* Fix overlapping buffers when decoding m4a files using ffmpeg `#11760 <https://github.com/mixxxdj/mixxx/pull/11760>`__ `#11545 <https://github.com/mixxxdj/mixxx/issues/11545>`__
* Fix possible crash with opus files with embedded cover arts and require TagLib 1.11 or newer
  `#4251 <https://github.com/mixxxdj/mixxx/pull/4251>`__
  `#4252 <https://github.com/mixxxdj/mixxx/pull/4252>`__ `#10500 <https://github.com/mixxxdj/mixxx/issues/10500>`__

Audio Engine
^^^^^^^^^^^^


* Add support for Saved loops
  `#2194 <https://github.com/mixxxdj/mixxx/pull/2194>`__
  `#3267 <https://github.com/mixxxdj/mixxx/pull/3267>`__
  `#3202 <https://github.com/mixxxdj/mixxx/pull/3202>`__
  `#4265 <https://github.com/mixxxdj/mixxx/pull/4265>`__
  `#7574 <https://github.com/mixxxdj/mixxx/issues/7574>`__
  `#11006 <https://github.com/mixxxdj/mixxx/pull/11006>`__
  `#11003 <https://github.com/mixxxdj/mixxx/issues/11003>`__
  `#12637 <https://github.com/mixxxdj/mixxx/pull/12637>`__
  `#12632 <https://github.com/mixxxdj/mixxx/pull/12632>`__
  `#12623 <https://github.com/mixxxdj/mixxx/pull/12623>`__
  `#12618 <https://github.com/mixxxdj/mixxx/issues/12618>`__
* Fix an issue when pressing multiple cue buttons at the same time `#3382 <https://github.com/mixxxdj/mixxx/pull/3382>`__
* Fix synchronization of main cue point/position
  `#4137 <https://github.com/mixxxdj/mixxx/pull/4137>`__
  `#10478 <https://github.com/mixxxdj/mixxx/issues/10478>`__
  `#4153 <https://github.com/mixxxdj/mixxx/pull/4153>`__
* Adjust ReplayGain: Allow user to update the replaygain value based on a deck pregain value `#4031 <https://github.com/mixxxdj/mixxx/pull/4031>`__
* Add halve/double controls for beatjump size `#4269 <https://github.com/mixxxdj/mixxx/pull/4269>`__
* Implement Un-eject by pressing eject again
  `#4668 <https://github.com/mixxxdj/mixxx/pull/4668>`__
  `#11246 <https://github.com/mixxxdj/mixxx/pull/11246>`__
* Implement Un-replace by double-clicking eject
  `#11246 <https://github.com/mixxxdj/mixxx/pull/11246>`__
* Allow to cancel active loops via beatloop_activate `#4328 <https://github.com/mixxxdj/mixxx/pull/4328>`__ `#9950 <https://github.com/mixxxdj/mixxx/issues/9950>`__
* Slip Mode: Preserve active (regular) loop when leaving Slip Mode `#11435 <https://github.com/mixxxdj/mixxx/pull/11435>`__ `#6993 <https://github.com/mixxxdj/mixxx/issues/6993>`__
* Fix possible segfault when ejecting track `#4362 <https://github.com/mixxxdj/mixxx/pull/4362>`__ `#10497 <https://github.com/mixxxdj/mixxx/issues/10497>`__
* Fix possible crash when ejecting track from a controller `#11884 <https://github.com/mixxxdj/mixxx/pull/11884>`__ `#11819 <https://github.com/mixxxdj/mixxx/issues/11819>`__
* Fix an assertion when loop is before track start `#4383 <https://github.com/mixxxdj/mixxx/pull/4383>`__ `#10556 <https://github.com/mixxxdj/mixxx/issues/10556>`__
* Fix and improve snapping to beats in various situations `#4366 <https://github.com/mixxxdj/mixxx/pull/4366>`__ `#10541 <https://github.com/mixxxdj/mixxx/issues/10541>`__
* Don't wipe inapplicable sound config immediately `#4544 <https://github.com/mixxxdj/mixxx/pull/4544>`__
* Rubberband: Support Version 3 "finer" (near-hi-fi quality) setting, on Windows and MacOs and when available on Linux
  `#4853 <https://github.com/mixxxdj/mixxx/pull/4853>`__
  `#4855 <https://github.com/mixxxdj/mixxx/pull/4855>`__
  `#11047 <https://github.com/mixxxdj/mixxx/pull/11047>`__
* Rubberband: Add missing padding, preventing it from eating the initial transient `#11120 <https://github.com/mixxxdj/mixxx/pull/11120>`__
* Rubberband: Improve mono-compatibility for R3 "finer" `#11418 <https://github.com/mixxxdj/mixxx/pull/11418>`__
* Fix a possible crash when ejecting a track `#11334 <https://github.com/mixxxdj/mixxx/pull/11334>`__ `#11257 <https://github.com/mixxxdj/mixxx/issues/11257>`__
* Add a range limits for beatjump_size of 512 `#11248 <https://github.com/mixxxdj/mixxx/pull/11248>`__ `#11203 <https://github.com/mixxxdj/mixxx/issues/11203>`__
* Auto DJ: Fix sharp cut transition after cueing a track without a defined intro `#11629 <https://github.com/mixxxdj/mixxx/pull/11629>`__ `#11621 <https://github.com/mixxxdj/mixxx/issues/11621>`__
* Auto DJ: Don't use removed Intro end and outro start makers, use transition time instead `#11830 <https://github.com/mixxxdj/mixxx/pull/11830>`__
* Auto DJ: Fix GUI freeze when updating duration for many selected tracks
  `#12530 <https://github.com/mixxxdj/mixxx/pull/12530>`__
  `#12520 <https://github.com/mixxxdj/mixxx/issues/12520>`__
  `#12537 <https://github.com/mixxxdj/mixxx/pull/12537>`__
* KeyControl: fix keylock/unlock bugs, reset pitch_adjust `4710 <https://github.com/mixxxdj/mixxx/pull/4710>`__
* Looping: fix asserts for loop move `#11735 <https://github.com/mixxxdj/mixxx/pull/11735>`__
* Looping: reset loop_end_pos on eject `#12224 <https://github.com/mixxxdj/mixxx/pull/12224>`__ `#12223 <https://github.com/mixxxdj/mixxx/issues/12223>`__
* Fix Loop_out not seeking back `#12739 <https://github.com/mixxxdj/mixxx/pull/12739>`__ `#12742 <https://github.com/mixxxdj/mixxx/pull/12742>`__
* ReadAheadManager: fix loop wraparound reader condition `#11717 <https://github.com/mixxxdj/mixxx/pull/11717>`__
* Slip mode: consider loop for background position only if it was enabled  before slip `#11848 <https://github.com/mixxxdj/mixxx/pull/11848>`__ `#11844 <https://github.com/mixxxdj/mixxx/issues/11844>`__
* Make decks' xfader assignment persistent `#12074 <https://github.com/mixxxdj/mixxx/pull/12074>`__ `#10122 <https://github.com/mixxxdj/mixxx/issues/10122>`__
* Fix gain issue with cloned tracks `#12435 <https://github.com/mixxxdj/mixxx/pull/12435>`__ `#10550 <https://github.com/mixxxdj/mixxx/issues/10550>`__

Controller Mappings
^^^^^^^^^^^^^^^^^^^


* new: Hercules DJControl MIX controller mapping `#11279 <https://github.com/mixxxdj/mixxx/pull/11279>`__
* new: Pioneer DDJ-FLX4 controller mapping based on DDJ-400 `#11245 <https://github.com/mixxxdj/mixxx/pull/11245>`__
* new: Traktor Kontrol S4 Mk3 controller mapping `#11284 <https://github.com/mixxxdj/mixxx/pull/11284>`__
* new: Traktor Kontrol Z1 HID controller mapping `#12366 <https://github.com/mixxxdj/mixxx/pull/12366>`__ `#12426 <https://github.com/mixxxdj/mixxx/pull/12426>`__
* new: Yaeltex MiniMixxx controller mapping `#4350 <https://github.com/mixxxdj/mixxx/pull/4350>`__
* Behringer DDM4000 mixer: Update controller mapping `#4262 <https://github.com/mixxxdj/mixxx/pull/4262>`__ `#4799 <https://github.com/mixxxdj/mixxx/pull/4799>`__
* Hercules DJ Console RMX: Replace not defined CO name pitch_reset by pitch_set_default `#12441 <https://github.com/mixxxdj/mixxx/pull/12441>`__
* Korg nanoKONTROL2: Don't try to configure more than 4 main decks `#12322 <https://github.com/mixxxdj/mixxx/pull/12322>`__ `#12317 <https://github.com/mixxxdj/mixxx/issues/12317>`__
* Korg nanoKONTROL2: Removed along with Mixco scripts `#2682 <https://github.com/mixxxdj/mixxx/pull/2682>`__
* MAudio Xponent: Removed along with Mixco scripts `#2682 <https://github.com/mixxxdj/mixxx/pull/2682>`__
* MIDI4lights: Give beginTimer callbacks the anonymous function expression form `#12048 <https://github.com/mixxxdj/mixxx/pull/12048>`__
* Novation Twitch: Removed along with Mixco scripts `#2682 <https://github.com/mixxxdj/mixxx/pull/2682>`__
* Novation Launchpad: Update controller scripts `#2600 <https://github.com/mixxxdj/mixxx/pull/2600>`__ `#11914 <https://github.com/mixxxdj/mixxx/pull/11914>`__
* Numark DJ2GO2 Touch: Fix sampler, hotcue, beatloop buttons `#4287 <https://github.com/mixxxdj/mixxx/pull/4287>`__ `#11595 <https://github.com/mixxxdj/mixxx/pull/11595>`__
* Numark MixTrack Pro 3: Fix beginTimer callback syntax `#12401 <https://github.com/mixxxdj/mixxx/pull/12401>`__ `#12369 <https://github.com/mixxxdj/mixxx/issues/12369>`__
* Roland DJ-505: Make blinking lights blink in sync and other improvements `#4159 <https://github.com/mixxxdj/mixxx/pull/4159>`__ `#4517 <https://github.com/mixxxdj/mixxx/pull/4517>`__
* Traktor Kontrol S2 MK1: Add calibration and refactor `#11237 <https://github.com/mixxxdj/mixxx/pull/11237>`__
* Traktor Kontrol S2 MK2 fix loaded chain preset CO `#11823 <https://github.com/mixxxdj/mixxx/pull/11823>`__ `#10667 <https://github.com/mixxxdj/mixxx/issues/10667>`__
* Traktor Kontrol S2 MK3: Use FX select buttons to set quick effect presets
  `#11702 <https://github.com/mixxxdj/mixxx/pull/11702>`__
* Traktor Kontrol S3: script improvements, vanilla-like FX behavior, control initialization, better scratching, and more
  `#11199 <https://github.com/mixxxdj/mixxx/pull/11199>`__
  `#10645 <https://github.com/mixxxdj/mixxx/issues/10645>`__
  `#12409 <https://github.com/mixxxdj/mixxx/pull/12409>`__
  `#12510 <https://github.com/mixxxdj/mixxx/pull/12510>`__
* Various mappings: Fix ``waveform_zoom`` ranges `#12393 <https://github.com/mixxxdj/mixxx/pull/12393>`__
* Various mappings: Ensure required samplers are created `#12769 <https://github.com/mixxxdj/mixxx/pull/12769>`__

Controller Backend
^^^^^^^^^^^^^^^^^^


* Never raise a fatal error if a controller mapping tries access a non-existent control object `#2947 <https://github.com/mixxxdj/mixxx/pull/2947>`__
* Add support to access HID FeatureReports
  `#11326 <https://github.com/mixxxdj/mixxx/pull/11326>`__
  `#10828 <https://github.com/mixxxdj/mixxx/issues/10828>`__
  `#11664 <https://github.com/mixxxdj/mixxx/pull/11664>`__
* Add function to request HID InputReports, to determine controller state at startup `#3317 <https://github.com/mixxxdj/mixxx/pull/3317>`__
* Exclude HID device: ELAN touch screen `#11324 <https://github.com/mixxxdj/mixxx/pull/11324>`__ `#11323 <https://github.com/mixxxdj/mixxx/issues/11323>`__
* Show otherwise hidden HID devices in developer mode  `#11317 <https://github.com/mixxxdj/mixxx/pull/11317>`__
* Use hidapi's hidraw backend instead of libusb on Linux `#4054 <https://github.com/mixxxdj/mixxx/pull/4054>`__
* Fix broken HID controller mappings Traktor Kontrol S2 MK3 and others `#11470 <https://github.com/mixxxdj/mixxx/pull/11470>`__ `#11461 <https://github.com/mixxxdj/mixxx/issues/11461>`__
* HID mappings: Modernize and document common-hid-packet-parser.js `#4718 <https://github.com/mixxxdj/mixxx/pull/4718>`__ `#4894 <https://github.com/mixxxdj/mixxx/pull/4894>`__
* HID mappings: Small fixes for common-hid-packet-parser.js `#11925 <https://github.com/mixxxdj/mixxx/pull/11925>`__
* HID mappings: Add [Main] to the list of valid groups `#12102 <https://github.com/mixxxdj/mixxx/pull/12102>`__ `#12406 <https://github.com/mixxxdj/mixxx/pull/12406>`__
* Consistently use "mapping" instead of "preset" to refer to controller mappings `#3472 <https://github.com/mixxxdj/mixxx/pull/3472>`__
* Introduce new control object ``[Library],show_track_menu`` to open/close the track menu `#4465 <https://github.com/mixxxdj/mixxx/pull/4465>`__
* Introduce new control object ``[Library],sort_focused_column`` `#4749 <https://github.com/mixxxdj/mixxx/pull/4749>`__ `#4763 <https://github.com/mixxxdj/mixxx/pull/4763>`__ `#10719 <https://github.com/mixxxdj/mixxx/issues/10719>`__
* Introduce new control objects ``[Master],indicator_250millis`` and ``[Master],indicator_500millis`` `#4157 <https://github.com/mixxxdj/mixxx/pull/4157>`__
* Introduce new control object ``[Library],clear_search`` `#4331 <https://github.com/mixxxdj/mixxx/pull/4331>`__
* Introduce new control object ``[Library],focused_widget`` to focus library directly `#4369 <https://github.com/mixxxdj/mixxx/pull/4369>`__ `#4490 <https://github.com/mixxxdj/mixxx/pull/4490>`__
* Introduce new control object ``LoadTrackFromDeck`` and ``LoadTrackFromSampler`` `#11244 <https://github.com/mixxxdj/mixxx/pull/11244>`__
* Don't automatically enable controller if it was disabled before `#4244 <https://github.com/mixxxdj/mixxx/pull/4244>`__ `#10503 <https://github.com/mixxxdj/mixxx/issues/10503>`__
* Enable Qt logging categories for controller logging `#4523 <https://github.com/mixxxdj/mixxx/pull/4523>`__
* Fix segfault during Mixxx shutdown due to a stale controller connection `#4476 <https://github.com/mixxxdj/mixxx/pull/4476>`__ `#10553 <https://github.com/mixxxdj/mixxx/issues/10553>`__
* Components JS: Fix syncbutton `#4329 <https://github.com/mixxxdj/mixxx/pull/4329>`__
* Components JS: Add script.posMod for euclidean modulo `#11415 <https://github.com/mixxxdj/mixxx/pull/11415>`__
* Components JS: make JogWheelBasic correctly switch which deck it controls `#11913 <https://github.com/mixxxdj/mixxx/pull/11913>`__ `#11867 <https://github.com/mixxxdj/mixxx/issues/11867>`__
* Add Trace for the mapping connections, to allow JS profiling `#4766 <https://github.com/mixxxdj/mixxx/pull/4766>`__
* Controller preferences: Allow creating a new mapping with 'No Mapping' selected
  `#4905 <https://github.com/mixxxdj/mixxx/pull/4905>`__
  `#10540 <https://github.com/mixxxdj/mixxx/issues/10540>`__
  `#10539 <https://github.com/mixxxdj/mixxx/issues/10539>`__
* Add TypeScript declarations for engine and controller scripting API to improve IDE code completion during mapping developent `#4759 <https://github.com/mixxxdj/mixxx/pull/4759>`__
* Retire Mixco Scripts `#2682 <https://github.com/mixxxdj/mixxx/pull/2682>`__
* Relax strictness of ``ControllerScriptInterfaceLegacy`` methods.  `#11474 <https://github.com/mixxxdj/mixxx/pull/11474>`__ `#11473 <https://github.com/mixxxdj/mixxx/issues/11473>`__
* Do not show ControlObject aliases in developer tools window `#12265 <https://github.com/mixxxdj/mixxx/pull/12265>`__
* Do not use deprecated COs in C++ code/Keyboard Mapping/Skins `#11990 <https://github.com/mixxxdj/mixxx/pull/11990>`__
* Fix creation of Sampler ``end_of_track`` ControlObjects `#12305 <https://github.com/mixxxdj/mixxx/pull/12305>`__ `#12304 <https://github.com/mixxxdj/mixxx/issues/12304>`__
* Add a test SoftTakeoverTest.CatchOutOfBounds `#12114 <https://github.com/mixxxdj/mixxx/pull/12114>`__ `#12011 <https://github.com/mixxxdj/mixxx/issues/12011>`__
* Make WHotcueButton learnable with the MIDI Wizard `#12252 <https://github.com/mixxxdj/mixxx/pull/12252>`__
* Control picker menu: add ``waveform_zoom_set_default`` `#12247 <https://github.com/mixxxdj/mixxx/pull/12247>`__
* CO Renaming
  `#12022 <https://github.com/mixxxdj/mixxx/pull/12022>`__
  `#12021 <https://github.com/mixxxdj/mixxx/pull/12021>`__
  `#11998 <https://github.com/mixxxdj/mixxx/pull/11998>`__
  `#11996 <https://github.com/mixxxdj/mixxx/pull/11996>`__
  `#11980 <https://github.com/mixxxdj/mixxx/pull/11980>`__
  `#12007 <https://github.com/mixxxdj/mixxx/pull/12007>`__
* Remove deprecated ControlObjects from Skins `#12030 <https://github.com/mixxxdj/mixxx/pull/12030>`__
* Log warning if deprecated control is used `#11972 <https://github.com/mixxxdj/mixxx/pull/11972>`__
* ControlObject alias improvements `#11973 <https://github.com/mixxxdj/mixxx/pull/11973>`__
* Keyboard mapping: Repeat certain control actions if key is held `#12474 <https://github.com/mixxxdj/mixxx/pull/12474>`__
* Keyboard mapping: Return triggers double-click, move Preview functions to P / Shift+P `#12639 <https://github.com/mixxxdj/mixxx/pull/12639>`__
* Keyboard mapping: Various fixes `#12730 <https://github.com/mixxxdj/mixxx/pull/12730>`__
* Update keyboard sheet `#12578 <https://github.com/mixxxdj/mixxx/pull/12578>`__
* Logging: Add support for ``QT_MESSAGE_PATTERN`` environment variable
  `#3204 <https://github.com/mixxxdj/mixxx/pull/3204>`__
  `#3518 <https://github.com/mixxxdj/mixxx/pull/3518>`__
* Avoid issue with ``stars_up/_down`` ControlObjects `#12591 <https://github.com/mixxxdj/mixxx/pull/12591>`__
* hotcue_X_color control: Fix color not stored in cue `#12733 <https://github.com/mixxxdj/mixxx/pull/12733>`__

Skins
^^^^^


* Add harmonic keywheel window
  `#1695 <https://github.com/mixxxdj/mixxx/pull/1695>`__
  `#3622 <https://github.com/mixxxdj/mixxx/pull/3622>`__
  `#3624 <https://github.com/mixxxdj/mixxx/pull/3624>`__
* Allow skin scaling from preferences
  `#3960 <https://github.com/mixxxdj/mixxx/pull/3960>`__
  `#11588 <https://github.com/mixxxdj/mixxx/pull/11588>`__
  `#11586 <https://github.com/mixxxdj/mixxx/issues/11586>`__
* Fix icon rendering on HiDPI/Retina screens `#12407 <https://github.com/mixxxdj/mixxx/pull/12407>`__ `#12361 <https://github.com/mixxxdj/mixxx/issues/12361>`__
* Increase pixmapCache size limit and made it dependent on devicePixelRatio (for HiDPI/Retina displays) `#12416 <https://github.com/mixxxdj/mixxx/pull/12416>`__
* Make beat indicator control behaviour more natural `#3608 <https://github.com/mixxxdj/mixxx/pull/3608>`__
* Fix crash if no skin is available
  `#3918 <https://github.com/mixxxdj/mixxx/pull/3918>`__
  `#3939 <https://github.com/mixxxdj/mixxx/pull/3939>`__
* Fix crash when starting without a valid skin directory `#4575 <https://github.com/mixxxdj/mixxx/pull/4575>`__ `#10461 <https://github.com/mixxxdj/mixxx/issues/10461>`__
* Fix leaked controls `#4213 <https://github.com/mixxxdj/mixxx/pull/4213>`__ `#10293 <https://github.com/mixxxdj/mixxx/issues/10293>`__
* Fix switching from Shade to other skins `#4421 <https://github.com/mixxxdj/mixxx/pull/4421>`__ `#10558 <https://github.com/mixxxdj/mixxx/issues/10558>`__
* Use double click to reset knobs and sliders `#4509 <https://github.com/mixxxdj/mixxx/pull/4509>`__ `#9947 <https://github.com/mixxxdj/mixxx/issues/9947>`__
* Use info not warning for skin COs `#4525 <https://github.com/mixxxdj/mixxx/pull/4525>`__
* Spinny: Allow to toggle cover art at runtime `#4565 <https://github.com/mixxxdj/mixxx/pull/4565>`__ `#10015 <https://github.com/mixxxdj/mixxx/issues/10015>`__
* Passthrough: improve UI / UX `#4794 <https://github.com/mixxxdj/mixxx/pull/4794>`__
* Knob: Hide cursor on wheel event for .8s `#11077 <https://github.com/mixxxdj/mixxx/pull/11077>`__
* Move skin control hack to c++ (spinny/cover controls, mic/ducking controls) `#11183 <https://github.com/mixxxdj/mixxx/pull/11183>`__
* LateNight: Move logo to the right `#4677 <https://github.com/mixxxdj/mixxx/pull/4677>`__
* LateNight: Use correct tooltip for key control toggle `#4696 <https://github.com/mixxxdj/mixxx/pull/4696>`__
* LateNight: Add toggles to show loop and beatjump controls `#4713 <https://github.com/mixxxdj/mixxx/pull/4713>`__
* LateNight: Remove blinking play indicator from mini samplers `#4807 <https://github.com/mixxxdj/mixxx/pull/4807>`__
* LateNight: Add buffer underflow indicator `#4906 <https://github.com/mixxxdj/mixxx/pull/4906>`__ `#10978 <https://github.com/mixxxdj/mixxx/pull/10978>`__
* LateNight: Fix xfader icons in samplers and aux units `#12477 <https://github.com/mixxxdj/mixxx/pull/12477>`__
* LateNight: use default RGB waveform colors `#12712 <https://github.com/mixxxdj/mixxx/pull/12712>`__
* Add LateNight (64 Samplers) `#11715 <https://github.com/mixxxdj/mixxx/pull/11715>`__
* Deere: fix skin/library layout (library missing in default view with Qt6) `#11912 <https://github.com/mixxxdj/mixxx/pull/11912>`__
* Deere: use decks' waveform colors for sliders (Vol + pitch) `#12129 <https://github.com/mixxxdj/mixxx/pull/12129>`__ `#10240 <https://github.com/mixxxdj/mixxx/issues/10240>`__
* Shade: Remove initial setting of now accessible effect controls `#4398 <https://github.com/mixxxdj/mixxx/pull/4398>`__ `#10557 <https://github.com/mixxxdj/mixxx/issues/10557>`__
* Shade: Audio Latency meter fix `#11601 <https://github.com/mixxxdj/mixxx/pull/11601>`__
* Tango: allow to toggle crossfader independently from mixer `#12703 <https://github.com/mixxxdj/mixxx/pull/12703>`__ `#12654 <https://github.com/mixxxdj/mixxx/issues/12654>`__
* Fix outdated tooltips
  `#11387 <https://github.com/mixxxdj/mixxx/pull/11387>`__
  `#11384 <https://github.com/mixxxdj/mixxx/issues/11384>`__
  `#11860 <https://github.com/mixxxdj/mixxx/pull/11860>`__
* Add settings directory link to Help menu `#11670 <https://github.com/mixxxdj/mixxx/pull/11670>`__ `#11667 <https://github.com/mixxxdj/mixxx/issues/11667>`__
* Fix sidebar item styling
  `#11975 <https://github.com/mixxxdj/mixxx/pull/11975>`__
  `#11957 <https://github.com/mixxxdj/mixxx/issues/11957>`__
* Fix 500ms blocking of the whole event loop, when holding mouse down on title bar on Windows `#12359 <https://github.com/mixxxdj/mixxx/pull/12359>`__ `#12358 <https://github.com/mixxxdj/mixxx/issues/12358>`__ `#12433 <https://github.com/mixxxdj/mixxx/pull/12433>`__ `#12458 <https://github.com/mixxxdj/mixxx/pull/12458>`__
* Change SKIN_WARNING to show the skin file and line first, then c++ context `#12253 <https://github.com/mixxxdj/mixxx/pull/12253>`__
* Fix style of selected QComboBox items on Windows `#12339 <https://github.com/mixxxdj/mixxx/pull/12339>`__ `#12323 <https://github.com/mixxxdj/mixxx/issues/12323>`__
* Fix reading the Spinny cover on Windows  `#12103 <https://github.com/mixxxdj/mixxx/pull/12103>`__ `#11131 <https://github.com/mixxxdj/mixxx/issues/11131>`__
* Fix inconsistent/wrong musical keys in the UI `#12051 <https://github.com/mixxxdj/mixxx/pull/12051>`__ `#12044 <https://github.com/mixxxdj/mixxx/issues/12044>`__
* Add ``skins:`` path alias `#12463 <https://github.com/mixxxdj/mixxx/pull/12463>`__
* Remove ``Text``\ , use ``TrackProperty`` or ``Label`` `#12004 <https://github.com/mixxxdj/mixxx/pull/12004>`__
* Beat spinBox/AutoDJ spinbox: Enter & Esc also move focus to library `#4617 <https://github.com/mixxxdj/mixxx/pull/4617>`__ `#4845 <https://github.com/mixxxdj/mixxx/pull/4845>`__
* Add effect chain menu button to Deere, polish in Tango `#12735 <https://github.com/mixxxdj/mixxx/pull/12735>`__
* Skins: reload default.qss when (re)loading a skin `#12219 <https://github.com/mixxxdj/mixxx/pull/12219>`__

Waveforms and GL Widgets
^^^^^^^^^^^^^^^^^^^^^^^^


* Waveform overhaul based on QOpenGlWindow and introduce full GLSL shader based waveforms, vumeters and spinnies. This fixes a couple of performance issues mainly on macOS.
  `#10989 <https://github.com/mixxxdj/mixxx/pull/10989>`__
  `#10416 <https://github.com/mixxxdj/mixxx/issues/10416>`__
  `#11460 <https://github.com/mixxxdj/mixxx/issues/11460>`__
  `#11556 <https://github.com/mixxxdj/mixxx/issues/11556>`__
  `#11450 <https://github.com/mixxxdj/mixxx/issues/11450>`__
  `#10416 <https://github.com/mixxxdj/mixxx/issues/10416>`__
  `#11734 <https://github.com/mixxxdj/mixxx/issues/11734>`__
  `#12466 <https://github.com/mixxxdj/mixxx/pull/12466>`__
  `#12678 <https://github.com/mixxxdj/mixxx/pull/12678>`__
  `#12731 <https://github.com/mixxxdj/mixxx/pull/12731>`__
* Default to 60 Hz waveform refresh rate `#11918 <https://github.com/mixxxdj/mixxx/pull/11918>`__
* Introduce a VSsync mode driven by a phase locked loop `#12469 <https://github.com/mixxxdj/mixxx/pull/12469>`__
* Make VSync mode 0 refer to the default mode and make ST_PLL the default on macOS, ST_TIMER otherwise `#12489 <https://github.com/mixxxdj/mixxx/pull/12489>`__
* Use WaveformWidgetType::AllShaderRGBWaveform as autoChooseWidgetType `#11822 <https://github.com/mixxxdj/mixxx/pull/11822>`__
* Add new "RGB Stacked" waveform `#3153 <https://github.com/mixxxdj/mixxx/pull/3153>`__
* Fix micro jitter from clamping position offset to vsync interval `#12470 <https://github.com/mixxxdj/mixxx/pull/12470>`__
* Avoid flickering when resizing `#12487 <https://github.com/mixxxdj/mixxx/pull/12487>`__
* Invert scroll wheel waveform zoom direction to mach other applications `#4195 <https://github.com/mixxxdj/mixxx/pull/4195>`__
* Waveform scrolling: Use set interval setting to fix performance degradation for AMD graphics adapters `#11681 <https://github.com/mixxxdj/mixxx/pull/11681>`__ `#11617 <https://github.com/mixxxdj/mixxx/issues/11617>`__
* Fix waveform zooming `#11650 <https://github.com/mixxxdj/mixxx/pull/11650>`__ `#11626 <https://github.com/mixxxdj/mixxx/issues/11626>`__
* Fix OpenGL version detection `#11673 <https://github.com/mixxxdj/mixxx/pull/11673>`__
* Fix crash when no GL context is available `#11963 <https://github.com/mixxxdj/mixxx/pull/11963>`__ `#11929 <https://github.com/mixxxdj/mixxx/issues/11929>`__
* Fix stopped waveform rendering in case of vinyl control `#11977 <https://github.com/mixxxdj/mixxx/pull/11977>`__ `#10764 <https://github.com/mixxxdj/mixxx/issues/10764>`__
* Fix visual play position related to looping
  `#11840 <https://github.com/mixxxdj/mixxx/pull/11840>`__
  `#11836 <https://github.com/mixxxdj/mixxx/issues/11836>`__
  `#12538 <https://github.com/mixxxdj/mixxx/pull/12538>`__
  `#12506 <https://github.com/mixxxdj/mixxx/issues/12506>`__
  `#12513 <https://github.com/mixxxdj/mixxx/issues/12513>`__
* Fix for visual position while scratching outside of an activated loop `#12281 <https://github.com/mixxxdj/mixxx/pull/12281>`__ `#12274 <https://github.com/mixxxdj/mixxx/issues/12274>`__
* Spinny: Fix drawing of non-square cover arts `#11971 <https://github.com/mixxxdj/mixxx/pull/11971>`__ `#11967 <https://github.com/mixxxdj/mixxx/issues/11967>`__
* Spinny/VU-Meter: Fix drawing `#12010 <https://github.com/mixxxdj/mixxx/pull/12010>`__ `#11930 <https://github.com/mixxxdj/mixxx/issues/11930>`__
* VU-Meter: Don't use OpenGL by default `#11722 <https://github.com/mixxxdj/mixxx/pull/11722>`__
* Improve GLSL pre-roll triangles `#12100 <https://github.com/mixxxdj/mixxx/pull/12100>`__ `#12015 <https://github.com/mixxxdj/mixxx/issues/12015>`__
* Make scaling of GLSL RGB and RGB L/R waveform amplitudes consistent with simple waveform `#12205 <https://github.com/mixxxdj/mixxx/pull/12205>`__ `#12356 <https://github.com/mixxxdj/mixxx/pull/12356>`__
* Improve rendering of waveform marks `#12203 <https://github.com/mixxxdj/mixxx/pull/12203>`__ `#12237 <https://github.com/mixxxdj/mixxx/pull/12237>`__
* avoid overlapping marks `#12273 <https://github.com/mixxxdj/mixxx/pull/12273>`__
* gradually "compact" the markers if the waveform height is reduced `#12501 <https://github.com/mixxxdj/mixxx/pull/12501>`__
* Fix clamping of the index for drawing the waveform left of zero position `#12411 <https://github.com/mixxxdj/mixxx/pull/12411>`__
* Fix possible crash when closing Mixxx `#12314 <https://github.com/mixxxdj/mixxx/pull/12314>`__ `#11737 <https://github.com/mixxxdj/mixxx/issues/11737>`__
* Fix EGL support
  `#11982 <https://github.com/mixxxdj/mixxx/pull/11982>`__
  `#11641 <https://github.com/mixxxdj/mixxx/issues/11641>`__
  `#11935 <https://github.com/mixxxdj/mixxx/pull/11935>`__
  `#11985 <https://github.com/mixxxdj/mixxx/pull/11985>`__
  `#11982 <https://github.com/mixxxdj/mixxx/pull/11982>`__
  `#11995 <https://github.com/mixxxdj/mixxx/pull/11995>`__
  `#11994 <https://github.com/mixxxdj/mixxx/pull/11994>`__
  `#12607 <https://github.com/mixxxdj/mixxx/pull/12607>`__
* Preferences: recall correct waveform type when selecting an overview type
  `#12231 <https://github.com/mixxxdj/mixxx/pull/12231>`__
  `#12226 <https://github.com/mixxxdj/mixxx/issues/12226>`__

Cover Art
^^^^^^^^^


* Prevent wrong cover art display due to hash conflicts `#2524 <https://github.com/mixxxdj/mixxx/pull/2524>`__ `#4904 <https://github.com/mixxxdj/mixxx/pull/4904>`__
* Add background color for quick cover art preview `#2524 <https://github.com/mixxxdj/mixxx/pull/2524>`__
* Fix coverart tooltip if cover is not cached `#12087 <https://github.com/mixxxdj/mixxx/pull/12087>`__
* Add cover art fetcher to the Musicbrainz dialog
  `#10908 <https://github.com/mixxxdj/mixxx/pull/10908>`__
  `#4871 <https://github.com/mixxxdj/mixxx/pull/4871>`__
  `#10795 <https://github.com/mixxxdj/mixxx/issues/10795>`__
  `#10796 <https://github.com/mixxxdj/mixxx/issues/10796>`__
  `#10902 <https://github.com/mixxxdj/mixxx/pull/10902>`__
  `#4851 <https://github.com/mixxxdj/mixxx/pull/4851>`__
  `#11938 <https://github.com/mixxxdj/mixxx/pull/11938>`__
  `#11086 <https://github.com/mixxxdj/mixxx/issues/11086>`__
  `#12041 <https://github.com/mixxxdj/mixxx/pull/12041>`__
  `#12300 <https://github.com/mixxxdj/mixxx/pull/12300>`__
  `#12543 <https://github.com/mixxxdj/mixxx/pull/12543>`__
  `#12532 <https://github.com/mixxxdj/mixxx/issues/12532>`__
  `#12543 <https://github.com/mixxxdj/mixxx/pull/12543>`__
* CoverArtCache refactoring + Fix scrolling lag after updating Mixxx  `#12009 <https://github.com/mixxxdj/mixxx/pull/12009>`__

Effects
^^^^^^^


* Effect refactoring: Effect chain saving/loading, parameter hiding/rearrangement, effect preferences overhaul
  `#4467 <https://github.com/mixxxdj/mixxx/pull/4467>`__
  `#4431 <https://github.com/mixxxdj/mixxx/pull/4431>`__
  `#4426 <https://github.com/mixxxdj/mixxx/pull/4426>`__
  `#4457 <https://github.com/mixxxdj/mixxx/pull/4457>`__
  `#4456 <https://github.com/mixxxdj/mixxx/pull/4456>`__
  `#4459 <https://github.com/mixxxdj/mixxx/pull/4459>`__
  `#4462 <https://github.com/mixxxdj/mixxx/pull/4462>`__
  `#4466 <https://github.com/mixxxdj/mixxx/pull/4466>`__
  `#4468 <https://github.com/mixxxdj/mixxx/pull/4468>`__
  `#4472 <https://github.com/mixxxdj/mixxx/pull/4472>`__
  `#4470 <https://github.com/mixxxdj/mixxx/pull/4470>`__
  `#4471 <https://github.com/mixxxdj/mixxx/pull/4471>`__
  `#4483 <https://github.com/mixxxdj/mixxx/pull/4483>`__
  `#4482 <https://github.com/mixxxdj/mixxx/pull/4482>`__
  `#4484 <https://github.com/mixxxdj/mixxx/pull/4484>`__
  `#4486 <https://github.com/mixxxdj/mixxx/pull/4486>`__
  `#4502 <https://github.com/mixxxdj/mixxx/pull/4502>`__
  `#4501 <https://github.com/mixxxdj/mixxx/pull/4501>`__
  `#4518 <https://github.com/mixxxdj/mixxx/pull/4518>`__
  `#4532 <https://github.com/mixxxdj/mixxx/pull/4532>`__
  `#4461 <https://github.com/mixxxdj/mixxx/pull/4461>`__
  `#4548 <https://github.com/mixxxdj/mixxx/pull/4548>`__
  `#4503 <https://github.com/mixxxdj/mixxx/pull/4503>`__
  `#4686 <https://github.com/mixxxdj/mixxx/pull/4686>`__
  `#4691 <https://github.com/mixxxdj/mixxx/pull/4691>`__
  `#4704 <https://github.com/mixxxdj/mixxx/pull/4704>`__
  `#4748 <https://github.com/mixxxdj/mixxx/pull/4748>`__
  `#4833 <https://github.com/mixxxdj/mixxx/pull/4833>`__
  `#10762 <https://github.com/mixxxdj/mixxx/issues/10762>`__
  `#4884 <https://github.com/mixxxdj/mixxx/pull/4884>`__
  `#10802 <https://github.com/mixxxdj/mixxx/issues/10802>`__
  `#10801 <https://github.com/mixxxdj/mixxx/issues/10801>`__
  `#4899 <https://github.com/mixxxdj/mixxx/pull/4899>`__
  `#8817 <https://github.com/mixxxdj/mixxx/pull/8817>`__
  `#10868 <https://github.com/mixxxdj/mixxx/pull/10868>`__
  `#11055 <https://github.com/mixxxdj/mixxx/pull/11055>`__
  `#11135 <https://github.com/mixxxdj/mixxx/pull/11135>`__
  `#11185 <https://github.com/mixxxdj/mixxx/pull/11185>`__
  `#11242 <https://github.com/mixxxdj/mixxx/pull/11242>`__
  `#10837 <https://github.com/mixxxdj/mixxx/pull/10837>`__
  `#10834 <https://github.com/mixxxdj/mixxx/issues/10834>`__
  `#11424 <https://github.com/mixxxdj/mixxx/pull/11424>`__
  `#11376 <https://github.com/mixxxdj/mixxx/pull/11376>`__
  `#11456 <https://github.com/mixxxdj/mixxx/pull/11456>`__
  `#11454 <https://github.com/mixxxdj/mixxx/issues/11454>`__
  `#11695 <https://github.com/mixxxdj/mixxx/pull/11695>`__
  `#12633 <https://github.com/mixxxdj/mixxx/pull/12633>`__
  `#12561 <https://github.com/mixxxdj/mixxx/pull/12561>`__
  `#10859 <https://github.com/mixxxdj/mixxx/pull/10859>`__
  `#10777 <https://github.com/mixxxdj/mixxx/issues/10777>`__
  `#11886 <https://github.com/mixxxdj/mixxx/pull/11886>`__
  `#12282 <https://github.com/mixxxdj/mixxx/pull/12282>`__
  `#12277 <https://github.com/mixxxdj/mixxx/issues/12277>`__
  `#11705 <https://github.com/mixxxdj/mixxx/pull/11705>`__
  `#4469 <https://github.com/mixxxdj/mixxx/pull/4469>`__
  `#11902 <https://github.com/mixxxdj/mixxx/pull/11902>`__
  `#10605 <https://github.com/mixxxdj/mixxx/issues/10605>`__
  `#4702 <https://github.com/mixxxdj/mixxx/pull/4702>`__
  `#10579 <https://github.com/mixxxdj/mixxx/issues/10579>`__
  `#4501 <https://github.com/mixxxdj/mixxx/pull/4501>`__
  `#4502 <https://github.com/mixxxdj/mixxx/pull/4502>`__
  `#4503 <https://github.com/mixxxdj/mixxx/pull/4503>`__
  `#4590 <https://github.com/mixxxdj/mixxx/pull/4590>`__
  `#4593 <https://github.com/mixxxdj/mixxx/pull/4593>`__
  `#11062 <https://github.com/mixxxdj/mixxx/pull/11062>`__
* Add Noise effect `#2921 <https://github.com/mixxxdj/mixxx/pull/2921>`__
* Add Pitch Shift effect
  `#4775 <https://github.com/mixxxdj/mixxx/pull/4775>`__
  `#7389 <https://github.com/mixxxdj/mixxx/issues/7389>`__
  `#4810 <https://github.com/mixxxdj/mixxx/pull/4810>`__
  `#4901 <https://github.com/mixxxdj/mixxx/pull/4901>`__
  `#10858 <https://github.com/mixxxdj/mixxx/pull/10858>`__
  `#12481 <https://github.com/mixxxdj/mixxx/pull/12481>`__
* Add Distortion effect `#10932 <https://github.com/mixxxdj/mixxx/pull/10932>`__
* Effect parameter knobs: Briefly show parameter value in parameter name widget
  `#11032 <https://github.com/mixxxdj/mixxx/pull/11032>`__
  `#9022 <https://github.com/mixxxdj/mixxx/issues/9022>`__
  `#11034 <https://github.com/mixxxdj/mixxx/pull/11034>`__
* Effect parameter knobs: Implement ValueScaler::Integral, snap value to int `#11061 <https://github.com/mixxxdj/mixxx/pull/11061>`__
* Show effect parameter units in parameter name label `#11041 <https://github.com/mixxxdj/mixxx/pull/11041>`__ `#11194 <https://github.com/mixxxdj/mixxx/pull/11194>`__
* Fix gain compensation for the Moog filter `#11177 <https://github.com/mixxxdj/mixxx/pull/11177>`__
* Fix memory leak in AutoPan `#11346 <https://github.com/mixxxdj/mixxx/pull/11346>`__
* EngineFilterDelay: clamp wrong delay values `#4869 <https://github.com/mixxxdj/mixxx/pull/4869>`__
* Fix crash when changing effect unit routing `#4707 <https://github.com/mixxxdj/mixxx/pull/4707>`__ `#9331 <https://github.com/mixxxdj/mixxx/issues/9331>`__
* Clear effect buffer after ejecting a track  `#10692 <https://github.com/mixxxdj/mixxx/issues/10692>`__
* Center Super knob when loading empty (QuickEffect) chain preset `#12320 <https://github.com/mixxxdj/mixxx/pull/12320>`__
* Don't reset "super" and "mix" knob on startup `#11781 <https://github.com/mixxxdj/mixxx/pull/11781>`__ `#11773 <https://github.com/mixxxdj/mixxx/issues/11773>`__
* Add a missing early return `#11809 <https://github.com/mixxxdj/mixxx/pull/11809>`__ `#111808 <https://github.com/mixxxdj/mixxx/issues/11808>`__
* Update EffectSlot meta default value according to loaded effect `#12480 <https://github.com/mixxxdj/mixxx/pull/12480>`__ `#12479 <https://github.com/mixxxdj/mixxx/issues/12479>`__

Target Support
^^^^^^^^^^^^^^


* Added support for macOS ARM builds on M1/M2 Apple silicon `#11398 <https://github.com/mixxxdj/mixxx/pull/11398>`__
* Set app_id to fix Mixxx window icon on Wayland `#12635 <https://github.com/mixxxdj/mixxx/pull/12635>`__
* Require C++20 but keep Ubuntu Focal support
  `#4889 <https://github.com/mixxxdj/mixxx/pull/4889>`__
  `#4895 <https://github.com/mixxxdj/mixxx/pull/4895>`__
  `#11204 <https://github.com/mixxxdj/mixxx/pull/11204>`__
  `#4832 <https://github.com/mixxxdj/mixxx/pull/4832>`__
  `#4803 <https://github.com/mixxxdj/mixxx/pull/4803>`__
  `#11551 <https://github.com/mixxxdj/mixxx/issues/11551>`__
  `#11573 <https://github.com/mixxxdj/mixxx/pull/11573>`__
* Drop Ubuntu Bionic support, require Qt 5.12
  `#3687 <https://github.com/mixxxdj/mixxx/pull/3687>`__
  `#3735 <https://github.com/mixxxdj/mixxx/pull/3735>`__
  `#3736 <https://github.com/mixxxdj/mixxx/pull/3736>`__
  `#3985 <https://github.com/mixxxdj/mixxx/pull/3985>`__
* Drop Ubuntu Groovy and Impish support because of EOL
  `#4283 <https://github.com/mixxxdj/mixxx/pull/4283>`__
  `#4849 <https://github.com/mixxxdj/mixxx/pull/4849>`__
  `#12353 <https://github.com/mixxxdj/mixxx/pull/12353>`__
* Support Ubuntu Noble and Jammy
  `#4780 <https://github.com/mixxxdj/mixxx/pull/4780>`__
  `#4857 <https://github.com/mixxxdj/mixxx/pull/4857>`__
  `#12353 <https://github.com/mixxxdj/mixxx/pull/12353>`__
* Add NixOS support
  `#2820 <https://github.com/mixxxdj/mixxx/pull/2820>`__
  `#2828 <https://github.com/mixxxdj/mixxx/pull/2828>`__
  `#2836 <https://github.com/mixxxdj/mixxx/pull/2836>`__
  `#2827 <https://github.com/mixxxdj/mixxx/pull/2827>`__
  `#2827 <https://github.com/mixxxdj/mixxx/pull/2827>`__
  `#2828 <https://github.com/mixxxdj/mixxx/pull/2828>`__
  `#3113 <https://github.com/mixxxdj/mixxx/pull/3113>`__
  `#3089 <https://github.com/mixxxdj/mixxx/pull/3089>`__
  `#3545 <https://github.com/mixxxdj/mixxx/pull/3545>`__
* Windows packaging: Use Azure for signing exe, msi and all dlls with timestamp and sha256
  `#12465 <https://github.com/mixxxdj/mixxx/pull/12465>`__
  `#4824 <https://github.com/mixxxdj/mixxx/pull/4824>`__
  `#4825 <https://github.com/mixxxdj/mixxx/pull/4825>`__
* macOS packaging: Fix signing and migrate script to ``notarytool``
  `#12123 <https://github.com/mixxxdj/mixxx/pull/12123>`__
  `#12089 <https://github.com/mixxxdj/mixxx/issues/12089>`__
  `#12095 <https://github.com/mixxxdj/mixxx/pull/12095>`__
* macOS packaging: Enable app sandbox and fix related issues
  `#12138 <https://github.com/mixxxdj/mixxx/pull/12138>`__
  `#12457 <https://github.com/mixxxdj/mixxx/pull/12457>`__
  `#12137 <https://github.com/mixxxdj/mixxx/issues/12137>`__
  `#11552 <https://github.com/mixxxdj/mixxx/issues/11552>`__
  `#4018 <https://github.com/mixxxdj/mixxx/pull/4018>`__
  `#10373 <https://github.com/mixxxdj/mixxx/issues/10373>`__
* macOS: Use rounded Mixxx Icon to follow Apples style guide
  `#4545 <https://github.com/mixxxdj/mixxx/pull/4545>`__
  `#10958 <https://github.com/mixxxdj/mixxx/pull/10958>`__
* macOS packaging: Capitalize bundle and executable name (Mixxx.app)
  `#12656 <https://github.com/mixxxdj/mixxx/pull/12656>`__
* OpenBSD: Allow building Mixxx `#11083 <https://github.com/mixxxdj/mixxx/pull/11083>`__
* Improve Linux launcher
  `#11826 <https://github.com/mixxxdj/mixxx/pull/11826>`__
  `#11820 <https://github.com/mixxxdj/mixxx/issues/11820>`__
  `#11805 <https://github.com/mixxxdj/mixxx/pull/11805>`__
  `#12424 <https://github.com/mixxxdj/mixxx/pull/12424>`__
* Experimental iOS support
  `#12665 <https://github.com/mixxxdj/mixxx/pull/12665>`__
  `#12666 <https://github.com/mixxxdj/mixxx/pull/12666>`__
  `#12662 <https://github.com/mixxxdj/mixxx/pull/12662>`__
  `#12663 <https://github.com/mixxxdj/mixxx/pull/12663>`__
  `#12661 <https://github.com/mixxxdj/mixxx/pull/12661>`__
  `#12650 <https://github.com/mixxxdj/mixxx/pull/12650>`__
* Fail early in case Taglib 2.0 is found `#12709 <https://github.com/mixxxdj/mixxx/pull/12709>`__

Track properties
^^^^^^^^^^^^^^^^


* Fix a SIGSEGV after a debug assertion `#4316 <https://github.com/mixxxdj/mixxx/pull/4316>`__
* Apply pending changes also when saving via hotkey `#4562 <https://github.com/mixxxdj/mixxx/pull/4562>`__ `#10612 <https://github.com/mixxxdj/mixxx/issues/10612>`__
* Fix crash when trying to scale 0.0 BPM `#4587 <https://github.com/mixxxdj/mixxx/pull/4587>`__ `#1955853 <https://github.com/mixxxdj/mixxx/issues/10625>`__
* Add track color selector `#11436 <https://github.com/mixxxdj/mixxx/pull/11436>`__ `#10324 <https://github.com/mixxxdj/mixxx/issues/10324>`__
* Don't clear unsaved properties when updating star rating `#11565 <https://github.com/mixxxdj/mixxx/pull/11565>`__ `#11540 <https://github.com/mixxxdj/mixxx/issues/11540>`__
* Fix glitch in Star rating `#12582 <https://github.com/mixxxdj/mixxx/pull/12582>`__ `#12576 <https://github.com/mixxxdj/mixxx/issues/12576>`__
* Focus Double-clicked property field for edit
  `#11764 <https://github.com/mixxxdj/mixxx/pull/11764>`__
  `#11804 <https://github.com/mixxxdj/mixxx/pull/11804>`__
  `#11802 <https://github.com/mixxxdj/mixxx/issues/11802>`__
* Display the samplerate `#12418 <https://github.com/mixxxdj/mixxx/pull/12418>`__

Preferences
^^^^^^^^^^^


* Always show tooltips `#4198 <https://github.com/mixxxdj/mixxx/pull/4198>`__ `#9716 <https://github.com/mixxxdj/mixxx/issues/9716>`__
* Add option to keep deck playing on track load `#10944 <https://github.com/mixxxdj/mixxx/pull/10944>`__ `#10548 <https://github.com/mixxxdj/mixxx/issues/10548>`__
* Always enable Alt shortcut keys `#11145 <https://github.com/mixxxdj/mixxx/pull/11145>`__ `#10413 <https://github.com/mixxxdj/mixxx/issues/10413>`__
* Sound Hardware: auto select free device channels `#11859 <https://github.com/mixxxdj/mixxx/pull/11859>`__ `#10163 <https://github.com/mixxxdj/mixxx/issues/10163>`__
* Various layout and UX fixes
  `#12429 <https://github.com/mixxxdj/mixxx/pull/12429>`__
  `#12399 <https://github.com/mixxxdj/mixxx/pull/12399>`__
  `#11663 <https://github.com/mixxxdj/mixxx/pull/11663>`__
  `#11926 <https://github.com/mixxxdj/mixxx/pull/11926>`__
  `#12057 <https://github.com/mixxxdj/mixxx/pull/12057>`__
* macOS: set preferences dialog title to the selected page title `#11696 <https://github.com/mixxxdj/mixxx/pull/11696>`__
* macOS: fix the preferences menu and opening the settings directory `#11679 <https://github.com/mixxxdj/mixxx/pull/11679>`__
* macOS: fix slider styling in preferences dialog `#11647 <https://github.com/mixxxdj/mixxx/pull/11647>`__
* Vinyl control: Improve quality indicator `#3279 <https://github.com/mixxxdj/mixxx/pull/3279>`__
* Mixer: apply & save settings only in slotApply(), fix bugs, improve UX `#11527 <https://github.com/mixxxdj/mixxx/pull/11527>`__
* Mixer: fix reset of EQ auto-reset checkbox `#11818 <https://github.com/mixxxdj/mixxx/pull/11818>`__ `#11817 <https://github.com/mixxxdj/mixxx/issues/11817>`__
* Interface: avoid unneeded skin reload, clean up `#11853 <https://github.com/mixxxdj/mixxx/pull/11853>`__
* Library: Add link to settings files info in the manual `#4367 <https://github.com/mixxxdj/mixxx/pull/4367>`__
* Controllers: add search bars to mapping tables `#11165 <https://github.com/mixxxdj/mixxx/pull/11165>`__
* Add 13 new translation languages `#4785 <https://github.com/mixxxdj/mixxx/pull/4785>`__ `#9702 <https://github.com/mixxxdj/mixxx/issues/9702>`__
* Join Franch translations to "fr" and remove all untranslated English strings.  `#12699 <https://github.com/mixxxdj/mixxx/pull/12699>`__
* Apply changes from all pages when pressing Apply (like when pressing Okay) `#12194 <https://github.com/mixxxdj/mixxx/pull/12194>`__

Known issues
^^^^^^^^^^^^


* Volume / Loudness spikes on Windows with M4A/AAC files.
  Last known working version is Windows 10 build 17763.
  Affected versions are Windows 10 build 19041 and Windows 11 build 22000.
  `#12289 <https://github.com/mixxxdj/mixxx/issues/12289>`__
  `#11094 <https://github.com/mixxxdj/mixxx/issues/11094>`__
* macOS: Library entries are now sorted using the language depending Unicode Collation Algorithm (UCA).
  `#12517 <https://github.com/mixxxdj/mixxx/issues/12517>`__
* macOS: Visual glitches with the main EQ sliders
  `#12517 <https://github.com/mixxxdj/mixxx/issues/12630>`__
* Linux: possible crash when enabling a MIDI controller `#12001 <https://github.com/mixxxdj/mixxx/issues/12001>`__
  Introduce with Qt 5.15.5, fixed in Qt 5.15.17 and Qt 6.6.3
* Extra Samplers are created during startup, when found in a saved Sampler Bank `#12657 <https://github.com/mixxxdj/mixxx/pull/12657>`__ `#12809 <https://github.com/mixxxdj/mixxx/pull/12809>`__

.. _v2-3-6:

`2.3.6 <https://github.com/mixxxdj/mixxx/milestone/40>`__ (2023-08-15)
-------------------------------------------------------------------------


* Fixed possible crash when closing Mixxx while browsing the file system
  `#11593 <https://github.com/mixxxdj/mixxx/pull/11593>`__
  `#11589 <https://github.com/mixxxdj/mixxx/issues/11589>`__
* No longer stop a track with an active loop at the very end
  `#11558 <https://github.com/mixxxdj/mixxx/pull/11558>`__
  `#11557 <https://github.com/mixxxdj/mixxx/issues/11557>`__
* Fixed resyncing when moving an active loop
  `#11152 <https://github.com/mixxxdj/mixxx/pull/11152>`__
  `#11381 <https://github.com/mixxxdj/mixxx/issues/11381>`__
* Allow true gapless playback when repeating full tracks
  `#11532 <https://github.com/mixxxdj/mixxx/pull/11532>`__
  `#9842 <https://github.com/mixxxdj/mixxx/issues/9842>`__
  `#11704 <https://github.com/mixxxdj/mixxx/pull/11704>`__
* Rhythmbox: Fixed bulk track imports from playlists
  `#11661 <https://github.com/mixxxdj/mixxx/pull/11661>`__
* Console log spam reduced
  `#11690 <https://github.com/mixxxdj/mixxx/pull/11690>`__
  `#11691 <https://github.com/mixxxdj/mixxx/issues/11691>`__
* Numark DJ2GO2 Touch: Add missing loop_out mapping for the right deck
  `#11595 <https://github.com/mixxxdj/mixxx/pull/11595>`__
  `#11659 <https://github.com/mixxxdj/mixxx/pull/11659>`__
* Shade: Fixed VU-Meter and other minor issues
  `#11598 <https://github.com/mixxxdj/mixxx/pull/11598>`__
* Fixed a rare crash when disabling quantize form a controller
  `#11744 <https://github.com/mixxxdj/mixxx/pull/11744>`__
  `#11709 <https://github.com/mixxxdj/mixxx/issues/11709>`__
* Controller Preferences: Avoid scrollbars in I/O tabs if Info tab exceeds page height
  `#11756 <https://github.com/mixxxdj/mixxx/pull/11756>`__
* Broadcast: Improved error message in case of timeout
  `#11775 <https://github.com/mixxxdj/mixxx/pull/11775>`__
* Handle setting ``loop_in`` and ``loop_out`` to the same position
  `#11771 <https://github.com/mixxxdj/mixxx/pull/11771>`__
  `#10600 <https://github.com/mixxxdj/mixxx/issues/10600>`__
* Fix build issues with Protobuf v23.4 and with clang 32
  `#11751 <https://github.com/mixxxdj/mixxx/pull/11751>`__
  `#11765 <https://github.com/mixxxdj/mixxx/pull/11765>`__
  `#11762 <https://github.com/mixxxdj/mixxx/issues/11762>`__
* Disable GL VU-Meters on Windows by default. They can be re-enabled via the command line option ``--enableVuMeterGL``.
  `#11787 <https://github.com/mixxxdj/mixxx/pull/11787>`__
  `#11785 <https://github.com/mixxxdj/mixxx/issues/11785>`__
  `#11789 <https://github.com/mixxxdj/mixxx/issues/11789>`__
* Library preferences: Uncheck Serato metadata export when file metadata export is unchecked
  `#11782 <https://github.com/mixxxdj/mixxx/pull/11782>`__
  `#11226 <https://github.com/mixxxdj/mixxx/issues/11226>`__
* Denon MC6000MK2: Delete mapping for main gain
  `#11792 <https://github.com/mixxxdj/mixxx/pull/11792>`__
* Improve output in case of some failed file system operations
  `#11783 <https://github.com/mixxxdj/mixxx/pull/11783>`__
* Fix overlapping buffers when decoding M4A files using FFmpeg before 4.4
  `#11760 <https://github.com/mixxxdj/mixxx/pull/11760>`__
  `#11545 <https://github.com/mixxxdj/mixxx/issues/11545>`__
* Don't reject key values from file metadata with non-minor/-major scales.
  `#11001 <https://github.com/mixxxdj/mixxx/pull/11001>`__
  `#10995 <https://github.com/mixxxdj/mixxx/issues/10995>`__
* Allow playing tracks with durations of more than 6 hours
  `#11511 <https://github.com/mixxxdj/mixxx/pull/11511>`__
  `#11504 <https://github.com/mixxxdj/mixxx/issues/11504>`__
* Update latency compensation for Soundtouch version 2.1.1 to 2.3
  `#11154 <https://github.com/mixxxdj/mixxx/pull/11154>`__

.. _v2-3-5:

`2.3.5 <https://github.com/mixxxdj/mixxx/milestone/39>`__ (2023-05-10)
-------------------------------------------------------------------------


* Fix empty waveform overview after loading a track (Mixxx 2.3.4 regression)
  Fixed by `#11333 <https://github.com/mixxxdj/mixxx/pull/11333>`__
  `#11359 <https://github.com/mixxxdj/mixxx/pull/11359>`__
  `#11344 <https://github.com/mixxxdj/mixxx/issues/11344>`__
* Fullscreen: Fix a crash that occurs on Linux after enabling fullsceen and using menu
  shortcuts e.g. Alt-F.
  `#11328 <https://github.com/mixxxdj/mixxx/pull/11328>`__
  `#11320 <https://github.com/mixxxdj/mixxx/issues/11320>`__
* Fullscreen: Rebuild & reconnect menu only on desktops with global menu
  `#11350 <https://github.com/mixxxdj/mixxx/pull/11350>`__
* macOS: Request Microphone and line-in access permission.
  `#11367 <https://github.com/mixxxdj/mixxx/pull/11367>`__
  `#11365 <https://github.com/mixxxdj/mixxx/issues/11365>`__
* JACK API: Allow to explicit select buffers of 2048 and 4096 frames/period. They are not
  supported by the automatic buffer setting of the used PortAudio library.
  `#11366 <https://github.com/mixxxdj/mixxx/pull/11366>`__
  `#11341 <https://github.com/mixxxdj/mixxx/issues/11341>`__
* Pioneer DDJ-400: Make Beat FX section more intuitive
  `#10912 <https://github.com/mixxxdj/mixxx/pull/10912>`__
* Playlist export: Adopt new extension after changing the playlist type
  `#11332 <https://github.com/mixxxdj/mixxx/pull/11332>`__
  `#11327 <https://github.com/mixxxdj/mixxx/issues/11327>`__
* LateNight: brighter fx parameter buttons
  `#11397 <https://github.com/mixxxdj/mixxx/pull/11397>`__
* Fix drift in analysis data after exporting metadata to MP3 files with ID3v1.1 tags
  `#11168 <https://github.com/mixxxdj/mixxx/pull/11168>`__
  `#11159 <https://github.com/mixxxdj/mixxx/issues/11159>`__
* Fix broadcasting using Opus encoding
  `#11349 <https://github.com/mixxxdj/mixxx/pull/11349>`__
  `#10666 <https://github.com/mixxxdj/mixxx/issues/10666>`__
* Tango: Remove VU peak indicators from stacked layout. This fixes a visual regression in Mixxx 2.3.4.
  `#11430 <https://github.com/mixxxdj/mixxx/pull/11430>`__
  `#11362 <https://github.com/mixxxdj/mixxx/issues/11362>`__
* Hercules P32: Allow optional using pregain instead of dry/wet knob
  `#3538 <https://github.com/mixxxdj/mixxx/pull/3538>`__
* Improve Color Picker dialog
  `#11439 <https://github.com/mixxxdj/mixxx/pull/11439>`__
* Fix blank Waveform overview after changing Skin with a track loaded
  `#11453 <https://github.com/mixxxdj/mixxx/pull/11453>`__
* Linux: Log a warning when the audio thread is not scheduled with real-time policy
  `#11472 <https://github.com/mixxxdj/mixxx/pull/11472>`__
  `#11465 <https://github.com/mixxxdj/mixxx/issues/11465>`__
* Auto DJ: Fixes stop due to tracks with changed length
  `#11479 <https://github.com/mixxxdj/mixxx/pull/11479>`__
  `#11492 <https://github.com/mixxxdj/mixxx/pull/11492>`__
  `#11448 <https://github.com/mixxxdj/mixxx/issues/11448>`__

  * Auto DJ: Fix Auto DJ indicator state when controlling it via  shortcut (SHIFT+F12)
    `#11494 <https://github.com/mixxxdj/mixxx/issues/11494>`__
    `#11495 <https://github.com/mixxxdj/mixxx/pull/11495>`__

* Fix building with Clang 15/16
  `#11490 <https://github.com/mixxxdj/mixxx/pull/11490>`__
  `#11485 <https://github.com/mixxxdj/mixxx/pull/11485>`__
* Fix EQ and waveforms analysis when compiling with GCC 13
  `#11501 <https://github.com/mixxxdj/mixxx/pull/11501>`__
  `#11483 <https://github.com/mixxxdj/mixxx/issues/11483>`__
  `#11502 <https://github.com/mixxxdj/mixxx/pull/11502>`__
  `#11480 <https://github.com/mixxxdj/mixxx/pull/11480>`__
  `#11488 <https://github.com/mixxxdj/mixxx/pull/11488>`__
* Numark Mixtrack Pro FX: Fix sound output via WDM-KS on Windows
  `#11393 <https://github.com/mixxxdj/mixxx/issues/11393>`__
* Fix crash on startup caused by faulty ASIO driver like FlexASIO 1.4 or Music Maker
  `#11426 <https://github.com/mixxxdj/mixxx/issues/11426>`__
  `#10081 <https://github.com/mixxxdj/mixxx/issues/10081>`__
* Windows: Show a loopback device that allows to mix in system sound
  `#11427 <https://github.com/mixxxdj/mixxx/issues/11427>`__
  `#11451 <https://github.com/mixxxdj/mixxx/issues/11451>`__
* Fix sorting via column header in external library features
  `#11491 <https://github.com/mixxxdj/mixxx/issues/11491>`__
  `#11499 <https://github.com/mixxxdj/mixxx/pull/11499>`__
  `#11498 <https://github.com/mixxxdj/mixxx/pull/11498>`__
* Fix wrong waveform background color on recent Linux distributions like Fedora 37
  `#11164 <https://github.com/mixxxdj/mixxx/issues/11164>`__
  `#11523 <https://github.com/mixxxdj/mixxx/pull/11523>`__
* Serato Metadata: Don't import empty (black) cue points
  `#11534 <https://github.com/mixxxdj/mixxx/pull/11534>`__
  `#11530 <https://github.com/mixxxdj/mixxx/issues/11530>`__
  `#11467 <https://github.com/mixxxdj/mixxx/pull/11467>`__
  `#11466 <https://github.com/mixxxdj/mixxx/pull/11466>`__
  `#11283 <https://github.com/mixxxdj/mixxx/issues/11283>`__
* Track context menu: Immediately adopt new position when resetting cues
  `#11482 <https://github.com/mixxxdj/mixxx/pull/11482>`__
* Windows: Fix possible crash with faulty mp3 files
  `#11535 <https://github.com/mixxxdj/mixxx/pull/11535>`__
  `#11531 <https://github.com/mixxxdj/mixxx/issues/11531>`__
  `#11528 <https://github.com/mixxxdj/mixxx/pull/11528>`__
  `#11521 <https://github.com/mixxxdj/mixxx/issues/11521>`__

.. _v2-3-4:

`2.3.4 <https://launchpad.net/mixxx/+milestone/2.3.4>`__ (2023-03-03)
------------------------------------------------------------------------


* Track Properties: Show 'date added' as local time `#4838 <https://github.com/mixxxdj/mixxx/pull/4838>`__ `#10776 <https://github.com/mixxxdj/mixxx/issues/10776>`__
* Shade: Fix library sidebar splitter glitch `#4828 <https://github.com/mixxxdj/mixxx/pull/4828>`__ `#10757 <https://github.com/mixxxdj/mixxx/issues/10757>`__
* LateNight: Add a border to the crossfader when Auto DJ is active. `#10913 <https://github.com/mixxxdj/mixxx/pull/10913>`__
* LateNight: Isolate searchbar so maximize button is attached to tracks view. `#11132 <https://github.com/mixxxdj/mixxx/pull/11132>`__
* macOS builds: Perform ad-hoc signing of macOS bundle in Pull request and personal repositories `#4774 <https://github.com/mixxxdj/mixxx/pull/4774>`__
* Waveform: Avoid visual glitch with ranges < 1 px `#4804 <https://github.com/mixxxdj/mixxx/pull/4804>`__
* Build Mixxx on macOS 11, replacing deprecated macOS 10.15 `#4863 <https://github.com/mixxxdj/mixxx/pull/4863>`__
* Add macOS 13.0 (Ventura) support, by using portaudio 19.7.0  `#11046 <https://github.com/mixxxdj/mixxx/pull/11046>`__
* EQ preferences: Properly restore 'One EQ for all decks' setting `#4886 <https://github.com/mixxxdj/mixxx/pull/4886>`__
* Cover Art: Fix picking wrong cover file, when track file name contains extra dots `#4909 <https://github.com/mixxxdj/mixxx/pull/4909>`__
* MusicBrainz: Respect rate limits `#10874 <https://github.com/mixxxdj/mixxx/pull/10874>`__ `#10795 <https://github.com/mixxxdj/mixxx/issues/10795>`__
* MusicBrainz: Stop fetching after closing the dialog `#10878 <https://github.com/mixxxdj/mixxx/pull/10878>`__ `#10877 <https://github.com/mixxxdj/mixxx/issues/10877>`__
* MusicBrainz: Fixed stalled GUI after client timeout `#10875 <https://github.com/mixxxdj/mixxx/pull/10875>`__ `#10883 <https://github.com/mixxxdj/mixxx/issues/10883>`__
* macOs: Fix frozen skin control after Ctrl-Click `#10869 <https://github.com/mixxxdj/mixxx/pull/10869>`__ `#10831 <https://github.com/mixxxdj/mixxx/issues/10831>`__
* Avoid redundant messages boxes after track loading fails `#10889 <https://github.com/mixxxdj/mixxx/pull/10889>`__
* Use OpenGL VU meter widgets. This aims to improve performance with macOS.
  `#10893 <https://github.com/mixxxdj/mixxx/pull/10893>`__
  `#11052 <https://github.com/mixxxdj/mixxx/pull/11052>`__
  `#10979 <https://github.com/mixxxdj/mixxx/pull/10979>`__
  `#10973 <https://github.com/mixxxdj/mixxx/pull/10973>`__
  `#10983 <https://github.com/mixxxdj/mixxx/pull/10983>`__
  `#11288 <https://github.com/mixxxdj/mixxx/pull/11288>`__
* Prevent wild numbers from appearing during scratching under vinyl control. `#10916 <https://github.com/mixxxdj/mixxx/pull/10916>`__
* Fixed a possible crash due to a race condition when editing cue points. `#10976 <https://github.com/mixxxdj/mixxx/pull/10976>`__ `#10689 <https://github.com/mixxxdj/mixxx/issues/10689>`__
* Fixed a possible crash when overing cue point via mouse in the waveforms. `#10960 <https://github.com/mixxxdj/mixxx/pull/10960>`__ `#10956 <https://github.com/mixxxdj/mixxx/issues/10956>`__
* History: Disallow dropping tracks. `#10969 <https://github.com/mixxxdj/mixxx/pull/10969>`__ `#10250 <https://github.com/mixxxdj/mixxx/issues/10250>`__
* WTrackMenu: Sort crates and playlists like in sidebar. `#11023 <https://github.com/mixxxdj/mixxx/pull/11023>`__
* WCoverArtLabel: Don't open full-size cover if no cover is loaded, to avoid an issue when closing. `#11022 <https://github.com/mixxxdj/mixxx/pull/11022>`__ `#11021 <https://github.com/mixxxdj/mixxx/issues/11021>`__
* Removed integer truncation of the position when reading cue points from the database. `#10998 <https://github.com/mixxxdj/mixxx/pull/10998>`__
* Fix cue points being assigned invalid value of -1.0 `#11000 <https://github.com/mixxxdj/mixxx/pull/11000>`__ `#10993 <https://github.com/mixxxdj/mixxx/issues/10993>`__
* Auto DJ: Added a warning in a message box when it is started without decks with left and a right crossfader orientation `#11018 <https://github.com/mixxxdj/mixxx/pull/11018>`__
* Fixed crash with FFmpeg decoder `#11044 <https://github.com/mixxxdj/mixxx/pull/11044>`__
* Fixed issue with finding moved library tracks. `#11051 <https://github.com/mixxxdj/mixxx/pull/11051>`__
* Preserve and synchronize ID3v1 tags (TagLib v1.12) `#11163 <https://github.com/mixxxdj/mixxx/pull/11163>`__ `#11123 <https://github.com/mixxxdj/mixxx/issues/11123>`__
* Replay Gain Preferences: Fix the "adjust by" text in case of negative adjustments `#11176 <https://github.com/mixxxdj/mixxx/pull/11176>`__
* macOs: Install Qt translation `#11134 <https://github.com/mixxxdj/mixxx/pull/11134>`__ `#11110 <https://github.com/mixxxdj/mixxx/issues/11110>`__
* macOs: Fix assuming wrong system language `#11218 <https://github.com/mixxxdj/mixxx/pull/11218>`__ `#11195 <https://github.com/mixxxdj/mixxx/issues/11195>`__
* Fix resetting track colors on metadata reimport (Serato metadata): `#11217 <https://github.com/mixxxdj/mixxx/pull/11217>`__ `#11213 <https://github.com/mixxxdj/mixxx/issues/11213>`__
* Preferences: Fix incomplete version check in 2.3 during upgrade `#11229 <https://github.com/mixxxdj/mixxx/pull/11229>`__ `#9709 <https://github.com/mixxxdj/mixxx/issues/9709>`__
* Allow search in external libraries `#11221 <https://github.com/mixxxdj/mixxx/pull/11221>`__ `#11216 <https://github.com/mixxxdj/mixxx/issues/11216>`__
* JACK buffer size fix `#11121 <https://github.com/mixxxdj/mixxx/pull/11121>`__
* Don't discard file tags with tuning information like "A#m +50" `#10992 <https://github.com/mixxxdj/mixxx/pull/10992>`__
* Year search: Find also full date entries `#11251 <https://github.com/mixxxdj/mixxx/pull/11251>`__ `#11113 <https://github.com/mixxxdj/mixxx/issues/11113>`__
* Fix visual alignment of beats and waveform in case of decoding issues `#11162 <https://github.com/mixxxdj/mixxx/pull/11162>`__
* Avoid "active key-value observers" messages during skin parsing on macOS `#11265 <https://github.com/mixxxdj/mixxx/pull/11265>`__
* Fullscreen on Linux: Fix issues caused by Ubuntu Unity workaround `#11295 <https://github.com/mixxxdj/mixxx/pull/11295>`__ `#11281 <https://github.com/mixxxdj/mixxx/issues/11281>`__ `#11294 <https://github.com/mixxxdj/mixxx/issues/11294>`__

New Controller Mappings
^^^^^^^^^^^^^^^^^^^^^^^


* Traktor Kontrol S2 Mk1: Add controller mapping `#3905 <https://github.com/mixxxdj/mixxx/pull/3905>`__
* Numark Party Mix: Mapping added `#4720 <https://github.com/mixxxdj/mixxx/pull/4720>`__

Controller Fixes
^^^^^^^^^^^^^^^^


* Traktor S3: Fix issues with sampler and hotcue buttons `#4676 <https://github.com/mixxxdj/mixxx/pull/4676>`__
* Numark DJ2GO2: Fix sliders and knobs `#4835 <https://github.com/mixxxdj/mixxx/pull/4835>`__ `#10586 <https://github.com/mixxxdj/mixxx/issues/10586>`__
* Numark DJ2Go2: Support HotCue clear with pad `#10841 <https://github.com/mixxxdj/mixxx/pull/10841>`__
* Numark DJ2Go2: Fix inverted tempo fader `#10852 <https://github.com/mixxxdj/mixxx/pull/10852>`__ `#10586 <https://github.com/mixxxdj/mixxx/issues/10586>`__
* Numark N4: Inverted pitch slider, to match the GUI orientation `#11057 <https://github.com/mixxxdj/mixxx/pull/11046>`__
* Ableton Push: Show as one device `#10905 <https://github.com/mixxxdj/mixxx/pull/10905>`__
* Denon DJ MC7000: off-by-one fix, soft-start/break effect, pitch play, 32 velocity samplers
  `#4902 <https://github.com/mixxxdj/mixxx/pull/4902>`__
  `#4729 <https://github.com/mixxxdj/mixxx/pull/4729>`__
* Potmeters: Add support for arbitrary maximums in 7-/14-bit handlers from controller scripts `#4495 <https://github.com/mixxxdj/mixxx/pull/4495>`__
* Controller Preferences: Fix some usability issues `#10821 <https://github.com/mixxxdj/mixxx/pull/10821>`__
* Controller mapping table: show readable/translated strings for script bindings `#11139 <https://github.com/mixxxdj/mixxx/pull/11139>`__
* Control picker menu: Added loop_in/out_goto to list `#11133 <https://github.com/mixxxdj/mixxx/pull/11133>`__

Packaging
^^^^^^^^^


* Fix compatibility with FFmpeg 5.1 and require FFmpeg v4.1.9 `#10862 <https://github.com/mixxxdj/mixxx/pull/10862>`__ `#10866 <https://github.com/mixxxdj/mixxx/pull/10866>`__
* Fix GCC 12.2.0 compatibility `#10863 <https://github.com/mixxxdj/mixxx/pull/10863>`__
* Improve CMake 3.24 compatibility `#10864 <https://github.com/mixxxdj/mixxx/pull/10864>`__
* Use MIXXX_VCPKG_ROOT cmake and environment variable to find the vcpkg environment `#10904 <https://github.com/mixxxdj/mixxx/pull/10904>`__
* Fix ``-Wswitch`` when building with FLAC >= 1.4.0 `#10921 <https://github.com/mixxxdj/mixxx/pull/10921>`__

.. _v2-3-3:

`2.3.3 <https://launchpad.net/mixxx/+milestone/2.3.3>`__ (2022-06-21)
------------------------------------------------------------------------


* Pioneer DDJ-SB3: Fix controller breaking when releasing the shift button `#4659 <https://github.com/mixxxdj/mixxx/pull/4659>`__
* Traktor S3: Push two deck switches to explicitly clone decks `#4665 <https://github.com/mixxxdj/mixxx/pull/4665>`__ `#4671 <https://github.com/mixxxdj/mixxx/pull/4671>`__ `#10660 <https://github.com/mixxxdj/mixxx/issues/10660>`__
* Behringer DDM4000: Improve stability and add soft-takeover for encoder knobs `#4318 <https://github.com/mixxxdj/mixxx/pull/4318>`__ `#4799 <https://github.com/mixxxdj/mixxx/pull/4799>`__
* Denon MC7000: Fix 'inverted shift' bug in the controller mapping `#4755 <https://github.com/mixxxdj/mixxx/pull/4755>`__
* Fix spinback and break effect in the controller engine `#4708 <https://github.com/mixxxdj/mixxx/pull/4708>`__
* Fix scratch on first wheel touch `#4761 <https://github.com/mixxxdj/mixxx/pull/4761>`__ `#9489 <https://github.com/mixxxdj/mixxx/issues/9489>`__
* Preferences: Prevent controller settings being treated as changed even though they were not `#4721 <https://github.com/mixxxdj/mixxx/pull/4721>`__ `#10365 <https://github.com/mixxxdj/mixxx/issues/10365>`__
* Fix rare crash when closing the progress dialog `#4695 <https://github.com/mixxxdj/mixxx/pull/4695>`__
* Prevent preferences dialog from going out of screen `#4613 <https://github.com/mixxxdj/mixxx/pull/4613>`__
* Fix undesired jump-cuts in Auto DJ `#4693 <https://github.com/mixxxdj/mixxx/pull/4693>`__ `#10592 <https://github.com/mixxxdj/mixxx/issues/10592>`__ `#10093 <https://github.com/mixxxdj/mixxx/issues/10093>`__
* Fix bug that caused Auto DJ to stop playback after some time `#4698 <https://github.com/mixxxdj/mixxx/pull/4698>`__ `#10093 <https://github.com/mixxxdj/mixxx/issues/10093>`__ `#10670 <https://github.com/mixxxdj/mixxx/issues/10670>`__
* Do not reset crossfader when Auto DJ is deactivated `#4714 <https://github.com/mixxxdj/mixxx/pull/4714>`__ `#10683 <https://bugs.launchpad.net/bugs/1965298>`__
* Change the minimum Auto DJ transition time to -99 `#4768 <https://github.com/mixxxdj/mixxx/pull/4768>`__ `#10739 <https://github.com/mixxxdj/mixxx/issues/10739>`__
* Samplers, crates, playlists: fix storing import/export paths `#4699 <https://github.com/mixxxdj/mixxx/pull/4699>`__ `#10679 <https://bugs.launchpad.net/bugs/1964508>`__
* Library: keep hidden tracks in history `#4725 <https://github.com/mixxxdj/mixxx/pull/4725>`__
* Broadcasting: allow multiple connections to same mount if only one is enabled `#4750 <https://github.com/mixxxdj/mixxx/pull/4750>`__ `#10727 <https://github.com/mixxxdj/mixxx/issues/10727>`__
* Fix a rare mouse vanish bug when controlling knobs `#4744 <https://github.com/mixxxdj/mixxx/pull/4744>`__ `#6922 <https://github.com/mixxxdj/mixxx/issues/6922>`__ `#10715 <https://github.com/mixxxdj/mixxx/issues/10715>`__
* Restore keylock from configuration and fix pitch ratio rounding issue `#4756 <https://github.com/mixxxdj/mixxx/pull/4756>`__ `#10518 <https://github.com/mixxxdj/mixxx/issues/10518>`__
* Improve CSV export of playlists and crates and fix empty rating column `#4762 <https://github.com/mixxxdj/mixxx/pull/4762>`__
* Fix passthrough-related crash in waveform code `#4789 <https://github.com/mixxxdj/mixxx/pull/4789>`__ `#4791 <https://github.com/mixxxdj/mixxx/pull/4791>`__ `#10650 <https://github.com/mixxxdj/mixxx/issues/10650>`__ `#10743 <https://github.com/mixxxdj/mixxx/issues/10743>`__
* Passthrough: stop rendering waveforms and disable Cue/Play indicators `4793 <https://github.com/mixxxdj/mixxx/pull/4793>`__

.. _v2-3-2:

`2.3.2 <https://launchpad.net/mixxx/+milestone/2.3.2>`__ (2022-01-31)
------------------------------------------------------------------------


* Playlist: Enable sorting by color `#4352 <https://github.com/mixxxdj/mixxx/pull/4352>`__ `#10546 <https://github.com/mixxxdj/mixxx/issues/10546>`__
* Fix crash when using Doubling/Halving/etc. BPM from track's Properties window on tracks without BPM `#4587 <https://github.com/mixxxdj/mixxx/pull/4587>`__ `#10625 <https://github.com/mixxxdj/mixxx/issues/10625>`__
* Fix writing metadata on Windows for files that have never been played `#4586 <https://github.com/mixxxdj/mixxx/pull/4586>`__ `#10620 <https://github.com/mixxxdj/mixxx/issues/10620>`__
* Preserve file creation time when writing metadata on Windows `#4586 <https://github.com/mixxxdj/mixxx/pull/4586>`__ `#10619 <https://github.com/mixxxdj/mixxx/issues/10619>`__
* Fix handling of file extension when importing and exporting sampler settings `#4539 <https://github.com/mixxxdj/mixxx/pull/4539>`__
* Fix crash when using an empty directory as resource path using the ``--resource-path`` command line option `#4575 <https://github.com/mixxxdj/mixxx/pull/4575>`__ `#10461 <https://github.com/mixxxdj/mixxx/issues/10461>`__
* Pioneer DDJ-SB3: Add controller mapping `#3821 <https://github.com/mixxxdj/mixxx/pull/3821>`__
* Don't wipe sound config during startup if configured devices are unavailable `#4544 <https://github.com/mixxxdj/mixxx/pull/4544>`__
* Append selected file extension when exporting to playlist files `#4531 <https://github.com/mixxxdj/mixxx/pull/4531>`__ `#10066 <https://github.com/mixxxdj/mixxx/issues/10066>`__
* Fix crash when using midi.sendShortMsg and platform vnc `#4635 <https://github.com/mixxxdj/mixxx/pull/4635>`__ `#10632 <https://github.com/mixxxdj/mixxx/issues/10632>`__
* Traktor S3: Fix timedelta calculation bugs `#4646 <https://github.com/mixxxdj/mixxx/pull/4646>`__ `#10645 <https://github.com/mixxxdj/mixxx/issues/10645>`__

Packaging
^^^^^^^^^


* Downloads of external dependencies are placed in build/downloads
* The sources for libkeyfinder are now expected in build/downloads/libkeyfinder-2.2.6.zip instead of build/download/libkeyfinder/v2.2.6.zip
* CMake: Adjust the download directory and name of external dependencies `#4511 <https://github.com/mixxxdj/mixxx/pull/4511>`__
* Fix/Improve Appstream metainfo
  `#4344 <https://github.com/mixxxdj/mixxx/pull/4344>`__
  `#4346 <https://github.com/mixxxdj/mixxx/pull/4346>`__
  `#4349 <https://github.com/mixxxdj/mixxx/pull/4349>`__

.. _v2-3-1:

`2.3.1 <https://launchpad.net/mixxx/+milestone/2.3.1>`__ (2021-09-29)
------------------------------------------------------------------------


* Added mapping for the Numark DJ2GO2 Touch controller `#4108 <https://github.com/mixxxdj/mixxx/pull/4108>`__ `#4287 <https://github.com/mixxxdj/mixxx/pull/4287>`__
* Added mapping for the Numark Mixtrack Pro FX controller `#4160 <https://github.com/mixxxdj/mixxx/pull/4160>`__
* Updated mapping for Behringer DDM4000 mixer `#4262 <https://github.com/mixxxdj/mixxx/pull/4262>`__
* Updated mapping for Denon MC7000 controller `#4021 <https://github.com/mixxxdj/mixxx/pull/4021>`__
* Hercules Inpulse 300: Add better FX controls and other minor improvements `#4246 <https://github.com/mixxxdj/mixxx/pull/4246>`__
* Denon MC7000: Improve slip mode and jog wheel handling `#4021 <https://github.com/mixxxdj/mixxx/pull/4021>`__ `#4324 <https://github.com/mixxxdj/mixxx/pull/4324>`__
* Disabled detection of keyboards and mice as HID controllers `#4243 <https://github.com/mixxxdj/mixxx/pull/4243>`__
* Disabled detection of all HID controllers with Apple's vendor ID. Apple doesn't build actual controllers. `#4260 <https://github.com/mixxxdj/mixxx/pull/4260>`__ `#4273 <https://github.com/mixxxdj/mixxx/pull/4273>`__
* Add support for HiDPI scale factors of 125% and 175% (only with Qt 5.14+) `#10485 <https://github.com/mixxxdj/mixxx/issues/10485>`__ `#4161 <https://github.com/mixxxdj/mixxx/pull/4161>`__
* Fix Echo effect adding left channel samples to right channel `#4141 <https://github.com/mixxxdj/mixxx/pull/4141>`__
* Fix bad phase seek when starting from preroll `#10423 <https://github.com/mixxxdj/mixxx/issues/10423>`__ `#4093 <https://github.com/mixxxdj/mixxx/pull/4093>`__
* Fix bad phase seek when a channel's audible status changes `#4156 <https://github.com/mixxxdj/mixxx/pull/4156>`__
* Tango skin: Show crossfader assign buttons by default `#4046 <https://github.com/mixxxdj/mixxx/pull/4046>`__
* Fix keyfinder library in arm64 builds `#4047 <https://github.com/mixxxdj/mixxx/pull/4047>`__
* Fix wrong track being recorded in History `#10454 <https://github.com/mixxxdj/mixxx/issues/10454>`__ `#4041 <https://github.com/mixxxdj/mixxx/pull/4041>`__ `#4059 <https://github.com/mixxxdj/mixxx/pull/4059>`__ `#4107 <https://github.com/mixxxdj/mixxx/pull/4107>`__ `#4296 <https://github.com/mixxxdj/mixxx/pull/4296>`__
* Fix support for relative paths in the skin system which caused missing images in third-party skins `#4151 <https://github.com/mixxxdj/mixxx/pull/4151>`__
* Fix relocation of directories with special/reserved characters in path name `#4146 <https://github.com/mixxxdj/mixxx/pull/4146>`__
* Update keyboard shortcuts sheet `#4042 <https://github.com/mixxxdj/mixxx/pull/4042>`__
* Library: resize the Played checkbox and BPM lock with the library font `#4050 <https://github.com/mixxxdj/mixxx/pull/4050>`__
* Don't allow Input focus on waveforms `#4134 <https://github.com/mixxxdj/mixxx/pull/4134>`__
* Fix performance issue on AArch64 by enabling flush-to-zero for floating-point arithmetic `#4144 <https://github.com/mixxxdj/mixxx/pull/4144>`__
* Fix custom key notation not restored correctly after restart `#4136 <https://github.com/mixxxdj/mixxx/pull/4136>`__
* Traktor S3: Disable scratch when switching decks to prevent locked scratch issue `#4073 <https://github.com/mixxxdj/mixxx/pull/4073>`__
* FFmpeg: Ignore inaudible samples before start of stream `#4245 <https://github.com/mixxxdj/mixxx/pull/4245>`__
* Controller Preferences: Don't automatically enable checkbox if controller is disabled `#4244 <https://github.com/mixxxdj/mixxx/pull/4244>`__ `#10503 <https://github.com/mixxxdj/mixxx/issues/10503>`__
* Tooltips: Always show tooltips in preferences `#4198 <https://github.com/mixxxdj/mixxx/pull/4198>`__ `#9716 <https://github.com/mixxxdj/mixxx/issues/9716>`__
* Tooltips: Use item label for tooltips in library side bar and show ID when debugging. `#4247 <https://github.com/mixxxdj/mixxx/pull/4247>`__
* Library sidebar: Also activate items on PageUp/Down events. `#4237 <https://github.com/mixxxdj/mixxx/pull/4237>`__
* Fix handling of preview button cell events in developer mode. `#4264 <https://github.com/mixxxdj/mixxx/pull/4264>`__ `#10418 <https://github.com/mixxxdj/mixxx/issues/10418>`__
* Auto DJ: Fix bug which could make an empty track stop Auto DJ. `#4267 <https://github.com/mixxxdj/mixxx/pull/4267>`__ `#10504 <https://github.com/mixxxdj/mixxx/issues/10504>`__
* Fix Auto DJ skipping tracks randomly `#4319 <https://github.com/mixxxdj/mixxx/pull/4319>`__ `#10505 <https://github.com/mixxxdj/mixxx/issues/10505>`__
* Fix high CPU load due to extremely high internal sync clock values `#4312 <https://github.com/mixxxdj/mixxx/pull/4312>`__ `#10520 <https://github.com/mixxxdj/mixxx/issues/10520>`__
* Fix preference option for re-analyzing beatgrids imported from other software `#4288 <https://github.com/mixxxdj/mixxx/pull/4288>`__
* Fix wrong base tag used for deployment and displayed in About dialog `#4070 <https://github.com/mixxxdj/mixxx/pull/4070>`__

Packaging
^^^^^^^^^


* It is no longer necessary to manually copy the udev rule file in packaging scripts. Now pkg-config is used to determine the udevdir used to install the rules file in the CMake install step when CMAKE_INSTALL_PREFIX is ``/`` or ``/usr``.  `#4126 <https://github.com/mixxxdj/mixxx/pull/4126>`__
* Various build issues on FreeBSD are fixed `#4122 <https://github.com/mixxxdj/mixxx/pull/4122>`__ `#4123 <https://github.com/mixxxdj/mixxx/pull/4123>`__ `#4124 <https://github.com/mixxxdj/mixxx/pull/4124>`__
* .desktop file has be renamed to org.mixxx.Mixxx.desktop according to Freedesktop standards `#4206 <https://github.com/mixxxdj/mixxx/pull/4206>`__
* Uses system provided hidapi library if version >= 0.10.1 `#4215 <https://github.com/mixxxdj/mixxx/pull/4215>`__
* Please update PortAudio to `19.7 <https://github.com/PortAudio/portaudio/releases/tag/v19.7.0>`__ if you have not done so already. This is required for Mixxx to work with PipeWire via the JACK API for many devices.
* Install multiple sizes of rasterized icons `#4204 <https://github.com/mixxxdj/mixxx/pull/4204>`__ `#4315 <https://github.com/mixxxdj/mixxx/pull/4315>`__ `#4254 <https://github.com/mixxxdj/mixxx/pull/4254>`__
* CMake: Fixed detection of SoundTouch pkgconfig file and version `#4209 <https://github.com/mixxxdj/mixxx/pull/4209>`__
* Fix AppStream metainfo `#4205 <https://github.com/mixxxdj/mixxx/pull/4205>`__ `#4317 <https://github.com/mixxxdj/mixxx/pull/4317>`__

.. _v2-3-0:

`2.3.0 <https://launchpad.net/mixxx/+milestone/2.3.0>`__ (2021-06-28)
------------------------------------------------------------------------

Hotcues
^^^^^^^


* Add hotcue colors and custom labels by right clicking hotcue buttons or right clicking hotcues on overview waveforms `#2016 <https://github.com/mixxxdj/mixxx/pull/2016>`__ `#2520 <https://github.com/mixxxdj/mixxx/pull/2520>`__ `#2238 <https://github.com/mixxxdj/mixxx/pull/2238>`__ `#2560 <https://github.com/mixxxdj/mixxx/pull/2560>`__ `#2557 <https://github.com/mixxxdj/mixxx/pull/2557>`__ `#2362 <https://github.com/mixxxdj/mixxx/pull/2362>`__
* Mouse hover cues on overview waveform to show time remaining until the cue `#2238 <https://github.com/mixxxdj/mixxx/pull/2238>`__

Hotcue & Track Colors
^^^^^^^^^^^^^^^^^^^^^


* Add configurable color per track `#2470 <https://github.com/mixxxdj/mixxx/pull/2470>`__ `#2539 <https://github.com/mixxxdj/mixxx/pull/2539>`__ `#2545 <https://github.com/mixxxdj/mixxx/pull/2545>`__ `#2630 <https://github.com/mixxxdj/mixxx/pull/2630>`__ `#6852 <https://github.com/mixxxdj/mixxx/issues/6852>`__
* Add customizable color palettes for hotcue and track colors `#2530 <https://github.com/mixxxdj/mixxx/pull/2530>`__ `#2589 <https://github.com/mixxxdj/mixxx/pull/2589>`__ `#3749 <https://github.com/mixxxdj/mixxx/pull/3749>`__ `#2902 <https://github.com/mixxxdj/mixxx/pull/2902>`__
* Add hotcue color find-and-replace tool `#2547 <https://github.com/mixxxdj/mixxx/pull/2547>`__

Importing From Other DJ Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* Import cue points, track colors, and playlists from Serato file tags & database `#2480 <https://github.com/mixxxdj/mixxx/pull/2480>`__ `#2526 <https://github.com/mixxxdj/mixxx/pull/2526>`__ `#2499 <https://github.com/mixxxdj/mixxx/pull/2499>`__ `#2495 <https://github.com/mixxxdj/mixxx/pull/2495>`__ `#2673 <https://github.com/mixxxdj/mixxx/pull/2673>`__ `#3885 <https://github.com/mixxxdj/mixxx/pull/3885>`__

  * Note: Mixxx does not yet support multiple loops per track. We are `working on this for Mixxx 2.4 <https://github.com/mixxxdj/mixxx/pull/2194>`_. In Mixxx 2.3, if you import a track with multiple loops from Serato, Mixxx will use the first loop cue as the single loop Mixxx currently supports. The imported loops are still stored in Mixxx's database and are treated as hotcues in Mixxx 2.3. If you do not delete these hotcues, they will be usable as loops in Mixxx 2.4. Serato keeps loops and hotcues in separate lists, but Mixxx does not, so loops from Serato are imported starting as hotcue 9.

* Import cue points, track colors, and playlists from Rekordbox USB drives `#2119 <https://github.com/mixxxdj/mixxx/pull/2119>`__ `#2555 <https://github.com/mixxxdj/mixxx/pull/2555>`__ `#2543 <https://github.com/mixxxdj/mixxx/pull/2543>`__ `#2779 <https://github.com/mixxxdj/mixxx/pull/2779>`__

  * Note: The first Rekordbox memory cue is imported for the main cue button in Mixxx and the remaining Rekordbox memory cues are imported as Mixxx hotcues, starting with the next hotcue number after the last hotcue from Rekordbox.
  * Note: Mixxx does not yet support multiple loops per track. Imported loops from Rekordbox are treated like imported loops from Serato, so refer to the note above for details.

Intro & Outro Cues
^^^^^^^^^^^^^^^^^^


* Add intro & outro range cues with automatic silence detection `#1242 <https://github.com/mixxxdj/mixxx/pull/1242>`__
* Show duration of intro & outro ranges on overview waveform `#2089 <https://github.com/mixxxdj/mixxx/pull/2089>`__
* Use intro & outro cues in AutoDJ transitions `#2103 <https://github.com/mixxxdj/mixxx/pull/2103>`__

Deck cloning
^^^^^^^^^^^^


* Add deck cloning (also known as "instant doubles" in other DJ software) by dragging and dropping between decks `#1892 <https://github.com/mixxxdj/mixxx/pull/1892>`__ and samplers `#3200 <https://github.com/mixxxdj/mixxx/pull/3200>`__
* Clone decks by double pressing the load button on a controller (with option to disable this) `#2024 <https://github.com/mixxxdj/mixxx/pull/2024>`__ `#2042 <https://github.com/mixxxdj/mixxx/pull/2042>`__

Skins & GUI
^^^^^^^^^^^


* Aesthetically revamped LateNight skin `#2298 <https://github.com/mixxxdj/mixxx/pull/2298>`__ `#2342 <https://github.com/mixxxdj/mixxx/pull/2342>`__
* Right click overview waveform to show time remaining until that point `#2238 <https://github.com/mixxxdj/mixxx/pull/2238>`__
* Show track info dialog when double clicking track labels in decks `#2990 <https://github.com/mixxxdj/mixxx/pull/2990>`__
* Show track context menu when right clicking text in decks `#2612 <https://github.com/mixxxdj/mixxx/pull/2612>`__ `#2675 <https://github.com/mixxxdj/mixxx/pull/2675>`__ `#2684 <https://github.com/mixxxdj/mixxx/pull/2684>`__ `#2696 <https://github.com/mixxxdj/mixxx/pull/2696>`__
* Add laptop battery widget to skins `#2283 <https://github.com/mixxxdj/mixxx/pull/2283>`__ `#2277 <https://github.com/mixxxdj/mixxx/pull/2277>`__ `#2250 <https://github.com/mixxxdj/mixxx/pull/2250>`__ `#2228 <https://github.com/mixxxdj/mixxx/pull/2228>`__ `#2221 <https://github.com/mixxxdj/mixxx/pull/2221>`__ `#2163 <https://github.com/mixxxdj/mixxx/pull/2163>`__ `#2160 <https://github.com/mixxxdj/mixxx/pull/2160>`__ `#2147 <https://github.com/mixxxdj/mixxx/pull/2147>`__ `#2281 <https://github.com/mixxxdj/mixxx/pull/2281>`__ `#2319 <https://github.com/mixxxdj/mixxx/pull/2319>`__ `#2287 <https://github.com/mixxxdj/mixxx/pull/2287>`__
* Show when passthrough mode is active on overview waveforms `#2575 <https://github.com/mixxxdj/mixxx/pull/2575>`__ `#2616 <https://github.com/mixxxdj/mixxx/pull/2616>`__
* Changed format of currently playing track in window title from "artist, title" to "artist - title" `#2807 <https://github.com/mixxxdj/mixxx/pull/2807>`__
* Workaround Linux skin change crash `#3144 <https://github.com/mixxxdj/mixxx/pull/3144>`__ `#10030 <https://github.com/mixxxdj/mixxx/issues/10030>`__
* Fix touch control `#10108 <https://github.com/mixxxdj/mixxx/issues/10108>`__
* Fix broken knob interaction on touchscreens `#3512 <https://github.com/mixxxdj/mixxx/pull/3512>`__
* AutoDJ: Make "enable" shortcut work after startup `#3242 <https://github.com/mixxxdj/mixxx/pull/3242>`__
* Add rate range indicator `#3693 <https://github.com/mixxxdj/mixxx/pull/3693>`__
* Allow menubar to be styled `#3372 <https://github.com/mixxxdj/mixxx/pull/3372>`__ `#3788 <https://github.com/mixxxdj/mixxx/pull/3788>`__
* Add Donate button to About dialog `#3838 <https://github.com/mixxxdj/mixxx/pull/3838>`__ `#3846 <https://github.com/mixxxdj/mixxx/pull/3846>`__
* Add Scrollable Skin Widget `#3890 <https://github.com/mixxxdj/mixxx/pull/3890>`__
* Fix minor visual issues in Skins `#3958 <https://github.com/mixxxdj/mixxx/pull/3958/>`__ `#3954 <https://github.com/mixxxdj/mixxx/pull/3954/>`__ `#3941 <https://github.com/mixxxdj/mixxx/pull/3941/>`__ `#3938 <https://github.com/mixxxdj/mixxx/pull/3938/>`__ `#3936 <https://github.com/mixxxdj/mixxx/pull/3936/>`__ `#3886 <https://github.com/mixxxdj/mixxx/pull/3886/>`__ `#3927 <https://github.com/mixxxdj/mixxx/pull/3927/>`__ `#3844 <https://github.com/mixxxdj/mixxx/pull/3844/>`__ `#3933 <https://github.com/mixxxdj/mixxx/pull/3933/>`__ `#3835 <https://github.com/mixxxdj/mixxx/pull/3835/>`__ `#3902 <https://github.com/mixxxdj/mixxx/pull/3902>`__ `#3931 <https://github.com/mixxxdj/mixxx/pull/3931>`__

Music Feature Analysis
^^^^^^^^^^^^^^^^^^^^^^


* Multithreaded analysis for much faster batch analysis on multicore CPUs `#1624 <https://github.com/mixxxdj/mixxx/pull/1624>`__ `#2142 <https://github.com/mixxxdj/mixxx/pull/2142>`__ `#8686 <https://github.com/mixxxdj/mixxx/issues/8686>`__
* Fix bugs affecting key detection accuracy `#2137 <https://github.com/mixxxdj/mixxx/pull/2137>`__ `#2152 <https://github.com/mixxxdj/mixxx/pull/2152>`__ `#2112 <https://github.com/mixxxdj/mixxx/pull/2112>`__ `#2136 <https://github.com/mixxxdj/mixxx/pull/2136>`__

  * Note: Users who have not manually corrected keys are advised to clear all keys in their library by pressing Ctrl + A in the library, right clicking, going to Reset -> Key, then reanalyzing their library. This will freeze the GUI while Mixxx clears the keys; this is a known problem that we will not be able to fix for 2.3. Wait until it is finished and you will be able to reanalyze tracks for better key detection results.

* Remove VAMP plugin support and use Queen Mary DSP library directly. vamp-plugin-sdk and vamp-hostsdk are no longer required dependencies. `#926 <https://github.com/mixxxdj/mixxx/pull/926>`__
* Improvements BPM detection on non-const beatgrids `#3626 <https://github.com/mixxxdj/mixxx/pull/3626>`__
* Fix const beatgrid placement `#3965 <https://github.com/mixxxdj/mixxx/pull/3965>`__ `#3973 <https://github.com/mixxxdj/mixxx/pull/3973>`__

Music Library
^^^^^^^^^^^^^


* Add support for searching for empty fields (for example ``crate:""``\ ) `#9411 <https://github.com/mixxxdj/mixxx/issues/9411>`__
* Improve synchronization of track metadata and file tags `#2406 <https://github.com/mixxxdj/mixxx/pull/2406>`__
* Library Scanner: Improve hashing of directory contents `#2497 <https://github.com/mixxxdj/mixxx/pull/2497>`__
* Rework of Cover Image Hashing `#8618 <https://github.com/mixxxdj/mixxx/issues/8618>`__ `#2507 <https://github.com/mixxxdj/mixxx/pull/2507>`__ `#2508 <https://github.com/mixxxdj/mixxx/pull/2508>`__
* MusicBrainz: Handle 301 status response `#2510 <https://github.com/mixxxdj/mixxx/pull/2510>`__
* MusicBrainz: Add extended metadata support `#8549 <https://github.com/mixxxdj/mixxx/issues/8549>`__ `#2522 <https://github.com/mixxxdj/mixxx/pull/2522>`__
* TagLib: Fix detection of empty or missing file tags `#9891 <https://github.com/mixxxdj/mixxx/issues/9891>`__ `#2535 <https://github.com/mixxxdj/mixxx/pull/2535>`__
* Fix caching of duplicate tracks that reference the same file `#3027 <https://github.com/mixxxdj/mixxx/pull/3027>`__
* Use 6 instead of only 4 compatible musical keys (major/minor) `#3205 <https://github.com/mixxxdj/mixxx/pull/3205>`__
* Fix possible crash when trying to refocus the tracks table while another Mixxx window has focus `#3201 <https://github.com/mixxxdj/mixxx/pull/3201>`__
* Don't create new tags in file when exporting metadata to it `#3898 <https://github.com/mixxxdj/mixxx/pull/3898>`__
* Fix playlist files beginning with non-english characters not being loaded `#3916 <https://github.com/mixxxdj/mixxx/pull/3916>`__
* Enable sorting in "Hidden Tracks" and "Missing Tracks" views `#3828 <https://github.com/mixxxdj/mixxx/pull/3828>`__ `#9658 <https://github.com/mixxxdj/mixxx/issues/9658/>`__ `#10397 <https://github.com/mixxxdj/mixxx/issues/10397/>`__
* Fix track table being empty after start `#3935 <https://github.com/mixxxdj/mixxx/pull/3935/>`__ `#10426 <https://github.com/mixxxdj/mixxx/issues/10426/>`__ `#10402 <https://github.com/mixxxdj/mixxx/issues/10402/>`__

Audio Codecs
^^^^^^^^^^^^


* Add FFmpeg audio decoder, bringing support for ALAC files `#1356 <https://github.com/mixxxdj/mixxx/pull/1356>`__
* Include LAME MP3 encoder with Mixxx now that the MP3 patent has expired `#7341 <https://github.com/mixxxdj/mixxx/issues/7341>`__ `buildserver:#37 <https://github.com/mixxxdj/buildserver/pull/37>`__ `buildserver:9e8bcee <https://github.com/mixxxdj/buildserver/commit/9e8bcee771731920ae82f3e076d43f0fb51e5027>`__
* Add Opus streaming and recording support. `#7530 <https://github.com/mixxxdj/mixxx/issues/7530>`__
* Remove support for SoundSource plugins because the code was not well-maintained and could lead to crashes `#9435 <https://github.com/mixxxdj/mixxx/issues/9435>`__
* Add HE-AAC encoding capabilities for recording and broadcasting `#3615 <https://github.com/mixxxdj/mixxx/pull/3615>`__

Audio Engine
^^^^^^^^^^^^


* Fix loss of precision when dealing with floating-point sample positions while setting loop out position and seeking using vinyl control `#3126 <https://github.com/mixxxdj/mixxx/pull/3126>`__ `#3127 <https://github.com/mixxxdj/mixxx/pull/3127>`__
* Prevent moving a loop beyond track end `#3117 <https://github.com/mixxxdj/mixxx/pull/3117>`__ `#9478 <https://github.com/mixxxdj/mixxx/issues/9478>`__
* Fix possible memory corruption using JACK on Linux `#3160 <https://github.com/mixxxdj/mixxx/pull/3160>`__
* Fix changing of vinyl lead-in time `#10319 <https://github.com/mixxxdj/mixxx/issues/10319>`__ `#3781 <https://github.com/mixxxdj/mixxx/pull/3781>`__
* Fix tempo change of non-const beatgrid track on audible deck when cueing another track `#3772 <https://github.com/mixxxdj/mixxx/pull/3772>`__
* Fix crash when changing effect unit routing `#3882 <https://github.com/mixxxdj/mixxx/pull/3882>`__ `#9331 <https://github.com/mixxxdj/mixxx/issues/9331>`__
* Make microphone ducking use strength knob the same way in automatic & manual mode `#2750 <https://github.com/mixxxdj/mixxx/pull/2750>`__

Controllers
^^^^^^^^^^^


* Improve workflow for configuring controller mappings and editing mappings `#2569 <https://github.com/mixxxdj/mixxx/pull/2569>`__ `#3278 <https://github.com/mixxxdj/mixxx/pull/3278>`__ `#3667 <https://github.com/mixxxdj/mixxx/pull/3667>`__
* Improve error reporting from controller scripts `#2588 <https://github.com/mixxxdj/mixxx/pull/2588>`__
* Make hotcue and track colors mappable on controllers `#2030 <https://github.com/mixxxdj/mixxx/pull/2030>`__ `#2541 <https://github.com/mixxxdj/mixxx/pull/2541>`__ `#2665 <https://github.com/mixxxdj/mixxx/pull/2665>`__ `#2520 <https://github.com/mixxxdj/mixxx/pull/2520>`__
* Add way to change library table sorting from controllers `#2118 <https://github.com/mixxxdj/mixxx/pull/2118>`__
* Add support for velocity sensitive sampler buttons in Components JS library `#2032 <https://github.com/mixxxdj/mixxx/pull/2032>`__
* Add logging when script ControlObject callback is disconnected successfully `#2054 <https://github.com/mixxxdj/mixxx/pull/2054>`__
* Add controller mapping for Roland DJ-505 `#2111 <https://github.com/mixxxdj/mixxx/pull/2111>`__
* Add controller mapping for Numark iDJ Live II `#2818 <https://github.com/mixxxdj/mixxx/pull/2818>`__
* Add controller mapping for Hercules DJControl Inpulse 200 `#2542 <https://github.com/mixxxdj/mixxx/pull/2542>`__
* Add controller mapping for Hercules DJControl Jogvision `#2370 <https://github.com/mixxxdj/mixxx/pull/2370>`__
* Add controller mapping for Pioneer DDJ-200 `#3185 <https://github.com/mixxxdj/mixxx/pull/3185>`__ `#3193 <https://github.com/mixxxdj/mixxx/pull/3193>`__ `#3742 <https://github.com/mixxxdj/mixxx/pull/3742>`__ `#3793 <https://github.com/mixxxdj/mixxx/pull/3793>`__ `#3949 <https://github.com/mixxxdj/mixxx/pull/3949>`__
* Add controller mapping for Pioneer DDJ-400 `#3479 <https://github.com/mixxxdj/mixxx/pull/3479>`__
* Add controller mapping for ION Discover DJ Pro `#2893 <https://github.com/mixxxdj/mixxx/pull/2893>`__
* Add controller mapping for Native Instrument Traktor Kontrol S3 `#3031 <https://github.com/mixxxdj/mixxx/pull/3031>`__
* Add controller mapping for Behringer BCR2000 `#3342 <https://github.com/mixxxdj/mixxx/pull/3342>`__ `#3943 <https://github.com/mixxxdj/mixxx/pull/3943>`__
* Add controller mapping for Behringer DDM4000 `#3542 <https://github.com/mixxxdj/mixxx/pull/3542>`__
* Add controller mapping for Native Instruments Traktor Kontrol S4MK3 `#11284 <https://github.com/mixxxdj/mixxx/pull/11284>`__
* Update controller mapping for Allen & Heath Xone K2 to add intro/outro cues `#2236 <https://github.com/mixxxdj/mixxx/pull/2236>`__
* Update controller mapping for Hercules P32 for more accurate headmix control `#3537 <https://github.com/mixxxdj/mixxx/pull/3537>`__
* Update controller mapping for Native Instruments Traktor Kontrol S4MK2 to add auto-slip mode and pitch fader range `#3331 <https://github.com/mixxxdj/mixxx/pull/3331>`__
* Fix Pioneer DDJ-SB2 controller mapping auto tempo going to infinity bug `#2559 <https://github.com/mixxxdj/mixxx/pull/2559>`__ `#9838 <https://github.com/mixxxdj/mixxx/issues/9838>`__
* Fix Numark Mixtrack Pro 3 controller mapping inverted FX on/off control `#3758 <https://github.com/mixxxdj/mixxx/pull/3758>`__
* Gracefully handle MIDI overflow `#825 <https://github.com/mixxxdj/mixxx/pull/825>`__

Other
^^^^^


* Add CMake build system with ``ccache`` and ``sccache`` support for faster compilation times and remove SCons `#2280 <https://github.com/mixxxdj/mixxx/pull/2280>`__ `#3618 <https://github.com/mixxxdj/mixxx/pull/3618>`__
* Make Mixxx compile even though ``QT_NO_OPENGL`` or ``QT_OPENGL_ES_2`` is defined (fixes build on Raspberry Pi) `#9887 <https://github.com/mixxxdj/mixxx/issues/9887>`__ `#2504 <https://github.com/mixxxdj/mixxx/pull/2504>`__
* Fix ARM build issues `#3602 <https://github.com/mixxxdj/mixxx/pull/3602>`__
* Fix missing manual in DEB package `#10070 <https://github.com/mixxxdj/mixxx/issues/10070>`__ `#2985 <https://github.com/mixxxdj/mixxx/pull/2985>`__
* Add macOS codesigning and notarization to fix startup warnings `#3281 <https://github.com/mixxxdj/mixxx/pull/3281>`__
* Don't trash user configuration if an error occurs when writing `#3192 <https://github.com/mixxxdj/mixxx/pull/3192>`__
* Enable CUE sheet recording by default `#3374 <https://github.com/mixxxdj/mixxx/pull/3374>`__
* Fix crash when double clicking GLSL waveforms with right mouse button `#3904 <https://github.com/mixxxdj/mixxx/pull/3904>`__
* Derive Mixxx version from ``git describe`` `#3824 <https://github.com/mixxxdj/mixxx/pull/3824>`__ `#3841 <https://github.com/mixxxdj/mixxx/pull/3841>`__ `#3848 <https://github.com/mixxxdj/mixxx/pull/3848>`__
* Improve tapping the BPM of a deck `#3790 <https://github.com/mixxxdj/mixxx/pull/3790>`__ `#10010 <https://github.com/mixxxdj/mixxx/issues/10010>`__
* And countless other small fixes and improvements (too many to list them all!)

.. _v2-2-4:

`2.2.4 <https://launchpad.net/mixxx/+milestone/2.2.4>`__ (2020-06-27)
------------------------------------------------------------------------


* Store default recording format after "Restore Defaults" `#9853 <https://github.com/mixxxdj/mixxx/issues/9853>`__ `#2414 <https://github.com/mixxxdj/mixxx/pull/2414>`__
* Prevent infinite loop when decoding corrupt MP3 files `#2417 <https://github.com/mixxxdj/mixxx/pull/2417>`__
* Add workaround for broken libshout versions `#2040 <https://github.com/mixxxdj/mixxx/pull/2040>`__ `#2438 <https://github.com/mixxxdj/mixxx/pull/2438>`__
* Speed up purging of tracks `#9762 <https://github.com/mixxxdj/mixxx/issues/9762>`__ `#2393 <https://github.com/mixxxdj/mixxx/pull/2393>`__
* Don't stop playback if vinyl passthrough input is configured and PASS button is pressed `#2474 <https://github.com/mixxxdj/mixxx/pull/2474>`__
* Fix debug assertion for invalid crate names `#9871 <https://github.com/mixxxdj/mixxx/issues/9871>`__ `#2477 <https://github.com/mixxxdj/mixxx/pull/2477>`__
* Fix crashes when executing actions on tracks that already disappeared from the DB `#2527 <https://github.com/mixxxdj/mixxx/pull/2527>`__
* AutoDJ: Skip next track when both deck are playing `#7712 <https://github.com/mixxxdj/mixxx/issues/7712>`__ `#2531 <https://github.com/mixxxdj/mixxx/pull/2531>`__
* Tweak scratch parameters for Mixtrack Platinum `#2028 <https://github.com/mixxxdj/mixxx/pull/2028>`__
* Fix auto tempo going to infinity on Pioneer DDJ-SB2 `#2559 <https://github.com/mixxxdj/mixxx/pull/2559>`__
* Fix bpm.tapButton logic and reject missed & double taps `#2594 <https://github.com/mixxxdj/mixxx/pull/2594>`__
* Add controller mapping for Native Instruments Traktor Kontrol S2 MK3 `#2348 <https://github.com/mixxxdj/mixxx/pull/2348>`__
* Add controller mapping for Soundless joyMIDI `#2425 <https://github.com/mixxxdj/mixxx/pull/2425>`__
* Add controller mapping for Hercules DJControl Inpulse 300 `#2465 <https://github.com/mixxxdj/mixxx/pull/2465>`__
* Add controller mapping for Denon MC7000 `#2546 <https://github.com/mixxxdj/mixxx/pull/2546>`__
* Add controller mapping for Stanton DJC.4 `#2607 <https://github.com/mixxxdj/mixxx/pull/2607>`__
* Fix broadcasting via broadcast/recording input `#9959 <https://github.com/mixxxdj/mixxx/issues/9959>`__ `#2743 <https://github.com/mixxxdj/mixxx/pull/2743>`__
* Only apply ducking gain in manual ducking mode when talkover is enabled `#7668 <https://github.com/mixxxdj/mixxx/issues/7668>`__ `#8995 <https://github.com/mixxxdj/mixxx/issues/8995>`__ `#8795 <https://github.com/mixxxdj/mixxx/issues/8795>`__ `#2759 <https://github.com/mixxxdj/mixxx/pull/2759>`__
* Ignore MIDI Clock Messages (0xF8) because they are not usable in Mixxx and inhibited the screensaver `#2786 <https://github.com/mixxxdj/mixxx/pull/2786>`__

.. _v2-2-3:

`2.2.3 <https://launchpad.net/mixxx/+milestone/2.2.3>`__ (2019-11-24)
------------------------------------------------------------------------


* Don't make users reconfigure sound hardware when it has not changed `#2253 <https://github.com/mixxxdj/mixxx/pull/2253>`__
* Fix MusicBrainz metadata lookup `#9780 <https://github.com/mixxxdj/mixxx/issues/9780>`__ `#2328 <https://github.com/mixxxdj/mixxx/pull/2328>`__
* Fix high DPI scaling of cover art `#2247 <https://github.com/mixxxdj/mixxx/pull/2247>`__
* Fix high DPI scaling of cue point labels on scrolling waveforms `#2331 <https://github.com/mixxxdj/mixxx/pull/2331>`__
* Fix high DPI scaling of sliders in Tango skin `#2318 <https://github.com/mixxxdj/mixxx/pull/2318>`__
* Fix sound dropping out during recording `#9732 <https://github.com/mixxxdj/mixxx/issues/9732>`__ `#2265 <https://github.com/mixxxdj/mixxx/pull/2265>`__ `#2305 <https://github.com/mixxxdj/mixxx/pull/2305>`__ `#2308 <https://github.com/mixxxdj/mixxx/pull/2308>`__ `#2309 <https://github.com/mixxxdj/mixxx/pull/2309>`__
* Fix rare crash on application shutdown `#2293 <https://github.com/mixxxdj/mixxx/pull/2293>`__
* Workaround various rare bugs caused by database inconsistencies `#9773 <https://github.com/mixxxdj/mixxx/issues/9773>`__ `#2321 <https://github.com/mixxxdj/mixxx/pull/2321>`__
* Improve handling of corrupt FLAC files `#2315 <https://github.com/mixxxdj/mixxx/pull/2315>`__
* Don't immediately jump to loop start when loop_out is pressed in quantized mode `#9694 <https://github.com/mixxxdj/mixxx/issues/9694>`__ `#2269 <https://github.com/mixxxdj/mixxx/pull/2269>`__
* Preserve order of tracks when dragging and dropping from AutoDJ to playlist `#9661 <https://github.com/mixxxdj/mixxx/issues/9661>`__ `#2237 <https://github.com/mixxxdj/mixxx/pull/2237>`__
* Explicitly use X11 Qt platform plugin instead of Wayland in .desktop launcher `#9787 <https://github.com/mixxxdj/mixxx/issues/9787>`__ `#2340 <https://github.com/mixxxdj/mixxx/pull/2340>`__
* Pioneer DDJ-SX: fix delayed sending of MIDI messages with low audio buffer sizes `#2326 <https://github.com/mixxxdj/mixxx/pull/2326>`__
* Enable modplug support on Linux by default `#9719 <https://github.com/mixxxdj/mixxx/issues/9719>`__ `#2244 <https://github.com/mixxxdj/mixxx/pull/2244>`__ `#2272 <https://github.com/mixxxdj/mixxx/pull/2272>`__
* Fix keyboard shortcut for View > Skin Preferences `#9796 <https://github.com/mixxxdj/mixxx/issues/9796>`__ `#2358 <https://github.com/mixxxdj/mixxx/pull/2358>`__ `#2372 <https://github.com/mixxxdj/mixxx/pull/2372>`__
* Reloop Terminal Mix: Fix mapping of sampler buttons 5-8 `#9772 <https://github.com/mixxxdj/mixxx/issues/9772>`__ `#2330 <https://github.com/mixxxdj/mixxx/pull/2330>`__

.. _v2-2-2:

`2.2.2 <https://launchpad.net/mixxx/+milestone/2.2.2>`__ (2019-08-10)
------------------------------------------------------------------------


* Fix battery widget with upower <= 0.99.7. `#2221 <https://github.com/mixxxdj/mixxx/pull/2221>`__
* Fix BPM adjust in BpmControl. `#9690 <https://github.com/mixxxdj/mixxx/issues/9690>`__
* Disable track metadata export for .ogg files and TagLib 1.11.1. `#9680 <https://github.com/mixxxdj/mixxx/issues/9680>`__
* Fix interaction of hot cue buttons and looping. `#9350 <https://github.com/mixxxdj/mixxx/issues/9350>`__
* Fix detection of moved tracks. `#2197 <https://github.com/mixxxdj/mixxx/pull/2197>`__
* Fix playlist import. `#2200 <https://github.com/mixxxdj/mixxx/pull/2200>`__ `#8852 <https://github.com/mixxxdj/mixxx/issues/8852>`__
* Fix updating playlist labels. `#9697 <https://github.com/mixxxdj/mixxx/issues/9697>`__
* Fix potential segfault on exit. `#9656 <https://github.com/mixxxdj/mixxx/issues/9656>`__
* Fix parsing of invalid BPM values in MP3 files. `#9671 <https://github.com/mixxxdj/mixxx/issues/9671>`__
* Fix crash when removing rows from empty model. `#2128 <https://github.com/mixxxdj/mixxx/pull/2128>`__
* Fix high DPI scaling of RGB overview waveforms. `#2090 <https://github.com/mixxxdj/mixxx/pull/2090>`__
* Fix for OpenGL SL detection on macOS. `#9653 <https://github.com/mixxxdj/mixxx/issues/9653>`__
* Fix OpenGL ES detection. `#9636 <https://github.com/mixxxdj/mixxx/issues/9636>`__
* Fix FX1/2 buttons missing Mic unit in Deere (64 samplers). `#9703 <https://github.com/mixxxdj/mixxx/issues/9703>`__
* Tango64: Re-enable 64 samplers. `#2223 <https://github.com/mixxxdj/mixxx/pull/2223>`__
* Numark DJ2Go re-enable note-off for deck A cue button. `#2087 <https://github.com/mixxxdj/mixxx/pull/2087>`__
* Replace Flanger with QuickEffect in keyboard mapping. `#2233 <https://github.com/mixxxdj/mixxx/pull/2233>`__

.. _v2-2-1:

`2.2.1 <https://launchpad.net/mixxx/+milestone/2.2.1>`__ (2019-04-22)
------------------------------------------------------------------------


* Include all fixes from Mixxx 2.1.7 and 2.1.8
* Fix high CPU usage on MAC due to preview column `#9574 <https://github.com/mixxxdj/mixxx/issues/9574>`__
* Fix HID controller output on Windows with common-hid-packet-parser.js
* Fix rendering slow down by not using QStylePainter in WSpinny `#8419 <https://github.com/mixxxdj/mixxx/issues/8419>`__
* Fix broken Mic mute button `#9387 <https://github.com/mixxxdj/mixxx/issues/9387>`__
* added quick effect enable button to the control picker menu
* Fix Cover Window close issue with empty cover arts
* Fix Numark Mixtrack 3 mapping. `#2057 <https://github.com/mixxxdj/mixxx/pull/2057>`__

.. _v2-2-0:

`2.2.0 <https://launchpad.net/mixxx/+milestone/2.2.0>`__ (2018-12-17)
------------------------------------------------------------------------

General
^^^^^^^


* Update from Qt4 to Qt5.
* Use Qt5's automatic high DPI scaling (and remove the old
  scaling option from the preferences).
* Vectorize remaining raster graphics for better HiDPI support.

Effects
^^^^^^^


* Add mix mode switch (Dry/Wet vs Dry+Wet) for effect units.
* Add support for LV2 effects plugins (currently no way to show plugin GUIs).
* Add preference option for selecting which effects are shown in the
  list of available effects in the main window (all LV2 effects are
  hidden by default and must be explicitly enabled by users).

Skins
^^^^^


* Add 8 sampler and small sampler options to LateNight.
* Add key / BPM expansion indicators to Deere decks.
* Add skin settings menu to LateNight.

Controllers
^^^^^^^^^^^


* Add controller mapping for Numark Mixtrack Platinum.
* Update controller mapping for Numark N4.
* Add spinback and break for Vestax VCI-400 mapping.

Miscellaneous
^^^^^^^^^^^^^


* Add preference option to adjust the play position marker of
  scrolling waveforms.
* Add preference option to adjust opacity of beatgrid markers on
  scrolling waveforms.
* Support IRC/AIM/ICQ broadcast metadata.

.. _v2-1-8:

`2.1.8 <https://launchpad.net/mixxx/+milestone/2.1.8>`__ (2019-04-07)
------------------------------------------------------------------------


* Fix a rare chance for a corrupt track file while writing metadata in out of disk situations. `lp:1815305 <https://bugs.launchpad.net/mixxx/+bug/1815305>`__
* Fix export of BPM track file metadata. `#9593 <https://github.com/mixxxdj/mixxx/issues/9593>`__
* Fix sending of broadcast metadata with TLS enabled libshout 2.4.1. `#9599 <https://github.com/mixxxdj/mixxx/issues/9599>`__
* Fix resdicovering purged tracks in all cases. `#9616 <https://github.com/mixxxdj/mixxx/issues/9616>`__
* Fix dropping track from OSX Finder. `#9620 <https://github.com/mixxxdj/mixxx/issues/9620>`__

.. _v2-1-7:

`2.1.7 <https://launchpad.net/mixxx/+milestone/2.1.7>`__ (2019-01-15)
------------------------------------------------------------------------


* Fix syncing to doublespeed `#9549 <https://github.com/mixxxdj/mixxx/issues/9549>`__
* Fix issues when changing beats of a synced track `#9550 <https://github.com/mixxxdj/mixxx/issues/9550>`__
* Fix direction of pitch bend buttons when inverting rate slider `#9284 <https://github.com/mixxxdj/mixxx/issues/9284>`__
* Use first loaded deck if no playing deck is found `#9397 <https://github.com/mixxxdj/mixxx/issues/9397>`__
* Encode file names correctly on macOS `lp:1776949 <https://bugs.launchpad.net/mixxx/+bug/1776949>`__

.. _v2-1-6:

`2.1.6 <https://launchpad.net/mixxx/+milestone/2.1.6>`__ (2018-12-23)
------------------------------------------------------------------------


* Fix crash when loading a Qt5 Soundsource / Vamp Plug-In. `#9324 <https://github.com/mixxxdj/mixxx/issues/9324>`__
* Validate effect parameter range. `lp:1795234 <https://bugs.launchpad.net/mixxx/+bug/1795234>`__
* Fix crash using the bpm_tap button without a track loaded. `#9512 <https://github.com/mixxxdj/mixxx/issues/9512>`__
* Fix possible crash after ejecting a track. `#9513 <https://github.com/mixxxdj/mixxx/issues/9513>`__
* Fix wrong bitrate reported for faulty mp3 files. `#9389 <https://github.com/mixxxdj/mixxx/issues/9389>`__
* Fix Echo effect syncing `#9442 <https://github.com/mixxxdj/mixxx/issues/9442>`__
* Fix iTunes context menu `#9484 <https://github.com/mixxxdj/mixxx/issues/9484>`__
* Fix loading the wrong track after delete search and scroll. `#9519 <https://github.com/mixxxdj/mixxx/issues/9519>`__
* Improve search bar timing. `#8665 <https://github.com/mixxxdj/mixxx/issues/8665>`__
* Fix quoted search sentence. `#9396 <https://github.com/mixxxdj/mixxx/issues/9396>`__
* Fix loading a track formerly not existing. `#9492 <https://github.com/mixxxdj/mixxx/issues/9492>`__
* Fix importing m3u files with blank lines. `#9535 <https://github.com/mixxxdj/mixxx/issues/9535>`__
* Fix position in sampler overview waveforms. `#9096 <https://github.com/mixxxdj/mixxx/issues/9096>`__
* Don't reset rate slider, syncing a track without a beatgrid. `#9391 <https://github.com/mixxxdj/mixxx/issues/9391>`__
* Clean up iTunes track context menu. `#9488 <https://github.com/mixxxdj/mixxx/issues/9488>`__
* Collapsed sampler are not analyzed on startup. `#9502 <https://github.com/mixxxdj/mixxx/issues/9502>`__
* search for decoration characters like "˚". `#9517 <https://github.com/mixxxdj/mixxx/issues/9517>`__
* Fix cue button blinking after pressing eject on an empty deck. `#9543 <https://github.com/mixxxdj/mixxx/issues/9543>`__

.. _v2-1-5:

`2.1.5 <https://launchpad.net/mixxx/+milestone/2.1.5>`__ (2018-10-28)
------------------------------------------------------------------------


* Code signing for Windows builds. `#8309 <https://github.com/mixxxdj/mixxx/issues/8309>`__
* Fix crash on exit when preferences is open. `#9438 <https://github.com/mixxxdj/mixxx/issues/9438>`__
* Fix crash when analyzing corrupt MP3s. `#9443 <https://github.com/mixxxdj/mixxx/issues/9443>`__
* Fix crash when importing metadata from MusicBrainz. `#9456 <https://github.com/mixxxdj/mixxx/issues/9456>`__
* Library search fixes when single quotes are used. `#9395 <https://github.com/mixxxdj/mixxx/issues/9395>`__ `#9419 <https://github.com/mixxxdj/mixxx/issues/9419>`__
* Fix scrolling waveform on Windows with WDM-KS sound API. `lp:1729345 <https://bugs.launchpad.net/mixxx/+bug/1729345>`__
* Fix right clicking on beatgrid alignment button in Tango and LateNight skins. `#9471 <https://github.com/mixxxdj/mixxx/issues/9471>`__
* Improve speed of importing iTunes library. `#9400 <https://github.com/mixxxdj/mixxx/issues/9400>`__
* Add 2 deck mapping for DJTechTools MIDI Fighter Twister.

.. _v2-1-4:

`2.1.4 <https://launchpad.net/mixxx/+milestone/2.1.4>`__ (2018-08-29)
------------------------------------------------------------------------

Fix track selection not getting shown in the track
table on Windows. There are no changes to the
source code, but the Jenkins build configuration
was changed to delete the Jenkins workspace before
each build. `lp:1751482 <https://bugs.launchpad.net/mixxx/+bug/1751482>`__

.. _v2-1-3:

`2.1.3 <https://launchpad.net/mixxx/+milestone/2.1.3>`__ (2018-08-20)
------------------------------------------------------------------------

Fix a severe performance regression on Windows:
`Mixxx 2.1.2 running much slower than 2.1.1 <https://mixxx.org/forums/viewtopic.php?f=3&t=12082>`_

.. _v2-1-2:

`2.1.2 <https://launchpad.net/mixxx/+milestone/2.1.2>`__ (2018-08-10)
------------------------------------------------------------------------

Yet another bugfix release of Mixxx 2.1.
Here is a quick summary of what is new in Mixxx 2.1.2:


* Allow maximum deck speed of 4x normal.
* Don't always quantize hotcues, a 2.1.1 regression. `#9345 <https://github.com/mixxxdj/mixxx/issues/9345>`__
* Fix artifacts using more than 32 samplers. `#9363 <https://github.com/mixxxdj/mixxx/issues/9363>`__
* store No EQ and Filter persistently. `#9376 <https://github.com/mixxxdj/mixxx/issues/9376>`__
* Pad unreadable samples with silence on cache miss. `#9346 <https://github.com/mixxxdj/mixxx/issues/9346>`__
* Fixing painting of preview column for Qt5 builds. `#9337 <https://github.com/mixxxdj/mixxx/issues/9337>`__
* LateNight: Fix play button right click. `#9384 <https://github.com/mixxxdj/mixxx/issues/9384>`__
* LateNight: Added missing sort up/down buttons.
* Fix sampler play button tooltips. `#9358 <https://github.com/mixxxdj/mixxx/issues/9358>`__
* Shade: remove superfluid margins and padding in sampler.xml. `#9310 <https://github.com/mixxxdj/mixxx/issues/9310>`__
* Deere: Fix background-color code.
* ITunes: Don't stop import in case of duplicated Playlists. `#9394 <https://github.com/mixxxdj/mixxx/issues/9394>`__

.. _v2-1-1:

`2.1.1 <https://launchpad.net/mixxx/+milestone/2.1.1>`__ (2018-06-13)
------------------------------------------------------------------------

After two months it is time to do a bugfix release of Mixxx 2.1.
Here is a quick summary of what is new in Mixxx 2.1.1:


* Require Soundtouch 2.0 to avoid segfault. `#8534 <https://github.com/mixxxdj/mixxx/issues/8534>`__
* Improved skins including library view fix. `#9317 <https://github.com/mixxxdj/mixxx/issues/9317>`__ `#9297 <https://github.com/mixxxdj/mixxx/issues/9297>`__ `#9239 <https://github.com/mixxxdj/mixxx/issues/9239>`__
* Fix crash when importing ID3v2 APIC frames. `#9325 <https://github.com/mixxxdj/mixxx/issues/9325>`__
* Synchronize execution of Vamp analyzers. `#9085 <https://github.com/mixxxdj/mixxx/issues/9085>`__
* DlgTrackInfo: Mismatching signal/slot connection.
* Detect M4A decoding errors on Windows. `#9266 <https://github.com/mixxxdj/mixxx/issues/9266>`__
* Fix spinback inertia effect.
* Fix decoding fixes and upgrade DB schema. `#9255 <https://github.com/mixxxdj/mixxx/issues/9255>`__ `#9275 <https://github.com/mixxxdj/mixxx/issues/9275>`__
* Fix integration of external track libraries. `#9264 <https://github.com/mixxxdj/mixxx/issues/9264>`__
* Fix memory leak when loading cover art. `#9267 <https://github.com/mixxxdj/mixxx/issues/9267>`__
* Fix clearing of ReplayGain gain/ratio in file tags. `#9256 <https://github.com/mixxxdj/mixxx/issues/9256>`__
* Fix crash when removing a quick link. `#8270 <https://github.com/mixxxdj/mixxx/issues/8270>`__
* Fidlib: Thread-safe and reentrant generation of filters. `#9247 <https://github.com/mixxxdj/mixxx/issues/9247>`__
* Fix unresponsive scrolling through crates & playlists using encoder. `#8941 <https://github.com/mixxxdj/mixxx/issues/8941>`__
* Swap default values for temp/perm rate changes. `#9243 <https://github.com/mixxxdj/mixxx/issues/9243>`__

.. _v2-1-0:

`2.1.0 <https://launchpad.net/mixxx/+milestone/2.1.0>`__ (2018-04-15)
------------------------------------------------------------------------

After two years of hard work, we are pleased to announce Mixxx 2.1. We
have overhauled the effects system, redesigned the skins, added and improved
lots of controller mappings, rewrote the audio file decoders twice, and of
course fixed a bunch of bugs. Download it!

Here is a quick summary of what is new in Mixxx 2.1.0:


* Graphical interface scales for high resolution screens
* Overhauled Deere and LateNight skins
* New Tango skin
* Effects are synchronized to the tempo
* Effects are processed post-fader and post-crossfader and can be previewed in headphones
* One metaknob per effect with customizable parameter control for intuitive use of effect chains
* Nine new effects: Autopan, Biquad Equalizer, Biquad Full Kill Equalizer, Loudness Contour, Metronome, Parametric Equalizer, Phaser, Stereo Balance, Tremolo
* Loaded effects and their parameters are saved and restored when Mixxx restarts
* More transparent sounding equalizers (Biquad Equalizer and Biquad Full Kill Equalizer)
* Improved scratching sounds with jog wheels, vinyl control, and dragging waveforms with the mouse
* Simplified looping and beatjump controls
* Configurable rows of 8 samplers with up to 8 rows available for a total of 64 samplers
* Files loaded to samplers are reloaded when Mixxx restarts
* Improved volume normalization algorithm (EBU-R 128)
* Filter library table by crates
* Sort musical keys in library table by circle of fifths
* Write metadata tags back to audio files
* New JavaScript library for controller mapping
* Configure multiple Internet broadcasting stations and use multiple stations at the same time
* Broadcast and record microphones with direct monitoring and latency compensation
* Broadcast and record from an external mixer
* Booth output with independent gain knob for using sound cards with 6 output channels without an external mixer
* Prevent screensaver from starting while Mixxx is running
* CUP (Cue And Play) cue button mode
* Time remaining and time elapsed now take into account the tempo fader
* Clicking cover art now shows it full size in a separate window
* and of course, lots and lots of bug fixes.

Here are controllers with mappings that have been added or updated since the 2.0
release. Mappings marked with an asterisk (*) have been updated for the new
effects interface:


* American Audio VMS2
* American Audio VMS4
* Allen & Heath Xone K2/K1*
* Behringer CMD Micro
* Behringer CMD MM1*
* Behringer CMD Studio 4a
* Denon MC4000*
* Denon MC6000 Mk2*
* FaderFox DJ2
* Hercules DJ Console 4-Mx*
* Hercules DJ Control MP3 LE / Glow
* Hercules DJ Control Compact
* Hercules P32*
* Ion Discover DJ
* Korg Nanokontrol 2
* Korg KAOSS DJ
* M-Audio Xponent
* Native Instruments Traktor Kontrol S4 Mk2*
* Novation Launchpad Mk1 & Mk2
* Novation Twitch
* Numark Mixtrack Pro 3 & Numark Mixtrack 3*
* Pioneer DDJ-SB2*
* Pioneer DDJ-SX*
* Reloop Beatmix 2
* Reloop Beatmix 4
* Reloop Digital Jockey 3 ME
* Reloop Terminal Mix 2
* Reloop Terminal Mix 4
* Vestax VCI-100 Mk2
* Vestax Typhoon

For users upgrading from older versions of Mixxx, we have a few important
announcements. First, if you are using Windows, you will have to uninstall any
old versions of Mixxx before you can install 2.1. How to uninstall Mixxx
varies on different versions of Windows:


* Windows Vista, 7, and 8: `Start > Control Panel > Programs > Uninstall a
  Program <https://support.microsoft.com/en-us/help/2601726>`_
* Windows 10: `Start > Control Panel > Programs > Programs And Features >
  look for Mixxx > Uninstall <https://support.microsoft.com/en-gb/help/4028054/windows-repair-or-remove-programs-in-windows-10>`_

If you are upgrading from an older version of Mixxx and have MP3 files in
your library, we have another important announcement. The good news is that we
fixed a bug where the waveforms and audio playback of MP3 files were
misaligned. The bad news is that we have no way of knowing which MP3 files were
affected or how much the offset was. That means that waveforms, beatgrids,
cues, and loops from older versions of Mixxx may be offset by an unknown amount
for any MP3 file. Only MP3 files were affected by this bug; other audio file
types are unaffected. You can either correct your beatgrids and cue points
manually for each track, or you can clear this information for all MP3s and
start fresh. Regardless, we recommend clearing the waveforms for all MP3
files. To clear these, type "location:mp3" into the library search bar, press
Control + A to select all tracks, right click, and select the information you
want to clear from the menu.

In the works for Mixxx 2.2, we have a big redesign of the library GUI. Along
with that will come saving & restoring search queries plus nested crates.
We are also planning on adding support for saving and loading custom effect
chain presets with the ability to import and export them to share online.

Want to help make Mixxx even more awesome? The biggest thing we need is more
people. You do not need to be a programmer to help out. Giving feedback on the
design of new features as they are being made is very valuable. Refer to the
Testing page on the wiki for more information on how to get involved with that.
Reporting bugs and telling us your ideas on the Launchpad bug tracker is a big
help too! We cannot fix problems we do not know about, so please let us know if
you find any issues with Mixxx. If you would like to help translate Mixxx into
another language, refer to the Internationalization wiki page.  Of course, more
programmers could always help. Read the Developer Documentation on the wiki for
tips on getting started contributing code to Mixxx.

We hope you have as much fun with Mixxx as we do!

For a full list of new features and bugfixes, check out the
`2.1.0 milestone on Launchpad <https://launchpad.net/mixxx/+milestone/2.1.0>`_.

.. _v2-0-0:

`2.0.0 <https://launchpad.net/mixxx/+milestone/2.0.0>`__ (2015-12-31)
------------------------------------------------------------------------


* 4 Decks with Master Sync
* New Effects Framework with 4 Effect Units and 5 Built-in Effects:

  * Flanger, Bit Crusher, Reverb, Echo, Filter
  * More to come!

* Configurable, Resizable User Interface with 3 Brand New Skins
* Cover Art Display
* Music Key Detection and Shifting
* Vinyl Audio Pass-Through
* 4 Microphone inputs and 4 Auxiliary inputs
* MIDI Mapping GUI and Improved Learning Wizard
* MusicBrainz metadata fetching
* RGB Musical Waveforms
* Hundreds of Bug Fixes and Improvements
* New Pitch-Independent Algorithm for Better-Sounding Key-lock

For a full list of new features and bugfixes, check out the
`2.0.0 milestone on Launchpad <https://launchpad.net/mixxx/+milestone/2.0.0>`_.


.. seealso:: For an overview of previous versions, `take a look
             <https://launchpad.net/mixxx/+series>`_ at the timeline.
