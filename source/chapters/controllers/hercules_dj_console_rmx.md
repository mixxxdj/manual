# Hercules DJ Console RMX

[[/media/hardware/hercules_dj_console_rmx.jpg|]]

  - [Manufacturer's product
    page](http://www.hercules.com/us/legacy/bdd/p/62/dj-console-rmx/)

The Hercules DJ Console RMX is a USB controller with a built in sound
card. It is a class compliant USB Audio and HID device. Older versions
of Mixxx that did not support HID required using Hercules' MIDI driver,
but it is now recommend to not use the Hercules driver on GNU/Linux. If
you have it installed, it is recommended to uninstall the driver and
upgrade to the [latest version of Mixxx](http://mixxx.org/download) if
you have not already. On Windows (and Mac OS X?) the driver is still
recommended.

## Audio

The sound card has 4 inputs and 4 outputs (2 stereo in/out). The inputs
are switchable between line-in and phono, so you can connect both CD
players and turntables on the inputs. The inputs require a high input
signal (\~10mV+) for turntables if you want to record audio or mix it to
the output. Time-coded vinyls, for Vinyl Control, should work okay with
lower input signal.

## MIDI Mappings

### Hercules DJ Console RMX

#### Global controls

<table>
<thead>
<tr class="header">
<th>Control</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Cross-Fader</td>
<td>Fades between left and right deck</td>
</tr>
<tr class="even">
<td>Vol. Main</td>
<td>Controls output volume of your mix</td>
</tr>
<tr class="odd">
<td>Balance</td>
<td>Controls balance between left and right audio channel of your mix</td>
</tr>
<tr class="even">
<td>Scratch</td>
<td>Toggles scratch on and off which changes the function of the deck jog wheels<br />
<strong>Effect Shift</strong> when held down:<br />
-Shifts function of each decks Bass, Medium, Treble to control effect parameters</td>
</tr>
<tr class="odd">
<td>Up / Down</td>
<td>Moves up and down in the library track list<br />
When held down changes the jog wheels behaviour to scroll the library list</td>
</tr>
<tr class="even">
<td>Left / Right</td>
<td>Moves up and down between the library sections</td>
</tr>
<tr class="odd">
<td>Monitor</td>
<td>Fades monitor output (headphones) between cue selected tracks output and the main mix</td>
</tr>
</tbody>
</table>

#### Deck / Channel specific controls

<table>
<thead>
<tr class="header">
<th>Control</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Play/Pause</td>
<td>Starts playing a loaded track if stopped. If track is currently playing it stops the track</td>
</tr>
<tr class="even">
<td>Stop</td>
<td>Stops a currently playing track and moves to the beginning.</td>
</tr>
<tr class="odd">
<td>Cue</td>
<td>Sets the cue point if a track is stoped and not at the current cue point<br />
Stops track and returns to the current cue point if a track is playing.<br />
Plays preview if a track is stopped at the cue point for as long as it's held down</td>
</tr>
<tr class="even">
<td>Jog wheel</td>
<td>Seeks forwards and backwards in a stopped track<br />
Temporarily changes the playback speed for playing tracks<br />
Scratches both stopped and playing tracks when scratch mode is on<br />
Moves up / down in the tracklist if either Up or Down is held down</td>
</tr>
<tr class="odd">
<td>Forward / Backward</td>
<td>Seeks at high speed in a track</td>
</tr>
<tr class="even">
<td>Load Deck A/B</td>
<td>Loads the currently selected track in the track list to the related deck</td>
</tr>
<tr class="odd">
<td>Cue Select</td>
<td>Toggles this decks output to the monitor (headphones) on and off</td>
</tr>
<tr class="even">
<td>Pitch</td>
<td>Adjusts playback speed +/-10% (can be adjusted in the preferences)</td>
</tr>
<tr class="odd">
<td>Sync</td>
<td>Automatically sets pitch so the BPM of the other deck is matched</td>
</tr>
<tr class="even">
<td>Pitch Reset</td>
<td>Resets the pitch to the tracks normal playback speed</td>
</tr>
<tr class="odd">
<td>Bass</td>
<td>Adjusts the volume of a channels low frequency content (ex. bass drum)<br />
Adjusts flanger period when Effect Shift is held down</td>
</tr>
<tr class="even">
<td>Medium</td>
<td>Adjusts the volume of a channels mid frequency content (ex. vocals)<br />
Adjusts flanger delay when Effect Shift is held down</td>
</tr>
<tr class="odd">
<td>Treble</td>
<td>Adjusts the volume of a channels high frequency content (ex. hi-hats)<br />
Adjusts flanger depth when Effect Shift is held down</td>
</tr>
<tr class="even">
<td>Kill (Bass / Medium / Treble)</td>
<td>Toggles output of a frequency band on and off</td>
</tr>
<tr class="odd">
<td>Gain</td>
<td>Controls a decks input volume</td>
</tr>
<tr class="even">
<td>Vol. Deck A/B</td>
<td>Controls a decks output volume</td>
</tr>
<tr class="odd">
<td>Keypad 1</td>
<td>Toggles a channels flanger effect on and off</td>
</tr>
<tr class="even">
<td>Keypad 4</td>
<td>Reveses playback direction when held down</td>
</tr>
</tbody>
</table>

### Hercules DJ Console RMX Advanced

The advanced mapping works similar to the normal RMX mapping, but also
supports loops and hot cues. This mapping was added to not brake the
previous (Mixxx -1.7.2) behaviour. Controls that differ between the
normal and advanced mappings are described here.

#### Global controls

<table>
<thead>
<tr class="header">
<th>Control</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Scratch</td>
<td>Toggles scratch on and off which changes the function of the deck jog wheels<br />
<strong>Effect Shift</strong> when held down:<br />
-Shifts function of each decks Bass, Medium, Treble to control effect parameters<br />
-Shifts the Keypad (1-6) functions to effects. Currently flanger and reverse</td>
</tr>
</tbody>
</table>

#### Deck / Channel specific controls

<table>
<thead>
<tr class="header">
<th>Control</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Stop</td>
<td><strong>Deck shift</strong> changes behaviour of other controls related to this deck when held down</td>
</tr>
<tr class="even">
<td>Forward / Backward</td>
<td>Adjusts position of loop in/out and hot cues when a loop / hot cue button is held down</td>
</tr>
<tr class="odd">
<td>Bass</td>
<td>Adjusts the volume of a channels low frequency content (ex. bass drum)<br />
Soft takeover when Deck Shift is held down, lets you move knob in position before adjusting<br />
Adjusts flanger period when Scratch is held down</td>
</tr>
<tr class="even">
<td>Medium</td>
<td>Adjusts the volume of a channels mid frequency content (ex. vocals)<br />
Soft takeover when Deck Shift is held down, lets you move knob in position before adjusting<br />
Adjusts flanger delay when Scratch is held down</td>
</tr>
<tr class="odd">
<td>Treble</td>
<td>Adjusts the volume of a channels high frequency content (ex. hi-hats)<br />
Soft takeover when Deck Shift is held down, lets you move knob in position before adjusting<br />
Adjusts flanger depth when Scratch is held down</td>
</tr>
<tr class="even">
<td>Keypad 1</td>
<td>Go to hotcue 1<br />
Set hotcue 1 when Deck Shift is held down<br />
Toggles a channels flanger effect on and off when Effect Shift is held down</td>
</tr>
<tr class="odd">
<td>Keypad 2</td>
<td>Go to hotcue 2<br />
Set hotcue 2 when Deck Shift is held down</td>
</tr>
<tr class="even">
<td>Keypad 3</td>
<td>Go to hotcue 3<br />
Set hotcue 3 when Deck Shift is held down</td>
</tr>
<tr class="odd">
<td>Keypad 4</td>
<td>Hold down to adjust loop in position with Forward / Backward<br />
Set loop in when Deck Shift is held down<br />
Reveses playback direction when held down if Effect Shift is held down</td>
</tr>
<tr class="even">
<td>Keypad 5</td>
<td>Hold down to adjust loop out position with Forward / Backward<br />
Set loop out when Deck Shift is held down</td>
</tr>
<tr class="odd">
<td>Keypad 6</td>
<td>Re-loop / exit turns looping on and off<br />
Half loop when Deck Shift is held down</td>
</tr>
</tbody>
</table>

## Mappings for Mixxx 1.6.1+herc - 1.7.2

### 1.6

[[/media/hercules_rmx_top_face.png|]]

| Hercules RMX Controls |                           |
| --------------------- | ------------------------- |
| Control               | Default Mixxx Mapping     |
| Vol Main (25)         | Master Gain               |
| 1 (9)                 | Flanger                   |
| 4 (9)                 | Reverse                   |
| Up (8)                | Select Prev Track in List |
| Down (8)              | Select Next Track in List |
| 2,3,5,6 (9)           | Unmapped                  |
| Right, Left (8)       | Unmapped                  |
| Stop (20)             | Unmapped                  |
| Pitch Reset (14)      | Unmapped                  |
| Beat Lock (13)        | Unmapped                  |
| Scratch (7)           | Unmapped                  |
| Mic Functions (1)     | Not Available in Mixxx    |

### 1.7

| Hercules RMX Controls - Mixxx 1.7 Additions |                                                                                                                |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Control                                     | Default Mixxx Mapping                                                                                          |
| Scratch (7)                                 | MIDI Script: Toggle Jog (18) Scratch/Pitch Adjust behaviour                                                    |
| Stop (20)                                   | MIDI Script: Stop + Reset Track to beginning                                                                   |
| Up (8)/Down (8) + Jog (18)                  | MIDI Script: Rapid Track List scrolling (buggy)                                                                |
| Cue (21) + Play (19)                        | MIDI Script: Pushing Play while holding Cue will cause track to continue to play after Cue is released (buggy) |
