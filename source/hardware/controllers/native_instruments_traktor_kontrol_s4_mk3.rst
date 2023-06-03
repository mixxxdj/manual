Native Instruments Traktor Kontrol S4 MK3
=========================================

The Kontrol S4 MK3 is a 4 deck all-in-one controller with a sturdy build quality and integrated sound card.
Compared to the MK2 and MK1, it also have motorised shiny aluminum jogwheels, screens and a set of pads which can be use for
various features.

The S4 MK3 uses the standard :term:`HID` protocol for the Buttons, Knobs, Faders and LEDs, and extends it for the motorized Jog-Wheels.
The screens use a USB Bulk transfer. Mixxx doesn't support rendering content for external screens yet.
The easiest way to tell the MK3 apart from the other MK1 and 2 are these screens, displace between the "Move" and "Loop" encoder.

The Kontrol S4 Mk3 can run from :term:`USB` power.
Using the separate power supply increases the brightness of the LEDs, which is helpful for using it in daylight, and increases the volume of the headphone output.

-  `Manufacturer’s product page <https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s4/>`__

.. versionadded:: 2.4

Compatibility
-------------

The Kontrol S4 MK3 is a USB class compliant audio and :term:`HID`, so it is compatible with Mixxx without any proprietary drivers on GNU/Linux, MacOS and Windows.

With the S4 plugged in, a HID device is listed as an available controller in Mixxx’s Preferences.
The controller uses HID for each components on the device, except the screens, so the mapping can only be loaded when you select the HID device on the left side of Mixxx’s Preferences.

Controller
-------------

Setup audio output
~~~~~~~~~~~~~~~~~~

In order to use the audio output of the controller, `Channels 1 - 2` should be set as `Main` and `Channels 3 - 4` should be set as `Headphones`

   .. note:: The master and headphone knobs aren't mapped to Mixxx but instead control the the hardware directly. If you don't use the controller outputs, these knobs won't have any effect.


Known bugs and limitation
~~~~~~~~~~~~~~~~~~~~~~~~~

Audio
^^^^^

During the development phase, it appears that using other Sound API than `ALSA` would lead the Master VU meter not to work. Furthermore, audio output power would be half as loud as it should
be, which can be a problem if you are also using other software, since you audio setting will suddenly become twice as loud. It remains unclear whether or not this was a common issue or if
this was specific to the used setup.

Screens
^^^^^^^

Currently, Mixxx doesn't support controller screen rendering. However, because the screens are technically a different device, it is safe to interact with them outside of Mixxx while
the device is being used by Mixxx. This can be particularly handy if you want to display some images or text, or even dynamic information.

.. _use-motors:

Motors
^^^^^^

Haptic feedback (know as Haptic Drive (TM)) are partially implemented. Supported features include jogwheel tensions and turntable mode but these features remains in beta and
may sometime have unexpected behaviours. Since there is no guarantee on the long term effect to the controller of how Mixxx implements these features, they are disabled by default.
You can enable them by setting `UseMotors` to `true` in :ref:`settings`.


Mapping Description
-------------------

.. _jogwheel-modes:

Jogwheel modes
~~~~~~~~~~~~~~

Jogwheel can be used to control various things, depending of the mode they are in.

1. **Vinyl mode** (*default*): The jogwheel platter can be used for scratch. The jogwheel crown can be used to jog up or down the playback.
2. **Jog mode**: The wheel platter and crown can be used to jog up or down the playback.
3. **Turntable mode**: The wheel behaves as a 33.3 RPM turntable. If the platter or crown are slowed down or speeded up, then it will scratch down or up the track.

   .. warning:: Because this mode relies on Mixxx's scratch mode, if the track has been pitched up, the keylock will be ignored!

   .. note:: This mode is only available if the motor features are enabled. See :ref:`use-motors` for more details.

4. **Loop in**: The wheel behaves similarly to CDJ. If the platter or crown are turned, it will move back or forth the start of the loop. Additionally, if the loop encoder is used, it will move the all loop back or forth.
5. **Loop out**: The wheel linke for the **loop in** mode, but for the exit of the loop. If the platter or crown are turned, it will move back or forth the end of the loop. Additionally, if the loop encoder is used in the same way than **Loop in** mode.

Here is how to tell what mode is on, depending the current state of the LED:

+----------------+----------+---------+------------------------------------------------+-----------------------------------------+
| Mode           | Jog      | TT      | Jogwheel                                       | Others                                  |
+================+==========+=========+================================================+=========================================+
| Vinyl mode     | On       | Off     | Circling while the track is playing/scratching | --                                      |
+----------------+----------+---------+------------------------------------------------+-----------------------------------------+
| Jog mode       | Off      | Off     | Circling while the track is playing/scratching | --                                      |
+----------------+----------+---------+------------------------------------------------+-----------------------------------------+
| Turntable mode | Off      | On      | Circling while the track is playing/scratching | --                                      |
+----------------+----------+---------+------------------------------------------------+-----------------------------------------+
| Loop in        | --       | --      | The whole circle is blinking                   | The "Rev" button is blinking            |
+----------------+----------+---------+------------------------------------------------+-----------------------------------------+
| Loop out       | --       | --      | The whole circle is blinking                   | The "Flx" button is blinking            |
+----------------+----------+---------+------------------------------------------------+-----------------------------------------+

Here is how to select each mode:

+----------------+---------------------------------------------------------------------------+
| Mode           |                                                                           |
+================+===========================================================================+
| Vinyl mode     | Press the "Jog" button (while the "Jog" button is off)                    |
+----------------+---------------------------------------------------------------------------+
| Jog mode       | Press the "Jog" button wgile in vinyl mode (while the "Jog" button is on) |
+----------------+---------------------------------------------------------------------------+
| Turntable mode | Press the "TT" button. Pressing again while restore the Vinyl mode        |
+----------------+---------------------------------------------------------------------------+
| Loop in        | Press :hwlabel:`SHIFT` + REV while a loop is enable                       |
+----------------+---------------------------------------------------------------------------+
| Loop out       | Press :hwlabel:`SHIFT` + Flux while a loop is enable                      |
+----------------+---------------------------------------------------------------------------+

For all modes but "Vinyl" and "Jog", re-selecting the mode will restore the previous one.


Move modes
~~~~~~~~~~

Moves modes define how the "move" encoder (the one on the left) reacts when used. Here are all the various modes:

1. **Beat** (*default*): The track will jump backward or forward by the number of beats selected. Press before turning to select the number of beats.
2. **Grid**: The track's detected beats will be move forward or backward on the waveform.
3. **BPM**: The track's detected BPM will be increased or decreased.
4. **Keyboard**: The keyboard's keys displayed on pads get moved up or down to display higher or lower keynotes.

Here is how to tell use each modes:

+----------+-------------------------------------------------------------+
| Mode     |                                                             |
+==========+=============================================================+
| Beat     | This mode is enable if no other mode are enabled            |
+----------+-------------------------------------------------------------+
| Grid     |  This mode is enabled while GRID is maintained pressed      |
+----------+-------------------------------------------------------------+
| BPM      | This mode is enabled while :hwlabel:`SHIFT` + GRID is       |
|          | maintained pressed                                          |
+----------+-------------------------------------------------------------+
| Keyboard | This mode is enabled while STEM is maintained pressed       |
+----------+-------------------------------------------------------------+

All mapping detail
~~~~~~~~~~~~~~~~~~

+------------------+------------------------------------------------------------------+------------------------------------------+
| Button           | Action                                                           | Lighting                                 |
+==================+==================================================================+==========================================+
| Jogwheel platter | - Scratch when in Vinyl mode and Turntable mode                  | - Static light rotation: Vinyl,          |
|                  | - Jog when in Jog mode                                           |   Turntable or Jog mode on               |
|                  | - Move loop start when in Loop In mode                           | - Ring blinking: Loop in or out mode on  |
|                  | - Move loop end when in Loop Out mode                            |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Jogwheel crown   | - Jog when in Vinyl mode                                         |                                          |
|                  | - Same as wheel platter otherwise                                |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Flux             | - Toggle Slip mode                                               | - Steady on: Reverse                     |
|                  | - On shift, set a loop end at the current track position if no   |   enabled                                |
|                  |   active loop, enable loop out wheel mode otherwise              | - Steady on while pressing               |
|                  |                                                                  |   :hwlabel:`SHIFT`: loop is active       |
|                  |                                                                  | - Blinking, but flux steady off while    |
|                  |                                                                  |   pressing :hwlabel:`SHIFT`: loop in set |
|                  |                                                                  |   wheel mode                             |
|                  |                                                                  | - Blinking, with flux steady on while    |
|                  |                                                                  |   pressing :hwlabel:`SHIFT`: loop in     |
|                  |                                                                  |   wheel mode active                      |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Reverse          | - Toggle reverse mode                                            | - Steady on: Flux                        |
|                  | - On shift, set a loop in the current track position if no active|   enabled                                |
|                  |   loop, enable loop out wheel mode otherwise                     | - Steady on while pressing               |
|                  |                                                                  |   :hwlabel:`SHIFT`: loop is active       |
|                  |                                                                  | - Blinking, with reverse steady on       |
|                  |                                                                  |   while pressing :hwlabel:`SHIFT`: loop  |
|                  |                                                                  |   out wheel mode active                  |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Grid             | - Set the beatgrid at the current track position (on release,    | - On when over a detected beat           |
|                  |   short press)                                                   | - Blinking when grid/BPM move is on      |
|                  | - Enable grid move mode while pressed                            | - Blinking when grid move mode is        |
|                  | - Enable BPM move mode while pressed and pressing                |   enabled                                |
|                  |   :hwlabel:`SHIFT`                                               |   enabled                                |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Turntable        | - Toggle on or off the turntable mode                            | - On: Turntable mode on, otherwise jog   |
|                  |                                                                  |   or vinyl                               |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Jog              | - Toggle on or off the vinyl mode                                | - On: Vinyl mode on, otherwise jog or    |
|                  |                                                                  |   turntable                              |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Deck Select      | - Select a deck                                                  | - The deck's main color will be the one  |
|                  |                                                                  |   of the selected deck                   |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Shift            | Shift controls for the all controller side, including effect     | - On or Off                              |
|                  | unit                                                             |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Cue              | - Trigger the cue default effect                                 | Depends of the cue mode                  |
|                  | - Start or stop the track while pressing :hwlabel:`SHIFT`        |                                          |
|                  | - Select the cue as the play mode when in Keyboard move mode     |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Play/Pause       | - Play/Pause the track                                           | On if track is playing                   |
|                  | - Long press: clone the playing track                            |                                          |
|                  | - :hwlabel:`SHIFT` + Long press: eject track                     |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Move             | - Beat jump forward (right) or backward by the number of         |                                          |
|                  |   selected beats                                                 |                                          |
|                  | - Increase/Decrease the beats if turned while pressed            |                                          |
|                  | - Increase/decrease pitch when pressing :hwlabel:`SHIFT`         |                                          |
|                  | - Move backward/forward the grid when in grid move mode          |                                          |
|                  | - Increase/decrease BPM when in BPM move mode                    |                                          |
|                  | - Move down/up the keyboard notes when in keyboard move mode     |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Loop             | - Enable/disable loop when pressed                               |                                          |
|                  | - Reactivate exited loop/exit loop when pressed and shifted      |                                          |
|                  | - Halve/double the loop size                                     |                                          |
|                  | - Move 1 beat backward/forward when shifted                      |                                          |
|                  | - On loop in/out wheel mode: move the loop with precision, left  |                                          |
|                  |   precision if shifted                                           |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Master           | - Make the current deck sync leader (on release)                 | - Steady on: the deck is sync leader     |
|                  | - Long press: Enabled/disable full range tempo fader             | - Blinking: the tempo fader is in full   |
|                  |                                                                  |   range                                  |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Sync             | - Toggle the sync mode (on release)                              | - On while no shift: Sync is on          |
|                  | - Toggle the keylock (on release)                                | - On while shift: Keylock is on          |
|                  | - Long press: copy the BPM of the other deck                     |                                          |
|                  | - :hwlabel:`SHIFT` + Long press: copy the key of the other deck  |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Tempo fader      | While change the tempo only of the left indicator is either off  | Deck color: default track speed          |
|                  | or of the color of the deck.                                     | Green: out of sync (down)                |
|                  |                                                                  | Green: out of sync (up)                  |
|                  | - If green, it means the fader is out of sync with the software, |                                          |
|                  |   bringing it down will eventually catch up.                     |                                          |
|                  | - If white, it means the fader is out of sync with the software, |                                          |
|                  |   bringing it up will eventually catch up.                       |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Hotcues          | - Toggle the hotcues page                                        | - Deck color with dim off: Current page  |
|                  | - Shift: toggle the second hotcue page                           |   isn't related to hotcue                |
|                  |                                                                  | - Deck color with dim on: page 1 of      |
|                  |                                                                  |   hotcue                                 |
|                  |                                                                  | - White: page 2 of hotcue                |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Rec              | Currently unused                                                                                            |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Sampler          | - Toggle the sampler page and display samplers on the Using      | - Off: Current page isn't related to     |
|                  |                                                                  |   sampler                                |
|                  |                                                                  | - On: sampler page is active             |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Mute             | Currently unused                                                                                            |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Stems            | - Toggle the keyboard (on release) while press: enable keyboard  | - Deck color with dim off: Current page  |
|                  |   move mode                                                      |   isn't related to keyboard              |
|                  |                                                                  | - Deck color with dim on: Keyboard       |
|                  |                                                                  |   active                                 |
|                  |                                                                  | - Green: keyboard play mode active       |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Pads             | - While in hotcue:                                               | - In hotcue: color of the cue            |
|                  |                                                                  | - In Sampler: Dim on, sample is playing  |
|                  |   - press will activate                                          |   dim off sampler is stopped,            |
|                  |   - :hwlabel:`SHIFT` + press will delete                         |   off no sampler loaded                  |
|                  |                                                                  | - In keyboard: keyboard color on each    |
|                  | - While in sample:                                               |   note, if Dim on, currently             |
|                  |                                                                  |   active note                            |
|                  |   - press will play (load selected track if none are)            | - In Beatloop roll: dimed on means a     |
|                  |   - :hwlabel:`SHIFT` + press will stop (if playing) or eject     |   loop rool is active with the given     |
|                  |                                                                  |   size                                   |
|                  | - While in keyboard:                                             |                                          |
|                  |                                                                  |                                          |
|                  |   - will set the key to the selected note                        |                                          |
|                  |   - will play from the cue if in keyboard play mode              |                                          |
|                  |                                                                  |                                          |
|                  | - While in beatlooproll mode:                                    |                                          |
|                  |                                                                  |                                          |
|                  | - Will activate a beatlooproll of 1/16, 1/8, 1/4 , 1/2, 1,       |                                          |
|                  |   2, 4 and 8 beats, or custom size if you have change            |                                          |
|                  |   `BeatLoopRolls` in :ref:`settings`                             |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| FX 1st knob      | - Master volume/mix of the unit                                  |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| FX 2nd knob      | - Meta arg of the first selected effect                          |                                          |
|                  | - First arg of the focused effect in effect focus mode           |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| FX 3rd knob      | - Meta arg of the second selected effect                         |                                          |
|                  | - Second arg of the focused effect in effect focus mode          |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| FX 4th knob      | - Meta arg of the third selected effect                          |                                          |
|                  | - Third arg of the focused effect in effect focus mode           |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| FX 1st button    | - Trigger all effect                                             | - On if all effect are off and not       |
|                  | - Trigger all effect                                             |   pressing :hwlabel:`SHIFT`              |
|                  | - Assign/de-assign effect to master while pressing               | - On when effect is attached to master   |
|                  |   :hwlabel:`SHIFT` and no focused effect                         |   and pressing :hwlabel:`SHIFT`          |
|                  | - Exit focused mode while pressing :hwlabel:`SHIFT` and          | - Blinking in effect focused mode        |
|                  |   focused effect                                                 | - Blinking in effect focused mode        |
+------------------+------------------------------------------------------------------+------------------------------------------+
| FX 2nd button    | - Toggle (short press) or trigger (long press) third effect      | - On if effect is active and no focused  |
|                  |   if not focused effect or if pressing :hwlabel:`SHIFT`          |   effect or if pressing :hwlabel:`SHIFT` |
|                  | - Toggle first arg (short press) or trigger first arg            | - On if focused effect parameter is      |
|                  |   (long press) of the focus effect if any                        |   enable                                 |
|                  | - Switch to next effect available if no focus effect and         |                                          |
|                  |   :hwlabel:`SHIFT`                                               |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| FX 3rd button    | - Toggle (short press) or trigger (long press) third effect      | - On if effect is active and no focused  |
|                  |   if not focused effect or if pressing :hwlabel:`SHIFT`          |   effect or if pressing :hwlabel:`SHIFT` |
|                  | - Toggle second arg (short press) or trigger second arg          | - On if focused effect parameter is      |
|                  |   (long press) of the focus effect if any                        |   enable                                 |
|                  | - Switch to next effect available if no focus effect and         |                                          |
|                  |   :hwlabel:`SHIFT`                                               |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| FX 4th button    | - Toggle (short press) or trigger (long press) third effect      | - On if effect is active and no focused  |
|                  |   if not focused effect or if pressing :hwlabel:`SHIFT`          |   effect or if pressing :hwlabel:`SHIFT` |
|                  | - Toggle (short press) or trigger (long press) third arg         | - On if focused effect parameter is      |
|                  |   on the focus effect if any                                     |   enable                                 |
|                  | - Switch to next effect available if no focus effect and         |                                          |
|                  |   :hwlabel:`SHIFT`                                               |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Library knob     | - Move up/down in tracklist                                      |                                          |
|                  | - Move up/down in tree structure while shifted                   |                                          |
|                  | - Move up/down in the context menu if playlist button is pressed |                                          |
|                  | - Zoom in/out the waveform when in grid move mode                |                                          |
|                  | - Beatjump by 16 beats backward/forward if a track is being      |                                          |
|                  |   previewed using the button                                     |                                          |
|                  | - Star down/up the currently playing track while pressing the    |                                          |
|                  |   star button                                                    |                                          |
|                  | - Sort by next/previous column while pressing the view button    |                                          |
|                  | - Expand the context-manu item when pressed while pressing the   |                                          |
|                  |   playlist button                                                |                                          |
|                  | - Load track when pressed or expand/collapse tree node when      |                                          |
|                  |   shifted (if view button is not pressed)                        |                                          |
|                  | - Inverse the column sorting if view button is pressed           |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Preview button   | Preview the currently selected track while pressed               |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Star button      | Change the selected track color on short press (next color, or   |                                          |
|                  | previous if shifted)                                             |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Playlist button  | Open or close a context menu for the currently selected track    | On if there is a context-menu open, off  |
|                  |                                                                  | otherwise                                |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Mixer FX button  | Toggle third effect (short press) or trigger third effect        | - Dim on if the effect is active         |
|                  | (long press) or assign the quick effect                          |                                          |
|                  | of FX select buttons are pressed                                 |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| FX Select        | Apply effect to all deck on release, if no mixer FX button have  |                                          |
| button           | been pressed                                                     |                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+
| Ext              | Apply the current gain as default. This will reset the gain knob.|                                          |
+------------------+------------------------------------------------------------------+------------------------------------------+


Looping
^^^^^^^

===================================================== ==============================================================================
Control                                               Description
===================================================== ==============================================================================
Right Encoder (turn)                                  Double/halve loop size.
Right Encoder (press)                                 Activate/exit loop of set size from current position
:hwlabel:`SHIFT` + :hwlabel:`REV` (while no loops are enabled)   Set the loop in point. This will reset the loop out point as well.
:hwlabel:`SHIFT` + REV (while a loop is enabled)      Toggle the loop in jogwheel mode. See :ref:`jogwheel-modes` for more details.
:hwlabel:`SHIFT` + FLX (while no loops are enabled)   Set the loop out point.
:hwlabel:`SHIFT` + FLX (while a loop is enabled)      Toggle the loop out jogwheel mode. See :ref:`jogwheel-modes` for more details.
===================================================== ==============================================================================

.. _settings:

Mapping options
---------------


There are various option that can be used to change some behavior:

======================================================================= =========================================== ================================================================================================================= ===================================================================================== ====================================================================================================================================================================================
Setting                                                                 Variable value                              Default                                                                                                           Range                                                                                 Description
======================================================================= =========================================== ================================================================================================================= ===================================================================================== ====================================================================================================================================================================================
Deck colors                                                             `DeckColors`                                LEDColors.red,LEDColors.blue,LEDColors.yellow, LEDColors.purple                                                   **All colors as defined in _LedColors_. Must be four color, separated by a comma**    Define the leading colors for each decks. Note that some buttons have only one color
Sortable column in the library                                          `LibrarySortableColumns`                    LibraryColumns.Artist, LibraryColumns.Title, LibraryColumns.BPM, LibraryColumns.Key, LibraryColumns.DatetimeAdded **All values defined in** `the Mixxx control documentation`_ **separated by a comma** Define the list of columns on which it possible to sort the library using the library encoder and the view button
Loop In/Out jogwheel sensistivity                                       `LoopWheelMoveFactor`                       50                                                                                                                -500..500 (Recommended)                                                               Define the sensistivity when moving the loop start or end point using the loop jogwheel mode. Negative value will reverse the order
Loop encoder sensistivity                                               `LoopEncoderMoveFactor`                     500                                                                                                               -3000..3000 (Recommended)                                                             Define the sensistivity when moving the loop with the encoder when using the loop jogwheel mode. Negative value will reverse the order
Loop encoder sensistivity (Shifted)                                     `LoopEncoderShiftMoveFactor`                2500                                                                                                              -5000..5000 (Recommended)                                                             Define the sensistivity when moving the loop with :hwlabel:`SHIFT` + the encoder when using the loop jogwheel mode. Negative value will reverse the order
Color of the tempo led when on low takeover                             `TempoFaderSoftTakeoverColorLow`            LEDColors.white                                                                                                   **All colors as defined on line 19**                                                  Define the color of thempo LED when the tempo fader is out of sync, and the actual value is less than on the controller
Color of the tempo led when on high takeover                            `TempoFaderSoftTakeoverColorHigh`           LEDColors.green                                                                                                   **All colors as defined on line 19**                                                  Define the color of thempo LED when the tempo fader is out of sync, and the actual value is more than on the controller
Keep transport and play button dimmed when off                          `KeepLEDWithOneColorDimedWhenInactive`      true                                                                                                              true/false                                                                            Having this setting on will keep LED always dimmed, even when off, although they may not have a matching color with the deck's color
Keep the unselected deck button offrather than show its deck color      `KeepDeckSelectDimmed`                      true                                                                                                              true/false                                                                            Having this setting on will keep the LED of the unselected deck dimmed instead of off.
Keylock on :hwlabel:`SHIFT` + MASTER instead of :hwlabel:`SHIFT` + SYNC `UseKeylockOnMaster`                        false                                                                                                             true/false                                                                            Use :hwlabel:`SHIFT` + MASTER to toggle the keylock instead of :hwlabel:`SHIFT` + SYNC
Make the grid button blink when over a detected beat                    `GridButtonBlinkOverBeat`                   false                                                                                                             true/false                                                                            Make the GRID button blinking when the playback goes over a detected beat
Make the jogwheel ring blink when the track playing is near the end     `WheelLedBlinkOnTrackEnd`                   true                                                                                                              true/false                                                                            The jogwheel LED ring will start blinking when a track is near the end. The end section can be defined in :menuselection:`Preferences --> Waveforms --> End of track warning`
Use the mixer to control input when using :hwlabel:`SHIFT`              `MixerControlsMixAuxOnShift`                false                                                                                                             true/false                                                                            Make the GRID button blinking when the playback goes over a detected beat
Number of samples used for jogwheel speed                               `WheelSpeedSample`                          3                                                                                                                 1..50                                                                                 Number of samples used to determine the jogwheel movement. A higher value will increase precision but latency too, and vice-versa
Replace the sampler tab by a beatloop roll tab                          `UseBeatloopRollInsteadOfSampler`           false                                                                                                             true/false                                                                            Replace the sample tab as well of the sample feature with 8 beatlooproll
Define the predefined size to use for the beatloop tab                  `BeatLoopRolls`                             1/16,1/8,1/4,1/2,1,2,4,8                                                                                          eight number in range 1/32..512                                                       Define the size of loops of each pad, from left to right, starting from the top row.
Use the two last tab as loop half/double buttons in the beatloop tab    `AddLoopHalveAndDoubleOnBeatloopRollTab`    true                                                                                                              true/false                                                                            Use the last two pad from the bottom row as loop half and loop double. These can be used to interact with beatlooproll and normal loop.
Jogwheel speed (in turntable mode, as well as LED indicator)            `BaseRevolutionsPerMinute`                  33 + 1/3                                                                                                          33+1/3, 45 (Recommended)                                                              The turntable mode defines how fast the jogwheel turns (if on) as well as the LED, and the overall jogwheel sensitivity. It is recommended to keep either 33 + 1/3 or 45 as a value
Whether or not to use haptic feedback features                          `UseMotors`                                 false                                                                                                             true/false                                                                            Whether or not to use haptic feedback features. This is a beta feature, some of them may be unstable.
======================================================================= =========================================== ================================================================================================================= ===================================================================================== ====================================================================================================================================================================================

.. _the Mixxx control documentation: https://manual.mixxx.org/latest/en/chapters/appendix/mixxx_controls.html#control-[Library]-sort_column

This settings are only useful if you are using haptic feedback features

================================================================ =========================================== ============== ============================================== ==========================================================================================================================================================
Setting                                                          Variable value                              Default        Range                                          Description
================================================================ =========================================== ============== ============================================== ==========================================================================================================================================================
Number of samples used for jogwheel speed in turntable mode      `TurnTableSpeedSample`                      20             1..50                                          Number of samples used to determine the jogwheel movement when the turntable is on. A higher value will increase precision but latency too, and vice-versa
Define the tension of the jogwheel                               `TightnessFactor`                           0.5            0..1.0                                         Define the jogwheel tension. 0 makes it very tight while 1 makes it very loose
Define how much force can the jogwheel use                       `MaxWheelForce`                             25000          10000..30000 (Recommended, can go up to 60000) Define how much resistance can the wheel use when its rotation is held
================================================================ =========================================== ============== ============================================== ==========================================================================================================================================================


Making these changes is still a little awkward and we will be making controller preferences easier to change in the future.
For now you’ll have to make a small change to the mapping script file. Don’t worry, the actual edit only involves replacing a single word in a text file.

1. Open Mixxx Preferences and select the Kontrol S4 in the side list.
2. Select :file:`Traktor-Kontrol-S4-MK3-hid-scripts.js`.
3. Click :guilabel:`Open Selected File`.
4. Either the file should open in an editor, or you should see a file browser window with that file selected. If you see a file browser, right click the file and select an option to edit it.
5. Starting from the block entitled `USER CONFIGURABLE SETTINGS`, there should be configurable options.
