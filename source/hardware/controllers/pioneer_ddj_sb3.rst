Pioneer DDJ-SB3
===============

.. sectionauthor::
   Javier Vilalta <javier at dancephy.com>

.. figure:: ../../_static/controllers/pioneer_ddj_sb3.svg
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (schematic view)
   :figclass: pretty-figures

   Pioneer DDJ-SB3 (schematic view)

The Pioneer DDJ-SB3 is a 4 deck USB DJ controller.

-  `Manufacturer's Product Page <https://www.pioneerdj.com/en-us/product/controller/ddj-sb3/black/overview/>`__
-  `Manufacturer's User Manual <https://docs.pioneerdj.com/Manuals/DDJ_SB3_DRI1533A_manual/>`__
-  `Manufacturer's Firmware Update <https://www.pioneerdj.com/en-us/product/controller/ddj-sb3/black/support/>`__
-  `Mixxx User Forum <https://mixxx.discourse.group/t/ddj-sb3/18346>`__

.. versionadded:: 2.3.0

Audio Setup
-----------

The mapping relies on the following channel assignments:

===================== ================
Output Channels       Assigned to
===================== ================
1-2                   Master
3-4                   Headphones
===================== ================

This controller mapping does not support any inputs. The controller itself has a microphone input, but that cannot be controlled via MIDI.

Controller Mapping
------------------

A schematic drawing with the control numbers that are used here can be found on the specified page in the User Manual in the Links section.

.. _pioneer-ddj-sb3-decks:

Deck section (p. 6)
~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_decks.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (deck section)
   :figclass: pretty-figures

   Deck section (p. 6)

===  =================================================  ============================================================================================
No.  Control                                            Function
===  =================================================  ============================================================================================
1    :hwlabel:`TEMPO` slider                            Adjust track playing speed (can be adjusted via :hwlabel:`SHIFT` + :hwlabel:`BEAT SYNC`)
2    Jog Wheel (top)                                    Pitch bend (nudge)
2    :hwlabel:`VINYL` + Jog Wheel (top)                 Scratch (move play position)
2    Jog Wheel (outer)                                  Pitch bend (nudge)
2    :hwlabel:`SHIFT` + Jog Wheel (top)                 Fast-forward or fast reverse track
3    :hwlabel:`HOT CUE`                                 Set hot cue mode
3    :hwlabel:`SHIFT` + :hwlabel:`HOT CUE`              Set BEAT JUMP mode
4    :hwlabel:`FX FADE`                                 Set FX fade mode
4    :hwlabel:`SHIFT` + :hwlabel:`FX FADE`              Set roll mode
5    :hwlabel:`PAD SCRATCH`                             Set pad scratch mode
5    :hwlabel:`SHIFT` + :hwlabel:`PAD SCRATCH`          Set slicer mode
6    :hwlabel:`SAMPLER`                                 Set sampler mode
6    :hwlabel:`SHIFT` + :hwlabel:`SAMPLER`              Set trans mode
7    :hwlabel:`VINYL`                                   Toggle vinyl mode
7    :hwlabel:`SHIFT` + :hwlabel:`VINYL`                Toggle slip mode
8    :hwlabel:`AUTO LOOP`                               Toggle auto loop
8    :hwlabel:`SHIFT` + :hwlabel:`AUTO LOOP`            Cancel loop or reloop
9    :hwlabel:`2X`                                      Double loop length
10   :hwlabel:`1/2X`                                    Halve loop length
11   Pad 1 - 8                                          Perform different functions depending on current mode
12   :hwlabel:`PLAY/PAUSE` button                       Play / pause
12   :hwlabel:`SHIFT` + :hwlabel:`PLAY/PAUSE` button    Return to temporary cue point
13   :hwlabel:`CUE` button                              Set, play and call out cue points
13   :hwlabel:`SHIFT` + :hwlabel:`CUE` button           Return to cue point and stop or load previous track
14   :hwlabel:`SYNC` button                             Match tempo and phase of adjacent deck
14   :hwlabel:`SHIFT` + :hwlabel:`SYNC` button          Turn off sync mode
15   :hwlabel:`SHIFT` + button                          Switch function of controls
16   :hwlabel:`DECK X`                                  Switch deck
17   :hwlabel:`KEY LOCK`                                Toggle key lock
17   :hwlabel:`SHIFT` + :hwlabel:`KEY LOCK`             Toggle tempo slider range
===  =================================================  ============================================================================================


.. _pioneer-ddj-sb3-mixer:

Mixer section (p. 8)
~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_mixer.svg
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (mixer section)
   :figclass: pretty-figures

   Mixer section (p. 8)

===  =====================================================  ============================================================================================
No.  Control                                                Function
===  =====================================================  ============================================================================================
1    :hwlabel:`TRIM` knob                                   Adjust inidvidual channel output gain
2    :hwlabel:`HI`/:hwlabel:`MID`/:hwlabel:`LOW` knobs      Adjust high/mid/low-frequencies
3    :hwlabel:`FILTER` knob                                 Low pass / high pass filter for each channel
4    :hwlabel:`HEADPHONE CUE 1` button                      Toggle headphone pre-fader listening of left deck.
4    :hwlabel:`HEADPHONE CUE 2` button                      Toggle headphone pre-fader listening of right deck.
5    Channel faders                                         Adjust the output level for each channel
6    Cross fader                                            Fade between left and right deck
7    :hwlabel:`MASTER` knob                                 Adjust master output level
8    :hwlabel:`HEADPHONES` knob                             Adjust headphones output level
9    :hwlabel:`MASTER` button                               Output master to headphones
===  =====================================================  ============================================================================================

Performance Pads
~~~~~~~~~~~~~~~~

You can use the Pad Mode Select buttons to select a mode for the
performance pads. Performance pads are numbered from top left to bottom right. First row is 1-4 and the second row is 5-8.

Hot Cue Mode
^^^^^^^^^^^^

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_hotcue.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (performance pads)
   :figclass: pretty-figures

   Pioneer DDJ-SB3 (performance pads)

Bookmark positions in the track and jump to them.

========  ===============================================================  ==========================================
No.       Control                                                          Function
========  ===============================================================  ==========================================
1-4       Pad (unlit)                                                      Save current position as hot cue.
1-4       Pad (lit)                                                        Jump to hot cue.
1-4       :hwlabel:`SHIFT` + Pad (lit)                                     Clear hot cue.
5         Pad                                                              Previous track
6         Pad                                                              Search left
7         Pad                                                              Search right
8         Pad                                                              Censor
========  ===============================================================  ==========================================

Beatjump Mode
^^^^^^^^^^^^^

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_beatjump.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (performance pads)
   :figclass: pretty-figures

   Pioneer DDJ-SB3 (performance pads)

========  ===============================================================  ==========================================
No.       Control                                                          Function
========  ===============================================================  ==========================================
1         Pad                                                              Decrease beatjump
2         Pad                                                              Increase beatjump
3         Pad                                                              Jump left
4         Pad                                                              Jump right
5         Pad                                                              Go back to beginning of track
6         Pad                                                              Search left
7         Pad                                                              Search right
8         Pad                                                              Censor
========  ===============================================================  ==========================================

FX Fade Mode
^^^^^^^^^^^^

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_fade.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (Fade mode performance pads)
   :figclass: pretty-figures

   Pioneer DDJ-SB3 (Fade mode performance pads)

========  ===============================================================  ==========================================
No.       Control                                                          Function
========  ===============================================================  ==========================================
1         Pad (unlit)                                                      Save current position as hot cue.
2         Pad (lit)                                                        Jump to hot cue.
3         :hwlabel:`SHIFT` + Pad (lit)                                     Clear hot cue.
4         Pad                                                              Previous track
5         Pad                                                              Search left
6         Pad                                                              Search right
7         Pad                                                              Search right
8         Pad                                                              Censor
========  ===============================================================  ==========================================

Loop Roll Mode
^^^^^^^^^^^^^^

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_roll.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (performance pads)
   :figclass: pretty-figures

   Pioneer DDJ-SB3 (performance pads)

========  ===============================================================  ==========================================
No.       Control                                                          Function
========  ===============================================================  ==========================================
1         Pad                                                              1/16 beat loop roll
2         Pad                                                              1/8 beat loop roll
3         Pad                                                              1/4 beat loop roll
4         Pad                                                              1/2 beat loop roll
5         Pad                                                              1 beat loop roll
6         Pad                                                              2 beat loop roll
7         Pad                                                              4 beat loop roll
8         Pad                                                              8 beat loop roll
========  ===============================================================  ==========================================


Pad Scratch Mode
^^^^^^^^^^^^^^^^

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_scratch.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (performance pads)
   :figclass: pretty-figures

   Pioneer DDJ-SB3 (performance pads)

Slicer Mode
^^^^^^^^^^^

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_slicer.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (performance pads)
   :figclass: pretty-figures

   Pioneer DDJ-SB3 (performance pads)

Sampler Mode
^^^^^^^^^^^^

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_sampler.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (performance pads)
   :figclass: pretty-figures

   Pioneer DDJ-SB3 (performance pads)

========  ===============================================================  ==========================================
No.       Control                                                          Function
========  ===============================================================  ==========================================
1         Pad                                                              Play sample 1
1         :hwlabel:`SHIFT` + Pad                                           Stop sample 1
2         Pad                                                              Play sample 2
2         :hwlabel:`SHIFT` + Pad                                           Stop sample 2
3         Pad                                                              Play sample 3
3         :hwlabel:`SHIFT` + Pad                                           Stop sample 3
4         Pad                                                              Play sample 4
4         :hwlabel:`SHIFT` + Pad                                           Stop sample 4
5         Pad                                                              Load sample 1
5         :hwlabel:`SHIFT` + Pad                                           Unload sample 1
6         Pad                                                              Load sample 2
6         :hwlabel:`SHIFT` + Pad                                           Unload sample 2
7         Pad                                                              Load sample 3
7         :hwlabel:`SHIFT` + Pad                                           Unload sample 3
8         Pad                                                              Load sample 4
8         :hwlabel:`SHIFT` + Pad                                           Unload sample 4
========  ===============================================================  ==========================================


Trans Mode
^^^^^^^^^^

.. figure:: ../../_static/controllers/pioneer_ddj_sb3_trans.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (performance pads)
   :figclass: pretty-figures

   Pioneer DDJ-SB3 (performance pads)