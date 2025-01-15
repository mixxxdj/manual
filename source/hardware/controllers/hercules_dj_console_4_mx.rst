Hercules DJ Console 4-Mx
========================

The Hercules DJ Console 4-Mx is a USB controller with a built in sound card. It is very similar to the [[Hercules DJ Console RMX]], but with switches for 4 decks.

-  `Manufacturer's product page <https://support.hercules.com/en/product/djconsole4mx-en/>`__

.. versionadded:: 1.11

Audio
-----

The DJ Console 4-Mx is not a USB class compliant MIDI device, although it is a USB Audio device. Drivers for Mac OS X and Windows can be found on the `Hercules support
page <http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=62&pid=263&cid=1>`__.

.. warning::
   The controller will not work on Linux out of the box. You will need to use the `Linux usermode driver <https://github.com/mixxxdj/mixxx/wiki/Hercules-Linux-Usermode-Driver>`__.
   The device will only produce audio if the device hasn’t been configured for ASIO under windows previously. Also, check the volumes in alsamixer.

The sound card has 4 inputs and 4 outputs (2 stereo in/out). The inputs are switchable between line-in and phono, and also is possible to select different line levels (consumer -10dBV, Pro +4dBu and
boost +8dBu ), so you can connect both CD players and turntables on the inputs. \* Inputs are RCA. \* Outputs are RCA or 1/4" TRS balanced. \* Microphone input is 1/4" TS \* Headphone jack is 1/4"
(6.35 mm) TRS stereo

Hercules Tray Icon configuration
--------------------------------

The drivers for Windows and OS X install an application that can be used to configure the audio and controller settings. Most of the settings work well on the default setting.

-  **Volume/Pan/Mute**: Sets the volume output for channels 1-2 and channels 3-4. Note that the volume of the channels 3-4 refers to the line output from behind. In other words. It does not affect the
   volume of the headphones.
-  **Line in mode**: Sets the line level of the inputs. In case of line 1-2, it also allows to redirect the microphone to the line 1-2. Else, it is mixed in hardware to the main out.
-  **Talkover attenuation**: Sets how much to attenuate the main output when activating the hardware mixed microphone.
-  **Enable/Disable jog wheels**: Allows to disable the jog wheels, in case the user desires not to use them.
-  **Sensitivity**: Alters the sensitivity of the jog wheels. If you change this, change also the sensitivity option in the script, as described below.
-  **Audio Mode**: Enables the WDM drivers (non-asio) or the specific ASIO-only driver.
-  **MIDI pitch resolution**: Sets the resolution of the pitch sliders. Mixxx will work with any of the two settings, but it is recommended to set it to 14bit (8bit used) which doubles the precision
   versus 7bit.
-  **ASIO**: You can configure the samplerate, bit depth and latency for the ASIO driver.
-  **MIDI channel for controls**: *Keep these at 1-2 (Default) when you use it with Mixxx.*
-  **Crossfader settings**: Allows to configure how does the crossfader react. Mixxx also offers an alternate invert option in the crossfader settings.
-  **Headphone channels**: Allows to setup which input channels are sent to the headphone output.
-  **Channels 1-2 hardware mix**: Allows mixing the line in or the microphone directly in hardware to the speaker output.
-  **Deck mode**: *Leave this at 4 Decks (Default) if you want to use four decks with Mixxx. Else, you will only be able to use two decks.*

Options
-------

There are several options that can be configured for this mapping. You can edit these by opening the JavaScript file in a
text editor like Notepad, TextEdit, or gEdit and editing the values at the top of the file.

-  **autoHeadMix**: Indicates if the headphone/main mix should automatically be set to main when none of the headphone cue buttons are activated.
-  **autoHeadcueOnLoad**: Automatically enable the headphone cue select (PFL) of the deck when a song is loaded. (Like in virtual-dj)
-  **beatFlashLed**: set which LED, if any, blinks with the beat
-  **useVuMeters**: Simulate vuMeters using the kill and source buttons’ LEDs. If enabled, shows main VUs, or deck VU depending if prefader listen button is enabled or not.
-  **naviScrollSpeed**: KeyRepeat speed for navigating up/down, in milliseconds. 100 is a good value. Lower values make it scroll faster.
-  **crossfaderScratchCurve**: The controller has two modes to report the crossfader position. The default/beatmix curve, and the scratch curve. The default curve reports the real position of the
   control. The scratch curve just crossfades on the edges. Setting this setting to true, the curve will change to scratch curve when the scratch mode is on (scratch button). Setting it to false will
   not change it, so it will use the setting configured in the DJHercules Tray-icon configuration.
-  **vinylSpeed**: Playback speed of the virtual vinyl that is being scratched. 45.00 and 33.33 are the common speeds. (Lower number equals faster scratch)
-  **sensitivity**: Jog wheel sensitivity. You should configure this setting to the same value than in the DJHercules tray icon configuration. (Normal means 1/1). If crossfaderScratchCurve is true, or
   the setting is changed while Mixxx is active, this value will be detected automatically.
-  **alpha**: alpha value for the scratch filter (start with 1/8 (0.125) and tune from there)
-  **beta**: beta value for the scratch filter (start with alpha/32 and tune from there)
-  **FXbuttonsSetup**: This indicates which mapping for the FX buttons should Mixxx use. The possible values are: mixxx21, mixxx20, and original (Hercules Manual and the default setup in Virtual DJ 7
   LE)

Main / Global controls
------------------------

+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Control                                                                                                | Mode                             | Function                                                |
+========================================================================================================+==================================+=========================================================+
| Cross-Fader                                                                                            |                                  | Fades between left and right decks                      |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Vol. Main                                                                                              |                                  | Controls the main volume knob of Mixxx.                 |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Scratch                                                                                                |                                  | Toggles scratch mode. When scratch mode is enabled,     |
|                                                                                                        |                                  | pressing a jog wheel controls scratching                |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Auto                                                                                                   |                                  | Enable AutoDJ. Stop decks 1 and 2 to disable it using   |
|                                                                                                        |                                  | the controller.                                         |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Auto                                                                                                   | AutoDJ on                        | Fade to next song.                                      |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Folders / Files                                                                                        |                                  | Switches between browsing the sidebar in the library,   |
|                                                                                                        |                                  | or the list. If Folders is pressed twice, opens/closes  |
|                                                                                                        |                                  | the tree branch                                         |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Files                                                                                                  | AutoDJ on                        | The next song in the Auto DJ cue is skipped             |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Up / Down                                                                                              |                                  | Moves up and down in the library track list. If held    |
|                                                                                                        |                                  | down and any of the jog wheels is moved, then the jog   |
|                                                                                                        |                                  | wheel takes over the cursor movement until the up/down  |
|                                                                                                        |                                  | button is released                                      |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Cue/Mix                                                                                                |                                  | Control mix of main and PFL (cue) output in             |
|                                                                                                        |                                  | headphones                                              |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+
| Mic On/Off                                                                                             |                                  | Enables or disables the microphone. The microphone is   |
|                                                                                                        |                                  | always mixed in hardware. The trayicon driver           |
|                                                                                                        |                                  | configuration allows to choose between direct mixing,   |
|                                                                                                        |                                  | or mix it only when enabled with the button. It no      |
|                                                                                                        |                                  | longer tries to activate Mixxx microphone talkover.     |
+--------------------------------------------------------------------------------------------------------+----------------------------------+---------------------------------------------------------+

Note: The Microphone volume and the Headphone volume controls are hardware controls (i.e. they don’t control Mixxx’s interface)

Deck / Channel specific controls
--------------------------------

+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Control   | Mode           | Function                                                                                                                                                                |
+===========+================+=========================================================================================================================================================================+
| Shift key |                | When this button is pressed and released, it toggles between keypad functions 1-6 to keypad functions 7-12. When keypad functions 7-12 are active, the shift button is  |
|           |                | lit orange.                                                                                                                                                             |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Shift key |                | When this button is pressed and released, it toggles between keypad functions 1-6 to k Hold it                                                                          |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P         |                | Play track if it is not playing; pause it if track is playing                                                                                                           |
| lay/Pause |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P         | Shift          | Play backwards. If slip mode is enabled (triangle image in Deere skin), it will resume beyond the previous position (i.e. the playback continues muted until the button |
| lay/Pause |                | is released)                                                                                                                                                            |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Stop      |                | Moves the cursor to the beginning, or to the cue point if it is set, and stops playing it, if it was playing.                                                           |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Stop      | Shift          | Brake (Slow it down progressively). Releasing it will continue playing, except if it has slowed a lot, in which case it stops.                                          |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cue       |                | Depends on the cue mode set in Mixxx preferences                                                                                                                        |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Jog wheel |                | Seeks forwards and backwards in a stopped track Temporarily changes the playback speed for playing tracks                                                               |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Jog wheel | Scratch on and | If Scratch is on and the jog is pressed, moving it will do a scratch effect                                                                                             |
|           | jog pressed    |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Jog wheel | Up/Down        | Moves up / down in the tracklist if either Up or Down are held down                                                                                                     |
|           | pressed        |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Jog wheel | LED            | If the beatflash led has been set to jogwheel in the JavaScript file, the light of this button will be flashing following the beats of the song.                        |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Forward / |                | Seeks at high speed.                                                                                                                                                    |
| Backward  |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Forward / |                | Seeks forward or backward in the track in steps of 4 beats (when the beatgrid has already been detected).                                                               |
| Backward  |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Forward / | Pressed for    | seeks at high speed.                                                                                                                                                    |
| Backward  | 500ms          |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Forward / | Shift          | Seeks forward or backward in the track in steps of 1 beats                                                                                                              |
| Backward  |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sync      |                | Automatically sets the pitch fader speed to match the BPM of the other deck.                                                                                            |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sync      | LED            | If the beatflash led has been set to Sync in the JavaScript file, the light of this button will be flashing following the beats of the song.                            |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sync      | Pressed for    | Activates sync lock for this deck.                                                                                                                                      |
|           | 500ms          |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sync      | Shift          | Activates the beatgrid edit mode                                                                                                                                        |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sync      | Beatgrid edit  | When the track is stopped, aligns the beatgrid with the current playback position. If playing, synchronizes the beatgrid to align with that of the other playing track. |
|           | mode           |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     |                | Adjusts playback speed (range and direction can be adjusted in Mixxx preferences)                                                                                       |
| fader     |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     |                | Adjusts playback speed temporarily (range can be adjusted in Mixxx preferences)                                                                                         |
| bend +/-  |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     | Beatgrid edit  | Increases or decreases the BPM of the track (the detected one).                                                                                                         |
| bend +/-  | mode           |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     | Shift          | Adjust playback speed permanently (range can be adjusted in Mixxx preferences)                                                                                          |
| bend +/-  |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     |                | These controls have a different meaning in Mixxx: They have been mapped to change the musical key                                                                       |
| Scale +/- |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     | Beatgrid edit  | Move the beatgrid to the left or to the right                                                                                                                           |
| Scale +/- | mode           |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     | Shift          | Activates or deactivates the (musical) keylock mode                                                                                                                     |
| Scale -   |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     | Shift          | Activates or deactivates the quantize (to beat) mode                                                                                                                    |
| Scale +   |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     |                | This is triggered when both pitch scale buttons are pressed at the same time. This control has a different meaning in Mixxx: It resets the musical key to the track’s   |
| Reset     |                | default.                                                                                                                                                                |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pitch     | LED            | This led has a different meaning in Mixxx: If the beatflash led has been set to pitchreset in the JavaScript file, the light of this button will be flashing following  |
| Reset     |                | the beats of the song. Else, the led is on if the key lock button is enabled for this deck.                                                                             |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Deck A/C, |                | Switches the deck to control between Deck A/C or between Deck B/D. Lights are changed accordingly                                                                       |
| B/D       |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Vol. Deck |                | Controls a deck’s output volume                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cue       |                | Toggles on and off this deck’s output to the monitor/prefader listen (headphones) By default, it is configured in the JavaScript to activate it automatically when a    |
| Select    |                | new track is loaded in the deck.                                                                                                                                        |
| Deck      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cue       | Shift          | Set this deck to control the “Preview Deck”. Press it again to leave this mode What works: Load track, stop, cue, play, forward, rewind, jog wheel, Gain and some Fx    |
| Select    |                | buttons, like hotcues. The preview deck is not a fully featured deck, so no pitch, sync, EQ or audio Fx.                                                                |
| Deck      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cue       | LED            | The led is active when the monitoring with headphones is active. The button led will flash if the “preview deck” mode is active.                                        |
| Select    |                |                                                                                                                                                                         |
| Deck      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|           | Load On        |                                                                                                                                                                         |
|           | Left/Right     |                                                                                                                                                                         |
|           | Deck           |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bass knob |                | EQ low frequencies                                                                                                                                                      |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Medium    |                | EQ mid frequencies                                                                                                                                                      |
| knob      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Treble    |                | EQ high frequencies                                                                                                                                                     |
| knob      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Gain      |                | Controls a deck’s gain before the volume fader                                                                                                                          |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Kill      |                | Toggles that frequency band completely off                                                                                                                              |
| (Bass/    |                |                                                                                                                                                                         |
| Medium/   |                |                                                                                                                                                                         |
| Treble)   |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Kill      | LED            | If the useVuMeters option is activated in the JavaScript file, these LEDs will simulate a VU meter of the main or the deck (if prefader-listen is on). They will        |
| (Bass/    |                | flicker if the sound clips. If EQ kill is enabled, the vumeter is temporarily disabled                                                                                  |
| Medium/   |                |                                                                                                                                                                         |
| Treble)   |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Source    |                | Toggles the deck to use the input channel 1/2 as its audio source instead of Mixxx’s deck. Concretely, it activates vinyl passthrough mode.                             |
| 1/2       |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Source    | LED            | If the vumeter is activated in the JavaScript file, they will show a vumeter of the main or the deck (if prefader-listen is on). If kill is enabled, the vumeter is     |
| 1/2       |                | temporarily disabled                                                                                                                                                    |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 1  |                | Set/Unset a beatloop of 0.5, 1, 2 or 4 beats. They act like the corresponding buttons in Mixxx. When a loop is set that isn’t one of these four main cases, buttons 3   |
| to 4      |                | and 4 will light to indicate a loop is present                                                                                                                          |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 1  | Shift          | Set/Unset a beatloop. buttons 1 and 2 use a beatloop size of 0.125 and 0.25, and buttons 3 and 4 act as loop end/reloop button.                                         |
| to 4      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 5  |                | Reveses playback direction when held down. keypad 6 does it with audio roll (censor-like)                                                                               |
| to 6      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 7  |                | Set/Unset the hotcues 1 to 4                                                                                                                                            |
| to 10     |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 7  | Shift          | The corresponding hotcue is cleared                                                                                                                                     |
| to 10     |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 11 |                | Enables the effect rack 1 and 2 for this specific deck                                                                                                                  |
| to 12     |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 1  |                | Sets the loop begin and Activates the loop edit mode                                                                                                                    |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 1  | Shift          | Same as click, but it will be a rolling loop (slip mode)                                                                                                                |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 1  | Loop edit mode | Exits the loop edit mode                                                                                                                                                |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 1  | Loop active    | Disable the loop                                                                                                                                                        |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 1  | LED            | The led is on if the loop is active                                                                                                                                     |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 2  |                | Reloop (Enable or disable the previously existing loop)                                                                                                                 |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 2  | Loop edit mode | Sets the loopend and exits the loop edit mode                                                                                                                           |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 2  | LED            | The led is on if a loop exists                                                                                                                                          |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 3  |                | Sets a loop of 4 or 16 beats.                                                                                                                                           |
| to 4      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 3  | Shift          | Same as click, but it will be a rolling loop (slip mode)                                                                                                                |
| to 4      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 3  | LED            | If a beatloop of 1 or 4 beats is enabled.                                                                                                                               |
| to 4      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 5  |                | starts or stops a sampler 1 or 2 (buttons on the left deck), or the sampler 3 or 4 (buttons on the right deck)                                                          |
| to 6      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 3  | Loop edit mode | Sets a beatloop of 2, 8, 16 or 32 beats                                                                                                                                 |
| to 6      |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 7  |                | Set/Unset the hotcues 1 to 4                                                                                                                                            |
| to 10     |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 7  | Shift          | The corresponding hotcue is cleared                                                                                                                                     |
| to 10     |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keypad 11 |                | Enables the effect rack 1 or 2 for this specific deck                                                                                                                   |
| to 12     |                |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fx knob   |                | Filter knob (the Quick Effect set in the equalizer preferences)                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fx knob   | Shift          | Move the filter knob slowly (the Quick Effect set in the equalizer preferences)                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fx knob   | Beatgrid edit  | Move the beatgrid position                                                                                                                                              |
|           | mode           |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fx knob   | Loop edit mode | Increase or decrease the loop size                                                                                                                                      |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fx knob   | audio effect   | If a keypad number is mapped to an audio effect, holding such button and moving the knob changes the “super” knob of that effect                                        |
|           | pressed        |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fx knob   | pitch Scale    | Increases or decreases the musical key (it doesn’t matter which of the pitch scale numbers is pressed)                                                                  |
|           | +/- pressed    |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fx knob   | Loop edit mode | Move the loop forward or backward in steps of one beat                                                                                                                  |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Fx knob   | keypad 1 held  | Increase or decrease the loop size                                                                                                                                      |
|           | down           |                                                                                                                                                                         |
+-----------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note: The actions of the Keypad buttons can be changed from the JavaScript. There are three preconfigured presets corresponding to Manual/Virtual DJ LE, Mixxx 2.0 and Mixxx 2.1.
