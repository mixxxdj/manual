[Documentation](../README.md) / [Modules](../modules.md) / [common-hid-packet-parser](../modules/common_hid_packet_parser.md) / HIDBitVector

# Class: HIDBitVector

[common-hid-packet-parser](../modules/common_hid_packet_parser.md).HIDBitVector

HID Bit Vector Class

Collection of bits in one parsed packet field. These objects are
created by HIDPacket addControl and addOutput and should not be
created manually.

## Table of contents

### Constructors

- [constructor](common_hid_packet_parser.HIDBitVector.md#constructor)

### Properties

- [bits](common_hid_packet_parser.HIDBitVector.md#bits)
- [size](common_hid_packet_parser.HIDBitVector.md#size)

### Methods

- [addBitMask](common_hid_packet_parser.HIDBitVector.md#addbitmask)
- [addOutputMask](common_hid_packet_parser.HIDBitVector.md#addoutputmask)
- [getOffset](common_hid_packet_parser.HIDBitVector.md#getoffset)

## Constructors

### constructor

• **new HIDBitVector**()

#### Defined in

[common-hid-packet-parser.js:153](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L153)

## Properties

### bits

• **bits**: `Object`

Object of bitObjects, referred by a string of group and control name separated by a dot

#### Defined in

[common-hid-packet-parser.js:165](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L165)

___

### size

• **size**: `number`

Number of bitObjects in bits array

#### Defined in

[common-hid-packet-parser.js:159](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L159)

## Methods

### addBitMask

▸ **addBitMask**(`group`, `name`, `bitmask`): `void`

Add a control bitmask to the HIDBitVector

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name e.g. "play" |
| `bitmask` | `number` | A bitwise mask of up to 32 bit. All bits set to'1' in this mask are considered. |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:192](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L192)

___

### addOutputMask

▸ **addOutputMask**(`group`, `name`, `bitmask`): `void`

Add an output control bitmask to the HIDBitVector

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name e.g. "play" |
| `bitmask` | `number` | A bitwise mask of up to 32 bit. All bits set to'1' in this mask are considered. |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:218](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L218)

___

### getOffset

▸ **getOffset**(`bitmask`): `number`

Get the index of the least significant bit that is 1 in `bitmask`

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `bitmask` | `number` | A bitwise mask of up to 32 bit. All bits set to'1' in this mask are considered. |

#### Returns

`number`

Index of the least significant bit that is 1 in `bitmask`

#### Defined in

[common-hid-packet-parser.js:174](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L174)
