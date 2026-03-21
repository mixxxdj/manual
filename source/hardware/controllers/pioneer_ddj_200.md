![Pioneer DDJ-200](https://www.pioneerdj.com/-/media/pioneerdj/images/products/controller/ddj-200/black/ddj-200-top.png?h=630&w=1200&hash=D4763E7B4F70241AE86F6072AB6649DB24B89F8E)

  - [Manufacturer's Product Page](https://www.pioneerdj.com/en-gb/product/controller/ddj-200/black/overview/)
  - [Manufacturer's User Manual](http://docs.pioneerdj.com/Manuals/DDJ_200_DRI1596B_manual/)
  - [Manufacturer's Firmware Update](https://www.pioneerdj.com/en/support/software/controller/ddj-200/)
  - [Midi Mappings](https://www.pioneerdj.com/-/media/pioneerdj/software-info/controller/ddj-200/ddj-200_midi_message_list_e2.pdf)
  - [Hardware Diagram](https://www.pioneerdj.com/-/media/pioneerdj/software-info/controller/ddj-200/ddj-200_hardwarediagram_rekordboxdj_e2.pdf)
  - [Mapping Git Fork](https://github.com/dan-giddins/mixxx/tree/ddj-200-support)
  - [Simple Mapping Git Repository](https://github.com/dan-giddins/mixxx-ddj-200-mapping)

The Pioneer DDJ-200 is a simple 2 deck USB DJ controller designed for WeDJ, djay, edjing Mix and rekordboxDJ.

## Controller Mapping

This mapping for the DDJ-200 is in the process of being [added to Mixxx](https://github.com/mixxxdj/mixxx/pull/2377).

A schematic drawing with the control numbers that are used here can be
found on the specified page in the User Manual in the Links section.

### Deck section (p. 8)

| No. | Control                           | Function                                                                         |
| --- | --------------------------------- | -------------------------------------------------------------------------------- |
| 1   | \[JOG WHEEL\] (top)               | Scratches the track                                                              |
| 1   | \[JOG WHEEL\] (outer)             | Pitch bend                                                                       |
| 1   | \[SHIFT\] + \[JOG WHEEL\] (top)   | Move Play position with higher speed in the direction the Wheel is turned        |
| 2   | \[SHIFT\] button                  | Change the function of another control                                           |
| 3   | \[PAD 1 - 8\]                     | Set (if empty) or play Hot cue point / loop\*1                                   |
| 3   | \[SHIFT\] + \[PAD 1 - 8\]         | Unset/Delete hot cue point / loop                                                |
| 4   | \[CUE\] button                    | Depends on the [cue mode](https://mixxx.org/manual/latest/en/chapters/user_interface.html#using-cue-modes) set in the Mixxx preferences              |
| 4   | \[SHIFT\] + \[CUE\] button        | Return to beginning of the cue point or track if not set                         |
| 5   | \[PLAY/PAUSE\] button             | Plays/pauses a track in the respective Deck                                      |
| 6   | \[BEAT SYNC\] button              | Match tempo and phase of other deck. Long press to enable Master Sync.           |
| 7   | \[TEMPO\] slider                  | Adjust the track playing speed (can be adjusted via \[SHIFT\] + \[BEAT SYNC\]    |


### Mixer section (p. 10)

| No. | Control                                       | Function                                                                  |
|---- | --------------------------------- | ------------------------------------------------------------------------- |
| 1   | \[MASTER CUE\] button             | Activates Master output on Headphones                                     |
| 2   | \[HI\], \[MID\], \[LOW\] knobs    | Adjust the high/mid/low-frequency regions of the song.                    |
| 3   | \[CFX\] knobs                     | Turns on the selected effects                                             |
| 4   | \[HEADPHONE CUE\] button          | Toggle PFL for the Channel                                                |
| 5   | Channel faders                    | Adjust the output level for each channel.                                 |
| 6   | Transition FX Button              | Turns on Mixxx AutoDJ                                                     |
| 7   | Cross fader                       | Fades between left and right deck.                                        |

### Known Issues
- Track does not align to the other track if jog wheel is used to move the play position.
