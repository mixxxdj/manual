Denon SC Live 4
===============

A controller mapping for using the **Denon DJ SC Live 4** with `Mixxx
<https://mixxx.org>`__, the free and open-source DJ software. It was built
control by control on the hardware with **Engine OS 5.0.4** and tested with
**Mixxx 2.5.6** on macOS, using Mixxx's default settings.

It covers both decks (decks 1–4), all four mixer channels, every pad mode, Sweep
FX, the Beat FX strip, meters, and otherwise follows Denon's original functions,
light patterns, color schemes, and library navigation from **SC Live 4 User
Guide v5.0.0**. It also will use any custom cue and loop colors the user chooses
in Mixxx. Some additional customization is available via the mapping page in
Mixxx Preferences > Controllers > SC Live 4.

For SC Live 4 settings that are normally only available onscreen in standalone
mode, mapping was included on otherwise unused controls. When possible,
functions are mapped to buttons or knobs that makes them intuitive to use (such
as using the buttons for Beat Jump and pitch bend during Beat Grid editing
mode).

Additionally, this mapping has created a "Settings Pad" mode. It allows the user
to access and change additional preferences with SHIFT + HOT CUE. This mode uses
Denon-style color-coding on pad lights to indicate which setting can be
modified. Once the user presses the button for a mode, the controller quickly
shows a "pad meter" indicating the current level of the setting, which can be
adjusted with the parameter buttons [< >].

The mapping has only been tested on macOS, but should work on Windows and Linux
as long as all typical Mixxx settings and requirements for your operating system
are correct. For instance, the audio setup may differ (Windows may need Denon's
SC Live 4 driver for the headphone outputs).

The code was adapted from the Denon Prime 4 mapping by Levi Williams and
RattyDAVE. While there are some key differences, many functions of the SC Live 4
are similar to those of the Prime 4 family.

-  `Manufacturer's product page <https://www.denondj.com/sclive4.html>`__
-  `Forum thread <https://mixxx.discourse.group/t/denon-sc-live-4-mapping-tested-in-2-5-6-2-6-beta/34288>`__

.. versionadded:: 2.5

Known limitations
-----------------

- **Stems:** This mapping doesn't include stem controls. Engine OS uses its own
  encrypted proprietary stems, and there don't yet appear to be practical
  alternatives for SC Live 4 users.

- **Custom Settings Reset:** Values changed on the Settings Pad mode (Shift +
  Hot Cue) reset each time Mixxx restarts.

- **Microphones/Aux:** At this time, it appears that microphones behave
  similarly to other Denon controllers in Mixxx. Mics and Aux inputs have been
  tested successfully, live and in recordings. However, the controller's main
  level meter only shows Mixxx's music output, not the mic/aux output when in
  Computer Mode.

  When using Mixxx's **Auto** ducking function, the music is lowered even while
  no one is speaking. For this reason, **Man** ducking mode was mapped as the
  controller's default Talkover function, but this preference can be changed on
  the mapping page.

  At this time, Mixxx's effects can't be used on the SC Live 4's mics, because
  the controller appears to mix them in after Mixxx.

  Due to these issues, it's recommended to connect mics/aux devices directly to
  an audio interface or computer input. However, if you wish to use the
  controller's inputs, see Microphones / Aux below for basic settings.

- **Control mirroring:** The SC Live 4 handles volume adjustments for headphones
  and microphones with dedicated controls, so mapping was disabled for them. In
  the Mixxx GUI, you will not see those knobs move. Be sure to keep the Mixxx
  knobs for mics and headphones in the 12 o'clock position to avoid unnecessary
  volume boosting and clipping. All other knobs, buttons and faders are
  reflected in Mixxx exactly as they appear on the controller, as long as the
  controller is in Computer Mode before Mixxx is launched.

- **Touch FX:** Since the SC Live 4's screen is inactive in Computer Mode, Touch
  FX isn't available. However, some otherwise hidden features and settings from
  the touchscreen view have been mapped for access via buttons, knobs, and/or
  pads.

- **Lighting:** Mixxx does not appear to have lighting features at this time.
  Also, the controller's Engine Lighting is a proprietary system and doesn't
  appear to send lighting data over MIDI outside of private integrations. The
  Lighting button has been repurposed for other functions which the user can
  change in mapping preferences.

Setup
-----

1. **Sound:** in **Preferences > Sound Hardware**, set **Main** to *SC LIVE 4
   Audio*, channels 1–2, and **Headphones** to channels 3–4.

2. **Mapping:** in **Preferences > Controllers > SC LIVE 4**, choose **Denon SC
   Live 4**, check **Enabled** and click **Apply**.

3. **Effects.** For FX to work correctly, it's important that you set up your
   Mixxx preferences before using the controller.

   The Sweep FX buttons and Fader Echo use effects from two lists in **Mixxx >
   Preferences > Effects**, on the **Effect Chain Presets** tab. This is a
   one-time setup, and Mixxx remembers it. Effects presets must be listed in a
   specific order if you want to use Sweep FX and Fader Echo. See Sweep FX
   Assignments and Fader Echo below for default Denon-style recommendations or
   how to assign Custom FX to buttons and faders.

   To assign FX for use with **Beat FX (the BPM FX knob)**, go to the **"Visible
   Effects"** tab. The effects you assign here can then be used with channel
   assign, time/parameter, amount, and FX on/off on the controller. Drag any of
   your favorite FX presets in the order you wish to see them in Mixxx's Effects
   section. This mapping also unlocks the ability to use up to six (6) chained
   Mixxx or imported custom FX at a time.

4. **Microphones (optional).** See Microphones / Aux below.

When Mixxx starts, the mapping asks the SC Live 4 for the position of every
fader, knob and switch, so Mixxx matches the hardware immediately. With the
exception of known limitations mentioned above, you will see the position of all
controls visibly reflected in Mixxx.

Main volume and headphones level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Main Volume knob on the SC Live 4 moves Mixxx's main gain knob to the same
position.

Note that in Mixxx, 12 o'clock is normal full volume for the main volume/gain.
Turning past 12 o'clock adds a boost of up to +14 dB, which can make your mix
and effects distort. For the best sound, keep Main Level at or below 12 o'clock
and use your speakers, amplifier or the Speaker/Booth Level knob to play louder.
If a track is particularly quiet, you can go higher, but keep an eye on the main
level meter to avoid clipping.

The Headphones Level knob controls the SC Live 4's headphone output directly, so
it isn't mapped to Mixxx, and Mixxx's own headphone gain knob doesn't move with
it. Leave Mixxx's headphone gain at its default (12 o'clock) to avoid
unnecessary volume boosting and clipping.

Sweep FX assignments
^^^^^^^^^^^^^^^^^^^^

Sweep FX are assigned using the **Quick Effect Chain Presets** list in **Mixxx >
Preferences > Effects** (under the **Effect Chain Presets** tab). You have the
option of using effects that are similar to the controller's four built-in
effects, or customizing the buttons to your own choices.

**For effects similar to the SC Live 4's sounds,** drag these built-in Mixxx
effects to the top of the list, in this order:

1. **Filter** or **Moog Filter**

2. **White Noise**

3. **Echo** (used for both Echo and Wash)

After setting the order, select **Default SCL4 Sweep FX** under **Which presets
have you assigned to the four Sweep FX buttons via the Quick Effects list?** on
the mapping's page in **Preferences > Controllers > SC LIVE 4**. The SC Live 4's
Wash button uses a variation of Echo, so this mapping setting automatically
assigns the fourth button a similar sound.

**Custom Sweep FX:** You also have the alternate option to assign any effect
preset you want to any of the four buttons. Drag presets to the top of the Quick
Effect Chain list in the order of the buttons you want to use them on:

1. Filter button

2. Noise button

3. Echo button

4. Wash button

**Important:** If you plan to use custom presets make sure you also select
**Custom Sweep FX** under **Which presets have you assigned to the four Sweep FX
buttons via the Quick Effects list?** on the mapping's page. This turns off
default SC Live 4 settings. If you do not choose "Custom Sweep FX" in the
mapping page, your fourth effect will have a Wash effect applied to it.

Fader Echo
^^^^^^^^^^

You can turn Fader Echo on or off from the controller, in the Settings Pad mode
(SHIFT + HOT CUE, then pad 4) but first need to make sure the effect you want is
set in Mixxx.

To use it, go to **Preferences > Effects > Effect Chain Presets** and make sure
**Echo** (or any other effect you wish to use on your fader) is at the very top
(position 1) of the **Effect Chain Presets** list.

On the mapping's page in **Preferences > Controllers > SC LIVE 4**, set **Fader
Echo Style (when activated)** to **Default SCL4 Fader Echo** for traditional
fader echo. This default setting is set up to work with Mixxx's Echo. If you
want to use any other effect (such as Reverb, Delay, Chorus, etc), choose
**Custom Fader Echo** and assign that effect to position 1 of Effect Chain
Presets.

Microphones / Aux
^^^^^^^^^^^^^^^^^

In testing, the SC Live 4 appeared to mix its microphones into its own outputs,
at levels set by the hardware knobs. It also appears to send its main mix (the
music and the mics together) back to the computer via its two input channels,
with Mic 1 on channel 1 and Mic 2 / Aux on channel 2. Mixxx can include this
output into recordings and broadcasts. If you plan to use microphones for live
broadcasting or recording, here are some recommended settings to get the
cleanest results:

**Setup:**

1. open **Mixxx > Preferences > Sound Hardware**, select the **Input** tab and
   set:

   .. list-table::
      :header-rows: 1
      :widths: 35 65

      * - Input
        - Set to
      * - Microphone 1
        - *SC LIVE 4 Audio*, Channel 1
      * - Microphone 2
        - *SC LIVE 4 Audio*, Channel 2
      * - Record/Broadcast
        - *SC LIVE 4 Audio*, Channels 1–2

2. Set **Microphone Monitor Mode** to **Direct monitor (recording and
   broadcasting only)** and click **OK**. This setting will prevent the
   controller and Mixxx's audio from doubling one another.

**Tips on Using mics:**

- **Mic 1 and Mic/Aux 2 ON buttons:** press to turn on or off. You will see
  Mixxx's "Talk" button turn on. The button is dim when the mic is off and lit
  bright when the mic is on.

- **SHIFT + Mic 1 (TALKOVER):** turns Mic 1 on, with Mixxx's ducking on for
  either mic. As it does in Engine OS, the button flashes when it is in Talkover
  mode. Press it again to turn both off. Note that you can choose your preferred
  Mixxx ducking mode on the mapping's page: **Man** keeps the music lowered the
  whole time the mic is on, and **Auto** lowers it only while the mic picks up
  sound.

- **When Mixxx starts:** the SC Live 4 doesn't tell Mixxx whether its mics are
  on, so the mapping assumes both are off. It's best to make sure the mics are
  off before you start Mixxx. If you forget, you can resync the buttons by
  quitting Mixxx, and restarting the controller in Computer mode before
  restarting Mixxx.

- **Mic level knobs:** set each mic's level. Since these are dedicated knobs
  that the controller uses, they aren't mapped to Mixxx. Leave Mixxx's own mic
  gain at its default to avoid unnecessary volume boosting and clipping. Use the
  controller's knobs and monitor clipping with peak indicator lights. Note that
  the controller's Main Volume knob does not change the output level of the
  mics.

- **Aux:** with the Mic 2 / Aux switch set to Aux, Aux appears to use the same
  path as Mic 2. As in Engine OS, the button doesn't flash for ducking while the
  switch is on Aux.

- **Effects:** Due to the controller's handling of mic/aux audio, FX cannot be
  mapped to them individually.

**If your mic/aux doesn't work as expected with Mixxx**, or you wish to use FX
with them, it is recommended that you plug the mic into your computer, or into a
separate audio interface, and set that as Mixxx's Microphone 1 input.

Settings
--------

The mapping's settings are on its own page in **Mixxx > Preferences >
Controllers > SC LIVE 4**. Choose a setting and click **OK**. The defaults match
the SC Live 4's own standalone behavior.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Setting
     - Choices
   * - **What should the Track Skip buttons do?**
     - This allows you to set how the Track Skip buttons behave, whether default SC Live 4 behavior or to jump to start, or hold to rewind/fast-forward.
   * - **What should Shift + Sync do?**
     - You can choose default SC Live 4 behavior to turn off Sync mode or use it to turn Quantize off/on for that particular deck.
   * - **Turn on quantize for all decks**
     - This allows you to automatically turn on Quantize for all decks when Mixxx starts.
   * - **Start with channel volumes at 0**
     - A moment after Mixxx starts, the SC Live 4 appears to report where its faders really are, and Mixxx follows them. This setting is a safety net so that nothing ever plays at full volume at startup.
   * - **When resizing loops, which end locks in place?**
     - These settings allow you to set which part of a loop doesn't change when resizing.
   * - **Jog wheel sensitivity**
     - The larger the number, the more the track moves for each turn of the wheel. The default 0.5.
   * - **Tempo Range Preference**
     - The tempo ranges you want to be able to adjust tempo by when you use SHIFT + Pitch Bend (- or +).
   * - **Which presets have you assigned to the four Sweep FX buttons via the Quick Effects list?**
     - Set so that the effects you've set up Sweep FX Assignments behave correctly on the Sweep FX buttons.
   * - **Fader Echo Style (when activated)**
     - This allows the mapping to adjust Fader Echo settings for Mixxx's Echo (default), or leaves them alone if you want to use other FX types on the Fader, such as Reverb or Delay (custom).
   * - **How many bars should Fader Echo last**
     - Allows you to adjust how long (in bars) that the effect lasts when the fader reaches zero.
   * - **What should the Lighting button do?**
     - Allows you to assign a specific function to the Lighting button on the controller: Auto DJ, Recording, or Live Broadcasting. Make sure you have appropriate settings for recording/broadcasting in Mixxx Preferences or tracks in the Auto DJ queue and you can then use the Lighting button to quickly turn those modes on or off. See LIGHTING section in the Quick Reference below.
   * - **What style of Talkover or mic ducking do you prefer?**
     - Allows you to set which Mixxx ducking mode will be used by SHIFT + Mic 1 (Talkover). See Microphones.

Mapping
-------

Decks (each side)
^^^^^^^^^^^^^^^^^

DECK SWITCH
"""""""""""

Press the Deck button to switch that side of the SC Live 4 between two Mixxx
decks: deck 1 or 3 on the left side, deck 2 or 4 on the right side.

The jog wheel display shows the word DECK and the active deck number in a box,
as on the SC Live 4 without a computer.

Additional Function: SHIFT + Deck button switches the Mixxx screen between
2-deck and 4-deck view.

PLAY
""""

Press PLAY to start playing the track. Press it again to pause.

If you've set a longer stop time on the Settings Pad mode (SHIFT + HOT CUE),
pausing slows the track to a stop like a turntable instead of stopping
instantly.

Additional Function: SHIFT + PLAY jumps back to the cue point and keeps playing
from there (stutter play).

CUE
"""

Press CUE to set a cue point or jump back to it, following the cue mode chosen
in Mixxx (Preferences > Decks).

Additional Function: SHIFT + CUE jumps back to the start of the track.

SYNC
""""

Tap SYNC once to match this deck's tempo to the other playing deck, one time
only.

Hold SYNC (for about half a second) to turn on sync lock, which keeps the tempo
matched until you turn it off. The button stays lit while sync lock is on. Tap
SYNC again to turn it off.

Additional Function: SHIFT + SYNC turns sync lock off. If you prefer, you can
make SHIFT + SYNC turn quantize on and off instead, under "What should Shift +
Sync do?" in Settings.

KEY LOCK
""""""""

Press KEY LOCK to turn key lock on or off. When key lock is on, changing the
tempo doesn't change the track's pitch. The button is lit while it's on.

Hold KEY LOCK to match this track's key to the other playing deck's key (key
sync).

Additional Function: SHIFT + KEY LOCK resets the track to its original key.

\|<<  >>\| TRACK SKIP
"""""""""""""""""""""

Tap \|<< or >>\| to load the previous or next track in the Mixxx library list
onto this deck.

If the track is paused part-way through, tapping \|<< goes back to the start of
the track instead.

Additional Function: SHIFT + hold \|<< or >>\| searches backward or forward
through the track for as long as you hold it.

(For this to load a track onto a deck while it's playing, you need to select
"allow loading tracks into playing decks" in Mixxx preferences.)

(You can choose a different behavior for these buttons under "What should the
Track Skip buttons do?" in Settings.)

Auto DJ: while Mixxx's Auto DJ is on, >>\| triggers Auto DJ's Fade Now, which
crossfades to the next track in the Auto DJ queue (see LIGHTING below).

BEAT JUMP <  >
""""""""""""""

Press BEAT JUMP < or > to jump backward or forward through the track by the beat
jump size you've chosen (shown in Mixxx).

Additional Function: SHIFT + BEAT JUMP < or > makes the jump size smaller or
larger. The new size briefly shows on the pads as a green pad meter (see PAD
METERS below).

PITCH BEND - +
""""""""""""""

Hold PITCH BEND - or + to slow down or speed up the track for as long as you
hold it. Use this to nudge two tracks back into time with each other.

Additional Function: SHIFT + PITCH BEND - or + changes the tempo fader's range:
4%, 8%, 10%, 20%, 50% or 100% (or the group chosen under "Tempo Range
Preference" in Settings). The new range briefly shows on the pads as a red pad
meter (see PAD METERS below).

TEMPO FADER
"""""""""""

Manually change the tempo. When the fader is exactly at its center, the tempo is
0% (the track's original BPM) and the center light illuminates, as in Engine OS.

JOG WHEEL
"""""""""

Jog wheels behave as they do in standalone mode and are fully mapped to Mixxx.
Touch the top of the jog wheel and turn it to scratch, or to scrub through a
paused track. Turn the outer edge of the jog wheel to nudge a playing track
slower or faster, to bring it back into time.

Jog wheels also display active deck numbers, BPM, time remaining, and playhead
location relative to the track length:

::

   DECK box   shows the active deck number.

   Ring       a white ring with a dark segment that turns like a spot on
              a record while the track plays. It stops when the track is
              paused, follows your hand when you scratch or scrub, and
              turns faster or slower when you change the tempo. With no
              track loaded, the whole ring is lit.

   BPM        the track's current tempo, including any tempo fader
              change, updating as you play.

   TIME       the track's time, counting as it plays. It shows elapsed
              or remaining time (with a minus sign), matching Mixxx's own
              setting: click the time on Mixxx's screen to switch.

BPM and TIME appear only when a track is loaded.

Near the end of a track, the ring warns you by switching back and forth between
its dark segment and a single lit segment. It starts at the end-of-track warning
time set in Mixxx (Preferences > Waveforms).

VINYL
"""""

Press VINYL to switch how the top of the jog wheel works:

::

   On  = touching the top of the jog wheel scratches (like a record)
         or allows you to scrub through the track.
   Off = the jog wheel only nudges, even when you touch the top.

SLIP
""""

Press SLIP to turn Slip mode on or off. Press and hold SLIP for about half a
second (or press SHIFT + SLIP) to turn on beat grid edit mode, for fixing
Mixxx's beat grid on the track. Holding SLIP doesn't also turn Slip mode on or
off.

The flashing Slip light is the only sign that beat grid edit mode is on. You'll
see its effect on the beat markers in Mixxx's waveform, and on the BPM. While in
this mode, you can use:

::

   BEAT JUMP < >    to move the grid earlier or later,

   PITCH BEND - +   to make the grid's tempo slower or faster,

   CUE              to move the nearest beat to the playhead,

   SHIFT + SLIP     to undo the last grid change,

   SLIP             to exit grid edit mode.

Each PITCH BEND press changes the grid's tempo by only 0.01 BPM, which may be
too small to see on the beat markers near the playhead. To confirm it's working,
watch the BPM instead, either on Mixxx's screen or on the jog wheel display: it
changes by 0.01 with each press (for example, 124.00 becomes 124.01).

CENSOR
""""""

Hold CENSOR to play the track backward (reverse roll). When you let go, the
track continues playing forward from where it would have been, so it stays in
time.

Additional Function: SHIFT + CENSOR plays the track in reverse while you hold
it, like a rewind. When you let go, it plays forward from where it reached.

LOOP IN / OUT
"""""""""""""

Manually set a loop: press LOOP IN where you want the loop to start, then press
LOOP OUT where you want it to end. The loop starts playing immediately.

Press LOOP OUT while a loop is playing to exit the loop. The track keeps
playing.

Lights: dim = no loop is playing. Bright = a loop is playing (started from any
loop control or pad).

LOOP KNOB
"""""""""

Turn the knob to set or change the loop size. This can be used to create or
change loops on-the-fly in real time, or to set the size in advance. The loop is
resized from its loop-in point (you can change this in Settings).

Press the knob to start a loop of that size, or to turn a playing loop off.

Additional Function: SHIFT + turn the knob moves the playing loop backward or
forward through the track, by the beat jump size you've set (shown in Mixxx).

Additional Function: SHIFT + press the knob starts a loop roll: the loop plays
while you hold it, and when you let go the track continues from where it would
have been.

Pad modes (press the mode button again to switch layers)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HOT CUE
"""""""

To set hot cues on pads 1-8, press any empty pad to set a cue on it. You can
change the color of the pad in Mixxx by right-clicking on the cue in Mixxx.

Additional Function: SHIFT + pad to delete an existing hot cue.

Lights: off = the pad is empty. Color-lit pads = the pad has been set.

HOT CUE, layer 2: Engine OS's PITCH PLAY feature
""""""""""""""""""""""""""""""""""""""""""""""""

Press HOT CUE a second time to switch to Pitch Play. Each pad plays the last hot
cue you used, at a different pitch. Press a pad to jump to that hot cue and play
it at that pitch.

Pad 5 (lit white) plays the original key. Pads 1-4 play 4, 3, 2 and 1 semitones
lower. Pads 6-8 play 1, 2 and 3 semitones higher.

PARAMETER < or > moves the whole range of pads one semitone lower or higher.

Additional Function: SHIFT + PARAMETER < or > shifts the track's key one
semitone lower or higher (up to 3 semitones either way), on top of the pad
you've played.

To return to the original key, press SHIFT + KEY LOCK.

Lights: pad 5 = white. The other pads = the hot cue's color, dim. The pad you
last played = full brightness.

LOOP, layer 1: SAVED LOOPS
""""""""""""""""""""""""""

Save up to 8 loops on the pads. They're stored in Mixxx's hot cue slots 9-16.

To save a loop on an empty pad, press it once to set the loop start (Loop In),
then press it again to set the loop end (Loop Out). The pad lights white while
it's waiting for the second press. If a loop is already playing, one press on an
empty pad saves that loop.

Press the pad of the loop that's playing to turn the loop off.

Press any other saved pad to jump to that loop and play it.

Additional Function: SHIFT + pad deletes that saved loop.

ACTIVE LOOPS: hold PARAMETER < and press a saved loop pad to mark it as an
Active Loop (press it again to unmark it). An Active Loop starts looping by
itself when playback reaches it, in any pad mode. Marked pads pulse. Marks clear
when a new track is loaded.

Lights: off = the pad is empty. Dim = a loop is saved. Full brightness = that
loop is playing.

LOOP, layer 2: AUTO LOOPS
"""""""""""""""""""""""""

Press LOOP a second time to switch to Auto Loops. Press a pad to start a loop of
that length: 1/16, 1/8, 1/4, 1/2, 1, 2, 4 or 8 beats (pads 1-8). Press it again
to turn the loop off.

PARAMETER < or > halves or doubles all 8 loop lengths (see PARAMETER below).

Additional Function: SHIFT + PARAMETER < or > moves the playing loop backward or
forward through the track.

Lights: green = ready. White = that loop is playing.

ROLL, layer 1
"""""""""""""

Hold a pad to play a loop roll of that length: 1/8, 1/4T, 1/4, 1/2T, 1/2, 1T, 1
or 2 beats (T = triplet), as in the SC Live 4 manual. When you let go, the track
continues playing from where it would have been, so it stays in time.

PARAMETER < or > halves or doubles all 8 roll lengths (see PARAMETER below).

Lights: green = normal roll. Purple = triplet roll. White = the pad you're
holding.

ROLL, layer 2: SAMPLER
""""""""""""""""""""""

Press ROLL a second time (or SHIFT + ROLL) to switch to the Sampler. Pads 1-8
play Mixxx's sampler decks 1-8.

To load a sample, turn the Browse knob to highlight a track in the Mixxx
library, then press an empty pad. The track is loaded into that sampler. (You
can also drag tracks onto Mixxx's on-screen samplers.)

Press a loaded pad to play its sample from the start.

Additional Function: SHIFT + pad stops the sample if it's playing. If it isn't
playing, SHIFT + pad unloads (ejects) it.

Lights: off = the pad is empty. Dim = a sample is loaded. Full brightness = the
sample is playing. Each pad has its own color, as on the SC Live 4 without a
computer.

SLICER, layer 1
"""""""""""""""

Press SLICER to divide the next 8 beats of the track into 8 slices, one per pad.
The lit pad follows the slice that's playing, and the 8 slices move on with the
track every 8 beats.

Hold a pad to jump to that slice and repeat it. When you let go, the track
continues from where it would have been, so it stays in time.

Lights: the slices are dim blue. The slice that's playing is lit white.

SLICER, layer 2: SLICER LOOP
""""""""""""""""""""""""""""

Press SLICER a second time to switch to Slicer Loop. The slices become a FIXED
loop that repeats until you leave, like a normal loop. Press the pads to jump
between slices in time and rearrange them.

To exit: press SLICER again (back to layer 1, where the slices move with the
song) or any other pad mode. The track keeps playing.

PARAMETER < or > changes the quantize size (1/8 to 1 beat): how finely the jumps
between slices are timed. The new size briefly shows as a yellow pad meter.

Additional Function: SHIFT + PARAMETER < or > changes the domain size (4 to 32
beats): how long the whole loop is. The new size briefly shows as a cyan pad
meter.

Lights: the slices are dim purple. The slice that's playing is lit white.

PARAMETER < >
"""""""""""""

What these buttons do depends on the pad mode you're in:

::

   In Pitch Play, PARAMETER < or > moves the whole range of pitches on the
   pads one semitone lower or higher. SHIFT + PARAMETER < or > shifts the
   track's key one semitone lower or higher.

   In Saved Loops, hold PARAMETER < and press a saved loop pad to make it
   an Active Loop.

   In Auto Loops and Roll (layer 1), PARAMETER < or > halves or doubles the
   lengths of all 8 pads at once (anywhere from 1/32 beat to 64 beats). They
   go back to the lengths listed above when the mapping reloads. In Auto
   Loops, SHIFT + PARAMETER < or > moves the playing loop backward or
   forward instead.

   In Slicer Loop, PARAMETER < or > changes the quantize size, and SHIFT +
   PARAMETER < or > changes the domain size (see PAD METERS above).

   In the Settings Pad mode, PARAMETER < or > changes the setting you've
   selected. See "Settings Pad Mode / Pad Meters" section below.

Settings Pad mode / pad meters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Settings Pad mode is a special system developed for the SC Live 4 / Mixxx
integration, so that users have a reference for screen-based settings that can't
otherwise be accessed in Computer Mode. Pad meters have been designed to display
quick visual confirmation on the pads when settings are changed, in this mode
and with some deck and Beat FX controls (see below).

Pad meters appear on the pads automatically, for about one second, whenever you
change one of the settings below. The pads then go back to showing your current
pad mode. You don't need to press any pads to see a meter. Just change the
setting. They're only visual references.

How to read Pad Meters: The color of the group of pads tells you which setting
you're looking at. The number of lit pads shows the setting's value, similar to
the lighted segments of a volume meter (ie. Seeing only Pad 1 means the setting
is at its lowest possible value. Seeing all 8 pads means it is at its highest
possible value). You can adjust them with the controls listed under HOW TO
ACCESS for each setting below.

SHIFT + HOT CUE: SETTINGS PAD MODE
""""""""""""""""""""""""""""""""""

Hold SHIFT and press HOT CUE to open the Settings Pad mode. It gives you Engine
OS Control Center settings that the SC Live 4 has no dedicated controls for.
Each setting has its own fixed pad, which is always in the same place.

Press pads 1-4 to choose a setting. The chosen setting's pad is bright, and the
others are dim, and its current value briefly shows as a pad meter in that pad's
color. Then press PARAMETER < (lower) or > (higher) to change it. The new value
briefly shows in the same way.

When the meter disappears, you're still in the Settings Pad mode with the same
setting selected. You can press PARAMETER < or > again at any time to change
that setting, and its current value shows again each time.

**CROSSFADER CONTOUR**

| Settings Pad: Pad 1
| Pad Color: Yellow

This sets how quickly the crossfader brings in the other side. The number of lit
pads increases as the cut gets sharper:

::

   Pad 1 = smoothest (a slow blend across the whole crossfader)
   Pad 2 = smooth (Mixxx's default)
   Pad 3 = gentle
   Pad 4 = medium
   Pad 5 = club-style
   Pad 6 = fairly sharp
   Pad 7 = sharp
   Pad 8 = sharp cut (for turntable-style scratching)

At the sharpest setting, the other side comes in fully after only a tiny
movement of the crossfader.

HOW TO ACCESS: press Pad 1, then press the PARAMETER arrows [< >] to make the
contour smoother or sharper.

**STOP TIME**

| Settings Pad: Pad 2
| Pad Color: Red

This sets how long a playing track takes to stop when you press PLAY to pause
it. The number of lit pads increases as the stop gets longer:

::

   Pad 1 = instant (a normal pause)
   Pad 2 = very quick
   Pad 3 = quick
   Pad 4 = short
   Pad 5 = medium
   Pad 6 = longer
   Pad 7 = long
   Pad 8 = longest (about 2 seconds)

At the longest setting, the track slows down like a turntable powering down.
These times are approximate, because Mixxx's brake has no setting in seconds.

HOW TO ACCESS: press Pad 2, then press the PARAMETER arrows [< >] to make the
stop time shorter or longer.

**SAMPLER VOLUME**

| Settings Pad: Pad 3
| Pad Color: Blue

This sets the volume of all 8 samplers (the Sampler pads). The number of lit
pads increases as the volume goes up:

::

   Pad 1 = 12%      Pad 5 = 62%
   Pad 2 = 25%      Pad 6 = 75%
   Pad 3 = 38%      Pad 7 = 88%
   Pad 4 = 50%      Pad 8 = 100%

HOW TO ACCESS: press Pad 3, then press the PARAMETER arrows [< >] to make the
samplers quieter or louder.

**FADER ECHO**

| Settings Pad: Pad 4
| Pad Color: Teal

This turns Fader Echo on or off. When it's on, pulling a playing channel's fader
down crossfades the track into its echo. At zero, the echo rings out for about 1
bar. (You can change how long it lasts in Settings.) Push the fader back up to
cancel. Moving the crossfader fully to one side echoes out the playing decks
assigned to the other side. The meter shows 1 pad when Fader Echo is off, and
all 8 pads when it's on.

HOW TO ACCESS: press Pad 4, then press PARAMETER > to turn Fader Echo on, or
PARAMETER < to turn it off.

Press any mode button to leave. Values last until Mixxx restarts (the contour
then returns to the one set in Mixxx's Preferences).

DECK PAD METERS (appearing only on the current deck you're using)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**BEAT JUMP SIZE**

| Pad Color: Green

This lets you adjust the default beat jump size: how far BEAT JUMP < or > moves
through the track. The number of lit pads increases as the size gets bigger. For
example, Pad 1 = 1/4 beat or less, Pad 3 = 1 beat, Pad 5 = 4 beats, while Pad 8
= 32 or more beats.

HOW TO ACCESS: hold SHIFT while pressing BEAT JUMP arrows [< >] to make the jump
size smaller or bigger.

**TEMPO RANGE**

| Pad Color: Red

This lets you choose how far the tempo fader can change the speed of the track.
The number of lit pads increases as the range gets wider. For example, with the
Denon tempo ranges (see Settings), Pad 1 = 4%, Pad 2 = 8%, Pad 3 = 10%, Pad 4 =
20%, Pad 5 = 50%, while Pad 6 = 100%. Only 6 pads are used.

HOW TO ACCESS: hold SHIFT while pressing PITCH BEND [- +] to make the tempo
range narrower or wider.

**ROLL AND AUTO LOOP LENGTHS**

| Pad Color: Orange

This lets you make the loop lengths of all 8 pads shorter or longer at once, in
Roll (layer 1) or Auto Loops (Loop layer 2). The meter shows the length of pad
1, the shortest. Each pad after it is double the one before. For example, Pad 1
= 1/32 beat, Pad 2 = 1/16 beat (the normal Auto Loop setting), Pad 3 = 1/8 beat
(the normal Roll setting), while Pad 8 = 4 beats.

HOW TO ACCESS: while you're in Roll or Auto Loops, press the PARAMETER arrows [<
>] to make the loop lengths shorter or longer.

**SLICER LOOP QUANTIZE SIZE**

| Pad Color: Yellow

When you press a pad in Slicer Loop, the jump keeps your place within this
length of time, so the rhythm stays in time. The number of lit pads increases as
the size gets longer. For example, Pad 1 = 1/8 beat, Pad 2 = 1/4 beat, Pad 3 =
1/2 beat, while Pad 4 = 1 beat (the normal setting). Only 4 pads are used.

HOW TO ACCESS: while you're in Slicer Loop (Slicer layer 2), press the PARAMETER
arrows [< >] to make the quantize size smaller or bigger.

**SLICER LOOP DOMAIN SIZE**

| Pad Color: Cyan

This is the total length of the Slicer Loop, which is divided into the 8 slices.
The number of lit pads increases as the loop gets longer. For example, Pad 1 = 4
beats, Pad 2 = 8 beats (the normal setting, 1 beat per slice), Pad 3 = 16 beats
(2 beats per slice), while Pad 4 = 32 beats. Only 4 pads are used.

HOW TO ACCESS: while you're in Slicer Loop (Slicer layer 2), hold SHIFT while
pressing the PARAMETER arrows [< >] to make the loop shorter or longer.

BEAT FX PAD METERS (always appearing on the LEFT deck's pads)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The Beat FX controls also activate a pad meter when they are used. You can
always tell which setting a meter is showing by the control you just used:
pressing the BPM FX knob shows the slot, turning the Time/Parameter knob shows
the time or the 2nd setting, and holding SHIFT while turning it shows the
strength. Pressing the Time/Parameter knob switches between the time and the 2nd
setting, and immediately shows the meter for the one you've switched to.
Whenever you move to a new slot, the Time/Parameter knob always starts on the
time.

**BEAT FX SLOT**

| Pad Color: White

There are six Beat FX slots. These are Mixxx's effect units FX1 (slots 1-3) and
FX2 (slots 4-6), the effects panels that appear under the decks in Mixxx. The
pads will briefly light up to let you know which slot you're on. Ex: If you only
see pad one, you are on Slot 1 of 6. If you see five pads, you're on Slot 5 of
6. Then turn the BPM FX knob to choose any FX that you have installed in Mixxx.

HOW TO ACCESS: press the BPM FX knob to move to the next slot.

**EFFECT TIME**

| Pad Color: Teal

This shows the time (or rate) of the effect in the current slot, for example how
far apart an echo's repeats are. The number of lit pads increases as the value
goes up. For example, Pad 1 = its lowest setting, while Pad 8 = its highest.

HOW TO ACCESS: turn the Time/Parameter knob to make the time shorter or longer.

**EFFECT'S 2ND SETTING**

| Pad Color: Magenta

This shows a second setting of the effect in the current slot. Which setting
this is depends on the effect. It's the second knob shown when you expand the
effect in Mixxx. The number of lit pads increases as the value goes up. For
example, Pad 1 = its lowest setting, while Pad 8 = its highest.

HOW TO ACCESS: press the Time/Parameter knob once, then turn it to lower or
raise the setting. Press the knob again to go back to the time.

**EFFECT STRENGTH**

| Pad Color: Purple

This shows how strongly the effect in the current slot is applied: the knob next
to the effect's name in Mixxx. The number of lit pads increases as the effect
gets stronger. For example, Pad 1 = weakest, while Pad 8 = strongest.

HOW TO ACCESS: hold SHIFT while turning the Time/Parameter knob to make the
effect weaker or stronger.

Mixer
^^^^^

SWEEP FX (Filter, Noise, Echo, Wash)
""""""""""""""""""""""""""""""""""""

Sweep FX follow the SC Live 4's default behavior. Press one of the four Sweep FX
buttons. The active button is bright, and it flashes while its effect is being
applied. Effects are not heard when the Sweep FX knob is in the center.

Make sure that you have assigned effects in order, at the top of the Quick
Effect Chain Presets list (see "Sweep FX Assignments" above). This is the setup
using Mixxx's Built-in Effects to simulate the SC Live 4's default sounds:

::

   FILTER button   uses the 1st preset in the list (Filter or Moog Filter)
   NOISE button    uses the 2nd preset (White Noise)
   ECHO button     uses the 3rd preset (Echo)
   WASH button     also uses the 3rd preset (Echo), see below

Once you have set up the FX in order, make sure "Default SCL4 Sweep FX" is
turned on in Mixxx mapping page preferences for the controller.

CUSTOM SWEEP FX: You can assign any effect you wish to any button, as long as
you assign the effect in the proper order for its corresponding button to use (1
Filter, 2 Noise, 3 Echo, 4 Wash). Also make sure to select "Custom Sweep FX" in
the preferences on the Mixxx mapping page for the controller.

CHANNELS
""""""""

The EQs, Fader, Cue buttons and level meters for each channel work as normal and
can be monitored in Mixxx.

BEAT FX
"""""""

This section is mapped to Mixxx's Effect Units (FX1 and FX2), which together
will give you six effect slots to use across the SC Live 4's decks. You can use
one effect at a time or chain several together. It uses the list of effects you
have placed in order in the Visible Effects tab within Preferences > Effects.

BPM FX knob: Push the knob to move through the six effect slots, 1 to 6. Slots
1-3 represent Mixxx's FX1 and slots 4-6 represent Mixxx's FX2. Each time you
push the knob, the slot number is briefly represented by the left deck's pads as
white pads. 1 pad lights up for slot 1, 2 pads light for slot 2, and so on... up
to 6 total.

Once you're on a slot, turn the BPM FX knob in either direction to scroll
through the effect list. Each effect loads into the slot as you turn
automatically and no extra press is required to choose it. If you wish to use
several effects together, push the BPM FX knob again to move to the next slot
and choose another effect.

Channel Assign (3 / 1 / 2 / 4 / M): Mixxx shows FX1 on the left of its screen
and FX2 on the right. However, both will follow the Channel Assign switch on the
controller. You can choose which deck gets the effects in all six slots, or M
for the main mix.

Time/Parameter knob: Turn the knob to change the current slot's effect time or
rate. You will briefly see teal-colored pads. The number of pads that light up
is a meter indicating the level of the current setting. The fewer pads, the
shorter the time, up to 8 pads for the longest. TURN the knob to increase or
decrease the value of the pad meter. PUSH the Time/Parameter knob to switch to
the effect's second setting, whose value is indicated briefly by a magenta pad
meter. Then, turn the knob to decrease or increase that value. Push the knob
again to switch back to the time. In Mixxx, both settings are shown when the
effect is expanded.

Additional Function: SHIFT + push the Time/Parameter knob resets the effect's
settings to the Mixxx default.

Additional Function: SHIFT + turn the Time/Parameter knob changes the effect's
strength: the knob next to its name in Mixxx (purple pad meter).

Amount: how much of the effects you hear (wet/dry), for all six slots.

FX On/Off: turns the effect in the current slot on or off. It flashes while the
effect is on and is dim while it's off, as in Engine OS. All effects are off
when Mixxx starts.

CROSSFADER, MAIN VOLUME LEVEL AND METERS
""""""""""""""""""""""""""""""""""""""""

Use the controller's THRU switch to assign channels to a specific crossfader
blend behavior.

Main Volume level is mapped to the volume of Mixxx's main output. However, be
aware that in Mixxx 12 o'clock is normal full volume. Anything above that on the
controller's own knob will boost volume up to about +14 dB and may lead to
clipping and distortion. (see "Main Volume and Headphones Level" above).

MICROPHONES
"""""""""""

Mic 1 and Aux/Mic 2 ON buttons: Mapped to Mixxx's Talk button, turning the mic
on or off. As with standalone controller mode, a dim light is off, bright is on,
and flashing is on with ducking/talkover activated.

Mic level knobs: set each mic's level independently on the SC Live 4. These are
not mapped to Mixxx to prevent the volume from being applied twice.

Additional Function: SHIFT + Mic 1 (TALKOVER) turns Mic 1 on with Mixxx's
ducking on (Man or Auto, chosen in Settings). Press it again to turn both off.

HEADPHONES
""""""""""

Headphones Level sets your headphone volume on the SC Live 4 itself and isn't
mapped to Mixxx to prevent the volume from being applied twice. Cue Mix blends
between the channels you've cued and the main mix.

SPLIT CUE switch: Mixxx follows the switch. On = your cued channels in the left
ear and the main mix in the right. Off = both blended together.

VIEW
""""

Press VIEW to switch the Mixxx screen between the large library view and the
decks view.

Additional Function: SHIFT + VIEW shows or hides Mixxx's sampler panel.

MENU
""""

Press MENU to show or hide Mixxx's effects panel.

Additional Function: SHIFT + MENU shows or hides Mixxx's microphone panel.

LIGHTING
""""""""

Engine Lighting isn't available in Mixxx. Instead, you can choose the function
of the controller's Lighting button under "What should the Lighting button do?"
on the mapping page. Make sure you have properly set up the feature you wish to
use the button with:

::

   Record on / off: automatically starts and stops Mixxx's recording.
   Recordings follow the Main Volume level knob and include both music and
   microphones (see Microphones above).

   Live broadcast on / off: starts and stops Mixxx's live broadcast, indicated
   by Mixxx's "On Air" badge.

   Auto DJ on / off: starts and stops Mixxx's Auto DJ feature. You must have
   tracks in the Auto DJ queue prior to use. While Auto DJ is on, you can also
   use the Track Skip button >>| to start automatic crossfade to the next
   track in the queue (Fade Now). You can set the transition time in Mixxx
   Auto DJ settings, or turn on sync lock.

BROWSE KNOB
"""""""""""

Turn the Browse knob to scroll through the Mixxx library. Press it to open a
folder or playlist, or to select a highlighted track.

Additional Function: SHIFT + press the Browse knob adds the highlighted track to
the end of Mixxx's Auto DJ queue.

BACK / FWD
""""""""""

Press BACK or FWD to move between the parts of the Mixxx library (playlists,
Auto DJ, crates, devices, etc).

Additional Function: SHIFT + FWD turns quantize on or off for all four decks.

LOAD
""""

Press LOAD to load the highlighted track onto that side's active deck.

Double-press LOAD to copy the track that's playing on the other side, including
its position, onto this deck.

Additional Function: SHIFT + LOAD unloads (ejects) the track from the deck.
