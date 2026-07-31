**Numark Mixtrack Go**
===================================

.. sectionauthor::
   mixo101 <https://github.com/josefveiga>

**Numark Mixtrack Go** is a USB :term:`MIDI` controller with an integrated audio interface.
It improves on the concept of the Numark DJ2GO2 Touch by adding:

- STEMS tracks support - the STEMS support in `Mixxx`_  is added on version 2.6.
- Shifting - now some buttons can do an alternative action if pressed while shifted.
- Mode selection is independent for each deck.
- Better LED feedback.
- More controls.

It is a USB Audio and MIDI Class compliant device and works with Linux, macOS, and Windows.

.. note::

   - If a Mixxx version under 2.6 is used, the :hwlabel:`acapel` :hwlabel:`instru` and :hwlabel:`mode STEMS` controls won't be available.
   - The same is true for tracks that are not STEMS tracks.


.. note::

   - While :hwlabel:`Fade FX` can use any effect available on each channel, effects that dont have their reset point at 0, may not work as expected.
   - Effects that don't reset at 0 are the effects that are at their lowest intensity when the knob is turned all the way to the left.
   - These effects currently are:
       - Filter Echo
       - Mid/Side
       - Balance
       - Filter
       - Loudness
       - Moog Filter
       - Pitch Shift


-  `Product page`_
-  `Forum thread`_


**Soundcard Setup**
--------------------

This controller has a built-in 4 channel output sound card, with a stereo Main output (3.5mm jack) and stereo Headphone output (3.5mm jack).

    - Open **Preferences** > **Sound Hardware**
    - Select the **Output** tab.
    - From the **Main** drop-down menu, select the audio interface, then **Channels 1-2**.
    - From the **Headphones** drop-down menu, select the audio interface, then **Channels 3-4**.
    - Click **Apply** to save the changes.




**Controller Layout**
---------------------
.. image:: ../../_static/controllers/numark_mixtrack_go.png


**Controller Mapping**
----------------------

======  ===============================================================  ===================================================================================================================================
No.     Control                                                          Function
======  ===============================================================  ===================================================================================================================================
**1**   :hwlabel:`browser`                                               A knob for browsing the Library. If pushed, loads a track on the Preview Deck.
**2**   :hwlabel:`load 1` :hwlabel:`load 2`                              Each button loads a track to the Deck on their side.
**2**   :hwlabel:`shift` + :hwlabel:`load 1`                             Switches the :hwlabel:`filter/low` knobs between controlling the Low EQ and the Filter (or any other) Effect.
**2**   :hwlabel:`shift` + :hwlabel:`load 2`                             Toggles the Vinyl mode in the Jogwheel.
**3**   :hwlabel:`bluetooth led`                                         There is currently no functionality for this LED in Mixxx.
**4**   :hwlabel:`main gain`                                             Controls the Main Output Gain
**5**   :hwlabel:`filter/low`                                            Controls either the Filter (or any other) Effect, or the Low EQ. This can be switched with :hwlabel:`shift` + :hwlabel:`load 1`
**6**   :hwlabel:`level`                                                 Controls the channel's Volume.
**7**   :hwlabel:`crossfader`                                            Fades between the Left and the Right channel.
**8**   :hwlabel:`headphone`                                             Sends the channel's audio through the :hwlabel:`Headphone Output`.
**9**   :hwlabel:`cue level`                                             Controls the headphone gain.
**10**  :hwlabel:`jogwheel`                                              If Vinyl Mode is active (:hwlabel:`shift` + :hwlabel:`load 2`), the top surface controls scratching and the side
                                                                         surface controls Pitch Bend. If Vinyl Mode is inactive, both surfaces control pitch bend.
**11**  :hwlabel:`tempo fader`                                           Speed Control. Changes the track's playback speed.
**12**  :hwlabel:`sync`                                                  Toggles Sync Lock.
**13**  :hwlabel:`cue`                                                   Sets the cue point or moves to the main cue point and stops. See options at **Preferences** > **Deck** > **Cue mode**.
**13**  :hwlabel:`shift` + :hwlabel:`cue`                                Moves to the main cue point and resumes playing from there.
**13**  :hwlabel:`shift` + :hwlabel:`2x cue`                             Loads the previous track on the Library and starts playing it from the main cue point. This action is prevented if
                                                                         **Preferences** > **Deck** > **Loading a track, when a deck is playing** is set to Reject.
**14**  :hwlabel:`play/pause`                                            Plays or Pauses the track.
**14**  :hwlabel:`shift` + :hwlabel:`cue`                                Moves to the main cue point and resumes playing from there. Same as :hwlabel:`shift` + :hwlabel:`cue`.
**15**  :hwlabel:`pads`                                                  Performance Pads: These pads can be used to trigger Hotcues, Loops, Samples, Stems, and to apply effects. To
                                                                         change the function of the pads, press the :hwlabel:`mode` button.
**16**  :hwlabel:`mode`                                                  Press this button to change the current function of the Performance Pads.
**17**  :hwlabel:`mode Hotcue`                                           In Hotcue Mode, a :hwlabel:`pad` sets a hotcue in the current position of the track.
                                                                         If that pad already has a hotcue set, the track jumps back to that hotcue and continues playing from there.
                                                                         :hwlabel:`shift` + :hwlabel:`pad` deletes it's corresponding hotcue.
**17**  :hwlabel:`mode Loops`                                            :hwlabel:`pad1` sets a 1 beat loop, :hwlabel:`pad2` sets a 2 beat loop, :hwlabel:`pad3` sets a 4 beat loop and
                                                                         :hwlabel:`pad4` sets an 8 beat loop. :hwlabel:`shift` + :hwlabel:`pad` deletes it's corresponding beat loop.
**17**  :hwlabel:`mode FX`                                               :hwlabel:`pad1` starts an Echo Effect, :hwlabel:`pad2` starts a Flanger Effect, :hwlabel:`pad3` starts a Reverb Effect and
                                                                         :hwlabel:`pad4` starts a 1 beat reverse beatroll.
                                                                         The effects assigned to :hwlabel:`pad1` :hwlabel:`pad2` and :hwlabel:`pad3` can be changed in Mixxx.
**17**  :hwlabel:`mode Sampler`                                          In Sampler Mode, each pad loads the currently selected track in the library into it's sampler. If it is already loaded,
                                                                         it starts playing the sample until the sample ends. :hwlabel:`shift` + :hwlabel:`pad` ejects the track from the corresponding sampler.
**17**  :hwlabel:`mode STEMS`                                            In STEMS Mode, pads mute and unmute the components of the loaded STEMS track: :hwlabel:`pad1` affects the Drums stem part,
                                                                         :hwlabel:`pad2` affects the FX/Bass stem part, :hwlabel:`pad3` affects the Synth stem part and :hwlabel:`pad4` affects the
                                                                         Voice stem part.
**18**  :hwlabel:`acapel`                                                The A cappella button activates an a cappella from the loaded track. This is a STEMS related button.
**19**  :hwlabel:`instru`                                                The Instrumental button activates an instrumental from the loaded track. This is a STEMS related button.
**20**  :hwlabel:`Fade FX`                                               This button toggles the Fade FX feature in Mixxx. When Fade FX is active, moving the :hwlabel:`crossfader` away
                                                                         from the current deck will apply the available Fade FX to that deck. When inactive, the :hwlabel:`crossfader` will work normally.
**21**  :hwlabel:`Main Audio output`                                     Connect this output to an amplifier or speaker system.
**22**  :hwlabel:`USB-C Port`                                            This USB connection serves as source of power and sends/receives audio, control information from a connected
                                                                         computer, tablet, or smartphone.
**23**  :hwlabel:`Headphone Output`                                      Connect headphones to this 1/8” (3.5 mm) jack for monitoring the signal. The headphone volume is controlled using the Cue Gain knob.
======  ===============================================================  ===================================================================================================================================


.. _Mixxx: https://mixxx.org/download/
.. _Midi: https://manual.mixxx.org/2.5/en/glossary#term-MIDI
.. _Product page: https://www.numark.com/new/mixtrack-go/
.. _Forum thread: https://mixxx.discourse.group/t/script-for-numark-mixtrack-go-for-mixxx-2-6-also-works-with-previous-versions/34022/
