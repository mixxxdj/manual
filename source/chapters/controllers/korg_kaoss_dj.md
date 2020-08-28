# Korg Kaoss DJ controller

2-deck controller with touch controlled jogwheels, built-in 4-channel
soundcard and a Korg Kaoss Pad as built-in effect section (can be
switched off for using software effects).

[[/media/hardware/korg_kaoss_dj.png|korg\_kaoss\_dj.png]]
[[/media/hardware/korg-kaoss-dj_mode-switch.jpg|]]
[[/media/hardware/korg-kaoss-dj_linein.jpg|]]
[[/media/hardware/korg-kaoss-dj_lineout.jpg|]]
[[/media/hardware/korg-kaoss-dj_headphones_mic.jpg|]]
[[/media/hardware/korg-kaoss-dj_overview.jpg|]]

  - [Manufacturer's product
    page](http://www.korg.com/uk/products/dj/kaoss_dj/)
  - [Forum
    thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=8479)
  - [Original mapping for
    Mixxx 2.1](https://www.mixxx.org/forums/viewtopic.php?f=7&t=8479&sid=ab4dc81e20ea737dd318d1b478fbb8ec&start=10#p33220)
  - [Current mapping for
    Mixxx 2.1](https://github.com/larromba/mixxx_kaoss_dj)
  - [Pull request on Github](https://github.com/mixxxdj/mixxx/pull/1509)

## Configuration options

## Mapping

[[/media/hardware/korg_kaoss_dj_diagram.png|]]

<table>
<thead>
<tr class="header">
<th>No.</th>
<th>Name</th>
<th>Function</th>
<th>Shifted Operation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Headphone knob</td>
<td>Adjusts the headphone level</td>
<td>---</td>
</tr>
<tr class="even">
<td>2</td>
<td>Balance knob</td>
<td>Adjusts the balance between the master level and the headphone monitor level</td>
<td>---</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Master knob</td>
<td>Adjust the master volume level</td>
<td>---</td>
</tr>
<tr class="even">
<td>4</td>
<td>Browse knob</td>
<td>Selects a song from the library</td>
<td>Moves between levels (TODO)</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Display</td>
<td>Indicates the effect number or parameter</td>
<td>Indicates the key or scale</td>
</tr>
<tr class="even">
<td>6</td>
<td>Touchpad Mode Button</td>
<td>Switches the touchpad between the Controller, KAOSS Effect, and Sampler modes (long press for blue LED)</td>
<td>---</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Program/Value Knob</td>
<td>Selects an effect</td>
<td>Selects a key, selects a scale</td>
</tr>
<tr class="even">
<td>8</td>
<td>Tap Button</td>
<td>Sets the tempo<br />
Long-press this button to access the auto BPM function</td>
<td>Key setting mode</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Hold Button</td>
<td>Enables/disables the touchpad’s hold function</td>
<td>Scale setting mode</td>
</tr>
<tr class="even">
<td>10</td>
<td>Touchpad (controller mode)</td>
<td>Controls the effects of the DJ software. The vertical axis controls the mix (dry/wet) knob and the horizontal axis controls the super knob.</td>
<td>Adjusts the Beats Multiplier (TODO)</td>
</tr>
<tr class="odd">
<td>:::</td>
<td>Touchpad (Kaoss Effect mode)</td>
<td>Controls the KAOSS effect</td>
<td>Adjusts the depth of the KAOSS Effect</td>
</tr>
<tr class="even">
<td>:::</td>
<td>Touchpad (sampler mode)</td>
<td>Controls the sampler function of the DJ software</td>
<td>---</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Crossfader</td>
<td>Adjusts the balance between Decks A and B</td>
<td>---</td>
</tr>
<tr class="even">
<td>12</td>
<td>Touch Slider mode button</td>
<td>Switches between the three touch slider mode</td>
<td>---</td>
</tr>
<tr class="odd">
<td>13</td>
<td>Touch Slider (Normal mode)</td>
<td>Left Side - Nudges (pitch -)<br />
Center - Enables the touch wheel's Scratch mode<br />
Right Side - Nudges (pitch +)</td>
<td>Moves to the specified position in the song (slider)</td>
</tr>
<tr class="even">
<td></td>
<td>Touch Slider (Hot Cue mode)</td>
<td>Left Side - Sets Hot Cue 1, and moves to Hot Cue 1<br />
Center - Sets Hot Cue 2, and moves to Hot Cue 2<br />
Right Side - Sets Hot Cue 3, and moves to Hot Cue 3</td>
<td>Deletes Hot Cue 1<br />
Deletes Hot Cue 2<br />
Deletes Hot Cue 3</td>
</tr>
<tr class="odd">
<td></td>
<td>Touch Slider (Loop mode)</td>
<td>Left Side - Auto Loop × 1/2<br />
Center - Loop on/off<br />
Right Side - Auto Loop × 2</td>
<td>Sets the Loop In point<br />
Auto Loop × 1<br />
Sets the Loop Out point</td>
</tr>
<tr class="even">
<td>14</td>
<td>EQ</td>
<td>Boosts or Cuts the Hi EQ<br />
Boosts or Cuts the Mid EQ<br />
Boosts or Cuts the Lo EQ</td>
<td>---<br />
---<br />
---</td>
</tr>
<tr class="odd">
<td>15</td>
<td>Gain knob</td>
<td>Adjusts the gain</td>
<td>---</td>
</tr>
<tr class="even">
<td>16</td>
<td>Load button</td>
<td>Loads the song into the selected deck</td>
<td>---</td>
</tr>
<tr class="odd">
<td>17</td>
<td>Fx button</td>
<td>Left - FX1 rack mix knob can be manipulated when enabled<br />
Right - FX2 rack mix knob can be manipulated when enabled</td>
<td>---</td>
</tr>
<tr class="even">
<td>18</td>
<td>Headphone cue button</td>
<td>Turns the headphone monitor on/off</td>
<td>Switches the function of the level meter between Deck A/B and the Master level</td>
</tr>
<tr class="odd">
<td>19</td>
<td>Touch wheel</td>
<td>Scratches (in scratch mode) or adjusts the pitch</td>
<td>Search function (in scratch mode) or moves beatgrid</td>
</tr>
<tr class="even">
<td>20</td>
<td>Pitch fader</td>
<td>Adjusts the pitch</td>
<td>---</td>
</tr>
<tr class="odd">
<td>21</td>
<td>Level meter</td>
<td>Indicates the input level to deck A/B or the master level</td>
<td>---</td>
</tr>
<tr class="even">
<td>22</td>
<td>Shift button</td>
<td>Holding this button provides access to the controllers SHIFT functions</td>
<td>---</td>
</tr>
<tr class="odd">
<td>23</td>
<td>Play / pause button</td>
<td>Starts/pauses the song</td>
<td>Key Lock On/Off</td>
</tr>
<tr class="even">
<td>24</td>
<td>Sync button</td>
<td>Synchronizes the tempo of Deck A and Deck B</td>
<td>Cancels tempo synchronization</td>
</tr>
<tr class="odd">
<td>25</td>
<td>Cue button</td>
<td>Sets the cue point or moves to the cue point</td>
<td>Returns to the beginning of the song.</td>
</tr>
<tr class="even">
<td>26</td>
<td>Level fader</td>
<td>Adjusts the level of deck A/B</td>
<td>---</td>
</tr>
</tbody>
</table>
