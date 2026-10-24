.. _pioneer-ddj-wego:

Pioneer DDJ-WeGO
================

.. sectionauthor::
   Samuel Nicholas
   Dmytro Hakman

The Pioneer DDJ-WeGO is a compact 2-channel DJ controller with an integrated
audio interface. This mapping adds 4-deck support (the two physical decks
switch between decks A/C and B/D with the :hwlabel:`DECK` button), jog wheel
scratching and pitch bend, jog-controlled effects ("Jog FX"), performance pads
in hot cue and sampler modes, and LED feedback including the jog ring.

- `Manufacturer's Product Page <https://www.pioneerdj.com/en/product/dj-controllers/ddj-wego/black/overview/>`__
- `Mapping Forum Thread <https://mixxx.discourse.group/t/pioneer-ddj-wego-mapping/34388>`__

Compatibility
-------------

The Pioneer DDJ-WeGO is USB audio and MIDI class compliant and works with
Linux, Windows, and macOS without needing to install any drivers.

Audio Setup
-----------

Configure Mixxx's :ref:`sound hardware settings <preferences-sound-hardware>`
as follows:

============ ========
Output       Channel
============ ========
Main         1-2
Headphones   3-4
============ ========

Controller Mapping
------------------

Decks
~~~~~

The controller has two physical decks. The :hwlabel:`DECK` button on each side
switches that side between decks A/C (left) and B/D (right). Because the
hardware does not remember the LEDs of a hidden deck, Mixxx re-sends them when
you switch back.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Control
     - Function
   * - :hwlabel:`PLAY/PAUSE`
     - Play or pause the track.
   * - :hwlabel:`SHIFT` + :hwlabel:`PLAY/PAUSE`
     - Censor (play in reverse while held, then resume where the track would be).
   * - :hwlabel:`CUE`
     - Behavior depends on the :ref:`cue mode <interface-cue-modes>`.
   * - :hwlabel:`SHIFT` + :hwlabel:`CUE`
     - Jump to the start of the track and stop.
   * - :hwlabel:`SYNC`
     - Sync tempo and phase to the other deck.
   * - :hwlabel:`SHIFT` + :hwlabel:`SYNC`
     - Toggle this deck as the sync leader.
   * - :hwlabel:`DECK`
     - Switch this side between decks A/C (left) or B/D (right).
   * - :hwlabel:`LOAD`
     - Load the track selected in the library into the deck.
   * - :hwlabel:`SHIFT` + :hwlabel:`LOAD`
     - Eject the loaded track.
   * - :hwlabel:`TEMPO` slider
     - Adjust playback speed. Uses soft-takeover so switching decks never jumps the tempo.

Loops
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Control
     - Function
   * - :hwlabel:`AUTO LOOP` (press)
     - Activate a loop at the current size, or toggle the existing loop on/off.
   * - :hwlabel:`SHIFT` + :hwlabel:`AUTO LOOP` (press)
     - Re-enable the last loop (reloop).
   * - :hwlabel:`AUTO LOOP` (turn)
     - Double or halve the loop size.
   * - :hwlabel:`SHIFT` + :hwlabel:`AUTO LOOP` (turn)
     - Beat jump forward or backward.

The loop size used at startup is configurable (see `Mapping settings`_).

Jog Wheels
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Control
     - Function
   * - Jog wheel (top, touched)
     - Scratch (move the play position).
   * - Jog wheel (outer edge)
     - Temporarily bend the tempo up or down.
   * - :hwlabel:`SHIFT` + jog wheel
     - Fast search through the track.

When a Jog FX button is lit (see below), the jog wheel controls the effect
instead of scratching (see the ``Scratch while in Jog FX mode`` setting under
`Mapping settings`_).

Performance Pads
~~~~~~~~~~~~~~~~~

The four performance pads per deck switch between hot cue and sampler modes
with the :hwlabel:`SAMPLER` button.

Hot Cue Mode
^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Control
     - Function
   * - Pad (unlit)
     - Save the current position as a hot cue.
   * - Pad (lit)
     - Jump to the hot cue.
   * - :hwlabel:`SHIFT` + Pad
     - Clear the hot cue.

Sampler Mode
^^^^^^^^^^^^

The four pads on the left deck control samplers 1-4. Mixxx shows the sampler
deck when a sampler is loaded.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Control
     - Function
   * - Pad (empty)
     - Load the track selected in the library into the sampler.
   * - Pad (loaded, stopped)
     - Play the sample from its cue point.
   * - Pad (loaded, playing)
     - Stop the sample and return to the cue point.
   * - :hwlabel:`SHIFT` + Pad (playing)
     - Stop the sample.
   * - :hwlabel:`SHIFT` + Pad (stopped)
     - Eject the sample.

Jog FX
~~~~~~

The Jog FX buttons turn the jog wheel into an effect controller. Each deck is
routed to its matching effect unit (deck 1 to effect unit 1, and so on); this
routing can be turned off (see `Mapping settings`_). While a button is lit the
jog wheel sends the effect value and the jog ring shows its position.

:hwlabel:`CTRL A` and :hwlabel:`CTRL B` are mutually exclusive: turning one on
turns the other off.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Control
     - Function
   * - :hwlabel:`CTRL A`
     - Jog wheel controls the effect unit's dry/wet mix.
   * - :hwlabel:`FX1` / :hwlabel:`FX2` / :hwlabel:`FX3`
     - Enable or disable effects 1-3 in the unit.
   * - :hwlabel:`SHIFT` + :hwlabel:`FX1` / :hwlabel:`FX2` / :hwlabel:`FX3`
     - Load the next effect in that slot.
   * - Jog wheel (with an FX button lit)
     - Adjust that effect's metaknob.
   * - :hwlabel:`CTRL B`
     - Jog wheel controls the deck's filter (QuickEffect superknob). Turning it off re-centers the filter.

Mixer
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Control
     - Function
   * - Channel fader
     - Adjust the deck's volume.
   * - EQ (:hwlabel:`HI` :hwlabel:`MID` :hwlabel:`LOW`)
     - Boost or cut the deck's frequency bands.
   * - :hwlabel:`CROSS FADER`
     - Fade between the left and right channels.
   * - Headphone :hwlabel:`CUE`
     - Send the channel to the headphones.
   * - :hwlabel:`HEADPHONES MIXING`
     - Blend between cue and main in the headphones.
   * - Channel level meters
     - Show each deck's level.

By default the mixer controls use soft-takeover so that switching a deck
between A/C or B/D does not jump the volume or EQ (see `Mapping settings`_).

Browser
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Control
     - Function
   * - :hwlabel:`BROWSE` (turn)
     - Move the selection up or down in the library.
   * - :hwlabel:`SHIFT` + :hwlabel:`BROWSE` (turn)
     - Move the selection faster.
   * - :hwlabel:`BROWSE` (press)
     - Open or load the selected item.
   * - :hwlabel:`SHIFT` + :hwlabel:`BROWSE` (press)
     - Switch focus between the library panes.

Mapping settings
----------------

This mapping exposes a few options in
:menuselection:`Preferences --> Controllers`, under the mapping settings for
the DDJ-WeGO:

Initial auto loop size (beats)
    Beat length the :hwlabel:`AUTO LOOP` button uses at startup (default 4).
    Turn the encoder to change it while running.

Blink SYNC on beat
    Blink the :hwlabel:`SYNC` LED on every beat instead of showing the sync
    state (off by default).

Route deck N to effect unit N
    On startup, route each deck into the effect unit its Jog FX buttons
    control (on by default). Turn off to keep your own effect routing.

Soft-takeover for mixer controls
    Ignore the volume, EQ, crossfader and headphone mix until the knob or
    fader passes the on-screen value, so switching decks does not jump them
    (on by default). The shared tempo slider always uses soft-takeover.

Scratch while in Jog FX mode
    When a Jog FX button is lit the jog wheel turns the effect. Off by
    default, so touching the jog then does nothing and the track keeps
    playing. Turn on to let the jog still scratch (which stops playback while
    held) in Jog FX mode.
