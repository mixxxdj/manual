.. _reloop-ready:

Reloop Ready
=============

.. sectionauthor::
   Nikolaus Einhauser <nikolaus.einhauser@mixxx.org>

The Reloop Ready controller is an entry-level 2-Deck :term:`MIDI` controller
featuring a built-in 4-channel USB audio interface.

-  `Manufacturer’s product page <https://www.reloop.com/reloop-ready>`__
-  `Serato DJ Hardware Page <https://serato.com/dj/hardware/reloop-ready>`__
-  `Instruction Manual <https://www.reloop.com/media/catalog/product/pdf/2/4/3/243598_Reloop_IM.pdf>`__

..
    -  `Mapping Forum Thread <>`__ TODO

.. versionadded:: 2.4.1


Audio Setup
-----------

For the controllers internal Audio interface to interact properly with Mixxx,
the following channel assignments are required:

===================== ================
Output Channels       Assigned to
===================== ================
1-2                   Main
3-4                   Headphones
===================== ================

.. figure:: ../../_static/controllers/reloop_ready_front.svg
    :align: center
    :width: 100%
    :figwidth: 100%
    :alt: Reloop-Ready (schematic view)
    :figclass: pretty-figures

    Reloop-Ready (schematic view)


========  ==================================================  ==========================================
No.       Control                                             Function
========  ==================================================  ==========================================
1 & 2     :hwlabel:`GAIN`, :hwlabel:`High`, :hwlabel:`LOW`    Gain / EQ, controls the Eq depending on the chosen setting TODO
3         :hwlabel:`BROWSE` Encoder                           Navigate the library view up and down
3         :hwlabel:`BROWSE` Encoder Button                    See :mixxx:coref:`[Library],GoToItem`
3         :hwlabel:`SHIFT` + :hwlabel:`BROWSE` Encoder        Move the library Focus horizontally
3         :hwlabel:`SHIFT` + :hwlabel:`BROWSE` Encoder Knob   (Un-)maximize the Library
4         :hwlabel:`LOAD` Button                              Load the selected track onto the corresponding deck
4         :hwlabel:`SHIFT` + :hwlabel:`LOAD` Button           Unload the currently loaded track from the deck
5         :hwlabel:`FILTER` Knob                              QuickEffect superknob (filter by default, can be changed in the UI or the preferences)
6         :hwlabel:`CUE` Button                               Enable Deck output to headphone (:term:`PFL`)
7         :hwlabel:`SHIFT` Button                             Access alternative functionality of some buttons.
8         :hwlabel:`TEMPO` Fader                              Adjust the tempo of the Deck (direction can be changed in the Deck preferences)
9         Channel faders                                      Adjust the output level for each channel.
10        Crossfader                                          Fades between left and right deck. (make sure the orientation is set correctly in Mixxx)
12        Pads                                                See the PadSection (TODO)
13        :hwlabel:`VINYL` Button                             Toggle vinyl control mode (if enabled, touching the top of the platter stops the playback)
13        :hwlabel:`SHIFT` + :hwlabel:`VINYL` Button          Toggle Slip Mode
14        :hwlabel:`KEY LOCK` Button                          Toggle whether the pitch of the track should be immune to tempo changes
14        :hwlabel:`SHIFT` + :hwlabel:`KEY LOCK` Button       Change Deck Pitch to match currently playing deck
15        :hwlabel:`PARAMETER 1/2` Buttons                    See the PadSection (TODO)
16        :hwlabel:`LOOP` Encoder                             Change Loop size
16        :hwlabel:`LOOP` Button                              Set loop at the current play position / disable currently active loop
16        :hwlabel:`SHIFT` + :hwlabel:`LOOP` Button           Tap to set the track BPM
17        :hwlabel:`FX UNIT`                                  TODO
18        :hwlabel:`LEVEL`                                    EffectUnit Meta Knob
19        :hwlabel:`MODE`                                     See the PadSection (TODO)
20        :hwlabel:`SYNC` Button (short press)                Copy the Tempo from the other deck to this deck
20        :hwlabel:`SYNC` Button (long press)                 Make this deck a tempo follower
21        :hwlabel:`CUE` Button                               Cue Button
22        :hwlabel:`CUE` Button                               Play Button
22        :hwlabel:`SHIFT` + :hwlabel:`CUE` Button            Censor (play in reverse then jump to were the track would've been)
========  ==================================================  ==========================================


Pad Section
~~~~~~~~~~~

.. figure:: ../../_static/controllers/reloop_ready_pads.svg
   :align: center
   :width: 65%
   :figwidth: 100%
   :alt: Reloop Ready Pads
   :figclass: pretty-figures


TODO
