(native-instruments-traktor-kontrol-s2-mk3)=

# Native Instruments Traktor Kontrol S2 MK3

The Kontrol S2 MK3 is a two-channel controller with an integrated sound card. It has two integrated stereo outputs (line and 1/8" / 3.5 mm TRS), headphone outputs (1/8" / 3.5 mm TRS) and microphone
inputs (1/4" / 6.3 mm TRS). The MK3 uses the standard HID protocol to send and receive signals from a computer, so it can work with Mixxx. The Kontrol S2 MK3 can run from USB bus power,
and using a separate power supply has no impact on the output level or LED brightness ([as opposed to the MK2](https://support.native-instruments.com/hc/en-us/articles/360001108518)).

- [Manufacturer’s product page](https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s2/)
- [Mapping forum thread](https://mixxx.discourse.group/t/native-instruments-traktor-kontrol-s2-mk3/18147)

:::{versionadded} 2.2.4
:::
:::{versionchanged} 2.3
   Unbind Main knob from Mixxx's Main Gain, because it controls the hardware volume.
:::
## Mixxx Sound Hardware Preferences

-  Main output: channels 1-2
-  Headphone output: channels 3-4

## Mixxx mapping

```{figure} ../../_static/controllers/native_instruments_traktor_kontrol_s2_mk3.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Native Instruments Traktor Kontrol S2 MK3 (schematic view)
   :figclass: pretty-figures

   Native Instruments Traktor Kontrol S2 MK3 (schematic view)

```
```{list-table}
:header-rows: 1

* - Element
  - Primary function
  - Secondary function (+ SHIFT)
* - **1**. REV Button
  - Reverse play while held
  - Reverse play + slip mode while held
* - **2**. FLX Button
  - Enable and disable slip mode
  -
* - **3**. Browse knob **turn**
  - Scroll vertically in library
  - Scroll horizontally in library
* - **3**. Browse knob **press**
  - Load selected track into deck
  - Eject current track
* - **4**. Preparation button
  - Add selected track to AutoDJ queue (bottom)
  - Add selected track to AutoDJ queue (top)
* - **5**. List view button
  - Toggles maximizing the library
  -
* - **6**. Sync button
  - Syncs the BPM and phase (depending on quantize). Press longer to activate sync lock on that deck.
  - Syncs the phase to that of the other track
* - **7**. Keylock button
  - Enable keylock for the deck
  -
* - **8**. Loop knob **turn**
  - Halve or double loop size
  -
* - **8**. Loop knob **press**
  - Set a loop of the defined number of beats and enables the loop
  - Toggles the current loop on or off
* - **9**. Samples button
  - Active sampler mode (for the number buttons)
  -
* - **10**. Hotcues button
  - Activate hotcue mode (for the number buttons)
  -
* - **11**. Move knob **turn**
  - Beatjump backwards/forwards
  - Halve or double beatjump size
* - **11**. Move knob **press**
  - Activates a rolling loop of the defined number of beats. Once disabled, playback will resume where the track would have been if it had not entered the loop
  - Activate current loop, jump to its loop in point, and stop playback
* - **12**. Jog wheels
  - Control scratching when touched from the top

    *(Missing: temporarily bend the pitch when touched from the side)*
  -
* - **13**. Grid button
  - Adjust beatgrid so closest beat is aligned with the current play position
  - Adjust beatgrid to match another playing deck
* - **14**. Shift button
  - Activates secondary functions when pressed
  -
* - **15**. CUE button
  - CUE default
  - If the CUE point is set, jump to it and stops
* - **16**. Play button
  - Toggles playing
  - Seeks a player to the start and then stops it
* - **17**. Number buttons
  - Function depends on current mode
  -
* - Hotcue mode
  - If hotcue is set, seeks the player to hotcue position. Otherwise set hotcue at current position
  - Clear the hotcue
* - Samples mode
  - ```{line-block}
    Load selected track into corresponding slot.
    If track is loaded into corresponding slot, go to CUE point and play
    ```
  - If track is playing, CUE default behaviour.

    Otherwise eject track
* - **18**. Tempo fader
  - Speed control
  -
* - **19**. Quantize button
  - Toggles quantization for both decks
  -
* - **20**. Gain knob
  - *Unmapped* (adjusts the hardware gain)
  -
* - **21**. Microphone button
  - Toggles microphone talkover, long press for permanent activation
  -
* - **22**. Pre-Gain knob
  - Adjusts the pre-fader gain of the deck
  -
* - **23**. HI knob
  - High frequency filter
  -
* - **24**. MID knob
  - Middle frequency filter
  -
* - **25**. LOW knob
  - Low frequency filter
  -
* - **26**. Effect knob
  - Quick effect knob for the corresponding deck
  -
* - **27**. Sample knob
  - Adjusts the pregain for all the sample decks combined
  -
* - **28**. Headphone mix knob
  - Adjusts the cue/main mix in the headphone output
  -
* - **29**. Headphone gain knob
  - Adjusts the headphone output gain
  -
* - **30**. Effect buttons
  - ```{line-block}
    Load preset from the Quick Effect presets list on both decks. 8 first presets from the list can be selected.
    Press the button once to get the first preset, press twice for the second preset.
    Press once (Press twice):
    1 (5)  2 (6)
    3 (7)  4 (8)
    ```
  - Load preset on selected deck
* - **31**. Headphone buttons
  - Toggles headphone cueing
  -
* - **32**. Volume fader
  - Adjusts the channel volume fader for the corresponding deck
  -
* - **33**. VuMeter LEDs
  - Show the current instantaneous deck volume
  -
* - **34**. Crossfader
  - Adjusts the crossfader between both decks
  -
```
