American Audio VMS2
===================

The American Audio VMS2 is a 2-deck all-in-one controller. It is a USB
class compliant MIDI and audio device that works with GNU/Linux, Mac OS
X, and Windows. It features a 4 channel input and 4 channel output sound
card with 2 phono preamps. The main output has XLR and RCA outputs (do
not use both at once). There is a separate RCA booth output. The VMS2
can also be used as a stand-alone mixer with analog sources without a
computer by setting the USB/Analog switches on the front of the device
to “Analog”.

-  `Manufacturer’s product page <http://www.americandj.eu/en/vms2.html>`__, provides manual and drivers for download.
-  `Forum thread <http://www.mixxx.org/forums/viewtopic.php?f=7&t=3202>`__, for discussion of mapping options.
-  `Pull Request <https://github.com/mixxxdj/mixxx/pull/876>`__, which this wiki page describes.

Audio Setup
-----------

No driver needs to be installed on GNU/Linux or Mac OS X. However, on
Windows, it is recommended to install the driver from the manufacturer
to be able to use the `ASIO sound
API <http://mixxx.org/manual/latest/chapters/configuration.html#audio-api>`__.

Unlike most controllers with built in sound cards, which rely on Mixxx
to do all mixing in software, the VMS2 mixes signals from the sound card
in hardware. To use it with Mixxx:

-  Bypass the built-in hardware equalizer of the VMS2 (i.e. use Post-EQ
   Mode). Hold the forward search button on the right deck as you turn
   the VMS2 on to switch between Post-EQ and Pre-EQ modes. See section
   15 of the `manufacturer’s manual <http://adjmedia.s3-website-eu-west-1.amazonaws.com/manuals/vms2_print_EN.pdf>`__
   for details.
-  Set the USB/Analog switches on the front side of the VMS2 to “USB”
-  In Mixxx’s Sound Hardware Preferences:
-  Set the sample rate to 48000 Hz
-  Select channels 1-2 for Deck 1 output
-  Select channels 3-4 for Deck 2 output

*Note*: You cannot use the preview deck to pre-listen in this setup, as
Mixxx routes the preview deck to Mixxx’s headphone output, which is not
mixed with the Deck 1/2 outputs. You could use a separate soundcard and
route the headphone output there to also pre-listen using the preview
deck. Of course, if you do so, attach the headphones to that other
soundcard instead of the VMS2.

Input and Recording
~~~~~~~~~~~~~~~~~~~

The analog inputs are captured by the built-in soundcard as input
signals. They can be used for timecode signals (e.g. timecode vinyl), as
the VMS2 also features built-in phono preamps. FIXME I did not try that,
please verify!

The microphone input is mixed directly into the master output signal of
the VMS2 in hardware and cannot be captured through software. If you
want to record voice over using the Mixxx software, you will need a
different solution. You can use a separate microphone attached to the
computer, but that signal will not be routed to the VMS2 and therefore
not be on the VMS2 master output (but in the Mixxx recording from the
software master/record output).

Mixxx’s Deck 1/2 outputs are affected by the Mixxx software EQs.
However, the VMS2’s volume faders and crossfader (as well as the
headphone buttons) control the VMS2’s hardware mixer and do not affect
Mixxx’s Deck 1 and Deck 2 output signals. Therefore, a recording using
the Mixxx software will sound different from what is played through the
VMS2 master output, as the crossfader curve and signal mixing are not
the same in hardware and software. If you require a recording that
captures exactly what the audience will hear, use a separate soundcard
and recording software to record from the VMS2 booth output.

Mapping description
-------------------

Mixer section
~~~~~~~~~~~~~

All main functions are mapped straightforwardly:

============== ======================
VMS2 Control   Mixxx Control
============== ======================
Crossfader     Crossfader
Volume Fader   Volume Fader
Cue (PFL)      PFL
Cue Mix        Cue Mix (PFL / Master)
Headphone Gain Headphone Gain
Channel Gain   Channel Gain
Master Gain    Master Gain
============== ======================

As noted in the `#Audio Setup <#Audio%20Setup>`__ section, these control
the VMS2’s hardware mixer. Although the state of the controls is
reflected on screen in Mixxx, the actual mixing is done by the VMS2’s
hardware mixer.

Deck Control
~~~~~~~~~~~~

Deck control is straightforward, too:

===================== ===============================================
VMS2 Control          Mixxx Control
===================== ===============================================
Play                  Toggle deck play/pause
Pause                 Pause the deck
Cue                   Cue Point (configure behavior in software)
Pitch +/-             Temporary pitch bend +/-
Pitch Fader           Pitch Fader
Range (Shift+Sync)    Cycle pitch fader range (+-8/10/30/100%)
Sync                  Sync to other deck
Search <</>>          Search through currently loaded track
Keylock (Shift+Vinyl) Toggle pitch independent time stretch (KeyLock)
Vinyl                 Toggle between Scratch mode and Pitch mode
Platter               Touch sensitive platters! Scratch or Pitchbend
Shift + Platter       Scroll through library quickly
===================== ===============================================

In Pitch mode, moving the platters from either the top or side will only
bend the pitch of the deck. In Scratch mode, the platters act like vinyl
turntables and can be used for scratching. Touching and holding them
from the top stops the deck. Moving them from the edge does not stop the
deck.

Library and Track loading
~~~~~~~~~~~~~~~~~~~~~~~~~

Use the encoder in the center of the controller to browse through the
library. Press the encoder to switch between library main window and
sidebar. Unfortunately there seems to be no way to expand entries in the
sidebar through the controller script.

Use the [LOAD] buttons to load the currently selected track into either
the left or right deck.

The four directional buttons around the knob also control the library:

====== ======================
Button Library function
====== ======================
Up     Previous library entry
Down   Next library entry
Left   Previous sidebar entry
Right  Next sidebar entry
====== ======================

If you hold Shift and then rotate a platter, you can scroll through the
library much faster.

Equalizer
~~~~~~~~~

The per deck EQ rotaries are mapped to their software counterparts. The
VMS2 has no dedicated kill switches for the EQ. However, in Mixxx,
pressing the following buttons with Shift acts as EQ kill switches.

============ ================
VMS2 Control Mixxx Control
============ ================
Shift+IN     Kill Switch Low
Shift+OUT    Kill Switch Mid
Shift+RELOOP Kill Switch High
============ ================

Hotcues
~~~~~~~

The VMS2 can control 6 hotcues per deck.

+-------------------------------------------------+---------------------------+
| VMS2 Control                                    | Mixxx Control             |
+=================================================+===========================+
| 1 / 2 / 3                                       | Set/Jump HotCue 1 / 2 / 3 |
+-------------------------------------------------+---------------------------+
| Vinyl + 1 / 2 / 3                               | Delete HotCue 1 / 2 / 3   |
+-------------------------------------------------+---------------------------+
| 4 / 5 / 6 = (Shift + 1 / 2 / 3)                 | Set/Jump HotCue 4 / 5 / 6 |
+-------------------------------------------------+---------------------------+
| Vinyl + 4 / 5 / 6 = (Vinyl + Shift + 1 / 2 / 3) | Delete HotCue 4 / 5 / 6   |
+-------------------------------------------------+---------------------------+

Pressing the vinyl/keylock button will not toggle scratch mode or
keylock as long as a hotcue is deleted before releasing the
vinyl/keylock button.

Loops
~~~~~

==================== =========================================
VMS2 Control         Mixxx Control
==================== =========================================
IN                   Mark beginning of loop
OUT                  Mark end of loop
RELOOP               Leave / Reenter current loop
LOOP                 Start a 4 Beat loop from current position
Smart (Shift + Loop) Toggle quantize
(:2) / (*2)          Halve or double the current loop length
==================== =========================================

As Mixxx currently only supports one active loop per deck, the secondary
loop controls have been remapped to EQ kill switches.
