Hercules DJ Console RMX
=======================

-  `Manufacturer’s product page <https://support.hercules.com/en/product/djconsolermx-en/>`__

The Hercules DJ Console RMX is a USB controller with a built in sound
card. It is a class compliant USB Audio and HID device. Older versions
of Mixxx that did not support HID required using Hercules’ MIDI driver,
but it is now recommend to not use the Hercules driver on GNU/Linux. If
you have it installed, it is recommended to uninstall the driver and
upgrade to the `latest version of Mixxx <http://mixxx.org/download>`__
if you have not already. On Windows (and Mac OS X?) the driver is still
recommended.

.. versionadded:: 1.11

Audio
-----

The sound card has 4 inputs and 4 outputs (2 stereo in/out). The inputs
are switchable between line-in and phono, so you can connect both CD
players and turntables on the inputs. The inputs require a high input
signal (~10mV+) for turntables if you want to record audio or mix it to
the output. Time-coded vinyls, for Vinyl Control, should work okay with
lower input signal.

MIDI Mappings
-------------

Regular mapping
~~~~~~~~~~~~~~~

Global controls
^^^^^^^^^^^^^^^

+----------------------------------+----------------------------------+
| Control                          | Function                         |
+==================================+==================================+
| Cross-Fader                      | Fades between left and right     |
|                                  | deck                             |
+----------------------------------+----------------------------------+
| Vol. Main                        | Controls output volume of your   |
|                                  | mix                              |
+----------------------------------+----------------------------------+
| Balance                          | Controls balance between left    |
|                                  | and right audio channel of your  |
|                                  | mix                              |
+----------------------------------+----------------------------------+
| Scratch                          | Toggles scratch on and off which |
|                                  | changes the function of the deck |
|                                  | jog wheels                       |
|                                  | **Effect Shift** when held down  |
|                                  | shifts function of each decks    |
|                                  | Bass, Medium, Treble to control  |
|                                  | effect parameters                |
+----------------------------------+----------------------------------+
| Up / Down                        | Moves up and down in the library |
|                                  | track list                       |
|                                  | When held down changes the jog   |
|                                  | wheels behaviour to scroll the   |
|                                  | library list                     |
+----------------------------------+----------------------------------+
| Left / Right                     | Moves up and down between the    |
|                                  | library sections                 |
+----------------------------------+----------------------------------+
| Monitor                          | Fades monitor output             |
|                                  | (headphones) between cue         |
|                                  | selected tracks output and the   |
|                                  | main mix                         |
+----------------------------------+----------------------------------+

Deck / Channel specific controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------+----------------------------------+
| Control                          | Function                         |
+==================================+==================================+
| Play/Pause                       | Starts playing a loaded track if |
|                                  | stopped. If track is currently   |
|                                  | playing it stops the track       |
+----------------------------------+----------------------------------+
| Stop                             | Stops a currently playing track  |
|                                  | and moves to the beginning.      |
+----------------------------------+----------------------------------+
| Cue                              | Sets the cue point if a track is |
|                                  | stopped and not at the current   |
|                                  | cue point                        |
|                                  | Stops track and returns to the   |
|                                  | current cue point if a track is  |
|                                  | playing.                         |
|                                  | Plays preview if a track is      |
|                                  | stopped at the cue point for as  |
|                                  | long as it's held down           |
+----------------------------------+----------------------------------+
| Jog wheel                        | Seeks forwards and backwards in  |
|                                  | a stopped track                  |
|                                  | Temporarily changes the playback |
|                                  | speed for playing tracks         |
|                                  | Scratches both stopped and       |
|                                  | playing tracks when scratch mode |
|                                  | is on                            |
|                                  | Moves up / down in the tracklist |
|                                  | if either Up or Down is held     |
|                                  | down                             |
+----------------------------------+----------------------------------+
| Forward / Backward               | Seeks at high speed in a track   |
+----------------------------------+----------------------------------+
| Load Deck A/B                    | Loads the currently selected     |
|                                  | track in the track list to the   |
|                                  | related deck                     |
+----------------------------------+----------------------------------+
| Cue Select                       | Toggles this decks output to the |
|                                  | monitor (headphones) on and off  |
+----------------------------------+----------------------------------+
| Pitch                            | Adjusts playback speed +/-10%    |
|                                  | (can be adjusted in the          |
|                                  | preferences)                     |
+----------------------------------+----------------------------------+
| Sync                             | Automatically sets pitch so the  |
|                                  | BPM of the other deck is matched |
+----------------------------------+----------------------------------+
| Pitch Reset                      | Resets the pitch to the tracks   |
|                                  | normal playback speed            |
+----------------------------------+----------------------------------+
| Bass                             | Adjusts the volume of a channels |
|                                  | low frequency content (ex. bass  |
|                                  | drum)                            |
|                                  | Adjusts flanger period when      |
|                                  | Effect Shift is held down        |
+----------------------------------+----------------------------------+
| Medium                           | Adjusts the volume of a channels |
|                                  | mid frequency content (ex.       |
|                                  | vocals)                          |
|                                  | Adjusts flanger delay when       |
|                                  | Effect Shift is held down        |
+----------------------------------+----------------------------------+
| Treble                           | Adjusts the volume of a channels |
|                                  | high frequency content (ex.      |
|                                  | hi-hats)                         |
|                                  | Adjusts flanger depth when       |
|                                  | Effect Shift is held down        |
+----------------------------------+----------------------------------+
| Kill (Bass / Medium / Treble)    | Toggles output of a frequency    |
|                                  | band on and off                  |
+----------------------------------+----------------------------------+
| Gain                             | Controls a decks input volume    |
+----------------------------------+----------------------------------+
| Vol. Deck A/B                    | Controls a decks output volume   |
+----------------------------------+----------------------------------+
| Keypad 1                         | Toggles a channels flanger       |
|                                  | effect on and off                |
+----------------------------------+----------------------------------+
| Keypad 4                         | Reveses playback direction when  |
|                                  | held down                        |
+----------------------------------+----------------------------------+

Advanced mapping
~~~~~~~~~~~~~~~~

The advanced mapping works similar to the normal RMX mapping, but also
supports loops and hot cues. This mapping was added to not brake the
previous (Mixxx -1.7.2) behaviour. Controls that differ between the
normal and advanced mappings are described here.

.. _global-controls-1:

Global controls
^^^^^^^^^^^^^^^

+----------------------------------+----------------------------------+
| Control                          | Function                         |
+==================================+==================================+
| Scratch                          | Toggles scratch on and off which |
|                                  | changes the function of the deck |
|                                  | jog wheels                       |
|                                  | **Effect Shift** when held down: |
|                                  | - Shifts function of each decks  |
|                                  | Bass, Medium, Treble to control  |
|                                  | effect parameters                |
|                                  | - Shifts the Keypad (1-6)        |
|                                  | functions to effects. Currently  |
|                                  | flanger and reverse              |
+----------------------------------+----------------------------------+

.. _deck-channel-specific-controls-1:

Deck / Channel specific controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------+----------------------------------+
| Control                          | Function                         |
+==================================+==================================+
| Stop                             | **Deck shift** changes behaviour |
|                                  | of other controls related to     |
|                                  | this deck when held down         |
+----------------------------------+----------------------------------+
| Forward / Backward               | Adjusts position of loop in/out  |
|                                  | and hot cues when a loop / hot   |
|                                  | cue button is held down          |
+----------------------------------+----------------------------------+
| Bass                             | Adjusts the volume of a channels |
|                                  | low frequency content (ex. bass  |
|                                  | drum)                            |
|                                  | Soft takeover when Deck Shift is |
|                                  | held down, lets you move knob in |
|                                  | position before adjusting        |
|                                  | Adjusts flanger period when      |
|                                  | Scratch is held down             |
+----------------------------------+----------------------------------+
| Medium                           | Adjusts the volume of a channels |
|                                  | mid frequency content (ex.       |
|                                  | vocals)                          |
|                                  | Soft takeover when Deck Shift is |
|                                  | held down, lets you move knob in |
|                                  | position before adjusting        |
|                                  | Adjusts flanger delay when       |
|                                  | Scratch is held down             |
+----------------------------------+----------------------------------+
| Treble                           | Adjusts the volume of a channels |
|                                  | high frequency content (ex.      |
|                                  | hi-hats)                         |
|                                  | Soft takeover when Deck Shift is |
|                                  | held down, lets you move knob in |
|                                  | position before adjusting        |
|                                  | Adjusts flanger depth when       |
|                                  | Scratch is held down             |
+----------------------------------+----------------------------------+
| Keypad 1                         | Go to hotcue 1                   |
|                                  | Set hotcue 1 when Deck Shift is  |
|                                  | held down                        |
|                                  | Toggles a channels flanger       |
|                                  | effect on and off when Effect    |
|                                  | Shift is held down               |
+----------------------------------+----------------------------------+
| Keypad 2                         | Go to hotcue 2                   |
|                                  | Set hotcue 2 when Deck Shift is  |
|                                  | held down                        |
+----------------------------------+----------------------------------+
| Keypad 3                         | Go to hotcue 3                   |
|                                  | Set hotcue 3 when Deck Shift is  |
|                                  | held down                        |
+----------------------------------+----------------------------------+
| Keypad 4                         | Hold down to adjust loop in      |
|                                  | position with Forward / Backward |
|                                  | Set loop in when Deck Shift is   |
|                                  | held down                        |
|                                  | Reveses playback direction when  |
|                                  | held down if Effect Shift is     |
|                                  | held down                        |
+----------------------------------+----------------------------------+
| Keypad 5                         | Hold down to adjust loop out     |
|                                  | position with Forward / Backward |
|                                  | Set loop out when Deck Shift is  |
|                                  | held down                        |
+----------------------------------+----------------------------------+
| Keypad 6                         | Re-loop / exit turns looping on  |
|                                  | and off                          |
|                                  | Half loop when Deck Shift is     |
|                                  | held down                        |
+----------------------------------+----------------------------------+
