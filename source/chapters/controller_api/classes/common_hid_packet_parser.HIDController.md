[Documentation](../README.md) / [Modules](../modules.md) / [common-hid-packet-parser](../modules/common_hid_packet_parser.md) / HIDController

# Class: HIDController

[common-hid-packet-parser](../modules/common_hid_packet_parser.md).HIDController

HID Controller Class with packet parser

## Table of contents

### Constructors

- [constructor](common_hid_packet_parser.HIDController.md#constructor)

### Properties

- [InputPackets](common_hid_packet_parser.HIDController.md#inputpackets)
- [LEDColors](common_hid_packet_parser.HIDController.md#ledcolors)
- [OutputFieldLookup](common_hid_packet_parser.HIDController.md#outputfieldlookup)
- [OutputPackets](common_hid_packet_parser.HIDController.md#outputpackets)
- [OutputUpdateInterval](common_hid_packet_parser.HIDController.md#outputupdateinterval)
- [activeDeck](common_hid_packet_parser.HIDController.md#activedeck)
- [auto\_repeat\_interval](common_hid_packet_parser.HIDController.md#auto_repeat_interval)
- [buttonStates](common_hid_packet_parser.HIDController.md#buttonstates)
- [connectDeck](common_hid_packet_parser.HIDController.md#connectdeck)
- [deckOutputColors](common_hid_packet_parser.HIDController.md#deckoutputcolors)
- [deckSwitchMap](common_hid_packet_parser.HIDController.md#deckswitchmap)
- [defaultPacket](common_hid_packet_parser.HIDController.md#defaultpacket)
- [disconnectDeck](common_hid_packet_parser.HIDController.md#disconnectdeck)
- [enableScratchCallback](common_hid_packet_parser.HIDController.md#enablescratchcallback)
- [initialized](common_hid_packet_parser.HIDController.md#initialized)
- [isScratchEnabled](common_hid_packet_parser.HIDController.md#isscratchenabled)
- [modifiers](common_hid_packet_parser.HIDController.md#modifiers)
- [postProcessDelta](common_hid_packet_parser.HIDController.md#postprocessdelta)
- [processDelta](common_hid_packet_parser.HIDController.md#processdelta)
- [scalers](common_hid_packet_parser.HIDController.md#scalers)
- [scratchAlpha](common_hid_packet_parser.HIDController.md#scratchalpha)
- [scratchBeta](common_hid_packet_parser.HIDController.md#scratchbeta)
- [scratchRPM](common_hid_packet_parser.HIDController.md#scratchrpm)
- [scratchRampOnDisable](common_hid_packet_parser.HIDController.md#scratchrampondisable)
- [scratchRampOnEnable](common_hid_packet_parser.HIDController.md#scratchramponenable)
- [scratchintervalsPerRev](common_hid_packet_parser.HIDController.md#scratchintervalsperrev)
- [timers](common_hid_packet_parser.HIDController.md#timers)
- [toggleButtons](common_hid_packet_parser.HIDController.md#togglebuttons)
- [valid\_groups](common_hid_packet_parser.HIDController.md#valid_groups)
- [virtualDecks](common_hid_packet_parser.HIDController.md#virtualdecks)

### Methods

- [autorepeatTimer](common_hid_packet_parser.HIDController.md#autorepeattimer)
- [close](common_hid_packet_parser.HIDController.md#close)
- [enableScratch](common_hid_packet_parser.HIDController.md#enablescratch)
- [getActiveFieldControl](common_hid_packet_parser.HIDController.md#getactivefieldcontrol)
- [getActiveFieldGroup](common_hid_packet_parser.HIDController.md#getactivefieldgroup)
- [getInputPacket](common_hid_packet_parser.HIDController.md#getinputpacket)
- [getOutputField](common_hid_packet_parser.HIDController.md#getoutputfield)
- [getOutputPacket](common_hid_packet_parser.HIDController.md#getoutputpacket)
- [getScaler](common_hid_packet_parser.HIDController.md#getscaler)
- [jog\_wheel](common_hid_packet_parser.HIDController.md#jog_wheel)
- [linkControl](common_hid_packet_parser.HIDController.md#linkcontrol)
- [linkModifier](common_hid_packet_parser.HIDController.md#linkmodifier)
- [linkOutput](common_hid_packet_parser.HIDController.md#linkoutput)
- [parsePacket](common_hid_packet_parser.HIDController.md#parsepacket)
- [processButton](common_hid_packet_parser.HIDController.md#processbutton)
- [processControl](common_hid_packet_parser.HIDController.md#processcontrol)
- [processIncomingPacket](common_hid_packet_parser.HIDController.md#processincomingpacket)
- [registerInputPacket](common_hid_packet_parser.HIDController.md#registerinputpacket)
- [registerOutputPacket](common_hid_packet_parser.HIDController.md#registeroutputpacket)
- [resolveDeck](common_hid_packet_parser.HIDController.md#resolvedeck)
- [resolveDeckGroup](common_hid_packet_parser.HIDController.md#resolvedeckgroup)
- [resolveGroup](common_hid_packet_parser.HIDController.md#resolvegroup)
- [setAutoRepeat](common_hid_packet_parser.HIDController.md#setautorepeat)
- [setCallback](common_hid_packet_parser.HIDController.md#setcallback)
- [setOutput](common_hid_packet_parser.HIDController.md#setoutput)
- [setOutputToggle](common_hid_packet_parser.HIDController.md#setoutputtoggle)
- [setPacketCallback](common_hid_packet_parser.HIDController.md#setpacketcallback)
- [setScaler](common_hid_packet_parser.HIDController.md#setscaler)
- [stopAutoRepeatTimer](common_hid_packet_parser.HIDController.md#stopautorepeattimer)
- [switchDeck](common_hid_packet_parser.HIDController.md#switchdeck)
- [toggle](common_hid_packet_parser.HIDController.md#toggle)
- [togglePlay](common_hid_packet_parser.HIDController.md#toggleplay)
- [unlinkControl](common_hid_packet_parser.HIDController.md#unlinkcontrol)
- [unlinkModifier](common_hid_packet_parser.HIDController.md#unlinkmodifier)
- [unlinkOutput](common_hid_packet_parser.HIDController.md#unlinkoutput)
- [fastForIn](common_hid_packet_parser.HIDController.md#fastforin)

## Constructors

### constructor

• **new HIDController**()

#### Defined in

[common-hid-packet-parser.js:1134](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1134)

## Properties

### InputPackets

• **InputPackets**: `Object`

HIDPackets representing HID InputReports, by packet name

#### Defined in

[common-hid-packet-parser.js:1154](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1154)

___

### LEDColors

• **LEDColors**: `Object`

List of named output colors to send
- must contain 'off' value

#### Type declaration

| Name | Type |
| :------ | :------ |
| `off` | `number` |
| `on` | `number` |

#### Defined in

[common-hid-packet-parser.js:1258](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1258)

___

### OutputFieldLookup

• **OutputFieldLookup**: `Map`<`string`, [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md) \| [`packetField`](../interfaces/common_hid_packet_parser.packetField.md)\>

A map to determine the output Bit or bytewise field by group and name,
across all OutputPackets

#### Defined in

[common-hid-packet-parser.js:1169](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1169)

___

### OutputPackets

• **OutputPackets**: `Object`

HIDPackets representing HID OutputReports, by packet name

#### Defined in

[common-hid-packet-parser.js:1161](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1161)

___

### OutputUpdateInterval

• **OutputUpdateInterval**: `number`

Set to value in ms to update Outputs periodically
- By default undefined.
- If set, it's a value for timer executed every n ms to update Outputs with updateOutputs()

**`Deprecated`**

This is unused and updateOutputs() doesn't exist - Remove?

#### Defined in

[common-hid-packet-parser.js:1335](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1335)

___

### activeDeck

• **activeDeck**: `number`

#### Defined in

[common-hid-packet-parser.js:1147](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1147)

[common-hid-packet-parser.js:2246](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2246)

___

### auto\_repeat\_interval

• **auto\_repeat\_interval**: `number`

Auto repeat interval default for fields, where not specified individual (in milliseconds)

**`Default`**

100

#### Defined in

[common-hid-packet-parser.js:1366](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1366)

___

### buttonStates

• **buttonStates**: `Object`

List of valid state values for buttons, should contain fields:
- 'released' (default 0)
- 'pressed' (default 1)

#### Type declaration

| Name | Type |
| :------ | :------ |
| `pressed` | `number` |
| `released` | `number` |

#### Defined in

[common-hid-packet-parser.js:1252](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1252)

___

### connectDeck

• **connectDeck**: `any`

#### Defined in

[common-hid-packet-parser.js:1181](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1181)

___

### deckOutputColors

• **deckOutputColors**: `Object`

List of colors to use for each deck
- Default is 'on' for first four decks.

Override to set specific colors for multicolor button output per deck:
- Values are like {1: 'red', 2: 'green' } and must reference valid OutputColors fields.

#### Type declaration

| Name | Type |
| :------ | :------ |
| `1` | `string` |
| `2` | `string` |
| `3` | `string` |
| `4` | `string` |

#### Defined in

[common-hid-packet-parser.js:1278](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1278)

___

### deckSwitchMap

• **deckSwitchMap**: `Object`

Mapping of automatic deck switching with switchDeck function

#### Type declaration

| Name | Type |
| :------ | :------ |
| `1` | `number` |
| `2` | `number` |
| `3` | `number` |
| `4` | `number` |
| `undefined` | `number` |

#### Defined in

[common-hid-packet-parser.js:1291](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1291)

___

### defaultPacket

• **defaultPacket**: `string`

Default input packet name: can be modified for controllers
which can swap modes (wiimote for example)

#### Defined in

[common-hid-packet-parser.js:1177](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1177)

___

### disconnectDeck

• **disconnectDeck**: `any`

#### Defined in

[common-hid-packet-parser.js:1180](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1180)

___

### enableScratchCallback

• **enableScratchCallback**: [`scratchingCallback`](../modules/common_hid_packet_parser.md#scratchingcallback)

Callback function to call when, jog wheel scratching got enabled or disabled

#### Defined in

[common-hid-packet-parser.js:1245](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1245)

___

### initialized

• **initialized**: `boolean`

- By default 'false'
- Should be set 'true', when controller is found and everything is OK

#### Defined in

[common-hid-packet-parser.js:1142](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1142)

___

### isScratchEnabled

• **isScratchEnabled**: `boolean`

Set to true, when button 'jog_touch' is active

#### Defined in

[common-hid-packet-parser.js:1190](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1190)

[common-hid-packet-parser.js:2027](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2027)

[common-hid-packet-parser.js:2039](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2039)

___

### modifiers

• **modifiers**: [`HIDModifierList`](common_hid_packet_parser.HIDModifierList.md)

Reference to HIDModifierList object

#### Defined in

[common-hid-packet-parser.js:1342](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1342)

___

### postProcessDelta

• **postProcessDelta**: [`packetCallback`](../modules/common_hid_packet_parser.md#packetcallback)

Callback that is executed after parsing incoming packet
(see Traktor-Kontrol-F1-scripts.js for an example)

#### Defined in

[common-hid-packet-parser.js:1381](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1381)

___

### processDelta

• **processDelta**: [`packetCallback`](../modules/common_hid_packet_parser.md#packetcallback)

**`Deprecated`**

Use [postProcessDelta](common_hid_packet_parser.HIDController.md#postprocessdelta) instead
(not used in any official mapping)

#### Defined in

[common-hid-packet-parser.js:1373](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1373)

___

### scalers

• **scalers**: `Object`

Object of scaling function callbacks by name

#### Defined in

[common-hid-packet-parser.js:1349](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1349)

___

### scratchAlpha

• **scratchAlpha**: `number`

The alpha coefficient of the filter
- Default is 1/8 (0.125) - start tune from there

#### Defined in

[common-hid-packet-parser.js:1214](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1214)

___

### scratchBeta

• **scratchBeta**: `number`

The beta coefficient of the filter
- Default is scratchAlpha/32 - start tune from there

#### Defined in

[common-hid-packet-parser.js:1222](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1222)

___

### scratchRPM

• **scratchRPM**: `number`

The speed of the imaginary record at 0% pitch - in revolutions per minute (RPM)
- Default 33+1/3 - adjust for comfort

#### Defined in

[common-hid-packet-parser.js:1206](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1206)

___

### scratchRampOnDisable

• **scratchRampOnDisable**: `boolean`

- Set 'true' to ramp the deck speed up.
- Set 'false' to jump to normal play speed instantly (default)

#### Defined in

[common-hid-packet-parser.js:1238](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1238)

___

### scratchRampOnEnable

• **scratchRampOnEnable**: `boolean`

- Set 'true' to ramp the deck speed down.
- Set 'false' to stop instantly (default)

#### Defined in

[common-hid-packet-parser.js:1230](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1230)

___

### scratchintervalsPerRev

• **scratchintervalsPerRev**: `number`

The resolution of the jogwheel HID control (in intervals per revolution)
- Default is 128

#### Defined in

[common-hid-packet-parser.js:1198](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1198)

___

### timers

• **timers**: `Object`

Object of engine timer IDs of running auto repeat timers
Key is a user specified timer_id.
Used only in the controller.startAutoRepeatTimer code stubs of Sony-SixxAxis.js and Nintendo-Wiimote.js.

#### Defined in

[common-hid-packet-parser.js:1358](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1358)

___

### toggleButtons

• **toggleButtons**: `string`[]

List of button names you wish to act as 'toggle'

i.e. pressing the button and releasing toggles state of the control and doesn't set it off again when released.

#### Defined in

[common-hid-packet-parser.js:1265](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1265)

___

### valid\_groups

• **valid\_groups**: `string`[]

Standard target groups available in mixxx.

This is used by HID packet parser to recognize group parameters we should try sending to mixxx.

#### Defined in

[common-hid-packet-parser.js:1300](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1300)

___

### virtualDecks

• **virtualDecks**: `string`[]

Used to map the virtual deck names 'deck', 'deck1' or 'deck2' to actual [ChannelX]

#### Defined in

[common-hid-packet-parser.js:1286](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1286)

## Methods

### autorepeatTimer

▸ **autorepeatTimer**(): `void`

Callback for auto repeat timer to send again the values for
buttons and controls marked as 'auto_repeat'
Timer must be defined from actual controller side, because of
callback call namespaces and 'this' reference

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2147](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2147)

___

### close

▸ **close**(): `void`

Function to close the controller object cleanly

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1385](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1385)

___

### enableScratch

▸ **enableScratch**(`group`, `status`): `void`

Processing of the 'jog_touch' special button name, which is used to detect
when scratching should be enabled.
Deck is resolved from group with 'resolveDeck'

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `status` | `boolean` | Enable or Disable scratching: - true enables scratching (press 'jog_touch' button) Sets the internal 'isScratchEnabled' attribute to true, and calls scratchEnable with the scratch attributes (see class definition) - false disables scratching (release 'jog_touch' button) Sets the internal 'isScratchEnabled attribute to false, and calls scratchDisable to end scratching mode |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2024](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2024)

___

### getActiveFieldControl

▸ **getActiveFieldControl**(`field`): `string`

Get active control name from field

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `field` | [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md) \| [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) | Object that describes a field inside of a packet, which can often mapped to a Mixxx control. |

#### Returns

`string`

Name of field

#### Defined in

[common-hid-packet-parser.js:1843](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1843)

___

### getActiveFieldGroup

▸ **getActiveFieldGroup**(`field`): `string`

Get active group for this field

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `field` | [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md) \| [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) | Object that describes a field inside of a packet, which can often mapped to a Mixxx control. |

#### Returns

`string`

Group

#### Defined in

[common-hid-packet-parser.js:1820](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1820)

___

### getInputPacket

▸ **getInputPacket**(`name`): [`HIDPacket`](common_hid_packet_parser.HIDPacket.md)

Find input packet matching given name.
Returns undefined if input packet name is not registered.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | Name of packet (it makes sense to refer the HID report type and HID Report-ID here e.g. 'InputReport_0x02') |

#### Returns

[`HIDPacket`](common_hid_packet_parser.HIDPacket.md)

The input packet

#### Defined in

[common-hid-packet-parser.js:1475](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1475)

___

### getOutputField

▸ **getOutputField**(`m_group`, `m_name`): [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md) \| [`packetField`](../interfaces/common_hid_packet_parser.packetField.md)

Find Output control matching give group and name

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `m_group` | `string` | Mapped group, must be a valid Mixxx control group name e.g. "[Channel1]" |
| `m_name` | `string` | Name of mapped control, must be a valid Mixxx control name "VuMeter" |

#### Returns

[`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md) \| [`packetField`](../interfaces/common_hid_packet_parser.packetField.md)

Bit or bytewise field - Returns undefined if output field
    can't be found.

#### Defined in

[common-hid-packet-parser.js:1464](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1464)

___

### getOutputPacket

▸ **getOutputPacket**(`name`): [`HIDPacket`](common_hid_packet_parser.HIDPacket.md)

Find output packet matching given name
Returns undefined if output packet name is not registered.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | Name of packet (it makes sense to refer the HID report type and HID Report-ID here e.g. 'OutputReport_0x81') |

#### Returns

[`HIDPacket`](common_hid_packet_parser.HIDPacket.md)

The output packet

#### Defined in

[common-hid-packet-parser.js:1489](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1489)

___

### getScaler

▸ **getScaler**(`name`, `_callback?`): [`scalingCallback`](../modules/common_hid_packet_parser.md#scalingcallback)

Lookup scaling function for control

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `name` | `string` | `undefined` | Reference of the scaling function in scalers list of HIDController |
| `_callback` | `any` | `undefined` | Unused |

#### Returns

[`scalingCallback`](../modules/common_hid_packet_parser.md#scalingcallback)

Scaling function. Returns undefined if function is not
    registered.

#### Defined in

[common-hid-packet-parser.js:1544](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1544)

___

### jog\_wheel

▸ **jog_wheel**(`field`): `void`

Default jog scratching function. Used to handle jog move events from special
input control field called 'jog_wheel'. Handles both 'scratch' and 'jog' mixxx
functions, depending on isScratchEnabled value above (see enableScratch())

Since most controllers require value scaling for jog and scratch functions,
you are warned if following scaling function names are not registered:

jog
     Scaling function from 'jog_wheel' for rate bend events with mixxx 'jog'
     function. Should return value range suitable for 'jog', whatever you
     wish it to do.
jog_scratch
     Scaling function from 'jog_wheel' for scratch movements with mixxx
     'scratchTick' function. Should return -1,0,1 or small ranges of integers
     both negative and positive values.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `field` | [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) | Object that describes a field inside of a packet, which can often mapped to a Mixxx control. |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2066](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2066)

___

### linkControl

▸ **linkControl**(`group`, `name`, `m_group`, `m_name`, `callback`): `void`

Link a previously declared HID control to actual mixxx control

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name |
| `name` | `string` | Control name |
| `m_group` | `string` | Mapped group, must be a valid Mixxx control group name e.g. "[Channel1]" |
| `m_name` | `string` | Name of mapped control, must be a valid Mixxx control name "pregain" |
| `callback` | [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback) | Callback function for the control |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1593](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1593)

___

### linkModifier

▸ **linkModifier**(`group`, `name`, `modifier`): `void`

Change type of a previously defined field to modifier and register it

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name |
| `modifier` | `string` | Name of the modifier e.g. 'shiftbutton' |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1557](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1557)

___

### linkOutput

▸ **linkOutput**(`group`, `name`, `m_group`, `m_name`, `callback`): `void`

Link a virtual HID Output to mixxx control

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name |
| `name` | `string` | Control name |
| `m_group` | `string` | Mapped group, must be a valid Mixxx control group name e.g. "[Channel1]" |
| `m_name` | `string` | Name of mapped control, must be a valid Mixxx control name "VuMeter" |
| `callback` | [`controlCallback`](../modules/common_hid_packet_parser.md#controlcallback) | Callback function for the control |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2260](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2260)

___

### parsePacket

▸ **parsePacket**(`data`, `length`): `void`

Parse a packet representing an HID InputReport, and processes each field with "unpack":
 - Calls packet callback and returns, if packet callback was defined
 - Calls processIncomingPacket and processes automated events there.
 - If defined, calls postProcessDelta for results after processing automated fields

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `data` | `Uint8Array` | The data received from an HID InputReport. In case of HID devices, which use ReportIDs to enumerate the reports, the ReportID is stored in the first byte and the data start at the second byte |
| `length` | `number` | Length of the data array in bytes |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1713](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1713)

___

### processButton

▸ **processButton**(`field`): `void`

Process given button field, triggering events

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `field` | [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md) | Object that describes a field inside of a packet, which can often mapped to a Mixxx control. |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1856](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1856)

___

### processControl

▸ **processControl**(`field`): `void`

Process given control field, triggering events

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `field` | [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) | Object that describes a field inside of a packet, which can often mapped to a Mixxx control. |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1927](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1927)

___

### processIncomingPacket

▸ **processIncomingPacket**(`packet`, `delta`): `void`

Process the modified field values (delta) from input packet fields for
input control packet, if packet name is in this.defaultPacket.

Button (Boolean value) field processing:
- Sets modifiers from buttons
- Calls button callbacks, if defined
- Finally tries to run matching engine.setValue() function for buttons
  in default mixxx groups, honoring toggleButtons and other button
  details. Not done if a callback was defined for button.

Control (Numeric value) field processing
- Calls scaling functions for control fields, if defined for field.
  Scaling function for encoders (isEncoder attribute is true) scales
  field delta instead of raw value.
- Calls callback functions for control fields, if defined for field
- Finally tries run matching engine.setValue() function for control
  fields in default mixxx groups. Not done if a callback was defined.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `packet` | `any` | Unused |
| `delta` | `Object` |  |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1790](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1790)

___

### registerInputPacket

▸ **registerInputPacket**(`packet`): `void`

Register HID input packet type to controller.
Input packets can be responses from device to queries, or control
data details. The default control data packet must be named in
variable this.defaultPacket to allow automatic processing.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `packet` | [`HIDPacket`](common_hid_packet_parser.HIDPacket.md) | The input packet to register |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1637](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1637)

___

### registerOutputPacket

▸ **registerOutputPacket**(`packet`): `void`

Register HID output packet type to controller
There are no special Output control output packets, just register Outputs to any
valid packet and we detect them here.
This module only supports sending bitvector values and byte fields to device.
If you need other data structures, patches are welcome, or you can just do it
manually in your script without registering the packet.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `packet` | [`HIDPacket`](common_hid_packet_parser.HIDPacket.md) | The output packet to register |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1671](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1671)

___

### resolveDeck

▸ **resolveDeck**(`group`): `number`

Return deck number from deck name. Deck name can't be virtual deck name
in this function call.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |

#### Returns

`number`

Number of deck

#### Defined in

[common-hid-packet-parser.js:1402](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1402)

___

### resolveDeckGroup

▸ **resolveDeckGroup**(`deck`): `string`

Return the group name from given deck number.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deck` | `number` | Number of deck |

#### Returns

`string`

Group name of the deck (e.g. Channel2 for deck number 2)

#### Defined in

[common-hid-packet-parser.js:1419](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1419)

___

### resolveGroup

▸ **resolveGroup**(`group`): `string`

Map virtual deck names to real deck group. If group is already
a real mixxx group value, just return it as it without mapping.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |

#### Returns

`string`

Channel

#### Defined in

[common-hid-packet-parser.js:1432](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1432)

___

### setAutoRepeat

▸ **setAutoRepeat**(`group`, `name`, `callback`, `interval`): `void`

Toggle field autorepeat on or off

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` |  |
| `name` | `string` |  |
| `callback` | [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback) | Callback function for the control |
| `interval` | `number` |  |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2124](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2124)

___

### setCallback

▸ **setCallback**(`packet`, `group`, `name`, `callback`): `void`

Register packet field's callback.
If packet has callback, it is still parsed but no field processing is done,
callback is called directly after unpacking fields from packet.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `packet` | `string` | The name of the input packet e.g. 'InputReport_0x02' |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name "pregain" |
| `callback` | [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback) | Callback function for the control |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1515](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1515)

___

### setOutput

▸ **setOutput**(`group`, `name`, `value`, `send_packet?`): `void`

Set output state to given value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name "cue_indicator" |
| `value` | `number` \| `boolean` | Value to set as new output state of the control |
| `send_packet?` | `boolean` | If true, the packet (an HID OutputReport) is send immediately |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2313](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2313)

___

### setOutputToggle

▸ **setOutputToggle**(`group`, `name`, `toggle_value`): `void`

Set Output to toggle between two values. Reset with setOutput(name,'off')

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name "cue_indicator" |
| `toggle_value` | `any` |  |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2332](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2332)

___

### setPacketCallback

▸ **setPacketCallback**(`packet`, `callback`): `void`

Set input packet callback afterwards

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `packet` | `string` | The name of the input packet e.g. 'InputReport_0x02' |
| `callback` | [`packetCallback`](../modules/common_hid_packet_parser.md#packetcallback) | Callback function for the control |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1501](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1501)

___

### setScaler

▸ **setScaler**(`name`, `callback`): `void`

Register scaling function for a control name
This does not check if given control name is valid

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | Reference of the scaling function in scalers list of HIDController |
| `callback` | [`scalingCallback`](../modules/common_hid_packet_parser.md#scalingcallback) | Scaling function |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1530](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1530)

___

### stopAutoRepeatTimer

▸ **stopAutoRepeatTimer**(`timer_id`): `void`

Stops the specified auto repeat timer

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `timer_id` | `string` | Reference of the timer to stop |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2108](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2108)

___

### switchDeck

▸ **switchDeck**(`deck`): `void`

Toggle active deck and update virtual output field control mappings

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deck` | `number` | Number of deck |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2173](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2173)

___

### toggle

▸ **toggle**(`group`, `control`, `value`): `void`

Toggle control state from toggle button

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `control` | `string` | Name of the control (button) |
| `value` | `number` | Value defined in this.buttonStates |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1984](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1984)

___

### togglePlay

▸ **togglePlay**(`group`, `field`): `void`

Toggle play/pause state

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `field` | [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) | Object that describes a field inside of a packet, which can often mapped to a Mixxx control. |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1998](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1998)

___

### unlinkControl

▸ **unlinkControl**(`_group`, `_name`): `void`

**`Todo`**

Implement unlinking of controls

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `_group` | `string` | Mixxx control group name e.g. "[Channel1]" |
| `_name` | `string` | Mixxx control name "pregain" |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1628](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1628)

___

### unlinkModifier

▸ **unlinkModifier**(`_group`, `_name`, `_modifier`): `void`

**`Todo`**

Implement unlinking of modifiers

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `_group` | `string` | Unused |
| `_name` | `string` | Unused |
| `_modifier` | `string` | Unused |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1580](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1580)

___

### unlinkOutput

▸ **unlinkOutput**(`group`, `name`, `callback`): `void`

Unlink a virtual HID Output from mixxx control

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Mixxx control group name e.g. "[Channel1]" |
| `name` | `string` | Mixxx control name "VuMeter" |
| `callback` | [`controlCallback`](../modules/common_hid_packet_parser.md#controlcallback) | Callback function for the control |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2288](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2288)

___

### fastForIn

▸ `Static` **fastForIn**(`object`, `body`): `void`

Fast loop implementation over object

Don't use 'continue' and 'break' don't work as in normal loops,
because body is a function
'return' statements in the body function behaves as 'continue' in normal loops

#### Parameters

| Name | Type |
| :------ | :------ |
| `object` | `Object` |
| `body` | (`arg0`: `string`) => `void` |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:2352](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L2352)
