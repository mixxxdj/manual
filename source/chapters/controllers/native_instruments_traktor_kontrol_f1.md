# Native Instruments Traktor Kontrol F1

[[/media/native-instruments-traktor-kontrol-f1.jpg|]]

  - [Manufacturer's product
    page](https://www.native-instruments.com/de/products/traktor/dj-controllers/traktor-kontrol-f1/)

The Traktor Kontrol F1 is a small versatile controller that is intended
to be used for remix decks but can easily be repurposed for other uses
such as hotcues.

## HID Specification

### Input

Report ID: 0x1

#### Buttons

The buttons are located at offset 1 and have the following bit order:

  - Grid buttons 8 - 1
  - Grid buttons 16 - 9
  - Shift
  - Reverse
  - Size
  - Type
  - Knob press
  - Browse
  - Bottom buttons 1 - 4
  - Sync
  - Quant
  - Capture

The scroll value of the infinite knob is located at offset 5 and spans a
whole byte.

#### Knobs & Faders

They are each of type \`short\` and thus the offset increases by 2 with
each, starting at 6

  - Knobs 1-4
  - Faders 1-4

### Output

Report ID: 0x80

All bytes represent Brightness and can be set granularly from 00 to 7F.

  - Left display segment - 7 Bytes
  - Dot between the display segment - 1 Byte
  - Right display segment - 7 Bytes
  - Browse
  - Size
  - Type
  - Reverse
  - Shift
  - Capture
  - Quant
  - Sync

#### Grid

Each pad in the grid has three bytes, controlling Red, Green and Blue
respectively, in order from 1 to 16, spanning bytes 25 to 72.

#### Bottom(Play) Buttons

Each of these is orange, but has a left and a right LED, so you can set
a brightness gradient. For each button there are two bytes, for the left
and right LED respectively, and they are in order from 4 to 1, spanning
bytes 73 to 80.
