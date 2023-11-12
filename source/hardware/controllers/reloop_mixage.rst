Reloop Mixage
=============

The Reloop Mixage line of controllers contains 2-channel DJ controller. It offers two jog wheels, line faders, a cross-fader, controls for looping, effects, equalizers and gain controls. The Interface Edition version comes with an integrated soundcard, headphone connection and microphone input and exists in version MK1 (unmarked) and MK2 (marked on back of device)

.. figure:: ../../_static/controllers/reloop_mixage_top.jpg
   :align: center
   :figwidth: 100%
   :alt: Reloop Mixage IE (top view)
   :figclass: pretty-figures

   Reloop Mixage top view (© Reloop, used with permission)

Audio
-----

This controller is a MIDI and audio class compliant device so it is compatible as-is with Linux, MacOS and Windows. On Windows, the manufacturer ships an :term:`ASIO` low-latency driver that can be found on the `manufacturer’s product
page <productpage_url_>`_.

The microphone :hwlabel:`🎤` input can be set to different modes. To make it usable in Mixxx, set it to **SW**. The :hwlabel:`MASTER` and :hwlabel:`PHONES` level controls work directly on the audio hardware and can't be mapped in Mixxx.


Mixer Section
-------------

All mapped controls use MIDI channel #1 (can be changed on the back of the device). Most functions on this controller are self-explanatory and mapped in that way (you might want to check the official manual). The others are explained here:

=======================================================  ============================================================================================================================================  ============================================================================
Control                                                  Function                                                                                                                                      SHIFT function
=======================================================  ============================================================================================================================================  ============================================================================
:hwlabel:`-` / :hwlabel:`+`                              Nudge deck while playing (slower / faster)                                                                                                    Adjust deck key (down / up)
:hwlabel:`LOOP` / :hwlabel:`IN`                          Set beatloop start at current play position and activate beatloop or turn if off if currently active                                          Set loop in point
:hwlabel:`RELOOP` / :hwlabel:`OUT`                       Toggle relooping on / off. Button is lit if there's a active loop set in the deck and blink if there's an inactive loop set in the deck       Set loop out point
:hwlabel:`FX SEL` / :hwlabel:`MASTER`                    Select effect in effect rack N for adjustment. Button is lit if an effect is selected                                                         Toggle if deck N is sync master
:hwlabel:`FX ON` / :hwlabel:`KEYLOCK`                    Toggle effect rack on / off for deck N                                                                                                        Toggle keylock (keep pitch on speed change) on / off
:hwlabel:`-LENGTH+` / :hwlabel:`BEATMOVE`                Halve / double loop length (push down to adjust move length instead). Click to clear beatloop                                                 Shift loop by move length beats left / right
:hwlabel:`-DRY/WET+` / :hwlabel:`PAN`                    Control dry / wet for effect rack N (push down to select effect preset for effect rack N). Click to toggle effect(s) in effect rack on / off  Select quick effect preset for deck N. Click to toggle quick effect on / off
:hwlabel:`AMOUNT` / :hwlabel:`FILTER`                    Control effect super knob                                                                                                                     Control quick effect super knob
Loupe icon :hwlabel:`🔍`                                 Toggle to use jog wheel to scroll through deck                                                                                                -
Disc icon :hwlabel:`💿`                                  Toggle to use jog wheel to scratch deck                                                                                                       -
Left headphone icon :hwlabel:`🎧` / :hwlabel:`PREV ⯈`    Route deck 1 audio to headphone output                                                                                                        Play / stop preview deck
Right headphone icon :hwlabel:`🎧` / :hwlabel:`PREV ⏹`   Route deck 2 audio to headphone output                                                                                                        Stop preview deck
:hwlabel:`⯈⯇` / :hwlabel:`CUE 1`                         Beat-sync deck as follower (hold to sync lock)                                                                                                If hot cue 1 is set, go to hot cue 1, else set hot cue 1
:hwlabel:`CUP` / :hwlabel:`CUE 2`                        If at cue point, play when released. If not at cue point, sets a cue point                                                                    If hot cue 2 is set, go to hot cue 2, else set hot cue 2
:hwlabel:`CUE` / :hwlabel:`CUE 3`                        If at cue point, plays until released. If not at cue point: If playing, goes to cue point and stops. If not playing, sets a cue point         If hot cue 3 is set, go to hot cue 3, else set hot cue 3
:hwlabel:`⏯` / :hwlabel:`CUE 4`                          Play / pause deck. Hold the disc button :hwlabel:`💿` to soft start or stop the deck                                                          If hot cue 4 is set, go to hot cue 4, else set hot cue 4
=======================================================  ============================================================================================================================================  ============================================================================

The effect buttons and knobs on the left side apply to effect rack 1, the ones on the right to effect rack 2.

Beatloop adjust mode
--------------------

When a beatloop has been set, press :hwlabel:`SHIFT` + :hwlabel:`-DRY/WET+` / :hwlabel:`PAN` to enable beatloop adjust mode. The :hwlabel:`LOOP` / :hwlabel:`IN` and :hwlabel:`RELOOP` / :hwlabel:`OUT` buttons will blink. Now you can:

- Shift the loop using the jog wheel
- Press :hwlabel:`LOOP` / :hwlabel:`IN` to shift the loop in point using the jog wheel. The :hwlabel:`LOOP` / :hwlabel:`IN` will blink
- Press :hwlabel:`RELOOP` / :hwlabel:`OUT` to shift the loop in point using the jog wheel. The :hwlabel:`RELOOP` / :hwlabel:`OUT` will blink

Press :hwlabel:`-DRY/WET+` / :hwlabel:`PAN`, the loupe button :hwlabel:`🔍` or disc button :hwlabel:`💿` again to leave betloop adjust mode

Trax selector
-------------

================================  ========================================================================================================  =========================================================================
Control                           Function                                                                                                  Shift function
================================  ========================================================================================================  =========================================================================
:hwlabel:`LOAD` / :hwlabel:`⯇`    Load selected track from library into deck 1                                                              Load selected track from library into deck 1 and play
:hwlabel:`TRAX`                   Turn to browse library. Press to play / pause track preview. Double-press to maximize / minimize library  Turn to browse side pane. Press to open / close folder
:hwlabel:`LOAD` / :hwlabel:`⯈`    Load selected track from library into deck 2                                                              Load selected track from library into deck 2 and play
================================  ========================================================================================================  =========================================================================

As a warning the :hwlabel:`LOAD` LEDs will be on if that deck is currently playing.

Jog wheel and pitch slider
--------------------------

- With the loupe button :hwlabel:`🔍` active: Touch the side of the jog wheel to nudge the deck. Touch the top of the jog wheel to scratch (either deck playing or not).
- With the disc button :hwlabel:`💿` active: Scroll through the track (either deck playing or not) silently.

The pitch sliders let you adjust pitch. The :hwlabel:`-` / :hwlabel:`+` buttons let you temporarily adjust the the speed one step higher / lower (aka nudge the deck).

User-adjustable script settings
-------------------------------

The `Reloop-Mixage.scripts.js` controller script provides the following settings:

-  Scratch behaviour can be changed to a more regular, turntable-like mode by changing the setting `scratchByWheelTouch` to `true`. Note that the jog wheels are not very sensitive to touch though (sensitivity can be adjusted on the back of the controller in the MK1 version).
-  Scratch speed can be adjusted by changing the setting `scratchTicksPerRevolution`. Smaller values "scratch more" of the track, larger values "scratch less".
-  Jog wheel scroll speed can be adjusted by changing the setting `jogWheelScrollSpeed`. The higher, the faster.

Controller diagnostic functions
-------------------------------

Turn off the controller and hold one of these buttons while turning on the controller:

-  Right :hwlabel:`SHIFT` to display the firmware version on the four deck play / cue buttons. The number is display in little-endian binary, e.g 0101 meaning 5.
-  Right :hwlabel:`⏯` to show jog wheel touch values. This can be used to adjust sensitivity on the MK1 version
-  Left :hwlabel:`⯈⯇` to light up all LEDs. Can be helpful when repairing the controller or replacing the LEDs

Info for mapping developers
---------------------------

.. figure:: ../../_static/controllers/reloop_mixage_overview.svg
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Reloop Mixage button overview
   :figclass: pretty-figures

   Reloop Mixage button overview

The numbers from the overview correspond to the product manual and mapping XML file Txx numbers.

-  `Manufacturer's product page <productpage_url_>`_
-  `Forum thread <forum_url_>`_

.. _productpage_url: https://www.reloop.com/reloop-mixage-ie
.. _forum_url: https://mixxx.discourse.group/t/reloop-mixage-mapping/14779
