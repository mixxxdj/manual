# Hercules DJ Control MP3 e2 / MP3 LE / Glow

MP3 e2

[[/media/16445_.jpg|16445\_.jpg]]

MP3 LE

[[/media/hardware/hercules-dj-control-mp3-le.jpeg|hercules-dj-control-mp3-le.jpeg]]

Glow

[[/media/hardware/hercules-dj-control-glow.jpeg|hercules-dj-control-glow.jpeg]]

The Hercules DJ Control MP3 e2, MP3 LE, and Glow are USB controllers
that have identical controls and share the same mapping. These
controllers do not have a built in sound card, so a [splitter
cable](hardware%20compatibility#splitter%20cables) or [separate sound
card](hardware%20compatibility#USB%20sound%20cards) is recommended for
use with it. They are not class compliant MIDI devices. [Older versions
of Mixxx](Hercules%20DJ%20Control%20MP3%20e2%20old) required using
[Hercules' MIDI driver](hercules_linux_kernel_module), but this driver
can be a hassle to set up and maintain on Linux, so it is recommended
only for Windows and Mac OS X. Another alternative is to use the [user
mode driver](hercules_linux_usermode_driver), or also upgrade to the
[latest version of Mixxx](http://mixxx.org/download) if you have not
already. Support for using the MP3 LE and Glow as USB Bulk controllers
without the driver on Linux is available in development versions of
Mixxx and will be included in Mixxx 2.1, but the MP3 e2 was already
supported in Mixxx 2.0.

The mapping is included in Mixxx and allows you to manipulate 4 decks, 2
at a time, switching Deck A (left) between Channel 1 and 3 and Deck B
(right) between Channel 2 and 4.

## Mapping description (by function)

#### Shift / Supershift

[[/media/hercules-mp3e2-schema-shift.jpg|]]

<table>
<thead>
<tr class="header">
<th>Function</th>
<th>Control</th>
<th>number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Shift button to obtain more controls than those provided by Hercules.<br />
Press &amp; Hold automix, then press corresponding button to obtain shifted behavior.</td>
<td>Automix</td>
<td>9</td>
</tr>
<tr class="even">
<td>Supershift button to obtain a third level of controls.<br />
Press &amp; Hold Automix, then press &amp; Hold Scratch, then press corresponding button to obtain supershifted behavior.</td>
<td>Shift-Scratch</td>
<td>7</td>
</tr>
<tr class="odd">
<td>Switch deck A (left) between Channel1 and Channel3 (also apply to Sampler1 and Sampler3)</td>
<td>Supershift + Load A</td>
<td>18</td>
</tr>
<tr class="even">
<td>Switch deck B (right) between Channel2 and Channel4 (also apply to Sampler2 and Sampler4)</td>
<td>Supershift + Load B</td>
<td>18</td>
</tr>
</tbody>
</table>

#### Library

[[/media/hercules-mp3e2-schema-library.jpg|]]

| Function                                                                    | Control                       | number |
| --------------------------------------------------------------------------- | ----------------------------- | ------ |
| Select prev/next playlist                                                   | Supershift + Deck A Jog Wheel | 16     |
| Toggles (expands/collapses) the currently selected library sidebar item     | Folder                        | 6      |
| Go one track down                                                           | Up arrow                      | 8      |
| Go one track up                                                             | Shift + Up arrow              | 8      |
| Select prev/next track                                                      | Supershift + Deck B Jog Wheel | 16     |
| Loads the currently highlighted track into the corresponding deck (A or B)  | Load A/B                      | 18     |
| Loads the current highlighted track into the corresponding sampler (1 or 2) | Shift + Load A/B              | 18     |

#### Master/Headphones/Microphone

[[/media/hercules-mp3e2-schema-masterheadmicro.jpg|]]

| Function                                                          | Control                   | number |
| ----------------------------------------------------------------- | ------------------------- | ------ |
| Microphone TalkOver                                               | Down Arrow                | 8      |
| Fades between left (channel 1 & 3) and right (channel 2 & 4) deck | Crossfader                | 19     |
| Headphone volume                                                  | Shift + Deck A pitch knob | 3      |
| Adjust the cue/main mix in the headphone output                   | Shift + Deck B pitch knob | 3      |
| Toggles deck output to the headphones monitor on/off              | Headphone monitor         | 20     |

#### Sampler

[[/media/hercules-mp3e2-schema-sampler.jpg|]]

| Function                                                                    | Control             | number |
| --------------------------------------------------------------------------- | ------------------- | ------ |
| Loads the current highlighted track into the corresponding sampler (1 or 2) | Shift + Load A/B    | 18     |
| Goto start & Play sampler 1/3                                               | Shift + Folder      | 6      |
| Stop sampler 1/3                                                            | Supershift + Folder | 6      |
| Goto start & Play sampler 2/4                                               | Shift + Files       | 10     |
| Stop sampler 2/4                                                            | Supershift + Files  | 10     |

#### Decks / Channels

##### Playing

[[/media/hercules-mp3e2-schema-deck-playing.jpg|]]

<table>
<thead>
<tr class="header">
<th>Function</th>
<th>Control</th>
<th>number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Loads the currently highlighted track into the corresponding deck (A or B)</td>
<td>Load A/B</td>
<td>18</td>
</tr>
<tr class="even">
<td>Starts or stop a loaded track</td>
<td>Play</td>
<td>14</td>
</tr>
<tr class="odd">
<td>Backward Play</td>
<td>Shift + Play</td>
<td>14</td>
</tr>
<tr class="even">
<td>Toggle Repeat</td>
<td>Supershift + Play</td>
<td>14</td>
</tr>
<tr class="odd">
<td>Sets the cue point if a track is stopped and not at the current cue point.<br />
Stops track and returns to the current cue point if a track is playing.<br />
Plays preview if a track is stopped at the cue point for as long as it's held down</td>
<td>Cue</td>
<td>15</td>
</tr>
<tr class="even">
<td>Move Forward/Backward in track</td>
<td>Forward / Backward</td>
<td>12</td>
</tr>
<tr class="odd">
<td>Enable or disable the scratch mode on all four decks</td>
<td>Scratch</td>
<td>7</td>
</tr>
<tr class="even">
<td>Seeks forwards and backwards in a stopped track.<br />
Temporarily changes the playback speed for playing tracks.<br />
Absolute sync of the track speed to the jog wheel if scratch mode enabled</td>
<td>Jog wheel</td>
<td>16</td>
</tr>
</tbody>
</table>

##### Volume / Equalizer / Effects

[[/media/hercules-mp3e2-schema-deck-voleffects.jpg|]]

| Function                                                                    | Control                                  | number |
| --------------------------------------------------------------------------- | ---------------------------------------- | ------ |
| Controls the deck output volume, with soft takeover on deck switch.         | Deck volume slider                       | 17     |
| Adjusts the gain of the low/medium/high equalizer filter. No soft takeover. | Equalizer knobs                          | 5      |
| Filter Low Kill                                                             | Supershift + Pitchbend -                 | 1      |
| Filter Mid Kill                                                             | Supershift + Sync                        | 13     |
| Filter High Kill                                                            | Supershift + Pitchbend +                 | 1      |
| Adjust pregain                                                              | Shift + Forward / Backward               | 12     |
| Quick Filter knob                                                           | Supershift + Pitch knobs                 | 3      |
| Brake Effect                                                                | Supershift + Forward (stops on release)  | 12     |
| Spinback Effect                                                             | Supershift + Backward (stops on release) | 12     |

##### Hotcues

[[/media/hercules-mp3e2-schema-hotcues.jpg|]]

*Need to be in Hotcue mode (button Loop/Fx (4) lit up). If not, press
Loop/Fx button to switch to hotcue mode.*

| Function                                                                                                                         | Control                 | number |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------ |
| If hotcue X is set, seeks the player to hotcue X's position. If hotcue X is not set, sets hotcue X to the current play position. | 1/2/3/4 buttons         | 11     |
| If hotcue X is set, clears its hotcue status.                                                                                    | Shift + 1/2/3/4 buttons | 11     |

  
  
  
  
\==Loops == [[/media/hercules-mp3e2-schema-loops.jpg|]]

*Need to be in Loop mode (button Loop/Fx (4) turned off). If not, press
Loop/Fx button to switch to Loop mode.*

| Function                       | Control               | number |
| ------------------------------ | --------------------- | ------ |
| loop-in                        | Button 1              | 11     |
| loop-out                       | Button 2              | 11     |
| Toggles current loop On or Off | Button 3              | 11     |
| Clear Loop                     | Supershift + Button 1 | 11     |
| loop 1/8                       | Supershift + Button 2 | 11     |
| loop 1/4                       | Shift + Button 1      | 11     |
| loop 1/2                       | Shift + Button 2      | 11     |
| loop 1                         | Shift + Button 3      | 11     |
| loop 2                         | Shift + Button 4      | 11     |
| loop 4                         | Button 4              | 11     |
| loop 8                         | Supershift + Button 3 | 11     |
| loop 16                        | Supershift + Button 4 | 11     |
| Double loop                    | Shift + Pitchbend +   | 1      |
| Half loop                      | Shift + Pitchbend -   | 1      |

##### Pitch / Syncing

[[/media/hercules-mp3e2-schema-pitchsync.jpg|]]

<table>
<thead>
<tr class="header">
<th>Function</th>
<th>Control</th>
<th>number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Temporary Holds the pitch 4% higher while pressed</td>
<td>Pitchbend +/-</td>
<td>1</td>
</tr>
<tr class="even">
<td>Set deck as master clock.<br />
Led blink: master<br />
Fixed led: Follower<br />
Led off: none</td>
<td>Master tempo (MP3 e2) / Pitch reset (MP3 LE &amp; Glow)</td>
<td>2</td>
</tr>
<tr class="odd">
<td>Adjust playback pitch / speed</td>
<td>Pitch knobs</td>
<td>3</td>
</tr>
<tr class="even">
<td>Automatically sets pitch so the BPM of the other deck is matched</td>
<td>Sync</td>
<td>13</td>
</tr>
<tr class="odd">
<td>Enable key-lock for the specified deck (rate changes only affect tempo, not key)</td>
<td>Shift + Master tempo</td>
<td>2</td>
</tr>
<tr class="even">
<td>Magnet (all cues, hotcues, loops, and beatloops will be automatically quantized so that they begin on a beat.)</td>
<td>Supershift + Master tempo</td>
<td>2</td>
</tr>
<tr class="odd">
<td>Adjust beatgrid</td>
<td>Shift + Sync</td>
<td>13</td>
</tr>
<tr class="even">
<td>Enable or disable the scratch mode on all four decks</td>
<td>scratch</td>
<td>7</td>
</tr>
<tr class="odd">
<td>Seeks forwards and backwards in a stopped track.<br />
Temporarily changes the playback speed for playing tracks.<br />
Absolute sync of the track speed to the jog wheel if scratch mode enabled</td>
<td>Jog wheel</td>
<td>16</td>
</tr>
</tbody>
</table>

## Mapping description (by knob/button)

[[/media/hercules_mappa.png|]]

#### Global controls

<table>
<thead>
<tr class="header">
<th>Number</th>
<th>Control</th>
<th>Function</th>
<th>shifted</th>
<th>Supershifted</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8</td>
<td>Arrow up/down</td>
<td>Up : goes one track down<br />
Down : Microphone TalkOver</td>
<td>Up : Goes one track up<br />
Down : Nothing</td>
<td>Nothing</td>
</tr>
<tr class="even">
<td>6</td>
<td>Folder</td>
<td>Toggles (expands/collapses) the currently selected library sidebar item</td>
<td>Play/Stutter sampler 1/3</td>
<td>Stop sampler 1/3</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Files</td>
<td>Toggles (expands/collapses) the currently selected library sidebar item</td>
<td>Play/Stutter sampler 2/4</td>
<td>Stop sampler 2/4</td>
</tr>
<tr class="even">
<td>18</td>
<td>Load A/B</td>
<td>Loads the currently highlighted track into the corresponding deck (A or B)</td>
<td>Loads the current highlighted track into the corresponding sampler (1 or 2)</td>
<td>Switch deckA between Channel 1 &amp; 3 and deckB between 2 &amp;4</td>
</tr>
<tr class="odd">
<td>19</td>
<td>Crossfader</td>
<td>Fades between left (channel 1 &amp; 3) and right (channel 2 &amp; 4) deck</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>9</td>
<td>Automix</td>
<td>Used as a master shift button to obtain more controls than those provided by Hercules. Press &amp; Hold automix, then press corresponding button to obtain shifted behavior.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Scratch</td>
<td>Enable or disable the scratch mode on both decks</td>
<td>Used as a master supershift button to obtain a third level of controls. Press &amp; Hold Automix, then press &amp; Hold Scratch, then press corresponding button to obtain supershifted behavior</td>
<td></td>
</tr>
</tbody>
</table>

#### Deck / Channel specific controls

<table>
<thead>
<tr class="header">
<th>Number</th>
<th>Control</th>
<th>Simple function</th>
<th>Shifted function</th>
<th>Supershifted function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Pitchbend +/-</td>
<td>Temporary Holds the pitch 4% higher while pressed</td>
<td>+ double loop<br />
- half loop</td>
<td>+ Filter High Kill<br />
- Filter Low Kill</td>
</tr>
<tr class="even">
<td>2</td>
<td>Master Tempo</td>
<td>Syncs the BPM and phase to that of the other track (if BPM is detected on both).<br />
Led blink: master<br />
Fixed led: follower<br />
Led off: none</td>
<td>Enable key-lock for the specified deck (rate changes only affect tempo, not key)</td>
<td>Quantize (Magnet)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Pitch knobs</td>
<td>Adjusts playback pitch/speed</td>
<td>Deck A: adjust the headphone volume<br />
Deck B: adjust the cue/main mix in the headphone output</td>
<td>Quick Filter knob</td>
</tr>
<tr class="even">
<td>4</td>
<td>Loop/Fx</td>
<td>Toggle the Loop/Hotcue mode for the keys buttons.<br />
When the button is not lit up the loop buttons are enabled, when the button is lit up the hotcue's buttons are enabled</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Equalizer knobs</td>
<td>Adjusts the gain of the low/medium/high equalizer filter</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>1/2/3/4 buttons</td>
<td>Loop mode:<br />
1 - loop-in<br />
2 - loop-out<br />
3 - Toggles current loop On or Off<br />
4 - Loop 4<br />
<br />
Hotcue mode:<br />
1, 2, 3 and 4: If hotcue X is set, seeks the player to hotcue X's position. If hotcue X is not set, sets hotcue X to the current play position.</td>
<td>Loop mode:<br />
1 - Loop 1/4<br />
2 - Loop 1/2<br />
3 - Loop 1<br />
4 - Loop 2<br />
<br />
Hotcue mode:<br />
If hotcue X is set, clears its hotcue status.</td>
<td>Loop mode:<br />
1 - Clear loop<br />
2 - Loop 1/8<br />
3 - Loop 8<br />
4 - Loop 16<br />
<br />
Hotcue mode:<br />
Nothing</td>
</tr>
<tr class="odd">
<td>12</td>
<td>Forward \ Backward</td>
<td>Fast forward/backward</td>
<td>Adjust pregain</td>
<td>Forward: brake effect (stay pushed)<br />
Backward: spinback effect (stay pushed)</td>
</tr>
<tr class="even">
<td>13</td>
<td>Sync</td>
<td>Automatically sets pitch so the BPM of the other deck is matched</td>
<td>Adjust BeatGrid</td>
<td>Kill Mid</td>
</tr>
<tr class="odd">
<td>14</td>
<td>Play</td>
<td>Starts or stop a loaded track</td>
<td>Backward Play</td>
<td>Repeat</td>
</tr>
<tr class="even">
<td>15</td>
<td>Cue</td>
<td>Sets the cue point if a track is stoped and not at the current cue point<br />
Stops track and returns to the current cue point if a track is playing.<br />
Plays preview if a track is stopped at the cue point for as long as it's held down</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td>Jog wheel</td>
<td>Seeks forwards and backwards in a stopped track.<br />
Temporarily changes the playback speed for playing tracks<br />
Absolute sync of the track speed to the jog wheel if the scratch mode is enabled</td>
<td></td>
<td>Deck A: Select prev/next playlist<br />
Deck B: select prev/next track</td>
</tr>
<tr class="even">
<td>17</td>
<td>Deck volume slider</td>
<td>Controls the deck output volume.<br />
There is soft takeover after deck switch (1/3 or 2/4) to prevent wide parameter changes when the on-screen control diverges from the hardware control. Manipulating the control on the hardware will have no effect until the position of the hardware control is close to that of the software, at which point it will take over and operate as usual.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>20</td>
<td>Headphone monitor</td>
<td>Toggles this deck output to the headphones monitor on/off</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Troubleshooting

### Jog wheels not working or controller not responding

If your jog wheels doesn't work, or nothing works on the controller even
when you have carefully read all other resources, you should be aware
that this controller stores at least two configuration options in the
controller:

  - Enable/disable Jog Wheels
  - MIDI channel to use

and maybe a third one: Jog wheel sensitivity

With factory default settings, the jog wheels are enabled and the MIDI
channel used is channel 1. The mapping is made for channel 1 only. If
your controller is configured for another channel, nothing will work and
if you launch Mixxx with `-``-controllerDebug` parameter, you will have
lines like this one showing in the logs when you press a button on the
controller :

``` 
Debug [Controller]: "DJ Control MP3 e2 : 3 bytes: B3 38 38 " 
```

note the B3 here. it's B\<MIDI Channel \# - 1\>. So this controller is
configured on channel 4. controller configured on channel 1 will show
B0, which is correct.

To change these parameters, you have to use the configuration tool that
comes with the Hercules driver on on [the Hercules support
page](http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=61&pid=241&cid=1).
Unfortunately, the configuration tool is only available for Windows and
Mac OS X. We are not aware of any solution for Linux. So if you normally
use Linux, you will have to find a computer with Windows or Mac OS X,
install the Hercules driver, plug-in the controller and change
configuration. You will only need to do this once, then the controller
should work with Linux.

### Controller not recognized as bulk controller

It has been reported that when the Hercules drivers are installed on a
Windows, the driver takes over the bulk communication with the
controller so it cannot be recognized by Mixxx as a bulk controller.
Uninstall the Hercules driver and use it as a USB bulk controller.

## Mapping files

This mapping consists of 4 files:

  - `Hercules DJ Control MP3 e2.midi.xml`: MIDI XML mapping file
  - `Hercules DJ Control MP3 e2-scripts.js`: The main script, used
    directly by the MIDI XML mapping and by the USB bulk compatibility
    script.
  - `Hercules DJ Control MP3 e2.bulk.xml`: The USB bulk XML mapping
    file. Tells Mixxx to pass all incoming data to the
    MP3e2.incomingData function in the bulk compatibility script.
  - `Hercules-mp3e2-compat.js`: The USB bulk controller script that
    reads incoming data and calls the appropriate function in `Hercules
    DJ Control MP3 e2-scripts.js`
