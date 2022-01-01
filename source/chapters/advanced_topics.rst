.. include:: /shortcuts.rstext

Advanced Topics
***************

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

For a list of controls that can be used in a keyboard mapping, see
:ref:`appendix-mixxxcontrols`.

You can download and share custom keyboard mappings in the
`Mixxx User customizations forums <https://mixxx.org/forums/viewforum.php?f=6>`_.

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

Deleting Your Library
=====================

The library file is stored in the following places depending on your
:term:`operating system`:

**Windows**
  The Mixxx library is stored in the
  :file:`%USERPROFILE%\\Local Settings\\Application Data\\Mixxx\\` folder.
  To delete your library on Windows, delete the :file:`mixxxdb.sqlite` file in
  this folder.

**macOS**
  The Mixxx library is stored in the :file:`Library/Application Support/Mixxx`
  folder in your home directory. To delete your library on macOS type the
  following command into a terminal: ::

       rm ~/Library/Application\ Support/Mixxx/mixxxdb.sqlite

**GNU/Linux**
  The Mixxx library is stored in the ``.mixxx`` folder in your home directory.
  To delete your library on GNU/Linux type the following command into a terminal: ::

       rm ~/.mixxx/mixxxdb.sqlite

.. warning:: Deleting your library will lose all of your :term:`metadata`. This
             includes saved hotcues, loops, comments, ratings, and other library
             related metadata. Only delete your library if you are fine with
             losing these.
