[Documentation](../README.md) / [Modules](../modules.md) / [common-hid-packet-parser](../modules/common_hid_packet_parser.md) / HIDModifierList

# Class: HIDModifierList

[common-hid-packet-parser](../modules/common_hid_packet_parser.md).HIDModifierList

HID Modifiers object

e.g. a shift button can be defined as modifier for the behavior of other controls.

Wraps all defined modifiers to one object with uniform API.
Don't call directly, this is available as HIDController.modifiers

## Table of contents

### Constructors

- [constructor](common_hid_packet_parser.HIDModifierList.md#constructor)

### Properties

- [callbacks](common_hid_packet_parser.HIDModifierList.md#callbacks)
- [modifiers](common_hid_packet_parser.HIDModifierList.md#modifiers)

### Methods

- [add](common_hid_packet_parser.HIDModifierList.md#add)
- [get](common_hid_packet_parser.HIDModifierList.md#get)
- [set](common_hid_packet_parser.HIDModifierList.md#set)
- [setCallback](common_hid_packet_parser.HIDModifierList.md#setcallback)

## Constructors

### constructor

• **new HIDModifierList**()

#### Defined in

[common-hid-packet-parser.js:251](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L251)

## Properties

### callbacks

• **callbacks**: `Object`

Function to be called after modifier value changes

#### Defined in

[common-hid-packet-parser.js:264](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L264)

___

### modifiers

• **modifiers**: `Object`

Actual value of the modifier

#### Defined in

[common-hid-packet-parser.js:257](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L257)

## Methods

### add

▸ **add**(`name`): `void`

Add a new modifier to controller.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | Name of modifier |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:271](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L271)

___

### get

▸ **get**(`name`): `boolean`

Get modifier value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | Name of modifier |

#### Returns

`boolean`

Value of modifier

#### Defined in

[common-hid-packet-parser.js:301](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L301)

___

### set

▸ **set**(`name`, `value`): `void`

Set modifier value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | Name of modifier |
| `value` | `boolean` | Value to be set |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:284](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L284)

___

### setCallback

▸ **setCallback**(`name`, `callback`): `void`

Set modifier callback function

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | Name of reference in HIDModifierList |
| `callback` | [`modifierCallback`](../modules/common_hid_packet_parser.md#modifiercallback) | Function to be called after modifier value changes |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:314](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L314)
