.. include:: /shortcuts.rstext

Advanced Topics
***************

.. _advanced-controller:

Adding support for your MIDI/HID Controller
===========================================

With several dozens of DJ controllers supported out-of-the-box, Mixxx gives you
comprehensive hardware control for your DJ mixes, see :ref:`control-midi`.

Support for additional devices can be added to Mixxx by creating a new mapping
file. This file tells Mixxx how to translate, or map, :term:`MIDI`/:term:`HID`
messages from a controller into commands that Mixxx understands.

You can download and share custom controller mappings in the
`Mixxx User Controller Mapping forums <https://mixxx.discourse.group/c/controller-mappings/10>`_.

For a list of controls that can be used in a controller mapping, see
:ref:`appendix-mixxxcontrols`.


.. _advanced-controller-wizard:

Controller Wizard
-----------------

.. figure:: ../_static/Mixxx-111-Controller-Learning-Wizard.png
   :align: center
   :width: 50%
   :figwidth: 100%
   :alt: Mixxx Controller Wizard -  Mapping a control
   :figclass: pretty-figures

   Mixxx Controller Wizard -  Mapping a control

By far, the easiest way to create a new MIDI mapping is by using the Controller
Wizard.

#. Connect your controller(s) to your computer
#. Start Mixxx
#. Go to :menuselection:`Preferences --> Controllers`
#. Select your device from the list of available devices on the left, and the
   right pane will change
#. Activate the :guilabel:`Enabled` checkbox
#. Click on :guilabel:`Learning Wizard` to open the selection dialog
#. Click any control in the Mixxx :term:`GUI`
#. Alternatively, click the :guilabel:`Choose Control` button and choose one
   from the selection list
#. Push :guilabel:`Learn` and then move a control or push a button on your
   controller to map it.  You can also move a control without pushing the
   :guilabel:`Learn` button if you are learning many controls.
#. If you are learning a button, just push it once.  If you are learning a knob
   or a slider, try to move it throughout its range.
#. After Mixxx detects the control, you may click :guilabel:`Learn Another` or
   you can click on another button in the Mixxx :term:`GUI` to learn another
   control.
#. When you are finished mapping controls, click :guilabel:`Done`

There are also some advanced options in the Midi Wizard you may need to use:

* Soft Takeover: Use this option for knobs or sliders to avoid sudden jumps in
  when the knob in the :term:`GUI` doesn't match the physical knob. If you
  select this option, you won't be able to perform super-fast motions as easily.
  (Recommended off)
* Invert: Use this option for controls that you want to work backwards from how
  they were detected.
* Switch Mode: Use this option on controllers that have controls that act like
  switches and emit one value on the first press, and a different value on the
  next press. (Think an actual hardware toggle switch, or a button that lights
  up on the first press and turns off on the second press).
* Jog Wheel / Select Knob:  Use this for knobs that don't have a beginning or an
  end, but spin continuously.

The Controller wizard saves the new mapping to the ``controllers`` directory in
the user settings directory, see :ref:`appendix-settings-files`.


You can then modify the XML file it creates (or any of the ones that
ship with Mixxx) if you'd like to fine-tune it or add more mappings. For more
information, go to
`<https://github.com/mixxxdj/mixxx/wiki/MIDI-Controller-Mapping-File-Format>`_.

The Controller Wizard works only for :term:`MIDI` devices. Currently you can't
map modifier (shift) keys and platter rotations. Use :ref:`MIDI Scripting
<advanced-controller-midiscript>` instead.

.. _advanced-controller-midiscript:

MIDI Scripting
--------------

In order to support the advanced features of many :term:`MIDI`/:term:`HID`
controllers, Mixxx offers what we call MIDI Scripting.

It enables MIDI controls to be mapped to `QtScript
<https://en.wikipedia.org/wiki/QtScript>`_ (aka Javascript/EMCAScript) functions
stored in function library files, freeing Mixxx from a one-to-one MIDI mapping
ideology. These user-created functions can then do anything desired with the
MIDI event such as have a single controller button simultaneously affect
two or more Mixxx properties (“controls”), adjust incoming control values to
work better with Mixxx (scratching), display a complex LED sequence, or even
send messages to text displays on the controller.

For more information, go to `<https://github.com/mixxxdj/mixxx/wiki/Midi-Scripting>`_
and `<https://github.com/mixxxdj/mixxx/wiki/Hid-Mapping>`_
, as well as the `Comonents-JS library <https://github.com/mixxxdj/mixxx/wiki/Components-JS>`_
which greatly simplifies mapping, for example effect units and complex behaviour
like switching deck layers or pad grid modes. Note that this is the preferred way
of mapping if intended your mapping to be included in Mixxx since Components-JS
significantly reduces effort for both mapping and reviewing Pull Requests.

.. _advanced-keyboard:

Making a Custom Keyboard Mapping
================================

The :ref:`default keyboard mappings<appendix-keyboard>` are defined in a text
file which can be found at the following location:

* Linux: :file:`/usr/local/share/mixxx/keyboard/en_US.kbd.cfg`
* macOS: :file:`/Applications/Mixxx.app/Contents/Resources/keyboard/en_US.kbd.cfg`
* Windows: :file:`<Mixxx installation directory>\\keyboard\\en_US.kbd.cfg`

Depending on your system's language settings, Mixxx might use a different
file as default, e.g. :file:`de_DE.kbd.cfg` for German or :file:`es_ES.kbd.cfg`
for Spanish.

It is not recommended that you modify the system-wide keyboard mapping file
because all your changes may be lost if you uninstall or upgrade Mixxx.
Instead, copy the default mapping file to the following location:

* Linux: :file:`~/.mixxx/Custom.kbd.cfg`
* macOS: :file:`~/Library/Containers/org.mixxx.mixxx/Data/Library/Application Support/Mixxx/Custom.kbd.cfg`
* Windows: :file:`%LOCALAPPDATA%\\Mixxx\\Custom.kbd.cfg`

Then edit this file and save the changes. On the next startup, Mixxx will check
if :file:`Custom.kbd.cfg` is present and load that file instead of the default
mapping file. This has the advantage that you can always revert back to the
default mapping by deleting :file:`Custom.kbd.cfg`.

Note that the situation is a bit different with the menubar shortcuts in the `[KeyboardShortcuts]` section.
If you want to use any of these default menubar shortcuts for something else, it is not sufficient to remove
the respective line from the mapping file. The menubar will use the hard-coded defaults if doesn't find an
entry in the mapping file.
Hence, to use any of the menubar shortcuts, you need to supply another key to be picked up by the menubar.
This may be an unused key, or if you don't need the menubar shortcut at all, a key that's not present on
your keyboard and can also not be composed by accident, for example Cyrillic characters on a french keyboard.

For a list of controls that can be used in a keyboard mapping, see
:ref:`appendix-mixxxcontrols`.

You can download and share custom keyboard mappings in the
`Mixxx User Keyboard Mapping forums <https://mixxx.discourse.group/c/keyboard-mappings/12>`_.

.. _advanced-external-fx:

Additional Effects via external Mixer Mode
==========================================

Mixxx comes with a set of :ref:`native effects <effects>`.
Additionally, using the :ref:`external mixer mode <intro-how-mixxx-works>` you
can route each deck directly to 3rd party effect hosts.

The following examples are only intended to encourage experimentation, they are
not definitive guidance.

Effects via AU Lab on macOS
-------------------------------

.. figure:: ../_static/Mixxx-111-external-fx-aulab-setup.png
   :align: center
   :width: 90%
   :figwidth: 100%
   :alt: The Au Lab routing for external effects
   :figclass: pretty-figures

   The Au Lab routing for external effects on macOS

On macOS there is a simple and free way to give Mixxx access to the
collection of AU/VST/MAS plugins that are installed on your system.

* Install the free `SoundflowerBed <https://github.com/anastasiuspernat/SoundflowerBed/releases>`_,
  a system extension for inter-application audio routing.
* Install the free digital audio mixing application
  `AU Lab <https://www.apple.com/apple-music/apple-digital-masters/docs/au_lab.zip>`_.

.. hint:: macOS 10.15 (Catalina) introduces additional restrictions on running
          non-Apple software. Make sure to grant permission in
          `System Preferences --> Security & Privacy --> Microphone --> AU Lab`.

Alternatively, try `Blackhole <https://github.com/ExistentialAudio/BlackHole>`_,
a modern virtual audio driver that allows applications to pass audio to other
applications with zero additional :term:`latency`, and
`Hosting AU <http://ju-x.com/hostingau.html>`_, a free micro-sized
:term:`DAW` that hosts Audio Unit instruments and effect plugins.

**In Mixxx**

* Go to :menuselection:`Preferences --> Sound Hardware--> Output`
* Select for :guilabel:`Deck 1` the :guilabel:`Soundflower 16` device with
  :guilabel:`Channel 1-2`
* Select for :guilabel:`Deck 2` the :guilabel:`Soundflower 16` device with
  :guilabel:`Channel 3-4`
* Click the :guilabel:`Apply` button

**In AU Lab**

* Click on the :guilabel:`+` button to create a new configuration
* Add 2 stereo input tracks in the :guilabel:`Audio Input Tab`
* Add 2 stereo output tracks in the :guilabel:`Audio Output Tab`
* Click :guilabel:`OK`
* Change the audio input device to :guilabel:`Soundflower 16`
* Change the audio output device for example to :guilabel:`Built-in Output`
* Click :guilabel:`Create document`
* In the :guilabel:`Output 1` channel, select an effect from the drop-down
  menu, for example :menuselection:`Apple --> AUCompressor`

The effect should now react if you play a track in Mixxx.

Effects via JACK Rack on GNU/Linux
----------------------------------

.. figure:: ../_static/Mixxx-111-external-fx-jackrack-setup.png
   :align: center
   :width: 90%
   :figwidth: 100%
   :alt: The Jack routing for external effects
   :figclass: pretty-figures

   The Jack routing for external effects on GNU/Linux

Use `Jack <https://en.wikipedia.org/wiki/JACK_Audio_Connection_Kit>`_ to route
each deck directly through `JACK Rack <http://jack-rack.sourceforge.net/>`_
effect racks, or for more control you can use Ardour (or another :term:`DAW`)
using sends for effects. This gives Mixxx access to the extensive collection of
:term:`LADSPA` plugins.

Make sure the correct multichannel audio interface has been selected in Jack
(Jack settings visible bottom left). Note that Mixxx possibly labels its Jack
ports as :guilabel:`Portaudio`.

.. _advanced-migrate-settings:

Migrate your Mixxx library and settings to a new computer
=========================================================

If you move to a new computer, or to another operating system on the same computer, you can take your existing Mixxx setup with you. This includes your track library, settings, controller mappings and broadcast profiles.

You don't necessarily need to be able to run your previous Mixxx installation, all you need is your :ref:`settings directory <appendix-settings-files>` and the music directories you imported into your Mixxx library via :menuselection:`Preferences --> Library`.

Preparation
-----------

* If you still have access to your Mixxx installation open Mixxx, go to :menuselection:`Preferences --> Library` and uncheck :guilabel:`Rescan on startup`. If you are not able to start Mixxx anymore, e.g. if you only managed to recover your settings directory, you can do this manually in the settings file: open :file:`mixxx.cfg` with a text editor, delete the line with :file:`RescanOnStartup` and save the file.
* Make a copy of both the Mixxx settings directory and your music directories. Put all in a save place. **Do not restructure your music directories!**
* Install your new operating system, get your new PC ready.
* Get the current stable Mixxx version from `the official download page <https://mixxx.org/download/>`_.
* Install Mixxx, though **don't run it, yet!**

Migration
---------

* Copy your Mixxx settings directory to the appropriate location, see :ref:`appendix-settings-files`. In case you already started Mixxx previously, make sure to rename or delete your existing settings directory in order to avoid any file conflicts.
* Copy your music directories to the new computer.
* Start Mixxx.
* If you've put the settings directory in the correct location Mixxx should not ask you for your music directories and all your settings should be as before.
* Go to :menuselection:`Preferences --> Library` and **Relink** each of your music directories as described in :ref:`configuration-import`.

Now, all your music files should be available, all your playlists, crates and your session histories be restored. A library rescan is not required. Configure a sound output and test if you can play all tracks as before. Note that this will obviously not include your external libraries (iTunes, Traktor etc.), you need to configure those again.

Known issues
------------

If you migrated to another operating system, operating system version or another Mixxx version, the used
audio decoders may have changed which may cause beatgrids and cue points to appear shifted, i.e. they are
set off from the desired points in the audio stream. Unfortunately, there is no automatic fix available, yet.
As of now you need to shift cues for each track individually with the cue shift buttons in the beatgrid editing
controls section, see :ref:`interface-waveform`.

.. _advanced-migrate-flatpak:

Migrate your Mixxx library and settings to Flatpak
==================================================

Since version 2.5 Mixxx is also provided as Flatpak.

If you do want to switch from a distribution package or Mixxx built from source code to the Flatpak, a little setup is required. Flatpak stores Mixxx's database, settings, and custom controller mappings in a different location than the `~/.mixxx` directory that Mixxx has always used before. Flatpak uses `~/.var/app/org.mixxx.Mixxx/.mixxx` instead. To copy your database, settings, and controller mappings into the Flatpak sandbox, run:
::

  mkdir -p ~/.var/app/org.mixxx.Mixxx
  cp -r ~/.mixxx ~/.var/app/org.mixxx.Mixxx

If your library contains any directories outside of your XDG Music Directory (`~/Music` unless you have reconfigured this), you will need to relink these directories to access the files inside of Flatpak's sandbox. Run Mixxx from the Flatpak and go to :menuselection:`Options --> Preferences --> Library`. Any directories that have a warning icon with `!` in a yellow triangle need to be relinked. Select the directory in the preferences window and click the Relink button, then select the directory in the file picker dialog. Flatpak will automatically remap the directory under `/run/user` so Mixxx can read and write your music files from inside the Flatpak sandbox. Press Ok in the preferences window, then in Mixxx's main window, go to :menuselection:`Library > Rescan Library`.
