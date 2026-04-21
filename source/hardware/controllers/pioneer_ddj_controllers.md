# Pioneer DDJ Controllers

This page describes the Pioneer DDJ controllers support in MIXXX.

## MIXXX DDJ support

### Built-in support

  - [pioneer\_ddj-400](pioneer_ddj-400)
  - [pioneer\_ddj-rb](pioneer_ddj-rb)
  - [pioneer\_ddj-sb](pioneer_ddj-sb)
  - [pioneer\_ddj-sb2](pioneer_ddj-sb2)
  - [pioneer\_ddj-sb3](pioneer_ddj-sb3)
  - [pioneer\_ddj-sx](pioneer_ddj-sx)
  - [pioneer\_ddj-wego](pioneer_ddj-wego)
  - [ddj-sx2](ddj-sx2)

Complete list: [github
code](https://github.com/mixxxdj/mixxx/tree/master/res/controllers)

### User contributed mappings

  - DDJ-1000:
  - mapping: <https://www.mixxx.org/forums/viewtopic.php?f=7&t=13346>
  - technical info: [ddj-1000](ddj-1000)
  - DDJ-800: <https://www.mixxx.org/forums/viewtopic.php?f=7&t=13367>
  - DDJ-400: <https://www.mixxx.org/forums/viewtopic.php?f=7&t=12113>
  - DDJ-200: <https://www.mixxx.org/forums/viewtopic.php?f=7&t=13160>

## Generic DDJ Technical info

### DDJ-1000 vs DDJ-1000SRT

Note that the 1000SRT has technical differences fom the original 1000.
Similar story for the 800 vs 10000.

|             | Jog Screens |     | PionnerFX              |
| ----------- | ----------- | --- | ---------------------- |
|             | MIDI        | HID |                        |
| DDJ-1000    | yes         | yes | **Only** BeatFX Master |
| DDJ-1000SRT | **no**      | yes | Any inputs             |
| DDJ-800     | **FW bug**  | yes | Unk                    |

more info:
<https://www.mixxx.org/wiki/doku.php/ddj-1000#pioneer_hardware_effects>

### DDJ pad colors

  - 0: off
  - 1: blue
  - 7: cyan
  - 12: cyan-blue
  - 17: green
  - 22: dark green
  - 25: green
  - 27: yellow-green
  - 29: yellow
  - 31: yellow
  - 33: yellow
  - 36: orange
  - 38: orange
  - 40: orange-red
  - 41: red
  - 42: red
  - 52: pink
  - 57: pink dark
  - 60: pink-blue
  - 62: blue
  - 63: off
  - 64: white

<!-- end list -->

    *
    * >65: default    color for that mode

### DDJ midi codes

List of all Pioneer MIDI
codes:[https://github.com/pestrela/music/tree/master/ddj/1%20MIDI%20codes](here)

Inside the same family, the DDJ controllers are mostly compatible.

Differences are:

1.  Buttons added: these get a new MIDI code
2.  Buttons moved around: The maintain the same midi code unless the
    feature is slightly different
3.  Buttons removed: if needed these can be emulated using additional
    shift layers on the software side (because the hardware shift layer
    is typically already busy).

#### Serato Family

  - All "S" controllers (SB, SX, SX2, SZ ...)
  - All "R" controllers (RB, RX, ...)
  - DDJ-1000SRT

#### Rekordbox-only Family

  - DDJ-1000
  - DDJ-800
  - etc

#### XDJ family

  - XDJ-XZ
  - XDJ-RX2
  - etc

### DDJ Channels overview

|                 | Serato    | RB-only    | XDJ  |
| --------------- | --------- | ---------- | ---- |
| Mixer           | 1..4      | 1..4       | 5    |
| Effect          | 5+6       | 5 only     | 5    |
| Browser, Global | 7         | 7          | 1    |
| Jog Display     | NA        | 1..4       | 12   |
|                 |           |            |      |
| Pad regular     | 8,9,10,11 | 8,10,12,14 | 6..9 |
| Pad shift       | same      | 9,11,13,15 | same |
| Pad sub pages   | no        | yes        | no   |

the different DDJs can be emulated to use a single mapping. This
requires converting both input and output messages.

In [this traktor example](https://maps.djtechtools.com/mappings/9222),
DDJ-SZ midi messages are converted to DDJ-1000 messages, and then feed
to the DDJ-1000 mapping.

In [this other traktor
example](https://maps.djtechtools.com/mappings/10305), the whole mapping
was ported as a one-off to the XDJ-XZ.
