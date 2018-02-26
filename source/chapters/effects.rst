.. _effects:

Effects
*******

Mixxx has a powerful sound effects system. Understanding how it works can open
you up to a wide variety of mixing techniques.

.. _effects-effect-unit:

Effect Units
============
Mixxx has 4 effect units. By default, only 2 of them are shown. The other 2
effect units can be shown by toggling the setting in the skin settings menu.

.. figure:: ../_static/effect-unit-collapsed.png
   :align: center
   :alt: An effect unit
   :figclass: pretty-figures

   An effect unit

Each effect unit can load up to 3 effects in a chain. These effects are
processed one after the other in series. You will hear different sounds
depending on the position of effects within the chain. Each effect in the chain
has its own button to toggle it on and off.

Effect units can process sound from:
  * decks
  * microphones
  * auxiliary inputs
  * the master mix
  * the :term:`PFL` (headphone) mix
  * left/middle/right crossfader buses

The buttons to route effect units to decks, microphones, and auxiliary inputs
are located in the deck, microphone, and auxiliary sections of the skin. The
buttons for routing other inputs to effect units are in different locations
depending on the skin.

If a channel is assigned to multiple effect units, those effect units are
chained together. This allows you to chain more than 3 effects at a time.

The mix knob crossfades between the dry signal (input to the unit) and the wet
signal (output of the last effect in the unit). This adjusts the level of all 3
effects in the unit together. When the knob is fully left, no sound will be
heard from the effect unit. When the knob is fully right, only the output of
the effect unit will be heard without any of the dry input signal.

Effects are processed after the deck faders and crossfader. This allows effects
like Echo and Reverb to continue outputting sound after their input has been
cut off by lowering the fader.

Effect Parameters & Metaknobs
=============================
Every effect within an :ref:`Effect Unit <effects-effect-unit>` has its own set
of parameters. By default, these are hidden. Instead, there is a single knob
called a "metaknob" for each effect which is linked to the different
parameters. The metaknob allows you to easily control the effects in a unit
without having to manipulate every parameter individually.

If you want more detailed control of effects, press the expansion button on the
effect unit to reveal the effect parameters:

.. figure:: ../_static/effect-unit-expanded.png
   :align: center
   :alt: An effect unit with parameters showing
   :figclass: pretty-figures

   An effect unit with parameters showing

You can customize how the metaknob is linked to the parameters by clicking the
buttons below the parameter knobs. The button under the parameter name
controls the metaknob link mode:

  * Inactive: parameter not linked
  * Active: parameter moves with metaknob
  * Left side active: parameter moves with left half of metaknob turn
  * Right side active: parameter moves with right half of metaknob turn
  * Left and right side active: parameter moves across range with half of
    metaknob turn and back with the other half

The button below the metaknob link button inverts the parameter's relationship
to the metaknob.

For information about specific effects and their parameters, hover your mouse
over them to show the tooltip. If you do not see tooltips, check that you have
them enabled for the skin in :menuselection:`Preferences --> Interface`.

Effects (except for Reverb) that have a length of time as a parameter are
synchronized to the tempo of decks. When these effects are in a unit which is
assigned to a channel that Mixxx does not know the tempo of (any channel other
than a normal deck), the :ref:`master-sync` tempo is used.

Effects In Headphones
=====================
To preview how a track will sound with effects before you mix in the track,
simply assign the deck to an effect unit and enable the headphone button for
the deck. Note that this will increase CPU compared to assigning an effect
unit to a deck without the headphone button enabled. This is because effects
are processed in parallel for the headphone output (prefader) and master output
(postfader).

Effects can also be previewed in headphones on decks that are playing to the
audience, but this requires a few more steps:

  #. Disable the effect unit for the deck
  #. Enable the headphone button for the deck
  #. Enable the headphone button for the effect unit
  #. When you are ready to mix in the effect, turn the mix knob fully left (dry)
  #. Enable the effect unit for the deck
  #. Turn the mix knob right
  #. Disable the headphone button for the effect unit so you do not forget to
     turn it off later
