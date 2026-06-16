# Nintendo Wii Remote

:::{versionadded} 1.11
:::

- [Forum thread](https://mixxx.discourse.group/t/nintendo-wiimote-hid-mapping/12649)

The Nintendo Wii Remote (Wiimote) can be used to control Mixxx on
Windows.

## Requirements

- A **Windows** computer with Bluetooth
- Mixxx
- [GlovePIE](http://glovepie.org/) — the Wiimote interpreter
- [LoopBe1](http://www.nerds.de/en/loopbe1.html) or
  [MIDI Yoke](http://www.midiox.com/index.htm?http://www.midiox.com/myoke.htm)
  — virtual MIDI device

## How it works

GlovePIE interprets signals from the Wiimote paired with your computer
over Bluetooth. These signals are converted to MIDI events and sent
through the virtual MIDI device to Mixxx. Mixxx then uses these events
to control various functions.

GlovePIE must be scripted to capture specific events, such as pressing
the 'B' button or using the built-in accelerometers. GlovePIE comes
with several example scripts that can be examined and adapted.
