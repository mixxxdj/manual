Denon MC6000MK2
===============

-  `Manufacturer’s product page <https://web.archive.org/web/20180712070421/http://denondj.com/products/view/mc6000mk2>`__ (archived)
-  `Forum thread <http://www.mixxx.org/forums/viewtopic.php?f=7&t=6251>`__
-  `Mixxx maintainer <https://github.com/uklotzde>`__

.. versionadded:: 2.0

The number in the first column refers to the corresponding label in the *Owner’s Manual* in the chapter *Part names and functions* starting on page 20.

============= ===================== ======== ================= =========================================================================================================================================================
# User Manual Control               Modifier Context           Function
============= ===================== ======== ================= =========================================================================================================================================================
1             BEATS/V.FX SEL.                Knob is turned    2.1.0: Effect unit dry/wet mix
\                                            Knob is pressed   2.1.0: Focus/unfocus effect unit
\                                   NONE     Knob is turned    2.0.0: Change musical key
\                                   NONE     Knob is pressed   2.0.0: Reset musical key
\                                   SHIFT    Knob is turned    2.0.0: Load prev/next EFX chain
\                                   SHIFT    Knob is pressed   2.0.0: Toggle between echo loop and default params
2             TAP                   NONE                       Toggle (enable/disable) EFX unit
\                                   SHIFT                      2.0.0: Enable/disable EFX unit + wet loop (automatically enables/disables slip mode when dry/wet mix becomes completely wet, indicated by a blinking LED)
3             EFX 1/2/3 KNOB                                   2.1.0: Effect meta knob
3             EFX 1 KNOB                     Echo loop params  2.0.0: Control echo delay (“parameter2”). The BPM of the echo effect is synchronized with the BPM of the currently assigned deck (length = 1 beat)
3             EFX 2 KNOB                     Echo loop params  2.0.0: Control echo feedback (“parameter3”)
3             EFX 3 KNOB                                       2.0.0: Control dry/wet mix
4             EFX 1/2/3 ON                                     2.1.0: Enable/disable effect
\                                   NONE                       2.0.0: Toggle effect parameter between max. (= ON) and current (= OFF) value
\                                   SHIFT                      2.0.0: Reset effect parameter to min. value
5             EFX CH. ASSIGN        NONE                       Assign/unassign deck
\                                   SHIFT                      Assign deck exclusively
6             LOOP IN               NONE                       Set loop in point
\                                   SHIFT                      Delete loop
6             LOOP OUT              NONE                       Set loop out point
\                                   SHIFT                      Delete loop out point
7             AUTO LOOP             NONE     Loop is undefined Activate a loop over beatloop size beats
\                                   SHIFT    Loop is undefined Activate a rolling loop over beatloop size beats
\                                   NONE     Loop is defined   Toggle reloop
\                                   SHIFT    Loop is defined   Delete loop
7             LOOP +                NONE                       2.1.0: Double beatloop size beats
\                                   SHIFT                      2.1.0: Move loop forward by beatloop size beats
\                                   NONE                       2.0.0: Double loop length
\                                   SHIFT                      2.0.0: Move loop forward by 1 beat
7             LOOP -                NONE                       2.1.0: Halve beatloop size beats
\                                   SHIFT                      2.1.0: Move loop backward by beatloop size beats
\                                   NONE                       2.0.0: Halve loop length
\                                   SHIFT                      2.0.0: Move loop backward by 1 beat
8             HOT CUE 1/2/3/4       NONE     Deck is stopped   Jump to hot cue and start playing while pressed
\                                   NONE     Deck is playing   Jump to hot cue
\                                   SHIFT                      Delete hot cue
8             SAMPLE 1/2/3/4        NONE     Sampler is empty  Load selected track into sampler
\                                   NONE     Press button      Play track from beginning while pressed
\                                   NONE     Release button    Stop playback
\                                   SHIFT    Release button    Continue playback
\                                   SHIFT    Press button      Eject track from sampler
9             DECK                                             Switch active deck
10            SHIFT                                            Modifier that activates a 2nd layer of functions. It does not matter which of the two shift buttons is pressed.
11            KEY LOCK                                         Enable/disable key lock mode
12            HOT CUE / SAMPLE                                 Switch between hot cues and samplers
13            JOG WHEEL             NONE                       Bend or scratch (vinyl mode)
\                                   SHIFT    Deck is stopped   Fast track seek (wheel search)
14            PITCH SLIDER                                     Change playback speed
15            SYNC                                             Trigger sync mode by short/long press
16            CUE                   NONE                       Trigger cue according to configured cue mode
\                                   SHIFT                      2.1.0: Stop playback and jump to beginning of track
\                                   SHIFT    Deck is stopped   2.0.0: Delete cue point or jump to beginning of the track if no cue point is set
\                                   SHIFT    Deck is playing   2.0.0: Stop deck with a break effect
\                                            Auto DJ: stopped  2.0.0: Skip the loaded/next track
17            PLAY                  NONE                       Start/stop/continue playback
\                                   SHIFT                      2.1.0: Reverse playback direction
\                                            Deck is empty     2.0.0: Load and play selected track
\                                   SHIFT                      2.0.0: Stutter playback
\                                            Auto DJ: stopped  2.0.0: Fade now and start playing the loaded/next track
18            SLIP/CENSOR           NONE                       Censor: Enable reverse and slip mode while pressed
\                                   SHIFT                      Toggle (enable/disable) slip mode permanently
19            PITCH BEND +                   Deck is stopped   Fast forward
\                                   NONE     Deck is playing   Pitch bend up
\                                   SHIFT    Deck is playing   Pitch bend up (small)
19            PITCH BEND -                   Deck is stopped   Fast rewind
\                                   NONE     Deck is playing   Pitch bend down
\                                   SHIFT    Deck is playing   Pitch bend down (small)
20            VINYL                                            Enable/disable vinyl mode (scratching)
21            PANEL                                            *Not yet mapped*
22            VIEW                                             *Not yet mapped*
23            X-F LINK                                         *Not yet mapped*
24            AREA                                             *Not yet mapped*
25            LIST                                             *Not yet mapped*
26            BACK                  NONE                       2.1.0: Scroll up
\                                   SHIFT                      2.1.0: Move focus backward to previous panel
\                                                              2.0.0: Select previous sidebar item
26            FWD                   NONE                       2.1.0: Scroll down
\                                   SHIFT                      2.1.0: Move focus forward to next panel
\                                                              2.0.0: Select next sidebar item
27            SELECT KNOB           NONE     Knob is turned    2.1.0: Move through focused panel/list
\                                   SHIFT                      2.1.0: Scroll through focused panel/list
\                                                              2.0.0: Move through track list
\                                   NONE     Knob is pressed   2.1.0: Go to the selected item
\                                   SHIFT                      2.1.0: Move focus backward to previous panel
\                                                              2.0.0: Expand/collapse the selected sidebar item
28            LOAD                  NONE                       Load selected track into active deck
\                                   SHIFT                      Eject loaded track from active deck
29            FILTER ON                                        Enable/disable filter effect for deck 1/3 or 2/4
30            FILTER KNOB                                      Control filter effect (low/high pass) for deck 1/3 or 2/4
31            MIC LEVEL 1/2                                    *Not yet mapped*
32            MIC ON 1/2                                       *Not yet mapped*
33            MIC DUCKING                                      *Not yet mapped*
34            MIC ECHO ON 1/2                                  *Not yet mapped*
35            CUE MIX               NONE                       Enable/disable cue mix
\                                   SHIFT                      Enable solo cue mix (only this channel)
36            VU METER DISP. SWITCH                            Select channel(s) for display
37            CHANNEL FADER                                    Control channel output volume
38            CROSS FADER                                      Control balance between assigned channels
39            VU METER                                         Display channel/master output volume
40            BOOTH ASSIGN                                     Select source for booth output
41            BOOTH LEVEL                                      Control booth output volume
42            MASTER LEVEL                                     Control master output volume
43            HI KNOB                                          Control channel EQ (high freq.)
43            MID KNOB                                         Control channel EQ (mid. freq.)
43            LOW KNOB                                         Control channel EQ (low freq.)
44            LEVEL KNOB                                       Control channel gain
45            CHANNEL INPUT SELECT                             Select channel input source
============= ===================== ======== ================= =========================================================================================================================================================
