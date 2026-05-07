# MIDI Codes

Here we document what MIDI packets you can expect from the [Numark Total
Control](Numark%20Total%20Control) surface, as well as what packets you
can send to do various things.

Messages sent by the Numark Total Control will be sent over MIDI channel
1. Messages sent to the Numark Total Control may be sent over any MIDI
channel. (In testing, it appears to react to all MIDI channels equally.)

The Numark Total Control does not have labeled controls. That is to say,
all labels are on removable/swapable face cards. In the tables below, we
refer to an individual control like "CxR," where C is the number of
columns from the left and R is the number of controls from the top of
the column.

![layout\_coordinates.jpg](_static/controllers/numark_totalcontrol/layout_coordinates.jpg)

## Buttons, Knobs, and Sliders

Numark Total Control will send either 0x90 (Note On) messages or 0xB0
(CC) messages for every control on the control surface.

Some CC controls are absolute and others are relative. Absolute controls
will report an absolute position from 0 to 127. (Unsigned 7-bit.)
Relative controls will report a change in position from -63 to 63.
(Signed 7-bit. Signed values are calculated using [Two's
Compliment](http://en.wikipedia.org/wiki/Two%27s_complement).)

Button presses will result in two events, one for press and one for
release. Oddly, although Numark Total Control sends a Note On message
for button presses, it does not send a Note Off message for button
release. Instead, button presses are Note On messages with a velocity of
127, and button releases are Note On messages with a velocity of 0.

### Leftmost Column

| Control     | Type | Decimal ID | Relative or Absolute | Comment                       |
| ----------- | ---- | ---------- | -------------------- | ----------------------------- |
| 1X1 (Press) | Note | 48         | N/A                  | N/A                           |
| 1X2 (Press) | Note | 56         | N/A                  | N/A                           |
| 1X3 (Press) | Note | 64         | N/A                  | N/A                           |
| 1X4 (Slide) | CC   | 11         | Absolute             | Vertical slider. (Left pitch) |
| 1X5 (Press) | Note | 51         | N/A                  | N/A                           |

### Second Column From The Left

| Control     | Type | Decimal ID | Relative or Absolute | Comment         |
| ----------- | ---- | ---------- | -------------------- | --------------- |
| 2X1 (Turn)  | CC   | 0          | Relative             | N/A             |
| 2X2 (Press) | Note | 49         | N/A                  | N/A             |
| 2X3 (Turn)  | CC   | 2          | Relative             | N/A             |
| 2X4 (Press) | Note | 57         | N/A                  | N/A             |
| 2X5 (Press) | Note | 65         | N/A                  | N/A             |
| 2X6 (Press) | Note | 73         | N/A                  | N/A             |
| 2X7 (Turn)  | CC   | 25         | Relative             | Left jog wheel. |
| 2X8 (Press) | Note | 59         | N/A                  | N/A             |

### Third Column From The Left

| Control     | Type | Decimal ID | Relative or Absolute | Comment |
| ----------- | ---- | ---------- | -------------------- | ------- |
| 3X1 (Turn)  | CC   | 1          | Relative             | N/A     |
| 3X2 (Press) | Note | 50         | N/A                  | N/A     |
| 3X3 (Turn)  | CC   | 3          | Relative             | N/A     |
| 3X4 (Press) | Note | 58         | N/A                  | N/A     |
| 3X5 (Press) | Note | 66         | N/A                  | N/A     |
| 3X6 (Press) | Note | 74         | N/A                  | N/A     |
| 3X7 (Press) | Note | 67         | N/A                  | N/A     |

### Forth Column From The Left

| Control     | Type | Decimal ID | Relative or Absolute | Comment                        |
| ----------- | ---- | ---------- | -------------------- | ------------------------------ |
| 4X1 (Turn)  | CC   | 13         | Absolute             | N/A                            |
| 4X2 (Turn)  | CC   | 16         | Absolute             | N/A                            |
| 4X2 (Press) | Note | 80         | N/A                  | N/A                            |
| 4X3 (Turn)  | CC   | 18         | Absolute             | N/A                            |
| 4X3 (Press) | Note | 85         | N/A                  | N/A                            |
| 4X4 (Turn)  | CC   | 20         | Absolute             | N/A                            |
| 4X4 (Press) | Note | 83         | N/A                  | N/A                            |
| 4X5 (Press) | Note | 75         | N/A                  | N/A                            |
| 4X6 (Slide) | CC   | 8          | Absolute             | Vertical slider. (Left volume) |

### Center Column

| Control     | Type | Decimal ID | Relative or Absolute | Comment                        |
| ----------- | ---- | ---------- | -------------------- | ------------------------------ |
| 5X1 (Turn)  | CC   | 23         | Absolute             | N/A                            |
| 5X2 (Turn)  | CC   | 22         | Absolute             | N/A                            |
| 5X3 (Turn)  | CC   | 15         | Absolute             | N/A                            |
| 5X4 (Turn)  | CC   | 26         | Relative             | N/A                            |
| 5X4 (Press) | Note | 79         | N/A                  | N/A                            |
| 5X5 (Press) | Note | 72         | N/A                  | N/A                            |
| 5X6 (Slide) | CC   | 10         | Absolute             | Horizontal slider. (Crossfade) |

### Forth Column From The Right

| Control     | Type | Decimal ID | Relative or Absolute | Comment                         |
| ----------- | ---- | ---------- | -------------------- | ------------------------------- |
| 6X1 (Turn)  | CC   | 14         | Absolute             | N/A                             |
| 6X2 (Turn)  | CC   | 17         | Absolute             | N/A                             |
| 6X2 (Press) | Note | 82         | N/A                  | N/A                             |
| 6X3 (Turn)  | CC   | 19         | Absolute             | N/A                             |
| 6X3 (Press) | Note | 81         | N/A                  | N/A                             |
| 6X4 (Turn)  | CC   | 21         | Absolute             | N/A                             |
| 6X4 (Press) | Note | 84         | N/A                  | N/A                             |
| 6X5 (Press) | Note | 52         | N/A                  | N/A                             |
| 6X6 (Slide) | CC   | 9          | Absolute             | Vertical slider. (Right volume) |

### Third Column From The Right

| Control     | Type | Decimal ID | Relative or Absolute | Comment |
| ----------- | ---- | ---------- | -------------------- | ------- |
| 7X1 (Turn)  | CC   | 4          | Relative             | N/A     |
| 7X2 (Press) | Note | 53         | N/A                  | N/A     |
| 7X3 (Turn)  | CC   | 6          | Relative             | N/A     |
| 7X4 (Press) | Note | 61         | N/A                  | N/A     |
| 7X5 (Press) | Note | 69         | N/A                  | N/A     |
| 7X6 (Press) | Note | 77         | N/A                  | N/A     |
| 7X7 (Press) | Note | 60         | N/A                  | N/A     |

### Second Column From The Right

| Control     | Type | Decimal ID | Relative or Absolute | Comment          |
| ----------- | ---- | ---------- | -------------------- | ---------------- |
| 8X1 (Turn)  | CC   | 5          | Relative             | N/A              |
| 8X2 (Press) | Note | 54         | N/A                  | N/A              |
| 8X3 (Turn)  | CC   | 7          | Relative             | N/A              |
| 8X4 (Press) | Note | 62         | N/A                  | N/A              |
| 8X5 (Press) | Note | 70         | N/A                  | N/A              |
| 8X6 (Press) | Note | 78         | N/A                  | N/A              |
| 8X7 (Turn)  | CC   | 24         | Relative             | Right jog wheel. |
| 8X8 (Press) | Note | 68         | N/A                  | N/A              |

### Rightmost Column

| Control     | Type | Decimal ID | Relative or Absolute | Comment                        |
| ----------- | ---- | ---------- | -------------------- | ------------------------------ |
| 9X1 (Press) | Note | 55         | N/A                  | N/A                            |
| 9X2 (Press) | Note | 63         | N/A                  | N/A                            |
| 9X3 (Press) | Note | 71         | N/A                  | N/A                            |
| 9X4 (Slide) | CC   | 12         | Absolute             | Vertical slider. (Right pitch) |
| 9X5 (Press) | Note | 76         | N/A                  | N/A                            |

## LED Lights (Status Indicators)

Most buttons, knobs, and sliders on the Numark Total Control are
designed to light up in one way or another.

LEDs are lit by sending a 0x90 (Note On) message with a non-zero
velocity to the appropriate note number. LEDs are turned off by either
sending a 0x80 (Note Off) message (any velocity) *or* by sending a 0x90
(Note On) message with a zero velocity.

Unfortunately, the Note Number mapping for LEDs is completely different
from the Note Numbers documented above, so we document the LED Note
Numbers in another set of tables below.

While most testing was done on MIDI channel one, the Numark Total
Control seems to respond to LED commands on any channel.

### Leftmost Column

| Control     | Decimal ID | Comment                                       |
| ----------- | ---------- | --------------------------------------------- |
| 1X1 (Press) | 53         | N/A                                           |
| 1X2 (Press) | 54         | N/A                                           |
| 1X3 (Press) | 55         | N/A                                           |
| 1X4 (Slide) | 52         | Left pitch slider, center position indicator. |
| 1X5 (Press) | 60         | N/A                                           |

### Second Column From The Left

| Control     | Decimal ID | Comment |
| ----------- | ---------- | ------- |
| 2X2 (Press) | 51         | N/A     |
| 2X4 (Press) | 50         | N/A     |
| 2X5 (Press) | 56         | N/A     |
| 2X6 (Press) | 58         | N/A     |
| 2X8 (Press) | 61         | N/A     |

### Third Column From The Left

| Control     | Decimal ID | Comment |
| ----------- | ---------- | ------- |
| 3X2 (Press) | 49         | N/A     |
| 3X4 (Press) | 48         | N/A     |
| 3X5 (Press) | 57         | N/A     |
| 3X6 (Press) | 59         | N/A     |
| 3X7 (Press) | 62         | N/A     |

### Forth Column From The Left

| Control     | Decimal ID | Comment                             |
| ----------- | ---------- | ----------------------------------- |
| 4X2 (Turn)  | 80         | EQ knob, center position indicator. |
| 4X3 (Turn)  | 81         | EQ knob, center position indicator. |
| 4X4 (Turn)  | 82         | EQ knob, center position indicator. |
| 4X5 (Press) | 63         | N/A                                 |

### Center Column

| Control     | Decimal ID | Comment |
| ----------- | ---------- | ------- |
| 5X5 (Press) | 86         | N/A     |

### Forth Column From The Right

| Control     | Decimal ID | Comment                             |
| ----------- | ---------- | ----------------------------------- |
| 6X2 (Turn)  | 83         | EQ knob, center position indicator. |
| 6X3 (Turn)  | 84         | EQ knob, center position indicator. |
| 6X4 (Turn)  | 85         | EQ knob, center position indicator. |
| 6X5 (Press) | 79         | N/A                                 |

### Third Column From The Right

| Control     | Decimal ID | Comment |
| ----------- | ---------- | ------- |
| 7X2 (Press) | 68         | N/A     |
| 7X4 (Press) | 70         | N/A     |
| 7X5 (Press) | 72         | N/A     |
| 7X6 (Press) | 74         | N/A     |
| 7X7 (Press) | 76         | N/A     |

### Second Column From The Right

| Control     | Decimal ID | Comment |
| ----------- | ---------- | ------- |
| 8X2 (Press) | 69         | N/A     |
| 8X4 (Press) | 71         | N/A     |
| 8X5 (Press) | 73         | N/A     |
| 8X6 (Press) | 75         | N/A     |
| 8X8 (Press) | 77         | N/A     |

### Rightmost Column

| Control     | Decimal ID | Comment                                        |
| ----------- | ---------- | ---------------------------------------------- |
| 9X1 (Press) | 64         | N/A                                            |
| 9X2 (Press) | 65         | N/A                                            |
| 9X3 (Press) | 66         | N/A                                            |
| 9X4 (Slide) | 67         | Right pitch slider, center position indicator. |
| 9X5 (Press) | 78         | N/A                                            |

## Legal

This is based on a work which is copyright (C) Alex Markley, 2008.

This work is licensed under the Creative Commons Attribution-Share Alike
3.0 United States License. To view a copy of this license, visit
<http://creativecommons.org/licenses/by-sa/3.0/us/> or send a letter to
Creative Commons, 171 Second Street, Suite 300, San Francisco,
California, 94105, USA.

Thanks to Numark for producing such a great standards-compliant product.

Please send corrections and/or comments to Alex Markley at
<http://malexmedia.net/contact/malex>
