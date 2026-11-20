.. _pioneer-ddj-1000:

Pioneer DDJ-1000
================

.. sectionauthor::
   Serhii O. Pashchenko <s.o.pashchenko@gmail.com>

.. TODO: add a schematic figure (../../_static/controllers/pioneer_ddj_1000.svg)
   like the other Pioneer pages once one is drawn.

The Pioneer DDJ-1000 is a 4-deck USB controller designed for rekordbox, with a
built-in audio interface, full-size jog wheels with displays in their centres,
RGB performance pads and a club-style mixer and effects section. The mapping
follows the functions printed on the unit and the functions rekordbox assigns
to them as closely as Mixxx allows.

- `Manufacturer's Product Page <https://www.pioneerdj.com/product/controller/ddj-1000/>`__
- `Manufacturer's Operating Instructions <https://www.manualslib.com/manual/1436395/Pioneer-Dj-Ddj-1000.html>`__
- `List of MIDI messages <https://downloads.support.alphatheta.com/software_info/dj-controllers/DDJ-1000/DDJ-1000_MIDI_Message_List_E1.pdf>`__

.. TODO: add "- `Mapping Forum Thread <...>`__" to the list above once the
   thread exists.

.. versionadded:: 2.5.7

Compatibility
-------------

The DDJ-1000 needs the manufacturer's driver on Windows and macOS: download
it from the product's support page. The controller is not USB audio class
compliant; on Linux its audio interface needs a patched kernel driver.

.. TODO: confirm Linux MIDI support before submitting.

Audio Setup
-----------

Select the DDJ-1000 in Mixxx's :ref:`sound hardware settings
<preferences-sound-hardware>`. On Windows, use the :guilabel:`ASIO` sound API
with the ``DDJ-1000 ASIO`` device for low latency.

============ ========
Output       Channel
============ ========
Main         1-2
Headphones   3-4
============ ========

The :hwlabel:`HEADPHONES LEVEL`, :hwlabel:`HEADPHONES MIXING`,
:hwlabel:`MASTER LEVEL`, :hwlabel:`BOOTH MONITOR LEVEL` and
:hwlabel:`MASTER CUE` controls act on the controller's hardware and are not
mapped. The controller blends the headphone channels (3-4) with main (1-2)
using its :hwlabel:`HEADPHONES MIXING` knob, so by default the mapping sets
Mixxx's own headphone mix to cue only while the controller is connected (see
:ref:`pioneer-ddj-1000-settings`).

.. _pioneer-ddj-1000-mono-split:

Headphones mono split
~~~~~~~~~~~~~~~~~~~~~

:hwlabel:`SHIFT` + :hwlabel:`QUANTIZE` (or :guilabel:`SPLIT` in the skin's
mixer) switches the headphones between stereo and mono split: the cue mix in
the left ear and main in the right, both in mono. Turn the controller's
:hwlabel:`HEADPHONES MIXING` knob fully to :hwlabel:`CUE` while split is on,
otherwise the controller also mixes main into the left ear.

.. TODO: check on the hardware whether the MIC 1/2 inputs appear as inputs in
   Mixxx's sound hardware preferences, and document it here.

.. _pioneer-ddj-1000-settings:

Mapping Settings
----------------

These options are in :menuselection:`Preferences --> Controllers --> Pioneer DDJ-1000`.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Setting
     - Effect
   * - Let the controller mix cue and main in the headphones
     - On (default): Mixxx's headphone mix is set to cue only and the
       :hwlabel:`HEADPHONES MIXING` knob on the controller blends cue and main.
   * - Tempo range when the mapping starts
     - Keep the Mixxx preference (default), or start every deck at ±6, ±10,
       ±16 or ±100 % as rekordbox does.
   * - COLOR knobs only work while a SOUND COLOR FX button is on
     - Off (default): the :hwlabel:`COLOR` knobs always control each deck's
       Quick Effect. On: they do nothing until a
       :hwlabel:`SOUND COLOR FX` button is lit, as in rekordbox.
   * - DUB ECHO / PITCH / NOISE / FILTER button: Quick Effect preset number
     - The Quick Effect chain preset each :hwlabel:`SOUND COLOR FX` button loads
       on all four decks, counted in the order of the Quick Effect preset list
       (0 keeps each deck's own preset).

.. _pioneer-ddj-1000-changes:

Changes to your Mixxx setup
---------------------------

Some controls change Mixxx settings that outlast a single button press:

- **Put back on disconnect:** Mixxx's headphone mix (setting above), the tempo
  range set at startup, effect unit 1's routing (changed by
  :hwlabel:`BEAT FX CH SELECT`) and the Quick Effect on/off switches (only with
  the "COLOR knobs only work while a SOUND COLOR FX button is on" setting).
  Anything you changed yourself in the meantime is left as you set it.
- **Memory cues** (:hwlabel:`MEMORY`) are stored as hot cues 17-36. They show
  up as hot cues on the waveforms, in skins and on other controllers, and a hot
  cue you set in that range elsewhere counts as a memory cue. :hwlabel:`MEMORY`
  only uses free hot cues; :hwlabel:`SHIFT` + :hwlabel:`MEMORY` deletes one.
- **CUE/LOOP CALL on a paused deck** moves the deck's cue point to the called
  cue, as on a CDJ. This replaces the cue point stored with the track.
- **Samplers:** the :hwlabel:`SAMPLER` pads use the samplers Mixxx already has,
  8 per bank. The mapping never adds samplers; show more samplers in the skin
  to get more banks.

Controller Mapping
------------------

Page numbers refer to the manufacturer's Operating Instructions.
:hwlabel:`SHIFT` combinations are done by the controller itself.

Browser section (p. 5)
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Control
     - Function
   * - Rotary selector (turn)
     - Move the selection in the library.
   * - :hwlabel:`SHIFT` + rotary selector
     - Zoom the waveforms in or out.
   * - Rotary selector (press)
     - Load the selected track into the deck on that side (deck 1/3 on the left,
       2/4 on the right). In the sidebar, open the selected item and move to
       its track list instead.
       Press twice quickly to clone the other deck on the same side
       (instant double).
   * - :hwlabel:`BACK`
     - Move focus between the sidebar and the track table.
   * - :hwlabel:`VIEW`
     - Maximize the library, or return to the decks.
   * - :hwlabel:`VIEW` (hold)
     - Add the selected track to the end of the :ref:`Auto DJ <library-auto-dj>` queue.

Deck sections (p. 6-7)
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Control
     - Function
   * - :hwlabel:`PLAY/PAUSE`
     - Play or pause.
   * - :hwlabel:`CUE`
     - Behaviour depends on the :ref:`cue mode <interface-cue-modes>`;
       :guilabel:`Pioneer` mode matches rekordbox.
   * - :hwlabel:`SHIFT` + :hwlabel:`CUE`
     - Jump to the start of the track.
   * - Jog wheel, top
     - With :hwlabel:`VINYL` on: scratch. Let go of a spinning platter and the
       track follows it until it slows down. With :hwlabel:`VINYL` off: pitch bend.
   * - Jog wheel, outer ring
     - Pitch bend. After a scratch or backspin the ring is ignored until the
       platter has stopped, so a coasting platter does not change the speed.
   * - :hwlabel:`SHIFT` + jog wheel
     - Search through the track.
   * - :hwlabel:`SEARCH` (hold) + jog wheel
     - Search through the track quickly.
   * - :hwlabel:`TEMPO` slider
     - Playback speed. Soft takeover prevents jumps
       when switching between decks 1/3 or 2/4.
   * - :hwlabel:`MASTER TEMPO`
     - Toggle :term:`key lock`.
   * - :hwlabel:`SHIFT` + :hwlabel:`MASTER TEMPO`
     - Cycle the tempo range: ±6, ±10, ±16, ±100 %.
   * - :hwlabel:`BEAT SYNC`
     - Toggle :term:`sync lock`.
   * - :hwlabel:`SHIFT` + :hwlabel:`BEAT SYNC`
     - Make this deck the sync leader.
   * - :hwlabel:`KEY SYNC`
     - Match the key of the other deck(s).
   * - :hwlabel:`KEY RESET`
     - Return to the track's original key.
   * - :hwlabel:`QUANTIZE`
     - Toggle quantize on all decks.
   * - :hwlabel:`SHIFT` + :hwlabel:`QUANTIZE`
     - Toggle headphones :ref:`mono split <pioneer-ddj-1000-mono-split>`. The
       :hwlabel:`QUANTIZE` button shows the state while :hwlabel:`SHIFT` is held.
   * - :hwlabel:`SLIP`
     - Toggle slip mode.
   * - :hwlabel:`SHIFT` + :hwlabel:`SLIP`
     - Toggle :hwlabel:`VINYL` mode (scratching with the jog wheel top).
   * - :hwlabel:`SLIP REVERSE`
     - Play in reverse while held, with slip. Releases by itself after 8 beats.
   * - :hwlabel:`SHIFT` + :hwlabel:`SLIP REVERSE`
     - Toggle reverse playback.
   * - :hwlabel:`LOOP IN`
     - Set the loop start. While a loop plays: halve the loop (:hwlabel:`1/2X`).
   * - :hwlabel:`SHIFT` + :hwlabel:`LOOP IN`
     - Move the loop start with the jog wheel; press again (or any loop button)
       to finish. The button blinks while adjusting.
   * - :hwlabel:`LOOP OUT`
     - Set the loop end. While a loop plays: double the loop (:hwlabel:`2X`).
   * - :hwlabel:`SHIFT` + :hwlabel:`LOOP OUT`
     - While a loop plays, move the loop end with the jog wheel. Otherwise, reloop.
   * - :hwlabel:`4 BEAT LOOP/EXIT`
     - Start a 4-beat loop, or leave the current loop.
   * - :hwlabel:`SHIFT` + :hwlabel:`4 BEAT LOOP/EXIT`
     - Enable or disable the stored loop without jumping.
   * - :hwlabel:`SEARCH` :hwlabel:`<<` / :hwlabel:`>>` (press)
     - :hwlabel:`<<`: go to the start of the track, or load the previous track
       from the library when already at the start. :hwlabel:`>>`: load the next
       track. Tracks are never loaded into a playing deck.
   * - :hwlabel:`SEARCH` :hwlabel:`<<` / :hwlabel:`>>` (hold)
     - Search backwards or forwards, speeding up the longer it is held.
   * - :hwlabel:`SHIFT` + :hwlabel:`SEARCH` :hwlabel:`<<` / :hwlabel:`>>`
     - :hwlabel:`CUE/LOOP CALL`: jump to the previous or next stored point
       (cue point, hot cues and memory cues). When paused, the point becomes
       the cue point (this replaces the track's stored cue point, see
       :ref:`pioneer-ddj-1000-changes`).
   * - :hwlabel:`MEMORY`
     - Store the current position as a memory cue. Memory cues are kept as hot
       cues 17-36 in red, so they appear on the waveforms.
   * - :hwlabel:`SHIFT` + :hwlabel:`MEMORY`
     - :hwlabel:`DELETE`: remove the memory cue at (or within one second of)
       the current position.
   * - :hwlabel:`DECK 1/3`, :hwlabel:`DECK 2/4`
     - Switch the deck the side controls. The controller does this itself.

Jog dial display (p. 8)
~~~~~~~~~~~~~~~~~~~~~~~

The centre displays show the position bar (turning like a record at 33⅓ RPM),
the time (elapsed or remaining, following Mixxx's time display setting), BPM,
tempo, key and key shift, the cue point marker, and whether sync and sync
leader are on.

.. note:: Artwork and the waveforms on the jog displays are not supported:
          rekordbox draws them over a separate, undocumented protocol.

Mixer section (p. 8-9)
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Control
     - Function
   * - :hwlabel:`TRIM`, :hwlabel:`EQ` :hwlabel:`HI` / :hwlabel:`MID` / :hwlabel:`LOW`
     - Channel gain and equalizer.
   * - :hwlabel:`COLOR`
     - The deck's Quick Effect (the filter by default).
   * - Channel faders, crossfader
     - Channel volume and crossfader.
   * - :hwlabel:`SHIFT` + channel fader or crossfader
     - Fader start: moving up plays the deck, moving down returns to the cue point.
   * - Crossfader assign switches
     - Assign each deck to side A, THRU or side B of the crossfader.
   * - Headphones :hwlabel:`CUE`
     - Toggle headphone cueing for the deck.
   * - :hwlabel:`SHIFT` + headphones :hwlabel:`CUE`
     - Tap the track's BPM.
   * - Channel level meters
     - Show each deck's level.
   * - :hwlabel:`SAMPLER VOL`
     - Volume of all samplers.
   * - :hwlabel:`SAMPLER CUE`
     - Toggle headphone cueing for all samplers.
   * - :hwlabel:`SOUND COLOR FX` buttons
     - Light the chosen effect and, if set up in the
       :ref:`mapping settings <pioneer-ddj-1000-settings>`, load a Quick Effect
       preset for all decks. Press again to switch off.

Beat FX section (p. 9)
~~~~~~~~~~~~~~~~~~~~~~

:hwlabel:`BEAT FX` controls :ref:`effect unit 1 <effects>`.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Control
     - Function
   * - :hwlabel:`BEAT FX SELECT`
     - Load effect unit 1's chain preset: position 1 (LOW CUT ECHO) loads the
       first preset in the effect chain preset list, and so on, skipping the
       two roll positions. Arrange the list in
       :menuselection:`Preferences --> Effects` to choose which effect each
       position loads. Positions without a preset leave the unit as it is.
       The effect names on the controller's display are fixed and will not
       match your presets.
   * - :hwlabel:`SLIP ROLL`, :hwlabel:`ROLL` positions
     - :hwlabel:`BEAT FX ON/OFF` starts a loop roll (with or without slip) on
       the selected channel, or on all playing decks for :hwlabel:`MASTER`.
   * - :hwlabel:`BEAT FX CH SELECT`
     - Route the effect unit to channel 1-4, :hwlabel:`MASTER`,
       :hwlabel:`MIC` (Mixxx's microphone channels) or :hwlabel:`SAMPLER`.
       The controller does not report this switch when Mixxx starts, so
       until it is moved the effect unit keeps the routing set in Mixxx. The
       routing is put back when the controller is disconnected.
   * - :hwlabel:`LEVEL/DEPTH`
     - Dry/wet mix of the effect unit.
   * - :hwlabel:`BEAT` :hwlabel:`<` / :hwlabel:`>`
     - Roll positions: halve or double the roll length (1/16 to 32 beats).
       Other positions: turn the first effect's first parameter down or up
       (its time for echo, flanger, phaser and similar effects).
   * - :hwlabel:`BEAT FX ON/OFF`
     - Switch the effect unit on or off.
   * - :hwlabel:`SHIFT` + :hwlabel:`BEAT FX ON/OFF`
     - :hwlabel:`RELEASE FX`: switch the effect off. With
       :hwlabel:`BEAT FX CH SELECT` on channel 1-4 that deck also stops with
       a vinyl brake; :hwlabel:`MASTER`, :hwlabel:`MIC` and
       :hwlabel:`SAMPLER` never stop a deck.

Performance pads (p. 6)
~~~~~~~~~~~~~~~~~~~~~~~

The mode buttons select what the pads do. :hwlabel:`SHIFT` + a mode button
selects the mode written below it, and lights that mode's button.
:hwlabel:`PAGE` :hwlabel:`<` / :hwlabel:`>` switch between the two pages of a
mode. :hwlabel:`SHIFT` + :hwlabel:`PAGE` :hwlabel:`<` / :hwlabel:`>` change
the sampler bank in any mode. In the tables, pads 1-4 are the top row and
pads 5-8 the bottom row.

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Mode
     - Pads
     - :hwlabel:`SHIFT` + pad
   * - :hwlabel:`HOT CUE`
     - Hot cues 1-8 (page 2: 9-16) in their colours. An empty pad sets a hot
       cue, or saves the playing loop. Holding a pad while paused previews it.
       A playing saved loop blinks.
     - Delete the hot cue.
   * - :hwlabel:`PAD FX1`
     - Page 1: pads 1-3 play effect 1, 2 or 3 of effect unit 3 on this deck
       while held, pad 4 the whole unit; pads 5-8 loop roll 1/16, 1/8, 1/4,
       1/2 beat. Page 2: the same with effect unit 4; rolls 1/32, 1, 2, 4.
     - Same as without :hwlabel:`SHIFT`.
   * - :hwlabel:`PAD FX2`
     - Page 1: vinyl brake, backspin, reverse (all with slip, so the track
       carries on where it would have been; a paused deck stays paused),
       roll 3/4; pads 5-8 effect unit 4. Page 2: the same tricks with roll
       3/2; pads 5-8 effect unit 3.
     - Same as without :hwlabel:`SHIFT`.
   * - :hwlabel:`BEAT JUMP`
     - Jump back or forward 1, 1, 2, 2 / 4, 4, 8, 8 beats (odd pads back, even
       pads forward). :hwlabel:`PAGE` :hwlabel:`<` / :hwlabel:`>` halve or
       double the distances.
     - Same as without :hwlabel:`SHIFT`.
   * - :hwlabel:`SAMPLER`
     - Play sampler 1-8 of the current bank from the start. An empty sampler
       loads the track selected in the library. :hwlabel:`PAGE`
       :hwlabel:`<` / :hwlabel:`>` change the bank (8 samplers per bank, as
       many banks as Mixxx has samplers).
     - Stop the sampler.
   * - :hwlabel:`KEYBOARD`
     - Play the chosen hot cue shifted by +4, +5, +6, +7 / 0, +1, +2, +3
       semitones (page 2: -4 to -1 / -8 to -5). Without that hot cue, the cue
       point is used.
     - Choose the hot cue (1-8) to play.
   * - :hwlabel:`BEAT LOOP`
     - Loops of 1/4, 1/2, 1, 2 / 4, 8, 16, 32 beats (page 2: 1/32, 1/16, 1/8,
       1/4 / 1/2, 1, 2, 4). Press the lit pad again to leave the loop.
     - Nothing.
   * - :hwlabel:`KEY SHIFT`
     - Shift the key by +4, +5, +6, +7 / 0, +1, +2, +3 semitones (page 2: -4
       to -1 / -8 to -5). Press the lit pad again to return to 0.
     - Same as without :hwlabel:`SHIFT`.

.. note:: Effects held from the pads are routed to the pad's deck only while
          the pad is held (also off :guilabel:`Main`, the headphones, samplers
          and microphones). The effect unit's routing and effect switches are
          restored when it is released, so the unit can still be used from
          the GUI.

Differences from rekordbox
--------------------------

- Artwork and waveforms on the jog displays are not shown.
- :hwlabel:`BEAT FX`, :hwlabel:`PAD FX` and :hwlabel:`SOUND COLOR FX` use
  Mixxx's effects, chosen through effect chain presets and effect units rather
  than rekordbox's fixed effect list.
- rekordbox's related tracks (:hwlabel:`SHIFT` + :hwlabel:`VIEW`) and
  playlist palette (:hwlabel:`SHIFT` + :hwlabel:`BACK`) have no equivalent
  and are not mapped. The tag list (:hwlabel:`VIEW` held) is the Auto DJ queue.
- Memory cues are stored as hot cues 17-36.
