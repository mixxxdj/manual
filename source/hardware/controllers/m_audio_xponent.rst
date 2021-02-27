M-Audio Torq Xponent
====================

This device has been discontinued. M-Audio discontinued its DJ products after the company was bought by inMusic in 2012. This device is a class compliant USB audio and MIDI device, so it does not
require a special driver on any OS that Mixxx runs on.

.. versionadded:: 1.6

Note for Windows users
----------------------

Typically, the ASIO sound API is the best option on Windows and it requires an ASIO driver from the sound card manufacturer. However, it seems that the current version of the Xponent ASIO driver for
Windows interferes with the ability to send MIDI control messages to the Xponent. As a result, if you are running M-Audio’s Xponent ASIO drivers on Windows, the lights will not work. If you uninstall
the drivers, the lights will work, but you can no longer use the Xponent’s sound card with the ASIO sound API.

It is recommended to **use the WDM-KS sound API** instead. The sound card will appear as “Analog Connector 1 (Xponent Audio)” and “Analog Connector 2 (Xponent Audio)”. Connector 2 is the main out, and
Connector 1 is the headphones. The latency meter seems to run a bit higher than it did under ASIO, so keep this in mind, and test both setups with your own system to see how they compare. If you
require low latency as well as a lot of effects or time stretching, you may want to run with the ASIO driver at the expense of the lights.

.. note::
   Unfortunately a detailed description of this controller mapping is still missing.
   If you own this controller, please consider
   `contributing one <https://github.com/mixxxdj/mixxx/wiki/Contributing-Mappings#user-content-documenting-the-mapping>`__.
