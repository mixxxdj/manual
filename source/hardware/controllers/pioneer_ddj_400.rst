Pioneer DDJ-400
===============

.. sectionauthor::
   jusko <justin.kourie@gmail.com>

.. figure:: ../../_static/controllers/pioneer_ddj_400.svg
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Pioneer DDJ-400 (schematic view)
   :figclass: pretty-figures

   Pioneer DDJ-400 (schematic view)

The Pioneer DDJ-400 is a 2 deck USB controller with integrated audio interface designed for rekordbox.

- `Manufacturer's Product Page <https://www.pioneerdj.com/en-us/product/controller/ddj-400/black/overview/>`__
- `Manufacturer's User Manual <http://docs.pioneerdj.com/Manuals/DDJ_400_DRI1551A_manual/>`__
- `Manufacturer's Firmware <https://www.pioneerdj.com/en/support/software/controller/ddj-400/>`__
- `Midi Mappings <https://www.pioneerdj.com/-/media/pioneerdj/software-info/controller/ddj-400/ddj-400_midi_message_list_e1.pdf>`__
- `Hardware Diagram <https://www.pioneerdj.com/-/media/pioneerdj/software-info/controller/ddj-400/ddj-400_hardwarediagram_rekordboxdj_e1.pdf?la=en-us>`__
- `Mapping Forum Thread <https://mixxx.org/forums/viewtopic.php?f=7&t=12113>`__

.. versionadded:: 2.3.0

Drivers
-------

You can download the latest firmware from
`the manufacturer's website <https://www.pioneerdj.com/en/support/software/controller/ddj-400/>`__.

Unfortunately Pioneer offers no Linux support, so to update your controller's
firmware you will need access to a Windows or Mac machine. Simply download the
drivers, attach your device and run the installer.

.. note:: It is highlty recommended that you update your controller's firmware.
          This will fix a bug in the release drivers which causes the tempo
          sliders to send signals without being touched!

Controller Mapping
------------------

The schematic drawings used here can be referenced in the
`original manual <http://docs.pioneerdj.com/Manuals/DDJ_400_DRI1551A_manual/>`__
on the given page number.

Browser section (p. 6)
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/pioneer_ddj_400_browser.svg
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Pioneer DDJ-400 (browser section)
   :figclass: pretty-figures

   Pioneer DDJ-400 (browser section)

========  ==================================================  ==========================================
No.       Control                                             Function
========  ==================================================  ==========================================
1         :hwlabel:`LOAD` buttons                             Load song into deck.
2         Rotary Selector                                     Press to toggle focus between the library sidebar and associated panels. Turn to move focus up or down.
========  ==================================================  ==========================================

Deck sections (p. 6)
~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/controllers/pioneer_ddj_400_deck.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Pioneer DDJ-400 (deck section)
   :figclass: pretty-figures

   Pioneer DDJ-400 (deck section)

====  =======================================================  ======================================================================
No.   Control                                                  Function
====  =======================================================  ======================================================================
1     :hwlabel:`BEAT SYNC`                                     Tap to sync tempo to the other playing track. Hold to enable sync lock.
1     :hwlabel:`SHIFT` + :hwlabel:`BEAT SYNC`                  Cycles through tempo ranges: +/-6%, +/-10%, +/-16%, +/-25%
2     :hwlabel:`CUE/LOOP CALL`:hwlabel:`>`                     Doubles the currently active loop.
2     :hwlabel:`SHIFT` + :hwlabel:`CUE/LOOP CALL`:hwlabel:`>`  Jumps a phrase forwards
3     :hwlabel:`CUE/LOOP CALL`:hwlabel:`<`                     Halves the currently active loop.
3     :hwlabel:`SHIFT` + :hwlabel:`CUE/LOOP CALL`:hwlabel:`<`  Jumps a phrase backwards
4     :hwlabel:`RELOOP/EXIT`                                   Activates/deactivates currently set loop
4     :hwlabel:`shift` + :hwlabel:`RELOOP/EXIT`                Activates current loop and stop playback
5     :hwlabel:`OUT`                                           Sets end of loop to the current playback position.
                                                               If quantize is enabled, it is set to the closest beat.
                                                               If held during an active loop, sets the new end point when released.
5     :hwlabel:`shift` + :hwlabel:`OUT`                        Toggle :hwlabel:`OUT ADJUST` mode on active loop. Adjust the loop's end position using the jog wheel.
6     :hwlabel:`IN/-4BEAT`                                     Sets start of loop to the current playback position. If quantize is enabled, it is set to the closest beat.
                                                               If held during an active loop, sets the new start point when released.
6     :hwlabel:`shift` + :hwlabel:`IN/-4BEAT`                  Toggle :hwlabel:`IN ADJUST` mode on active loop. Adjust the loop's start position using the jog wheel.
7     Jog Wheel (top)                                          Scratch (move play position)
7     Jog Wheel (outer)                                        Nudge tempo up or down temporarily
8     :hwlabel:`HOT CUE` mode                                  Sets pads to hot cue mode. *TODO: See using hotcues*
9     :hwlabel:`BEAT LOOP` mode                                Sets pads to beat loop mode. *TODO: See using beat loop*
10    :hwlabel:`BEAT JUMP` mode                                Sets pads to beat jump mode. *TODO: See using beat jump*
11    :hwlabel:`SAMPLER` mode                                  Sets pads to sampler mode. *TODO: See using sampler*
12    :hwlabel:`TEMPO` slider                                  Adjust playback speed
13    Performance pads                                         Functionality differs depending on the pad mode selected by 8-11 *See pad mode descriptions*
14    :hwlabel:`PLAY/PAUSE`                                    Play/pauses a track
15    :hwlabel:`CUE`                                           Sets cue point if paused. Return to cue point and stop if playing. Play while held on the set cue point.
====  =======================================================  ======================================================================
