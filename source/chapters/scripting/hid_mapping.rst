.. include:: /shortcuts.rstext

.. _hid-mapping:

HID controller mapping
**********************

Mixxx doesn’t currently have a semantic mapping format for HID or USB
bulk-transfer mode controllers, so they must be handled entirely in
script. That said, the procedure to do so is exactly the same as for
:ref:`MIDI controllers that use scripting <midi-scripting>`, but you also add an
``incomingData`` function to handle all input from the controller.

The steps are:

1. Create your script file.
   The same function and file naming conventions as well as ``init`` and
   ``shutdown`` function requirements apply as with MIDI scripting.
2. The script file must also contain a function called ``incomingData``.
   This will receive all data packets from the controller and is responsible for
   parsing them and taking appropriate actions based on which bytes change. It
   has the same signature as the ``inboundSysex`` function in MIDI scripting.
3. Create an XML file that tells Mixxx the name of the controller and which
   script file(s) to load, but make sure to end the file name with ``.hid.xml``
   or ``.bulk.xml`` as appropriate.


Script file
-----------

Here is an example file containing the required elements:

::

   var SuperCool = {};

   SuperCool.init = function (ID,debugging) {
       // Do setup here
       if (debugging) print("SuperCool "+ID+" initialized!");
   }

   SuperCool.shutdown = function () {
       // Do shutdown steps here, like turning off all LEDs
   }

   SuperCool.incomingData = function(data,length) {
       // Parse packet data here & call relevant functions
   }

Packet format
~~~~~~~~~~~~~

There is no standard HID packet arrangement/structure. The length and
contents (and even
`endianness <https://en.wikipedia.org/wiki/Endianness>`__) are
completely up to the manufacturer. For input packets, you can watch the
incoming packets in Mixxx’s console output when running Mixxx with the
``--controllerDebug`` command line option. For output, you can examine
the USB descriptors of the HID device to figure out what packets to
send. On Linux you can use the
`usbhid-dump <https://github.com/DIGImend/usbhid-dump>`__ and
`hidrd-convert <https://github.com/DIGImend/hidrd>`__ tools to show
these descriptors in a human readable format. First, identify the USB
product and vendor ID of your device with lsusb:

::

   $ lsusb
   Bus 001 Device 004: ID 046d:c52b Logitech, Inc. Unifying Receiver

Here the vendor ID is 046d and the product ID is c52b. Use these with
usbhid-dump:

::

   usbhid-dump -dVENDORID:PRODUCTID | grep -v : | xxd -r -p | hidrd-convert -o spec

Refer to this
`tutorial <http://eleccelerator.com/tutorial-about-usb-hid-report-descriptors/>`__
for how to interpret the information from hidrd-convert.

Sending data to the controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you know what data you want to send, simply call
``controller.send()`` with:

- An array of data bytes to send,
- null (the second parameter is required for backwards compatibility,
  but it is actually ignored by Mixxx)
- The HID report ID. If the controller only supports a single report
  packet, set this as 0.

.. raw:: html

   <!-- end list -->

.. code:: javascript

   var byteArray = [ byte1, byte2, byte3, ..., byteN ];
   controller.send(byteArray, null, reportID);

XML file
--------

Here is an example containing everything you need. Just copy and change
the appropriate parts:

::

   <?xml version="1.0" encoding="utf-8"?>
   <MixxxControllerPreset schemaVersion="1" mixxxVersion="1.11+">
       <info>
           <name>SuperCool HID Controller</name>
           <author>Your Name Here</author>
           <description>HID mapping for the SuperCool controller</description>
           <devices> <!-- Optional section that Mixxx can use to auto-load presets on matching devices -->
               <!-- Get the vendor and product IDs for the controller from your operating system -->
               <product protocol="hid" vendor_id="0x1111" product_id="0x100" />
           </devices>
       </info>
       <controller id="SuperCoolHID">
           <scriptfiles>
               <file filename="SuperCool-Controller.js" functionprefix="SuperCool"/>
           </scriptfiles>
       </controller>
   </MixxxControllerPreset>

There is also an HID Packet Parser JS script in the ``res/controllers``
directory you can examine for parsing hints. If you would like to try using it
directly, simply add it to the top of the ``scriptfiles`` list in your XML
file:

::

    <file filename="common-hid-packet-parser.js" functionprefix=""/>

However, the structure of this library’s code is messy and it may cause
as many hassles to use it as it solves.


How to map a new HID device
---------------------------

Familiarise yourself with HID scripting by reading the previous sections
and looking into existing HID mappings. Basic programming knowledge is
required.

Inputs
~~~~~~

Run ``mixxx --controllerDebug`` and see which bytes change when you toy
around with the controls. Map these bytes to the mixxx controls.

Outputs (e.g. LEDs)
~~~~~~~~~~~~~~~~~~~

Go into Windows and download software which natively supports this
controller (e.g. you can use the demo of Traktor Pro for Traktor
Controllers). Get `USBlyzer <http://www.usblyzer.com/>`__ (it has a free
demo) and watch which signals the software sends and what that changes
on the controller. Then try to send something to these in your mapping
script via an output package and see if you are right. If yes, proceed
mapping them to the correct values.
