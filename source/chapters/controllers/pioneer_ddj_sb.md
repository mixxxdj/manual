# Pioneer DDJ-SB

![https://pdj-ecom-cdn.azureedge.net/-/media/pioneerdj/images/products/controller/ddj-sb/black/ddj-sb-main.png](https://pdj-ecom-cdn.azureedge.net/-/media/pioneerdj/images/products/controller/ddj-sb/black/ddj-sb-main.png)

``` 
 *[[http://www.pioneerdj.com/en/product/controller/ddj-sb/|Manufacturer's product page]]
 *[[http://mixxx.org/forums/viewtopic.php?f=7&t=6886|Forum thread]]
 *[[https://github.com/mixxxdj/mixxx/pull/663|GitHub pull request]]
```

The Pioneer DDJ-SB is an all-in-one 2 deck USB MIDI controller with a
built in soundcard. Mixxx allows it to control 4 decks. It is compatible
with Mixxx since version 1.12.

## Drivers

### Windows

Windows Vista, Windows 7 and Windows 8 are supported. You can download
the latest drivers and firmware from
<http://www.pioneerdj.com/en/support/software/ddj-sb>.

**<span class="underline">IMPORTANT for Windows users</span>**: If you
are having issues getting both sound outputs to work properly, please
try using a different Sound API (see the Preferences menu). DirectSound
seems to have issues with this controller. WASAPI seems to work fine, as
does MME, although only with higher latencies. On Windows 10, only MME
works.

### Mac OS X & Linux

You don't need any drivers on Mac OS X and Linux.

The controller supports Mac OS X 10.6 and up.

## Usage

### Library browsing

The controls for library browsing can be found in the center top of the
controller.

| Control                     | Function                                                                                                                                              |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rotary knob                 | Track selection                                                                                                                                       |
| Load buttons                | Loads currently highlighted track to the corresponding deck                                                                                           |
| Pushing rotary knob         | Push: Loads currently highlighted track to the preview deck and plays it. -- Release: jump to 30% position -- Push again without rotary: Stop preview |
| Shift + rotary knob         | Library section selection                                                                                                                             |
| Shift + pushing rotary knob | toggle expanding library section                                                                                                                      |

### Switching between decks

Pressing shift + "key lock / tempo range" allows the left deck to switch
between decks 1 and 3 and the right deck to swicth between decks 2 and
4.

### Volume, equalizers & filters

Between the decks the usual faders, crossfader and EQ knobs can be
found. A filter knob is also available.

Knobs are available for the master and headphones level. These are
functional but are not reflected in Mixxx, as they control the
controller's soundcard directly.

The filter fade button allows to use the crossfader in an innovative way
that fades accross songs through filtering instead of fading.

There is no trim/gain knob, but the same effect can be achieved by using
the filter knobs while holding shift.

### Jogwheels, tempo & vinyl mode

When a deck is paused, the jogwheel allows you to browse through a
track. If you want to browse faster, hold shift while using the
jogwheel.

When a deck is playing, using the jogwheel allows you to temporarily
change the tempo of the playing track. Again, holding shift exaggerates
this effect.

The tempo slider allows changing the tempo of each deck. This normally
changes the pitch of a track, you can make the pitch stay constant by
pressing the "key lock / tempo range" button.

Vinyl mode makes the jogwheels emulate the way turntables work. Vinyl
mode can be toggled by pressing the "vinyl / slip" button. Touching the
outer plastic ring of the jogwheel will make it behave as with vinyl
mode off. Touching the metal disc simulates touching the vinyl record,
so just putting your hand on it will stop the "vinyl". You can scratch
in a similar way as with turntables in vinyl mode.

### Slip mode

By pressing shift + "vinyl / slip" you can toggle slip mode. When
entering slip mode, Mixxx remembers what point exactly of the track
should be playing even if, for example, you scratch or make a loop. This
allows to return to the original pace of the track.

### Pads - lower row

The play and cue pads should be self-explaining. The sync pad toggles
master sync for a deck, which tries to beatmatch the deck with the
others, and also syncs the tempo between them, even when the tempo of
one deck is changed.

Additional functions can be accessed by holding shift

| Control      | Function                                                                                              |
| ------------ | ----------------------------------------------------------------------------------------------------- |
| Shift + play | Plays the track in reverse and enables slipping (see slip mode)                                       |
| Shift + cue  | Brakes the track as if the power of the motor on a turntable was turned off                           |
| Shift + sync | Enables quantize mode (this makes most actions, e.g. setting the cue point, fall to the nearest beat) |

### Pads - hot cue mode

In hot cue mode the upper row of pads control the hotcues. Pressing a
pad that is not lit sets a hotcue. Pressing a pad that is lit makes the
track jump and play from that hotcue. Pressing a pad while holding shift
deletes that hotcue.

You can control a set of 4 more hotcues by pressing shift + hot cue. The
hot cue button will start blinking. The pads will behave in the same
way, but controlling hotcues 5 to 8.

### Pads - auto loop mode

Pressing the pads in auto loop mode will make loops of a specific length
measured in beats.

| Control       | Function     |
| ------------- | ------------ |
| Pad 1         | 1 beat loop  |
| Pad 2         | 2 beat loop  |
| Pad 3         | 4 beat loop  |
| Pad 4         | 8 beat loop  |
| Shift + pad 1 | 16 beat loop |
| Shift + pad 2 | 32 beat loop |
| Shift + pad 3 | 64 beat loop |

### Pads - manual loop mode

This mode will make the pads control looping in the way labeled on them.

| Control       | Function                    |
| ------------- | --------------------------- |
| Pad 1         | Set loop in                 |
| Pad 2         | Set loop out                |
| Pad 3         | Toggles loop                |
| Pad 4         | Halve loop length           |
| Shift + pad 4 | Double loop length          |
| Shift + pad 1 | Move loop one beat backward |
| Shift + pad 2 | Move loop one beat forward  |

### Pads - sampler mode

In sampler mode the sampler can be controlled. To load a file into a
sampler, first press the sampler button while holding shift, so that the
sampler button starts blinking. Now pressing a pad will load the
currently highlighted track on the library into the corresponding
sampler. Pressing a pad while holding shift will eject the sample.

To play samples, press the sampler button without holding shift (it
should not blink). Pressing a pad will start playing the corresponding
sample, pressing a pad while holding shift will stop it.

### Pads - loop roll (shift + auto loop)

By pressing the auto loop button while holding shift (it should start
blinking) you can make loop rolls. This mode combines auto loops with
slip mode. The pads will start a loop in the current position with a
determinate beat length while simultaneously enabling slip mode, so that
when releasing the pad the track will continue playing as if the loop
never happened.

| Control       | Function              |
| ------------- | --------------------- |
| Pad 1         | 1/16th beat loop roll |
| Pad 2         | 1/8th beat loop roll  |
| Pad 3         | 1/4th beat loop roll  |
| Pad 4         | 1/2 beat loop roll    |
| Shift + pad 1 | 1 beat loop roll      |
| Shift + pad 2 | 2 beat loop roll      |
| Shift + pad 3 | 4 beat loop roll      |
| Shift + pad 4 | 8 beat loop roll      |

### Pads - kill (shift + manual loop)

By pressing the manual loop button while holding shift (it should start
blinking) you can make the pads behave as kill switches.

| Control | Function  |
| ------- | --------- |
| Pad 1   | Kill low  |
| Pad 2   | Kill mid  |
| Pad 3   | Kill high |
| Pad 4   | Mute      |

### Effects

Over the jogwheels there are sections allowing to control effects.

Turning the knobs will control the wet/dryness of an effect.

Turning the knobs while holding one of the three FX buttons will control
the first, second or third parameter of an effect, respectively.

If holding shift when using the knobs the "super" parameter can be
controlled.

Pressing the central FX button (number 2) while holding shift will
toggle the effect for the headphones, while the left and right buttons
(number 1 and 3) will toggle the effect for the active deck in the left
and right sides of the controller respectively.

You can choose between effects by entering "kill mode" and using pads 1
and 2 while holding shift.

### Channel fader start

By moving a channel fader up from the very bottom while holding shift
when a deck is paused, the deck will start playing. Moving the fader
back to the bottom without releasing shift stops the deck and moves it
back to its original position.
