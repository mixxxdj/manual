# Denon MC7000

[[/media/hardware/denondj-img-mc7000.jpg]]

  - [Denon MC7000 Mapping thread](https://mixxx.discourse.group/t/denon-mc7000-mapping/18235)
  - [Manufacturer's product page](https://www.denondj.com/professional-dj-controller-for-serato-mc7000xus)
  - [User Guide](http://cdn.inmusicbrands.com/denondj/MC7000/MC7000-UserGuide-v1.1.pdf)
  - [Hardware Setting Specification](http://cdn.inmusicbrands.com/denondj/MC7000/MC7000-Hardware-Settings-Mode-Specification-v1_4.pdf)

## General

The Denon MC7000 is a professional DJ controller which has got 4-channel
capability and dual USB connections. These two USB audio interfaces
enable two DJs to play together. This controller includes Denon's high
build quality and superior 24-bit audio reproduction, makes this suited
to both mobile and club DJs.

The dual 6" platters have a touch-capacitive design with rotational LED
displays. The MC7000 has exclusive and dedicated Key Matching and
Changing controls that deliver an unprecedented ability to instantly and
harmonically match musical keys. The unit’s comprehensive, multi-input
mixer also provides access to line/phono inputs from both authentic
analogue (vinyl) and digital sources.

### Features

  - 4-channel DJ controller with digital mixer
  - Dual USB audio interfaces - connect 2 computers at once
  - 16 velocity-sensitive performance pads
  - New dedicated key-matching and changing controls
  - Solid 6-inch touch-capacitive platters with tracking LED
  - 2 mic inputs with dedicated controls
  - XLR Booth and Master connections

## Compatibility

  - **Mac** users should be just fine connecting the MC7000 and go.
  - **Windows** users need to install the Windows Driver from [Denon
    Download Site](https://www.denondj.com/downloads).
  - **Linux** users need to know that the MC7000 internal audio
    interface is not available out-of-the-box for older Linux Kernels.
    You should upgrade your **Kernel** to minimum versions LTS:
    **4.19.105** or **5.4.21**, stable branch **5.6.x** or mainline
    **5.7.x** (valid at date 2020-04-28). Newer Kernels will also
    provide native audio support for this controller. Linux Kernel 5.3.x
    does not support that device and together with 5.5.x reached
    End-Of-Life.
    * Linux Distributions built upon Ubuntu 18.04 and derivatives, like
    Linux Mint, KDE Neon etc. must update the Kernel to one of the
    mentioned above. As of July 2020 the Kernel 5.4.x is available from 
    the Ubuntu 18.04 Update repo... Get latest upgrades with "sudo apt dist-upgrade".
    Alternatively, there is a [Kernel update script](https://github.com/pimlie/ubuntu-mainline-kernel.sh)
    available that helps fetching and installing different Linux Kernels
    from the Ubuntu Kernel PPA.
    * Ubuntu 20.04 already comes with Kernel 5.4.x so it supports the
    MC7000 Audio Interface out-of-the-box. A fresh install is
    recommended but you can read further how to [upgrade Ubuntu 18.04
    to 20.04](https://ubuntu.com/tutorials/tutorial-upgrading-ubuntu-desktop#1-before-you-start).
    * OpenSUSE Tumbleweed is currently on Kernel 5.6.x supporting the
    MC7000 Audio Interface.
    * Manjaro Linux 19.0 and 20.0 feature Linux Kernel 5.4.x supporting
    the MC7000 Audio Interface.

## Mapping

### How to get the mapping

For MIXXX 2.2.4 and following the mapping will be included in the
Software. You don't need to download.

The version for MIXXX 2.2.2 or MIXXX 2.2.3 is on GitHub. You need both
files so please just right click each of the links and "save link as".

  - [Denon MC7000 Mapping \*.xml
    file](https://github.com/mixxxdj/mixxx/raw/2.2/res/controllers/Denon-MC7000.midi.xml)
  - [Denon MC7000 Mapping \*.js
    file](https://github.com/mixxxdj/mixxx/raw/2.2/res/controllers/Denon-MC7000-scripts.js)

Read further [where to place the mapping
files](https://github.com/mixxxdj/mixxx/wiki/controller_mapping_file_locations)
for your system.

**You need to activate the mapping in Preferences -\> Controller -\>
chose the MC7000 mapping.**

This controller is made for Serato DJ and most of the mapping is made
for MIXXX accordingly. Anyhow, there are several differences for
functions not matching the Serato mapping. If you have any wishes to
improve the mapping, then please discuss it in the [Denon MC7000
Mapping](https://mixxx.discourse.group/t/denon-mc7000-mapping/18235) thread.

### User Variables

Please check the \*.js mapping file for user variables to:

  - activate NeedleDrop sensor while a track is playing (default: false)
  - set the Pitch Fader ranges in % to toggle between them (default: 4,
    6, 10, 16, 24)
  - Platter Ring LED mode: single LED on or off (default: 1). Can be
    switched with SHIFT + Deck button
  - Vinyl Mode on or off at MIXXX start which also triggers the Platter
    Ring LED function (default: 1)
  - Scratch Parameters (default: 33.3, 1/10, 1/10/32)
  - Jog Parameters (default: 30, 3)

### Layout and functions

[[/media/denonmc7000-layout.png]]

1\. **Input Selector:** Set this switch to the desired audio source from
this channel. Channel’s controls will only send MIDI information when
its input selector is set to USB.

2\. **USB Selector:** Press this button to select whether the deck is
controlling the computer connected to USB Port 1 or USB Port 2. If only
one USB Port is connected the controller activates this automatically.

3\. **Channel Level:** Turn this knob to adjust the level of the
pre-fader, pre-EQ audio signal for the channel.

4\. **Channel Level Meters:** These LEDs display the audio signal level
of the channel as in MIXXX GUI.

5\. **Channel EQ:** Turn these knobs to boost or cut the high,
mid-range, and low frequencies for the channel.

6\. **Channel Filter:** Turn this knob to adjust the filter applied to
the channel. Turn the knob counterclockwise to apply a low-pass filter.
Turn the knob clockwise to apply a high-pass Filter.

7\. **Channel Cue:** Press this button to send the channel’s pre-fader
signal to the headphones’ cue channel.

8\. **Channel Fader:** Use this fader to adjust the channel’s volume
level.

9\. **Crossfader Assign:** Routes the audio playing on the corresponding
channel to either side of the crossfader (L or R), or bypasses the
crossfader and sends the audio directly to the program mix (center,
Thru).

10\. **Crossfader:** Use this crossfader to mix between the left and
right decks.

11\. **Channel FX:** Use these buttons to apply Effect A and/or B to the
corresponding channel.

12\. **Sampler Volume:** Turn this knob to adjust the volume level of
the software’s sampler. If the volume is set to 0 then the Sampler banks
are hidden, otherwise shown.

13\. **Master Level Meters:** These LEDs show the Master Audio signal
(hardware). **They will not match with the Master Level in MIXXX.**

14\. **Master Level:** Turn this knob to adjust the volume level of the
master outputs (hardware).

15\. **Booth Level:** Turn this knob to adjust the volume level of the
booth outputs (hardware).

16\. **Mic On/Off:** Press this button to activate/deactivate the
microphones (hardware).

17\. **Mic Level:** Turn these knobs to adjust the volume levels of the
corresponding microphone inputs (hardware). The Peak light next to each
knob indicates the current signal level by its color: green (low), amber
(normal/optimal), or red (maximum/peak).

18\. **MIC settings: Left Deck:** *Mic EQ:* Turn these knobs to boost or
cut the high and low frequencies for Mic 1. **Right Deck:** *Tone:* Turn
this knob to adjust the tone of the Mic 2 audio signal. *Mic Echo
Level:* Turn this knob to adjust the amount of the echo effect on the
microphones’ audio signal. This works on both: Mic 1 and Mic 2.

19\. **MIC switch: Left Deck:** Talkover/Post: Press this button to use
the “talkover” feature, which automatically reduces the volume level of
the master mix when you speak into the microphones. Press and hold Shift
and then press this button to activate/deactivate the “post” feature.
When on, the microphones’ signal will be sent to the Booth Outputs. When
off, the microphones’ signal will not be routed to the Booth Outputs.
**Right Deck:** Echo On/Off: Press this button to activate or deactivate
the echo effect on the microphones’ audio signal.

20\. **Phones Level:** Adjusts the volume of the headphones (hardware).

21\. **Phones Mix:** Adjusts the software’s audio output to the
headphones, mixing between the cue output and the master mix output
(hardware).

22\. **Split Cue:** When this switch is in the On position, the
headphone audio will be “split” such that all channels sent to cue
channel are summed to mono and sent to the left headphone channel and
the master mix is summed to mono and sent to the right channel. When the
switch is in the Off position, the cue channel and master mix will be
“blended” together.

23\. **Deck:** Selects which deck in the software is controlled by that
hardware deck. The left deck can control Deck 1 or 3; the right deck can
control Deck 2 or 4.

24\. **Shift:** Press and hold this button to access secondary functions
of other controls.

25\. **Sync / Sync Off:** Press this button to automatically match the
corresponding deck’s tempo with the tempo and phase of the opposite
deck. Press again to deactivate Sync. Hold this button down for one sec
to permanently match the tempo.

26\. **Cue / Track Start:** During playback, press this button to return
the track to the cue point. If a cue point is not set yet, then press
this button to set it at the current track position. If the deck is
paused, press and hold this button to play the track from the cue point.
Release the button to return the track to the cue point and pause it. To
continue playback without returning to the cue point, press and hold
this button and then press the Play button, afterwards release cue
button. Press and hold Shift and then press this button to return to the
start of the track.

27\. **Play/Pause / Stutter:** This button pauses or resumes playback.
Press and hold Shift and then press this button to “stutter-play” the
track from the last set cue point.

28\. **Platter:** This capacitive, touch-sensitive platter controls the
audio playhead when the wheel is touched and moved. When the Vinyl
button is on, move the platter to “scratch” the track as you would with
a vinyl record. When the Vinyl button is off (or if you are touching
only the side of the platter), move the platter to temporarily adjust
the track’s speed.

29\. **Stop Time:** Controls the rate at which the track slows to a
complete stop (“brake time”) during backspin.

30\. **Vinyl:** Press this button to activate/deactivate a “vinyl mode”
for the platter. When activated, you can use the platter to “scratch”
the track as you would with a vinyl record.

31\. **Pitch Fader:** Move this fader to adjust the speed (pitch) of the
track. You can adjust its total range with the Pitch Bend buttons.

32\. **Pitch Bend –/+:** Press and hold one of these buttons to
momentarily reduce or increase (respectively) the speed of the track.
Press and hold Shift and then press one of these buttons to set the
range of the Pitch Fader to values of 4%, 6%, 10%, 16% and 24%. Can be
customized within the \*.js file.

33\. **Key Lock / Key Sync:** Press this button to activate/deactivate
Key Lock. When Key Lock is activated, the track’s key will remain the
same even if you adjust its speed. Press and hold Shift, and then press
this button to automatically match the corresponding deck’s key with the
key of the opposite deck.

34\. **Key Select/Reset:** Turn this knob to raise or lower the key of
the track. Press this knob to reset the track’s key to its original key.

35\. **Pads:** Performance PADs have different functions based on the
PAD Mode described below.

36\. **Cue / Cue Loop / Flip:**

  - HOT CUE: Push a Performance PAD to set or play a HOT CUE. Press and
    hold Shift to delete HOT CUE.
  - *This section needs further development.* **HELP APPRECIATED**

37\. **Roll / Saved Loop:**

  - ROLL Mode lets you repeat a number of beats while keep pushing the
    PAD button down. From first to 8th PAD button the loop size is set
    as 1/16, 1/8, 1/4, 1/2, 1, 2, 4 and 8 beats. The SLIP function
    remains active so that the track continues at the position where it
    had been playing forward the whole time.
  - *This section needs further development.* **HELP APPRECIATED**

38\. **Slicer / Slicer Loop:**

  - SLICER Mode is set as beatjump only (way different to Serato). The
    first row buttons jump forward by 1, 2, 4 and 8 beats. The 2nd row
    buttons jump backward by 1, 2, 4 and 8 beats.
  - *This section needs further development.* **HELP APPRECIATED**

39\. **Sampler / Velocity Samp.:**

  - SAMPLER: 8 samplers can be triggered from either Deck. Add samplers
    to the sampler bank pushing a PAD button. If a sampler is loaded
    then the push will start the sampler, push again while playing will
    replay the track from start. Press and hold SHIFT and push a PAD
    button to stop a sampler while playing or eject a sampler when
    stopped.
  - *This section needs further development.* **HELP APPRECIATED**

40\. **Auto-Loop/Reloop:** Press this button to create an auto-loop with
the length of 4 beats. You may change the length of beats by using the
1/2 or X2 buttons. Press and hold Shift and then press this button to
toggle the current loop on or off. If the loop is ahead of the current
play position, the track will keep playing normally until it reaches the
loop.

41\. **X 1/2 Loop / Loop In:** Press this button to halve the length of
the current loop. Press and hold Shift and then press this button to
create a Loop In point at the current Location.

42\. **X 2 Loop / Loop Out:** Press this button to double the length of
the current loop. Press and hold Shift and then press this button to
create a Loop Out point at the current Location.

43\. **\< / \> Param 1/2:** These are currently used to beat jump
backward or forward by 8 beats. Press and hold Shift and then press
these buttons jumps 32 beats. *This section needs further development.*
**HELP APPRECIATED**

44\. **Slip:** Press this button to enable or disable Slip Mode. In Slip
Mode, you can jump to cue points, trigger loop rolls, or use the
platters, while the track’s timeline continues. In other words, when you
stop the action, the track will resume normal playback from where it
would have been if you had never done anything (i.e., as if the track
had been playing forward the whole time).

45\. **Censor / Rev:** Press this button to activate the Backspin
feature. If the track did not stop yet then when you release the button,
normal playback will resume. Press and hold Shift and then press this
button to reverse the playback of the track. The original CENSOR
function (as in Serato) can be manually triggered by activating SLIP
followed by SHIFT + CENSOR.

46\. **Adjust/Set:** Press this button to adjust the Beat Grid to the
current location.

47\. **Slide/Clr:** Press this button to adjust the Beat Grid to another
playing track.

48\. **Select/Load Knob:** Turn this knob to navigate through lists.
Press and hold Shift and then turn this knob to browse quickly through
the tracks in your library. Press the left side button to load a track
into the active Deck (1 or 3), press the right side button to load a
track into the active Deck (2 or 4). Press and hold Shift and push the
knob to open folders on the left side of the library.

49\. **Sort:** *will be implemented with MIXXX 2.3*

50\. **Back/Fwd/Sort BPM:** Press this button to move to the previous
window. Press and hold Shift and then press this button to move to the
next window. *MIXXX 2.3: Press and hold Sort and then press this button
to sort the tracks by BPM.*

51\. **Load Prep/Open Prep/Sort Key:** Press this button to load the
currently selected track to the Preview Deck. Press and hold Shift and
then press this button to start the track in Preview Deck. *MIXXX 2.3:
Press and hold Sort and then press this button to sort the tracks by
key.*

52\. **Files/History/Sort Artist:** Press this to maximise the library.
*MIXXX 2.3: Press and hold Sort and then press this button to sort the
tracks by artist.*

53\. **Panel/View/Sort Title:** Press this to open and close the FX
section inside the GUI. *MIXXX 2.3: Press and hold Sort and then press
this button to sort the tracks by title.*

54\. **Needle Drop Strip:** The length of this strip represents the
length of the entire track. Place your finger on a point along this
sensor to jump to that point in the track. Press and hold Shift to jump
to a position while a track is currently playing.

55\. **FX On / Select:** Press this button to turn the corresponding
effect on or off. Press and hold Shift and then press this button to
select an effect from the list that was enabled in the MIXXX Properties
FX section.

56\. **FX Level:** Turn this knob to adjust the level of the
corresponding effect. The FX On button under the knob must be lit for
this knob to function.

57\. **FX Beats:** Turn this knob to adjust the Wet/Dry rate of the
effects.

58\. **FX Tap:** Press this button will activate effects for the Master
Signal instead of the individual Decks. Press and hold Shift and then
press this button to have the effects also on the Headphone preview.

Front Panel. **Crossfader Contour:** Adjusts the slope of the crossfader
curve. Turn the knob to the left for a smooth fade (mixing) or to the
right for a sharp cut (scratching). The center position is a typical
setting. This seams to have a very minor effect in MIXXX.

### LEDs

The Channel Volume Meters matches to the ones shown in MIXXX GUI. Only
when clipping the red LED illuminates.

As mentioned before the Master Volume Meter is not correlated to MIXXX
GUI as the controller handles that in Hardware.

Button LEDs are fully mapped for the first function. As you press and
hold Shift then the secondary function has only got some mappings, e.g.
flashing TAP and KEY SYNC when activated.

Platter Ring LEDs are correlated with the VINYL button.

  - If VINYL Mode is set ON then the LED follows the 33.3 rpm value and
    is correlated with the platter movement too.
  - If VINYL Mode is set OFF the current track position is indicated by
    the Platter LEDs starting at the top.
