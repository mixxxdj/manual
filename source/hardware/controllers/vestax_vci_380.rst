Vestax VCI-380
==============

The Vestax VCI-380 is a 2-deck controller with integrated audio interface and stand-alone mixer.  
It requires its own external barrel plug power adapter.  

Outputs: Balanced XLR and RCA output, and both 3.5 and 6.35mm headphone jacks.  

Inputs: 2 microphones, and RCA inputs with line/phono switch.  

The output will refuse to work at any other sample rate than 48Khz, so there's an option to automatically set Mixxx output sample rate to 48Khz when using the mapping.  

As Vestax went out if business in 2014, there is no support for this hardware anymore. But as it is class compliant, no driver should be needed.  

Mapping
=======

Mixer functions
---------------

Main knobs and sliders work straightforward.  

Hold :kbd:`SHIFT` while turning EQ knobs (:kbd:`HIGH`/:kbd:`MID`/:kbd:`LOW`) for EQ kill mode  

Hold :kbd:`SHIFT` while moving the crossfader to control output balance  

Wheels
------

You can turn the wheels with our without touching the sensitive metallic part.  
Get sure that the sensibility is correctly set with :kbd:`TOUCH SENSOR ADJ` knobs on the front panel: the wheels must turn red when touched, and only then. If not, the tracks will refuse to play if Mixxx thinks that a platter is touched!  

The LED rings are simulating a vinyl record spin.

================================================== =================================
Action                                             Effect
-------------------------------------------------- ---------------------------------
Touch and turn wheels                              scratching
Touch and turn wheels with :kbd:`SHIFT`            scratching at 10X speed
Turn wheels without touching                       temporary rate adjustments (jog)
Turn wheels without touching and with :kbd:`SHIFT` beatjump
Turn wheels with :kbd:`JOG SCROLL`                 library scrolling
================================================== =================================

:kbd:`SYNC` / :kbd:`CUE` / :kbd:`>||`
-------------------------------------

================================================== =================================
Key                                                Function
-------------------------------------------------- ---------------------------------
:kbd:`>/\|\|`                                      Play/pause
:kbd:`SHIFT`+:kbd:`>/\|\|`                         Soft start / brake
:kbd:`CUE`                                         go to cue point
:kbd:`SHIFT` + :kbd:`CUE`                          set the cue point
:kbd:`SYNC`                                        blinks on each beat. Press to adjust beatgrid position.
:kbd:`SHIFT`+:kbd:`SYNC`                           activates auto-sync
:kbd:`VINYL`                                       toggles slip mode
================================================== ================================

"Tempo" sliders (pitch)
-----------------------

The sliders adjust pitch  

================================================== =================================
Action                                             Effect
-------------------------------------------------- ---------------------------------
:kbd:`SHIFT` + move slider                         reset speed to 1X  
:kbd:`SHIFT` + :kbd:`RANGE`                        toggle keylock  
:kbd:`RANGE`                                       toggle quantization
================================================== =================================

While the pitch is different from zero, the red PAD FX LED will light up as a reminder that the deck is pitched 

Navigation area
---------------

Library
^^^^^^^
================================================== =================================
Action                                             Effect
-------------------------------------------------- ---------------------------------
:kbd:`SCROLL` turn                                 move up/down
:kbd:`BACK` and :kbd:`FWD`                         move left/right
Left :kbd:`PAD FX` turn                            move up/down (equivalent to turning SCROLL)
:kbd:`SHIFT` + Left :kbd:`PAD FX` turn             page up/down
Right :kbd:`PAD FX` turn                           move left/right
:kbd:`SHIFT` + Right :kbd:`PAD FX` turn            adjust waveform zoom
:kbd:`SHIFT` + :kbd:`PAD FX` push                  clone other deck
:kbd:`AREA` or any :kbd:`PAD FX` push              Default action
:kbd:`SCROLL` push                                 change focus zone (:kbd:`TAB`)
:kbd:`SORT`                                        Sort according to active column
:kbd:`JOGSCROLL` + :kbd:`LOAD A` / :kbd:`LOAD B`     Load selected track into deck A or B
:kbd:`VIEW`                                        Load and play selected track on preview deck. Push again to stop.
================================================== =================================

End-of-track alerts
^^^^^^^^^^^^^^^^^^^

When a track is playing with less than 30 seconds remaining, the library LEDs will blink.  

For deck 1: :kbd:`AREA` and :kbd:`BACK`  

For deck 2: :kbd:`SORT` and :kbd:`FWD`  

Quick Effects
-------------

For both decks:  

================================================== =================================
Action                                             Effect
-------------------------------------------------- ---------------------------------
:kbd:`FX SELECT` turn                              Select a quick effect preset  
:kbd:`FX SELECT` push                              Reset quick effect preset selection  
:kbd:`FX ON/OFF`                                   Toggle quick effect ON/OFF
:kbd:`FX DEPTH` turn                               adjust the effect parameter ("superknob")
================================================== =================================

Performance pads and strips
---------------------------
They work in different modes, according to the selection buttons on the top of the controller.

My modes are not always related to the names they bear on the controller :
The left strip is used in any mode for needle drop (quick navigate) on the preview deck

To do a needle drop on the main decks, touch the strip with :kbd:`SHIFT`

:kbd:`HOT CUE` mode: HOTCUES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
8 hot cues available, one per pad. The pads will light up when their hotcue is set.  
the colors of the lights will approximate the colors defined for the hot cues.  

- push a lighted pad to play the hotcue
- push a blank pad to set a new hotcue to the current position.
- push :kbd:`SHIFT` + lighted pad to clear a hotcue
- loop hotcues: the pad will turn green when the loop is active, push to disable loop

:kbd:`SLICER` mode : BEAT GRID tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The 8 pads will illuminate in sequence following the beat grid. To reset the sequence to beat 1, push the :kbd:`SLICER` button again.
- Push a button of higher row: BPM tap. Tap it in rhythm to adjust the calculated BPM of the track  
- Push a button of lower row: align beatgrid. Tap it to align the beatgrid bars to the current position.    

:kbd:`AUTO LOOP`: loop mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The green buttons on the left control loop activation.  

- upper (button 1): creates or disables a loop (beatloop_activate)  
- lower (button 5): reactivates existing loop (reloop_toggle)  

The yellow buttons control beatloop size

- left (button 3): halves the size
- right (button 4): doubles the size

The white buttons control the loop position  

- left (button 7): move left  
- right (button 8): move right  

:kbd:`ROLL`: Stems mode
^^^^^^^^^^^^^^^^^^^^^^^
If the loaded track has stems, the pads will light up in vertical pairs with the corresponding stem colors  
Stems 1 to 4, left to right  

- Push the lower button to mute/unmute the stem  
- Maintain the upper button (it will turn white) for FX control. While the button is pressed:  

  - the quick effect buttons (FX Depth, FX select and FX on/off) apply to the selected stem instead of the whole track. (see: quick effects)  
  - the parameter strip sets the individual volume of the selected stem  


:kbd:`SAMPLER` mode (:kbd:`SHIFT` + :kbd:`HOT CUE`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In Sampler mode, each pad is controlling one of the samplers.  
They are mapped so the pads are organized in the same layout as the 8 samplers on mixxx default skin.  

====== ================= ==================== =========================
Color  Meaning           Pad action           :kbd:`SHIFT` + pad action
------ ----------------- -------------------- -------------------------
OFF    no track loaded   load selected track
green  a track is loaded play                 eject
yellow playing           restart              stop
====== ================= ==================== =========================

