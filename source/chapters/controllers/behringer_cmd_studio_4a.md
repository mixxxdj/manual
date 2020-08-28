# Behringer CMD Studio 4a

[[/media/hardware/cmd-studio-4a_p0809_top_l.png|]]

The Behringer CMD Studio 4a is a 2 deck controller that supports 4
virtual decks and has a built in 4 channel (one stereo master, one
stereo headphones) USB sound card built in.

  - [Mixxx Forum
    Thread](http://www.mixxx.org/forums/viewtopic.php?f=7&t=7868)
  - [Manufacturer's product
    page](http://www.music-group.com/Categories/Behringer/Computer-Audio/DJ-Controllers/CMD-STUDIO-4a/p/P0809/Features)
  - [Manufacturer's
    manual](https://media.music-group.com/media/PLM/data/docs/P0809/CMD-STUDIO-4A_QSG_WW.pdf)

## Mixxx Sound Hardware Preferences

  - Master output: channels 1-2
  - Headphone output: channels 3-4

## Mapping description

(This page details v1.4 of the Behringer CMD STUDIO 4a controler
mapping)

Most of the buttons and knobs on the controller behave as they are
labelled:

[[/media/hardware/cmd-studio-4a-layout.png|]]

The only major departure from the above are the 4 "FX Control" knobs and
buttons at the top of each deck.

### Mixer

  - The HIGH, MID, and LOW EQ knobs & kill buttons, deck faders,
    cross-fader, master, and headphone monitoring (mix & volume) knobs
    all operate as labelled.
  - Each deck also has a gain knob (leftmost "FX Control" knob).

### Navigation Control

  - The BROWSE knob scrolls thorough the track list in the library
    panel.
  - The BROWSE LEFT/RIGHT buttons move through the library tree (and can
    also select effects, see later).
  - The ENTER button expands/collapses library tree items.

### Deck Select Buttons

  - The deck select buttons (A, B, C, D) make the respective "virtual"
    deck active.
  - On the left deck: A = Channel 1, C = Channel 3.
  - On the right deck: B = Channel 2, D = Channel 4.

### Transport Control

  - The deck LOAD buttons will load the currently highlighted track in
    the library window into that deck.
  - The deck CUE, PLAY, SYNC, and LOOP buttons work as labelled (SYNC
    toggles master sync for the deck).

### Wheels

  - While a track is playing, spinning the wheels temporarily speeds up
    or slows down the track.
  - When a track is stopped, spinning the wheels results in a fast
    search.
  - When the top wheel surface is touched the wheels act as as a
    precision jog.
  - When the SCRATCH button is activated, moving the wheel while
    touching the top surface scratches the track.

### Hot Cue Buttons

  - If not currently set, pressing a HOT CUE button sets that hot cue at
    the current playback position.
  - If already set, pressing a HOT CUE button jumps to that hot cue
    position.
  - If the DEL button is \*held\*, pressing an already set HOT CUE
    button will clear that hot cue.
  - Tapping the DEL button toggles [\#DEL-mode](#DEL-mode). The button
    will light up blue. DEL-mode alters some of the other button
    functions like a shift button on other controllers.

### Playback Pitch/Rate

  - The pitch sliders control the pitch.
  - The PITCH BEND +/- buttons step the playback rate up or down
    (pressing both resets the rate back to normal).
  - The LOCK buttons turn on key lock so the pitch doesn't change when
    the playback rate changes.
  - The PITCH BEND button lights will indicate whether the current pitch
    is higher or lower than normal.

### FX Control Buttons

These do not control effects; they have other functions:

  - FX Control button 1 toggles the deck slip-mode on/off, (button
    lights blue when active). Slip-mode is not available in any Mixxx
    skin yet so may be unfamiliar. When slip-mode is active, playback
    continues (muted in the background) during a loop/scratch etc. Once
    disabled, playback will resume where the track would have been if
    the loop/scratch has not taken place (thus preserving the track
    beat).
  - FX Control button 2 toggles the deck repeat mode, (button lights
    blue when active).
  - FX Control button 3 can be tapped to adjust the beat-grid position.
  - FX Control button 4 toggles the deck quantise mode on/off, (button
    lights blue when active).

### FX Control knobs

  - FX Control knob 1 = Deck gain.
  - FX Control knob 2 = FX 1 "super" control (FX unit 1 on left deck,
    unit 3 on right deck).
  - FX Control knob 3 = FX 2 "super" control (FX unit 2 on left deck,
    unit 4 on right deck).
  - FX Control knob 4 = Deck "quick effect" control (by default this is
    a filter effect but can be changed in Mixxx's preferences).

### FX Assign Buttons

  - Tapping either of the 2 FX ASSIGN buttons on each deck will toggle
    the deck's output to one (or both) of two effects in the (default)
    4-unit effects rack. The left deck (A or C) can be assigned to
    effect units 1 and/or 2. The right deck (B or D) can be assigned to
    effect units 3 and/or 4.
  - \*Holding\* an FX ASSIGN button allows the effect in that effect
    unit to be changed using the BROWSE LEFT/RIGHT buttons.

### DEL-mode

DEL-mode is activated by \*tapping\* the deck's hot cue DEL button (the
button will light up blue). This is equivalent to a shift button on
other controllers and so changes the behaviour of a number of the
controller buttons as follows:

  - The HOT CUE buttons act as auto-loop triggers (when \*held\*) in
    DEL-mode. The button layout follows the default "LateNight" skin
    (i.e. top row = \[1/8\] to \[1\], bottom row = \[2\] to \[16\]
    beats). Longer auto-loops can be "locked" (so the HOT CUE button
    doesn't have to be held) by pressing the LOOP ON/OFF button after an
    auto-loop is selected, (locked/playing auto-loops can also be
    resized by selecting a different auto-loop and then re-locking the
    new size with the LOOP ON/OFF button).
  - The CUE button triggers reverse playback (while \*held\*).
  - The PLAY button triggers reverse-slip playback (while \*held\*). NB:
    if you already have slip-mode activated before you trigger
    reverse-slip playback, (e.g. by having pressed FX-Control button 1),
    then slip-mode will be turned off as soon as you release the PLAY
    button (and you will return to the playback point where you would
    have been if you hadn't altered the playback).
  - The PITCH BEND +/- buttons step the key up/down without altering the
    playback rate. If both PITCH BEND buttons are pressed together, the
    playback key is reset to normal.

### Auto-Loops and Slip-Mode

There are no "slip-mode aware" skins in Mixxx yet so the auto-loop
behaviour of this controller (which \*is\* "slip-mode aware") may be a
little different than you might expect to take advantage of this
feature.

  - Auto-loop buttons are (by default) only active when held.
  - In slip-mode, releasing an auto-loop button will immediately
    "re-sync" playback (by disabling, then immediately re-enabling slip
    mode), you may see the slip-mode button flash briefly when this
    happens. This allows for some very interesting "slip-auto-loop"
    effects.
