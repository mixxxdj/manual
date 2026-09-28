.. include:: /shortcuts.rstext

.. _midi-crash-course:

MIDI Crash Course
*****************

MIDI (Musical Instrument Digital Interface) is a standard for electronic musical
devices to communicate.
This page is a brief introduction to MIDI that should explain what you need to
know to :ref:`map MIDI controllers to Mixxx <advanced-controller>`.
Refer to :ref:`reverse-engineering` for tips to intercept MIDI data from a
device.

MIDI is a widely used standard that a lot of hardware and software supports.
It dates back to the 1980s when it was used to make synthesizers, samplers, and
sequencers communicate.
These older devices used cables with 5-pin DIN connectors to carry MIDI signals.
Most MIDI devices today send the MIDI signals over a USB cable.
Some modern devices can also use cables with the 5-pin DIN connectors.
DJ controllers with these 5-pin DIN connectors do not ordinarily use them to
send signals to the computer; they are used to communicate via MIDI with other
gear and the ability to use MIDI without being plugged into a computer (although
they need to be plugged into another power source without a USB cable supplying
power).

Controllers that comply with the USB MIDI class standard (also called “class
compliant” devices) do not require any special drivers.
Most controllers are USB MIDI class compliant, but not all.
See the :ref:`manual for your hardware <hardware-manuals>` for information about
particular controllers.

Mixxx displays the numbers in MIDI signals in hexadecimal.
If you are unfamiliar with hexadecimal numbers, read `this tutorial
<http://codemastershawn.com/2014/04/03/understanding-binary-and-hex-numbers>`__.

An explanation of the MIDI signals that your controller sends to
computers and how it reacts to MIDI signals that computers send to it
should be available from the controller manufacturer. This is likely in
a document on the product page for your controller on the manufacturer’s
website or in the support section of the website. If it is not in a
separate document, it is likely at the end of the manual. Unfortunately,
not every manufacturer provides this information.

MIDI Messages
-------------

Most MIDI messages are three bytes long. The first byte of any MIDI
message is called the **Status** byte. The first nybble (hex digit) is
the op-code and the second is the MIDI channel number. So if you have
``0x90`` the op-code is ``0x9`` and the channel number is ``0x0`` (Ch
1.) The full list of MIDI messages is below, where *n* represents the
channel number (0..F inclusive):

+------------+------------------------+-----------------+----------------+
| Status     | Function               | Data bytes      |                |
+============+========================+=================+================+
| **0x8\ n** | **Note off**           | **Note number** | **Note         |
|            |                        |                 | velocity**     |
+------------+------------------------+-----------------+----------------+
| **0x9\ n** | **Note on**            | **Note number** | **Note         |
|            |                        |                 | velocity**     |
+------------+------------------------+-----------------+----------------+
| 0xAn       | Polyphonic after-touch | Note number     | Amount         |
+------------+------------------------+-----------------+----------------+
| **0xB\ n** | **Control/mode         | **Control       | **Value**      |
|            | change**               | number**        |                |
+------------+------------------------+-----------------+----------------+
| 0xC\ *n*   | Program change         | Program number  | (n/a)          |
+------------+------------------------+-----------------+----------------+
| 0xD\ *n*   | Channel after-touch    | Amount          | (n/a)          |
+------------+------------------------+-----------------+----------------+
| **0xE\ n** | **Pitch wheel**        | **LSB**         | **MSB**        |
+------------+------------------------+-----------------+----------------+
| 0xF0       | System Exclusive       | Vendor ID       | (data)         |
|            | message                |                 |                |
+------------+------------------------+-----------------+----------------+
| 0xF1       | MIDI Time Code Qtr.    | (see spec)      |                |
|            | Frame                  |                 |                |
+------------+------------------------+-----------------+----------------+
| 0xF2       | Song Position Pointer  | LSB             | MSB            |
+------------+------------------------+-----------------+----------------+
| 0xF3       | Song Select            | Song number     | (n/a)          |
+------------+------------------------+-----------------+----------------+
| 0xF4       | Undefined              |                 |                |
+------------+------------------------+-----------------+----------------+
| 0xF5       | Undefined              |                 |                |
+------------+------------------------+-----------------+----------------+
| 0xF6       | Tune request           | (n/a)           |                |
+------------+------------------------+-----------------+----------------+
| 0xF7       | End of SysEx (EOX)     | (n/a)           |                |
+------------+------------------------+-----------------+----------------+
| 0xF8       | Timing clock           | (n/a)           |                |
+------------+------------------------+-----------------+----------------+
| 0xF9       | Undefined              | (n/a)           |                |
+------------+------------------------+-----------------+----------------+
| 0xFA       | Start                  | (n/a)           |                |
+------------+------------------------+-----------------+----------------+
| 0xFB       | Continue               | (n/a)           |                |
+------------+------------------------+-----------------+----------------+
| 0xFC       | Stop                   | (n/a)           |                |
+------------+------------------------+-----------------+----------------+
| 0xFD       | Undefined              | (n/a)           |                |
+------------+------------------------+-----------------+----------------+
| 0xFE       | Active Sensing         | (n/a)           |                |
+------------+------------------------+-----------------+----------------+
| 0xFF       | System Reset           | (n/a)           |                |
+------------+------------------------+-----------------+----------------+

The boldface entries in the table above are the messages we are most
concerned with since most DJ controllers use only these for all
functions. You’ll need to consult the MIDI spec for the DJ controller
you’re working with to determine which messages and note/control numbers
correspond to the DJ controller functions & LEDs. If your controller’s
MIDI spec gives only note names and not numbers, `use this
table <http://www.wavosaur.com/download/midi-note-hex.php>`__ to convert
them. To convert from decimal to hex, `use
this <http://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html>`__.

(Note that in order to use System Exclusive messages, you will need
:ref:`midi-scripting`.)

Typical MIDI signals used by DJ controllers
-------------------------------------------

Every controller works differently, but these are some typical patterns.

Buttons
~~~~~~~

- When pressed: Op-code ``0x9``, value of ``0x7F``
- When released: Op-code ``0x9``, value of ``0x00``
- or Op-code ``0x8``, value of ``0x00``

LEDs
~~~~

If there’s a LED behind the button, usually it can be controlled by
sending a message to the controller using the same status and note
number that the controller sends when the button is pressed. As for the
value field, for LEDs that can only be turned on or off, typically
``0x00`` turns it off and ``0x01`` or ``0x7F`` turns it on. For
multi-color LEDs, the color is typically controlled by sending different
values. Which ones correspond to which colors should be in the MIDI
specification document for your controller. If they are not, you will
have to look at mappings for other DJ software, or just try a few
different values.

Knobs & sliders
~~~~~~~~~~~~~~~

These usually send messages with an op-code of ``0xB`` and a value
corresponding to the absolute position of the knob or slider (between
``0x00`` and ``0x7F``

Endless knobs/encoders (that you can turn continuously) typically send
messages with an op-code of ``0xB`` and the value only indicates whether
the encoder is being turned left or right (``0x01`` & ``0x7F`` or
``0x41`` & ``0x3F``)

Jog wheels, touch strips, platters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These usually operate exactly like endless knobs/encoders above, and
they usually also send messages just like buttons above when they’re
touched or released which is intended to mark when scratching begins and
ends respectively.
