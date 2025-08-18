Native Instruments Traktor Kontrol S4 MK3
=========================================

The Kontrol S4 MK3 is a 4-deck all-in-one controller with a sturdy build quality and integrated sound card.
Compared with the MK2 and MK1, it also has motorized aluminum jog wheels, LCD screens and a set of pads which can be used for various features.

The S4 MK3 uses a standard USB :term:`HID` protocol for the Buttons, Knobs, Faders and LEDs, and extends it for the motorized Jog-Wheels.
The screens use a custom USB Bulk transfer protocol.
Mixxx doesn't support rendering content for external screens yet, but that work is in progress and will be available in a future version.
The easiest way to tell the MK3 apart from the older MK1 and MK2 are these screens, between the "Move" and "Loop" encoders.

Unlike its predecessor, the Kontrol S4 Mk3 cannot run solely on :term:`USB` power and a separate power supply must be used.

-  `Manufacturer's product page <https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s4/>`__

.. versionadded:: 2.4

Compatibility
-------------

The Kontrol S4 MK3 is a USB class compliant audio and :term:`HID` device, so it is compatible with Mixxx without any proprietary drivers on GNU/Linux, MacOS and Windows.

With the S4 plugged in, a HID device is listed as an available controller in the Mixxx Preferences.
The controller uses HID for each components on the device except the screens, so the mapping can only be loaded when you select the HID device on the left side of Mixxx's Preferences.

Controller
-------------

Setup audio output
~~~~~~~~~~~~~~~~~~

Using the S4 audio interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use the audio output of the controller, select the device :guilabel:`Traktor Kontrol S4 MK3`. :guilabel:`Channels 1 - 2` should be set as :guilabel:`Main` and :guilabel:`Channels 3 - 4` should be set as :guilabel:`Headphones`.

Using software mixing
^^^^^^^^^^^^^^^^^^^^^

If you don't want to use the audio outputs of the controller, you can enable the mapping of the mixer knob to the Mixxx internal mixer.
Head over to the :ref:`settings` to enable these optional mappings.

   .. note:: The mixer knobs are physically linked to the S4 embedded mixer. This means that there is no way to prevent these buttons to adjust gains of the output and will lead to unexpected volume mixing if the Mixxx mixer is used while also using the S4's outputs.


Known bugs and limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~

Audio
^^^^^

On GNU/Linux, it appears that using a sound API other than `ALSA` causes the Master VU meter not to work.
Furthermore, audio output level is half as loud as it should be.
It remains unclear whether or not this was a common issue or if
this was specific to the used setup.
Users should use the ALSA sound API for the best performance.

Screens
^^^^^^^

Currently, Mixxx doesn't support controller screen rendering.

.. _use-motors:

Motors
^^^^^^

Haptic feedback (know as Haptic Drive (TM)) is partially implemented.
Supported features include jog wheel tension and turntable mode but these features remain in beta and may have unexpected behaviour.
To avoid any possible chance that incorrect motor settings might affect the controller in the long term these features are disabled by default.
You can enable them by setting `UseMotors` to `true` in :ref:`settings`.


Mapping Description
-------------------

.. _jog-wheel-modes:

Jog wheel modes
~~~~~~~~~~~~~~~

The jog wheel can be used to control various things, depending on the mode they are in.

1. **Vinyl mode** (*default*): The jog wheel platter can be used for scratching. The jog wheel crown can be used to increase or decrease the speed of playback.
2. **Jog mode**: The wheel platter and crown can be used to adjust the playback speed up or down.
3. **Turntable mode**: The wheel behaves like a 33.3 RPM turntable. Touching the platter or crown will scratch the track like a regular turntable.

   .. warning:: Because this mode relies on Mixxx's scratch mode, if the track has been pitched up, keylock will be ignored!

   .. note:: This mode is only available if the motor features are enabled. See :ref:`use-motors` for more details.

4. **Loop in**: The wheel behaves similarly to a Pioneer CDJ device. If the platter or crown are turned, it will adjust the start of the loop back and forth. Additionally, if the loop encoder is used, it will move the entire loop back and forth.
5. **Loop out**: Similar to the **loop in** mode, but with the end position of the loop. If the platter or crown are turned, it will move the end of the loop back and forth. Additionally, if the loop encoder is used it will move the entire loop in the same way as **Loop in** mode.

Here is how to tell what mode is enabled, depending the current state of the LED:

+----------------+----------------+---------------+------------------------------------------------+-----------------------------------------+
| Mode           | :hwlabel:`Jog` | :hwlabel:`TT` | Jogwheel LED                                   | Others                                  |
+================+================+===============+================================================+=========================================+
| Vinyl mode     | On             | Off           | Circling while the track is playing/scratching | --                                      |
+----------------+----------------+---------------+------------------------------------------------+-----------------------------------------+
| Jog mode       | Off            | Off           | Circling while the track is playing/scratching | --                                      |
+----------------+----------------+---------------+------------------------------------------------+-----------------------------------------+
| Turntable mode | Off            | On            | Circling while the track is playing/scratching | --                                      |
+----------------+----------------+---------------+------------------------------------------------+-----------------------------------------+
| Loop in mode   | --             | --            | The whole circle is blinking                   | The :hwlabel:`REV` button is blinking   |
+----------------+----------------+---------------+------------------------------------------------+-----------------------------------------+
| Loop out mode  | --             | --            | The whole circle is blinking                   | The :hwlabel:`FLX` button is blinking   |
+----------------+----------------+---------------+------------------------------------------------+-----------------------------------------+

Here is how to select each mode:

+----------------+---------------------------------------------------------------------------------------------+
| Mode           |                                                                                             |
+================+=============================================================================================+
| Vinyl mode     | Press the :hwlabel:`Jog` button (while the :hwlabel:`Jog` button is off)                    |
+----------------+---------------------------------------------------------------------------------------------+
| Jog mode       | Press the :hwlabel:`Jog` button while in vinyl mode (while the :hwlabel:`Jog` button is on) |
+----------------+---------------------------------------------------------------------------------------------+
| Turntable mode | Press the :hwlabel:`TT` button. Pressing again will restore the Vinyl mode                  |
+----------------+---------------------------------------------------------------------------------------------+
| Loop in        | Press :hwlabel:`SHIFT` + :hwlabel:`REV` while a loop is enabled                             |
+----------------+---------------------------------------------------------------------------------------------+
| Loop out       | Press :hwlabel:`SHIFT` + :hwlabel:`FLX` while a loop is enabled                             |
+----------------+---------------------------------------------------------------------------------------------+

For all modes but :hwlabel:`Vinyl` and :hwlabel:`Jog`, re-selecting the mode will restore the previous one.


Move modes
~~~~~~~~~~

Move modes define what effect the "move" encoder (the knob on the left) will have when used.
Here are all the various modes:

1. **Beat** (*default*): The track will jump backward or forward by the number of beats selected. Press before turning to select the number of beats.
2. **Grid**: The track's detected beats will be adjusted forward or backward on the waveform.
3. **BPM**: The track's detected BPM will be increased or decreased.
4. **Keyboard**: The melodic keys displayed on pads get adjusted up or down to display higher or lower notes.

Here is how to tell use each modes:

+----------+---------------------------------------------------------------------+
| Mode     |                                                                     |
+==========+=====================================================================+
| Beat     | This mode is enabled if no other modes are enabled                  |
+----------+---------------------------------------------------------------------+
| Grid     | This mode is enabled when :hwlabel:`GRID` is held down              |
+----------+---------------------------------------------------------------------+
| BPM      | This mode is enabled when :hwlabel:`SHIFT` + :hwlabel:`GRID` are    |
|          | held down                                                           |
+----------+---------------------------------------------------------------------+
| Keyboard | This mode is enabled when STEM is held down                         |
+----------+---------------------------------------------------------------------+

Full mapping details
~~~~~~~~~~~~~~~~~~~~

+-------------------+------------------------------------------------------------------+------------------------------------------+
| Button            | Action                                                           | Lighting                                 |
+===================+==================================================================+==========================================+
| Jog wheel platter | - Scratch when in Vinyl mode and Turntable mode                  | - light rotation: Vinyl,                 |
|                   | - Jog when in Jog mode                                           |   Turntable or Jog mode on               |
|                   | - Move loop start when in Loop In mode                           | - Ring blinking: Loop in or out mode on  |
|                   | - Move loop end when in Loop Out mode                            |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Jog wheel crown   | - Jog when in Vinyl mode                                         |                                          |
|                   | - Same as wheel platter otherwise                                |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Flux              | - Toggle Slip mode                                               | - Steady on: Reverse                     |
|                   | - On shift, if no active loop, set a loop end at the current     |   enabled                                |
|                   |   track position. Otherwise, enable loop out wheel mode          | - Steady on while pressing               |
|                   |                                                                  |   :hwlabel:`SHIFT`: loop is active       |
|                   |                                                                  | - Blinking and flux off,                 |
|                   |                                                                  |   pressing :hwlabel:`SHIFT`: loop in set |
|                   |                                                                  |   wheel mode                             |
|                   |                                                                  | - Blinking and flux steady on,           |
|                   |                                                                  |   pressing :hwlabel:`SHIFT`: loop in     |
|                   |                                                                  |   wheel mode active                      |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Reverse           | - Toggle reverse mode                                            | - Steady on: Flux                        |
|                   | - On shift, set a loop in the current track position if no active|   enabled                                |
|                   |   loop, otherwise enable loop out wheel mode                     | - Steady on while pressing               |
|                   |                                                                  |   :hwlabel:`SHIFT`: loop is active       |
|                   |                                                                  | - Blinking, with reverse steady on       |
|                   |                                                                  |   while pressing :hwlabel:`SHIFT`: loop  |
|                   |                                                                  |   out wheel mode active                  |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Grid              | - Set the beatgrid at the current track position (short press)   | - On when over a detected beat           |
|                   |                                                                  | - Blinking when grid/BPM move is on      |
|                   | - Enable grid move mode while pressed                            | - Blinking when grid move mode is        |
|                   | - With :hwlabel:`SHIFT`: enable BPM move mode while pressed      |   enabled                                |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Turntable         | - Toggle turntable mode                                          | - On: Turntable mode on, otherwise jog   |
|                   |                                                                  |   or vinyl                               |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Jog               | - Toggle vinyl mode                                              | - On: Vinyl mode on, otherwise jog or    |
|                   |                                                                  |   turntable                              |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Deck Select       | - Select a deck                                                  | - The deck's main color will be the one  |
|                   |                                                                  |   of the selected deck                   |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Shift             | Shift controls for that side of the controller, including effect | - On or Off                              |
|                   | unit                                                             |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Cue               | - Trigger the cue default button behavior                        | Depends on the cue mode                  |
|                   | - Start or stop the track while pressing :hwlabel:`SHIFT`        |                                          |
|                   | - Select the cue as the play mode when in Keyboard move mode     |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Play/Pause        | - Play/Pause the track                                           | On if track is playing                   |
|                   | - Long press: clone the playing track                            |                                          |
|                   | - :hwlabel:`SHIFT` + Long press: eject track                     |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Move              | - Beat jump forward or backward by the number of                 |                                          |
|                   |   selected beats                                                 |                                          |
|                   | - Increase/Decrease the move distance if turned while pressed    |                                          |
|                   | - When pressing :hwlabel:`SHIFT`, increase/decrease pitch        |                                          |
|                   | - Move the grid backward/forward when in grid move mode          |                                          |
|                   | - Increase/decrease BPM when in BPM move mode                    |                                          |
|                   | - Move keyboard notes down/up when in keyboard move mode         |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Loop              | - Enable/disable loop when pressed                               |                                          |
|                   | - Reactivate exited loop/exit loop when pressed and shifted      |                                          |
|                   | - Halve/double the loop size                                     |                                          |
|                   | - Move 1 beat backward/forward when shifted                      |                                          |
|                   | - On loop in/out wheel mode: move the loop with precision, left  |                                          |
|                   |   precision if shifted                                           |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Master            | - Make the current deck sync leader                              | - Steady on: the deck is sync leader     |
|                   | - Long press: Enabled/disable full range tempo fader             | - Blinking: the tempo fader is in full   |
|                   |                                                                  |   range                                  |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Sync              | - Toggle sync mode                                               | - On while no shift: Sync is on          |
|                   | - Toggle keylock                                                 | - On while shift: Keylock is on          |
|                   | - Long press: copy the BPM of the other deck                     |                                          |
|                   | - :hwlabel:`SHIFT` + Long press: copy the key of the other deck  |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Tempo fader       | Changes tempo only if the left indicator is either off           | Deck color: default track speed          |
|                   | or matches the color of the deck.                                | Green: out of sync (down)                |
|                   |                                                                  | Green: out of sync (up)                  |
|                   | - If green, it means the fader is out of sync with the software, |                                          |
|                   |   moving it down will eventually catch up.                       |                                          |
|                   | - If white, it means the fader is out of sync with the software, |                                          |
|                   |   moving it up will eventually catch up.                         |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Hotcues           | - Toggle the hotcues page                                        | - Deck color with dim off: Current page  |
|                   | - Shift: toggle the second hotcue page                           |   isn't related to hotcue                |
|                   |                                                                  | - Deck color with dim on: page 1 of      |
|                   |                                                                  |   hotcue                                 |
|                   |                                                                  | - White: page 2 of hotcue                |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Rec               | Currently unused                                                                                            |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Sampler           | - Toggle the sampler page and display samplers on the GUI        | - Off: Current page isn't related to     |
|                   |                                                                  |   sampler                                |
|                   |                                                                  | - On: sampler page is active             |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Mute              | Currently unused                                                                                            |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Stems             | - Toggle the keyboard mode(on release)                           |  - Deck color with dim off: Current page |
|                   | - while pressed: enable keyboard                                 |    isn't related to keyboard             |
|                   |   move mode                                                      |  - Deck color with dim on: Keyboard      |
|                   |                                                                  |    active                                |
|                   |                                                                  |  - Green: keyboard play mode active      |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Pads              | - While in hotcue mode:                                          | - Hotcue mode: color of the cue          |
|                   |                                                                  | - Sampler mode: Dim on, sample is playing|
|                   |   - press will activate                                          |   dim off sampler is stopped,            |
|                   |   - :hwlabel:`SHIFT` + press will delete                         |   off no sampler loaded                  |
|                   |                                                                  | - In keyboard: keyboard color on each    |
|                   | - While in sampler mode:                                         |   note, if Dim on, current               |
|                   |                                                                  |   active note                            |
|                   |   - press will play (load selected track if none are)            | - In Beatloop roll: brighter means a     |
|                   |   - :hwlabel:`SHIFT` + press will stop (if playing) or eject     |   loop roll is active with the given     |
|                   |                                                                  |   size                                   |
|                   | - While in keyboard mode:                                        |                                          |
|                   |                                                                  |                                          |
|                   |   - will set the key to the selected note                        |                                          |
|                   |   - will play from the cue if in keyboard is in play mode        |                                          |
|                   |                                                                  |                                          |
|                   | - While in beatloop roll mode:                                   |                                          |
|                   |                                                                  |                                          |
|                   | - Will activate a beatloop roll of 1/16, 1/8, 1/4 , 1/2, 1,      |                                          |
|                   |   2, 4 and 8 beats, or custom size if you have changed           |                                          |
|                   |   `BeatLoopRolls` in :ref:`settings`                             |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| FX 1st knob       | - Master volume/mix of the unit                                  |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| FX 2nd knob       | - Meta parameter of the first selected effect                    |                                          |
|                   | - First parameter of the focused effect in effect focus mode     |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| FX 3rd knob       | - Meta parameter of the second selected effect                   |                                          |
|                   | - Second parameter of the focused effect in effect focus mode    |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| FX 4th knob       | - Meta parameter of the third selected effect                    |                                          |
|                   | - Third parameter of the focused effect in effect focus mode     |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| FX 1st button     | - Trigger all effects                                            | - On if all effects are off and not      |
|                   | - Assign/de-assign effect to master while pressing               |   pressing :hwlabel:`SHIFT`              |
|                   |   :hwlabel:`SHIFT` and no focused effect                         | - On when effect is attached to master   |
|                   | - Exit focused mode while pressing :hwlabel:`SHIFT` and          |   and pressing :hwlabel:`SHIFT`          |
|                   |   focused effect                                                 | - Blinking in effect focused mode        |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| FX 2nd button     | - Toggle (short press) or trigger (long press) third effect      | - On if effect is active and no focused  |
|                   |   if not focused effect or if pressing :hwlabel:`SHIFT`          |   effect or if pressing :hwlabel:`SHIFT` |
|                   | - Toggle first arg (short press) or trigger first arg            | - On if focused effect parameter is      |
|                   |   (long press) of the focus effect if any                        |   enable                                 |
|                   | - Switch to next effect available if no focus effect and         |                                          |
|                   |   :hwlabel:`SHIFT`                                               |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| FX 3rd button     | - Toggle (short press) or trigger (long press) third effect      | - On if effect is active and no focused  |
|                   |   if not focused effect or if pressing :hwlabel:`SHIFT`          |   effect or if pressing :hwlabel:`SHIFT` |
|                   | - Toggle second arg (short press) or trigger second arg          | - On if focused effect parameter is      |
|                   |   (long press) of the focus effect if any                        |   enable                                 |
|                   | - Switch to next effect available if no focus effect and         |                                          |
|                   |   :hwlabel:`SHIFT`                                               |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| FX 4th button     | - Toggle (short press) or trigger (long press) third effect      | - On if effect is active and no focused  |
|                   |   if not focused effect or if pressing :hwlabel:`SHIFT`          |   effect or if pressing :hwlabel:`SHIFT` |
|                   | - Toggle (short press) or trigger (long press) third arg         | - On if focused effect parameter is      |
|                   |   on the focus effect if any                                     |   enable                                 |
|                   | - Switch to next effect available if no focus effect and         |                                          |
|                   |   :hwlabel:`SHIFT`                                               |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Library knob      | - Move up/down in tracklist                                      |                                          |
|                   | - :hwlabel:`SHIFT`: Move up/down in tree structure               |                                          |
|                   | - Move up/down in the context menu if playlist button is pressed |                                          |
|                   | - Zoom in/out the waveform when in grid move mode                |                                          |
|                   | - Beatjump by 16 beats backward/forward if a track is being      |                                          |
|                   |   previewed using the button                                     |                                          |
|                   | - Star down/up the currently playing track while pressing the    |                                          |
|                   |   star button                                                    |                                          |
|                   | - Sort by next/previous column while pressing the view button    |                                          |
|                   | - Expand the context-manu item when pressed while pressing the   |                                          |
|                   |   playlist button                                                |                                          |
|                   | - Load track when pressed or expand/collapse tree node when      |                                          |
|                   |   shifted (if view button is not pressed)                        |                                          |
|                   | - Inverse the column sorting if view button is pressed           |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Preview button    | Previews the currently selected track while pressed              |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Star button       | Change the selected track color on short press (next color, or   |                                          |
|                   | previous if shifted)                                             |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Playlist button   | Open or close a context menu for the currently selected track    | On if there is a context-menu open, off  |
|                   |                                                                  | otherwise                                |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Mixer FX button   | Toggle third effect (short press) or trigger third effect        | - Dim on if the effect is active         |
|                   | (long press) or assign the quick effect                          |                                          |
|                   | of FX select buttons are pressed                                 |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| FX Select         | Apply effect to all deck on release, if no mixer FX button have  |                                          |
| button            | been pressed                                                     |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Ext               | Apply the current gain as default. This will reset the gain knob.|                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Master            | If enabled in the :ref:`settings`, change the main gain          |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Booth             | If enabled in the :ref:`settings`, change the booth gain         |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Cue               | If enabled in the :ref:`settings`, adjust the headphone mix      |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+
| Headphone volume  | If using Mixxx internal mixer, change the headphone gain         |                                          |
+-------------------+------------------------------------------------------------------+------------------------------------------+


Looping
^^^^^^^

================================================================ ==============================================================================
Control                                                          Description
================================================================ ==============================================================================
Right Encoder (turn)                                             Double/halve loop size.
Right Encoder (press)                                            Activate/exit loop of set size from current position
:hwlabel:`SHIFT` + :hwlabel:`REV` (while no loops are enabled)   Set the loop in point. This will reset the loop out point as well.
:hwlabel:`SHIFT` + :hwlabel:`REV` (while a loop is enabled)      Toggle the loop in jog wheel mode. See :ref:`jog-wheel-modes` for more details.
:hwlabel:`SHIFT` + :hwlabel:`FLX` (while no loops are enabled)   Set the loop out point.
:hwlabel:`SHIFT` + :hwlabel:`FLX` (while a loop is enabled)      Toggle the loop out jog wheel mode. See :ref:`jog-wheel-modes` for more details.
================================================================ ==============================================================================

.. _settings:

Mapping options
---------------

Settings can be edited in the preference windows, under :guilabel:`Preferences` > :guilabel:`Controllers` > :guilabel:`Traktor Kontrol S4 MK3 ...`.

There are various options that can be used to change some behavior:

============================================================================================== =========================================== ================================================================================================================= ===================================================================================== ================================================================================================================================================================================================================
Setting                                                                                        Variable value                              Default                                                                                                           Range                                                                                 Description
============================================================================================== =========================================== ================================================================================================================= ===================================================================================== ================================================================================================================================================================================================================
Deck colors                                                                                    `DeckColors`                                LEDColors.red,LEDColors.blue,LEDColors.yellow, LEDColors.purple                                                   **All colors as defined in _LedColors_. Must be four color, separated by a comma**    Define the leading colors for each decks. Note that some buttons have only one color
Tempo fader center range                                                                       `tempoCenterRangeMm`                        1.0                                                                                                               0.3..5.0                                                                              Defines the center range in mm where the rate snaps to 0.
Tempo fader center offset                                                                      `tempoCenterOffsetMm`                       0.0                                                                                                               -3.0..3.0                                                                             Shifts the center range in case it doesn't match the center marker.
Sortable column in the library                                                                 `LibrarySortableColumns`                    LibraryColumns.Artist, LibraryColumns.Title, LibraryColumns.BPM, LibraryColumns.Key, LibraryColumns.DatetimeAdded **All values defined in** `the Mixxx control documentation`_ **separated by a comma** Define the list of columns on which it possible to sort the library using the library encoder and the view button
Loop In/Out jogwheel sensitivity                                                               `LoopWheelMoveFactor`                       50                                                                                                                -500..500 (Recommended)                                                               Define the sensitivity when moving the loop start or end point using the loop jogwheel mode. Negative value will reverse the order
Loop encoder sensitivity                                                                       `LoopEncoderMoveFactor`                     500                                                                                                               -3000..3000 (Recommended)                                                             Define the sensitivity when moving the loop with the encoder when using the loop jogwheel mode. Negative value will reverse the order
Loop encoder sensitivity (Shifted)                                                             `LoopEncoderShiftMoveFactor`                2500                                                                                                              -5000..5000 (Recommended)                                                             Define the sensitivity when moving the loop with :hwlabel:`SHIFT` + the encoder when using the loop jogwheel mode. Negative value will reverse the order
Color of the tempo led when on low takeover                                                    `TempoFaderSoftTakeoverColorLow`            LEDColors.white                                                                                                   **All colors as defined on line 19**                                                  Define the color of tempo LED when the tempo fader is out of sync, and the actual value is less than on the controller
Color of the tempo led when on high takeover                                                   `TempoFaderSoftTakeoverColorHigh`           LEDColors.green                                                                                                   **All colors as defined on line 19**                                                  Define the color of tempo LED when the tempo fader is out of sync, and the actual value is more than on the controller
Keep transport and play button dimmed when off                                                 `InactiveLightsAlwaysBacklit`               true                                                                                                              true/false                                                                            Having this setting on will keep LED always dimmed, even when off, although they may not have a matching color with the deck's color
Keep the unselected deck button off rather than show its deck color                            `DeckSelectAlwaysBacklit`                   true                                                                                                              true/false                                                                            Having this setting on will keep the LED of the unselected deck dimmed instead of off.
Keylock on :hwlabel:`SHIFT` + :hwlabel:`MASTER` instead of :hwlabel:`SHIFT` + :hwlabel:`SYNC`  `UseKeylockOnMaster`                        false                                                                                                             true/false                                                                            Use :hwlabel:`SHIFT` + :hwlabel:`MASTER` to toggle the keylock instead of :hwlabel:`SHIFT` + :hwlabel:`SYNC`
Make the :hwlabel:`grid` button blink when over a detected beat                                `GridButtonBlinkOverBeat`                   false                                                                                                             true/false                                                                            Make the :hwlabel:`GRID` button blinking when the playback goes over a detected beat
Make the jogwheel ring blink when the track playing is near the end                            `WheelLedBlinkOnTrackEnd`                   true                                                                                                              true/false                                                                            The jogwheel LED ring will start blinking when a track is near the end. The end section can be defined in :menuselection:`Preferences --> Waveforms --> End of track warning`
Use the mixer to control input when using :hwlabel:`SHIFT`                                     `MixerControlsMixAuxOnShift`                false                                                                                                             true/false                                                                            Make the :hwlabel:`GRID` button blinking when the playback goes over a detected beat
Number of samples used for jogwheel speed                                                      `WheelSpeedSample`                          3                                                                                                                 1..50                                                                                 Number of samples used to determine the jogwheel movement. A higher value will increase precision but latency too, and vice-versa
Replace the sampler tab by a beatloop roll tab                                                 `UseBeatloopRollInsteadOfSampler`           false                                                                                                             true/false                                                                            Replace the sample tab as well of the sample feature with 8 beatloop roll
Define the predefined size to use for the beatloop tab                                         `BeatLoopRolls`                             1/16,1/8,1/4,1/2,1,2,4,8                                                                                          eight number in range 1/32..512                                                       Define the size of loops of each pad, from left to right, starting from the top row.
Use the two last tab as loop half/double buttons in the beatloop tab                           `AddLoopHalveAndDoubleOnBeatloopRollTab`    true                                                                                                              true/false                                                                            Use the last two pad from the bottom row as loop half and loop double. These can be used to interact with beatloop roll and normal loop.
Jogwheel speed (in turntable mode, as well as LED indicator)                                   `BaseRevolutionsPerMinute`                  33 + 1/3                                                                                                          33+1/3, 45 (Recommended)                                                              The turntable mode defines how fast the jogwheel turns (if on) as well as the LED, and the overall jogwheel sensitivity. It is recommended to keep either 33 + 1/3 or 45 as a value
Whether or not to use haptic feedback features                                                 `UseMotors`                                 false                                                                                                             true/false                                                                            Whether or not to use haptic feedback features. This is a beta feature, some of them may be unstable.
Map the mixer :hwlabel:`Master` knob to the Mixxx internal mixer                               `SoftwareMixerMain`                         false                                                                                                             true/false                                                                            When enabled, the Master knob will drive the Main gain of the Mixxx internal mixer as well as the hardware built-in mixer in the device.
Map the mixer :hwlabel:`Booth` knob to the Mixxx internal mixer                                `SoftwareMixerBooth`                        false                                                                                                             true/false                                                                            When enabled, the Booth knob will drive the Booth gain of the Mixxx internal mixer as well as the hardware built-in mixer in the device.
Map the mixer headphone knobs  :hwlabel:`VOL` and :hwlabel:`MIX` to the Mixxx internal mixer   `SoftwareMixerHeadphone`                    false                                                                                                             true/false                                                                            When enabled, the headphone knobs will drive the headphone controls of the Mixxx internal mixer as well as the hardware built-in mixer in the device.
Default Pad Layout                                                                             `DefaultPadLayout`                          default                                                                                                           default,hotcue,samplerBeatloop,keyboard                                               Define the default layout used for the pads.
============================================================================================== =========================================== ================================================================================================================= ===================================================================================== ================================================================================================================================================================================================================

.. _the Mixxx control documentation: https://manual.mixxx.org/latest/en/chapters/appendix/mixxx_controls.html#control-[Library]-sort_column

These settings are only useful if you are using haptic feedback features:

================================================================ =========================================== ============== ============================================== ==========================================================================================================================================================
Setting                                                          Variable value                              Default        Range                                          Description
================================================================ =========================================== ============== ============================================== ==========================================================================================================================================================
Number of samples used for jogwheel speed in turntable mode      `TurnTableSpeedSample`                      20             1..50                                          Number of samples used to determine the jogwheel movement when the turntable is on. A higher value will increase precision but latency too, and vice-versa
Define the tension of the jogwheel                               `TightnessFactor`                           0.5            0..1.0                                         Define the jogwheel tension. 0 makes it very tight while 1 makes it very loose
Define how much force can the jogwheel use                       `MaxWheelForce`                             25000          10000..30000 (Recommended, can go up to 60000) Define how much resistance can the wheel use when its rotation is held
================================================================ =========================================== ============== ============================================== ==========================================================================================================================================================
