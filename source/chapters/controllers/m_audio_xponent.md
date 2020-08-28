# M-Audio Torq Xponent

![http://ecx.images-amazon.com/images/I/41Fm-FrL5gL.jpg](http://ecx.images-amazon.com/images/I/41Fm-FrL5gL.jpg)

This device has been discontinued. M-Audio discontinued its DJ products
after the company was bought by inMusic in 2012. This device is a class
compliant USB audio and MIDI device, so it does not require a special
driver on any OS that Mixxx runs on.

## Note for Windows users

Typically, the ASIO sound API is the best option on Windows and it
requries an ASIO driver from the sound card manufacturer. However, it
seems that the current version of the Xponent ASIO driver for Windows
interferes with the ability to send MIDI control messages to the
Xponent. As a result, if you are running M-Audio's Xponent ASIO drivers
on Windows, the lights will not work. If you uninstall the drivers, the
lights will work, but you can no longer use the Xponent's sound card
with the ASIO sound API.

It is recommended to **use the WDM-KS sound API** instead. The sound
card will appear as "Analog Connector 1 (Xponent Audio)" and "Analog
Connector 2 (Xponent Audio)". Connector 2 is the main out, and Connector
1 is the headphones. The latency meter seems to run a bit higher than it
did under ASIO, so keep this in mind, and test both setups with your own
system to see how they compare. If you require low latency as well as a
lot of effects or time stretching, you may want to run with the ASIO
driver at the expense of the lights.

## Mixxx version 2.0 or later

A new mapping has been merged with Mixxx and will be included in Mixxx
in the 2.1 release. You can use it now with Mixxx 2.0 by downloading the
following files and putting them in your [controller mapping file
locations\#user controller mapping
folder](controller%20mapping%20file%20locations#user%20controller%20mapping%20folder):

  - [JS
    file](https://raw.githubusercontent.com/mixxxdj/mixxx/master/res/controllers/maudio_xponent.mixco.output.js)
  - [XML
    file](https://raw.githubusercontent.com/mixxxdj/mixxx/master/res/controllers/maudio_xponent.mixco.output.midi.xml)

The script was written with the [Mixco mapping
framework](https://sinusoid.es/mixco/). [Documentation for the
mapping](https://sinusoid.es/mixco/script/maudio_xponent.mixco.html) is
available on the Mixco website.

A separate, "[Advanced](M-Audio-Xponent-Advanced)" mapping has also been
created, and is currently in testing, but is available from the Mixxx
forums
[here](https://www.mixxx.org/forums/viewtopic.php?f=7&t=8884&sid=f9e6ecc3e7882a88a5dbe178a84dc8e7).

## Getting LEDs to work with old mappings (pre-2.0)

The Mixco mapping included with Mixxx 2.1 and usable with Mixxx 2.0 does
not require these steps.

How to start up Xponent in Listening Mode for LED support:

1.  Hold down the keys "2" (cues, not loops) and "key-lock" on the left
    deck of the Xponent
2.  Switch on the Xponent (while holding both keys)
3.  Wait until the Xponent is completely started up (red progress LEDS
    on both decks are fully lit) then release the keys
4.  Now LEDs work\!

You can verify that the Xponent is in "listening" mode by observing the
button behavior. If the buttons no longer pulse brightly and fade down
when you press them, then the Xponent is in the correct mode for use
with Mixxx.

## Advanced Mapping (beta)

A separate "Advanced" mapping is currently in its testing phase. The
latest version can be found in this [Forum
Post](https://www.mixxx.org/forums/viewtopic.php?f=7&t=8884).

This mapping expands on the stock 2.0 mapping by adding advanced
features such as:

  - Lights (No need to hold down any keys, but see the note for Windows
    users above)
  - Samplers
  - Effects
  - Beatgrid manipulation
  - Rolling beatloops
  - Soft-takeover for critical controls

This mapping is not yet final, and is not included in current Mixxx
distributions. This documentation should be considered preliminary and
subject to change.

Please refer to the following diagram for control numbers.
[[/media/xponent-mapping-2.png|]]

<table>
<thead>
<tr class="header">
<th>Number</th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 - 9</td>
<td>Connections (Not pictured)</td>
<td>Audio, power, and USB connections. These are located on the back of the unit.</td>
</tr>
<tr class="even">
<td>Bank</td>
<td>Bank switch (Not pictured)</td>
<td>Toggles between controlling decks 1 &amp; 2 to decks 3 &amp; 4.</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Touch Sensitivity</td>
<td>Enables or disables "scratch mode". When the button is lit, scratch mode is enabled.</td>
</tr>
<tr class="even">
<td>11</td>
<td>Jog Wheel</td>
<td>When the track is stopped, the jog wheel seeks forward and backward in the corresponding track.<br />
<br />
When the track is playing, the jog wheel speeds up or slows down the track.<br />
<br />
When scratch mode is enabled, moving the wheel by touching the top surface will scratch, while moving the wheel by touching the outer ring will act as a normal jog-wheel.</td>
</tr>
<tr class="odd">
<td>12</td>
<td>PFL (Pre-fade listen)</td>
<td>Selects which track(s) are heard through the headphone output<br />
<br />
This mapping has two PFL modes. The default is "independent" in which each deck's PFL can be enabled or disabled independently. The alternate mode is "toggle" in which only one deck will be active at a time. Pressing the PFL button on any deck will disable PFL on any other decks automatically. Pressing the already-selected PFL button will disable it. This setting can be toggled by holding both shift buttons and pressing any PFL button. The default mode can be changed in the config section of the M-Audio-Xponent-Advanced-scripts.js file.</td>
</tr>
<tr class="even">
<td>13</td>
<td>Master Output Volume</td>
<td>Controls the volume of the master audio output.<br />
<br />
<strong>Note:</strong> This is a hardware control, and changes will not be reflected in the Mixxx UI</td>
</tr>
<tr class="odd">
<td>14</td>
<td>Booth Output Volume</td>
<td>Controls the volume of the booth audio output.<br />
<br />
<strong>Note:</strong> This is a hardware control, and changes will not be reflected in the Mixxx UI</td>
</tr>
<tr class="even">
<td>15</td>
<td>Shift</td>
<td>Alters the behavior of certain controls. Certain controls have multiple "modes" which can be cycled through by holding both shift keys. These will be mentioned in-line.</td>
</tr>
<tr class="odd">
<td>16</td>
<td>Trackpad</td>
<td>Acts as a mouse input to the computer. The Midi mode (see #19) is not mapped at this time.</td>
</tr>
<tr class="even">
<td>17</td>
<td>Left Mouse Button</td>
<td>Used in conjunction with the Trackpad (see #16).</td>
</tr>
<tr class="odd">
<td>18</td>
<td>Right Mouse Button</td>
<td>Used in conjunction with the Trackpad (see #16).</td>
</tr>
<tr class="even">
<td>19</td>
<td>MIDI Mode Button</td>
<td>Changes the Trackpad and mouse buttons (See #16, #17, #18) into an X/Y input and two additional note inputs.<br />
<br />
<strong>Note:</strong> These MIDI inputs are not used in this mapping.</td>
</tr>
<tr class="odd">
<td>20</td>
<td>Channel Kills</td>
<td>The Gain kill (G), will momentarily silence the track entirely. The High (H), Mid (M) and Low (L) kills will cut that frequency band from the output.<br />
<br />
Holding both shift keys while pressing either gain kill button will toggle the vu meters between master output mode and per-channel mode (see #23).</td>
</tr>
<tr class="even">
<td>21</td>
<td>Brake / Play Backwards</td>
<td>The Big X button is tied to the Brake effect. Releasing the brake before the track has stopped will resume playing, while holding it until the track has stopped completely will leave the track paused.<br />
<br />
The Big Minus button momentarily plays the corresponding track backwards. Normal play will resume when it is released. Holding the corresponding deck's shift button while pressing the Big Minus button will do a rolling reverse (censor mode), and will resume play at the point the track would have been if the Big Minus had never been pressed.</td>
</tr>
<tr class="odd">
<td>22</td>
<td>Gain / EQ</td>
<td>The top knob controls the gain for that deck, while the lower three control the High, Mid, and Low EQ channels. All are soft-takeover enabled.</td>
</tr>
<tr class="even">
<td>23</td>
<td>VU Meters</td>
<td>Displays the current output level for the corresponding deck.<br />
<br />
<strong>Note:</strong> This behavior can be switched to behave as a master-out meter instead by setting the value of MaudioXponent.vuMeterMode to 1 in the M-Audio-Xponent-Advanced-scripts.js file, or by holding both shift keys and pressing either gain kill button (see #20).</td>
</tr>
<tr class="odd">
<td>24 / 25</td>
<td>Samplers / Effects</td>
<td>The four knobs and buttons below each jogwheel perform different functions.<br />
<br />
The left-hand side controls the samplers, with the knobs controlling the volume, and the buttons firing off the samples.<br />
<br />
The right-hand side controls effects. Pressing one of the buttons will give the corresponding effect (1-4) the "focus", and light up accordingly. Once an effect has the focus, pressing the button again will toggle it on and off. The knobs will control the parameters of the effect that currently has the focus. The first three knobs will control the first three parameters for that effect. The fourth knob will always control the wet/dry mix. Any additional effect parameters beyond three will have to be controlled from the Mixx UI.<br />
<br />
<strong>Note:</strong> Due to limitations in the 2.0 release of Mixxx, the parameter knobs cannot perform a soft-takeover, so be aware of this if you are using multiple effects. This is expected to change in 2.1</td>
</tr>
<tr class="even">
<td>26</td>
<td>Nudge</td>
<td>Temporarily speeds up or slows down the corresponding track. These buttons have an alternate "backwards" mode with respect to the Mixxx UI. In this mode the "&lt;" button "nudges" the track to the left (looking at the waveform displays), while "&gt;" slows the track down, "nudging" it to the right. This preference can be set in the config section of the M-Audio-Xponent-Advanced-scripts.js file, or toggled by holding both shift keys and pressing any nudge button.</td>
</tr>
<tr class="odd">
<td>27</td>
<td>PFL Mix</td>
<td>Controls the headphone mix. All the way to the left sends only the track(s) selected by the PFL buttons (see #12) to the headphones. All the way to the right sends only the main output to the headphones</td>
</tr>
<tr class="even">
<td>28</td>
<td>Headphone Volume</td>
<td>Controls the volume of the headphones.<br />
<br />
<strong>Note:</strong> This is a hardware control, and changes will not be reflected in the Mixxx UI.</td>
</tr>
<tr class="odd">
<td>29</td>
<td>Progress meter</td>
<td>Indicates the progress through the corresponding track. At thirty seconds from the end of the track, the progress meter will flash to indicate that the end of the track is approaching.</td>
</tr>
<tr class="even">
<td>30</td>
<td>Seek</td>
<td>Fast-forward and fast-rewind.</td>
</tr>
<tr class="odd">
<td>31</td>
<td>Hotcues and Beatgrid</td>
<td>The upper numbered buttons set or activate hotcues. Holding shift while pressing a hotcue button clears that hotcue.<br />
<br />
The &lt; and &gt; buttons shift the beatgrid left or right and can be used to make minor corrections on the fly. Holding shift while pressing either button will align the beatgrid to the current position.<br />
<br />
The lock button toggles Keylock on and off for that deck. Holding shift while pressing it toggles Quantize on and off for that deck.<br />
<br />
The + and - buttons increase or decrease the speed of the corresponding track.</td>
</tr>
<tr class="even">
<td>32</td>
<td>Rate Slider</td>
<td>Affects the speed of the corresponding track. Soft-takeover is enabled for this control, so if you don't typically use the sliders, you can safely "stow" them at either extreme and then reset the track speed using the Mixxx UI.</td>
</tr>
<tr class="odd">
<td>33</td>
<td>Channel Volume</td>
<td>Normal function, but with soft-takeover enabled.</td>
</tr>
<tr class="even">
<td>34</td>
<td>Sync</td>
<td>Normal function. Flashes on each beat of the corresponding track.<br />
<br />
<strong>Note:</strong> The flashing behavior can be customized by setting the MaudioXponent.syncFlashMode value in the M-Audio-Xponent-Advanced-scripts.js file. 0=No flash, 1=Simple flash, 2=Toggle flash. In Toggle mode, the button will toggle between lit and unlit with each beat. Holding both shift buttons while pressing either Sync button will cycle through the available modes at runtime.</td>
</tr>
<tr class="odd">
<td>35</td>
<td>Cue</td>
<td>Normal function.</td>
</tr>
<tr class="even">
<td>36</td>
<td>Loops</td>
<td>The 1, 2, 4, and 8 buttons behave as normal, starting a loop of X beats at the current position. Pressing the same button again while looping will exit that loop. Holding shift while pressing the loop buttons will do a rolling beat loop of 1, 1/2, 1/4, or 1/8th beats, continuing where the song would have been without the loop when they are released.</td>
</tr>
<tr class="odd">
<td>37</td>
<td>Play/Pause</td>
<td>Normal function.</td>
</tr>
<tr class="even">
<td>38</td>
<td>Punch-In</td>
<td>Momentarily pulls the cross-fader to the center position while pressed. This only works when the cross-fader is far enough toward the opposite deck, and can be used to momentarily "punch-in" audio from the other deck.</td>
</tr>
<tr class="odd">
<td>39</td>
<td>Cross-fader</td>
<td>Normal function, but with soft-takeover enabled.</td>
</tr>
</tbody>
</table>
