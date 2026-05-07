# Faderfox DJ44

![](../../_static/controllers/hardware/faderfox_dj44_01-2.jpg)
![](../../_static/controllers/hardware/faderfox_dj44_02-2.jpg)
![](../../_static/controllers/hardware/faderfox_dj44_03-2.jpg)

  - [Manufacturer's product page](http://www.faderfox.de/dj44.html)
  - [Forum
    thread](https://www.mixxx.org/forums/viewtopic.php?f=7&t=9366&p=33897#p33897)
  - [Manufacturer's user
    guide](http://www.faderfox.de/PDF/Manual%20DJ44%20V01.pdf)
  - [Description for hardware-implemented options in system
    mode](http://www.faderfox.de/PDF/short%20description%20DJ44%20system%20V0100.PDF)
  - [Standard mapping for
    Traktor](http://www.faderfox.de/PDF/short%20description%20DJ44%20Traktor%20Pro%202%20V01.pdf)
    \[1\]

## Description

Fully midi compliant controller, industrial style, built by hand in
Hamburg, Germany by Mathias Fuchß. Compact style for mobile DJ-ing, the
controller comes in its own carrying case. No jog wheels, scratching
(kind of) and strip search can be done via encoders. The crossfader also
is not initially built for scratching, as it runs pretty tight and
slower (but precise). Default values for Deck, FX slots and global
controls can be changed, so one can use two DJ44 devices side by side
for 4 decks.

## Mapping

Every control is sending a midi note, so the basic mapping is easy.
Javascript is needed for Loop section, scratching via encoders and
perhaps for some LED.

### Progress

v0.5: Basic mapping for Mixxx 2.0. is done via xml for essential
functions and LED. Looping display does not work so far, changing loop
size works via Shift+Button at the moment (encoder unused) and effects
sections need more attention. Quick Filter button and LED is unused at
the moment. Javascript mapping is needed for more comfort.

### Roadmap

Mixxx 2.0

  - Javascript mapping for Loop section and display, scratching, VuMeter
    perhaps.
  - Understanding effect section and filtering and effects assigning
    (not so important for me originally)
  - Better nudging (progressive possible?)
  - Check 4 deck mode - what's necessary for that?

Mixxx 2.1

  - Using new Component JS
  - Adapting effects section

### Overview (what's working?)

Graphical overview comes later, let's say, in v1?

#### Transport

  - Play/Pause with LED (static or blinking - control commands are
    documented in xml)
  - Cue (Shift+Play)
  - Fast play forward/backward (grey buttons)
  - Nudging forward/backward (dark grey buttons) - but not progressive
  - Pitch up/down, Pitch reset (encoder push)
  - Key reset (at any Pitch rate, Shift plus encoder push)
  - Hotcues 1 to 8 (clear with Shift)
  - Sync button and LED (Shift unused so far)
  - Seek encoders (push unused, should be scratching later --\>
    Javascript)

#### Mixing

  - Crossfader
  - Line fader
  - Prelisten buttons and LED
  - **unused:** VuMeter (to solve, possibly Javascript)

#### Master

  - Master volume
  - Headphones volume
  - Headphone mix

#### Library

  - Tree browsing, open/close elements (encoder push)
  - Track browsing, loading in next stopped deck via push, load in Deck
    A or B (via black buttons under track browser)
  - Load track in previews section and start play (left black button
    above tree browser)
  - Toggle library maximizing (right black button above tree browser)
  - **unused:** Shift + tree and track browsing encoders, shift + black
    buttons above tree browser/under track browser

#### Equalizer

  - Deck Gain
  - High, Mid and Low EQ
  - Kill low and mid EQ with LED (Shift = mid)
  - **unused:** Pan knobs, shift + all buttons for effects

#### Effects, filters

Mixxx 2.0 - only first two racks are mapped. The whole sections needs
more attention, since I don't use effects until today.

  - Quick filter knob
  - **unused:** button and LED for Quick filter (possibly: LED for
    effect loaded?)
  - Switch effect rack on/off
  - Next effect in Rack (Reset button used)
  - Activate effect for Master output (button 1)
  - Activate effect for Headphone output (button 2)
  - Dry/wet knob, parameter knobs 1 to 3, parameter 4 must be done via
    mouse
  - **unused**: FX assign buttons and LED (todo, what could they do...)

#### Looping

  - Loop in and out
  - Double and halve loop length (Shift plus in/out)
  - Start/Stop loop with LED (static or blinking - control commands are
    documented in xml)
  - Move loop forward/backward via Shift + dark gray transport buttons
  - **unused:** Loop encoder, loop encoder push, Shift + loop encoder
    push, loop display --\> Javascript)

<!-- end list -->

1.  link will vanish, when graphical mapping chart is available here
