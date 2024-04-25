.. _pioneer-ddj-200:

Pioneer DDJ-200
===============

.. sectionauthor::
   Daniel Giddins <daniel.giddins at nottingham.ac.uk>
   Frank Breitling <frank.breitling at gmx.de>

.. figure:: ../../_static/controllers/pioneer_ddj_200.svg
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Pioneer DDJ-200 (schematic view)
   :figclass: pretty-figures

   Pioneer DDJ-200 (schematic view)

The Pioneer DDJ-200 is a 2 deck USB and Bluetooth DJ controller designed for WeDJ, djay, edjing Mix and Rekordbox.

-  `Manufacturer's Product Page <https://www.pioneerdj.com/en-gb/product/controller/ddj-200/black/overview/>`__
-  `Manufacturer's User Manual <https://support.pioneerdj.com/hc/en-us/articles/4404919733401-How-to-use-the-Pioneer-DJ-DDJ-200-Controller-Instruction-manual/>`__
-  `Manufacturer's Firmware Update <https://www.pioneerdj.com/en/support/software/controller/ddj-200/>`__
-  `Mixxx User Forum <https://mixxx.discourse.group/t/pioneer-ddj-200-mapping/18259>`__

.. versionadded:: 2.2.5

Controller Mapping
------------------

A schematic drawing with the control numbers that are used here can be found on the specified page in the User Manual in the Links section.

.. _pioneer-ddj-200-decks:

Deck section (p. 8)
~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/pioneer_ddj_200_decks.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-200 (deck section)
   :figclass: pretty-figures

   Deck section (p. 8)

===  =================================================  ============================================================================================
No.  Control                                            Function
===  =================================================  ============================================================================================
1    Jog Wheel (top)                                    Scratch (move play position)
1    Jog Wheel (outer)                                  Pitch bend (nudge)
1    :hwlabel:`SHIFT` + Jog Wheel (top)                 Scratch (move play position) faster
1    :hwlabel:`SHIFT (left)` + Jog Wheel (outer)        Move track selection in library
2    :hwlabel:`SHIFT` button                            Switch function of controls
3    Pad 1 - 8                                          Set (if empty) or play (if set) hot cue point / loop 1 - 8
3    :hwlabel:`SHIFT` + Pad 1 - 8                       Unset / delete hot cue 1 - 8
4    :hwlabel:`CUE` button                              Set or play cue point, change cue point with JOG WHEEL (top) + cue point
4    :hwlabel:`SHIFT` + :hwlabel:`CUE` button           Return to cue point and stop
5    :hwlabel:`PLAY/PAUSE` button                       Play / pause
6    :hwlabel:`BEAT SYNC` button                        Match tempo and phase of other deck, long press to enable master sync
7    :hwlabel:`TEMPO` slider                            Adjust track playing speed (can be adjusted via :hwlabel:`SHIFT` + :hwlabel:`BEAT SYNC`)
===  =================================================  ============================================================================================


.. _pioneer-ddj-200-mixer:

Mixer section (p. 10)
~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/pioneer_ddj_200_mixer.svg
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Pioneer DDJ-200 (mixer section)
   :figclass: pretty-figures

   Mixer section (p. 10)

===  =====================================================  ============================================================================================
No.  Control                                                Function
===  =====================================================  ============================================================================================
1    :hwlabel:`MASTER` button                               Toggle main/cue knob of headphones between left and right
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
