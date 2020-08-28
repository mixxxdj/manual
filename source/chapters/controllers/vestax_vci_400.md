# Vestax VCI-400

[[/media/vci-400dj_layout2.png|vci-400dj\_layout2.png]]

The Vestax VCI-400 is a 4 deck controller. It has an integrated audio
interface with balanced outputs (XLR and 1/4" TRS), two pairs of RCA
inputs, and two XLR / 1/4" combination microphone inputs. The microphone
inputs can be sent to the computer for recording and broadcasting. The
RCA inputs do not have phono preamps and do not work for vinyl control.
The VCI-400 requires its own power supply; it does not run on USB bus
power.

Vestax went out of business in 2014.

## Compatibility

The original VCI-400 firmware has a bug that prevents the sound card
from working with Linux. Now that Vestax is out of business, drivers and
firmware for Vestax devices are hosted on [Serato's
website](https://support.serato.com/hc/en-us/articles/203593924-Vestax-Hardware-Drivers-and-Firmware).
If your VCI-400's sound card does not appear as an available device
using Linux, use the firmware updater on a computer running Windows or
Mac OS X. This will only need to be done once and then the controller
will continue to work with Linux.

Note that the VCI-400 and VCI-400 Ean Golden Edition are incompatible.
Their firmwares use different MIDI messages to communicate with the
computer. Unfortunately, [it is not possible to switch between the
VCI-400 and VCI-400 EGE
firmware](http://forum.djtechtools.com/showthread.php?t=64071&p=572022&viewfull=1#post572022).

## Mapping

The VCI-400 mapping for Mixxx is based on the Serato Limited Edition
overlay.

**For regular use, make sure the "mixer select" switches are all the way
to the left.** If you move them to the right, the Play / Cue buttons
will be used to select vinyl control modes instead.

Most of the functions are exactly as they appear on the overlay, and the
overlay is very nicely labeled so that's the best place to start.

The four small buttons below the grouping of 8 buttons selects which
mode the 8 buttons are in, either Hot Cues, Loops, Rolls, or Samples.
Mixxx remembers which mode is selected on a per-deck basis, so when you
toggle the deck-selection switches the mode may change. The button
corresponding to the current mode will be lit so you know what mode
you're in.

Button Modes:

  - In Hot Cue mode, the 8 buttons will move Mixxx to the designated
    hotcue. If you hold the shift button, the hotcue will be cleared.
  - In Loop mode, the 8 buttons will create a new loop at the current
    position from size 32nd note to 16 beats.
  - In Roll mode, holding any of the buttons will temporarily create a
    loop anywhere from 32nd note to 16 beats.
  - In Sampler mode, both sides of the controller launch the same set of
    8 samplers. Holding shift will eject a sample.

Some of the buttons have special functions in Mixxx:

1.  The Vinyl / Slip button. While pushed, the jog wheel is in
    scratching mode (similar to if you push down on the platter). If you
    hold this button while spinning the jog wheel, you can let go of the
    wheel and Mixxx will still be in scratch mode. Great for backspins.
2.  The Param knob can be used to adjust the musical key of the current
    track. Twist to make the tone higher or lower. If you hold the shift
    button (3), use this knob to scroll quickly through the track.
    Pushing this knob will reset the key.
3.  Shift button
4.  Auto Loop knob. Twisting this will change the size of the current
    loop, either doubling or halving the size. If you hold shift (3),
    twisting this knob will move the loop left or right by 1 beat per
    click. Pushing this knob will enable or disable looping.
5.  The Master FX button enables the 1st FX bank to be applied to the
    master output.
6.  The FX Mode button toggles which effect is in the first FX bank.
7.  Controls FX1 Parameter 1
8.  Controls FX1 Parameter 2
9.  Controls FX1 Parameter 3
10. Controls FX1 Dry / Wet
11. Enable/Disable Quantize Mode.
12. Enable/Disable Keylock

The four small buttons in the center, Area, Panel, Back, and Prepare,
don't do anything. Neither does the sampler volume slider.

Some additional functions are accessible with the shift button:

  - Shift + Load to eject a track.
  - Shift + Play while the deck is playing does a breaking stop.
  - Shift + Censor does a spinback stop.

### Vinyl Control Mode

If you want to use vinyl control instead of the jog wheels, you can move
the mixer selection switches all the way to the right. In this mode, the
Play button becomes a Vinyl Control Enable/Disable button, and the Cue
button selects which Vinyl Control mode is active -- Absolute, Relative,
or Constant. The cue button lights up when Absolute is selected.

### Note about VU Meters

There's a bug in the way that the VCI400 firmware works -- although
Mixxx can control the VU meters, the VCI's internal soundcard always
*also* controls the VU Meters. This can result in an odd flickering
effect that looks strange. For this reason, the Master VU meters are
disabled by default. If you've installed the firmware that allows decks
C and D to act as pass-through mixer channels, you may see flickering
there too.
