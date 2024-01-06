.. include:: /shortcuts.rstext

.. _configuration-colors:

Colors
======

.. _configuration-colors-palette:

Selecting Palettes and Default Colors
-------------------------------------

**Track/Hotcue Palette**
  It is possible to assign colors to tracks and :ref:`hotcues <interface-hotcues>`
  to highlight them. Mixxx offers a selection of different palettes that you can
  choose colors from.

  You can also make your own palette by clicking the :guilabel:`Edit` button next
  to the palette name. This will open a the :ref:`palette editor <configuration-colors-editor>`.

**Default Hotcue Color**
  It is possible to either select a single color from the current hotcue palette
  that will be assigned to all newly created hotcue colors, or select the
  :guilabel:`By hotcue number` option. The latter will automatically assign a
  color from the palette to new hotcues based on the hotcue number.

.. _configuration-colors-editor:

Editing Palettes
----------------

The palette editor allows you add, modify, reorder and remove colors in a color
palette and save it under a new name. You can also delete custom palettes.

To modify a color, double-click it to open the color picker window.

When editing the hotcue palette, the palette editor also allows assigning a
specific default color to a hotcue number. This setting is honored when
:guilabel:`Hotcue default color` is set to `By hotcue number`.

That makes it possible to assign just a few distinct colors to your hotcues
automatically, but still have more colors available in the palette in case you
want to override the color manually.

For example, if you have a color palette consisting of 4 colors, and you
configure the palette to assign the first color to hotcue 1 and the third color
to hotcue 2, then hotcue 1 will use the first color and hotcue 2 will be
assigned the third color. The colors will repeat when setting a hotcue with a
number greater than those used in the palette. In the example above, hotcue 3
will use the first color and hotcue 4 the second color, and so on.

You can also assign the same color to more than one hotcue. For example by
separating the hotcue numbers with a comma (“2, 4, 7”), expressing a range
of numbers (“1 - 3”) or any combination of that (“6, 1 - 3, 7”).

If no color in the palette has a hotcue number assigned to it, new hotcues will
use the color at the same index from the palette (i.e. hotcue 1 will be
assigned the first color in the palette, hotcue 2 uses the second color in the
palette, etc.).

.. _configuration-colors-replace:

Replacing Hotcue Colors
-----------------------

Sometimes it's necessary to bulk replace colors of existing hotcues in your library.
Instead of changing the color of every single hotcue manually, you can
:guilabel:`Replace` to open the cue color replace dialog.

In addition to selecting the new color, you may set conditions that determine
which hotcues the new color will be assigned to.
If you tick both checkboxes, the new color will only applied if both conditions match.
