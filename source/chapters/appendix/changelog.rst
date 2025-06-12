.. This is a generated file. Do not edit it manually, because it is updated
   automatically via tools/update_changelog.py.

.. include:: /shortcuts.rstext

.. _appendix-changelog:


Changelog
=========

.. _v2-5-2:

`2.5.2 <https://github.com/mixxxdj/mixxx/milestone/49>`__ (unreleased)
-------------------------------------------------------------------------

Library
^^^^^^^


* Fix playlist export when name contains a dot `#14737 <https://github.com/mixxxdj/mixxx/pull/14737>`__
* Fix loading the wrong track via drag and drop when using symlinks
  `#13708 <https://github.com/mixxxdj/mixxx/pull/13708>`__
  `#13706 <https://github.com/mixxxdj/mixxx/issues/13706>`__
* Fix: byte order in hotcue comments imported from rekordbox
  `#14808 <https://github.com/mixxxdj/mixxx/pull/14808>`__
  `#14789 <https://github.com/mixxxdj/mixxx/issues/14789>`__
* Tracks table: show ReplayGain with max. 2 decimals, full precision in tooltip
  `#14868 <https://github.com/mixxxdj/mixxx/pull/14868>`__
  `#14867 <https://github.com/mixxxdj/mixxx/issues/14867>`__
* Fix keyboard mappings with non-ASCII characters on Linux
  `#14843 <https://github.com/mixxxdj/mixxx/pull/14843>`__
  `#14734 <https://github.com/mixxxdj/mixxx/issues/14734>`__
* Computer feature: enable initial sorting during population `#14688 <https://github.com/mixxxdj/mixxx/pull/14688>`__
* Computer feature: avoid false-positve 'has children' for non-directory links
  `#14907 <https://github.com/mixxxdj/mixxx/pull/14907>`__
* Fix column header mapping when using external library `#13782 <https://github.com/mixxxdj/mixxx/pull/13782>`__
* Fixed Single track cover reload on reload metadata from file
  `#14494 <https://github.com/mixxxdj/mixxx/pull/14494>`__
  `#14409 <https://github.com/mixxxdj/mixxx/issues/14409>`__

Controller Mappings
^^^^^^^^^^^^^^^^^^^


* Arturia KeyLab Mk1: initial mapping `#14502 <https://github.com/mixxxdj/mixxx/pull/14502>`__
* Denon MC7000: slicer mode TypeError `#14804 <https://github.com/mixxxdj/mixxx/pull/14804>`__
* Denon MC7000: crossfader curve using wrong parameter `#14803 <https://github.com/mixxxdj/mixxx/pull/14803>`__
* DJ TechTools MIDI Fighter Twister: support 4 decks `#14557 <https://github.com/mixxxdj/mixxx/pull/14557>`__
* Hercules DJControl Inpulse 500: the crossfader was not reaching 100% to the right end
  `#14722 <https://github.com/mixxxdj/mixxx/pull/14722>`__
* Icon Pro Audio iControls: initial mapping `#14591 <https://github.com/mixxxdj/mixxx/pull/14591>`__
* Numark Mixtrack Platinium FX: Fix 4 steps browsing issue `#14778 <https://github.com/mixxxdj/mixxx/pull/14778>`__
* Traktor Kontrol S3: Use GUI config for settings `#14904 <https://github.com/mixxxdj/mixxx/pull/14904>`__
* Traktor S2 MK3: Fixed LED issue `#14717 <https://github.com/mixxxdj/mixxx/pull/14717>`__
* Traktor S4 MK2: Use engine settings API for configuration `#14781 <https://github.com/mixxxdj/mixxx/pull/14781>`__
* Traktor S4 MK3: prevent sync lockup, add setting for tempo center snap
  `#14735 <https://github.com/mixxxdj/mixxx/pull/14735>`__
  `#14721 <https://github.com/mixxxdj/mixxx/issues/14721>`__

Controller Backend
^^^^^^^^^^^^^^^^^^


* Control picker: Allow to learn MIDI Aux/Mic enable controls
  `#14720 <https://github.com/mixxxdj/mixxx/pull/14720>`__
  `#14718 <https://github.com/mixxxdj/mixxx/issues/14718>`__
* Make ``[Main],headSplit`` CO persistent across restart `#14817 <https://github.com/mixxxdj/mixxx/pull/14817>`__
* Fix MIDI Controller button learning
  `#14816 <https://github.com/mixxxdj/mixxx/pull/14816>`__
  `#14805 <https://github.com/mixxxdj/mixxx/issues/14805>`__
* Fix learning with "No Mapping" selected `#14829 <https://github.com/mixxxdj/mixxx/pull/14829>`__
* Unit tests for engine.beginTimer `#12437 <https://github.com/mixxxdj/mixxx/pull/12437>`__
* engine-api.d.ts: brake()/spinback() documentation
  `#14929 <https://github.com/mixxxdj/mixxx/pull/14929>`__

Target support
^^^^^^^^^^^^^^


* Fix building with a CMake multi-config setup `#14614 <https://github.com/mixxxdj/mixxx/pull/14614>`__
* Fix building with gcc >= 14 with LTO and clang >= 19 (fpclassify)
  `#14749 <https://github.com/mixxxdj/mixxx/pull/14749>`__
  `#14716 <https://github.com/mixxxdj/mixxx/issues/14716>`__
* Fix: gcc ``-Warray-bounds=`` in fidlib by using a flexible member `#14798 <https://github.com/mixxxdj/mixxx/pull/14798>`__
* Added Linux Mint Codenames to debian_buildenv.sh `#14709 <https://github.com/mixxxdj/mixxx/pull/14709>`__
* Add hidden ``[Config],notify_max_dbg_time`` setting to reduce warnings in developer mode `#14015 <https://github.com/mixxxdj/mixxx/pull/14015>`__
* Detect arch and fail early if not supported when installing buildenv `#14478 <https://github.com/mixxxdj/mixxx/pull/14478>`__

Misc
^^^^


* Vinyl Control: Reduce sticker drift `#14435 <https://github.com/mixxxdj/mixxx/pull/14435>`__
* Fix infinite number of pop ups of the "No Vinyl|Mic|Aux|Passthrough input configured" dialog
  `#14841 <https://github.com/mixxxdj/mixxx/pull/14841>`__
  `#14837 <https://github.com/mixxxdj/mixxx/issues/14837>`__
* Reduce CPU usage with Trace log messages
  `#14862 <https://github.com/mixxxdj/mixxx/pull/14862>`__
  `#14791 <https://github.com/mixxxdj/mixxx/issues/14791>`__
* Fix adjust Gain after adopting it as ReplayGain only in requesting player
  `#14812 <https://github.com/mixxxdj/mixxx/pull/14812>`__
  `#14806 <https://github.com/mixxxdj/mixxx/pull/14806>`__
* Skins: add loop anchor toggle to Deere, Shade, Tango
  `#14890 <https://github.com/mixxxdj/mixxx/pull/14890>`__
  `#14173 <https://github.com/mixxxdj/mixxx/issues/14173>`__
* Sound Hardware preferences: add manual link for Mic monitoring modes
  `#14889 <https://github.com/mixxxdj/mixxx/pull/14889>`__
* Work around an Ubuntu, Ibus or Qt issue regarding detecting the current keyboard layout.
  `#14883 <https://github.com/mixxxdj/mixxx/pull/14883>`__
  `#14838 <https://github.com/mixxxdj/mixxx/issues/14838>`__
  `#14797 <https://github.com/mixxxdj/mixxx/issues/14797>`__
* Fix BPM rounding for the 3/2 case `#14751 <https://github.com/mixxxdj/mixxx/pull/14751>`__
* Update cue & play indicators on paused decks when switching cue mode
  `14930 <https://github.com/mixxxdj/mixxx/pull/14930>`__
  `9928 <https://github.com/mixxxdj/mixxx/issues/9928>`__

.. _v2-5-1:

`2.5.1 <https://github.com/mixxxdj/mixxx/milestone/45>`__ (2025-04-27)
-------------------------------------------------------------------------

Controller Mappings
^^^^^^^^^^^^^^^^^^^


* Behringer DDM4000 & BCR2000: Update mappings to 2.5
  `#14232 <https://github.com/mixxxdj/mixxx/pull/14232>`__
  `#14349 <https://github.com/mixxxdj/mixxx/pull/14349>`__
* DJ TechTools MIDI Fighter Spectra: Add controller mapping
  `#14559 <https://github.com/mixxxdj/mixxx/pull/14559>`__
* Hercules DJControl Inpulse 300: add toneplay, slicer, and beatmatch functionalities
  `#14051 <https://github.com/mixxxdj/mixxx/pull/14051>`__
  `#14057 <https://github.com/mixxxdj/mixxx/pull/14057>`__
* Hercules DJControl Inpulse 500: New mapping
  `#14491 <https://github.com/mixxxdj/mixxx/pull/14491>`__
  `#14510 <https://github.com/mixxxdj/mixxx/pull/14510>`__
* Hercules DJ Console Mk1: Fix pitch bend buttons `#14447 <https://github.com/mixxxdj/mixxx/pull/14447>`__
* M-Vave SMC-Mixer: Add controller mapping
  `#14411 <https://github.com/mixxxdj/mixxx/pull/14411>`__
  `#14448 <https://github.com/mixxxdj/mixxx/pull/14448>`__
  `#14457 <https://github.com/mixxxdj/mixxx/pull/14457>`__
  `#14458 <https://github.com/mixxxdj/mixxx/pull/14458>`__
* M-Vave SMK-25 II: Piano keyboard mapping
  `#14412 <https://github.com/mixxxdj/mixxx/pull/14412>`__
  `#14484 <https://github.com/mixxxdj/mixxx/pull/14484>`__
* Numark Mixtrack Platinum: Fix VU Meters `#14575 <https://github.com/mixxxdj/mixxx/pull/14575>`__
* Numark NS6II: New mapping `#11075 <https://github.com/mixxxdj/mixxx/pull/11075>`__
* Numark Platinum FX: New mapping `#12872 <https://github.com/mixxxdj/mixxx/pull/12872>`__
* Pioneer-DDJ-SB3: Fixes slip mode and adds missing knob controls `#11307 <https://github.com/mixxxdj/mixxx/pull/11307>`__
* Reloop Digital Jockey 2 IE: New mapping
  `#4614 <https://github.com/mixxxdj/mixxx/pull/4614>`__
  `#14328 <https://github.com/mixxxdj/mixxx/pull/14328>`__
* Traktor S4mk3: Set 4 decks, avoid CO warnings for decks 3/4, eg. VU meter
  `#14249 <https://github.com/mixxxdj/mixxx/pull/14249>`__
* Traktor S4mk3: Smooth xfader curve for Const Power mode
  `#14305 <https://github.com/mixxxdj/mixxx/pull/14305>`__
  `#14329 <https://github.com/mixxxdj/mixxx/pull/14329>`__
  `#14103 <https://github.com/mixxxdj/mixxx/issues/14103>`__
* Traktor S4mk3: stop wheel led blinking when track is over/stopped
  `#14028 <https://github.com/mixxxdj/mixxx/pull/14028>`__
  `#13995 <https://github.com/mixxxdj/mixxx/issues/13995>`__
* Traktor Kontrol S3: Use pitch absolute mode as described in the manual `#14123 <https://github.com/mixxxdj/mixxx/pull/14123>`__
* Stanton SCS.1m/d; Keith McMillen QuNeo; EKS Otus: use ``playposition`` instead of non-existent ``visual_playposition``
  `#14609 <https://github.com/mixxxdj/mixxx/pull/14609>`__
  `#14603 <https://github.com/mixxxdj/mixxx/issues/14603>`__

Controller Backend
^^^^^^^^^^^^^^^^^^


* Controllers: Avoid timer warning on button release `#14323 <https://github.com/mixxxdj/mixxx/pull/14323>`__
* Controller preferences: Fix notify of pending changes when closing preferences `#14234 <https://github.com/mixxxdj/mixxx/pull/14234>`__
  `#14220 <https://github.com/mixxxdj/mixxx/issues/14220>`__
* Controller preferences: Fix broken overwrite dialog ('Save as..' not working) `#14263 <https://github.com/mixxxdj/mixxx/pull/14263>`__
* Controller preferences: Don't break support link texts `#14079 <https://github.com/mixxxdj/mixxx/pull/14079>`__
* Controller preferences: Fix wrong mapping change confirmation request caused by MidiController::makeInputHandler()
  `#14281 <https://github.com/mixxxdj/mixxx/pull/14281>`__
  `#14280 <https://github.com/mixxxdj/mixxx/issues/14280>`__
  `#14292 <https://github.com/mixxxdj/mixxx/pull/14292>`__
* Controller mapping info: Fix cropped description text
  `#14332 <https://github.com/mixxxdj/mixxx/pull/14332>`__
  `#14117 <https://github.com/mixxxdj/mixxx/issues/14117>`__
* MIDI controller learning: Make control box search usable `#14260 <https://github.com/mixxxdj/mixxx/pull/14260>`__
* MIDI controller learning: Don't reload mapping after learn `#14253 <https://github.com/mixxxdj/mixxx/pull/14253>`__
* MIDI controller learning: Correct skin control for mic/aux section `#14221 <https://github.com/mixxxdj/mixxx/pull/14221>`__
* MIDI controller learning: Add more cue controls for samplers
  `#14419 <https://github.com/mixxxdj/mixxx/pull/14419>`__
* MIDI controller learning: Continue after the maximum learning time is over `#14429 <https://github.com/mixxxdj/mixxx/pull/14429>`__
* Allow ``midino`` 0 in `MidiController::makeInputHandler()
  `#14266 <https://github.com/mixxxdj/mixxx/pull/14266>`__
  `#14265 <https://github.com/mixxxdj/mixxx/issues/14265>`__
* Fix: provide ``incomingData`` to MIDI sysex mappings
  `#14368 <https://github.com/mixxxdj/mixxx/pull/14368>`__
  `#13133 <https://github.com/mixxxdj/mixxx/issues/13133>`__
* Fix log spam when using Midi for light mapping
  `#14326 <https://github.com/mixxxdj/mixxx/issues/14326>`__
  `#14327 <https://github.com/mixxxdj/mixxx/pull/14327>`__
  `#14333 <https://github.com/mixxxdj/mixxx/pull/14333>`__
  `#14338 <https://github.com/mixxxdj/mixxx/pull/14338>`__
  `#14371 <https://github.com/mixxxdj/mixxx/pull/14371>`__
* Fix for ``TypeError`` in ``midi-components-0.0.js``
  `#14203 <https://github.com/mixxxdj/mixxx/pull/14203>`__
  `#14197 <https://github.com/mixxxdj/mixxx/issues/14197>`__
* Fix crash due to concurrent access in MidiController `#14159 <https://github.com/mixxxdj/mixxx/pull/14159>`__

Skins
^^^^^


* Deere/LateNight (64 samplers): Bring back library in regular view
  `#14101 <https://github.com/mixxxdj/mixxx/pull/14101>`__
  `#14097 <https://github.com/mixxxdj/mixxx/issues/14097>`__
  `#14700 <https://github.com/mixxxdj/mixxx/issues/14700>`__
* Fix crash when hiding waveforms in Deere
  `#14170 <https://github.com/mixxxdj/mixxx/pull/14170>`__
* Waveform Overview: Abort play pos dragging if cursor is released outside the valid area
  `#13741 <https://github.com/mixxxdj/mixxx/pull/13741>`__
  `#13732 <https://github.com/mixxxdj/mixxx/issues/13732>`__
* Waveform Overview: Also render analysis progress when triggered by track menu or analysis feature `#14150 <https://github.com/mixxxdj/mixxx/pull/14150>`__
* Don't show 'menubar hide' dialog when switching skins `#14254 <https://github.com/mixxxdj/mixxx/pull/14254>`__
* Key Wheel: Move to View menu and make it a floating tool window
  `#14256 <https://github.com/mixxxdj/mixxx/pull/14256>`__
  `#14239 <https://github.com/mixxxdj/mixxx/pull/14239>`__
* Center effect parameter names `#14598 <https://github.com/mixxxdj/mixxx/pull/14598>`__
* Track menu: highlight row when hovering checkbox
  `#14636 <https://github.com/mixxxdj/mixxx/pull/14636>`__
  `#14680 <https://github.com/mixxxdj/mixxx/pull/14680>`__

Library
^^^^^^^


* Add Ctrl+Shift+C to copy the content of the selected cell(s) (The Mxxx 2.4 behaviour of Ctrl+C).
  `#14114 <https://github.com/mixxxdj/mixxx/pull/14114>`__
  `#14065 <https://github.com/mixxxdj/mixxx/issues/14065>`__
* Fix MusicBrainz lookup on Windows and macOS `#14216 <https://github.com/mixxxdj/mixxx/pull/14216>`__
* Library scanner: Update cached 'missing' flag when file is redicovered
  `#14250 <https://github.com/mixxxdj/mixxx/pull/14250>`__
* Hidden Tracks: Allow 'load to' via track context manu `#14077 <https://github.com/mixxxdj/mixxx/pull/14077>`__
* Update to libdjinterop 0.24.3 - support for Engine 4.1/4.2
  `#14172 <https://github.com/mixxxdj/mixxx/pull/14172>`__
  `#14289 <https://github.com/mixxxdj/mixxx/pull/14289>`__
* Fix writing metadata via symlink `#13711 <https://github.com/mixxxdj/mixxx/pull/13711>`__
* Library menu: change "Engine DJ Prime" to "Engine DJ"
  `#14248 <https://github.com/mixxxdj/mixxx/pull/14248>`__
  `#14682 <https://github.com/mixxxdj/mixxx/pull/14682>`__
* Fix file extension handling during playlist export `#14381 <https://github.com/mixxxdj/mixxx/pull/14381>`__
* Fix manual key metadata editing in track properties dialog
  `#14022 <https://github.com/mixxxdj/mixxx/pull/14022>`__
  `#14400 <https://github.com/mixxxdj/mixxx/issues/14400>`__
  `#14295 <https://github.com/mixxxdj/mixxx/pull/14295>`__
  `#14294 <https://github.com/mixxxdj/mixxx/issues/14294>`__
* History: Don't allow joining with locked previous playlist
  `#14401 <https://github.com/mixxxdj/mixxx/pull/14401>`__
  `#14399 <https://github.com/mixxxdj/mixxx/issues/14399>`__
* Track info dialog: fixed cover label (max) size `#14418 <https://github.com/mixxxdj/mixxx/pull/14418>`__
* Track Menu: Reset ``eject`` after moving track file to trash `#14402 <https://github.com/mixxxdj/mixxx/pull/14402>`__
* Fix AutoDJ "Remove Crate" action
  `#14426 <https://github.com/mixxxdj/mixxx/pull/14426>`__
  `#14425 <https://github.com/mixxxdj/mixxx/issues/14425>`__
* Fix scrolling issue with coverart columns visible
  `#13719 <https://github.com/mixxxdj/mixxx/pull/13719>`__
  `#14631 <https://github.com/mixxxdj/mixxx/pull/14631>`__
* Developer Tools: multi-word search, no Tab navigation in controls table `#14474 <https://github.com/mixxxdj/mixxx/pull/14474>`__
* Analyze feature: respect New / All selection when searching
  `#14660 <https://github.com/mixxxdj/mixxx/pull/14660>`__
  `#14659 <https://github.com/mixxxdj/mixxx/issues/14659>`__
* Stop populating Computer library feature when Mixxx should close `#14573 <https://github.com/mixxxdj/mixxx/pull/14573>`__
* Tracks: apply played/missing text color also to selected tracks `#13583 <https://github.com/mixxxdj/mixxx/pull/13583>`__
* Tracks: ``show_track_menu`` at index position `#14385 <https://github.com/mixxxdj/mixxx/pull/14385>`__
* Search related menu: improve checkbox click UX `#14637 <https://github.com/mixxxdj/mixxx/pull/14637>`__
* Avoid false missing tracks due to db inconsistency
  `#14615 <https://github.com/mixxxdj/mixxx/pull/14615>`__
  `#14513 <https://github.com/mixxxdj/mixxx/issues/14513>`__
* Fix automatic trimming of search bar text
  `#14497 <https://github.com/mixxxdj/mixxx/pull/14497>`__
  `#14486 <https://github.com/mixxxdj/mixxx/issues/14486>`__
* Avoid crash after removing Quick Link
  `#14556 <https://github.com/mixxxdj/mixxx/pull/14556>`__
  `#8270 <https://github.com/mixxxdj/mixxx/issues/8270>`__

Other Fixes
^^^^^^^^^^^


* Enable R3 time-stretching with Rubberband 4.0.0 API version numbers `#14100 <https://github.com/mixxxdj/mixxx/pull/14100>`__
* Preferences Effects: add Hide/Unhide (move) buttons to Effects tab `#13329 <https://github.com/mixxxdj/mixxx/pull/13329>`__
* Preferences Effects: left/right key in effect lists trigger hide/unhide `#14205 <https://github.com/mixxxdj/mixxx/pull/14205>`__
* Fix beat sync in Flanger effect `#14351 <https://github.com/mixxxdj/mixxx/pull/14351>`__
* Apply talkover ducking after main effects to allow using a compressor effect
  `#13844 <https://github.com/mixxxdj/mixxx/pull/13844>`__
  `#12451 <https://github.com/mixxxdj/mixxx/issues/12451>`__
* Fix sporadic deadlocks when closing Mixxx or changing sound devices
  `#14208 <https://github.com/mixxxdj/mixxx/pull/14208>`__
  `#14055 <https://github.com/mixxxdj/mixxx/issues/14055>`__
* PositionScratchController: Fix loop wrap-around case `#14379 <https://github.com/mixxxdj/mixxx/pull/14379>`__
* Allow seeking to a hotcue during waveform scratching
  `#14357 <https://github.com/mixxxdj/mixxx/pull/14357>`__
  `#13981 <https://github.com/mixxxdj/mixxx/issues/13981>`__
* Reset saved loop when toggling off after switching cue type
  `#14661 <https://github.com/mixxxdj/mixxx/pull/14661>`__
  `#14657 <https://github.com/mixxxdj/mixxx/issues/14657>`__
* Fix leaks from fid_design()
  `#14567 <https://github.com/mixxxdj/mixxx/pull/14567>`__
  `#9470 <https://github.com/mixxxdj/mixxx/issues/9470>`__

Target support
^^^^^^^^^^^^^^


* Allow to build with git "showSignature = true"
  `#14115 <https://github.com/mixxxdj/mixxx/pull/14115>`__
  `#12997 <https://github.com/mixxxdj/mixxx/issues/12997>`__
* Support building with Qt 6.8/6.9
  `#14080 <https://github.com/mixxxdj/mixxx/pull/14080>`__
  `#14071 <https://github.com/mixxxdj/mixxx/issues/14071>`__
  `#14200 <https://github.com/mixxxdj/mixxx/pull/14200>`__
  `#14204 <https://github.com/mixxxdj/mixxx/pull/14204>`__
  `#14440 <https://github.com/mixxxdj/mixxx/pull/14440>`__
  `#14518 <https://github.com/mixxxdj/mixxx/pull/14518>`__
* Welcome Ubuntu Plucky Puffin; Good bye Mantic Minotaur
  `#14148 <https://github.com/mixxxdj/mixxx/pull/14148>`__
  `#14158 <https://github.com/mixxxdj/mixxx/pull/14158>`__
* Add more translations to Linux desktop file
  `#14153 <https://github.com/mixxxdj/mixxx/pull/14153>`__
  `#14169 <https://github.com/mixxxdj/mixxx/pull/14169>`__
* Debian: recommend qt6-translations-l10n `#14147 <https://github.com/mixxxdj/mixxx/pull/14147>`__
* Update FindFFTW3.cmake to not find version 2
  `#13937 <https://github.com/mixxxdj/mixxx/pull/13937>`__
  `#13931 <https://github.com/mixxxdj/mixxx/issues/13931>`__
* Allow building without tests-tools via new CMake options BUILD_TESTING and BUILD_BENCH
  `#14269 <https://github.com/mixxxdj/mixxx/pull/14269>`__
* Fix and improve "missing env" error message `#14321 <https://github.com/mixxxdj/mixxx/pull/14321>`__
* Qt 6.8: Ensure Mixxx uses "windowsvista" Qt style on Windows `#14228 <https://github.com/mixxxdj/mixxx/pull/14228>`__
* Raise macOS target version to 11 (Qt 6.5 requirement). `#14440 <https://github.com/mixxxdj/mixxx/pull/14440>`__
* Fail early when building on WSL `#14481 <https://github.com/mixxxdj/mixxx/pull/14481>`__
* Remove useless udev rule `#14630 <https://github.com/mixxxdj/mixxx/pull/14630>`__
* Handle new " / " from taglib 2.0
  `#12854 <https://github.com/mixxxdj/mixxx/pull/12854>`__
  `#12790 <https://github.com/mixxxdj/mixxx/issues/12790>`__

.. _v2-5-0:

`2.5.0 <https://github.com/mixxxdj/mixxx/issues?q=milestone%3A2.5.0>`__ (2024-12-24)
---------------------------------------------------------------------------------------

Modernized Platform: Update to Qt6
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* Mixxx is now using Qt6, offering improved performance and enhanced compatibility with modern systems.
  `#11863 <https://github.com/mixxxdj/mixxx/pull/11863>`__
  `#11892 <https://github.com/mixxxdj/mixxx/pull/11892>`__
* Build system defaults to Qt6. Qt5 build support will be dropped with Mixxx 2.6
  `#11934 <https://github.com/mixxxdj/mixxx/pull/11934>`__
* Drop support for macOS versions earlier than 11
* Drop support for Windows versions earlier than Windows 10 build 1809
* Drop support for Ubuntu versions earlier than 22.04
* Require a C++20 compiler
* Support GCC 14
  `#13504 <https://github.com/mixxxdj/mixxx/pull/13504>`__
  `#13467 <https://github.com/mixxxdj/mixxx/issues/13467>`__
* DlgAbout: Add Qt version to the dialog `#11862 <https://github.com/mixxxdj/mixxx/pull/11862>`__
* WWidget: Disable touch events on macOS (fixing trackpad issues on Qt 6) `#11870 <https://github.com/mixxxdj/mixxx/pull/11870>`__
* Various Skin adjustments
  `#11970 <https://github.com/mixxxdj/mixxx/pull/11970>`__
  `#11957 <https://github.com/mixxxdj/mixxx/issues/11957>`__
  `#12050 <https://github.com/mixxxdj/mixxx/pull/12050>`__
  `#12939 <https://github.com/mixxxdj/mixxx/pull/12939>`__
  `#13242 <https://github.com/mixxxdj/mixxx/pull/13242>`__
  `#14014 <https://github.com/mixxxdj/mixxx/pull/14014>`__
  `#13535 <https://github.com/mixxxdj/mixxx/pull/13535>`__
  `#14013 <https://github.com/mixxxdj/mixxx/pull/14013>`__
  `#13959 <https://github.com/mixxxdj/mixxx/issues/13959>`__
  `#14034 <https://github.com/mixxxdj/mixxx/pull/14034>`__
  `#12972 <https://github.com/mixxxdj/mixxx/issues/12972>`__
  `#14035 <https://github.com/mixxxdj/mixxx/pull/14035>`__
* Various Library adjustments
  `#12380 <https://github.com/mixxxdj/mixxx/pull/12380>`__
  `#12478 <https://github.com/mixxxdj/mixxx/pull/12478>`__
  `#13035 <https://github.com/mixxxdj/mixxx/pull/13035>`__
  `#13033 <https://github.com/mixxxdj/mixxx/issues/13033>`__
  `#12488 <https://github.com/mixxxdj/mixxx/pull/12488>`__
  `#12216 <https://github.com/mixxxdj/mixxx/pull/12216>`__
  `#13448 <https://github.com/mixxxdj/mixxx/pull/13448>`__

Engine
^^^^^^


* Beats: allow undoing the last BPM/beats change `#12954 <https://github.com/mixxxdj/mixxx/pull/12954>`__
  `#12774 <https://github.com/mixxxdj/mixxx/issues/12774>`__
  `#10138 <https://github.com/mixxxdj/mixxx/issues/10138>`__
  `#13339 <https://github.com/mixxxdj/mixxx/pull/13339>`__
* Add beatloop anchor to set and adjust loop from either start or end
  `#12745 <https://github.com/mixxxdj/mixxx/pull/12745>`__
  `#13241 <https://github.com/mixxxdj/mixxx/pull/13241>`__
* Add Rate Tap button `#12104 <https://github.com/mixxxdj/mixxx/pull/12104>`__
* Store/restore regular loop when toggling rolling loops
  `#12475 <https://github.com/mixxxdj/mixxx/pull/12475>`__
  `#8947 <https://github.com/mixxxdj/mixxx/issues/8947>`__
* Add ``beats_translate_move`` ControlEncoder `#12376 <https://github.com/mixxxdj/mixxx/pull/12376>`__
* Looping/Beatjump: use seconds if track has no beats
  `#12961 <https://github.com/mixxxdj/mixxx/pull/12961>`__
  `#11124 <https://github.com/mixxxdj/mixxx/issues/11124>`__
* Add Track colour palette cycling controls ``track_color_next`` and ``track_color_prev`` to library, decks and samplers
  `#13066 <https://github.com/mixxxdj/mixxx/pull/13066>`__
  `#12905 <https://github.com/mixxxdj/mixxx/issues/12905>`__
* Add Tempo locking controls
  `#13041 <https://github.com/mixxxdj/mixxx/pull/13041>`__
  `#13041 <https://github.com/mixxxdj/mixxx/pull/13041>`__
  `#13038 <https://github.com/mixxxdj/mixxx/issues/13038>`__
  `#13199 <https://github.com/mixxxdj/mixxx/pull/13199>`__
* Recording: Fix bogus timestamp in CUE sheet after restarting a recording
  `#13966 <https://github.com/mixxxdj/mixxx/pull/13966>`__
  `#13964 <https://github.com/mixxxdj/mixxx/issues/13964>`__
* Improve Taglib/SoundSource logging `#13541 <https://github.com/mixxxdj/mixxx/pull/13541>`__

Skins / Interface
^^^^^^^^^^^^^^^^^


* Toggle the menubar with single Alt key press (auto hide)
  `#11526 <https://github.com/mixxxdj/mixxx/pull/11526>`__
  `#13301 <https://github.com/mixxxdj/mixxx/pull/13301>`__
* Fullscreen toggle rework
  `#11566 <https://github.com/mixxxdj/mixxx/pull/11566>`__
  `#13189 <https://github.com/mixxxdj/mixxx/pull/13189>`__
  `#13030 <https://github.com/mixxxdj/mixxx/issues/13030>`__
* Allow to edit track title and artist directly within the decks via a delayed double-click
  `#11755 <https://github.com/mixxxdj/mixxx/pull/11755>`__
  `#13930 <https://github.com/mixxxdj/mixxx/pull/13930>`__
* Require a minimum movement before initiating the drag&drop of tracks `#12903 <https://github.com/mixxxdj/mixxx/pull/12903>`__
* Add type toggle to cue popup `#13215 <https://github.com/mixxxdj/mixxx/pull/13215>`__
* Effect Meta Knob: draws arc from default meta position
  `#12638 <https://github.com/mixxxdj/mixxx/pull/12638>`__
  `#12634 <https://github.com/mixxxdj/mixxx/issues/12634>`__
* Handle not supported files when dragging to waveforms and spinnies
  `#13206 <https://github.com/mixxxdj/mixxx/issues/13206>`__
* Tooltips: Improve ``rate_up/down`` description regarding pitch vs. speed `#12590 <https://github.com/mixxxdj/mixxx/pull/12590>`__
* Tooltips: Add description for expand/collapse samplers buttons
  `#13005 <https://github.com/mixxxdj/mixxx/pull/13005>`__
  `#12998 <https://github.com/mixxxdj/mixxx/issues/12998>`__
* Track label widgets: Set ``show_track_menu`` only for main decks `#12978 <https://github.com/mixxxdj/mixxx/pull/12978>`__
* MacOS: App proxy icon of the playing track to the window title `#12116 <https://github.com/mixxxdj/mixxx/pull/12116>`__
* Auto DJ: Force-show decks 3/4 if we are going to use them `#13455 <https://github.com/mixxxdj/mixxx/pull/13455>`__
* Auto DJ: Add new random tracks if one track does not exists `#13551 <https://github.com/mixxxdj/mixxx/pull/13551>`__
* Allow to set LaunchImage style per color scheme `#13731 <https://github.com/mixxxdj/mixxx/pull/13731>`__
* Show wait cursor when re/loading a skin (not during startup) `#13747 <https://github.com/mixxxdj/mixxx/pull/13747>`__
* LateNight: Merge vinyl control toggle and status light
  `#12947 <https://github.com/mixxxdj/mixxx/pull/12947>`__
  `#10192 <https://github.com/mixxxdj/mixxx/issues/10192>`__
* LateNight, Deere, Tango: Deactivate beatgrid edit controls if BPM is locked
  `#13320 <https://github.com/mixxxdj/mixxx/pull/13320>`__
  `#13323 <https://github.com/mixxxdj/mixxx/pull/13323>`__
  `#13325 <https://github.com/mixxxdj/mixxx/pull/13325>`__
* LateNight: Add/tweak CueDelete icons
  `#13495 <https://github.com/mixxxdj/mixxx/pull/13495>`__
  `#13492 <https://github.com/mixxxdj/mixxx/issues/13492>`__
* LateNight: Use Classic launch image style also for 64 samplers version `#13796 <https://github.com/mixxxdj/mixxx/pull/13796>`__
* Adjust some skin controls, to allow point-and-click mapping
  `#13906 <https://github.com/mixxxdj/mixxx/pull/13906>`__
* PreviewDeckN,LoadSelectedTrackAndPlay toggles play/pause if the track is already loaded
  `#12920 <https://github.com/mixxxdj/mixxx/pull/12920>`__
  `#9819 <https://github.com/mixxxdj/mixxx/issues/9819>`__
* Command line interface: Determine whether to color output based on ``TERM`` variable
  `#13486 <https://github.com/mixxxdj/mixxx/pull/13486>`__
* Command line interface: Add option ``--start-autodj`` to start Auto DJ immediately after Mixxx start.
  `#13017 <https://github.com/mixxxdj/mixxx/pull/13017>`__
  `#10189 <https://github.com/mixxxdj/mixxx/issues/10189>`__
* Logging: Include timestamps in messages by default `#11861 <https://github.com/mixxxdj/mixxx/pull/11861>`__
* Logging: Limit mixxx.log size to 100 MB or via --log-max-file-size
  `#13684 <https://github.com/mixxxdj/mixxx/pull/13684>`__
  `#13660 <https://github.com/mixxxdj/mixxx/issues/13660>`__
* Fix skin reload after changing color scheme `#13847 <https://github.com/mixxxdj/mixxx/pull/13847>`__

Effects
^^^^^^^


* Add Compressor effect `#12523 <https://github.com/mixxxdj/mixxx/pull/12523>`__
* add Glitch effect `#11329 <https://github.com/mixxxdj/mixxx/pull/11329>`__
* Add backend for Audio Unit (AU) plugins on macOS
  `#12112 <https://github.com/mixxxdj/mixxx/pull/12112>`__
  `#13938 <https://github.com/mixxxdj/mixxx/pull/13938>`__
* Effect Meta knob: Draw arc from default meta position
  `#12638 <https://github.com/mixxxdj/mixxx/pull/12638>`__
  `#12634 <https://github.com/mixxxdj/mixxx/issues/12634>`__
* Show newly added effects, read/write HiddenEffects
  `#13326 <https://github.com/mixxxdj/mixxx/pull/13326>`__
  `#11343 <https://github.com/mixxxdj/mixxx/issues/11343>`__

Library
^^^^^^^


* Shortkeys Cut, Copy, Paste for track list management
  `#12020 <https://github.com/mixxxdj/mixxx/pull/12020>`__
  `#13361 <https://github.com/mixxxdj/mixxx/issues/13361>`__
  `#13364 <https://github.com/mixxxdj/mixxx/pull/13364>`__
  `#13958 <https://github.com/mixxxdj/mixxx/pull/13958>`__
  `#13100 <https://github.com/mixxxdj/mixxx/issues/13100>`__
* Playlists: move tracks with Alt + Up/Down/PageUp/PageDown/Home/End
  `#13092 <https://github.com/mixxxdj/mixxx/pull/13092>`__
  `#10826 <https://github.com/mixxxdj/mixxx/issues/10826>`__
  `#13098 <https://github.com/mixxxdj/mixxx/pull/13098>`__
* Search: Add special BPM filters
  `#12072 <https://github.com/mixxxdj/mixxx/pull/12072>`__
  `#8191 <https://github.com/mixxxdj/mixxx/issues/8191>`__
* Search: Add "OR" search operator
  `#12061 <https://github.com/mixxxdj/mixxx/pull/12061>`__
  `#8881 <https://github.com/mixxxdj/mixxx/issues/8881>`__
* Search: Add 'type' filter
  `#13338 <https://github.com/mixxxdj/mixxx/issues/13338>`__
* Search: Add 'id' filter `#13694 <https://github.com/mixxxdj/mixxx/pull/13694>`__
* Search related Tracks menu: Allow to use multiple filters at once
  `#12213 <https://github.com/mixxxdj/mixxx/pull/12213>`__
  `#12211 <https://github.com/mixxxdj/mixxx/issues/12211>`__
* Track menu: Rephrase "Reset" to "Clear" `#12955 <https://github.com/mixxxdj/mixxx/pull/12955>`__
* Track menu: Add support for scaling BPM by different ratios
  `#12934 <https://github.com/mixxxdj/mixxx/pull/12934>`__
  `#9133 <https://github.com/mixxxdj/mixxx/issues/9133>`__
* Track menu: Remove from disk: stop and eject all affected decks `#13214 <https://github.com/mixxxdj/mixxx/pull/13214>`__
* Track menu: add star rating
  `#12700 <https://github.com/mixxxdj/mixxx/pull/12700>`__
  `#10652 <https://github.com/mixxxdj/mixxx/issues/10652>`__
* Track menu: Show Properties in Missing and Hidden view `#13426 <https://github.com/mixxxdj/mixxx/pull/13426>`__
* Add multi-track property editor / batch tag editor
  `#12548 <https://github.com/mixxxdj/mixxx/pull/12548>`__
  `#9023 <https://github.com/mixxxdj/mixxx/issues/9023>`__
  `#13299 <https://github.com/mixxxdj/mixxx/pull/13299>`__
  `#13609 <https://github.com/mixxxdj/mixxx/pull/13609>`__
  `#13597 <https://github.com/mixxxdj/mixxx/issues/13597>`__
  `#13631 <https://github.com/mixxxdj/mixxx/pull/13631>`__
* Track property editor: focus the editing field in the track properties that corresponds to the focused column
  `#13841 <https://github.com/mixxxdj/mixxx/pull/13841>`__
  `#14036 <https://github.com/mixxxdj/mixxx/pull/14036>`__
* Computer feature: add sidebar action "Refresh directory tree" `#12908 <https://github.com/mixxxdj/mixxx/pull/12908>`__
* Add feedback to directory operations (add, remove, relink)
  `#12436 <https://github.com/mixxxdj/mixxx/pull/12436>`__
  `#10481 <https://github.com/mixxxdj/mixxx/issues/10481>`__
* Add ability to import external playlists as crates `#11852 <https://github.com/mixxxdj/mixxx/pull/11852>`__
* Add 'Shuffle playlist' sidebar action
  `#12498 <https://github.com/mixxxdj/mixxx/pull/12498>`__
  `#6988 <https://github.com/mixxxdj/mixxx/issues/6988>`__
* Playlists: Update of playlist labels after adding tracks `#12866 <https://github.com/mixxxdj/mixxx/pull/12866>`__ `#12761 <https://github.com/mixxxdj/mixxx/issues/12761>`__
* Tracks: Custom color for missing tracks `#12895 <https://github.com/mixxxdj/mixxx/pull/12895>`__
* Tracks: Custom text color for played tracks (qss)
  `#12744 <https://github.com/mixxxdj/mixxx/pull/12744>`__
  `#5911 <https://github.com/mixxxdj/mixxx/issues/5911>`__
  `#12912 <https://github.com/mixxxdj/mixxx/pull/12912>`__
  `#13538 <https://github.com/mixxxdj/mixxx/pull/13538>`__
* History: Show track count and duration in sidebar
  `#12811 <https://github.com/mixxxdj/mixxx/pull/12811>`__
  `#12788 <https://github.com/mixxxdj/mixxx/issues/12788>`__
* Don't allow pasting tracks into locked playlists/crates or History `#12926 <https://github.com/mixxxdj/mixxx/pull/12926>`__
* Optimize Library scrolling `#13358 <https://github.com/mixxxdj/mixxx/pull/13358>`__
* Keep the metadata key text unchanged, use it as the origin of information
  `#11096 <https://github.com/mixxxdj/mixxx/pull/11096>`__
  `#11095 <https://github.com/mixxxdj/mixxx/issues/11095>`__
  `#13650 <https://github.com/mixxxdj/mixxx/pull/13650>`__
  `#14011 <https://github.com/mixxxdj/mixxx/pull/14011>`__
  `#14008 <https://github.com/mixxxdj/mixxx/pull/14008>`__
  `#14020 <https://github.com/mixxxdj/mixxx/pull/14020>`__
* Center date values, right-align Track # `#13674 <https://github.com/mixxxdj/mixxx/pull/13674>`__
* Analysis: Fix stop button when analyzing crate/playlist `#13902 <https://github.com/mixxxdj/mixxx/pull/13902>`__
* Add a debug message, which appears when event loop processing in Mixxx application takes very long
  `#12094 <https://github.com/mixxxdj/mixxx/pull/12094>`__
  `#13900 <https://github.com/mixxxdj/mixxx/pull/13900>`__
  `#13889 <https://github.com/mixxxdj/mixxx/pull/13889>`__
  `#13903 <https://github.com/mixxxdj/mixxx/pull/13903>`__
  `#14012 <https://github.com/mixxxdj/mixxx/pull/14012>`__

Preferences
^^^^^^^^^^^


* Add load point option 'First hotcue'
  `#12869 <https://github.com/mixxxdj/mixxx/pull/12869>`__
  `#12740 <https://github.com/mixxxdj/mixxx/issues/12740>`__
* MIDI Input editor: allow selecting multiple Options `#12348 <https://github.com/mixxxdj/mixxx/pull/12348>`__
* Apply changes only after pressing Apply in color preferences `#13302 <https://github.com/mixxxdj/mixxx/pull/13302>`__
* Add/reorder tabstops in Library and Waveform preferences
  `#13846 <https://github.com/mixxxdj/mixxx/pull/13846>`__
* Add missing spacer in interface preferences `#13094 <https://github.com/mixxxdj/mixxx/pull/13094>`__
* Fix fetching of soundcard sample rate
  `#11951 <https://github.com/mixxxdj/mixxx/pull/11951>`__
  `11949 <https://github.com/mixxxdj/mixxx/issues/11949>`__

Controller Mappings
^^^^^^^^^^^^^^^^^^^


* Denon MC7000: Add optional jog wheel acceleration to the controller mapping `#4684 <https://github.com/mixxxdj/mixxx/pull/4684>`__
* Denon MC7000: Unify parameter button logic and add customizable modes `#13589 <https://github.com/mixxxdj/mixxx/pull/13589>`__
* Denon MC7000: Add sampler options to mapping settings `#13950 <https://github.com/mixxxdj/mixxx/pull/13950>`__
* MIDI for light: Implement new Active deck heuristic `#13513 <https://github.com/mixxxdj/mixxx/pull/13513>`__
* MIDI for light: Add settings GUI `#13721 <https://github.com/mixxxdj/mixxx/pull/13721>`__
* Numark Scratch: Add controller settings  `#13404 <https://github.com/mixxxdj/mixxx/pull/13404>`__
* Pioneer DDJ-FLX4: Mapping improvements `#12842 <https://github.com/mixxxdj/mixxx/pull/12842>`__
* Traktor Kontrol S4 MK3: Add setting definition for  `#12995 <https://github.com/mixxxdj/mixxx/pull/12995>`__
* Traktor Kontrol S4 MK3: Software mixer support and default pad layout customisation `#13059 <https://github.com/mixxxdj/mixxx/pull/13059>`__
* Traktor Kontrol S4 Mk3: Rework jogwheel speed compute and motorized platter `#13393 <https://github.com/mixxxdj/mixxx/pull/13393>`__
* Traktor Kontrol S4 Mk3: Revert QuickEffect preset offset `#13997 <https://github.com/mixxxdj/mixxx/pull/13997>`__
* Traktor Kontrol S4 Mk3: Correct wheel timestamp wrap-around `#14016 <https://github.com/mixxxdj/mixxx/pull/14016>`__

Controller Backend
^^^^^^^^^^^^^^^^^^


* Send sysex to all handlers `#12827 <https://github.com/mixxxdj/mixxx/pull/12827>`__
* Speed up midi sysex receive `#12843 <https://github.com/mixxxdj/mixxx/pull/12843>`__
* Add control for showing a deck's track menu `#10825 <https://github.com/mixxxdj/mixxx/pull/10825>`__
* Removed old examples HID keyboard and HID trackpad `#12977 <https://github.com/mixxxdj/mixxx/pull/12977>`__
* Reduce log noise with HID device
  `#13010 <https://github.com/mixxxdj/mixxx/pull/13010>`__
  `#13125 <https://github.com/mixxxdj/mixxx/pull/13125>`__
* Allow controller mapping to discard polling `#12558 <https://github.com/mixxxdj/mixxx/pull/12558>`__
* Add support for mapping user settings
  `#11300 <https://github.com/mixxxdj/mixxx/pull/11300>`__
  `#13046 <https://github.com/mixxxdj/mixxx/pull/13046>`__
  `#13057 <https://github.com/mixxxdj/mixxx/pull/13057>`__
  `#13045 <https://github.com/mixxxdj/mixxx/pull/13045>`__
  `#13656 <https://github.com/mixxxdj/mixxx/pull/13656>`__
  `#13738 <https://github.com/mixxxdj/mixxx/pull/13738>`__
  `#13979 <https://github.com/mixxxdj/mixxx/pull/13979>`__
  `#13990 <https://github.com/mixxxdj/mixxx/pull/13990>`__
* Registering MIDI Input Handlers From Javascript
  `#12781 <https://github.com/mixxxdj/mixxx/pull/12781>`__
  `#13089 <https://github.com/mixxxdj/mixxx/pull/13089>`__
* Controller IO table: Fix display text for Action/control delegate `#13188 <https://github.com/mixxxdj/mixxx/pull/13188>`__
* Drop lodash dependency in ComponentJS `#12779 <https://github.com/mixxxdj/mixxx/pull/12779>`__
* Support for bulk devices on Windows and Mac `#13008 <https://github.com/mixxxdj/mixxx/pull/13008>`__
* Drop lodash dependency in ComponentJS
  `#12779 <https://github.com/mixxxdj/mixxx/pull/12779>`__
* Fix pending reference to the old mapping after selecting 'No mapping' `#13907 <https://github.com/mixxxdj/mixxx/pull/13907>`__
* Fix crash with GoToItem when no app windows has the focus `#13657 <https://github.com/mixxxdj/mixxx/pull/13657>`__

Waveforms
^^^^^^^^^


* Visualize slip mode position by splitting waveform (RGB GLSL only)
  `#13002 <https://github.com/mixxxdj/mixxx/pull/13002>`__
  `#13256 <https://github.com/mixxxdj/mixxx/pull/13256>`__
  `#10063 <https://github.com/mixxxdj/mixxx/issues/10063>`__
* Show beats and time until next marker in the waveform
  `#12994 <https://github.com/mixxxdj/mixxx/pull/12994>`__
  `#13311 <https://github.com/mixxxdj/mixxx/pull/13311>`__
  `#13953 <https://github.com/mixxxdj/mixxx/pull/13953>`__
  `#13314 <https://github.com/mixxxdj/mixxx/issues/13314>`__
* Don't elide hotcue labels
  `#13219 <https://github.com/mixxxdj/mixxx/pull/13219>`__
  `#10722 <https://github.com/mixxxdj/mixxx/issues/10722>`__
* Allshader RGB, Filtered and Stacked Waveforms using textures for waveform data
  `#13151 <https://github.com/mixxxdj/mixxx/pull/13151>`__
  `#12641 <https://github.com/mixxxdj/mixxx/issues/12641>`__
* Allow changing the waveform overview type without reloading the skin
  `#13273 <https://github.com/mixxxdj/mixxx/pull/13273>`__
* Overview: Update immediately, when the normalize option or global gain changed
  `#13634 <https://github.com/mixxxdj/mixxx/pull/13634>`__
* Overview: Clear pickup position display when opening cue menu
  `#13693 <https://github.com/mixxxdj/mixxx/pull/13693>`__

Experimental Features
^^^^^^^^^^^^^^^^^^^^^


* QML Skin: Can be tested via the --qml command line option
  `#13152 <https://github.com/mixxxdj/mixxx/pull/13152>`__
  `#12139 <https://github.com/mixxxdj/mixxx/pull/12139>`__
  `#13152 <https://github.com/mixxxdj/mixxx/pull/13152>`__
* QML Skin related changes
  `#11423 <https://github.com/mixxxdj/mixxx/pull/11423>`__
  `#12559 <https://github.com/mixxxdj/mixxx/pull/12559>`__
  `#12549 <https://github.com/mixxxdj/mixxx/pull/12549>`__
  `#12541 <https://github.com/mixxxdj/mixxx/pull/12541>`__
  `#12795 <https://github.com/mixxxdj/mixxx/pull/12795>`__
  `#12844 <https://github.com/mixxxdj/mixxx/pull/12844>`__
  `#12546 <https://github.com/mixxxdj/mixxx/pull/12546>`__
  `#12794 <https://github.com/mixxxdj/mixxx/pull/12794>`__
  `#12536 <https://github.com/mixxxdj/mixxx/issues/12536>`__
  `#13058 <https://github.com/mixxxdj/mixxx/pull/13058>`__
  `#12604 <https://github.com/mixxxdj/mixxx/pull/12604>`__
  `#3967 <https://github.com/mixxxdj/mixxx/pull/3967>`__
  `#13009 <https://github.com/mixxxdj/mixxx/pull/13009>`__
  `#13009 <https://github.com/mixxxdj/mixxx/pull/13009>`__
  `#13011 <https://github.com/mixxxdj/mixxx/pull/13011>`__
  `#13506 <https://github.com/mixxxdj/mixxx/pull/13506>`__
* iOS support: Mixxx can be built for iOS
  `#12672 <https://github.com/mixxxdj/mixxx/pull/12672>`__
* iOS support related changes
  `#12689 <https://github.com/mixxxdj/mixxx/pull/12689>`__
  `#12714 <https://github.com/mixxxdj/mixxx/pull/12714>`__
  `#12716 <https://github.com/mixxxdj/mixxx/pull/12716>`__
  `#12698 <https://github.com/mixxxdj/mixxx/pull/12698>`__
  `#12676 <https://github.com/mixxxdj/mixxx/pull/12676>`__
  `#12688 <https://github.com/mixxxdj/mixxx/pull/12688>`__
  `#13379 <https://github.com/mixxxdj/mixxx/pull/13379>`__
  `#13378 <https://github.com/mixxxdj/mixxx/issues/13378>`__
  `#13383 <https://github.com/mixxxdj/mixxx/pull/13383>`__
* Emscripten/WebAssembly support, to run Mixxx hardware independent in a browser
  `#12918 <https://github.com/mixxxdj/mixxx/pull/12918>`__
* Emscripten/WebAssembly related changes
  `#12910 <https://github.com/mixxxdj/mixxx/pull/12910>`__
  `#12913 <https://github.com/mixxxdj/mixxx/pull/12913>`__
  `#12916 <https://github.com/mixxxdj/mixxx/pull/12916>`__
  `#12915 <https://github.com/mixxxdj/mixxx/pull/12915>`__
  `#12921 <https://github.com/mixxxdj/mixxx/pull/12921>`__
  `#12922 <https://github.com/mixxxdj/mixxx/pull/12922>`__
  `#12931 <https://github.com/mixxxdj/mixxx/pull/12931>`__
  `#12940 <https://github.com/mixxxdj/mixxx/pull/12940>`__
  `#12945 <https://github.com/mixxxdj/mixxx/pull/12945>`__
  `#12952 <https://github.com/mixxxdj/mixxx/pull/12952>`__
  `#12930 <https://github.com/mixxxdj/mixxx/pull/12930>`__
  `#12917 <https://github.com/mixxxdj/mixxx/pull/12917>`__

Target support
^^^^^^^^^^^^^^


* Maintain GL ES support `#13485 <https://github.com/mixxxdj/mixxx/pull/13485>`__
* Tools: Add ``rpm_buildenv.sh`` for building on Fedora `#13069 <https://github.com/mixxxdj/mixxx/pull/13069>`__
* Lenient taglib 2.0 guard `#12793 <https://github.com/mixxxdj/mixxx/pull/12793>`__
* MixxxApplication: Support linking Qt statically on Linux `#12284 <https://github.com/mixxxdj/mixxx/pull/12284>`__
* FindSndFile: Link mpg123 in static builds `#13087 <https://github.com/mixxxdj/mixxx/pull/13087>`__
* FindPortMidi: Link ALSA in static builds on Linux `#12292 <https://github.com/mixxxdj/mixxx/pull/12292>`__ `#12291 <https://github.com/mixxxdj/mixxx/pull/12291>`__
* FindLibudev: Link hidapi and libusb with libudev in static builds on Linux `#12294 <https://github.com/mixxxdj/mixxx/pull/12294>`__
* FindVorbis: Link ogg in static builds `#12297 <https://github.com/mixxxdj/mixxx/pull/12297>`__
* FindSleef: Use OpenMP in static builds `#12295 <https://github.com/mixxxdj/mixxx/pull/12295>`__
* macOS packaging: Enable app sandbox in ad-hoc-packaged (i.e. non-notarized) bundles too `#12101 <https://github.com/mixxxdj/mixxx/pull/12101>`__
* CMakeLists: Match arbitrary ``arm64-osx`` triplets `#11933 <https://github.com/mixxxdj/mixxx/pull/11933>`__
* Disable warning in lib/apple code `#13522 <https://github.com/mixxxdj/mixxx/pull/13522>`__
* GitHub CI: Use retry loop for CPack to work around macOS issue `#13991 <https://github.com/mixxxdj/mixxx/pull/13991>`__
* Github CI: Enable ``WARNINGS_FATAL`` on macOS, too `#11905 <https://github.com/mixxxdj/mixxx/pull/11905>`__

.. _v2-4-2:

`2.4.2 <https://github.com/mixxxdj/mixxx/milestone/43?closed=1>`__ (2024-11-26)
----------------------------------------------------------------------------------

Controller Mappings
^^^^^^^^^^^^^^^^^^^


* Denon MC7000: Fix star up/down logic by only handling button down events `#13588 <https://github.com/mixxxdj/mixxx/pull/13588>`__
* Intech TEK2: Add initial mapping `#13521 <https://github.com/mixxxdj/mixxx/pull/13521>`__
* Korg Kaoss DJ: Update script `#12683 <https://github.com/mixxxdj/mixxx/pull/12683>`__
* MIDI for light: Fix unsound timer handling `#13117 <https://github.com/mixxxdj/mixxx/pull/13117>`__
* Novation Dicer: Remove Flanger mapping with quickeffect toggle
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

Older Changelog
---------------

Find older changelog entries `here <https://github.com/mixxxdj/mixxx/blob/2.5.0/CHANGELOG.md>`__.


.. seealso:: For an overview of previous versions, `take a look
             <https://launchpad.net/mixxx/+series>`_ at the timeline.
