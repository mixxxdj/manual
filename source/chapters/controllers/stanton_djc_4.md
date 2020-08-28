# Stanton DJC.4

[[/media/hardware/stanton-djc4_top.jpg|]]

  - [Manufacturer's product
    page](http://www.stantondj.com/stanton-controllers-systems/djc4.html//)
  - [Manual / Midi
    commands](http://www.stantondj.com/pdf/products/controllers/djc4/DJC.4ManualV1.1.pdf//)
  - [Review by
    DJWORKX](https://djworx.com/review-stanton-djc-4-controller//)
  - [Review by DJ
    TechTools](https://djtechtools.com/2012/08/29/review-stanton-djc-4-controller//)
  - [Forum
    thread](https://mixxx.discourse.group/t/mapping-for-stanton-djc-4/14074)

## Compatibility

This controller is a class compliant USB MIDI and audio device, so it
can be used without any special drivers on GNU/Linux, Mac OS X, and
Windows. However, if you wish to use the [ASIO sound
API](http://mixxx.org/manual/latest/chapters/configuration.html#audio-api)
under Windows, please install the latest driver package available from
the [Product
page](http://www.stantondj.com/stanton-controllers-systems/djc4.html//).

## Sound card setup

[[/media/hardware/stanton-djc-4-rear.jpg|]]

This controller has a built-in 4 channel sound card, with MASTER output
(RCA and balanced 6.3 mm TRS) and HEADPHONE output (6.3 and 3.5mm jack).

| Output        |                          |
| ------------- | ------------------------ |
| Channels      | Assign to                |
| 1-2           | Master                   |
| 3-4           | Headphones               |
| Input         |                          |
| Channels      | Assign to                |
| 1-2 (Input 1) | Vinyl Control 1 or Aux 1 |
| 3-4 (Input 2) | Vinyl Control 2 or Aux 2 |

Above the **Gain** knobs are switches to select which input should be
sent to the PC. For input 1 this can be Aux (3.5 mm TRS) or Line/Phono
1/2 (RCA) and for input 2 this can be microphone (6.3 mm TRS on front)
or Line/Phono 3/4 (RCA).

#### Input 1 routing

On the rear side is a small switch to select if Input 1 is routed to the
PC or directly to the master output (through). It is therefore possible
to include the microphone into a recording/stream or to exclude it.

Please refer to [the user
manual](https://mixxx.org/manual/latest/en/chapters/example_setups.html#laptop-and-external-usb-audio-interface)
for more details about the audio configuration in Mixxx.

#### Hardware controls

The **Master** and **Mic Level** are hardware controls and interact
directly with the integrated sound card and are not mapped to Mixxx.

Please refer to [the user
manual](https://mixxx.org/manual/latest/en/chapters/djing_with_mixxx.html#djing-gain-staging)
in order to learn how to set your levels properly when using Mixxx.

[[/media/hardware/stanton-djc-4-front.jpg|]]

## Mapping description

The mapping is included in Mixxx 2.2.4 and newer.

Load the preset as described in [the user
manual](https://mixxx.org/manual/latest/en/chapters/controlling_mixxx.html#using-midi-hid-controllers)

#### Controls not included in this mapping

  - Master knob (Hardware control)
  - Mic level knob (Hardware control)
  - Mic on/off switch (Hardware control)
  - Loop Delete button (no matching function in Mixxx)
  - X-Fader Link button
  - Smart Fade button
  - Smart button (Shift + Scratch)
  - Video button (Shift + Smart Fade)
  - FX Ctrl 1/2 fader (Shift + Channel fader)
  - TX/FX Select rotary encoder
  - TX/FX Action rotary encoder button

### Controls

<table>
<thead>
<tr class="header">
<th>Center section</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No.</td>
<td>Control</td>
<td>Function</td>
</tr>
<tr class="even">
<td>1</td>
<td>SAMPLER VOLUME knob</td>
<td>Change the volume of all eight samplers at the same time. If the SAMPLER VOLUME is at zero hide the sampler bank.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>BROWSER Rotary encoder</td>
<td>Turn to move tracklist/sidebar cursor up/down. Press to toggle between sidebar and tracklist.</td>
</tr>
<tr class="even">
<td>2</td>
<td>SHIFT + BROWSER Rotary encoder</td>
<td>Turn to move tracklist/sidebar cursor page wise up/down. Press to (Un-)Maximizes the library view.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>LOAD buttons</td>
<td>Load song into active deck (Depending on Deck select).</td>
</tr>
<tr class="even">
<td>3</td>
<td>SHIFT + LOAD buttons</td>
<td>Open/close a tree view. Equivalent to pressing the LEFT/RIGHT key on the keyboard</td>
</tr>
<tr class="odd">
<td>Mixer section</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>No.</td>
<td>Control</td>
<td>Function</td>
</tr>
<tr class="odd">
<td>1</td>
<td>GAIN knobs</td>
<td>Adjust the deck gain (prefader)</td>
</tr>
<tr class="even">
<td>2</td>
<td>HI, MID, LOW knobs</td>
<td>Adjust the high/mid/low-frequency regions of the song. Press to kill this frequency region.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>SHIFT + LOW knob</td>
<td>QuickEffect superknob (filter by default). Press to (de-)activate QuickEffect.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Channel CUE buttons</td>
<td>Toggle PFL for each channel.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Channel faders</td>
<td>Adjust the output level for each channel.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Cross fader</td>
<td>Fades between left and right deck.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Level indicator</td>
<td>Indicate the output level of master.</td>
</tr>
<tr class="even">
<td>8</td>
<td>CROSSFADER CURVE (front side of controller)</td>
<td>Adjust crossfader curve between fade and cut.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>HEADPHONES MIX (front side of controller)</td>
<td>Adjusts the cue/main mix in the headphone output.</td>
</tr>
<tr class="even">
<td>10</td>
<td>HEADPHONES LEVEL (front side of controller)</td>
<td>Adjusts the headphone output gain.</td>
</tr>
<tr class="odd">
<td>Deck section</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>No.</td>
<td>Control</td>
<td>Function</td>
</tr>
<tr class="odd">
<td>1</td>
<td>Jog dial (top surface)</td>
<td>Perform scratch operation if Scratch is enabled.</td>
</tr>
<tr class="even">
<td>1</td>
<td>Jog dial (outer edge)</td>
<td>Rotate to lower/raise playback speed if Scratch is enabled (and pitch if key lock is off).</td>
</tr>
<tr class="odd">
<td>1</td>
<td>SHIFT + Jog dial (top surface)</td>
<td>Search fast through the playback location.</td>
</tr>
<tr class="even">
<td>2</td>
<td>SCRATCH button</td>
<td>En-/Disable scratch function</td>
</tr>
<tr class="odd">
<td>3</td>
<td>SHIFT button</td>
<td>Hold down to access other functions.</td>
</tr>
<tr class="even">
<td>4</td>
<td>SYNC button</td>
<td>Match tempo and phase of other deck.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>SHIFT + SYNC button</td>
<td>Plays the track reverse as long as pressed.</td>
</tr>
<tr class="even">
<td>4</td>
<td>TAP button (tap repeatedly)</td>
<td>Set tempo by tapping on each beat.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>CUE button</td>
<td>Specifies, plays or recalls temporary cue point.</td>
</tr>
<tr class="even">
<td>5</td>
<td>SHIFT + CUE button</td>
<td>Jumps to the cue point and stops.</td>
</tr>
<tr class="odd">
<td>6</td>
<td>PLAY/PAUSE button</td>
<td>Plays or pause the song.</td>
</tr>
<tr class="even">
<td>11</td>
<td>DECK select buttons</td>
<td>Switches the deck (left: decks 1 and 3, right: decks 2 and 4)</td>
</tr>
<tr class="odd">
<td>12</td>
<td>KEY LOCK</td>
<td>Toggle key lock.</td>
</tr>
<tr class="even">
<td>12</td>
<td>SHIFT + KEY LOCK</td>
<td>Toggle beats quantization.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>Tempo slider</td>
<td>Adjust song playback speed (and pitch if key lock if off).</td>
</tr>
<tr class="even">
<td>14</td>
<td>PITCH BEND +</td>
<td>Holds the speed one step (4 % default) higher while pushed.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>PITCH BEND -</td>
<td>Holds the speed one step (4 % default) lower while pushed.</td>
</tr>
<tr class="even">
<td>14, 15</td>
<td>SHIFT + PITCH BEND</td>
<td>Not mapped.</td>
</tr>
<tr class="odd">
<td>16</td>
<td>HOT CUE</td>
<td>Set (if empty) or Play Hot Cue Point.</td>
</tr>
<tr class="even">
<td>16</td>
<td>SHIFT + HOT CUE</td>
<td>Unset/Delete Hot Cue Point</td>
</tr>
<tr class="odd">
<td>Loop section</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>No.</td>
<td>Control</td>
<td>Function</td>
</tr>
<tr class="odd">
<td>1</td>
<td>IN</td>
<td>If loop is disabled, sets the player loop in position to the current play position. If loop is enabled, press and hold to move loop in position to the current play position.</td>
</tr>
<tr class="even">
<td>1</td>
<td>SHIFT + IN</td>
<td>Seek to the loop in point.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>OUT</td>
<td>If loop is disabled, sets the player loop out position to the current play position. If loop is enabled, press and hold to move loop out position to the current play position.</td>
</tr>
<tr class="even">
<td>2</td>
<td>SHIFT + OUT</td>
<td>Seek to the loop out point.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>ON</td>
<td>Toggles the current loop on or off. If the loop is ahead of the current play position, the track will keep playing normally until it reaches the loop.</td>
</tr>
<tr class="even">
<td>3</td>
<td>SHIFT + ON</td>
<td>Activate current loop, jump to its loop in point, and stop playback.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>DELETE</td>
<td>Not mapped.</td>
</tr>
<tr class="even">
<td>5</td>
<td>LOOP LENGTH /</td>
<td>Halves beatloop_size.</td>
</tr>
<tr class="odd">
<td>6</td>
<td>LOOP LENGTH X</td>
<td>Doubles beatloop_size.</td>
</tr>
<tr class="even">
<td>7</td>
<td>BEAT MULTIPLIER encoder</td>
<td>Turn to move the loop left or right by 1 beat per click.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>BEAT MULTIPLIER button</td>
<td>Set a loop that is beatloop_size beats long and enables the loop.</td>
</tr>
<tr class="even">
<td>7</td>
<td>SHIFT + BEAT MULTIPLIER button</td>
<td>Activates a rolling loop over beatloop_size beats.</td>
</tr>
<tr class="odd">
<td>Sampler section</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>No.</td>
<td>Control</td>
<td>Function</td>
</tr>
<tr class="odd">
<td>1</td>
<td>SAMPLER 1-4</td>
<td>Left deck controls sampler 1-4, right deck sampler 5-8 (independent of deck selection)<br />
<em>See <a href="contributing_mappings#sampler_buttons">Standard sampler mapping</a>.</em></td>
</tr>
<tr class="even">
<td>Effect section</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>No.</td>
<td>Control</td>
<td>Function</td>
</tr>
<tr class="even">
<td>1</td>
<td>ON</td>
<td>Toggle FX 1 for decks 1/3 (both on the left) and FX 2 for decks 2/4 (both on the right).</td>
</tr>
<tr class="odd">
<td>2-5</td>
<td><em>Various</em></td>
<td><em>See <a href="standard_effects_mapping">Standard effects mapping</a>.</em></td>
</tr>
</tbody>
</table>

### Tweakables

At the top of the file \`Stanton-DJC-4-scripts.js\` there are a few
customizable options to change the default mapping.

| Variable          | Function                                                                                   | Default |
| ----------------- | ------------------------------------------------------------------------------------------ | ------- |
| autoShowFourDecks | If a track gets loaded into deck 3 or 4, should automatically four decks be shown in Mixxx | false   |
| showMasterVu      | If set to false, show channel VU meter instead of Master L/R                               | true    |
| dryWetAdjustValue | Amount the dryWetKnob changes the value for each increment                                 | 0.05    |
