.. _reloop_digital_jockey_2_master_edition:

Reloop Digital Jockey 2 Master Edition
======================================

The *Reloop Digital Jockey 2 Master Edition* is a 2 deck USB MIDI controller
with an integrated 24 bit audio interface and a full analogue mixer section.
Compared to the *Interface Edition* it adds balanced master outputs, a booth
output, phono/line inputs with RIAA preamps and a microphone input, so it can
also be used as a stand-alone mixer without a computer.

-  `Manufacturer's product page <http://www.reloop.com/reloop-digital-jockey-2-me>`__
-  `Forum thread <https://mixxx.discourse.group/t/help-reloop-digital-jockey-2-master-edition/12583>`__

.. versionadded:: 1.8

.. important::
   This device is **not** USB :term:`MIDI` class compliant. Its signals are
   translated to :term:`MIDI` by a vendor driver, so a driver must be
   installed before Mixxx sees the controller or its audio interface.

   * **Windows and macOS** — use the driver from the manufacturer's product
     page linked above.
   * **GNU/Linux** — no vendor driver exists. Use the community driver
     `snd-usb-ozzy <https://github.com/julled/Ozzy-reloop>`__, an ALSA kernel
     module that provides audio and MIDI for this controller
     (`upstream pull request <https://github.com/mischa85/Ozzy/pull/80>`__).
     Without it the device enumerates as a vendor-specific USB device and
     neither the MIDI controls nor the sound card are available.

Compatibility
-------------

Once the driver is installed the controller registers as a normal sound card
with a MIDI port, and works on Windows, macOS and GNU/Linux.

.. note::
   Set the :hwlabel:`MIDI/PHONO/LINE` switch on the front panel to
   :hwlabel:`MIDI` for the channel you want to control from Mixxx. In the
   :hwlabel:`PHONO`/:hwlabel:`LINE` position that channel's gain, EQ and line
   fader stay in the analogue signal path and send no MIDI, so those controls
   appear dead in Mixxx while the buttons still work.

Mixxx Sound Hardware Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The audio interface runs at 44.1 kHz. Its inputs are assigned as follows:

.. table::
    :widths: 100 100

    ========================  =======================
    Input                     Channels
    ========================  =======================
    :guilabel:`Line In 1`     Channel 1 - 2
    :guilabel:`Line In 2`     Channel 3 - 4
    :guilabel:`Microphone`    Channel 5 - 6
    ========================  =======================

Mapping
-------

The controller shares its :term:`MIDI` layout with the
:ref:`Interface Edition <reloop_digital_jockey_2_interface_edition>`, and the
mapping follows that description, including the jog wheel modes, the
:hwlabel:`CUP` button behaviour and the :hwlabel:`SHIFT` layer.

In addition, this mapping uses two front panel controls that the
*Interface Edition* does not have:

.. table::
    :widths: 40 60

    ==============================  ==========================================
    Control                         Mapped to
    ==============================  ==========================================
    :hwlabel:`CROSS-FADER CURVE`    :mixxx:coref:`[Mixer Profile],xFaderCurve`
    :hwlabel:`MIC-LEVEL`            :mixxx:coref:`[Microphone],pregain`
    ==============================  ==========================================

.. note::
   :hwlabel:`PHONE-TONE` and :hwlabel:`MIC-TONE` are intentionally not
   mapped. They shape the analogue headphone and microphone path on the
   mixer itself and have no equivalent control in Mixxx.
