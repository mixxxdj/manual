# Electrix Tweaker
![http://electrixpro.com/wp-content/uploads/2014/09/Tweaker-Angle-570x380.jpg](http://electrixpro.com/wp-content/uploads/2014/09/Tweaker-Angle-570x380.jpg)

  - [Manufacturer's website](http://electrixpro.com/)
  - [Forum topic](http://mixxx.org/forums/viewtopic.php?f=7&t=7189)
  - [Manufacturer's
    manual](http://electrixpro.com/wp-content/uploads/2014/10/Tweaker_User_Manual.pdf)
  - [Blank template
    image](https://www.google.com/search?q=lib/exe/detail.php/hardware:tweaker-blank-template.svg&btnI=lucky)

The Electrix Tweaker is an unconventional MIDI controller that can
control most aspects of Mixxx. Instead of jog wheels, it fits an 8x4
grid of multicolor backlit buttons, 8 velocity-sensitive buttons, and 6
push encoders with LED rings into a relatively small package. It does
not have a built in sound card, so it requires a [separate sound
card](hardware%20compatibility#usb%20sound%20cards) or [splitter
cable](hardware%20compatibility#splitter%20cables) (although it does
include 5-pin MIDI in and out ports).

The mapping is included with Mixxx starting with Mixxx 2.0.

## Compatibility and setup

The Tweaker is a USB MIDI class compliant device, so it does not require
any special drivers on any operating system. Just plug it in and load
the Mixxx mapping on any OS that Mixxx runs on.

Use it with the Tweaker MIDI 1 port (Tweaker MIDI 2 is the 5-pin MIDI
I/O on the Tweaker).

## Reviews

  - [DJ Tech
    Tools](http://djtechtools.com/2012/09/27/review-electrix-tweaker-midi-performance-controller/)
  - [Digital DJ
    Tips](http://www.digitaldjtips.com/2013/01/electrix-tweaker-review-video/)
  - [DJWORX](http://djworx.com/review-electrix-tweaker-dj-controller/)
  - [Magnetic
    Mag](http://www.magneticmag.com/2013/03/gear-review-electrix-pro-tweaker-dj-controller/)
  - [Crossfadr](http://www.crossfadr.com/2013/05/10/tweaking-knobs-on-the-electrix-tweaker/)
  - [Core Mag TV](https://www.youtube.com/watch?v=Tk-I_lJfxys)

## Mapping description

### Global controls

[[/media/hardware/Tweaker-global-controls.svg|Tweaker-global-controls.svg]]

    -Scroll through library. Press to toggle big library view -Scroll up left panel of library -Scroll down left panel of library -Samplers
    * Off when empty, red when loaded
    * Press a button to load the selected sample into a sampler and play it
    * Press a button to play a sample. When the button is released, the sample will stop playing.
    * Press [[#top-shift-layer|top shift]] and a sampler button to eject a sample from a sampler
    * Samples will play with their volume proportional to how much force was used to strike the button. You can adjust the sensitivity or disable the velocity sensitivity (and make them work as on/off switches) by adjusting options at the top of the JavaScript file in a text editor.
    -Crossfader

### Top shift layer
[[/media/hardware/Tweaker-top-shift.svg|Tweaker-top-shift.svg]]

This layer is active while the top shift button (\#1 in the diagram) is
held down.

With the exception of the headphone mix encoder (\#8 in the diagram),
pressing the encoders 7-12 resets them to center.

  - Top shift button
  - Eject left deck
  - Eject right deck
  - Expand/collapse selected item in left library pane
  - Expand/collapse selected item in left library pane
  - Scroll through library quickly. Push to load selected track into first stopped deck.
  - Headphone gain
  - Headphone cue/master mix in headphones. Press to toggle split cue mode. The blue LED below encoder is lit when split cue mode is enabled.
  - Channel gain for active deck on left side
  - Master output gain
  - Master output balance
  - Channel gain for active deck on right side
  - Eject sampler
  - Delete hotcue
  - Deck shift button. Press to enable [[#vinyl timecode mode]] on the deck that is active on the left side (press top shift button first, then this button while holding down top shift)
  - Deck shift button. Press to enable [[#vinyl timecode mode]] on the deck that is active on the right side (press top shift button first, then this button while holding down top shift)

### Deck controls

[[/media/hardware/Tweaker-deck-controls.svg|Tweaker-deck-controls.svg]]

The deck controls are the same on each half of the controller. Which
deck each side controls can be switched with the deck toggle button,
labeled \#11 in the diagram. When controlling deck 1 or 2, the switches
on that side (9, 11, 13, 14, and 15 in the diagram) are blue when
enabled, as shown on the left side of the diagram. When controlling deck
3 or 4, the switches on that side are magenta when enabled, as shown on
the right side of the diagram.

  - Filter (low pass filter left of center; high pass filter right of center)
  - Load track selected in library into deck
  - Toggle encoders between EQ and loop mode (see [[#channel-encoder-layers|below]])
  - Headphone cueing
  - Volume
  - Play/pause
  - Hotcues. Press an unlit button to set a hotcue. When slip mode is disabled (see #9 below), pressing a hotcue simply jumps to that hotcue. When slip mode is on, hotcues can be previewed on a stopped deck. While previewing a hotcue, press the play button to let the track keep playing after the hotcue is released. Pressing a hotcue while a deck is playing and slip mode is on will jump to the hotcue then jump back to where the track would have been once the last hotcue button is released.
  - Jump 4 beats forward (with quantize enabled)
  - Slip mode. When active, loops and hotcues will only play as long as they are held down. When they are released, the track will jump to where it would have been if the loop or hotcue was not pressed. 
  - [[#deck-shift-layer|Deck shift]]
  - Deck toggle between decks 1 & 3 on the left and decks 2 & 4 on the right.
  - Jump 4 beats backward (with quantize enabled)
  - Quantize. In addition to snapping cues, loops, and play button presses to the nearest beat, this changes the behavior of the controller's navigation buttons. When enabled, the navigation buttons are white as shown by 8 & 11 in the diagram. With quantize enabled, the navigation buttons jump by 4 beats or 1 beat with [[#deck-shift-layer|deck shift (#10)]] pressed. When disabled, the navigation buttons are green as shown by 15 & 16 in the diagram. With quantize disabled, the navigation buttons fast forward and rewind the track. When quantize is disabled and deck shift is pressed, the navigation buttons are temporary pitch bend buttons.
  - Key lock
  - Sync lock
  - Fast forward (with quantize disabled)
  - Rewind (with quantize disabled)

### Deck shift layer

[[/media/hardware/Tweaker-deck-shift.svg|Tweaker-deck-shift.svg]]

This layer is active while the yellow deck shift button on that side of
the controller is held down.

  - Pitch (only adjusts tempo with keylock on)
  - Jump 32 beats forward or backward
  - Scroll through hotcue pages. The pages are color coded, in order, cyan, green, red, and white. The LED around the encoder indicates the hotcue page number. The active page on a deck is remembered when toggling between decks (see [[#deck-controls|deck controls (#11)]] above).
  - Exit loop
  - Volume
  - Cue. When previewing from the cue point on a stopped deck, release this cue button to stop playing and jump back to the cue point. Release deck shift to continue playing.
  - Move hotcue to current position
  - Jump forward 1 beat (with quantize enabled, see [[#deck-controls|deck controls #13]])
  - Manually place loop start point
  - Deck shift button
  - Manually place loop end point
  - Jump back 1 beat (with quantize enabled, see [[#deck-controls|deck controls #13]])
  - Align beatgrid with current position
  - Sync key. If key has been changed from track's original key, reset the key.
  - Reset tempo
  - Temporarily raise pitch while pressed (with quantize disabled, see [[#deck-controls|deck controls #13]])
  - Temporarily lower pitch while pressed (with quantize disabled, see [[#deck-controls|deck controls #13]])

### Channel encoder layers

[[/media/hardware/Tweaker-encoder-layers.svg|Tweaker-encoder-layers.svg]]

The encoder layer buttons (\#4 and \#8 in the diagram) toggle the
encoders between EQ and loop layers.

The left side of the diagram shows EQ mode. In EQ mode, pressing
encoders toggles that EQ's kill switch. The blue LED below the encoder
is lit while the kill switch is on. Pressing the encoder while holding
deck shift (see [deck controls \#10](#deck-controls)) resets the EQ to
center.

Tip: You can go to Options \> Preferences \> Equalizers and check "Reset
equalizers on track load". On most controllers, this would be an issue
because the physical knobs would be misaligned with the values in
software when the EQs were reset, but because the Tweaker has LED rings
around encoders instead of knobs, this is not an issue.

The right side of the diagram shows loop mode. The LEDs on the loop move
length and loop length encoders represent numbers of beats. Center means
1 beat. Each step to the right doubles the beats and each step to the
left halves the beats. For example, the default loop length is 4 beats,
so the center LED and 2 LEDs to the right are lit (2 x 2 = 4).

  - High EQ
  - Mid EQ
  - Low EQ
  - Encoder mode button. Press to switch to loop mode.
  - Loop move length
  - Move loop
  - Loop length. Press to toggle loop. When in slip mode (see [[#deck-controls|deck control button #9]]), the loop is only active while this is held down. The blue LED below the encoder is lit while a loop is active.
  - Encoder mode button. Press to switch to EQ mode.

### Vinyl timecode mode

[[/media/hardware/Tweaker-vinyl-mode.svg|Tweaker-vinyl-mode.svg]]

Toggle vinyl timecode mode by pressing deck shift (\#2 in the diagram)
while holding top shift (\#1 in the the diagram). This replaces the
navigation buttons for that deck with buttons that toggle options for
timecode control.

3: cycle through vinyl control modes: absolute (LED off), relative (LED
indicates cue mode), and constant (LED red). If the deck is in relative
mode and playing, pressing the button cycles through cue modes: off
(white), cue (yellow), hotcue (green). When the deck is playing in
relative mode, pressing the button with deck shift (\#2) switches to
constant mode.

4: toggle vinyl control. Turns green when vinyl control is enabled. With
deck shift (\#2) pressed, it toggles passthrough mode and turns white.
Pressing the button while passthrough mode is enabled turns passthrough
mode off (without toggling whether vinyl control is enabled).
