# Denon MC3000


The Denon MC3000 is a 4-channel, 4-deck DJ controller and mixer with a
built-in USB audio interface. It has two physical deck sections (jog wheel,
transport, hot cues, loop controls) and a 4-channel mixer, but only two FX
units and eight sampler pads shared across all four decks. The manual
describes this as a "deck layer function that can control four decks
separately": the left deck section can be switched between controlling deck
A or deck C with the {hwlabel}`DECK CHG.` buttons, and the right deck
section between deck B or deck D.

If you'd like to see something changed or extended in this mapping,
please share feedback in the
[forum thread](https://mixxx.discourse.group/t/denon-mc3000-midi-script/12283).

:::{versionadded} 2.0
:::
:::{versionchanged} 2.6
Added full 4-deck (A/B/C/D) support, current EffectRack/beatloop/
QuickEffect controls, and LED feedback for all four decks.
:::
## Useful links


- [Manufacturer's product page](https://web.archive.org/web/20140713040211if_/https://www.denondj.com/products/view/mc3000) (archived, product discontinued)
- [Forum thread](https://mixxx.discourse.group/t/denon-mc3000-midi-script/12283)
- [Owner's manual (PDF)](https://cdn.inmusicbrands.com/denondj/legacy/mc3000/MC3000EM_ENG_IM_v00.pdf)
- [Quick setup guide (PDF)](https://cdn.inmusicbrands.com/denondj/legacy/mc3000/MC3000EM_Quick_Setup_Guide.pdf)
- [Windows driver v1.0.0, 2015](<https://cdn.inmusicbrands.com/denondj/legacy/mc3000/Denon_DJ_MC3000_Driver_v1.0.0(2015).zip>)

## Compatibility


- **macOS**: no driver installation is required. The official quick setup
  guide's only macOS step is configuring the device in Audio MIDI Setup,
  with no driver install step at all, consistent with class-compliant USB
  audio.
- **Windows**: requires the official ASIO driver, linked above (also
  originally shipped on the controller's Resource CD-ROM). After
  installing, check that MC3000 has a checkmark in the ASIO driver control
  panel and is enabled. The driver is old (2015) and not verified against
  recent Windows versions - if it fails to install, Windows' generic USB
  audio class driver may still work for basic use.
- **Linux**: not explicitly documented by the manufacturer; expected to
  work with the kernel's built-in ALSA USB audio driver as a
  class-compliant device, but not verified.

## Audio Interface Setup


The MC3000's built-in USB audio interface is documented (official quick
setup guide) as:

- Channels 1-2 = Master output.
- Channels 3-4 = Headphone output.

Configure these in Mixxx's Sound Hardware preferences accordingly. The
single 1/4" microphone input and the LINE 1/2 inputs are analog mixer
inputs only - not available to Mixxx as audio devices.

:::{note}
{hwlabel}`MASTER LEVEL`, {hwlabel}`MIC LEVEL`, {hwlabel}`MONITOR PAN`,
{hwlabel}`MONITOR PHONES`, and the {hwlabel}`LINE TO MASTER` {hwlabel}`PAN`
and {hwlabel}`LEVEL` knobs are fully analog on this hardware and are not
sent over MIDI at all, so adjusting them changes nothing on screen in
Mixxx.
:::
## Mapping Settings


The mapping features a number of options that can be customized from
{guilabel}`Preferences` > {guilabel}`Controllers`, after selecting your
controller and the Denon MC3000 mapping:

- **Jog wheel sensitivity** sets the jog wheel's pitch-bend sensitivity
  for turning without an active touch-scratch - that is, whenever
  {hwlabel}`VINYL MODE` is off, or the wheel isn't currently touched
  (default: `2.0`). Higher values reduce sensitivity.
- **Scratch sensitivity** sets the jog wheel's scratch sensitivity
  while actively touch-scratching with {hwlabel}`VINYL MODE` on
  (default: `1.0`). Higher values reduce sensitivity.
- **VINYL MODE on by default** sets whether {hwlabel}`VINYL MODE` is
  enabled by default at startup, for all four decks (default: off).
- **KEY LOCK on by default** sets whether {hwlabel}`KEY LOCK` is
  enabled by default at startup, for all four decks (default: off).
- **Quantize on by default** sets whether quantize
  ({hwlabel}`SHIFT` + {hwlabel}`SYNC`) is enabled by default at startup,
  for all four decks (default: off).

## Mixer Section


| Control | Function |
| --- | --- |
| Channel fader, Cross fader | Standard volume and crossfader control. |
| {hwlabel}`LEVEL` | Channel pregain/trim. |
| {hwlabel}`FILTER` | QuickEffect filter. |
| {hwlabel}`HI` / {hwlabel}`MID` / {hwlabel}`LOW` | 3-band channel EQ. |
| {hwlabel}`CUE` (left channel strip) / {hwlabel}`CUE` (right channel strip) | Headphone cue (PFL) toggle. Only 2 physical buttons, one per channel strip; each toggles PFL for whichever deck (A or C on the left strip, B or D on the right strip) is currently active on that strip. |
| {hwlabel}`KEY LOCK` | Toggles keylock for the deck. Off by default at startup for all four decks; see Mapping Settings above to change the default. |
| {hwlabel}`SYNC` | Beat-syncs the deck. Hold past a short delay to enable continuous sync lock instead of a one-time sync. The LED lights while sync is active. |
| {hwlabel}`SHIFT` + {hwlabel}`SYNC` | Toggles quantize for the deck. Off by default at startup for all four decks; see Mapping Settings above to change the default. |

:::{hint}
{hwlabel}`LEVEL`, {hwlabel}`FILTER`, {hwlabel}`HI`, {hwlabel}`MID`,
{hwlabel}`LOW`, and the pitch fader (see Deck Section below) use
soft-takeover: turning the physical control has no effect until it
reaches the value Mixxx is currently using, so there's no jump.
:::
## Deck Section


| Control | Function |
| --- | --- |
| {hwlabel}`PLAY` | Standard play/pause. |
| {hwlabel}`CUE` | Standard cue-point behavior. |
| Jog wheel (touch + turn) | Scratches when touched with {hwlabel}`VINYL MODE` on; otherwise bends pitch while turning. |
| {hwlabel}`VINYL MODE` | Toggles scratch (vinyl) mode for the deck. Off by default at startup for all four decks; see Mapping Settings above to change the default. |
| Pitch fader | Adjusts the deck's playback rate. |
| {hwlabel}`PITCH BEND -` / {hwlabel}`PITCH BEND +` | Temporary pitch bend while playing. |
| {hwlabel}`SHIFT` + {hwlabel}`PITCH BEND -` / {hwlabel}`SHIFT` + {hwlabel}`PITCH BEND +` | While paused, jumps to the track start/end instead of bending pitch. |
| {hwlabel}`SHIFT` | Modifier used by several controls throughout this mapping. |
| {hwlabel}`DECK CHG.` (A/B/C/D) | Switches the left (A/C) or right (B/D) deck layer for the jog wheel, hot cues, loop controls, EFX and other per-deck controls. {hwlabel}`LOAD A` / {hwlabel}`LOAD B` are the one exception - see the Library Section below. |

:::{hint}
Jog wheel and scratch sensitivity can be tuned to taste; see Mapping
Settings above.
:::
## Hot Cue Section


| Control | Function |
| --- | --- |
| {hwlabel}`CUE1` - {hwlabel}`CUE4`, {hwlabel}`CUE5` - {hwlabel}`CUE8` (with {hwlabel}`CUE5-8 MODE`) | Sets/jumps to a hot cue point. |
| {hwlabel}`SHIFT` + hot cue button | Clears the hot cue instead. |

## Loop Section


| Control | Function |
| --- | --- |
| {hwlabel}`AUTO LOOP` | Engages/releases a beat-synced loop at the current position. |
| {hwlabel}`SHIFT` + {hwlabel}`AUTO LOOP` | Deletes the current loop points instead of engaging a loop. |
| {hwlabel}`LOOP IN` / {hwlabel}`LOOP OUT` | Manually sets the loop start/end point. |
| {hwlabel}`LOOP CUT -` / {hwlabel}`LOOP CUT +` | Halves or doubles the active (or next) loop's length. |

## FX Section


| Control | Function |
| --- | --- |
| {hwlabel}`EFX.1` - {hwlabel}`EFX.3` buttons | Toggles the corresponding effect slot on/off in the side's assigned effect unit (left = Unit 1, right = Unit 2). |
| {hwlabel}`EFX.1` - {hwlabel}`EFX.3` knobs | Adjusts that effect's meta knob parameter. |
| {hwlabel}`EFX.4` button | Hold, then press {hwlabel}`EFX.1` - {hwlabel}`EFX.3` to focus one effect for individual parameter control -- while focused, those buttons/knobs control that effect's own parameters instead of the enable toggle/meta knob. A short press shows/hides the focused effect's parameters. |
| {hwlabel}`EFX.4` knob | Adjusts the assigned effect unit's overall dry/wet mix. |
| {hwlabel}`FX ON 1` / {hwlabel}`FX ON 2` | Assigns effect Unit 1 or Unit 2 to whichever deck is currently active on that side. |
| {hwlabel}`EFX` | Shows/hides the effect rack. |

## Sampler Section


:::{note}
Per the official manual, the four {hwlabel}`EFX.1` - {hwlabel}`EFX.4`
knob/button pairs above are dual-purpose, switched entirely in hardware
by the {hwlabel}`SAMP.` button: "OFF: Switches to the effect mode. EFX.
1-4 are used to operate the effects. ON: Switches to the sample deck
mode. EFX. 1-4 are used to operate the sample deck." There is no
separate physical SAMP 1-4 control - it is the same EFX.1-4
buttons/knobs, relabeled in hardware.
:::
| Control | Function |
| --- | --- |
| {hwlabel}`EFX.1` - {hwlabel}`EFX.4` as SAMP 1-4 buttons (while {hwlabel}`SAMP.` is on) | If a track is loaded, plays it from its cue point. If the slot is empty, loads the currently-selected library track into it. |
| {hwlabel}`SHIFT` + SAMP button | Stops the sampler if playing, or ejects the loaded track if stopped. |
| {hwlabel}`EFX.1` - {hwlabel}`EFX.4` as SAMP 1-4 knobs (while {hwlabel}`SAMP.` is on) | Adjusts the sampler's gain. |
| {hwlabel}`SAMPLE` | Shows/hides the sampler section. |

The SAMP pad LEDs light solid when a sampler is loaded and blink while it's
playing.

## Library Section


| Control | Function |
| --- | --- |
| Track select knob ({hwlabel}`SEL.`) | Browses the track library. |
| Track select knob push ({hwlabel}`SW`) | Loads the highlighted track into the first stopped deck. |
| {hwlabel}`FWD` / {hwlabel}`BCK` | Selects the next/previous playlist or crate. |
| {hwlabel}`LOAD A` | Loads the selected track to deck A. |
| {hwlabel}`SHIFT` + {hwlabel}`LOAD A` | Loads the selected track to deck C instead. |
| {hwlabel}`LOAD B` | Loads the selected track to deck B. |
| {hwlabel}`SHIFT` + {hwlabel}`LOAD B` | Loads the selected track to deck D instead. |
| {hwlabel}`BROWSE` | Toggles the maximized library view. |
| {hwlabel}`RECORD` | Starts/stops recording the mix. |

## Known Issues


- {hwlabel}`CF MODE` is not mapped: its stock function, toggling the
  crossfader between audio and video assignment, has no Mixxx equivalent.
- {hwlabel}`DUCKING` is not mapped to anything.
- {hwlabel}`MASTER LEVEL`, {hwlabel}`MIC LEVEL`, {hwlabel}`MONITOR PAN`,
  {hwlabel}`MONITOR PHONES`, and the {hwlabel}`LINE TO MASTER` {hwlabel}`PAN`
  and {hwlabel}`LEVEL` knobs are fully analog hardware controls, invisible
  to MIDI.
