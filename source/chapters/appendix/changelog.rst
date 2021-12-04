.. This is a generated file. Do not edit it manually, because it is updated
   automatically via tools/update_changelog.py.

.. include:: /shortcuts.rstext

.. _appendix-changelog:


Changelog
=========

.. _v2-4-0:

`2.4.0 <https://launchpad.net/mixxx/+milestone/2.4.0>`_ (Unreleased)
------------------------------------------------------------------------

Cover Art
^^^^^^^^^


* Prevent wrong cover art display due to hash conflicts `#2524 <https://github.com/mixxxdj/mixxx/pull/2524>`_
* Add background color for quick cover art preview `#2524 <https://github.com/mixxxdj/mixxx/pull/2524>`_

Music Library
^^^^^^^^^^^^^


* Ensure that tracks with an invalid BPM are re-analyzed `#2776 <https://github.com/mixxxdj/mixxx/pull/2776>`_
* Add support for exporting crates, playlists and the library to Engine Prime and Denon standalone controllers
  `#2753 <https://github.com/mixxxdj/mixxx/pull/2753>`_
  `#2932 <https://github.com/mixxxdj/mixxx/pull/2932>`_
  `#3102 <https://github.com/mixxxdj/mixxx/pull/3102>`_
  `#3155 <https://github.com/mixxxdj/mixxx/pull/3155>`_
  `#3621 <https://github.com/mixxxdj/mixxx/pull/3621>`_
  `#3776 <https://github.com/mixxxdj/mixxx/pull/3776>`_
  `#3787 <https://github.com/mixxxdj/mixxx/pull/3787>`_
  `#3797 <https://github.com/mixxxdj/mixxx/pull/3797>`_
  `#3798 <https://github.com/mixxxdj/mixxx/pull/3798>`_
  `#4025 <https://github.com/mixxxdj/mixxx/pull/4025>`_
  `#4087 <https://github.com/mixxxdj/mixxx/pull/4087>`_
  `#4102 <https://github.com/mixxxdj/mixxx/pull/4102>`_
  `#4143 <https://github.com/mixxxdj/mixxx/pull/4143>`_
* Rekordbox: Save all loops and correct AAC timing offset for CoreAudio `#2779 <https://github.com/mixxxdj/mixxx/pull/2779>`_
* Improve log messages during schema migration `#2979 <https://github.com/mixxxdj/mixxx/pull/2979>`_
* Search related tracks in collection
  `#3181 <https://github.com/mixxxdj/mixxx/pull/3181>`_
  `#3213 <https://github.com/mixxxdj/mixxx/pull/3213>`_
  `#2796 <https://github.com/mixxxdj/mixxx/pull/2796>`_
  `#4207 <https://github.com/mixxxdj/mixxx/pull/4207>`_
* Add recent searches to a drop down menu of the search box
  `#3171 <https://github.com/mixxxdj/mixxx/pull/3171>`_
  `#3262 <https://github.com/mixxxdj/mixxx/pull/3262>`_
* Add new "[AutoDJ],add_random_track" to make this feature accessible from controllers `#3076 <https://github.com/mixxxdj/mixxx/pull/3076>`_
* Add new library column that shows the last time a track was played
  `#3140 <https://github.com/mixxxdj/mixxx/pull/3140>`_
  `#3457 <https://github.com/mixxxdj/mixxx/pull/3457>`_
  `#3494 <https://github.com/mixxxdj/mixxx/pull/3494>`_
  `#3596 <https://github.com/mixxxdj/mixxx/pull/3596>`_
  `#3740 <https://github.com/mixxxdj/mixxx/pull/3740>`_
* Improve presentation of the history library tree `#2996 <https://github.com/mixxxdj/mixxx/pull/2996>`_
* Don't store or update metadata of missing tracks in the Mixxx database to prevent inconsistencies with file tags `#3811 <https://github.com/mixxxdj/mixxx/pull/3811>`_
* Code improvements and minor bug fixes when importing track metadata
  `#3851 <https://github.com/mixxxdj/mixxx/pull/3851>`_
  `#3858 <https://github.com/mixxxdj/mixxx/pull/3858>`_
  `#3860 <https://github.com/mixxxdj/mixxx/pull/3860>`_
  `#3866 <https://github.com/mixxxdj/mixxx/pull/3866>`_
  `#3871 <https://github.com/mixxxdj/mixxx/pull/3871>`_
  `#3870 <https://github.com/mixxxdj/mixxx/pull/3870>`_
  `#3924 <https://github.com/mixxxdj/mixxx/pull/3924>`_
  `#3906 <https://github.com/mixxxdj/mixxx/pull/3906>`_
  `#3998 <https://github.com/mixxxdj/mixxx/pull/3998>`_
* Update library schema to 37 for synchronizing file modified time with track source on metadata import/export
  `#3978 <https://github.com/mixxxdj/mixxx/pull/3978>`_
  `#4012 <https://github.com/mixxxdj/mixxx/pull/4012>`_
* Logging: Suppress expected and harmless schema migration errors `#4248 <https://github.com/mixxxdj/mixxx/pull/4248>`_
* Only show the date in Date Added / Last Played columns. Move the time of day to tooltips `#3945 <https://github.com/mixxxdj/mixxx/pull/3945>`_
* Fix handling of undefined BPM values
  `#4062 <https://github.com/mixxxdj/mixxx/pull/4062>`_
  `#4063 <https://github.com/mixxxdj/mixxx/pull/4063>`_
  `#4100 <https://github.com/mixxxdj/mixxx/pull/4100>`_
  `#4154 <https://github.com/mixxxdj/mixxx/pull/4154>`_
  `#4165 <https://github.com/mixxxdj/mixxx/pull/4165>`_
  `#4168 <https://github.com/mixxxdj/mixxx/pull/4168>`_
* Add support for m4v files `#4088 <https://github.com/mixxxdj/mixxx/pull/4088>`_
* Adjust ReplayGain: Allow user to update the replaygain value based on a deck pregain value `#4031 <https://github.com/mixxxdj/mixxx/pull/4031>`_
* Automatic analyze and optimize database `#4199 <https://github.com/mixxxdj/mixxx/pull/4199>`_
* Re-import and update metadata after files have been modified when loading tracks `#4218 <https://github.com/mixxxdj/mixxx/pull/4218>`_
* Fix playlists sidebar navigation/activation `#4193 <https://github.com/mixxxdj/mixxx/pull/4193>`_ `lp:1939082 <https://bugs.launchpad.net/mixxx/+bug/1939082>`_
* Refactoring of library code
  `#2756 <https://github.com/mixxxdj/mixxx/pull/2756>`_
  `#2717 <https://github.com/mixxxdj/mixxx/pull/2717>`_
  `#2715 <https://github.com/mixxxdj/mixxx/pull/2715>`_
  `#2810 <https://github.com/mixxxdj/mixxx/pull/2756>`_
  `#2900 <https://github.com/mixxxdj/mixxx/pull/2900>`_
  `#2906 <https://github.com/mixxxdj/mixxx/pull/2906>`_
  `#2925 <https://github.com/mixxxdj/mixxx/pull/2925>`_
  `#3017 <https://github.com/mixxxdj/mixxx/pull/3017>`_
  `#3475 <https://github.com/mixxxdj/mixxx/pull/3475>`_
  `#4164 <https://github.com/mixxxdj/mixxx/pull/4164>`_
  `#4152 <https://github.com/mixxxdj/mixxx/pull/4152>`_
  `#4162 <https://github.com/mixxxdj/mixxx/pull/4162>`_
  `#4101 <https://github.com/mixxxdj/mixxx/pull/4101>`_
  `#4214 <https://github.com/mixxxdj/mixxx/pull/4214>`_

Sync
^^^^


* Add support for setting an explicit leader for sync lock
  `#2768 <https://github.com/mixxxdj/mixxx/pull/2768>`_
  `#3099 <https://github.com/mixxxdj/mixxx/pull/3099>`_
  `#3695 <https://github.com/mixxxdj/mixxx/pull/3695>`_
  `#3734 <https://github.com/mixxxdj/mixxx/pull/3734>`_
  `#3698 <https://github.com/mixxxdj/mixxx/pull/3698>`_
  `#3864 <https://github.com/mixxxdj/mixxx/pull/3864>`_
  `#3867 <https://github.com/mixxxdj/mixxx/pull/3867>`_
  `#3921 <https://github.com/mixxxdj/mixxx/pull/3921>`_
  `#4119 <https://github.com/mixxxdj/mixxx/pull/4119>`_
  `#4135 <https://github.com/mixxxdj/mixxx/pull/4135>`_
  `#4149 <https://github.com/mixxxdj/mixxx/pull/4149>`_
* Fix issue with half/double BPM calculation when using sync
  `#3899 <https://github.com/mixxxdj/mixxx/pull/3899>`_
  `#3706 <https://github.com/mixxxdj/mixxx/pull/3706>`_
* Sync Lock: Don't seek phase when disabling sync `#4169 <https://github.com/mixxxdj/mixxx/pull/4169>`_

Audio Codecs
^^^^^^^^^^^^


* Fix recovering from FAAD2 decoding issues `#2850 <https://github.com/mixxxdj/mixxx/pull/2850>`_

Audio Engine
^^^^^^^^^^^^


* Add support for Saved loops
  `#2194 <https://github.com/mixxxdj/mixxx/pull/2194>`_
  `#3267 <https://github.com/mixxxdj/mixxx/pull/3267>`_
  `#3202 <https://github.com/mixxxdj/mixxx/pull/3202>`_
* Fix an issue when pressing multiple cue buttons at the same time `#3382 <https://github.com/mixxxdj/mixxx/pull/3382>`_
* Fix synchronization of main cue point/position
  `#4137 <https://github.com/mixxxdj/mixxx/pull/4137>`_
  `lp1937074 <https://bugs.launchpad.net/mixxx/+bug/1937074>`_
  `#4153 <https://github.com/mixxxdj/mixxx/pull/4153>`_
* Refactoring of beatgrid/beatmap code
  `#4044 <https://github.com/mixxxdj/mixxx/pull/4044>`_
  `#4048 <https://github.com/mixxxdj/mixxx/pull/4048>`_
  `#4045 <https://github.com/mixxxdj/mixxx/pull/4045>`_
  `#4049 <https://github.com/mixxxdj/mixxx/pull/4049>`_
  `#4092 <https://github.com/mixxxdj/mixxx/pull/4092>`_
  `#4094 <https://github.com/mixxxdj/mixxx/pull/4094>`_
  `#4104 <https://github.com/mixxxdj/mixxx/pull/4104>`_
  `#4103 <https://github.com/mixxxdj/mixxx/pull/4103>`_
  `#4127 <https://github.com/mixxxdj/mixxx/pull/4127>`_
  `#4099 <https://github.com/mixxxdj/mixxx/pull/4099>`_
  `#4071 <https://github.com/mixxxdj/mixxx/pull/4071>`_
  `#4184 <https://github.com/mixxxdj/mixxx/pull/4184>`_
  `#4234 <https://github.com/mixxxdj/mixxx/pull/4234>`_
  `#4233 <https://github.com/mixxxdj/mixxx/pull/4233>`_
  `#4258 <https://github.com/mixxxdj/mixxx/pull/4258>`_
  `#4259 <https://github.com/mixxxdj/mixxx/pull/4259>`_
  `#4263 <https://github.com/mixxxdj/mixxx/pull/4263>`_
  `#4272 <https://github.com/mixxxdj/mixxx/pull/4272>`_
* Refactoring of audio engine code
  `#2762 <https://github.com/mixxxdj/mixxx/pull/2762>`_
  `#2801 <https://github.com/mixxxdj/mixxx/pull/2801>`_
  `#2885 <https://github.com/mixxxdj/mixxx/pull/2885>`_
  `#2997 <https://github.com/mixxxdj/mixxx/pull/2997>`_
  `#3266 <https://github.com/mixxxdj/mixxx/pull/3266>`_
  `#4064 <https://github.com/mixxxdj/mixxx/pull/4064>`_
  `#4065 <https://github.com/mixxxdj/mixxx/pull/4065>`_
  `#4066 <https://github.com/mixxxdj/mixxx/pull/4066>`_
  `#4069 <https://github.com/mixxxdj/mixxx/pull/4069>`_
  `#4074 <https://github.com/mixxxdj/mixxx/pull/4074>`_
  `#4075 <https://github.com/mixxxdj/mixxx/pull/4075>`_
  `#4076 <https://github.com/mixxxdj/mixxx/pull/4076>`_
  `#4078 <https://github.com/mixxxdj/mixxx/pull/4078>`_
  `#4082 <https://github.com/mixxxdj/mixxx/pull/4082>`_
  `#4077 <https://github.com/mixxxdj/mixxx/pull/4077>`_
  `#4080 <https://github.com/mixxxdj/mixxx/pull/4080>`_
  `#4086 <https://github.com/mixxxdj/mixxx/pull/4086>`_
  `#4089 <https://github.com/mixxxdj/mixxx/pull/4089>`_
  `#4090 <https://github.com/mixxxdj/mixxx/pull/4090>`_
  `#4079 <https://github.com/mixxxdj/mixxx/pull/4079>`_
  `#4091 <https://github.com/mixxxdj/mixxx/pull/4091>`_
  `#4083 <https://github.com/mixxxdj/mixxx/pull/4083>`_
  `#4095 <https://github.com/mixxxdj/mixxx/pull/4095>`_
  `#4081 <https://github.com/mixxxdj/mixxx/pull/4081>`_
  `#4061 <https://github.com/mixxxdj/mixxx/pull/4061>`_
  `#4105 <https://github.com/mixxxdj/mixxx/pull/4105>`_
  `#4183 <https://github.com/mixxxdj/mixxx/pull/4183>`_
  `#4186 <https://github.com/mixxxdj/mixxx/pull/4186>`_
  `#4189 <https://github.com/mixxxdj/mixxx/pull/4189>`_
  `#4216 <https://github.com/mixxxdj/mixxx/pull/4216>`_
  `#4221 <https://github.com/mixxxdj/mixxx/pull/4221>`_
  `#4219 <https://github.com/mixxxdj/mixxx/pull/4219>`_
  `#4191 <https://github.com/mixxxdj/mixxx/pull/4191>`_
  `#4232 <https://github.com/mixxxdj/mixxx/pull/4232>`_
  `#4231 <https://github.com/mixxxdj/mixxx/pull/4231>`_
  `#4229 <https://github.com/mixxxdj/mixxx/pull/4229>`_
  `#4257 <https://github.com/mixxxdj/mixxx/pull/4257>`_
  `#4266 <https://github.com/mixxxdj/mixxx/pull/4266>`_
  `#4217 <https://github.com/mixxxdj/mixxx/pull/4217>`_

Controllers
^^^^^^^^^^^


* Never raise a fatal error if a controller mapping tries access a non-existent control object `#2947 <https://github.com/mixxxdj/mixxx/pull/2947>`_
* Update Novation Launchpad controller scripts `#2600 <https://github.com/mixxxdj/mixxx/pull/2600>`_
* Add generic USB HID "Set Reports (Feature)" functionality `#3051 <https://github.com/mixxxdj/mixxx/pull/3051>`_
* Add support for reading the status of an HID controller (like MIDI SYSEX) `#3317 <https://github.com/mixxxdj/mixxx/pull/3317>`_
* Use hidapi's hidraw backend instead of libusb on Linux `#4054 <https://github.com/mixxxdj/mixxx/pull/4054>`_
* Consistently use "mapping" instead of "preset" to refer to controller mappings `#3472 <https://github.com/mixxxdj/mixxx/pull/3472>`_
* Introduce new control objects ``[Master],indicator_250millis`` and ``[Master],indicator_500millis`` `#4157 <https://github.com/mixxxdj/mixxx/pull/4157>`_
* Don't automatically enable controller if it was disabled before `#4244 <https://github.com/mixxxdj/mixxx/pull/4244>`_ `lp:1941042 <https://bugs.launchpad.net/mixxx/+bug/1941042>`_
* Roland DJ-505: Use new ControlIndicator COs for blinking lights `#4159 <https://github.com/mixxxdj/mixxx/pull/4159>`_
* Prepare code for upcoming ES6 based controller mapping system with module support
  `#2682 <https://github.com/mixxxdj/mixxx/pull/2682>`_
  `#2868 <https://github.com/mixxxdj/mixxx/pull/2868>`_
  `#2875 <https://github.com/mixxxdj/mixxx/pull/2875>`_
  `#2936 <https://github.com/mixxxdj/mixxx/pull/2936>`_
  `#2946 <https://github.com/mixxxdj/mixxx/pull/2946>`_
* Other refactorings of controller code
  `#2904 <https://github.com/mixxxdj/mixxx/pull/2904>`_
  `#3308 <https://github.com/mixxxdj/mixxx/pull/3308>`_
  `#3463 <https://github.com/mixxxdj/mixxx/pull/3463>`_
  `#3634 <https://github.com/mixxxdj/mixxx/pull/3634>`_
  `#3635 <https://github.com/mixxxdj/mixxx/pull/3635>`_
  `#3636 <https://github.com/mixxxdj/mixxx/pull/3636>`_
  `#3676 <https://github.com/mixxxdj/mixxx/pull/3676>`_
  `#3880 <https://github.com/mixxxdj/mixxx/pull/3880>`_
  `#4085 <https://github.com/mixxxdj/mixxx/pull/4085>`_

Skins
^^^^^


* Add experimental QML skin
  `#3345 <https://github.com/mixxxdj/mixxx/pull/3345>`_
  `#3446 <https://github.com/mixxxdj/mixxx/pull/3446>`_
  `#3854 <https://github.com/mixxxdj/mixxx/pull/3854>`_
  `#3891 <https://github.com/mixxxdj/mixxx/pull/3891>`_
  `#2874 <https://github.com/mixxxdj/mixxx/pull/2874>`_
  `#3915 <https://github.com/mixxxdj/mixxx/pull/3915>`_
  `#3894 <https://github.com/mixxxdj/mixxx/pull/3894>`_
  `#3920 <https://github.com/mixxxdj/mixxx/pull/3920>`_
  `#3907 <https://github.com/mixxxdj/mixxx/pull/3907>`_
  `#3925 <https://github.com/mixxxdj/mixxx/pull/3925>`_
  `#3928 <https://github.com/mixxxdj/mixxx/pull/3928>`_
  `#3932 <https://github.com/mixxxdj/mixxx/pull/3932>`_
  `#3911 <https://github.com/mixxxdj/mixxx/pull/3911>`_
  `#3937 <https://github.com/mixxxdj/mixxx/pull/3937>`_
  `#3940 <https://github.com/mixxxdj/mixxx/pull/3940>`_
  `#3913 <https://github.com/mixxxdj/mixxx/pull/3913>`_
  `#3950 <https://github.com/mixxxdj/mixxx/pull/3950>`_
  `#3919 <https://github.com/mixxxdj/mixxx/pull/3919>`_
  `#3955 <https://github.com/mixxxdj/mixxx/pull/3955>`_
  `#3957 <https://github.com/mixxxdj/mixxx/pull/3957>`_
  `#3961 <https://github.com/mixxxdj/mixxx/pull/3961>`_
  `#3952 <https://github.com/mixxxdj/mixxx/pull/3952>`_
  `#3963 <https://github.com/mixxxdj/mixxx/pull/3963>`_
  `#3971 <https://github.com/mixxxdj/mixxx/pull/3971>`_
  `#3959 <https://github.com/mixxxdj/mixxx/pull/3959>`_
  `#3972 <https://github.com/mixxxdj/mixxx/pull/3972>`_
  `#3992 <https://github.com/mixxxdj/mixxx/pull/3992>`_
  `#4003 <https://github.com/mixxxdj/mixxx/pull/4003>`_
  `#4004 <https://github.com/mixxxdj/mixxx/pull/4004>`_
  `#3999 <https://github.com/mixxxdj/mixxx/pull/3999>`_
  `#4000 <https://github.com/mixxxdj/mixxx/pull/4000>`_
  `#4067 <https://github.com/mixxxdj/mixxx/pull/4067>`_
  `#4068 <https://github.com/mixxxdj/mixxx/pull/4068>`_
  `#4060 <https://github.com/mixxxdj/mixxx/pull/4060>`_
  `#4037 <https://github.com/mixxxdj/mixxx/pull/4037>`_
  `#3934 <https://github.com/mixxxdj/mixxx/pull/3934>`_
  `#4117 <https://github.com/mixxxdj/mixxx/pull/4117>`_
* Add new "RGB Stacked" waveform `#3153 <https://github.com/mixxxdj/mixxx/pull/3153>`_
* Add harmonic keywheel window
  `#1695 <https://github.com/mixxxdj/mixxx/pull/1695>`_
  `#3622 <https://github.com/mixxxdj/mixxx/pull/3622>`_
  `#3624 <https://github.com/mixxxdj/mixxx/pull/3624>`_
* Make beat indicator control behaviour more natural `#3608 <https://github.com/mixxxdj/mixxx/pull/3608>`_
* Fix crash if no skin is available
  `#3918 <https://github.com/mixxxdj/mixxx/pull/3918>`_
  `#3939 <https://github.com/mixxxdj/mixxx/pull/3939>`_
* Inverted scroll wheel waveform zoom direction to mach other applications `#4195 <https://github.com/mixxxdj/mixxx/pull/4195>`_
* Fix leaked controls `#4213 <https://github.com/mixxxdj/mixxx/pull/4213>`_ `lp:1912129 <https://bugs.launchpad.net/mixxx/+bug/1912129>`_

Other
^^^^^


* Improve/fix the build system
  `#2796 <https://github.com/mixxxdj/mixxx/pull/2796>`_
  `#2937 <https://github.com/mixxxdj/mixxx/pull/2937>`_
  `#2943 <https://github.com/mixxxdj/mixxx/pull/2943>`_
  `#3041 <https://github.com/mixxxdj/mixxx/pull/3041>`_
  `#3046 <https://github.com/mixxxdj/mixxx/pull/3046>`_
  `#3114 <https://github.com/mixxxdj/mixxx/pull/3114>`_
  `#3182 <https://github.com/mixxxdj/mixxx/pull/3182>`_
  `#3274 <https://github.com/mixxxdj/mixxx/pull/3274>`_
  `#3300 <https://github.com/mixxxdj/mixxx/pull/3300>`_
  `#3471 <https://github.com/mixxxdj/mixxx/pull/3471>`_
  `#3514 <https://github.com/mixxxdj/mixxx/pull/3514>`_
  `#3765 <https://github.com/mixxxdj/mixxx/pull/3765>`_
  `#3849 <https://github.com/mixxxdj/mixxx/pull/3849>`_
  `#3876 <https://github.com/mixxxdj/mixxx/pull/3876>`_
  `#3861 <https://github.com/mixxxdj/mixxx/pull/3861>`_
  `#3923 <https://github.com/mixxxdj/mixxx/pull/3923>`_
  `#3948 <https://github.com/mixxxdj/mixxx/pull/3948>`_
  `#3929 <https://github.com/mixxxdj/mixxx/pull/3929>`_
  `#4007 <https://github.com/mixxxdj/mixxx/pull/4007>`_
  `#4070 <https://github.com/mixxxdj/mixxx/pull/4070>`_
  `#4084 <https://github.com/mixxxdj/mixxx/pull/4084>`_
  `#4098 <https://github.com/mixxxdj/mixxx/pull/4098>`_
  `#4113 <https://github.com/mixxxdj/mixxx/pull/4113>`_
  `#4163 <https://github.com/mixxxdj/mixxx/pull/4163>`_
  `#4166 <https://github.com/mixxxdj/mixxx/pull/4166>`_
  `#4185 <https://github.com/mixxxdj/mixxx/pull/4185>`_
  `#4187 <https://github.com/mixxxdj/mixxx/pull/4187>`_
  `#4192 <https://github.com/mixxxdj/mixxx/pull/4192>`_
  `#4226 <https://github.com/mixxxdj/mixxx/pull/4226>`_
  `#4203 <https://github.com/mixxxdj/mixxx/pull/4203>`_
  `#4250 <https://github.com/mixxxdj/mixxx/pull/4250>`_
  `#4274 <https://github.com/mixxxdj/mixxx/pull/4274>`_
* Drop Ubuntu Bionic support, require Qt 5.12
  `#3687 <https://github.com/mixxxdj/mixxx/pull/3687>`_
  `#3735 <https://github.com/mixxxdj/mixxx/pull/3735>`_
  `#3736 <https://github.com/mixxxdj/mixxx/pull/3736>`_
  `#3985 <https://github.com/mixxxdj/mixxx/pull/3985>`_
* Add NixOS support
  `#2820 <https://github.com/mixxxdj/mixxx/pull/2820>`_
  `#2828 <https://github.com/mixxxdj/mixxx/pull/2828>`_
  `#2836 <https://github.com/mixxxdj/mixxx/pull/2836>`_
  `#2827 <https://github.com/mixxxdj/mixxx/pull/2827>`_
  `#2827 <https://github.com/mixxxdj/mixxx/pull/2827>`_
  `#2828 <https://github.com/mixxxdj/mixxx/pull/2828>`_
  `#3113 <https://github.com/mixxxdj/mixxx/pull/3113>`_
  `#3089 <https://github.com/mixxxdj/mixxx/pull/3089>`_
  `#3545 <https://github.com/mixxxdj/mixxx/pull/3545>`_
* Add support for saving loops as hotcues
  `#2194 <https://github.com/mixxxdj/mixxx/pull/2194>`_
  `#4265 <https://github.com/mixxxdj/mixxx/pull/4265>`_
  `lp:1367159 <https://bugs.launchpad.net/mixxx/+bug/1367159>`_
* Make use of inclusive language
  `#2894 <https://github.com/mixxxdj/mixxx/pull/2894>`_
  `#3868 <https://github.com/mixxxdj/mixxx/pull/3868>`_
* Add Noise effect `#2921 <https://github.com/mixxxdj/mixxx/pull/2921>`_
* Improve Unittests
  `#2938 <https://github.com/mixxxdj/mixxx/pull/2938>`_
  `#2980 <https://github.com/mixxxdj/mixxx/pull/2980>`_
  `#3006 <https://github.com/mixxxdj/mixxx/pull/3006>`_
* Logging: Add support for ``QT_MESSAGE_PATTERN`` environment variable
  `#3204 <https://github.com/mixxxdj/mixxx/pull/3204>`_
  `#3518 <https://github.com/mixxxdj/mixxx/pull/3518>`_
* Colored logging console output
  `#3197 <https://github.com/mixxxdj/mixxx/pull/3197>`_
* Improve command line argument parser
  `#3640 <https://github.com/mixxxdj/mixxx/pull/3640>`_
  `#3962 <https://github.com/mixxxdj/mixxx/pull/3962>`_
  `#4022 <https://github.com/mixxxdj/mixxx/pull/4022>`_
  `#4036 <https://github.com/mixxxdj/mixxx/pull/4036>`_
  `#4170 <https://github.com/mixxxdj/mixxx/pull/4170>`_
  `#4057 <https://github.com/mixxxdj/mixxx/pull/4057>`_
* Improve message when dealing with macOS sandbox `#4018 <https://github.com/mixxxdj/mixxx/pull/4018>`_ `lp:1921541 <https://bugs.launchpad.net/mixxx/+bug/1921541>`_
* Move contribution guidelines into our git repository `#2699 <https://github.com/mixxxdj/mixxx/pull/2699>`_
* Automize deployment of CHANGELOG to the manual
  `#4180 <https://github.com/mixxxdj/mixxx/pull/4180>`_
  `#4256 <https://github.com/mixxxdj/mixxx/pull/4256>`_
  `#4208 <https://github.com/mixxxdj/mixxx/pull/4208>`_
  `#4228 <https://github.com/mixxxdj/mixxx/pull/4228>`_
  `#4222 <https://github.com/mixxxdj/mixxx/pull/4222>`_
* Always show tooltips in preferences `#4198 <https://github.com/mixxxdj/mixxx/pull/4198>`_ `lp:1840493 <https://bugs.launchpad.net/mixxx/+bug/1840493>`_
* Allow to build Mixxx on Linux without ALSA, working around a Pipewire bug `#4242 <https://github.com/mixxxdj/mixxx/pull/4242>`_
* Fix possible crash with opus files with embedded cover arts and require TagLib 1.11 or newer
  `#4251 <https://github.com/mixxxdj/mixxx/pull/4251>`_
  `#4252 <https://github.com/mixxxdj/mixxx/pull/4252>`_
  `lp:1940777 <https://bugs.launchpad.net/mixxx/+bug/1940777>`_
* Misc. refactorings
  `#3154 <https://github.com/mixxxdj/mixxx/pull/3154>`_
  `#2870 <https://github.com/mixxxdj/mixxx/pull/2870>`_
  `#2872 <https://github.com/mixxxdj/mixxx/pull/2872>`_
  `#2978 <https://github.com/mixxxdj/mixxx/pull/2978>`_
  `#2969 <https://github.com/mixxxdj/mixxx/pull/2969>`_
  `#3016 <https://github.com/mixxxdj/mixxx/pull/3016>`_
  `#3320 <https://github.com/mixxxdj/mixxx/pull/3320>`_
  `#3356 <https://github.com/mixxxdj/mixxx/pull/3356>`_
  `#3453 <https://github.com/mixxxdj/mixxx/pull/3453>`_
  `#3487 <https://github.com/mixxxdj/mixxx/pull/3487>`_
  `#3558 <https://github.com/mixxxdj/mixxx/pull/3558>`_
  `#3685 <https://github.com/mixxxdj/mixxx/pull/3685>`_
  `#3741 <https://github.com/mixxxdj/mixxx/pull/3741>`_
  `#3744 <https://github.com/mixxxdj/mixxx/pull/3744>`_
  `#3753 <https://github.com/mixxxdj/mixxx/pull/3753>`_
  `#3761 <https://github.com/mixxxdj/mixxx/pull/3761>`_
  `#3834 <https://github.com/mixxxdj/mixxx/pull/3834>`_
  `#3842 <https://github.com/mixxxdj/mixxx/pull/3842>`_
  `#3853 <https://github.com/mixxxdj/mixxx/pull/3853>`_
  `#3874 <https://github.com/mixxxdj/mixxx/pull/3874>`_
  `#3883 <https://github.com/mixxxdj/mixxx/pull/3883>`_
  `#3922 <https://github.com/mixxxdj/mixxx/pull/3922>`_
  `#3947 <https://github.com/mixxxdj/mixxx/pull/3947>`_
  `#3974 <https://github.com/mixxxdj/mixxx/pull/3974>`_
  `#4024 <https://github.com/mixxxdj/mixxx/pull/4024>`_
  `#4026 <https://github.com/mixxxdj/mixxx/pull/4026>`_
  `#4034 <https://github.com/mixxxdj/mixxx/pull/4034>`_
  `#4038 <https://github.com/mixxxdj/mixxx/pull/4038>`_
  `#4039 <https://github.com/mixxxdj/mixxx/pull/4039>`_
  `#4043 <https://github.com/mixxxdj/mixxx/pull/4043>`_
  `#4053 <https://github.com/mixxxdj/mixxx/pull/4053>`_
  `#4072 <https://github.com/mixxxdj/mixxx/pull/4072>`_
  `#4097 <https://github.com/mixxxdj/mixxx/pull/4097>`_
  `#4096 <https://github.com/mixxxdj/mixxx/pull/4096>`_
  `#4118 <https://github.com/mixxxdj/mixxx/pull/4118>`_
  `#4130 <https://github.com/mixxxdj/mixxx/pull/4130>`_
  `#4129 <https://github.com/mixxxdj/mixxx/pull/4129>`_
  `#4109 <https://github.com/mixxxdj/mixxx/pull/4109>`_
  `#4106 <https://github.com/mixxxdj/mixxx/pull/4106>`_
  `#4131 <https://github.com/mixxxdj/mixxx/pull/4131>`_
  `#4140 <https://github.com/mixxxdj/mixxx/pull/4140>`_
  `#3032 <https://github.com/mixxxdj/mixxx/pull/3032>`_
  `#4110 <https://github.com/mixxxdj/mixxx/pull/4110>`_
  `#4173 <https://github.com/mixxxdj/mixxx/pull/4173>`_
  `#4178 <https://github.com/mixxxdj/mixxx/pull/4178>`_
  `#4194 <https://github.com/mixxxdj/mixxx/pull/4194>`_
  `#4197 <https://github.com/mixxxdj/mixxx/pull/4197>`_
  `#4190 <https://github.com/mixxxdj/mixxx/pull/4190>`_
  `#4212 <https://github.com/mixxxdj/mixxx/pull/4212>`_
  `#4223 <https://github.com/mixxxdj/mixxx/pull/4223>`_
  `#4238 <https://github.com/mixxxdj/mixxx/pull/4238>`_
  `#4236 <https://github.com/mixxxdj/mixxx/pull/4236>`_

.. _v2-3-2:

`2.3.2 <https://launchpad.net/mixxx/+milestone/2.3.2>`_ (Unreleased)
------------------------------------------------------------------------


* Improve robustness of file type detection by considering the actual MIME type of the content. `lp:1445885 <https://bugs.launchpad.net/mixxx/+bug/1445885>`_ `#4356 <https://github.com/mixxxdj/mixxx/pull/4356>`_ `#4357 <https://github.com/mixxxdj/mixxx/pull/4357>`_

Packaging
^^^^^^^^^


* Downloads of external dependencies are placed in build/downloads
* The sources for libkeyfinder are now expected in build/downloads/libkeyfinder-2.2.5.zip instead of build/download/libkeyfinder/v2.2.5.zip

.. _v2-3-1:

`2.3.1 <https://launchpad.net/mixxx/+milestone/2.3.1>`_ (2021-09-29)
------------------------------------------------------------------------


* Added mapping for the Numark DJ2GO2 Touch controller `#4108 <https://github.com/mixxxdj/mixxx/pull/4108>`_ `#4287 <https://github.com/mixxxdj/mixxx/pull/4287>`_
* Added mapping for the Numark Mixtrack Pro FX controller `#4160 <https://github.com/mixxxdj/mixxx/pull/4160>`_
* Updated mapping for Behringer DDM4000 mixer `#4262 <https://github.com/mixxxdj/mixxx/pull/4262>`_
* Updated mapping for Denon MC7000 controller `#4021 <https://github.com/mixxxdj/mixxx/pull/4021>`_
* Hercules Inpulse 300: Add better FX controls and other minor improvements `#4246 <https://github.com/mixxxdj/mixxx/pull/4246>`_
* Denon MC7000: Improve slip mode and jog wheel handling `#4021 <https://github.com/mixxxdj/mixxx/pull/4021>`_ `#4324 <https://github.com/mixxxdj/mixxx/pull/4324>`_
* Disabled detection of keyboards and mice as HID controllers `#4243 <https://github.com/mixxxdj/mixxx/pull/4243>`_
* Disabled detection of all HID controllers with Apple's vendor ID. Apple doesn't build actual controllers. `#4260 <https://github.com/mixxxdj/mixxx/pull/4260>`_ `#4273 <https://github.com/mixxxdj/mixxx/pull/4273>`_
* Add support for HiDPI scale factors of 125% and 175% (only with Qt 5.14+) `lp1938102 <https://bugs.launchpad.net/mixxx/+bug/1938102>`_ `#4161 <https://github.com/mixxxdj/mixxx/pull/4161>`_
* Fix unhandled exception when parsing corrupt Rekordbox PDB files `lp1933853 <https://bugs.launchpad.net/mixxx/+bug/1933853>`_ `#4040 <https://github.com/mixxxdj/mixxx/pull/4040>`_
* Fix Echo effect adding left channel samples to right channel `#4141 <https://github.com/mixxxdj/mixxx/pull/4141>`_
* Fix bad phase seek when starting from preroll `lp1930143 <https://bugs.launchpad.net/mixxx/+bug/1930143>`_ `#4093 <https://github.com/mixxxdj/mixxx/pull/4093>`_
* Fix bad phase seek when a channel's audible status changes `#4156 <https://github.com/mixxxdj/mixxx/pull/4156>`_
* Tango skin: Show crossfader assign buttons by default `#4046 <https://github.com/mixxxdj/mixxx/pull/4046>`_
* Fix keyfinder library in arm64 builds `#4047 <https://github.com/mixxxdj/mixxx/pull/4047>`_
* Fix wrong track being recorded in History `lp1933991 <https://bugs.launchpad.net/mixxx/+bug/1933991>`_ `#4041 <https://github.com/mixxxdj/mixxx/pull/4041>`_ `#4059 <https://github.com/mixxxdj/mixxx/pull/4059>`_ `#4107 <https://github.com/mixxxdj/mixxx/pull/4107>`_ `#4296 <https://github.com/mixxxdj/mixxx/pull/4296>`_
* Fix support for relative paths in the skin system which caused missing images in third-party skins `#4151 <https://github.com/mixxxdj/mixxx/pull/4151>`_
* Fix relocation of directories with special/reserved characters in path name `#4146 <https://github.com/mixxxdj/mixxx/pull/4146>`_
* Update keyboard shortcuts sheet `#4042 <https://github.com/mixxxdj/mixxx/pull/4042>`_
* Library: resize the Played checkbox and BPM lock with the library font `#4050 <https://github.com/mixxxdj/mixxx/pull/4050>`_
* Don't allow Input focus on waveforms `#4134 <https://github.com/mixxxdj/mixxx/pull/4134>`_
* Fix performance issue on AArch64 by enabling flush-to-zero for floating-point arithmetic `#4144 <https://github.com/mixxxdj/mixxx/pull/4144>`_
* Fix custom key notation not restored correctly after restart `#4136 <https://github.com/mixxxdj/mixxx/pull/4136>`_
* Traktor S3: Disable scratch when switching decks to prevent locked scratch issue `#4073 <https://github.com/mixxxdj/mixxx/pull/4073>`_
* FFmpeg: Ignore inaudible samples before start of stream `#4245 <https://github.com/mixxxdj/mixxx/pull/4245>`_
* Controller Preferences: Don't automatically enable checkbox if controller is disabled `#4244 <https://github.com/mixxxdj/mixxx/pull/4244>`_ `lp:1941042 <https://bugs.launchpad.net/mixxx/+bug/1941042>`_
* Tooltips: Always show tooltips in preferences `#4198 <https://github.com/mixxxdj/mixxx/pull/4198>`_ `lp:1840493 <https://bugs.launchpad.net/mixxx/+bug/1840493>`_
* Tooltips: Use item label for tooltips in library side bar and show ID when debugging. `#4247 <https://github.com/mixxxdj/mixxx/pull/4247>`_
* Library sidebar: Also activate items on PageUp/Down events. `#4237 <https://github.com/mixxxdj/mixxx/pull/4237>`_
* Fix handling of preview button cell events in developer mode. `#4264 <https://github.com/mixxxdj/mixxx/pull/4264>`_ `lp:1929141 <https://bugs.launchpad.net/mixxx/+bug/1929141>`_
* Auto DJ: Fix bug which could make an empty track stop Auto DJ. `#4267 <https://github.com/mixxxdj/mixxx/pull/4267>`_ `lp:1941743 <https://bugs.launchpad.net/mixxx/+bug/1941743>`_
* Fix Auto DJ skipping tracks randomly `#4319 <https://github.com/mixxxdj/mixxx/pull/4319>`_ `lp1941989 <https://bugs.launchpad.net/mixxx/+bug/1941989>`_
* Fix high CPU load due to extremely high internal sync clock values `#4312 <https://github.com/mixxxdj/mixxx/pull/4312>`_ `lp1943320 <https://bugs.launchpad.net/mixxx/+bug/1943320>`_
* Fix preference option for re-analyzing beatgrids imported from other software `#4288 <https://github.com/mixxxdj/mixxx/pull/4288>`_

Packaging
^^^^^^^^^


* It is no longer necessary to manually copy the udev rule file in packaging scripts. Now pkg-config is used to determine the udevdir used to install the rules file in the CMake install step when CMAKE_INSTALL_PREFIX is ``/`` or ``/usr``.  `#4126 <https://github.com/mixxxdj/mixxx/pull/4126>`_
* Various build issues on FreeBSD are fixed `#4122 <https://github.com/mixxxdj/mixxx/pull/4122>`_ `#4123 <https://github.com/mixxxdj/mixxx/pull/4123>`_ `#4124 <https://github.com/mixxxdj/mixxx/pull/4124>`_
* .desktop file has be renamed to org.mixxx.Mixxx.desktop according to Freedesktop standards `#4206 <https://github.com/mixxxdj/mixxx/pull/4206>`_
* Uses system provided hidapi library if version >= 0.10.1 `#4215 <https://github.com/mixxxdj/mixxx/pull/4215>`_
* Please update PortAudio to `19.7 <https://github.com/PortAudio/portaudio/releases/tag/v19.7.0>`_ if you have not done so already. This is required for Mixxx to work with PipeWire via the JACK API for many devices.
* Install multiple sizes of rasterized icons `#4204 <https://github.com/mixxxdj/mixxx/pull/4204>`_ `#4315 <https://github.com/mixxxdj/mixxx/pull/4315>`_
* CMake: Fixed detection of SoundTouch pkgconfig file and version `#4209 <https://github.com/mixxxdj/mixxx/pull/4209>`_
* Fix AppStream metainfo `#4205 <https://github.com/mixxxdj/mixxx/pull/4205>`_ `#4317 <https://github.com/mixxxdj/mixxx/pull/4317>`_

.. _v2-3-0:

`2.3.0 <https://launchpad.net/mixxx/+milestone/2.3.0>`_ (2021-06-28)
------------------------------------------------------------------------

Hotcues
^^^^^^^


* Add hotcue colors and custom labels by right clicking hotcue buttons or right clicking hotcues on overview waveforms `#2016 <https://github.com/mixxxdj/mixxx/pull/2016>`_ `#2520 <https://github.com/mixxxdj/mixxx/pull/2520>`_ `#2238 <https://github.com/mixxxdj/mixxx/pull/2238>`_ `#2560 <https://github.com/mixxxdj/mixxx/pull/2560>`_ `#2557 <https://github.com/mixxxdj/mixxx/pull/2557>`_ `#2362 <https://github.com/mixxxdj/mixxx/pull/2362>`_
* Mouse hover cues on overview waveform to show time remaining until the cue `#2238 <https://github.com/mixxxdj/mixxx/pull/2238>`_

Hotcue & Track Colors
^^^^^^^^^^^^^^^^^^^^^


* Add configurable color per track `#2470 <https://github.com/mixxxdj/mixxx/pull/2470>`_ `#2539 <https://github.com/mixxxdj/mixxx/pull/2539>`_ `#2545 <https://github.com/mixxxdj/mixxx/pull/2545>`_ `#2630 <https://github.com/mixxxdj/mixxx/pull/2630>`_ `lp:1100882 <https://bugs.launchpad.net/mixxx/+bug/1100882>`_
* Add customizable color palettes for hotcue and track colors `#2530 <https://github.com/mixxxdj/mixxx/pull/2530>`_ `#2589 <https://github.com/mixxxdj/mixxx/pull/2589>`_ `#3749 <https://github.com/mixxxdj/mixxx/pull/3749>`_ `#2902 <https://github.com/mixxxdj/mixxx/pull/2902>`_
* Add hotcue color find-and-replace tool `#2547 <https://github.com/mixxxdj/mixxx/pull/2547>`_

Importing From Other DJ Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* Import cue points, track colors, and playlists from Serato file tags & database `#2480 <https://github.com/mixxxdj/mixxx/pull/2480>`_ `#2526 <https://github.com/mixxxdj/mixxx/pull/2526>`_ `#2499 <https://github.com/mixxxdj/mixxx/pull/2499>`_ `#2495 <https://github.com/mixxxdj/mixxx/pull/2495>`_ `#2673 <https://github.com/mixxxdj/mixxx/pull/2673>`_ `#3885 <https://github.com/mixxxdj/mixxx/pull/3885>`_

  * Note: Mixxx does not yet support multiple loops per track. We are `working on this for Mixxx 2.4 <https://github.com/mixxxdj/mixxx/pull/2194>`_. In Mixxx 2.3, if you import a track with multiple loops from Serato, Mixxx will use the first loop cue as the single loop Mixxx currently supports. The imported loops are still stored in Mixxx's database and are treated as hotcues in Mixxx 2.3. If you do not delete these hotcues, they will be usable as loops in Mixxx 2.4. Serato keeps loops and hotcues in separate lists, but Mixxx does not, so loops from Serato are imported starting as hotcue 9.

* Import cue points, track colors, and playlists from Rekordbox USB drives `#2119 <https://github.com/mixxxdj/mixxx/pull/2119>`_ `#2555 <https://github.com/mixxxdj/mixxx/pull/2555>`_ `#2543 <https://github.com/mixxxdj/mixxx/pull/2543>`_ `#2779 <https://github.com/mixxxdj/mixxx/pull/2779>`_

  * Note: The first Rekordbox memory cue is imported for the main cue button in Mixxx and the remaining Rekordbox memory cues are imported as Mixxx hotcues, starting with the next hotcue number after the last hotcue from Rekordbox.
  * Note: Mixxx does not yet support multiple loops per track. Imported loops from Rekordbox are treated like imported loops from Serato, so refer to the note above for details.

Intro & Outro Cues
^^^^^^^^^^^^^^^^^^


* Add intro & outro range cues with automatic silence detection `#1242 <https://github.com/mixxxdj/mixxx/pull/1242>`_
* Show duration of intro & outro ranges on overview waveform `#2089 <https://github.com/mixxxdj/mixxx/pull/2089>`_
* Use intro & outro cues in AutoDJ transitions `#2103 <https://github.com/mixxxdj/mixxx/pull/2103>`_

Deck cloning
^^^^^^^^^^^^


* Add deck cloning (also known as "instant doubles" in other DJ software) by dragging and dropping between decks `#1892 <https://github.com/mixxxdj/mixxx/pull/1892>`_ and samplers `#3200 <https://github.com/mixxxdj/mixxx/pull/3200>`_
* Clone decks by double pressing the load button on a controller (with option to disable this) `#2024 <https://github.com/mixxxdj/mixxx/pull/2024>`_ `#2042 <https://github.com/mixxxdj/mixxx/pull/2042>`_

Skins & GUI
^^^^^^^^^^^


* Aesthetically revamped LateNight skin `#2298 <https://github.com/mixxxdj/mixxx/pull/2298>`_ `#2342 <https://github.com/mixxxdj/mixxx/pull/2342>`_
* Right click overview waveform to show time remaining until that point `#2238 <https://github.com/mixxxdj/mixxx/pull/2238>`_
* Show track info dialog when double clicking track labels in decks `#2990 <https://github.com/mixxxdj/mixxx/pull/2990>`_
* Show track context menu when right clicking text in decks `#2612 <https://github.com/mixxxdj/mixxx/pull/2612>`_ `#2675 <https://github.com/mixxxdj/mixxx/pull/2675>`_ `#2684 <https://github.com/mixxxdj/mixxx/pull/2684>`_ `#2696 <https://github.com/mixxxdj/mixxx/pull/2696>`_
* Add laptop battery widget to skins `#2283 <https://github.com/mixxxdj/mixxx/pull/2283>`_ `#2277 <https://github.com/mixxxdj/mixxx/pull/2277>`_ `#2250 <https://github.com/mixxxdj/mixxx/pull/2250>`_ `#2228 <https://github.com/mixxxdj/mixxx/pull/2228>`_ `#2221 <https://github.com/mixxxdj/mixxx/pull/2221>`_ `#2163 <https://github.com/mixxxdj/mixxx/pull/2163>`_ `#2160 <https://github.com/mixxxdj/mixxx/pull/2160>`_ `#2147 <https://github.com/mixxxdj/mixxx/pull/2147>`_ `#2281 <https://github.com/mixxxdj/mixxx/pull/2281>`_ `#2319 <https://github.com/mixxxdj/mixxx/pull/2319>`_ `#2287 <https://github.com/mixxxdj/mixxx/pull/2287>`_
* Show when passthrough mode is active on overview waveforms `#2575 <https://github.com/mixxxdj/mixxx/pull/2575>`_ `#2616 <https://github.com/mixxxdj/mixxx/pull/2616>`_
* Changed format of currently playing track in window title from "artist, title" to "artist - title" `#2807 <https://github.com/mixxxdj/mixxx/pull/2807>`_
* Workaround Linux skin change crash `#3144 <https://github.com/mixxxdj/mixxx/pull/3144>`_ `lp:1885009 <https://bugs.launchpad.net/mixxx/+bug/1885009>`_
* Fix touch control `lp:1895431 <https://bugs.launchpad.net/mixxx/+bug/1895431>`_
* Fix broken knob interaction on touchscreens `#3512 <https://github.com/mixxxdj/mixxx/pull/3512>`_
* AutoDJ: Make "enable" shortcut work after startup `#3242 <https://github.com/mixxxdj/mixxx/pull/3242>`_
* Add rate range indicator `#3693 <https://github.com/mixxxdj/mixxx/pull/3693>`_
* Allow menubar to be styled `#3372 <https://github.com/mixxxdj/mixxx/pull/3372>`_ `#3788 <https://github.com/mixxxdj/mixxx/pull/3788>`_
* Add Donate button to About dialog `#3838 <https://github.com/mixxxdj/mixxx/pull/3838>`_ `#3846 <https://github.com/mixxxdj/mixxx/pull/3846>`_
* Add Scrollable Skin Widget `#3890 <https://github.com/mixxxdj/mixxx/pull/3890>`_
* Fix minor visual issues in Skins `#3958 <https://github.com/mixxxdj/mixxx/pull/3958/>`_ `#3954 <https://github.com/mixxxdj/mixxx/pull/3954/>`_ `#3941 <https://github.com/mixxxdj/mixxx/pull/3941/>`_ `#3938 <https://github.com/mixxxdj/mixxx/pull/3938/>`_ `#3936 <https://github.com/mixxxdj/mixxx/pull/3936/>`_ `#3886 <https://github.com/mixxxdj/mixxx/pull/3886/>`_ `#3927 <https://github.com/mixxxdj/mixxx/pull/3927/>`_ `#3844 <https://github.com/mixxxdj/mixxx/pull/3844/>`_ `#3933 <https://github.com/mixxxdj/mixxx/pull/3933/>`_ `#3835 <https://github.com/mixxxdj/mixxx/pull/3835/>`_ `#3902 <https://github.com/mixxxdj/mixxx/pull/3902>`_ `#3931 <https://github.com/mixxxdj/mixxx/pull/3931>`_

Music Feature Analysis
^^^^^^^^^^^^^^^^^^^^^^


* Multithreaded analysis for much faster batch analysis on multicore CPUs `#1624 <https://github.com/mixxxdj/mixxx/pull/1624>`_ `#2142 <https://github.com/mixxxdj/mixxx/pull/2142>`_ `lp:1641153 <https://bugs.launchpad.net/mixxx/+bug/1641153>`_
* Fix bugs affecting key detection accuracy `#2137 <https://github.com/mixxxdj/mixxx/pull/2137>`_ `#2152 <https://github.com/mixxxdj/mixxx/pull/2152>`_ `#2112 <https://github.com/mixxxdj/mixxx/pull/2112>`_ `#2136 <https://github.com/mixxxdj/mixxx/pull/2136>`_

  * Note: Users who have not manually corrected keys are advised to clear all keys in their library by pressing Ctrl + A in the library, right clicking, going to Reset -> Key, then reanalyzing their library. This will freeze the GUI while Mixxx clears the keys; this is a known problem that we will not be able to fix for 2.3. Wait until it is finished and you will be able to reanalyze tracks for better key detection results.

* Remove VAMP plugin support and use Queen Mary DSP library directly. vamp-plugin-sdk and vamp-hostsdk are no longer required dependencies. `#926 <https://github.com/mixxxdj/mixxx/pull/926>`_
* Improvements BPM detection on non-const beatgrids `#3626 <https://github.com/mixxxdj/mixxx/pull/3626>`_
* Fix const beatgrid placement `#3965 <https://github.com/mixxxdj/mixxx/pull/3965>`_ `#3973 <https://github.com/mixxxdj/mixxx/pull/3973>`_

Music Library
^^^^^^^^^^^^^


* Add support for searching for empty fields (for example ``crate:""``\ ) `lp:1788086 <https://bugs.launchpad.net/mixxx/+bug/1788086>`_
* Improve synchronization of track metadata and file tags `#2406 <https://github.com/mixxxdj/mixxx/pull/2406>`_
* Library Scanner: Improve hashing of directory contents `#2497 <https://github.com/mixxxdj/mixxx/pull/2497>`_
* Rework of Cover Image Hashing `lp:1607097 <https://bugs.launchpad.net/mixxx/+bug/1607097>`_ `#2507 <https://github.com/mixxxdj/mixxx/pull/2507>`_ `#2508 <https://github.com/mixxxdj/mixxx/pull/2508>`_
* MusicBrainz: Handle 301 status response `#2510 <https://github.com/mixxxdj/mixxx/pull/2510>`_
* MusicBrainz: Add extended metadata support `lp:1581256 <https://bugs.launchpad.net/mixxx/+bug/1581256>`_ `#2522 <https://github.com/mixxxdj/mixxx/pull/2522>`_
* TagLib: Fix detection of empty or missing file tags `lp:1865957 <https://bugs.launchpad.net/mixxx/+bug/1865957>`_ `#2535 <https://github.com/mixxxdj/mixxx/pull/2535>`_
* Fix caching of duplicate tracks that reference the same file `#3027 <https://github.com/mixxxdj/mixxx/pull/3027>`_
* Use 6 instead of only 4 compatible musical keys (major/minor) `#3205 <https://github.com/mixxxdj/mixxx/pull/3205>`_
* Fix possible crash when trying to refocus the tracks table while another Mixxx window has focus `#3201 <https://github.com/mixxxdj/mixxx/pull/3201>`_
* Don't create new tags in file when exporting metadata to it `#3898 <https://github.com/mixxxdj/mixxx/pull/3898>`_
* Fix playlist files beginning with non-english characters not being loaded `#3916 <https://github.com/mixxxdj/mixxx/pull/3916>`_
* Enable sorting in "Hidden Tracks" and "Missing Tracks" views `#3828 <https://github.com/mixxxdj/mixxx/pull/3828>`_ `lp:1828555 <https://bugs.launchpad.net/mixxx/+bug/1828555/>`_ `lp:1924616 <https://bugs.launchpad.net/mixxx/+bug/1924616/>`_
* Fix track table being empty after start `#3935 <https://github.com/mixxxdj/mixxx/pull/3935/>`_ `lp:1930546 <https://bugs.launchpad.net/mixxx/+bug/1930546/>`_ `lp:1924843 <https://bugs.launchpad.net/mixxx/+bug/1924843/>`_

Audio Codecs
^^^^^^^^^^^^


* Add FFmpeg audio decoder, bringing support for ALAC files `#1356 <https://github.com/mixxxdj/mixxx/pull/1356>`_
* Include LAME MP3 encoder with Mixxx now that the MP3 patent has expired `lp:1294128 <https://bugs.launchpad.net/mixxx/+bug/1294128>`_ `buildserver:#37 <https://github.com/mixxxdj/buildserver/pull/37>`_ `buildserver:9e8bcee <https://github.com/mixxxdj/buildserver/commit/9e8bcee771731920ae82f3e076d43f0fb51e5027>`_
* Add Opus streaming and recording support. `lp:1338413 <https://bugs.launchpad.net/mixxx/+bug/1338413>`_
* Remove support for SoundSource plugins because the code was not well-maintained and could lead to crashes `lp:1792747 <https://bugs.launchpad.net/mixxx/+bug/1792747>`_
* Add HE-AAC encoding capabilities for recording and broadcasting `#3615 <https://github.com/mixxxdj/mixxx/pull/3615>`_

Audio Engine
^^^^^^^^^^^^


* Fix loss of precision when dealing with floating-point sample positions while setting loop out position and seeking using vinyl control `#3126 <https://github.com/mixxxdj/mixxx/pull/3126>`_ `#3127 <https://github.com/mixxxdj/mixxx/pull/3127>`_
* Prevent moving a loop beyond track end `#3117 <https://github.com/mixxxdj/mixxx/pull/3117>`_ `lp:1799574 <https://bugs.launchpad.net/mixxx/+bug/1799574>`_
* Fix possible memory corruption using JACK on Linux `#3160 <https://github.com/mixxxdj/mixxx/pull/3160>`_
* Fix changing of vinyl lead-in time `lp:1915483 <https://bugs.launchpad.net/mixxx/+bug/1915483>`_ `#3781 <https://github.com/mixxxdj/mixxx/pull/3781>`_
* Fix tempo change of non-const beatgrid track on audible deck when cueing another track `#3772 <https://github.com/mixxxdj/mixxx/pull/3772>`_
* Fix crash when changing effect unit routing `#3882 <https://github.com/mixxxdj/mixxx/pull/3882>`_ `lp:1775497 <https://bugs.launchpad.net/mixxx/+bug/1775497>`_
* Make microphone ducking use strength knob the same way in automatic & manual mode `#2750 <https://github.com/mixxxdj/mixxx/pull/2750>`_

Controllers
^^^^^^^^^^^


* Improve workflow for configuring controller mappings and editing mappings `#2569 <https://github.com/mixxxdj/mixxx/pull/2569>`_ `#3278 <https://github.com/mixxxdj/mixxx/pull/3278>`_ `#3667 <https://github.com/mixxxdj/mixxx/pull/3667>`_
* Improve error reporting from controller scripts `#2588 <https://github.com/mixxxdj/mixxx/pull/2588>`_
* Make hotcue and track colors mappable on controllers `#2030 <https://github.com/mixxxdj/mixxx/pull/2030>`_ `#2541 <https://github.com/mixxxdj/mixxx/pull/2541>`_ `#2665 <https://github.com/mixxxdj/mixxx/pull/2665>`_ `#2520 <https://github.com/mixxxdj/mixxx/pull/2520>`_
* Add way to change library table sorting from controllers `#2118 <https://github.com/mixxxdj/mixxx/pull/2118>`_
* Add support for velocity sensitive sampler buttons in Components JS library `#2032 <https://github.com/mixxxdj/mixxx/pull/2032>`_
* Add logging when script ControlObject callback is disconnected successfully `#2054 <https://github.com/mixxxdj/mixxx/pull/2054>`_
* Add controller mapping for Roland DJ-505 `#2111 <https://github.com/mixxxdj/mixxx/pull/2111>`_
* Add controller mapping for Numark iDJ Live II `#2818 <https://github.com/mixxxdj/mixxx/pull/2818>`_
* Add controller mapping for Hercules DJControl Inpulse 200 `#2542 <https://github.com/mixxxdj/mixxx/pull/2542>`_
* Add controller mapping for Hercules DJControl Jogvision `#2370 <https://github.com/mixxxdj/mixxx/pull/2370>`_
* Add controller mapping for Pioneer DDJ-200 `#3185 <https://github.com/mixxxdj/mixxx/pull/3185>`_ `#3193 <https://github.com/mixxxdj/mixxx/pull/3193>`_ `#3742 <https://github.com/mixxxdj/mixxx/pull/3742>`_ `#3793 <https://github.com/mixxxdj/mixxx/pull/3793>`_ `#3949 <https://github.com/mixxxdj/mixxx/pull/3949>`_
* Add controller mapping for Pioneer DDJ-400 `#3479 <https://github.com/mixxxdj/mixxx/pull/3479>`_
* Add controller mapping for ION Discover DJ Pro `#2893 <https://github.com/mixxxdj/mixxx/pull/2893>`_
* Add controller mapping for Native Instrument Traktor Kontrol S3 `#3031 <https://github.com/mixxxdj/mixxx/pull/3031>`_
* Add controller mapping for Behringer BCR2000 `#3342 <https://github.com/mixxxdj/mixxx/pull/3342>`_ `#3943 <https://github.com/mixxxdj/mixxx/pull/3943>`_
* Add controller mapping for Behringer DDM4000 `#3542 <https://github.com/mixxxdj/mixxx/pull/3542>`_
* Update controller mapping for Allen & Heath Xone K2 to add intro/outro cues `#2236 <https://github.com/mixxxdj/mixxx/pull/2236>`_
* Update controller mapping for Hercules P32 for more accurate headmix control `#3537 <https://github.com/mixxxdj/mixxx/pull/3537>`_
* Update controller mapping for Native Instruments Traktor Kontrol S4MK2 to add auto-slip mode and pitch fader range `#3331 <https://github.com/mixxxdj/mixxx/pull/3331>`_
* Fix Pioneer DDJ-SB2 controller mapping auto tempo going to infinity bug `#2559 <https://github.com/mixxxdj/mixxx/pull/2559>`_ `lp:1846403 <https://bugs.launchpad.net/mixxx/+bug/1846403>`_
* Fix Numark Mixtrack Pro 3 controller mapping inverted FX on/off control `#3758 <https://github.com/mixxxdj/mixxx/pull/3758>`_
* Gracefully handle MIDI overflow `#825 <https://github.com/mixxxdj/mixxx/pull/825>`_

Other
^^^^^


* Add CMake build system with ``ccache`` and ``sccache`` support for faster compilation times and remove SCons `#2280 <https://github.com/mixxxdj/mixxx/pull/2280>`_ `#3618 <https://github.com/mixxxdj/mixxx/pull/3618>`_
* Make Mixxx compile even though ``QT_NO_OPENGL`` or ``QT_OPENGL_ES_2`` is defined (fixes build on Raspberry Pi) `lp:1863440 <https://bugs.launchpad.net/mixxx/+bug/1863440>`_ `#2504 <https://github.com/mixxxdj/mixxx/pull/2504>`_
* Fix ARM build issues `#3602 <https://github.com/mixxxdj/mixxx/pull/3602>`_
* Fix missing manual in DEB package `lp:1889776 <https://bugs.launchpad.net/mixxx/+bug/1889776>`_ `#2985 <https://github.com/mixxxdj/mixxx/pull/2985>`_
* Add macOS codesigning and notarization to fix startup warnings `#3281 <https://github.com/mixxxdj/mixxx/pull/3281>`_
* Don't trash user configuration if an error occurs when writing `#3192 <https://github.com/mixxxdj/mixxx/pull/3192>`_
* Enable CUE sheet recording by default `#3374 <https://github.com/mixxxdj/mixxx/pull/3374>`_
* Fix crash when double clicking GLSL waveforms with right mouse button `#3904 <https://github.com/mixxxdj/mixxx/pull/3904>`_
* Derive Mixxx version from ``git describe`` `#3824 <https://github.com/mixxxdj/mixxx/pull/3824>`_ `#3841 <https://github.com/mixxxdj/mixxx/pull/3841>`_ `#3848 <https://github.com/mixxxdj/mixxx/pull/3848>`_
* Improve tapping the BPM of a deck `#3790 <https://github.com/mixxxdj/mixxx/pull/3790>`_ `lp:1882776 <https://bugs.launchpad.net/mixxx/+bug/1882776>`_
* And countless other small fixes and improvements (too many to list them all!)

.. _v2-2-4:

`2.2.4 <https://launchpad.net/mixxx/+milestone/2.2.4>`_ (2020-06-27)
------------------------------------------------------------------------


* Store default recording format after "Restore Defaults" `lp:1857806 <https://bugs.launchpad.net/mixxx/+bug/1857806>`_ `#2414 <https://github.com/mixxxdj/mixxx/pull/2414>`_
* Prevent infinite loop when decoding corrupt MP3 files `#2417 <https://github.com/mixxxdj/mixxx/pull/2417>`_
* Add workaround for broken libshout versions `#2040 <https://github.com/mixxxdj/mixxx/pull/2040>`_ `#2438 <https://github.com/mixxxdj/mixxx/pull/2438>`_
* Speed up purging of tracks `lp:1845837 <https://bugs.launchpad.net/mixxx/+bug/1845837>`_ `#2393 <https://github.com/mixxxdj/mixxx/pull/2393>`_
* Don't stop playback if vinyl passthrough input is configured and PASS button is pressed `#2474 <https://github.com/mixxxdj/mixxx/pull/2474>`_
* Fix debug assertion for invalid crate names `lp:1861431 <https://bugs.launchpad.net/mixxx/+bug/1861431>`_ `#2477 <https://github.com/mixxxdj/mixxx/pull/2477>`_
* Fix crashes when executing actions on tracks that already disappeared from the DB `#2527 <https://github.com/mixxxdj/mixxx/pull/2527>`_
* AutoDJ: Skip next track when both deck are playing `lp:1399974 <https://bugs.launchpad.net/mixxx/+bug/1399974>`_ `#2531 <https://github.com/mixxxdj/mixxx/pull/2531>`_
* Tweak scratch parameters for Mixtrack Platinum `#2028 <https://github.com/mixxxdj/mixxx/pull/2028>`_
* Fix auto tempo going to infinity on Pioneer DDJ-SB2 `#2559 <https://github.com/mixxxdj/mixxx/pull/2559>`_
* Fix bpm.tapButton logic and reject missed & double taps `#2594 <https://github.com/mixxxdj/mixxx/pull/2594>`_
* Add controller mapping for Native Instruments Traktor Kontrol S2 MK3 `#2348 <https://github.com/mixxxdj/mixxx/pull/2348>`_
* Add controller mapping for Soundless joyMIDI `#2425 <https://github.com/mixxxdj/mixxx/pull/2425>`_
* Add controller mapping for Hercules DJControl Inpulse 300 `#2465 <https://github.com/mixxxdj/mixxx/pull/2465>`_
* Add controller mapping for Denon MC7000 `#2546 <https://github.com/mixxxdj/mixxx/pull/2546>`_
* Add controller mapping for Stanton DJC.4 `#2607 <https://github.com/mixxxdj/mixxx/pull/2607>`_
* Fix broadcasting via broadcast/recording input `lp:1876222 <https://bugs.launchpad.net/mixxx/+bug/1876222>`_ `#2743 <https://github.com/mixxxdj/mixxx/pull/2743>`_
* Only apply ducking gain in manual ducking mode when talkover is enabed `lp:1394968 <https://bugs.launchpad.net/mixxx/+bug/1394968>`_ `lp:1737113 <https://bugs.launchpad.net/mixxx/+bug/1737113>`_ `lp:1662536 <https://bugs.launchpad.net/mixxx/+bug/1662536>`_ `#2759 <https://github.com/mixxxdj/mixxx/pull/2759>`_
* Ignore MIDI Clock Messages (0xF8) because they are not usable in Mixxx and inhibited the screensaver `#2786 <https://github.com/mixxxdj/mixxx/pull/2786>`_

.. _v2-2-3:

`2.2.3 <https://launchpad.net/mixxx/+milestone/2.2.3>`_ (2019-11-24)
------------------------------------------------------------------------


* Don't make users reconfigure sound hardware when it has not changed `#2253 <https://github.com/mixxxdj/mixxx/pull/2253>`_
* Fix MusicBrainz metadata lookup `lp:1848887 <https://bugs.launchpad.net/mixxx/+bug/1848887>`_ `#2328 <https://github.com/mixxxdj/mixxx/pull/2328>`_
* Fix high DPI scaling of cover art `#2247 <https://github.com/mixxxdj/mixxx/pull/2247>`_
* Fix high DPI scaling of cue point labels on scrolling waveforms `#2331 <https://github.com/mixxxdj/mixxx/pull/2331>`_
* Fix high DPI scaling of sliders in Tango skin `#2318 <https://github.com/mixxxdj/mixxx/pull/2318>`_
* Fix sound dropping out during recording `lp:1842679 <https://bugs.launchpad.net/mixxx/+bug/1842679>`_ `#2265 <https://github.com/mixxxdj/mixxx/pull/2265>`_ `#2305 <https://github.com/mixxxdj/mixxx/pull/2305>`_ `#2308 <https://github.com/mixxxdj/mixxx/pull/2308>`_ `#2309 <https://github.com/mixxxdj/mixxx/pull/2309>`_
* Fix rare crash on application shutdown `#2293 <https://github.com/mixxxdj/mixxx/pull/2293>`_
* Workaround various rare bugs caused by database inconsistencies `lp:1846971 <https://bugs.launchpad.net/mixxx/+bug/1846971>`_ `#2321 <https://github.com/mixxxdj/mixxx/pull/2321>`_
* Improve handling of corrupt FLAC files `#2315 <https://github.com/mixxxdj/mixxx/pull/2315>`_
* Don't immediately jump to loop start when loop_out is pressed in quantized mode `lp:1837077 <https://bugs.launchpad.net/mixxx/+bug/1837077>`_ `#2269 <https://github.com/mixxxdj/mixxx/pull/2269>`_
* Preserve order of tracks when dragging and dropping from AutoDJ to playlist `lp:1829601 <https://bugs.launchpad.net/mixxx/+bug/1829601>`_ `#2237 <https://github.com/mixxxdj/mixxx/pull/2237>`_
* Explicitly use X11 Qt platform plugin instead of Wayland in .desktop launcher `lp:1850729 <https://bugs.launchpad.net/mixxx/+bug/1850729>`_ `#2340 <https://github.com/mixxxdj/mixxx/pull/2340>`_
* Pioneer DDJ-SX: fix delayed sending of MIDI messages with low audio buffer sizes `#2326 <https://github.com/mixxxdj/mixxx/pull/2326>`_
* Enable modplug support on Linux by default `lp:1840537 <https://bugs.launchpad.net/mixxx/+bug/1840537>`_ `#2244 <https://github.com/mixxxdj/mixxx/pull/2244>`_ `#2272 <https://github.com/mixxxdj/mixxx/pull/2272>`_
* Fix keyboard shortcut for View > Skin Preferences `lp:1851993 <https://bugs.launchpad.net/mixxx/+bug/1851993>`_ `#2358 <https://github.com/mixxxdj/mixxx/pull/2358>`_ `#2372 <https://github.com/mixxxdj/mixxx/pull/2372>`_
* Reloop Terminal Mix: Fix mapping of sampler buttons 5-8 `lp:1846966 <https://bugs.launchpad.net/mixxx/+bug/1846966>`_ `#2330 <https://github.com/mixxxdj/mixxx/pull/2330>`_

.. _v2-2-2:

`2.2.2 <https://launchpad.net/mixxx/+milestone/2.2.2>`_ (2019-08-10)
------------------------------------------------------------------------


* Fix battery widget with upower <= 0.99.7. `#2221 <https://github.com/mixxxdj/mixxx/pull/2221>`_
* Fix BPM adjust in BpmControl. `lp:1836480 <https://bugs.launchpad.net/mixxx/+bug/1836480>`_
* Disable track metadata export for .ogg files and TagLib 1.11.1. `lp:1833190 <https://bugs.launchpad.net/mixxx/+bug/1833190>`_
* Fix interaction of hot cue buttons and looping. `lp:1778246 <https://bugs.launchpad.net/mixxx/+bug/1778246>`_
* Fix detection of moved tracks. `#2197 <https://github.com/mixxxdj/mixxx/pull/2197>`_
* Fix playlist import. `#2200 <https://github.com/mixxxdj/mixxx/pull/2200>`_ `lp:1687828 <https://bugs.launchpad.net/mixxx/+bug/1687828>`_
* Fix updating playlist labels. `lp:1837315 <https://bugs.launchpad.net/mixxx/+bug/1837315>`_
* Fix potential segfault on exit. `lp:1828360 <https://bugs.launchpad.net/mixxx/+bug/1828360>`_
* Fix parsing of invalid BPM values in MP3 files. `lp:1832325 <https://bugs.launchpad.net/mixxx/+bug/1832325>`_
* Fix crash when removing rows from empty model. `#2128 <https://github.com/mixxxdj/mixxx/pull/2128>`_
* Fix high DPI scaling of RGB overview waveforms. `#2090 <https://github.com/mixxxdj/mixxx/pull/2090>`_
* Fix for OpenGL SL detection on macOS. `lp:1828019 <https://bugs.launchpad.net/mixxx/+bug/1828019>`_
* Fix OpenGL ES detection. `lp:1825461 <https://bugs.launchpad.net/mixxx/+bug/1825461>`_
* Fix FX1/2 buttons missing Mic unit in Deere (64 samplers). `lp:1837716 <https://bugs.launchpad.net/mixxx/+bug/1837716>`_
* Tango64: Re-enable 64 samplers. `#2223 <https://github.com/mixxxdj/mixxx/pull/2223>`_
* Numark DJ2Go re-enable note-off for deck A cue button. `#2087 <https://github.com/mixxxdj/mixxx/pull/2087>`_
* Replace Flanger with QuickEffect in keyboard mapping. `#2233 <https://github.com/mixxxdj/mixxx/pull/2233>`_

.. _v2-2-1:

`2.2.1 <https://launchpad.net/mixxx/+milestone/2.2.1>`_ (2019-04-22)
------------------------------------------------------------------------


* Include all fixes from Mixxx 2.1.7 and 2.1.8
* Fix high CPU usage on MAC due to preview column `lp:1812763 <https://bugs.launchpad.net/mixxx/+bug/1812763>`_
* Fix HID controller output on Windows with common-hid-packet-parser.js
* Fix rendering slow down by not using QStylePainter in WSpinny `lp:1530720 <https://bugs.launchpad.net/mixxx/+bug/1530720>`_
* Fix broken Mic mute button `lp:1782568 <https://bugs.launchpad.net/mixxx/+bug/1782568>`_
* added quick effect enable button to the control picker menu
* Fix Cover Window close issue with empty cover arts
* Fix Numark Mixtrack 3 mapping. `#2057 <https://github.com/mixxxdj/mixxx/pull/2057>`_

.. _v2-2-0:

`2.2.0 <https://launchpad.net/mixxx/+milestone/2.2.0>`_ (2018-12-17)
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

`2.1.8 <https://launchpad.net/mixxx/+milestone/2.1.8>`_ (2019-04-07)
------------------------------------------------------------------------


* Fix a rare chance for a corrupt track file while writing metadata in out of disk situations. `lp:1815305 <https://bugs.launchpad.net/mixxx/+bug/1815305>`_
* Fix export of BPM track file metadata. `lp:1816490 <https://bugs.launchpad.net/mixxx/+bug/1816490>`_
* Fix sending of broadcast metadata with TLS enabled libshout 2.4.1. `lp:1817395 <https://bugs.launchpad.net/mixxx/+bug/1817395>`_
* Fix resdicovering purged tracks in all cases. `lp:1821514 <https://bugs.launchpad.net/mixxx/+bug/1821514>`_
* Fix dropping track from OSX Finder. `lp:1822424 <https://bugs.launchpad.net/mixxx/+bug/1822424>`_

.. _v2-1-7:

`2.1.7 <https://launchpad.net/mixxx/+milestone/2.1.7>`_ (2019-01-15)
------------------------------------------------------------------------


* Fix syncing to doublespeed `lp:1808697 <https://bugs.launchpad.net/mixxx/+bug/1808697>`_
* Fix issues when changing beats of a synced track `lp:1808698 <https://bugs.launchpad.net/mixxx/+bug/1808698>`_
* Fix direction of pitch bend buttons when inverting rate slider `lp:1770745 <https://bugs.launchpad.net/mixxx/+bug/1770745>`_
* Use first loaded deck if no playing deck is found `lp:1784185 <https://bugs.launchpad.net/mixxx/+bug/1784185>`_
* Encode file names correctly on macOS `lp:1776949 <https://bugs.launchpad.net/mixxx/+bug/1776949>`_

.. _v2-1-6:

`2.1.6 <https://launchpad.net/mixxx/+milestone/2.1.6>`_ (2018-12-23)
------------------------------------------------------------------------


* Fix crash when loading a Qt5 Soundsource / Vamp Plug-In. `lp:1774639 <https://bugs.launchpad.net/mixxx/+bug/1774639>`_
* Validate effect parameter range. `lp:1795234 <https://bugs.launchpad.net/mixxx/+bug/1795234>`_
* Fix crash using the bpm_tap button without a track loaded. `lp:1801844 <https://bugs.launchpad.net/mixxx/+bug/1801844>`_
* Fix possible crash after ejecting a track. `lp:1801874 <https://bugs.launchpad.net/mixxx/+bug/1801874>`_
* Fix wrong bitrate reported for faulty mp3 files. `lp:1782912 <https://bugs.launchpad.net/mixxx/+bug/1782912>`_
* Fix Echo effect syncing `lp:1793232 <https://bugs.launchpad.net/mixxx/+bug/1793232>`_
* Fix iTunes context menu `lp:1799932 <https://bugs.launchpad.net/mixxx/+bug/1799932>`_
* Fix loading the wrong track after delete search and scroll. `lp:1803148 <https://bugs.launchpad.net/mixxx/+bug/1803148>`_
* Improve search bar timing. `lp:1635087 <https://bugs.launchpad.net/mixxx/+bug/1635087>`_
* Fix quoted search sentence. `lp:1784141 <https://bugs.launchpad.net/mixxx/+bug/1784141>`_
* Fix loading a track formerly not existing. `lp:1800395 <https://bugs.launchpad.net/mixxx/+bug/1800395>`_
* Fix importing m3u files with blank lines. `lp:1806271 <https://bugs.launchpad.net/mixxx/+bug/1806271>`_
* Fix position in sampler overview waveforms. `lp:1744170 <https://bugs.launchpad.net/mixxx/+bug/1744170>`_
* Don't reset rate slider, syncing a track without a beatgrid. `lp:1783020 <https://bugs.launchpad.net/mixxx/+bug/1783020>`_
* Clean up iTunes track context menu. `lp:1800335 <https://bugs.launchpad.net/mixxx/+bug/1800335>`_
* Collapsed sampler are not analyzed on startup. `lp:1801126 <https://bugs.launchpad.net/mixxx/+bug/1801126>`_
* search for decoration characters like "˚". `lp:1802730 <https://bugs.launchpad.net/mixxx/+bug/1802730>`_
* Fix cue button blinking after pressing eject on an empty deck. `lp:1808222 <https://bugs.launchpad.net/mixxx/+bug/1808222>`_

.. _v2-1-5:

`2.1.5 <https://launchpad.net/mixxx/+milestone/2.1.5>`_ (2018-10-28)
------------------------------------------------------------------------


* Code signing for Windows builds. `lp:1517823 <https://bugs.launchpad.net/mixxx/+bug/1517823>`_
* Fix crash on exit when preferences is open. `lp:1793185 <https://bugs.launchpad.net/mixxx/+bug/1793185>`_
* Fix crash when analyzing corrupt MP3s. `lp:1793387 <https://bugs.launchpad.net/mixxx/+bug/1793387>`_
* Fix crash when importing metadata from MusicBrainz. `lp:1794993 <https://bugs.launchpad.net/mixxx/+bug/1794993>`_
* Library search fixes when single quotes are used. `lp:1784090 <https://bugs.launchpad.net/mixxx/+bug/1784090>`_ `lp:1789728 <https://bugs.launchpad.net/mixxx/+bug/1789728>`_
* Fix scrolling waveform on Windows with WDM-KS sound API. `lp:1729345 <https://bugs.launchpad.net/mixxx/+bug/1729345>`_
* Fix right clicking on beatgrid alignment button in Tango and LateNight skins. `lp:1798237 <https://bugs.launchpad.net/mixxx/+bug/1798237>`_
* Improve speed of importing iTunes library. `lp:1785545 <https://bugs.launchpad.net/mixxx/+bug/1785545>`_
* Add 2 deck mapping for DJTechTools MIDI Fighter Twister.

.. _v2-1-4:

`2.1.4 <https://launchpad.net/mixxx/+milestone/2.1.4>`_ (2018-08-29)
------------------------------------------------------------------------

Fix track selection not getting shown in the track
table on Windows. There are no changes to the
source code, but the Jenkins build configuration
was changed to delete the Jenkins workspace before
each build. `lp:1751482 <https://bugs.launchpad.net/mixxx/+bug/1751482>`_

.. _v2-1-3:

`2.1.3 <https://launchpad.net/mixxx/+milestone/2.1.3>`_ (2018-08-20)
------------------------------------------------------------------------

Fix a severe performance regression on Windows:
`Mixxx 2.1.2 running much slower than 2.1.1 <https://mixxx.org/forums/viewtopic.php?f=3&t=12082>`_

.. _v2-1-2:

`2.1.2 <https://launchpad.net/mixxx/+milestone/2.1.2>`_ (2018-08-10)
------------------------------------------------------------------------

Yet another bugfix release of Mixxx 2.1.
Here is a quick summary of what is new in Mixxx 2.1.2:


* Allow maximum deck speed of 4x normal.
* Don't always quantize hotcues, a 2.1.1 regression. `lp:1777429 <https://bugs.launchpad.net/mixxx/+bug/1777429>`_
* Fix artifacts using more than 32 samplers. `lp:1779559 <https://bugs.launchpad.net/mixxx/+bug/1779559>`_
* store No EQ and Filter persistently. `lp:1780479 <https://bugs.launchpad.net/mixxx/+bug/1780479>`_
* Pad unreadable samples with silence on cache miss. `lp:1777480 <https://bugs.launchpad.net/mixxx/+bug/1777480>`_
* Fixing painting of preview column for Qt5 builds. `lp:1776555 <https://bugs.launchpad.net/mixxx/+bug/1776555>`_
* LateNight: Fix play button right click. `lp:1781829 <https://bugs.launchpad.net/mixxx/+bug/1781829>`_
* LateNight: Added missing sort up/down buttons.
* Fix sampler play button tooltips. `lp:1779468 <https://bugs.launchpad.net/mixxx/+bug/1779468>`_
* Shade: remove superfluid margins and padding in sampler.xml. `lp:1773588 <https://bugs.launchpad.net/mixxx/+bug/1773588>`_
* Deere: Fix background-color code.
* ITunes: Don't stop import in case of duplicated Playlists. `lp:1783493 <https://bugs.launchpad.net/mixxx/+bug/1783493>`_

.. _v2-1-1:

`2.1.1 <https://launchpad.net/mixxx/+milestone/2.1.1>`_ (2018-06-13)
------------------------------------------------------------------------

After two months it is time to do a bugfix release of Mixxx 2.1.
Here is a quick summary of what is new in Mixxx 2.1.1:


* Require Soundtouch 2.0 to avoid segfault. `lp:1577042 <https://bugs.launchpad.net/mixxx/+bug/1577042>`_
* Improved skins including library view fix. `lp:1773709 <https://bugs.launchpad.net/mixxx/+bug/1773709>`_ `lp:1772202 <https://bugs.launchpad.net/mixxx/+bug/1772202>`_ `lp:1763953 <https://bugs.launchpad.net/mixxx/+bug/1763953>`_
* Fix crash when importing ID3v2 APIC frames. `lp:1774790 <https://bugs.launchpad.net/mixxx/+bug/1774790>`_
* Synchronize execution of Vamp analyzers. `lp:1743256 <https://bugs.launchpad.net/mixxx/+bug/1743256>`_
* DlgTrackInfo: Mismatching signal/slot connection.
* Detect M4A decoding errors on Windows. `lp:1766834 <https://bugs.launchpad.net/mixxx/+bug/1766834>`_
* Fix spinback inertia effect.
* Fix decoding fixes and upgrade DB schema. `lp:1766042 <https://bugs.launchpad.net/mixxx/+bug/1766042>`_ `lp:1769717 <https://bugs.launchpad.net/mixxx/+bug/1769717>`_
* Fix integration of external track libraries. `lp:1766360 <https://bugs.launchpad.net/mixxx/+bug/1766360>`_
* Fix memory leak when loading cover art. `lp:1767068 <https://bugs.launchpad.net/mixxx/+bug/1767068>`_
* Fix clearing of ReplayGain gain/ratio in file tags. `lp:1766094 <https://bugs.launchpad.net/mixxx/+bug/1766094>`_
* Fix crash when removing a quick link. `lp:1510068 <https://bugs.launchpad.net/mixxx/+bug/1510068>`_
* Fidlib: Thread-safe and reentrant generation of filters. `lp:1765210 <https://bugs.launchpad.net/mixxx/+bug/1765210>`_
* Fix unresponsive scrolling through crates & playlists using encoder. `lp:1719474 <https://bugs.launchpad.net/mixxx/+bug/1719474>`_
* Swap default values for temp/perm rate changes. `lp:1764254 <https://bugs.launchpad.net/mixxx/+bug/1764254>`_

.. _v2-1-0:

`2.1.0 <https://launchpad.net/mixxx/+milestone/2.1.0>`_ (2018-04-15)
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

`2.0.0 <https://launchpad.net/mixxx/+milestone/2.0.0>`_ (2015-12-31)
------------------------------------------------------------------------


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

For a full list of new features and bugfixes, check out the
`2.0.0 milestone on Launchpad <https://launchpad.net/mixxx/+milestone/2.0.0>`_.


.. seealso:: For an overview of previous versions, `take a look
             <https://launchpad.net/mixxx/+series>`_ at the timeline.
