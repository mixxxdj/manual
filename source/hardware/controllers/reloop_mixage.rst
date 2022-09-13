Reloop Mixage
=============

The **Reloop Mixage** is a 2-channel DJ controller. It offers two jog wheels, line faders, a cross-fader, controls for looping, effects, equalizers and gain controls. The **Interface Edition** version comes with an integrated soundcard, headphone connection and microphone input.

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

Most functions on this controller are self-explanatory and mapped in that way. The others are explained here:

=======================================================  =====================================================================================================================================  =========================================================================
Control                                                  Function                                                                                                                               Shift function
=======================================================  =====================================================================================================================================  =========================================================================
:hwlabel:`-` / :hwlabel:`+`                              Nudge deck while playing (slower / faster)                                                                                             -
:hwlabel:`LOOP` / :hwlabel:`IN`                          Set beatloop start at current play position and turn beatloop on                                                                       Set loop in point
:hwlabel:`RELOOP` / :hwlabel:`OUT`                       Toggle relooping on / off                                                                                                              Set loop out point
:hwlabel:`FX SEL` / :hwlabel:`MASTER`                    Toggle which effect racks are applied to deck N (effect rack 1 ➝ 2 ➝ 1+2 ⮌)                                                            Toggle if effect rack N is enabled for master
:hwlabel:`FX ON` / :hwlabel:`KEYLOCK`                    Toggle effect racks on / off for deck N                                                                                                Toggle keylock (keep pitch on speed change) on / off
:hwlabel:`-LENGTH+` / :hwlabel:`BEATMOVE`                Halve / double loop length (push knob to adjust move length instead)                                                                   Shift loop by move length beats left / right
:hwlabel:`-DRY/WET+` / :hwlabel:`PAN`                    Control dry / wet for effect rack N                                                                                                    Control super knob for effect rack N
:hwlabel:`AMOUNT` / :hwlabel:`FILTER`                    Control quick effect (can be changed in settings) super knob                                                                           -
Loupe icon :hwlabel:`🔍`                                 Hold to use jog wheel to scroll through library                                                                                        -
Disc icon :hwlabel:`💿`                                  Hold to use jog wheel to scratch deck                                                                                                  -
Left headphone icon :hwlabel:`🎧` / :hwlabel:`PREV ⯈`    Route deck 1 audio to headphone output                                                                                                 Play / stop preview deck
Right headphone icon :hwlabel:`🎧` / :hwlabel:`PREV ⏹`   Route deck 2 audio to headphone output                                                                                                 Stop preview deck
:hwlabel:`⯈⯇` / :hwlabel:`CUE 1`                         Beat-sync deck as follower (hold to sync lock)                                                                                         If hot cue 1 is set, go to hot cue 1, else set hot cue 1
:hwlabel:`CUP` / :hwlabel:`CUE 2`                        If at cue point, play when released. If not at cue point, sets a cue point                                                             If hot cue 2 is set, go to hot cue 2, else set hot cue 2
:hwlabel:`CUE` / :hwlabel:`CUE 3`                        If at cue point, plays until released. If not at cue point: If playing, goes to cue point and stops. If not playing, sets a cue point  If hot cue 3 is set, go to hot cue 3, else set hot cue 3
:hwlabel:`⏯` / :hwlabel:`CUE 4`                          Play / pause deck                                                                                                                      If hot cue 4 is set, go to hot cue 4, else set hot cue 4
=======================================================  =====================================================================================================================================  =========================================================================

The effect buttons and knobs on the left side apply to effect rack 1, the ones on the right to effect rack 2.

Trax selector
-------------

================================  ===========================================================  =========================================================================
Control                           Function                                                     Shift function
================================  ===========================================================  =========================================================================
:hwlabel:`LOAD` / :hwlabel:`⯇`    Load selected track from library into deck 1                 Load selected track from library into deck 1 and play
:hwlabel:`TRAX`                   Turn to browse library. Press to play / pause track preview  -
:hwlabel:`LOAD` / :hwlabel:`⯈`    Load selected track from library into deck 2                 Load selected track from library into deck 2 and play
================================  ===========================================================  =========================================================================

Scrolling the library will resize it and hide the decks for better browsing. The decks will be shown again after 4s, or when selecting a song into a deck.

Jog wheel and pitch slider
--------------------------

Touch and move the jog wheel while pressing the Loupe icon :hwlabel:`🔍` to scratch (either deck playing or not).
Touch and move the jog wheel while pressing the Disc icon :hwlabel:`💿` to scroll through the library (either deck playing or not).

The pitch sliders let you adjust pitch. The :hwlabel:`-` / :hwlabel:`+` buttons let you temporarily adjust the the speed one step higher / lower (aka nudge the deck).

-  `Manufacturer's product page <productpage_url_>`_
-  `Forum thread <forum_url_>`_

.. _productpage_url: https://www.reloop.com/reloop-mixage-ie
.. _forum_url: https://mixxx.discourse.group/t/reloop-mixage-mapping/14779
