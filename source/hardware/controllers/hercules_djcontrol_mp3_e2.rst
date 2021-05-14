Hercules DJControl MP3 e2 / MP3 LE / Glow
=========================================

The Hercules DJ Control MP3 e2, MP3 LE, and Glow are USB controllers that have identical controls and share the same mapping.
These controllers do not have a built in sound card, so a :ref:`splitter cable <hardware-splitter-cables>` or :ref:`separate audio interface <hardware-audio-interfaces>` is recommended for use with it.

.. versionadded:: 1.11
.. versionchanged:: 2.3.0

This new version is intended to work in a more intuitive way. Once you click on a button, it does its original function.

.. note::
   These controllers are not class compliant :term:`MIDI` devices.
   On Linux, older versions of Mixxx required using a custom Hercules kernel module.
   This is neither necessary not recommended anymore.


.. figure:: ../../_static/controllers/hercules_djcontrol_mp3_e2_mapping.png
   :align: center
   :width: 100%
   :figwidth: 100%
   :alt: Hercules DJControl MP3 e2 (schematic view)
   :figclass: pretty-figures

   Hercules DJControl MP3 e2 (schematic view)


Mapping description (by function)
---------------------------------

Library
^^^^^^^

+----------------------------------------------------------------------------+------------+--------+
| Function                                                                   | Control    | Number |
+============================================================================+============+========+
| Toggle playlist selection                                                  | Folder     | 6      |
+----------------------------------------------------------------------------+------------+--------+
| Toggle track selection                                                     | Files      | 10     |
+----------------------------------------------------------------------------+------------+--------+
| Go one playlst/track up                                                    | Up arrow   | 8      |
+----------------------------------------------------------------------------+------------+--------+
| Go one playlst/track down                                                  | Down arrow | 8      |
+----------------------------------------------------------------------------+------------+--------+
| Loads the currently highlighted track into the corresponding deck (A or B) | Load A/B   | 18     |
+----------------------------------------------------------------------------+------------+--------+


Master/Headphones
^^^^^^^^^^^^^^^^^

+---------------------------------------------------------------------+-------------------+--------+
| Function                                                            | Control           | Number |
+=====================================================================+===================+========+
| Fades between left (channel 1) and right (channel 2) deck           | Crossfader        | 19     |
+---------------------------------------------------------------------+-------------------+--------+
| Toggles deck output to the headphones monitor on/off                | Headphone monitor | 20     |
+---------------------------------------------------------------------+-------------------+--------+

Decks / Channels
^^^^^^^^^^^^^^^^

Playing
'''''''

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------+
| Function                                                                                                                                                                                                                              | Control            | Number |
+=======================================================================================================================================================================================================================================+====================+========+
| Loads the currently highlighted track into the corresponding deck (A or B)                                                                                                                                                            | Load A/B           | 18     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------+
| Starts or stop a loaded track                                                                                                                                                                                                         | Play               | 14     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------+
| Sets the cue point if a track is stopped and not at the current cue point. Stops track and returns to the current cue point if a track is playing. Plays preview if a track is stopped at the cue point for as long as it’s held down | Cue                | 15     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------+
| Move Forward/Backward in track                                                                                                                                                                                                        | Forward / Backward | 12     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------+
| Enable or disable the scratch mode on all two decks                                                                                                                                                                                   | Scratch            | 7      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------+
| Seeks forwards and backwards in a stopped track. Temporarily changes the playback speed for playing tracks.  Absolute sync of the track speed to the jog wheel if scratch mode enabled                                                | Jog wheel          | 16     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------+

Volume / Equalizer / Effects
''''''''''''''''''''''''''''

+-----------------------------------------------------------------------------+--------------------+--------+
| Function                                                                    | Control            | Number |
+=============================================================================+====================+========+
| Controls the deck output volume, with soft takeover on deck switch.         | Deck volume slider | 17     |
+-----------------------------------------------------------------------------+--------------------+--------+
| Adjusts the gain of the low/medium/high equalizer filter. No soft takeover. | Equalizer knobs    | 5      |
+-----------------------------------------------------------------------------+--------------------+--------+
| Toggle Effects Selection                                                    | Shift              |  4     |
+-----------------------------------------------------------------------------+--------------------+--------+
| Toggle Effect 1/2/3 for corresponding deck (with shift activated)           | Button 1/2/3       | 11     |
+-----------------------------------------------------------------------------+--------------------+--------+

Loops
'''''

+----------+----------+--------+
| Function | Control  | Number |
+==========+==========+========+
| Loop 1   | Button 1 | 11     |
+----------+----------+--------+
| Loop 2   | Button 2 | 11     |
+----------+----------+--------+
| Loop 4   | Button 3 | 11     |
+----------+----------+--------+
| Loop 8   | Button 4 | 11     |
+----------+----------+--------+

Pitch / Syncing
'''''''''''''''

+------------------------------------------------------------------+---------------+--------+
| Function                                                         | Control       | Number |
+==================================================================+===============+========+
| Temporary Holds the pitch 4% higher while pressed                | Pitchbend +/- | 1      |
+------------------------------------------------------------------+---------------+--------+
| Adjust playback pitch / speed                                    | Pitch knobs   | 3      |
+------------------------------------------------------------------+---------------+--------+
| Automatically sets pitch so the BPM of the other deck is matched | Sync          | 13     |
+------------------------------------------------------------------+---------------+--------+
| Enable and lock Sync Mode                                        | Master Tempo  | 2      |
+------------------------------------------------------------------+---------------+--------+

Troubleshooting
---------------

Jog wheels not working or controller not responding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your jog wheels doesn’t work, or nothing works on the controller even when you have carefully read all other resources, you should be aware that this controller stores at least two configuration
options in the controller:

-  Enable/disable Jog Wheels
-  MIDI channel to use

and maybe a third one: Jog wheel sensitivity

With factory default settings, the jog wheels are enabled and the MIDI channel used is channel 1. The mapping is made for channel 1 only. If your controller is configured for another channel, nothing
will work and if you launch Mixxx with :literal:`-``-controllerDebug` parameter, you will have lines like this one showing in the logs when you press a button on the controller :

::

   Debug [Controller]: "DJ Control MP3 e2 : 3 bytes: B3 38 38 "

note the B3 here. it’s B<MIDI Channel # - 1>. So this controller is configured on channel 4. controller configured on channel 1 will show B0, which is correct.

To change these parameters, you have to use the configuration tool that comes with the Hercules driver on on `the Hercules support
page <http://ts.hercules.com/eng/index.php?pg=view_files&gid=17&fid=61&pid=241&cid=1>`__. Unfortunately, the configuration tool is only available for Windows and Mac OS X. We are not aware of any
solution for Linux. So if you normally use Linux, you will have to find a computer with Windows or Mac OS X, install the Hercules driver, plug-in the controller and change configuration. You will only
need to do this once, then the controller should work with Linux.

Controller not recognized as bulk controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It has been reported that when the Hercules drivers are installed on a Windows, the driver takes over the bulk communication with the controller so it cannot be recognized by Mixxx as a bulk
controller. Uninstall the Hercules driver and use it as a USB bulk controller.
