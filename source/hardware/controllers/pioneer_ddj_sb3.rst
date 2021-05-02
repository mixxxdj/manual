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

Controller Mapping
------------------

A schematic drawing with the control numbers that are used here can be found on the specified page in the User Manual in the Links section.

.. _pioneer-ddj-SB3-decks:

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

.. figure:: ../../_static/controllers/pioneer_ddj_200_mixer.svg
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Pioneer DDJ-SB3 (mixer section)
   :figclass: pretty-figures

   Mixer section (p. 10)

===  =====================================================  ============================================================================================
No.  Control                                                Function
===  =====================================================  ============================================================================================
1    :hwlabel:`MASTER` button                               Toggle Master/Cue knob of headphones between left and right
1    :hwlabel:`SHIFT` + :hwlabel:`MASTER` button            Toggle between 2- and 4-deck mode
2    :hwlabel:`HI`/:hwlabel:`MID`/:hwlabel:`LOW` knobs      Adjust high/mid/low-frequencies
3    :hwlabel:`CFX` knobs                                   Turns on the selected effects
4    :hwlabel:`HEADPHONE CUE 1` button                      Toggle headphone pre-fader listening of left deck.
4    :hwlabel:`HEADPHONE CUE 2` button                      Toggle headphone pre-fader listening of right deck.
4    :hwlabel:`SHIFT (left)` + :hwlabel:`HEADPHONE CUE 1`   Load selected track to left deck.
4    :hwlabel:`SHIFT (left)` + :hwlabel:`HEADPHONE CUE 2`   Load selected track to right deck.
4    :hwlabel:`SHIFT (right)` + :hwlabel:`HEADPHONE CUE 1`  Toggle between left deck between 1 / 3 in 4-deck mode (if LED is lit, deck 3 is active). If 4-deck mode is disabled, this behaves the same as :hwlabel:`SHIFT (left)` + :hwlabel:`HEADPHONE CUE 1`.
4    :hwlabel:`SHIFT (right)` + :hwlabel:`HEADPHONE CUE 2`  Toggle between right deck between 2 / 4 in 4-deck mode (if LED is lit, deck 4 is active). If 4-deck mode is disabled, this behaves the same as :hwlabel:`SHIFT (left)` + :hwlabel:`HEADPHONE CUE 2`.
5    Channel faders                                         Adjust the output level for each channel
6    Transition FX Button                                   Turns on :ref:`AutoDJ <djing-auto-dj>`
7    Cross fader                                            Fade between left and right deck
===  =====================================================  ============================================================================================
