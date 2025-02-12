Hercules DJControl Starlight
============================

Ultra-compact, ultra-light, ultra-practical and ultra-unique with its
lights, the DJControl Starlight packs all the features needed to mix and
scratch. With its built-in audio interface, the DJControl Starlight
offers pre-listening in the headphones so you can then play your mix on
speakers, which is perfect for learning or creating new mixes. The
system is so comprehensive for its size that it boasts all the essential
features such as bass equalization/filter knobs for smooth transitions
or touch-sensitive jog wheels for easy scratching. The added bonus: the
bright and powerful RGB backlighting.

-  `Manufacturer’s product page <https://www.hercules.com/en-us/product/djcontrolstarlight/>`__
-  `Manufacturer’s support and downloads page <https://support.hercules.com/en/product/djcontrolstarlight-en/>`__
-  `Forum thread <https://mixxx.discourse.group/t/hercules-djcontrol-starlight/17833/4>`__

.. versionadded:: 2.3

Compatibility
-------------

This controller is a class compliant USB :term:`MIDI` and audio device, so it can be used without any special drivers on GNU/Linux, macOS, and Windows.
However, if you wish to use the ASIO sound :term:`API` under Windows, please install the latest driver package available from the `Support page <https://support.hercules.com/en/product/djcontrolstarlight-en/>`__.

Sound card setup
----------------

This controller has built-in 4 channel output sound card, with main and headphone output (both 3.5mm jack).

-  Open **Preferences > Sound Hardware**
-  Select the **Output** tab
-  From the **Main** drop-down menu, select the audio interface, then **Channels 1-2**
-  From the **Headphones** drop-down menu, select the audio interface, then **Channels 3-4**
-  Click **Apply** to save the changes.

.. seealso::
   More details about audio configuration can be found in the :ref:`here <setup-laptop-and-external-card>`.

.. note::
   The **Main** and **Headphone** knobs are hardware controls and interact directly with the integrated sound card’s output.
   Although they also send :term:`MIDI` messages, they have NOT been mapped in Mixxx, so do not expect an on-screen reaction when using them.
   This was done to prevent the knobs to adjust both the gain on the controller’s sound card and in Mixxx.

   The :ref:`gain staging section of this manual <djing-gain-staging>` explains how to set your levels properly when using Mixxx.

Mapping description
-------------------

The base LED is linked to the VU Meter for light show effect on each deck respectively.

All controls not listed here work as labeled.

Decks
^^^^^

===================  =======================
Button               Description
===================  =======================
SYNC                 Sync lock
SHIFT + SYNC         Set deck as sync leader
CUE                  Cue point
SHIFT + CUE          Return to beginning of loaded song
PLAY                 Play/Pause
SHIFT + PLAY         Cue Stutter
VINYL                Scratch On/Off (Default: on)
SHIFT + Bass/Filter  Move FX chain metaknobs
===================  =======================

When Vinyl is on, turning a jog wheel scratches that deck. When Vinyl is
off, turning a jog wheel bends the pitch of the track.

Pads
^^^^

==========  =================  =======================
Pad Mode    Button             Description
==========  =================  =======================
Hot Cue     Pads 1-4           Set and trigger Hot Cue 1-4
Hot Cue     SHIFT + Pads 1-4   Pad = Delete Hot Cue 1-4.
Loop        Pad 1              Beatloop 1/2 beat
Loop        Pad 2              Beatloop 1 beat
Loop        Pad 3              Beatloop 2 beats
Loop        Pad 4              Beatloop 4 beats
FX          Pads 1-3           FX 1-3 on/off
FX          SHIFT + Pads 1-3   FX 1-3 select
FX          Pad 4              FX Rack 1/2 On/Off (Deck A/B respectively)
Sampler     Pads 1-4 (Deck A)  Sampler 1-4
Sampler     Pads 1-4 (Deck B)  Sampler 5-8
==========  =================  =======================
