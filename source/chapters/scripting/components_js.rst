.. include:: /shortcuts.rstext

.. _components-js:

Componments.JS
**************

Components.JS is a JavaScript library that makes it easier to code MIDI
controller mappings for Mixxx. It lets you focus more on your controller
and less on the details of MIDI signals and how Mixxx works. It is
centered around JavaScript objects called Components that represent a
physical component of a controller, such as a button, knob, fader, or
encoder. Components provide generic functions that can be made to work
for most use cases just by changing some attributes of the Component,
without having to write many or any custom functions. The library also
provides more specialized Components for common use cases. Components
can be organized into ComponentContainer objects, making it easy to
iterate over them and change their behavior to switch between different
modes.

.. note:: Components JS was added in Mixxx 2.1 and does not work with older
          versions of Mixxx.

To use the library, in the ``<scriptfiles>`` element at the
top of your mapping’s :ref:`XML file <midi-mapping-file-format>`, and load the
the Components library above the link to your controller’s script file:

.. code::

   <file filename="midi-components-0.0.js"/>
   <file functionprefix="MyController" filename="My_Controller_SCRIPT.js"/>

Importing the ``midi-components-0.0.js`` file makes the library accessible by an
object called ``components`` (plural, lower case).

If you are not familiar with object oriented programming in JavaScript,
read Mozilla Developer Network’s `Object-oriented JavaScript
introduction <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS>`__.
If you are familiar with OOP in other languages but new to JavaScript,
you can skip ahead to the `Constructors and object
instances <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS#Constructors_and_object_instances>`__
section of that tutorial.

File structure
==============

To map most controllers, create a custom subtype of `Deck <#deck>`__
and create instances of your custom Deck objects in your controller’s
``init`` function. Use the custom Deck’s constructor function to create
all the Components you need for your particular controller. The example
below is for a typical 2 deck controller. If you are mapping a
controller with a different layout, some changes to this general
structure may be necessary. There is a lot to explain here, so don’t
worry about understanding every detail just yet:

.. code:: javascript

   // Declare the variable for your controller and assign it to an empty object
   // eslint-disable-next-line no-var
   var MyController = {};

   // Mixxx calls this function on startup or when the controller
   // is enabled in the Mixxx Preferences
   MyController.init = function () {
       // create an instance of your custom Deck object for each side of your controller
       MyController.leftDeck = new MyController.Deck([1, 3], 1);
       MyController.rightDeck = new MyController.Deck([2, 4], 2);
   };

   MyController.shutdown = function () {
       // send whatever MIDI messages you need to turn off the lights of your controller
   };

   // implement a constructor for a custom Deck object specific to your controller
   MyController.Deck = function (deckNumbers, midiChannel) {
       // Call the generic Deck constructor to setup the currentDeck and deckNumbers properties,
       // using Function.prototype.call to assign the custom Deck being constructed
       // to 'this' in the context of the generic components.Deck constructor
       // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call
       components.Deck.call(this, deckNumbers);
       this.playButton = new components.PlayButton([0x90 + midiChannel, 0x01]);
       this.cueButton = new components.CueButton([0x90 + midiChannel, 0x02]);
       this.syncButton = new components.SyncButton([0x90 + midiChannel, 0x03]);
       this.pflButton = new components.Button({
           midi: [0x90 + channel, 0x04],
           key: 'pfl',
       });
       this.hotcueButtons = [];
       for (var i = 1; i <= 8; i++) {
           this.hotcueButtons[i] = new components.HotcueButton({
               midi: [0x90 + midiChannel, 0x10 + i],
               number: i,
           });
       }

       this.volume = new components.Pot({
           midi: [0xB0 + midiChannel, 0x01],
           inKey: 'volume',
       });

       this.eqKnob = [];
       for (var k = 1; k <= 3; k++) {
           this.eqKnob[k] = new components.Pot({
               midi: [0xB0 + midiChannel, 0x02 + k],
               group: '[EqualizerRack1_' + this.currentDeck + '_Effect1]',
               inKey: 'parameter' + k,
           });
       }

       // ... define as many other Components as necessary ...

       // Set the group properties of the above Components and connect their output callback functions
       // Without this, the group property for each Component would have to be specified to its
       // constructor.
       this.reconnectComponents(function (c) {
           if (c.group === undefined) {
               // 'this' inside a function passed to reconnectComponents refers to the ComponentContainer
               // so 'this' refers to the custom Deck object being constructed
               c.group = this.currentDeck;
           }
       });
       // when called with JavaScript's 'new' keyword, a constructor function
       // implicitly returns 'this'
   };
   // give your custom Deck all the methods of the generic Deck in the Components library
   MyController.Deck.prototype = new components.Deck();

Component
=========

The basic building block of the library are Component objects that
represent a physical component of a controller, such as a button, knob,
fader, or encoder. The JavaScript object encapsulates all the
information needed to receive MIDI input from that component and send
MIDI signals out to the controller to activate its LED(s).

Components should generally be properties of a
`ComponentContainer <#componentcontainer-and-managing-layers>`__ object.
Most Components should be properties of a custom `Deck <#deck>`__
object as demonstrated in the example in the previous section.

In general, you should not use the basic Component constructor directly;
instead, use one of its subtypes (`Button <#button>`__, `Pot <#pot>`__,
or `Encoder <#encoder>`__). If you do need to use Component directly, do
not confuse it with the ``components`` object (plural, lower case) that
contains all the objects for the library; access Component as
``components.Component`` (plural lower case then singular upper case).

Component Setup
---------------

.. note:: Since Mixxx version 2.5.0 input handlers can be registered in
          javascript, i.e. the xml mapping described in the following paragraph
          is not required anymore.

The input function of each Component needs to be mapped to the incoming
MIDI signals in the XML file. For example:

.. code:: xml

   <control>
       <group>[Channel1]</group>
       <!-- MyController.leftDeck would be an instance of a custom Deck. -->
       <key>MyController.leftDeck.quantizeButton.input</key>
       <status>0x90</status>
       <midino>0x01</midino>
       <options>
           <script-binding/>
       </options>
   </control>

Unless you are using JavaScript mappings, if you decide to rename a Component or
map it to different MIDI input signals, you need to edit the XML file and reload
the mapping in Mixxx’s Preferences. The output does not need to be mapped in
XML. It is handled by the library in JavaScript.

Create Components by calling the constructor with JavaScript’s ``new``
keyword. The Component constructor takes a single object as an argument.
Generally you should provide this as an `object
literal <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Object_literals>`__.
Each property of that object passed to the constructor becomes a
property of the new Component object, making it easy to customize the
functionality of the Component. The constructors for all Component
subtypes work the same way. Most Components need at least these
properties defined:

- ``midi`` (array with 2 numbers): the first two MIDI bytes that the
  controller sends/receives when the physical component changes state.
  Refer to the :ref:`midi-crash-course` if you do not understand what this
  means.
- ``inKey`` (string): the key of the :ref:`Mixxx control <appendix-mixxxcontrols>`
  that this Component manipulates when it receives a MIDI input signal
- ``outKey`` (string): when the :ref:`Mixxx control <appendix-mixxxcontrols>`
  specified by this key changes value, the ``output`` function will be
  called
- ``group`` (string): the group of the :ref:`Mixxx control
  <appendix-mixxxcontrols>` for both inKey and outKey, for example
  ``[Channel1]`` for deck 1

For example:

.. code:: javascript

   var quantizeButton = new components.Button({
       midi: [0x91, 0x01],
       group: '[Channel1]'
       inKey: 'quantize',
       outKey: 'quantize',
   });

If ``inKey`` and ``outKey`` are the same, you can specify ``key`` in the
options object for the constructor to set both the ``inKey`` and
``outKey`` properties of the new Component. For example:

.. code:: javascript

   var quantizeButton = new components.Button({
       midi: [0x91, 0x01],
       group: '[Channel1]',
       key: 'quantize',
   });

Setting the ``key`` property after calling the constructor will not
automatically set ``inKey`` and ``outKey``; you would need to do that
manually if necessary.

Methods
-------

The following methods (in JavaScript, methods are just object properties
that happen to be functions) must be defined for every Component, but in
most cases the defaults (from the inherited prototype Component) will
work so you do not need to define them yourself:

- ``input``: the function that receives MIDI input
- ``output``: the function that gets called when outKey changes
  value. Typically this sends MIDI output to the controller to change the state
  of an LED, but it can do anything.
- ``connect``: register ``output`` as the callback function that gets executed
  when the value of the control object specified by ``group``, ``outKey``
  changes. This is called automatically by the Component constructor if
  ``group`` and ``outKey`` are defined (otherwise it needs to be called after
  construction).  Implement a custom function if you need to connect callbacks
  for multiple Mixxx ControlObjects in one Component. Refer to the source code
  of `SamplerButton.prototype.connect <#samplerbutton>`__ for an example.

The following methods are called by the default Component ``input`` and
``output`` methods, as well as the default ``input`` functions of
`Button <#button>`__, `Pot <#pot>`__, and `Encoder <#encoder>`__. If you
do not need to implement complex custom behavior, you can overwrite
these instead of the default ``input`` and ``output`` methods:

- ``inValueScale``: takes the third byte of the incoming MIDI signal as
  its first argument and returns the value to set ``group``, ``inKey``
  to
- ``outValueScale``: takes the value of ``group``, ``outKey`` as its
  first argument and returns the third byte of the outgoing MIDI signal

Each Component also has these methods that you probably should not
overwrite:

- ``disconnect``: disconnect the ``output`` function from being called
  when ``group``, ``outKey`` changes
- ``trigger``: manually call ``output`` with the same arguments as if
  ``group``, ``outKey`` had changed
- ``send``: send a 3 byte (short) MIDI message out to the controller.
  The first two bytes of the MIDI message are specified by the
  Component’s ``midi`` property. The third MIDI byte is provided as the
  first argument to the ``send`` function.
- ``inGetParameter``: returns the value of ``group``, ``inKey``
  normalized to a 0-1 scale
- ``inSetParameter``: sets the value of ``group``, ``inKey`` to the
  function’s first argument, normalized to a 0-1 scale
- ``inGetValue``: returns the value of ``group``, ``inKey``
- ``inSetValue``: sets the value of ``group``, ``inKey`` to the
  function’s first argument
- ``inToggle``: sets ``group``, ``inKey`` to its inverse (0 if it is >0;
  1 if it is
  0)
- ``outGetParameter``: returns the value of ``group``, ``outKey``
  normalized to a 0-1 scale
- ``outSetParameter``: sets the value of ``group``, ``outKey`` to the
  function’s first argument, normalized to a 0-1 scale
- ``outGetValue``: returns the value of ``group``, ``outKey``
- ``outSetValue``: sets the value of ``group``, ``outKey`` to the
  function’s first argument
- ``outToggle``: sets ``group``, ``outKey`` to its inverse (0 if it is
  >0; 1 if it is
  0)

Optional properties
-------------------

The following properties can be specified in the options object passed
to the Component constructor to customize the Component’s
initialization. Changing their value after creating the Component does
not do anything.

- ``outConnect`` (boolean, default true): whether to call ``connect`` in
  the constructor (assuming ``group`` and ``outKey`` were specified in
  the options object)
- ``outTrigger`` (boolean, default true): whether to call ``trigger`` in
  the constructor (assuming ``group`` and ``outKey`` were specified in
  the options object)

Some controllers send and receive two sets of MIDI signals for most
physical components, one for when the shift button is pressed and one
for when the shift button is not pressed. To avoid defining two
Components for every physical component of your controller, set the
following options as appropriate:

- ``sendShifted`` (boolean, default false): whether to send a second,
  shifted MIDI message for every call to ``send``
- ``shiftChannel`` (boolean, default false): whether the shifted MIDI
  message changes the MIDI channel (second nybble of the first byte of
  the MIDI signal)
- ``shiftControl`` (boolean, default false): whether the shifted MIDI
  message changes the MIDI control number (second byte) of the MIDI
  signal
- ``shiftOffset`` (number, default 0): how much to shift the MIDI
  channel or control number by

To avoid having to define those properties for every Component, you can
change the properties of ``components.Component.prototype`` in your
controller’s ``init`` function. For example:

.. code:: javascript

   components.Component.prototype.shiftOffset = 3;
   components.Component.prototype.shiftChannel = true;
   components.Component.prototype.sendShifted = true;

Syntactic sugar
---------------

Components JS provides convenient shortcuts for common situations.

To avoid typing out the group for the constructor of each Component,
Components that share a group can be part of a ComponentContainer and
the `ComponentContainer’s <#componentcontainer-and-managing-layers>`__
``reconnectComponents`` method can assign the group to all of them.
Refer to the `Deck <#deck>`__ ComponentContainer documentation for an
example.

If a Component only needs its ``midi`` property specified for its
constructor, this can be provided simply as an array without wrapping it
in an object. For example:

.. code:: javascript

   var playButton = new components.PlayButton([0x90 + channel, 0x0A]);

instead of

.. code:: javascript

   var playButton = new components.PlayButton({
       midi: [0x90 + channel, 0x0A]
   });

Button
======

A Button is a subtype of Component for buttons/pads. Subtypes of Button
are provided for many common use cases, documented in the subsections
below, making it easy to map those buttons without having to worry about
particularities of Mixxx’s ControlObjects. To use the Button subtypes,
you only need to specify their ``midi`` and ``group`` properties, except
for HotcueButton and SamplerButton.

A generic Button toggles the state of a binary ``inKey`` and sends
outgoing MIDI messages indicating whether a binary ``outKey`` is on or
off. Button adds the following properties to Component:

- ``type``: determines the behavior of the Button. Can be any of these
  values:

  - ``Button.prototype.types.push`` (default): set inKey to 1 on button
    press and 0 on button release. For example, use this type with the
    beatloop_activate
    `Control <https://manual.mixxx.org/latest/chapters/appendix/mixxx_controls.html>`__
  - ``Button.prototype.types.toggle``: invert value of inKey on button
    press. Use this with Controls whose values indicate the state of a
    switch, for example pfl
  - ``Button.prototype.types.powerWindow``: like toggle, but toggles the
    value of inKey again on button up when long pressed, for example
    with [EffectRack1_EffectUnit2_Effect1], enabled Control.

- ``on`` (number, default 127): number to send as the third byte of
  outgoing MIDI messages when ``group``, ``outKey`` is on (its value is
  > 0)
- ``off`` (number, default 0): number to send as the third byte of
  outgoing MIDI messages when ``group``, ``outKey`` is off (its value is
  0)
- ``isPress`` (function): function that takes the same first 4 arguments
  as a MIDI input function (channel, control, value, status) and returns
  a boolean indicating whether the button was pressed.

For buttons/pads with multicolor LEDs, you can change the color of the
LED by defining the ``on`` and ``off`` properties to be the MIDI value
to send for that state. For example, if the LED turns red when sent a
MIDI value of 127 and blue when sent a value of 126:

.. code:: javascript

   MyController.padColors = {
       red: 127,
       blue: 126
   };
   MyController.quantize = new components.Button({
       midi: [0x91, 0x01],
       group: '[Channel1]',
       key: 'quantize',
       type: components.Button.prototype.types.toggle,
       on: MyController.padColors.red,
       off: MyController.padColors.blue,
   });

The default ``isPress`` function works for controllers that indicate
whether a button is pressed or released by sending a different third
MIDI byte (value). Some controllers distinguish between a button press
and release by changing the first nybble (hexadecimal digit) of the
first byte of the MIDI message, also known as an opcode. These
controllers typically use an opcode of 9 to indicate a button press and
8 to indicate a button release. Both the press and release signals need
to be mapped in the XML file to the Button’s ``input`` method. To make
Button work for such a controller, reimplement the prototype ``isPress``
function:

.. code:: javascript

   components.Button.prototype.isPress = function(channel, control, value, status) {
       return (status & 0xF0) === 0x90;
   }

PlayButton
----------

Default behavior: play/pause

Shift behavior: reverse playback

.. seealso:: The actual behavior of the Play/Pause button depends on the
             selected :ref:`Cue mode <interface-cue-modes>`.

CueButton
---------

Default behavior: depends on the :ref:`cue mode <interface-cue-modes>`
configured by the user in the preferences.


SyncButton
----------

Default behavior: momentary sync without toggling sync lock

Shift behavior: toggle sync lock (master sync)

HotcueButton
------------

Default behavior: set hotcue if it is not set. If it is set, jump to it.
Shift behavior: delete hotcue

The LED indicates whether the hotcue is set.

Pass the number of the hotcue as the ``number`` property of the options
argument for the constructor. For example:

.. code:: javascript

   var hotcues = [];
   for (var i = 1; i <= 8; i++) {
       hotcues[i] = new components.HotcueButton({
           number: i,
           group: '[Channel1]',
           midi: [0x91, 0x26 + i],
       });
   }

Hotcue colors
~~~~~~~~~~~~~

HotcueButton can show hotcue colors on the controller. There are three
ways of implementing this. Which one to choose depends on the
controller.

1. Set color via single byte based on controller internal palette
2. Set color via SysEx based on custom palette.
3. Set color via SysEx based on predefined colors by Mixxx.

Option 1 is the simplest and most common method for most controllers.
You must figure out which MIDI values correspond to which colors and the
correlate it with the predefined hotcue colors (the controller’s manual from the
manufacturer may document this). Creating such HotcueButton could look like
this:

.. code:: javascript

   var hotcueButton = new components.HotcueButton({
       number: 1,
       group: '[Channel1]',
       midi: [0x91, 0x26],
       // key-value map to correlate the Mixxx ColorID
       // with the value the controller expects for
       // specific colors. These values are passed to
       // the HotcueButton's send method.
       colors: {
           0: 0x10,
           1: 0x18,
           2: 0x20,
           ...
       },
       // value to turn off the buttons LED.
       off: 0x00,
   });

With the second option, you can send predefined colors from the palette
to the controller but this time via SysEx. Since SysEx is very
controller specific, it is mandatory to specify a custom ``sendRGB``
method which is responsible for taking a color description, extracting
the relevant information, and sending the SysEx Message to the
controller. In this case, the values of the attributes in the ``colors``
object are passed as the input to the ``sendRGB`` method.

.. code:: javascript

   var hotcueButton = new components.HotcueButton({
       number: 1,
       group: '[Channel1]',
       midi: [0x91, 0x26],
       // key-value map to correlate the Mixxx ColorID
       // with an array which contains (in this case)
       // the RGB components of a color. These values
       // are passed as input to the sendRGB method.
       colors: {
           0: [0x00,0x00,0x00], // black
           1: [0xFF,0x00,0x00], // pure red
           2: [0xFF,0xFF,0x00], // pure Yellow
           ...
       },
       sendRGB: function (color_obj) {
           // example Message (hardcoded bytes are controller specific).
       // colors entries contain 8-bit values, but SysEx only supports 7-bit values
       // so were bitshifting by 1 to reduce the resolution.
           var msg = [0xF0, 0x00, 0x01, color_obj[0]>>1,color_obj[1]>>1,color_obj[2]>>1];
           // send message
       midi.sendSysexMsg(msg, msg.length);
       }
   });

The third option is similar to the second one. You need to define a
``sendRGB`` method again, but in this Mixxx provides the color palette
automatically and you do not provide a ``colors`` object for the
HotcueButton. The ``sendRGB(color)`` method gets passed a color object.
Such a button could be defined like this:

.. code:: javascript

   var hotcueButton = new components.HotcueButton({
       number: 1,
       group: '[Channel1]',
       midi: [0x91, 0x26],
       // colors automatically assigned by Components.JS framework
       sendRGB: function (color_obj) {
           // example Message (hardcoded bytes are controller specific).
       // colors entries contain 8-bit values, but SysEx only supports 7-bit values
       // so were bitshifting by 1 to reduce the resolution.
           var msg = [0xF0, 0x00, 0x01, color_obj.red>>1,color_obj.green>>1,color_obj.blue>>1];
           // send message
       midi.sendSysexMsg(msg, msg.length);
       }
   });

SamplerButton
-------------

Default behavior: Press the button to load the track selected in the
library into an empty sampler. Press a loaded sampler to play it from
its cue point. Press again while playing to jump back to the cue point.
Shift behavior: If the sampler is playing, stop it. If the sampler is
stopped, eject it.

Specify the sampler number as the number property of the object passed
to the constructor. There is no need to manually specify the group. For
example:

.. code:: javascript

   var samplerButtons = [];
   for (var n = 1; n <= 8; n++) {
       samplerButtons[n] = new components.SamplerButton({
           number: n,
           midi: [0x91, 0x02],
       });
   };

You can also make the SamplerButtons velocity sensitive by setting the
``volumeByVelocity: true`` property on the object that gets passed to
the constructor. This will change the volume at which the sample is
being played at depending on how hard you pressed the button. Obviously,
it will only work if your hardware features velocity sensitive buttons.

.. code:: javascript

   var samplerButtons = [];
   for (var n = 1; n <= 8; n++) {
       samplerButtons[n] = new components.SamplerButton({
           number: n,
           midi: [0x91, 0x02],
           volumeByVelocity: true,
       });
   };

When the sampler is loaded, the LED will be sent a MIDI message with the
value of the ``on`` property (default 127) When the sampler is empty,
the LED will be sent a MIDI message with the value of the ``off``
property (default 0). If your controller’s pads have multicolor LEDs,
specify the value to send for a different LED color with the ``playing``
property to set the LED to a different color while the sampler is
playing. For example:

.. code:: javascript

   MyController.padColors = {
   // These values are just examples, consult the MIDI documentation from your controller's
   // manufacturer to find the values for your controller. If that information is not available,
   // guess and check to find the values.
       red: 125,
       blue: 126,
       purple: 127,
       off: 0
   };
   var samplerButton = [];
   var samplerButton[1] = new components.SamplerButton({
       midi: [0x91, 0x02],
       number: 1,
       on: MyController.padColors.blue,
       playing: MyController.padColors.red,
       // off is inherited from Button.prototype
   });

EffectAssignmentButton
----------------------

An EffectAssignmentButton routes a deck through an EffectUnit. It is
separate from the `EffectUnit <#effectunit>`__ ComponentContainer
because it is-meant to be a part of a `Deck <#deck>`__. Using
``Deck.setCurrentDeck`` to switch decks will switch the deck an
EffectAssignmentButton assigns an EffectUnit to.

.. code:: javascript

   var effectAssignmentButtons = [];
   for (var u = 1; u <= 4; u++) {
       effectAssignmentButtons = new components.EffectAssignmentButton({
           midi: [0x92, 0x20 + u],
           effectUnit: u,
           group: '[Channel1]',
       });
   }

Pot
===

A Pot is a Component subtype for potentiometers (faders and knobs) with
finite ranges. Pot’s ``connect`` and ``disconnect`` methods take care of
soft takeover when switching layers with
`ComponentContainer’s <#componentcontainer-and-managing-layers>`__
``reconnectComponents`` or ``applyLayer`` methods. Soft takeover is not
activated until the first input signal is received, so it does not
interfere with setting initial values for controllers that can report
that information.

For example:

.. code:: javascript

   var eqKnobs = [];
   for (var i = 1; i <= 3; i++) {
       eqKnobs[i] = new components.Pot({
           midi: [0xB1, 0x02 + i],
           group: '[EqualizerRack1_[Channel1]_Effect1]',
           inKey: 'parameter' + i,
       });
   }

To use a Pot with a fader or knob that uses 14 bit MIDI (sends two MIDI
messages, one with a least significant byte and one with a most
significant byte) for higher precision, map the incoming signals to the
Pot’s ``inputLSB`` and ``inputMSB`` functions instead of ``input`` in
the XML file. Nothing extra needs to be done in JavaScript.

The Pot components supports ``max`` values up to 16384 (``2^14``). So if
(for some obscure reason) a control only sends 6 bytes of precision, you
can map ``input`` as if the control had 7 bits of precision and then
specify ``max: 64``. The same would work for 10 bits for example, just
map ``inputLSB`` and ``inputMSB`` as if the control sent 14 bits of
precision and then specify ``max: 1024``.

By default the Pot Component will try to deal with soft takeover
for you, but if that interferes with your component or is unnecessary
(for example when the Component never switches layers), you can specify
``softTakeover: false`` to disable it.

Pot Components support an optional relative mode as an alternative to
dealing with soft takeover. To use it, set the ``relative`` property to
``true`` in the options object for the constructor. In this mode, moving
the Pot will adjust the Mixxx Control relative to its current value. For
example:

.. code:: javascript

   var tempoFader = new components.Pot({
       midi: [0xB1, 0x32],
       group: '[Channel1]',
       inKey: 'rate',
       relative: true,
   });

Encoder
=======

Encoder is a Component for infinitely turning encoders. The default
``input`` function assumes the encoder sends MIDI signals on a continuous
scale from 0 to 127 (0x7F). If the encoder sends relative MIDI signals
to indicate whether it turns right or left, you will need to define your
own ``input`` function. For example, for an encoder that sends a value
of 1 when it is turned left and a value of 127 when it is turned right:

.. code:: javascript

   MyController.SomeEncoder = new components.Encoder({
       midi: [0xB1, 0x03],
       group: '[Channel1]',
       inKey: 'pregain',
       input: function (channel, control, value, status, group) {
           if (value === 1) {
               this.inSetParameter(this.inGetParameter() - .05);
           } else if (value === 127) {
               this.inSetParameter(this.inGetParameter() + .05);
           }
       },
   });

To map an Encoder with an LED ring around it that receives MIDI signals
on a continuous 0-127 scale, define an ``outKey`` property in the
options object for the constructor. Similar to ``input``, if the LEDs do
not respond to a continuous 0-127 scale, define your own ``output``
function. If ``outKey`` and ``inKey`` are the same, you can just specify
one ``key`` property for the constructor.

Encoders can often be pushed like a button. Usually, it is best to use a
separate Button Component to handle the MIDI signals from pushing it.

JogWheelBasic
-------------

Since mapping Jogwheels in mixxx can be cumbersome we introduced a new component
called ``JogWheelBasic`` in Mixxx 2.3.4.

.. code:: js

   this.jogWheel = components.JogWheelBasic({
     deck: 1, // whatever deck this jogwheel controls
     wheelResolution: 1000, // how many ticks per revolution the jogwheel has
     alpha: 1/8 // alpha-filter
     beta: 1/8/32 // optional
     rpm: 33 + 1/3 // optional
     group: // optional
   });

The XML should map ``jogWheel.inputWheel`` to the messages containing rotation
information of the wheel and ``jogWheel.inputTouch`` on messages that contain
info on whether the top of the platter was touched. If you need to make some
adjustments how the wheel interprets the incoming rotation information, you can
overwrite ``onValueScale(midiValue)``. If your controller has an option to
enable/disable vinylmode, you can set ``jogWheel.vinylMode`` and the controller
will behave appropriately (touching the jogwheel platter is ignored when
``vinylMode`` is ``false``).

ComponentContainer and Managing Layers
======================================

A ComponentContainer is an object that contains Components as
properties. ComponentContainer has methods to easily iterate through the
Components, which makes it easy to manage different layers of
functionality. The basic ComponentContainer methods are:

- ``forEachComponent``: Iterate over all Components in this
  ComponentContainer and perform an operation on them. The operation is
  a function provided as the first argument to ``forEachComponent``. The
  operation function takes each Component as its first argument. In the
  context of the operation function, ``this`` refers to the
  ComponentContainer. ``forEachComponent`` iterates recursively through
  the Components in any ComponentContainers and arrays that are
  properties of this ComponentContainer. If you do not want
  ``forEachComponent`` to operate recursively, pass ``false`` as the
  second argument to ``forEachComponent``.
- ``reconnectComponents``: Call each Component’s ``disconnect`` method,
  optionally perform an operation on it, then call its ``connect`` and
  ``trigger`` methods to sync the state of the controller’s LEDs.
  Arguments are the same as ``forEachComponent``.
- ``shutdown``: Iterate over all Components and call their shutdown
  methods. The Button is the only component with a predefined shutdown
  method. All other components have to be implemented manually if they
  require anything to be done when Mixxx shuts down.

Typically, ``reconnectComponents`` is used to switch between layers. The
callback passed to reconnectComponents can manipulate each Component’s
properties as appropriate for the new layer. Below is a basic example
for switching between decks 1 and 3. This is a simple example that does
not handle the complexities presented by EQs, QuickEffects, or
EffectAssignmentButtons like `Deck.setCurrentDeck <#deck>`__ does.

.. code:: javascript

   // Define a constructor for a ComponentContainer that adds some Components to it
   var ExampleContainer = function () {
       this.play = new components.PlayButton({
           midi: [0x91, 0x40],
           group: '[Channel1]',
       });
       this.cue = new components.CueButton({
           midi: [0x91, 0x41],
           group: '[Channel1]',
       });
   };
   // This will give any object created with "new exampleContainer()"
   // the ComponentContainer methods.
   exampleContainer.prototype = new components.ComponentContainer();

   var demonstration = new ExampleContainer();
   demonstration.reconnectComponents(function (component) {
       component.group = '[Channel3]';
   )};

In simple cases like the demonstration above, changing a property of
each Component in the callback passed to ``reconnectComponents`` is
sufficient. When more complex manipulation is required, especially if
the manipulation varies between Components, it is a good idea to use the
``reconnectComponents`` callback to call a specific method on each
Component. This keeps all the logic for that Component together instead
of scattering it between the Component construction and the layer
switching function.

Shift layers
------------

The most common use case for changing layers is for shift buttons. If
your controller sends different MIDI signals depending on whether shift
is pressed, map both the shifted and unshifted input signals to the
Component’s ``input`` function in XML. For each Component that has
different behavior depending on whether shift is pressed, implement
``shift`` and ``unshift`` methods that manipulate the Component
appropriately. When the shift button is pressed call
``ComponentContainer.shift()`` and the shift method of each Component in
the ComponentContainer will be executed (if it exists). When the shift
button is released, call ``ComponentContainer.unshift()`` to call each
Component’s ``unshift`` method.

Note that any *Button.prototype.types.push* type `Buttons <#button>`__
in the ComponentContainer will have their inKey reset to 0 if the user
happens to have them pressed when ``ComponentContainer.shift()`` or
``ComponentContainer.unshift()`` is called. This prevents the Button’s
inKey from getting stuck in a pressed (1) state, which can cause
confusing behavior with some controls.

For convenience, the Component constructor will automatically call the
``unshift`` function if it exists. This allows you to avoid redundancy
when constructing Components.

To use separate ``output`` callback functions in shifted and unshifted
modes, the Component’s ``shift`` and ``unshift`` functions need to call
``disconnect``/``connect`` and ``trigger``. ComponentContainer’s
``shift``/``unshift`` methods will not do this automatically like
``reconnectComponents``.

Generally, you should avoid making LEDs change when a shift button is
pressed. This is distracting if the user is pressing shift to use the
shifted functionality of a different part of the controller. If the
alternate layer is confined to a specific part of the controller,
changing LEDs is not an issue.

To handle the interaction of shifted and unshifted states with another
layer, you can create another system of methods for each Component that
changes properties of the Component when a layer is activated, and
within those methods, you can assign the ``shift`` and ``unshift``
properties of the Component to different functions. Refer to the source
code of `EffectUnit <#effectunit>`__ for an example.

Deck
====

Deck is a `ComponentContainer <#componentcontainer-and-managing-layers>`__ with
methods for conveniently changing the ``group`` attributes of contained
Components to switch the deck that a set of Components is manipulating.
The ``setCurrentDeck`` method takes the new deck as a string and sets
the Components’ ``group`` property appropriately, including for
equalizer knobs and QuickEffect (filter) knobs.

The Deck constructor takes one argument, which is an array of deck
numbers to cycle through with the ``toggle`` method. Typically this will
be ``[1, 3]`` or ``[2, 4]``.

Refer to the `File structure <#file-structure>`__ section above for an
example.

EffectUnit
==========

EffectUnit is a
`ComponentContainer <#componentcontainer-and-managing-layers>`__ that
contains Components designed to be mapped to the common arrangement of 4
knobs and 4 buttons for controlling effects. If your controller’s
effects section has fewer components, the EffectUnit object provided by
Components JS probably will not be very helpful. You may want to read
the source code for the library’s EffectUnit to get an idea for how to
map your controller though.

There is no need to use Components for the rest of your mapping if you
just want to use the EffectUnit from the library.

The Components provided are:

- dryWetKnob (`Pot <#pot>`__)
- effectFocusButton (`Button <#button>`__)
- enableButtons[1-3]
  (`ComponentContainer <#componentcontainer-and-managing-layers>`__ of
  `Button <#button>`__\ s)
- knobs[1-3]
  (`ComponentContainer <#componentcontainer-and-managing-layers>`__ of
  `Pot <#pot>`__\ s)

Refer to the `Standard Effects Mapping <Standard-Effects-Mapping>`__
page for a description of how to use the EffectUnit object. On the wiki
page for your controller, link to the `Standard Effects
Mapping <Standard-Effects-Mapping>`__ page instead of rewriting a
description for your controller.

EffectUnit Setup
----------------

To map an EffectUnit for your controller, call the constructor like the
`Deck <#deck>`__ constructor. The only argument to the constructor is
an array of numbers that specifies which EffectUnits pressing the
effectFocusButton with shift toggles between. Then, set the midi
attributes for the showParametersButton, enableButtons[1-3], and
optionally enableOnChannelButtons. After the ``midi`` attributes are set
up, call the EffectUnit’s ``init`` method to set up the output
callbacks. For example:

.. code:: javascript

   MyController.effectUnit = new components.EffectUnit([1, 3]);
   MyController.effectUnit.enableButtons[1].midi = [0x90, 0x01];
   MyController.effectUnit.enableButtons[2].midi = [0x90, 0x02];
   MyController.effectUnit.enableButtons[3].midi = [0x90, 0x03];
   MyController.effectUnit.knobs[1].midi = [0xB0, 0x01];
   MyController.effectUnit.knobs[2].midi = [0xB0, 0x02];
   MyController.effectUnit.knobs[3].midi = [0xB0, 0x03];
   MyController.effectUnit.dryWetKnob.midi = [0xB0, 0x04];
   MyController.effectUnit.effectFocusButton.midi = [0x90, 0x04];
   MyController.effectUnit.init();

Controllers designed for Serato and Rekordbox often have an encoder
instead of a dry/wet knob (labeled “Beats” for Serato or “Release FX”
for Rekordbox) and a button labeled “Tap”. Map the ``effectFocusButton``
to the controller’s “Tap” button. To use the ``dryWetKnob`` Pot with an
encoder, replace its ``input`` function with a function that can
appropriately handle the signals sent by your controller. For example:

.. code:: javascript

   MyController.effectUnit = new components.EffectUnit([1, 3]);
   MyController.effectUnit.enableButtons[1].midi = [0x90, 0x01];
   MyController.effectUnit.enableButtons[2].midi = [0x90, 0x02];
   MyController.effectUnit.enableButtons[3].midi = [0x90, 0x03];
   MyController.effectUnit.knobs[1].midi = [0xB0, 0x01];
   MyController.effectUnit.knobs[2].midi = [0xB0, 0x02];
   MyController.effectUnit.knobs[3].midi = [0xB0, 0x03];
   MyController.effectUnit.dryWetKnob.midi = [0xB0, 0x04];
   MyController.effectUnit.dryWetKnob.input = function (channel, control, value, status, group) {
       if (value === 1) {
          // 0.05 is an example. Adjust that value to whatever works well for your controller.
          this.inSetParameter(this.inGetParameter() - .05);
       } else if (value === 127) {
          this.inSetParameter(this.inGetParameter() + .05);
       }
   };
   MyController.effectUnit.effectFocusButton.midi = [0x90, 0x04];
   MyController.effectUnit.init();

For the shift functionality to work, the shift button of your controller
must be mapped to a function that calls the ``shift``/``unshift``
methods of the EffectUnit on button press/release. Also, if your
controller sends different MIDI signals when shift is pressed, map those
as well as the unshifted signals to the ``input`` method of each
Component in your XML file. If the EffectUnit is a property of another
`ComponentContainer <#componentcontainer-and-managing-layers>`__ (for
example a `Deck <#deck>`__), calling ``shift`` and ``unshift`` on the
parent ComponentContainer will recursively call it on the EffectUnit too
(just like it will for any other ComponentContainer).

By default an effect can only be focused when the respective GUI unit is
expanded: when the focus button of a collapsed unit is pressed, the GUI
counterpart is expanded. Accordingly, units release the effect focus and
switch back to Meta knob mapping as soon as an unit is collapsed.
However, there are situations when the on-screen parameters of a focused
effect can safely stay hidden while the controller is mapped to the
parameter knobs. Collapsed units show a focus indicator then. To enable
this mode instantiate effect units with ‘true’ added after the effect
unit numbers array. For example:

.. code:: javascript

   MyController.effectUnit = new components.EffectUnit([1, 3],true);
   //...

Assignment switches
-------------------

Generally, most controllers should use
`EffectAssignmentButton <#effectassignmentbutton>`__\ s in
`Deck <#deck>`__\ s to enable effect units on decks. If you have a
dedicated effects controller that does not manipulate decks, the
enableOnChannelButtons provided by EffectUnit would be more appropriate.
You can easily create these by calling
``enableOnChannelButtons.addButton('CHANNEL_NAME')`` (do not put
brackets around the CHANNEL_NAME) on the EffectUnit object, then define
their ``midi`` properties.
