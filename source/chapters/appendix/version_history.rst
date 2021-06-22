.. include:: /shortcuts.rstext

.. _appendix-version-history:

Version History
===============

2.3.0 (Unreleased)
------------------

*Hotcues*

  * Add hotcue colors and custom labels by right clicking hotcue buttons or right clicking hotcues on overview waveforms `#2016 <https://github.com/mixxxdj/mixxx/pull/2016>`__ `#2520 <https://github.com/mixxxdj/mixxx/pull/2520>`__ `#2238 <https://github.com/mixxxdj/mixxx/pull/2238>`__ `#2560 <https://github.com/mixxxdj/mixxx/pull/2560>`__ `#2557 <https://github.com/mixxxdj/mixxx/pull/2557>`__ `#2362 <https://github.com/mixxxdj/mixxx/pull/2362>`__
  * Mouse hover cues on overview waveform to show time remaining until the cue `#2238 <https://github.com/mixxxdj/mixxx/pull/2238>`__

*Hotcue & Track Colors*

  * Add configurable color per track `#2470 <https://github.com/mixxxdj/mixxx/pull/2470>`__ `#2539 <https://github.com/mixxxdj/mixxx/pull/2539>`__ `#2545 <https://github.com/mixxxdj/mixxx/pull/2545>`__ `#2630 <https://github.com/mixxxdj/mixxx/pull/2630>`__ `lp:1100882 <https://bugs.launchpad.net/mixxx/+bug/1100882>`__
  * Add customizable color palettes for hotcue and track colors `#2530 <https://github.com/mixxxdj/mixxx/pull/2530>`__ `#2589 <https://github.com/mixxxdj/mixxx/pull/2589>`__
  * Add hotcue color find-and-replace tool `#2547 <https://github.com/mixxxdj/mixxx/pull/2547>`__

*Importing From Other DJ Software*

  * Import cue points, track colors, and playlists from Serato file tags & database `#2480 <https://github.com/mixxxdj/mixxx/pull/2480>`__ `#2526 <https://github.com/mixxxdj/mixxx/pull/2526>`__ `#2499 <https://github.com/mixxxdj/mixxx/pull/2499>`__ `#2495 <https://github.com/mixxxdj/mixxx/pull/2495>`__ `#2673 <https://github.com/mixxxdj/mixxx/pull/2673>`__ `#3885 <https://github.com/mixxxdj/mixxx/pull/3885>`__

    * Note: Mixxx does not yet support multiple loops per track. We are `working on this for Mixxx 2.4 <https://github.com/mixxxdj/mixxx/pull/2194>`__. In Mixxx 2.3, if you import a track with multiple loops from Serato, Mixxx will use the first loop cue as the single loop Mixxx currently supports. The imported loops are still stored in Mixxx's database and are treated as hotcues in Mixxx 2.3. If you do not delete these hotcues, they will be usable as loops in Mixxx 2.4. Serato keeps loops and hotcues in separate lists, but Mixxx does not, so loops from Serato are imported starting as hotcue 9.

  * Import cue points, track colors, and playlists from Rekordbox USB drives `#2119 <https://github.com/mixxxdj/mixxx/pull/2119>`__ `#2555 <https://github.com/mixxxdj/mixxx/pull/2555>`__ `#2543 <https://github.com/mixxxdj/mixxx/pull/2543>`__ `#2779 <https://github.com/mixxxdj/mixxx/pull/2779>`__

    * Note: The first Rekordbox memory cue is imported for the main cue button in Mixxx and the remaining Rekordbox memory cues are imported as Mixxx hotcues, starting with the next hotcue number after the last hotcue from Rekordbox.
    * Note: Mixxx does not yet support multiple loops per track. Imported loops from Rekordbox are treated like imported loops from Serato, so refer to the note above for details.

*Intro & Outro Cues*

  * Add intro & outro range cues with automatic silence detection `#1242 <https://github.com/mixxxdj/mixxx/pull/1242>`__
  * Show duration of intro & outro ranges on overview waveform `#2089 <https://github.com/mixxxdj/mixxx/pull/2089>`__
  * Use intro & outro cues in AutoDJ transitions `#2103 <https://github.com/mixxxdj/mixxx/pull/2103>`__

*Deck cloning*

  * Add deck cloning (also known as "instant doubles" in other DJ software) by dragging and dropping between decks `#1892 <https://github.com/mixxxdj/mixxx/pull/1892>`__ and samplers `#3200 <https://github.com/mixxxdj/mixxx/pull/3200>`__
  * Clone decks by double pressing the load button on a controller (with option to disable this) `#2024 <https://github.com/mixxxdj/mixxx/pull/2024>`__ `#2042 <https://github.com/mixxxdj/mixxx/pull/2042>`__

*Skins & GUI*

  * Aesthetically revamped LateNight skin `#2298 <https://github.com/mixxxdj/mixxx/pull/2298>`__ `#2342 <https://github.com/mixxxdj/mixxx/pull/2342>`__
  * Right click overview waveform to show time remaining until that point `#2238 <https://github.com/mixxxdj/mixxx/pull/2238>`__
  * Show track info dialog when double clicking track labels in decks `#2990 <https://github.com/mixxxdj/mixxx/pull/2990>`__
  * Show track context menu when right clicking text in decks `#2612 <https://github.com/mixxxdj/mixxx/pull/2612>`__ `#2675 <https://github.com/mixxxdj/mixxx/pull/2675>`__ `#2684 <https://github.com/mixxxdj/mixxx/pull/2684>`__ `#2696 <https://github.com/mixxxdj/mixxx/pull/2696>`__
  * Add laptop battery widget to skins `#2283 <https://github.com/mixxxdj/mixxx/pull/2283>`__ `#2277 <https://github.com/mixxxdj/mixxx/pull/2277>`__ `#2250 <https://github.com/mixxxdj/mixxx/pull/2250>`__ `#2228 <https://github.com/mixxxdj/mixxx/pull/2228>`__ `#2221 <https://github.com/mixxxdj/mixxx/pull/2221>`__ `#2163 <https://github.com/mixxxdj/mixxx/pull/2163>`__ `#2160 <https://github.com/mixxxdj/mixxx/pull/2160>`__ `#2147 <https://github.com/mixxxdj/mixxx/pull/2147>`__ `#2281 <https://github.com/mixxxdj/mixxx/pull/2281>`__ `#2319 <https://github.com/mixxxdj/mixxx/pull/2319>`__ `#2287 <https://github.com/mixxxdj/mixxx/pull/2287>`__
  * Show when passthrough mode is active on overview waveforms `#2575 <https://github.com/mixxxdj/mixxx/pull/2575>`__ `#2616 <https://github.com/mixxxdj/mixxx/pull/2616>`__
  * Changed format of currently playing track in window title from "artist, title" to "artist - title" `#2807 <https://github.com/mixxxdj/mixxx/pull/2807>`__
  * Workaround Linux skin change crash `#3144 <https://github.com/mixxxdj/mixxx/pull/3144>`__ `lp:1885009 <https://bugs.launchpad.net/mixxx/+bug/1885009>`__
  * Fix touch control `lp:1895431 <https://bugs.launchpad.net/mixxx/+bug/1895431>`__
  * Fix broken knob interaction on touchscreens `#3512 <https://github.com/mixxxdj/mixxx/pull/3512>`__
  * AutoDJ: Make "enable" shortcut work after startup `#3242 <https://github.com/mixxxdj/mixxx/pull/3242>`__
  * Add rate range indicator `#3693 <https://github.com/mixxxdj/mixxx/pull/3693>`__
  * Allow menubar to be styled `#3372 <https://github.com/mixxxdj/mixxx/pull/3372>`__ `#3788 <https://github.com/mixxxdj/mixxx/pull/3788>`__
  * Add Donate button to About dialog `#3838 <https://github.com/mixxxdj/mixxx/pull/3838>`__ `#3846 <https://github.com/mixxxdj/mixxx/pull/3846>`__
  * Add Scrollable Skin Widget `#3890 <https://github.com/mixxxdj/mixxx/pull/3890>`__
  * Fix minor visual issues in Skins `#3958 <https://github.com/mixxxdj/mixxx/pull/3958/>`__ `#3954 <https://github.com/mixxxdj/mixxx/pull/3954/>`__ `#3941 <https://github.com/mixxxdj/mixxx/pull/3941/>`__ `#3938 <https://github.com/mixxxdj/mixxx/pull/3938/>`__ `#3936 <https://github.com/mixxxdj/mixxx/pull/3936/>`__ `#3886 <https://github.com/mixxxdj/mixxx/pull/3886/>`__ `#3927 <https://github.com/mixxxdj/mixxx/pull/3927/>`__ `#3844 <https://github.com/mixxxdj/mixxx/pull/3844/>`__ `#3933 <https://github.com/mixxxdj/mixxx/pull/3933/>`__ `#3835 <https://github.com/mixxxdj/mixxx/pull/3835/>`__ `#3902 <https://github.com/mixxxdj/mixxx/pull/3902>`__ `#3931 <https://github.com/mixxxdj/mixxx/pull/3931>`__

*Music Feature Analysis*

  * Multithreaded analysis for much faster batch analysis on multicore CPUs `#1624 <https://github.com/mixxxdj/mixxx/pull/1624>`__ `#2142 <https://github.com/mixxxdj/mixxx/pull/2142>`__ `lp:1641153 <https://bugs.launchpad.net/mixxx/+bug/1641153>`__
  * Fix bugs affecting key detection accuracy `#2137 <https://github.com/mixxxdj/mixxx/pull/2137>`__ `#2152 <https://github.com/mixxxdj/mixxx/pull/2152>`__ `#2112 <https://github.com/mixxxdj/mixxx/pull/2112>`__ `#2136 <https://github.com/mixxxdj/mixxx/pull/2136>`__

    * Note: Users who have not manually corrected keys are advised to clear all keys in their library by pressing Ctrl + A in the library, right clicking, going to Reset -> Key, then reanalyzing their library. This will freeze the GUI while Mixxx clears the keys; this is a known problem that we will not be able to fix for 2.3. Wait until it is finished and you will be able to reanalyze tracks for better key detection results.

  * Remove VAMP plugin support and use Queen Mary DSP library directly. vamp-plugin-sdk and vamp-hostsdk are no longer required dependencies. `#926 <https://github.com/mixxxdj/mixxx/pull/926>`__
  * Improvements BPM detection on non-const beatgrids `#3626 <https://github.com/mixxxdj/mixxx/pull/3626>`__
  * Fix const beatgrid placement `#3965 <https://github.com/mixxxdj/mixxx/pull/3965>`__ `#3973 <https://github.com/mixxxdj/mixxx/pull/3973>`__

*Music Library*

  * Add support for searching for empty fields (for example `crate:""`) `lp:1788086 <https://bugs.launchpad.net/mixxx/+bug/1788086>`__
  * Improve synchronization of track metadata and file tags `#2406 <https://github.com/mixxxdj/mixxx/pull/2406>`__
  * Library Scanner: Improve hashing of directory contents `#2497 <https://github.com/mixxxdj/mixxx/pull/2497>`__
  * Rework of Cover Image Hashing `lp:1607097 <https://bugs.launchpad.net/mixxx/+bug/1607097>`__ `#2507 <https://github.com/mixxxdj/mixxx/pull/2507>`__ `#2508 <https://github.com/mixxxdj/mixxx/pull/2508>`__
  * MusicBrainz: Handle 301 status response `#2510 <https://github.com/mixxxdj/mixxx/pull/2510>`__
  * MusicBrainz: Add extended metadata support `lp:1581256 <https://bugs.launchpad.net/mixxx/+bug/1581256>`__ `#2522 <https://github.com/mixxxdj/mixxx/pull/2522>`__
  * TagLib: Fix detection of empty or missing file tags `lp:1865957 <https://bugs.launchpad.net/mixxx/+bug/1865957>`__ `#2535 <https://github.com/mixxxdj/mixxx/pull/2535>`__
  * Fix caching of duplicate tracks that reference the same file `#3027 <https://github.com/mixxxdj/mixxx/pull/3027>`__
  * Use 6 instead of only 4 compatible musical keys (major/minor) `#3205 <https://github.com/mixxxdj/mixxx/pull/3205>`__
  * Fix possible crash when trying to refocus the tracks table while another Mixxx window has focus `#3201 <https://github.com/mixxxdj/mixxx/pull/3201>`__
  * Don't create new tags in file when exporting metadata to it `#3898 <https://github.com/mixxxdj/mixxx/pull/3898>`__
  * Fix playlist files beginning with non-english characters not being loaded `#3916 <https://github.com/mixxxdj/mixxx/pull/3916>`__
  * Enable sorting in "Hidden Tracks" and "Missing Tracks" views `#3828 <https://github.com/mixxxdj/mixxx/pull/3828>`__ `lp:1828555 <https://bugs.launchpad.net/mixxx/+bug/1828555/>`__ `lp:1924616 <https://bugs.launchpad.net/mixxx/+bug/1924616/>`__
  * Fix track table being empty after start `#3935 <https://github.com/mixxxdj/mixxx/pull/3935/>`__ `lp:1930546 <https://bugs.launchpad.net/mixxx/+bug/1930546/>`__ `lp:1924843 <https://bugs.launchpad.net/mixxx/+bug/1924843/>`__

*Audio Codecs*

  * Add FFmpeg audio decoder, bringing support for ALAC files `#1356 <https://github.com/mixxxdj/mixxx/pull/1356>`__
  * Include LAME MP3 encoder with Mixxx now that the MP3 patent has expired `lp:1294128 <https://bugs.launchpad.net/mixxx/+bug/1294128>`__ `buildserver:#37 <https://github.com/mixxxdj/buildserver/pull/37>`__ `buildserver:9e8bcee <https://github.com/mixxxdj/buildserver/commit/9e8bcee771731920ae82f3e076d43f0fb51e5027>`__
  * Add Opus streaming and recording support. `lp:1338413 <https://bugs.launchpad.net/mixxx/+bug/1338413>`__
  * Remove support for SoundSource plugins because the code was not well-maintained and could lead to crashes `lp:1792747 <https://bugs.launchpad.net/mixxx/+bug/1792747>`__
  * Add HE-AAC encoding capabilities for recording and broadcasting `#3615 <https://github.com/mixxxdj/mixxx/pull/3615>`__

*Audio Engine*

  * Fix loss of precision when dealing with floating-point sample positions while setting loop out position and seeking using vinyl control `#3126 <https://github.com/mixxxdj/mixxx/pull/3126>`__ `#3127 <https://github.com/mixxxdj/mixxx/pull/3127>`__
  * Prevent moving a loop beyond track end `#3117 <https://github.com/mixxxdj/mixxx/pull/3117>`__ `lp:1799574 <https://bugs.launchpad.net/mixxx/+bug/1799574>`__
  * Fix possible memory corruption using JACK on Linux `#3160 <https://github.com/mixxxdj/mixxx/pull/3160>`__
  * Fix changing of vinyl lead-in time `lp:1915483 <https://bugs.launchpad.net/mixxx/+bug/1915483>`__ `#3781 <https://github.com/mixxxdj/mixxx/pull/3781>`__
  * Fix tempo change of non-const beatgrid track on audible deck when cueing another track `#3772 <https://github.com/mixxxdj/mixxx/pull/3772>`__
  * Fix crash when changing effect unit routing `#3882 <https://github.com/mixxxdj/mixxx/pull/3882>`__ `lp:1775497 <https://bugs.launchpad.net/mixxx/+bug/1775497>`__
  * Make microphone ducking use strength knob the same way in automatic & manual mode `#2750 <https://github.com/mixxxdj/mixxx/pull/2750>`__

*Controllers*

  * Improve workflow for configuring controller mappings and editing mappings `#2569 <https://github.com/mixxxdj/mixxx/pull/2569>`__ `#3278 <https://github.com/mixxxdj/mixxx/pull/3278>`__ `#3667 <https://github.com/mixxxdj/mixxx/pull/3667>`__
  * Improve error reporting from controller scripts `#2588 <https://github.com/mixxxdj/mixxx/pull/2588>`__
  * Make hotcue and track colors mappable on controllers `#2030 <https://github.com/mixxxdj/mixxx/pull/2030>`__ `#2541 <https://github.com/mixxxdj/mixxx/pull/2541>`__ `#2665 <https://github.com/mixxxdj/mixxx/pull/2665>`__ `#2520 <https://github.com/mixxxdj/mixxx/pull/2520>`__
  * Add way to change library table sorting from controllers `#2118 <https://github.com/mixxxdj/mixxx/pull/2118>`__
  * Add support for velocity sensitive sampler buttons in Components JS library `#2032 <https://github.com/mixxxdj/mixxx/pull/2032>`__
  * Add logging when script ControlObject callback is disconnected successfully `#2054 <https://github.com/mixxxdj/mixxx/pull/2054>`__
  * Add controller mapping for :ref:`Roland DJ-505 <roland-dj-505>` `#2111 <https://github.com/mixxxdj/mixxx/pull/2111>`__
  * Add controller mapping for :ref:`Numark iDJ Live II <numark-idj-live-ii>` `#2818 <https://github.com/mixxxdj/mixxx/pull/2818>`__
  * Add controller mapping for :ref:`Hercules DJControl Inpulse 200 <hercules-djcontrol-inpulse-200>` `#2542 <https://github.com/mixxxdj/mixxx/pull/2542>`__
  * Add controller mapping for :ref:`Hercules DJControl Jogvision <hercules-djcontrol-jogvision>` `#2370 <https://github.com/mixxxdj/mixxx/pull/2370>`__
  * Add controller mapping for :ref:`Pioneer DDJ-200 <pioneer-ddj-200>` `#3185 <https://github.com/mixxxdj/mixxx/pull/3185>`__ `#3193 <https://github.com/mixxxdj/mixxx/pull/3193>`__ `#3479 <https://github.com/mixxxdj/mixxx/pull/3742>`__ `#3793 <https://github.com/mixxxdj/mixxx/pull/3793>`__ `#3949 <https://github.com/mixxxdj/mixxx/pull/3949>`__
  * Add controller mapping for :ref:`Pioneer DDJ-400 <pioneer-ddj-400>` `#3479 <https://github.com/mixxxdj/mixxx/pull/3479>`__
  * Add controller mapping for :ref:`ION Discover DJ Pro <ion-discover-dj-pro>` `#2893 <https://github.com/mixxxdj/mixxx/pull/2893>`__
  * Add controller mapping for :ref:`Native Instrument Traktor Kontrol S3 <native-instruments-traktor-kontrol-s3>` `#3031 <https://github.com/mixxxdj/mixxx/pull/3031>`__
  * Add controller mapping for :ref:`Behringer B-Control BCR2000 <behringer-b-control-bcr2000>` `#3342 <https://github.com/mixxxdj/mixxx/pull/3342>`__ `#3943 <https://github.com/mixxxdj/mixxx/pull/3943>`__
  * Add controller mapping for :ref:`Behringer DDM4000 <behringer-ddm4000>` `#3542 <https://github.com/mixxxdj/mixxx/pull/3542>`__
  * Update controller mapping for :ref:`Allen & Heath Xone K2 <allen-heath-xone-k2>` to add intro/outro cues `#2236 <https://github.com/mixxxdj/mixxx/pull/2236>`__
  * Update controller mapping for :ref:`Hercules P32 DJ <hercules-p32-dj>` for more accurate headmix control `#3537 <https://github.com/mixxxdj/mixxx/pull/3537>`__
  * Update controller mapping for :ref:`Native Instruments Traktor Kontrol S4MK2 <native-instruments-traktor-kontrol-s2-mk3>` to add auto-slip mode and pitch fader range `#3331 <https://github.com/mixxxdj/mixxx/pull/3331>`__
  * Fix :ref:`Pioneer DDJ-SB2 <pioneer-ddj-sb2>` controller mapping auto tempo going to infinity bug `#2559 <https://github.com/mixxxdj/mixxx/pull/2559>`__ `lp:1846403 <https://bugs.launchpad.net/mixxx/+bug/1846403>`__
  * Fix :ref:`Numark Mixtrack Pro 3 <numark-mixtrack-pro-3>` controller mapping inverted FX on/off control `#3758 <https://github.com/mixxxdj/mixxx/pull/3758>`__
  * Gracefully handle MIDI overflow `#825 <https://github.com/mixxxdj/mixxx/pull/825>`__

*Development*

  * Add CMake build system with ``ccache`` and ``sccache`` support for faster compilation times and remove SCons `#2280 <https://github.com/mixxxdj/mixxx/pull/2280>`__ `#3618 <https://github.com/mixxxdj/mixxx/pull/3618>`__
  * Make Mixxx compile even though ``QT_NO_OPENGL`` or ``QT_OPENGL_ES_2`` is defined (fixes build on Raspberry Pi) `lp:1863440 <https://bugs.launchpad.net/mixxx/+bug/1863440>`__ `#2504 <https://github.com/mixxxdj/mixxx/pull/2504>`__
  * Fix ARM build issues `#3602 <https://github.com/mixxxdj/mixxx/pull/3602>`__
  * Fix missing manual in DEB package `lp:1889776 <https://bugs.launchpad.net/mixxx/+bug/1889776>`__ `#2985 <https://github.com/mixxxdj/mixxx/pull/2985>`__
  * Add macOS codesigning and notarization to fix startup warnings `#3281 <https://github.com/mixxxdj/mixxx/pull/3281>`__
  * Don't trash user configuration if an error occurs when writing `#3192 <https://github.com/mixxxdj/mixxx/pull/3192>`__
  * Enable CUE sheet recording by default `#3374 <https://github.com/mixxxdj/mixxx/pull/3374>`__
  * Fix crash when double clicking GLSL waveforms with right mouse button `#3904 <https://github.com/mixxxdj/mixxx/pull/3904>`__
  * Derive Mixxx version from `git describe` `#3824 <https://github.com/mixxxdj/mixxx/pull/3824>`__ `#3841 <https://github.com/mixxxdj/mixxx/pull/3841>`__ `#3848 <https://github.com/mixxxdj/mixxx/pull/3848>`__
  * Improve tapping the bpm of a deck `#3790 <https://github.com/mixxxdj/mixxx/pull/3790>`__ `lp:1882776 <https://bugs.launchpad.net/mixxx/+bug/1882776>`__
  * And countless other small fixes and improvements (too many to list them all!)

2.2.4 (2020-06-27)
------------------

  * Store default recording format after "Restore Defaults" `lp:1857806 <https://bugs.launchpad.net/mixxx/+bug/1857806>`__ `#2414 <https://github.com/mixxxdj/mixxx/pull/2414>`__
  * Prevent infinite loop when decoding corrupt MP3 files `#2417 <https://github.com/mixxxdj/mixxx/pull/2417>`__
  * Add workaround for broken libshout versions `#2040 <https://github.com/mixxxdj/mixxx/pull/2040>`__ `#2438 <https://github.com/mixxxdj/mixxx/pull/2438>`__
  * Speed up purging of tracks `lp:1845837 <https://bugs.launchpad.net/mixxx/+bug/1845837>`__ `#2393 <https://github.com/mixxxdj/mixxx/pull/2393>`__
  * Don't stop playback if vinyl passthrough input is configured and PASS button is pressed `#2474 <https://github.com/mixxxdj/mixxx/pull/2474>`__
  * Fix debug assertion for invalid crate names `lp:1861431 <https://bugs.launchpad.net/mixxx/+bug/1861431>`__ `#2477 <https://github.com/mixxxdj/mixxx/pull/2477>`__
  * Fix crashes when executing actions on tracks that already disappeared from the DB `#2527 <https://github.com/mixxxdj/mixxx/pull/2527>`__
  * AutoDJ: Skip next track when both deck are playing `lp:1399974 <https://bugs.launchpad.net/mixxx/+bug/1399974>`__ `#2531 <https://github.com/mixxxdj/mixxx/pull/2531>`__
  * Tweak scratch parameters for Mixtrack Platinum `#2028 <https://github.com/mixxxdj/mixxx/pull/2028>`__
  * Fix auto tempo going to infinity on Pioneer DDJ-SB2 `#2559 <https://github.com/mixxxdj/mixxx/pull/2559>`__
  * Fix bpm.tapButton logic and reject missed & double taps `#2594 <https://github.com/mixxxdj/mixxx/pull/2594>`__
  * Add controller mapping for Native Instruments Traktor Kontrol S2 MK3 `#2348 <https://github.com/mixxxdj/mixxx/pull/2348>`__
  * Add controller mapping for Soundless joyMIDI `#2425 <https://github.com/mixxxdj/mixxx/pull/2425>`__
  * Add controller mapping for Hercules DJControl Inpulse 300 `#2465 <https://github.com/mixxxdj/mixxx/pull/2465>`__
  * Add controller mapping for Denon MC7000 `#2546 <https://github.com/mixxxdj/mixxx/pull/2546>`__
  * Add controller mapping for Stanton DJC.4 `#2607 <https://github.com/mixxxdj/mixxx/pull/2607>`__
  * Fix broadcasting via broadcast/recording input `lp:1876222 <https://bugs.launchpad.net/mixxx/+bug/1876222>`__ `#2743 <https://github.com/mixxxdj/mixxx/pull/2743>`__
  * Only apply ducking gain in manual ducking mode when talkover is enabed `lp:1394968 <https://bugs.launchpad.net/mixxx/+bug/1394968>`__ `lp:1737113 <https://bugs.launchpad.net/mixxx/+bug/1737113>`__ `lp:1662536 <https://bugs.launchpad.net/mixxx/+bug/1662536>`__ `#2759 <https://github.com/mixxxdj/mixxx/pull/2759>`__
  * Ignore MIDI Clock Messages (0xF8) because they are not usable in Mixxx and inhibited the screensaver `#2786 <https://github.com/mixxxdj/mixxx/pull/2786>`__


2.2.3 (2019-11-24)
------------------

  * Don’t make users reconfigure sound hardware when it has not changed `#2253 <https://github.com/mixxxdj/mixxx/pull/2253>`__
  * Fix MusicBrainz metadata lookup `lp:1848887 <https://bugs.launchpad.net/mixxx/+bug/1848887>`__ `#2328 <https://github.com/mixxxdj/mixxx/pull/2328>`__
  * Fix high DPI scaling of cover art `#2247 <https://github.com/mixxxdj/mixxx/pull/2247>`__
  * Fix high DPI scaling of cue point labels on scrolling waveforms `#2331 <https://github.com/mixxxdj/mixxx/pull/2331>`__
  * Fix high DPI scaling of sliders in Tango skin `#2318 <https://github.com/mixxxdj/mixxx/pull/2318>`__
  * Fix sound dropping out during recording `lp:1842679 <https://bugs.launchpad.net/mixxx/+bug/1842679>`__ `#2265 <https://github.com/mixxxdj/mixxx/pull/2265>`__ `#2305 <https://github.com/mixxxdj/mixxx/pull/2305>`__ `#2308 <https://github.com/mixxxdj/mixxx/pull/2308>`__ `#2309 <https://github.com/mixxxdj/mixxx/pull/2309>`__
  * Fix rare crash on application shutdown `#2293 <https://github.com/mixxxdj/mixxx/pull/2293>`__
  * Workaround various rare bugs caused by database inconsistencies `lp:1846971 <https://bugs.launchpad.net/mixxx/+bug/1846971>`__ `#2321 <https://github.com/mixxxdj/mixxx/pull/2321>`__
  * Improve handling of corrupt FLAC files `#2315 <https://github.com/mixxxdj/mixxx/pull/2315>`__
  * Don’t immediately jump to loop start when loop_out is pressed in quantized mode `lp:1837077 <https://bugs.launchpad.net/mixxx/+bug/1837077>`__ `#2269 <https://github.com/mixxxdj/mixxx/pull/2269>`__
  * Preserve order of tracks when dragging and dropping from AutoDJ to playlist `lp:1829601 <https://bugs.launchpad.net/mixxx/+bug/1829601>`__ `#2237 <https://github.com/mixxxdj/mixxx/pull/2237>`__
  * Explicitly use X11 Qt platform plugin instead of Wayland in .desktop launcher `lp:1850729 <https://bugs.launchpad.net/mixxx/+bug/1850729>`__ `#2340 <https://github.com/mixxxdj/mixxx/pull/2340>`__
  * Pioneer DDJ-SX: fix delayed sending of MIDI messages with low audio buffer sizes `#2326 <https://github.com/mixxxdj/mixxx/pull/2326>`__
  * Enable modplug support on Linux by default `lp:1840537 <https://bugs.launchpad.net/mixxx/+bug/1840537>`__ `#2244 <https://github.com/mixxxdj/mixxx/pull/2244>`__ `#2272 <https://github.com/mixxxdj/mixxx/pull/2272>`__
  * Fix keyboard shortcut for View > Skin Preferences `lp:1851993 <https://bugs.launchpad.net/mixxx/+bug/1851993>`__ `#2358 <https://github.com/mixxxdj/mixxx/pull/2358>`__ `#2372 <https://github.com/mixxxdj/mixxx/pull/2372>`__
  * Reloop Terminal Mix: Fix mapping of sampler buttons 5-8 `lp:1846966 <https://bugs.launchpad.net/mixxx/+bug/1846966>`__ `#2330 <https://github.com/mixxxdj/mixxx/pull/2330>`__


2.2.2 (2019-08-10)
------------------

  * Fix battery widget with upower <= 0.99.7. `#2221 <https://github.com/mixxxdj/mixxx/pull/2221>`__
  * Fix BPM adjust in BpmControl. `lp:1836480 <https://bugs.launchpad.net/mixxx/+bug/1836480>`__
  * Disable track metadata export for .ogg files and TagLib 1.11.1. `lp:1833190 <https://bugs.launchpad.net/mixxx/+bug/1833190>`__
  * Fix interaction of hot cue buttons and looping. `lp:1778246 <https://bugs.launchpad.net/mixxx/+bug/1778246>`__
  * Fix detection of moved tracks. `#2197 <https://github.com/mixxxdj/mixxx/pull/2197>`__
  * Fix playlist import. `lp:1687828 <https://bugs.launchpad.net/mixxx/+bug/1687828>`__
  * Fix updating playlist labels. `lp:1837315 <https://bugs.launchpad.net/mixxx/+bug/1837315>`__
  * Fix potential segfault on exit. `lp:1828360 <https://bugs.launchpad.net/mixxx/+bug/1828360>`__
  * Fix parsing of invalid bpm values in MP3 files. `lp:1832325 <https://bugs.launchpad.net/mixxx/+bug/1832325>`__
  * Fix crash when removing rows from empty model. `#2128 <https://github.com/mixxxdj/mixxx/pull/2128>`__
  * Fix high DPI scaling of RGB overview waveforms. `#2090 <https://github.com/mixxxdj/mixxx/pull/2090>`__
  * Fix for OpenGL SL detection on macOS. `lp:1828019 <https://bugs.launchpad.net/mixxx/+bug/1828019>`__
  * Fix OpenGL ES detection. `lp:1825461 <https://bugs.launchpad.net/mixxx/+bug/1825461>`__
  * Fix FX1/2 buttons missing Mic unit in Deere (64 samplers). `lp:1837716 <https://bugs.launchpad.net/mixxx/+bug/1837716>`__
  * Tango64: Re-enable 64 samplers. `#2223 <https://github.com/mixxxdj/mixxx/pull/2223>`__
  * Numark DJ2Go re-enable note-off for deck A cue button. `#2087 <https://github.com/mixxxdj/mixxx/pull/2087>`__
  * Replace Flanger with QuickEffect in keyboard mapping. `#2233 <https://github.com/mixxxdj/mixxx/pull/2233>`__


2.2.1 (2019-04-22)
------------------

  * Include all fixes from Mixxx 2.1.7 and 2.1.8
  * Fix high CPU usage on MAC due to preview column `lp:1812763 <https://bugs.launchpad.net/mixxx/+bug/1812763>`__
  * Fix HID controller output on Windows with common-hid-packet-parser.js
  * Fix rendering slow down by not using QStylePainter in WSpinny `lp:1530720 <https://bugs.launchpad.net/mixxx/+bug/1530720>`__
  * Fix broken Mic mute button `lp:1782568 <https://bugs.launchpad.net/mixxx/+bug/1782568>`__
  * added quick effect enable button to the control picker menu
  * Fix Cover Window close issue with empty cover arts
  * Fix Numark Mixtrack 3 mapping. `#2057 <https://github.com/mixxxdj/mixxx/pull/2057>`__


2.2.0 (2018-12-17)
------------------

*General*

  * Update from Qt4 to Qt5.
  * Use Qt5's automatic high DPI scaling (and remove the old scaling option from the preferences).
  * Vectorize remaining raster graphics for better HiDPI support.

*Effects*

  * Add mix mode switch (Dry/Wet vs Dry+Wet) for effect units.
  * Add support for LV2 effects plugins (currently no way to show plugin GUIs).
  * Add preference option for selecting which effects are shown in the list of available effects in the main window (all LV2 effects are hidden by default and must be explicitly enabled by users).

*Skins*

  * Add 8 sampler and small sampler options to LateNight.
  * Add key / BPM expansion indicators to Deere decks.
  * Add skin settings menu to LateNight.

*Controllers*

  * Add controller mapping for Numark Mixtrack Platinum.
  * Update controller mapping for Numark N4.
  * Add spinback and break for Vestax VCI-400 mapping.

*Miscellaneous*

  * Add preference option to adjust the play position marker of scrolling waveforms.
  * Add preference option to adjust opacity of beatgrid markers on scrolling waveforms.
  * Support IRC/AIM/ICQ broadcast metadata.


2.1.8 (2019-04-07)
------------------

  * Fix a rare chance for a corrupt track file while writing metadata in out of disk situations. `lp:1815305 <https://bugs.launchpad.net/mixxx/+bug/1815305>`__
  * Fix export of BPM track file metadata. `lp:1816490 <https://bugs.launchpad.net/mixxx/+bug/1816490>`__
  * Fix sending of broadcast metadata with TLS enabled libshout 2.4.1. `lp:1817395 <https://bugs.launchpad.net/mixxx/+bug/1817395>`__
  * Fix resdicovering purged tracks in all cases. `lp:1821514 <https://bugs.launchpad.net/mixxx/+bug/1821514>`__
  * Fix dropping track from OSX Finder. `lp:1822424 <https://bugs.launchpad.net/mixxx/+bug/1822424>`__


2.1.7 (2019-01-15)
------------------

  * Fix syncing to doublespeed `lp:1808697 <https://bugs.launchpad.net/mixxx/+bug/1808697>`__
  * Fix issues when changing beats of a synced track `lp:1808698 <https://bugs.launchpad.net/mixxx/+bug/1808698>`__
  * Fix direction of pitch bend buttons when inverting rate slider `lp:1770745 <https://bugs.launchpad.net/mixxx/+bug/1770745>`__
  * Use first loaded deck if no playing deck is found `lp:1784185 <https://bugs.launchpad.net/mixxx/+bug/1784185>`__
  * Encode file names correctly on macOS `lp:1776949 <https://bugs.launchpad.net/mixxx/+bug/1776949>`__


2.1.6 (2018-12-23)
------------------

  * Fix crash when loading a Qt5 Soundsource / Vamp Plug-In. `lp:1774639 <https://bugs.launchpad.net/mixxx/+bug/1774639>`__
  * Validate effect parameter range. `lp:1795234 <https://bugs.launchpad.net/mixxx/+bug/1795234>`__
  * Fix crash using the bpm_tap button without a track loaded. `lp:1801844 <https://bugs.launchpad.net/mixxx/+bug/1801844>`__
  * Fix possible crash after ejecting a track. `lp:1801874 <https://bugs.launchpad.net/mixxx/+bug/1801874>`__
  * Fix wrong bitrate reported for faulty mp3 files. `lp:1782912 <https://bugs.launchpad.net/mixxx/+bug/1782912>`__
  * Fix Echo effect syncing `lp:1793232 <https://bugs.launchpad.net/mixxx/+bug/1793232>`__
  * Fix iTunes context menu `lp:1799932 <https://bugs.launchpad.net/mixxx/+bug/1799932>`__
  * Fix loading the wrong track after delete search and scroll. `lp:1803148 <https://bugs.launchpad.net/mixxx/+bug/1803148>`__
  * Improve search bar timing. `lp:1635087 <https://bugs.launchpad.net/mixxx/+bug/1635087>`__
  * Fix quoted search sentence. `lp:1784141 <https://bugs.launchpad.net/mixxx/+bug/1784141>`__
  * Fix loading a track formerly not existing. `lp:1800395 <https://bugs.launchpad.net/mixxx/+bug/1800395>`__
  * Fix importing m3u files with blank lines. `lp:1806271 <https://bugs.launchpad.net/mixxx/+bug/1806271>`__
  * Fix position in sampler overview waveforms. `lp:1744170 <https://bugs.launchpad.net/mixxx/+bug/1744170>`__
  * Don’t reset rate slider, syncing a track without a beatgrid. `lp:1783020 <https://bugs.launchpad.net/mixxx/+bug/1783020>`__
  * Clean up iTunes track context menu. `lp:1800335 <https://bugs.launchpad.net/mixxx/+bug/1800335>`__
  * Collapsed sampler are not analyzed on startup. `lp:1801126 <https://bugs.launchpad.net/mixxx/+bug/1801126>`__
  * search for decoration characters like “˚”. `lp:1802730 <https://bugs.launchpad.net/mixxx/+bug/1802730>`__
  * Fix cue button blinking after pressing eject on an empty deck. `lp:1808222 <https://bugs.launchpad.net/mixxx/+bug/1808222>`__


2.1.5 (2018-10-28)
------------------

  * Code signing for Windows builds. `lp:1517823 <https://bugs.launchpad.net/mixxx/+bug/1517823>`__
  * Fix crash on exit when preferences is open. `lp:1793185 <https://bugs.launchpad.net/mixxx/+bug/1793185>`__
  * Fix crash when analyzing corrupt MP3s. `lp:1793387 <https://bugs.launchpad.net/mixxx/+bug/1793387>`__
  * Fix crash when importing metadata from MusicBrainz. `lp:1794993 <https://bugs.launchpad.net/mixxx/+bug/1794993>`__
  * Library search fixes when single quotes are used. `lp:1784090 <https://bugs.launchpad.net/mixxx/+bug/1784090>`__ `lp:1789728 <https://bugs.launchpad.net/mixxx/+bug/1789728>`__
  * Fix scrolling waveform on Windows with WDM-KS sound API. `lp:1729345 <https://bugs.launchpad.net/mixxx/+bug/1729345>`__
  * Fix right clicking on beatgrid alignment button in Tango and LateNight skins. `lp:1798237 <https://bugs.launchpad.net/mixxx/+bug/1798237>`__
  * Improve speed of importing iTunes library. `lp:1785545 <https://bugs.launchpad.net/mixxx/+bug/1785545>`__
  * Add 2 deck mapping for DJTechTools MIDI Fighter Twister.


2.1.4 (2018-08-29)
------------------

  * Fix track selection not getting shown in the track table on Windows. There are no changes to the source code, but the Jenkins build configuration was changed to delete the Jenkins workspace before each build. `lp:1751482 <https://bugs.launchpad.net/mixxx/+bug/1751482>`__


2.1.3 (2018-08-20)
------------------

  * Fix a severe `performance regression on Windows <https://mixxx.discourse.group/t/mixxx-2-1-2-running-much-slower-than-2-1-1/17447>`__


2.1.2 (2018-08-10)
------------------

  * Allow maximum deck speed of 4x normal.
  * Don’t always quantize hotcues, a 2.1.1 regression. `lp:1777429 <https://bugs.launchpad.net/mixxx/+bug/1777429>`__
  * Fix artifacts using more than 32 samplers. `lp:1779559 <https://bugs.launchpad.net/mixxx/+bug/1779559>`__
  * store No EQ and Filter persistently. `lp:1780479 <https://bugs.launchpad.net/mixxx/+bug/1780479>`__
  * Pad unreadable samples with silence on cache miss. `lp:1777480 <https://bugs.launchpad.net/mixxx/+bug/1777480>`__
  * Fixing painting of preview column for Qt5 builds. `lp:1776555 <https://bugs.launchpad.net/mixxx/+bug/1776555>`__
  * LateNight: Fix play button right click. `lp:1781829 <https://bugs.launchpad.net/mixxx/+bug/1781829>`__
  * LateNight: Added missing sort up/down buttons.
  * Fix sampler play button tooltips. `lp:1779468 <https://bugs.launchpad.net/mixxx/+bug/1779468>`__
  * Shade: remove superfluid margins and padding in sampler.xml. `lp:1773588 <https://bugs.launchpad.net/mixxx/+bug/1773588>`__
  * Deere: Fix background-color code.
  * ITunes: Don’t stop import in case of duplicated Playlists. `lp:1783493 <https://bugs.launchpad.net/mixxx/+bug/1783493>`__


2.1.1 (2018-06-13)
------------------

  * Require Soundtouch 2.0 to avoid segfault. `lp:1577042 <https://bugs.launchpad.net/mixxx/+bug/1577042>`__
  * Improved skins including library view fix. `lp:1773709 <https://bugs.launchpad.net/mixxx/+bug/1773709>`__ `lp:1772202 <https://bugs.launchpad.net/mixxx/+bug/1772202>`__
  * `lp:1763953 <https://bugs.launchpad.net/mixxx/+bug/1763953>`__
  * Fix crash when importing ID3v2 APIC frames. `lp:1774790 <https://bugs.launchpad.net/mixxx/+bug/1774790>`__
  * Synchronize execution of Vamp analyzers. `lp:1743256 <https://bugs.launchpad.net/mixxx/+bug/1743256>`__
  * DlgTrackInfo: Mismatching signal/slot connection.
  * Detect M4A decoding errors on Windows. `lp:1766834 <https://bugs.launchpad.net/mixxx/+bug/1766834>`__
  * Fix spinback inertia effect.
  * Fix decoding fixes and upgrade DB schema. `lp:1766042 <https://bugs.launchpad.net/mixxx/+bug/1766042>`__ `lp:1769717 <https://bugs.launchpad.net/mixxx/+bug/1769717>`__
  * Fix integration of external track libraries. `lp:1766360 <https://bugs.launchpad.net/mixxx/+bug/1766360>`__
  * Fix memory leak when loading cover art. `lp:1767068 <https://bugs.launchpad.net/mixxx/+bug/1767068>`__
  * Fix clearing of ReplayGain gain/ratio in file tags. `lp:1766094 <https://bugs.launchpad.net/mixxx/+bug/1766094>`__
  * Fix crash when removing a quick link. `lp:1510068 <https://bugs.launchpad.net/mixxx/+bug/1510068>`__
  * Fidlib: Thread-safe and reentrant generation of filters. `lp:1765210 <https://bugs.launchpad.net/mixxx/+bug/1765210>`__
  * Fix unresponsive scrolling through crates & playlists using encoder. `lp:1719474 <https://bugs.launchpad.net/mixxx/+bug/1719474>`__
  * Swap default values for temp/perm rate changes. `lp:1764254 <https://bugs.launchpad.net/mixxx/+bug/1764254>`__


2.1.0 (2018-04-15)
------------------

  * Graphical interface scales for high resolution screens
  * Overhauled Deere and LateNight skins
  * New Tango skin
  * Resizable waveforms
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

For a full list of new features and bugfixes, go to:
`https://launchpad.net/mixxx/2.1 <https://launchpad.net/mixxx/+milestone/2.1.0>`_.


2.0.0 (2015-12-31)
------------------

  * 4 Decks with Master Sync
  * New Effects Framework with 4 Effect Units and 5 Built-in Effects:
    * Flanger, Bit Crusher, Reverb, Echo, Filter
    * More to come!
  * Configurable, Resizeable User Interface with 3 Brand New Skins
  * Cover Art Display
  * Music Key Detection and Shifting
  * Vinyl Audio Pass-Through
  * 4 Microphone inputs and 4 Auxiliary inputs
  * MIDI Mapping GUI and Improved Learning Wizard
  * MusicBrainz metadata fetching
  * RGB Musical Waveforms
  * Hundreds of Bug Fixes and Improvements
  * New Pitch-Independent Algorithm for Better-Sounding Key-lock

For a full list of new features and bugfixes, go to:
`https://launchpad.net/mixxx/2.0 <https://launchpad.net/mixxx/+milestone/2.0.0>`_.

.. seealso:: For an overview of previous versions, `take a look
             <https://launchpad.net/mixxx/+series>`_ at the timeline.
