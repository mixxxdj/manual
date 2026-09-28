.. include:: /shortcuts.rstext

.. _midi-mapping-file-format:

MIDI Mapping File Format
************************

.. seealso:: :ref:`advanced-controller-wizard` for information about making simple mappings with no scripting.

Support for additional MIDI devices can be added to Mixxx by creating a
new "MIDI preset" file. This file tells Mixxx how to translate, or map,
MIDI messages from a controller into commands that Mixxx understands.

XML Crash Course
----------------

Mixxx uses a well defined XML format to store its MIDI mappings. It is
easy to learn the basics of XML so you can edit Mixxx mappings. If you
know HTML, the language that is used to define web pages, that will help
because XML is very similar.

XML is a language for describing data. It does not do anything by itself
and it has no predefined uses. Many other programs have their own ways
of using XML that convey different information. For example, Traktor TSI
controller mapping files are XML files, but Traktor's mapping system is
completely different from Mixxx's mapping systems, so TSI files make no
sense to Mixxx.

XML files are hierarchies of elements. Elements have starting and
closing tags surrounded by angle brackets (also known as less than (\<)
and greater than (\>) signs). The starting tags can be as simple as
naming the element surrounded by angle brackets, for example, ``<group>``.
Starting tags can also have attributes to specify more detail about the
element, for example, in ``<controller name="Stanton SCS.3d">``, `name` is
an attribute of the `controller` element with a value of `Stanton
SCS.3d`. Ending tags have a slash after the `<`, for example,
``</group>``. Between the starting and ending tags, elements can contain
data or other elements. Empty elements are also allowed, which have a
slash before the `>`, for example, ``<SelectKnob/>``.

Header
------

Each XML mapping file starts with a header with metadata: ::

    <?xml version="1.0" encoding="utf-8"?>
        <!-- Schema version number to help compatibility, should the MIDI format change -->
        <MixxxControllerPreset mixxxVersion="2.0" schemaVersion="1">
        <info>
            <name>Example MIDI Preset for Mixxx</name>
            <author>Tom Care</author>
            <description>
              This is an example XML MIDI preset for Mixxx. The scope of the
              preset could be from a small functionality addition, to a complete
              mapping for a controller, to a complex personal setup with
              multiple controllers. This description is intended for
              distribution and could include comments about the extent of the
              functionality.
            </description>
            <wiki>Encoded URL to Mixxx wiki page documenting this controller mapping</wiki>
            <forums>Encoded URL to Mixxx discussion forums page for this controller mapping</forums>
        </info>
        <!--
          Many controllers are supported in a single file.
          A controller id should only be used once.
        -->
        <controller id="controller name">

The schemaVersion and mixxxVersion attributes of the ``MixxxControllerPreset``
element are important for future compatibility as the Mixxx MIDI mapping
format changes. The child elements of the ``<info>`` element are used to
display information about the mapping in the Mixxx controller
preferences. Note that ``&`` is a reserved character in XML, so the URL to
the forum thread must use ``&amp;`` instead of just ``&``. (When a preset does
not have a name in its ``<info>`` section, Mixxx 1.11+ use the filename
without the extension).

Write the brand and model of the controller (for example, "Stanton
SCS.3d") in the id attribute of the ``<controller>`` element. The
``<controller>`` element is a container for a ``<controls>`` element and an
``<outputs>`` element, which are described below.

Inputs
------

The ``<controls>`` element tells Mixxx what to do with signals it receives
from your controller such as knob turns and button presses. Within the
``<controls>`` (plural) element, put as many ``<control>`` (singular) elements
as necessary. ::

        <controls> <!-- One control group -->
            <control> <!-- Several controls -->
                <group>[Master]</group>
                <key>crossfader</key>
                <status>0xB0</status> <!-- CC on channel 1 -->
                <midino>0x07</midino>
                <options>
                    <!--
                      all control specific options should go here - sensitivity
                      etc. Specifics to be decided by spec
                    -->
                </options>
            </control>
        </controls>

The ``<group>`` and ``<key>`` elements define the value in Mixxx that this
MIDI signal controls. The :ref:`appendix-mixxxcontrols` page lists the
available values for these group and key elements.

The ``<status>`` and ``<midino>`` elements define the MIDI signal that Mixxx
will listen for.

.. seealso:: :ref:`midi-crash-course` for a brief introduction to MIDI signals.


Pitch controls
==============

Some controllers send messages with a status byte of ``0xEn`` which, per
the MIDI standard (see the :ref:`midi-crash-course`) are followed by two value
bytes in little-endian format.
These are usually used for pitch sliders or pitch wheels.
To map these controls, do the same as above but omit the ``<midino>`` element.

Input options
=============

These are all specified with empty XML elements as children of the
``<options>`` element.
For example, to use the SelectKnob option, in the XML, write: ::

    <options>
        <SelectKnob/>
    </options>

- **Normal**: No modifications, MIDI\_NOTE\_OFF or value == 0 is used
  as "released" and all other values as "pressed"
- **Script-Binding**: Bind to a MIDI script function given in the
  "key" tag. (See :ref:`midi-scripting` for details.)
- **SelectKnob**: For relative controls centered on 64 (0x40)
- **Diff**: Adds the current value of a relative control to the
  previous value
- **Invert**: Subtracts the value from 127, giving an inverted control
  (-127..0)
- **Rot64**: For encoders sending 63 (0x3F) or 65 (0x41),
  increment/decrement of 1/16 the value
- **Rot64inv**: For encoders sending 63 (0x3F) or 65 (0x41),
  increment/decrement of 1/16 the value but with inverted controls
- **Rot64fast**: For encoders sending 63 (0x3F) or 65 (0x41),
  increment/decrement the value with a multiplier of 1.5
- Button (deprecated): Ignore opcode, use value \> 0 as "pressed"
- **Switch**: Ignore opcode and value, all messages are used as
  "pressed"
- **Spread64**: Exponential spread either side of 64, aka "relative"
  controller
- **Soft-takeover**: prevents the physical control from affecting
  Mixxx until it's close to the on-screen control's position.
- **fourteen-bit-lsb**/**fourteen-bit-msb** *New in 1.12*
  14-bit (high resolution)
  MIDI least/most significant byte. Some controls, most often pitch
  faders, send two MIDI messages so their values can be combined to
  form 127 :sup:`2` (16,384) possible values rather than 127 for
  more precise control. Use two controls to catch both messages: ::

    <control>
        <group>[Channel1]</group>
        <key>rate</key>
        <status>0xB0</status>
        <midino>0x29</midino>
        <options>
            <fourteen-bit-lsb/>
        </options>
    </control>
    <control>
        <group>[Channel1]</group>
        <key>rate</key>
        <status>0xB0</status>
        <midino>0x09</midino>
        <options>
            <fourteen-bit-msb/>
        </options>
    </control>

Outputs
-------

The ``<outputs>`` element defines outputs that use "short" (3-byte) MIDI
messages.
Use this to control LEDs and other features of your controller to make them
react to changes in Mixxx.
Within the ``<outputs>`` (plural) element, put as many ``<output>`` (singular)
elements as necessary.
Note that this can only send either of two different values, so it is most
useful for LEDs that can only be switched on and off.
For other parts of controllers that are controlled with more than two values
such as multicolored LEDs or VU meters, you need to use :ref:`midi-scripting`.
Scripting is also necessary for sysex messages. ::

    <outputs>
        <output>
            <group>[Channel1]</group>
            <key>play</key>
            <status>0x7F</status>    <!-- First byte sent to device -->
            <midino>0x08</midino>    <!-- Second byte -->
            <on>0x01</on>            <!-- Third byte. If not specified, 0x7F is used. -->
            <off>0x00</off>          <!-- Alternate third byte. 0x00 is the default.
                                          If set to 0xFF, nothing is sent. -->
            <minimum>0.9</minimum>   <!-- Required: Lower value for the Mixxx control,
                                          below which the 'off' value is sent -->
            <maximum>0.99</maximum>  <!-- Optional: upper value for the Mixxx control,
                                          above which the 'off' value is sent.
                                          1.0 is the default. -->
        </output>
    </outputs>

This allows you to send any three bytes to the MIDI controller in the order
``<status>``, ``<midino>``, ``<on>``/``<off>``.
The ``<minimum>`` and ``<maximum>`` elements define the range of the
:ref:`appendix-mixxxcontrols`'s values within which the ``<on>`` MIDI value is
sent.
Outside this range, the ``<off>`` MIDI value is sent.
If ``<off>`` is set to ``0xFF``, no message will be sent outside the range (this
is useful for LED sequences).

Closing
-------

Don't forget to close the elements that were opened at the top of the
file. ::

        </controller>
    </MixxxControllerPreset>
