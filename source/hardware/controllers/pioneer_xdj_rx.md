# Pioneer-XDJ-RX

<https://www.pioneerdj.com/en/product/all-in-one-system/archive/xdj-rx/black/overview/>

![](https://www.pioneerdj.com/-/media/pioneerdj/images/products/all-in-one-system/xdj-rx/black/xdj-rx-main.png?h=768&w=1024&hash=ED833BBB74C84C859FB673CF01986313765E9BC8)

## Controller description
This device can work as a stand alone system. Users are supposed to prepare flash drive(s) with Rekordbox software, and connect those to the device. Luckily, it also works as MIDI device, thus this mapping is possible.
Unfortunately, XDJ-RX doesn't have MIDI OUT, which means, it is not possible to control LEDs via MIDI signals, and those won't flash, go on/off. What the author of the mapping personally will miss, and that was one of the main reasons to buy this exact model - LED animation on a jog wheel, which shows that this "turntable" is currently playing.

## Incompatibilities
If you are a Linux user, currently Linux (ALSA) doesn't recognize XDJ-RX's soundcard, and will unlikely recognize. So for previews via headphones, another sound card is necessary: one card for your master output, let's say your laptop card, and other card to route previews to your headphones.

## Differences
When using this mapping, some pads are used differently than when XDR-RX works in standalone mode: you put hot cues by using hot cue buttons, but you clean them, by pressing same buttons with 'shift'.

Quantize button is one for all decks on XDJ-RX, while Mixxx has the separate quantize buttons for each deck.

Mixxx has the super effect button, which controls all the selected effects. XDJ-RX cannot mix so called "sound color fx", i. e. "gate/comp", "filter", "noise", "crush" with each other - the blue buttons on the left side of the mixer. The same effect is chosen for both channels. However you can mix one of "color fx" with one (and only one) of the effects, located on the right side of the mixer - echo, spiral, flanger, pitch, etc.

In Mixxx, you can use several (and any) effects simultaneously. For that you select some effects (well, choose and add those first), and then use super knob to manipulate em all.

In this mapping Loop slice buttons are used to enable-disable (chosen) effects, and then one must use the color fx knob as a super knob.

tempo button changes the tempo slider diapason as:

-3 to +3 BPM,

-6 to +6 BPM,

-12 to +12 BPM.

## Temporary information
While the mapping is not added to Mixxx, you can get it from https://github.com/norayr/xdj-rx-mixxx-mapping
