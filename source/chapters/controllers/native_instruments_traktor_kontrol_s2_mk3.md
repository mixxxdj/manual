# Native Instruments Traktor Kontrol S2 MK3

[[/media/hardware/nativeinstruments/traktorkontrols2mk3.png|]]

  - [Manufacturer's product
    page](https://www.native-instruments.com/en/products/traktor/dj-controllers/traktor-kontrol-s2/)
  - [DJTechTools
    Review](https://djtechtools.com/2018/09/06/traktor-kontrol-s2-mk3-simplified-and-mobile-friendly/)
  - [Digital DJ Tips
    Review](https://www.digitaldjtips.com/reviews/traktor-kontrol-s2-mk3/)
  - [DJWORX
    Review](https://djworx.com/the-small-and-perfectly-formed-traktor-kontrol-s2-mk3/)

The Kontrol S2 MK3 is a two-channel controller with an integrated sound
card. It has two integrated stereo outputs (line and 1/8" / 3.5 mm TRS),
headphone outputs (1/8" / 3.5 mm TRS) and microphone inputs (1/4" / 6.3
mm TRS). The MK3 uses the standard HID protocol to send and receive
signals from a computer, so it can work with Mixxx. The Kontrol S2 MK3
can run from USB bus power, but using the separate power supply
increases the brightness of the LEDs, which is helpful for using it in
daylight, and increases the volume of the headphone output.

### Mixxx Sound Hardware Preferences

  - Master output: channels 1-2
  - Headphone output: channels 3-4

### Mixxx mapping

**HINT:** Since this controller is a USB-HID device, you might need to set the corresponding [udev rules](https://github.com/mixxxdj/mixxx/wiki/Troubleshooting#user-content-hid-and-usb-bulk-controllers-on-gnulinux) in Linux.

Have a look at the corresponding thread in the forums for questions and
feedback:
<https://www.mixxx.org/forums/viewtopic.php?uid=14478&f=7&t=12999&start=0>

[[/media/hardware/nativeinstruments/traktorkontrols2mk3-schema.png|]]

| Element                  | Primary function                                                                                                                                            | Secondary function (+ SHIFT)                                        |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| (1) REV Button           | Reverse play while held                                                                                                                                     | Reverse play + slip mode while held                                 |
| (2) FLX Button           | Enable and disable slip mode                                                                                                                                |                                                                     |
| (3) Browse knob (turn)   | Scroll vertically in library                                                                                                                                | Scroll horizontally in library                                      |
| (3) Browse knob (press)  | Load selected track into deck                                                                                                                               | Eject current track                                                 |
| (4) Preparation button   | Add selected track to AutoDJ queue (bottom)                                                                                                                 | Add selected track to AutoDJ queue (top)                            |
| (5) List view button     | Toggles maximizing the library                                                                                                                              |                                                                     |
| (6) Sync button          | Syncs the BPM and phase (depending on quantize). Press longer to activate master sync on that deck.                                                         | Syncs the phase to that of the other track                          |
| (7) Keylock button       | Enable keylock for the deck                                                                                                                                 |                                                                     |
| (8) Loop knob (turn)     | Halve or double loop size                                                                                                                                   |                                                                     |
| (8) Loop knob (press)    | Set a loop of the defined number of beats and enables the loop                                                                                              | Toggles the current loop on or off                                  |
| (9) Samples button       | Active sampler mode (for the number buttons)                                                                                                                |                                                                     |
| (10) Hotcues button      | Activate hotcue mode (for the number buttons)                                                                                                               |                                                                     |
| (11) Move knob (turn)    | Beatjump backwards/forwards                                                                                                                                 | Halve or double beatjump size                                       |
| (11) Move knob (press)   | Activates a rolling loop of the defined number of beats. Once disabled, playback will resume where the track would have been if it had not entered the loop | Activate current loop, jump to its loop in point, and stop playback |
| (12) Jog wheels          | Control scratching when touched from the top *(Missing: temporarily bend the pitch when touched from the side)*                                             |                                                                     |
| (13) Grid button         | Adjust beatgrid so closest beat is aligned with the current play position                                                                                   | Adjust beatgrid to match another playing deck                       |
| (14) Shift button        | Activates secondary functions when pressed                                                                                                                  |                                                                     |
| (15) CUE button          | CUE default                                                                                                                                                 | If the CUE point is set, jump to it and stops                       |
| (16) Play button         | Toggles playing                                                                                                                                             | Seeks a player to the start and then stops it                       |
| (17) Number buttons      | Function depends on current mode                                                                                                                            |                                                                     |
| Hotcue mode              | If hotcue is set, seeks the player to hotcue position. Otherwise set hotcue at current position                                                             | Clear the hotcue                                                    |
| Samples mode             | If track is loaded into corresponding slot, go to CUE point and play                                                                                        | If track is playing, CUE default behaviour. Otherwise eject track   |
| (18) Tempo fader         | Speed control                                                                                                                                               |                                                                     |
| (19) Quantize button     | Toggles quantization for both decks                                                                                                                         |                                                                     |
| (20) Gain knob           | Adjusts the gain for the master output                                                                                                                      |                                                                     |
| (21) Microphone button   | Toggles microphone talkover, long press for permanent activation                                                                                            |                                                                     |
| (22) Pre-Gain knob       | Adjusts the pre-fader gain of the deck                                                                                                                      |                                                                     |
| (23) HI knob             | High frequency filter                                                                                                                                       |                                                                     |
| (24) MID knob            | Middle frequency filter                                                                                                                                     |                                                                     |
| (25) LOW knob            | Low frequency filter                                                                                                                                        |                                                                     |
| (26) Effect Superknob    | Quick effect superknob for the corresponding deck                                                                                                           |                                                                     |
| (27) Sample knob         | Adjusts the pregain for all the sample decks combined                                                                                                       |                                                                     |
| (28) Headphone mix knob  | Adjusts the cue/main mix in the headphone output                                                                                                            |                                                                     |
| (29) Headphone gain knob | Adjusts the headphone output gain                                                                                                                           |                                                                     |
| (30) Effect buttons      | Enable or disable effect units for both decks                                                                                                               |                                                                     |
| (31) Headphone buttons   | Toggles headphone cueing                                                                                                                                    |                                                                     |
| (32) Volume fader        | Adjusts the channel volume fader for the corresponding deck                                                                                                 |                                                                     |
| (33) VuMeter LEDs        | Show the current instantaneous deck volume                                                                                                                  |                                                                     |
| (34) Crossfader          | Adjusts the crossfader between both decks                                                                                                                   |                                                                     |

### Technical details

**USB HID descriptors**

    $> usbhid-dump -d17cc:1710 | grep -v : | xxd -r -p | hidrd-convert -o spec
    
     Usage Page (FF01h),          ; FF01h, vendor-defined
     Usage (00h),
     Collection (Application),
         Usage (01h),
         Collection (Logical),
            Report ID (1),
            Usage (02h),
            Logical Minimum (0),
            Logical Maximum (1),
            Report Size (1),
            Report Count (64),
            Input (Variable),
            Usage (03h),
            Logical Minimum (0),
            Logical Maximum (15),
            Report Size (4),
            Report Count (6),
            Input (Variable),
            Usage (31h),
            Logical Minimum (0),
            Logical Maximum (65535),
            Report Size (16),
            Report Count (4),
            Input (Variable),
        End Collection,
        Usage (01h),
        Collection (Logical),
            Report ID (2),
            Usage (05h),
            Logical Minimum (0),
            Logical Maximum (4095),
            Report Size (16),
            Report Count (5),
            Input (Variable),
            Usage (04h),
            Logical Minimum (0),
            Logical Maximum (4095),
            Report Size (16),
            Report Count (14),
            Input (Variable),
        End Collection,
        Usage (80h),
        Collection (Logical),
            Report ID (128),
            Usage (81h),
            Logical Minimum (0),
            Logical Maximum (127),
            Report Size (8),
            Report Count (61),
            Output (Variable),
        End Collection,
    End Collection

There are two types of incoming packets. Packets with reportID 0x1
represents the state of the buttons and the jog wheels, while reportID
0x2 is about the scalers. Here are the details for reportID 0x1:

``` 
    Offset 0x01, Bitmasks:
    - 0x01 Rev Left - 0x02 FLX Left - 0x04 Prepation Left - 0x08 Browse View Left 
    - 0x10 Grid Left - 0x20 Shift Left - 0x40 Hotcues Left - 0x80 Samples Left
    Offset 0x02, Bitmasks:
    - 0x01 Sync Left - 0x02 Keylock Left - 0x04 Cue Left - 0x08 Play Left
    - 0x10 Hotcue1 Left - 0x20 Hotcue2 Left - 0x40 Hotcue3 Left - 0x80 Hotcue4 Left
    Offset 0x03, Bitmasks:
    - 0x01 Hotcue5 Left - 0x02 Hotcue6 Left - 0x04 Hotcue7 Left - 0x08 Hotcue8 Left
    - 0x10 FX Select1 - 0x20 FX Select2 - 0x40 FX Select3 - 0x80 FX Select4
    Offset 0x04, Bitmasks:
    - 0x01 Phones Left - 0x02 Phones Right - 0x04 Rev Right - 0x08 FLX Right
    - 0x10 Prepation Right - 0x20 Browse View Right - 0x40 Grid Right - 0x80 Shift Right
    Offset 0x05, Bitmasks:
    - 0x01 Hotcues Right - 0x02 Samples Right - 0x04 Sync Right - 0x08 Keylock Right
    - 0x10 Cue Right - 0x20 Play Right - 0x40 Hotcue1 Right - 0x80 Hotcue2 Right
    Offset 0x06, Bitmasks:
    - 0x01 Hotcue3 Right - 0x02 Hotcue4 Right - 0x04 Hotcue5 Right - 0x08 Hotcue6 Right
    - 0x10 Hotcue7 Right - 0x20 Hotcue8 Right - 0x40 GNT - 0x80 MIC
    Offset 0x07, Bitmasks:
    - 0x01 Browse Left Click - 0x02 Move Left Click - 0x04 Loop Left Click - 0x08 Browse Right Click
    - 0x10 Move Right Click - 0x20 Loop Right Click - 0x40 ??? - 0x80 ???
    Offset 0x08, Bitmasks:
    - 0x01 Browse Left Touch - 0x02 Move Left Touch - 0x04 Loop Left Touch - 0x08 Browse Right Touch
    - 0x10 Move Right Touch - 0x20 Loop Right Touch - 0x40 Jog Wheel Left Touch - 0x80 Jog Wheel Right Touch
    Offset 0x09, Bitmasks:
    - Lowest nibble: Browse Left
    - Highest nibble: Move Left
    Offset 0x0A, Bitmasks:
    - Lowest nibble: Loop Left
    - Highest nibble: Browse Right
    Offset 0x0B, Bitmasks:
    - Lowest nibble: Move Right
    - Highest nibble: Loop Right
    Offset 0x0C - 0x0F: Jog Wheel Left
    Offset 0x10 - 0x13: Jog Wheel Right
```

Outgoing packets with reportID 0x80 control only the LEDs on the
controller. No light is 0x00 and full light is 0x7E (except for the
multi-color hotcue buttons).

``` javascript
var data_string = "00 00 00 \n" + // Rev Left, FLX Left, Preparation Left
               "00 00 00 00 \n" + // Browse View Left, Grid Left, Shift Left, Hotcues Left
               "00 00 00 00 \n" + // Samples Left, Sync Left, Keylock Left, Cue Left
               "00 00 00 00 \n" + // Play Left, Hotcue1 Left, Hotcue2 Left, Hotcue3 Left
               "00 00 00 00 \n" + // Hotcue4 Left, Hotcue5 Left, Hotcue6 Left, Hotcue7 Left
               "00 00 00 00 \n" + // Hotcue8 Left, Sample Mixer LED, FX Select1, FX Select2
               "00 00 00 00 \n" + // FX Select3, FX Select4, Phones Left, Phones Right
               "00 00 00 00 \n" + // Level Channel A -18, -12, -6, 0
               "00 00 00 00 \n" + // Level Channel A 6, Level Channel B -18, -12
               "00 00 00 00 \n" + // Level Channel B -6, 0, 6, Clip
               "00 00 00 00 \n" + // Rev Right, FLX Right, Preparation Right, Browse View Right
               "00 00 00 00 \n" + // Grid Right, Shift Right, Hotcues Right, Samples Right
               "00 00 00 00 \n" + // Sync Right, Keylock Right, Cue Right, Play Right
               "00 00 00 00 \n" + // Hotcue1 Right, Hotcue2 Right, Hotcue3 Right, Hotcue4 Right
               "00 00 00 00 \n" + // Hotcue5 Right, Hotcue6 Right, Hotcue7 Right, Hotcue8 Right
               "00 00"; // GNT, MIC
this.rawOutput(data_string);
```
