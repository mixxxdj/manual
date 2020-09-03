.. _numark-mixtrack:

Numark Mixtrack
===============

-  `Manufacturer’s product page <http://www.numark.com/mixtrack>`__
-  `Forum thread <http://mixxx.org/forums/viewtopic.php?f=7&t=1808>`__

This controller as the same as the :ref:`Numark Mixtrack Pro <numark-mixtrack-pro>`__ but without a built-in sound card.
It has been discontinued and succeeded by the :ref:`Numark Mixtrack 3 <numark-mixtrack-pro-3>`__.

Mapping Description
-------------------

[[/media/numarkmixtrack_tech.png|]]

1.  USB cable
2.  Channel Treble
3.  Channel Mid
4.  Channel Bass
5.  Cue: send the corresponding track to the headphones
6.  Cue Gain: adjust audio level of cue channel
7.  Cue Mix: adjust mix between Cue and Audio out in the headphones.
8.  Browser Knob: help browse through your collection without using a mouse or trackpad
9.  Back: takes you up one level in your file hierarchy
10. Load A/Load B: Load the highlighted track to the corresponding Deck
11. Channel faders: control the volume of each channel
12. Master fader: adjust the output volume of mixxx
13. Crossfader
14. Jog Wheels (see below for details)
15. Scratch mode (see below for details)
16. Play/Pause
17. Stutter: press while music is playing to jump back to the cue point
18. CUE: plays from the cue point if hold. When released, jumps back to the cue point
19. SYNC: automatically matches the corresponding Deck’s tempo to the other Deck’s tempo
20. Pitch Faders
21. Pitch Bend: when pressed, the pitch will adjust -/+4%, when released, the tempo will set back to the right one
22. Keylock
23. View: dynamically set cue point for Deck A
24. Tick: dynamically set cue point for Deck B
25. Eq Kill Switches
26. Effect On/Off: turn on/off the flanger effect
27. On Deck A: control the Flagner’s LFO (unassigned on Deck B)
28. On Deck A: control the Flagner’s Depth and delay (unassigned on Deck B)
29. Loop Mode: press to alternate between manual or autolooping

    -  Manual Looping

       -  In: set loop start
       -  Out: set loop end
       -  Reloop: exit or reenter loop

    -  Auto Looping

       -  1/2 X: devide loop length by 2
       -  1 Bar: make a loop of just one bar (the current one)
       -  2 X: multiply loop length by 2

The Jogs
~~~~~~~~

Not in scratch mode
^^^^^^^^^^^^^^^^^^^

When not in scratch mode, touching the jogs won’t pause the song. Turning them will slightly adjust the tempo, which will resume slowly to its speed. This slowness to resume is somehow equivalent to
what you would expect from drivebelt turntables. I hate it, and I have not found a way to correct it… This is why I mostly mix using the pitch bend buttons, which allow for an instant resume to the
“pitch slider assigned” pitch for the track.

In scratch mode
^^^^^^^^^^^^^^^

In scratch mode, touching the jogs will pause the song. The jogs are very sensitive, and allow for scratching and launching tracks on a given moments when “cueing them in your headphones”. Be very
careful with this: never remain in scratch mode if not needed, you will touch the jogs by error and put your tracks out of sync because one has pause, or worse, produce a “blank”.

Known problems
--------------

-  The pitch on the controller has a very short run. Thus, having it configured as a +10/-10 (or more) is tricky because you will get a very low pitch precision. Configuring it as +8/-8 (Mk2 style) is
   higly recommended
-  The autolooping functions, altough implemented are quite flawed. The “loop one bar”, which is present since the 1.0b version, is making a loop between two bars, which are rarely fitted on real
   “measures”. As of mixxx 1.9, there is no possibility to adjust the bars to make them fit perfectly to the tempo
-  Pressing play while “cue previewing” should start the track for real, CDJ style. This is not implemented yet, and is marked as a TODO in Mixxx code, so it is unlikely to get implemented on the
   controller mapping side. \*NOTE: If you use the mapping included with the software, this feature is supported. Controls in this mapping are different than the community made one, so be careful.\*
-  Final remark on the hardware design: be very, very careful not to press the “Load A” or “Load B” button, instead of the corresponding track’s “cue” button. They are very near, the error is easy and
   produces the most dire effect in a party: an awful blank !
