[Documentation](../README.md) / [Modules](../modules.md) / [common-hid-packet-parser](../modules/common_hid_packet_parser.md) / packetField

# Interface: packetField<\>

[common-hid-packet-parser](../modules/common_hid_packet_parser.md).packetField

## Table of contents

### Properties

- [auto\_repeat](common_hid_packet_parser.packetField.md#auto_repeat)
- [auto\_repeat\_interval](common_hid_packet_parser.packetField.md#auto_repeat_interval)
- [bitmask](common_hid_packet_parser.packetField.md#bitmask)
- [callback](common_hid_packet_parser.packetField.md#callback)
- [delta](common_hid_packet_parser.packetField.md#delta)
- [end\_offset](common_hid_packet_parser.packetField.md#end_offset)
- [group](common_hid_packet_parser.packetField.md#group)
- [id](common_hid_packet_parser.packetField.md#id)
- [ignored](common_hid_packet_parser.packetField.md#ignored)
- [isEncoder](common_hid_packet_parser.packetField.md#isencoder)
- [mapped\_callback](common_hid_packet_parser.packetField.md#mapped_callback)
- [mapped\_group](common_hid_packet_parser.packetField.md#mapped_group)
- [mapped\_name](common_hid_packet_parser.packetField.md#mapped_name)
- [max](common_hid_packet_parser.packetField.md#max)
- [min](common_hid_packet_parser.packetField.md#min)
- [mindelta](common_hid_packet_parser.packetField.md#mindelta)
- [name](common_hid_packet_parser.packetField.md#name)
- [offset](common_hid_packet_parser.packetField.md#offset)
- [pack](common_hid_packet_parser.packetField.md#pack)
- [packet](common_hid_packet_parser.packetField.md#packet)
- [soft\_takeover](common_hid_packet_parser.packetField.md#soft_takeover)
- [toggle](common_hid_packet_parser.packetField.md#toggle)
- [type](common_hid_packet_parser.packetField.md#type)
- [value](common_hid_packet_parser.packetField.md#value)

## Properties

### auto\_repeat

• **auto\_repeat**: [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback)

#### Defined in

[common-hid-packet-parser.js:108](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L108)

___

### auto\_repeat\_interval

• **auto\_repeat\_interval**: `number`

#### Defined in

[common-hid-packet-parser.js:109](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L109)

___

### bitmask

• **bitmask**: `number`

#### Defined in

[common-hid-packet-parser.js:103](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L103)

___

### callback

• **callback**: [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback)

#### Defined in

[common-hid-packet-parser.js:105](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L105)

___

### delta

• **delta**: `number`

#### Defined in

[common-hid-packet-parser.js:117](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L117)

___

### end\_offset

• **end\_offset**: `number`

Position of the last byte in the packet in bytes ([offset](common_hid_packet_parser.packetField.md#offset) + packet size)

#### Defined in

[common-hid-packet-parser.js:102](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L102)

___

### group

• **group**: `string`

#### Defined in

[common-hid-packet-parser.js:95](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L95)

___

### id

• **id**: `string`

Group and control name separated by a dot

#### Defined in

[common-hid-packet-parser.js:94](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L94)

___

### ignored

• **ignored**: `boolean`

#### Defined in

[common-hid-packet-parser.js:107](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L107)

___

### isEncoder

• **isEncoder**: `boolean`

#### Defined in

[common-hid-packet-parser.js:104](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L104)

___

### mapped\_callback

• **mapped\_callback**: [`controlCallback`](../modules/common_hid_packet_parser.md#controlcallback)

#### Defined in

[common-hid-packet-parser.js:99](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L99)

___

### mapped\_group

• **mapped\_group**: `string`

Mapped group, must be a valid Mixxx control group name e.g. "[Channel1]"

#### Defined in

[common-hid-packet-parser.js:97](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L97)

___

### mapped\_name

• **mapped\_name**: `string`

Name of mapped control, must be a valid Mixxx control name "VuMeter"

#### Defined in

[common-hid-packet-parser.js:98](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L98)

___

### max

• **max**: `number`

#### Defined in

[common-hid-packet-parser.js:111](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L111)

___

### min

• **min**: `number`

#### Defined in

[common-hid-packet-parser.js:110](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L110)

___

### mindelta

• **mindelta**: `number`

#### Defined in

[common-hid-packet-parser.js:118](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L118)

___

### name

• **name**: `string`

#### Defined in

[common-hid-packet-parser.js:96](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L96)

___

### offset

• **offset**: `number`

Position of the first byte in the packet in bytes (first byte is 0)

#### Defined in

[common-hid-packet-parser.js:101](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L101)

___

### pack

• **pack**: `string`

Control packing format for unpack(), one of b/B, h/H, i/I

#### Defined in

[common-hid-packet-parser.js:100](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L100)

___

### packet

• **packet**: [`HIDPacket`](../classes/common_hid_packet_parser.HIDPacket.md)

#### Defined in

[common-hid-packet-parser.js:93](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L93)

___

### soft\_takeover

• **soft\_takeover**: `boolean`

#### Defined in

[common-hid-packet-parser.js:106](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L106)

___

### toggle

• **toggle**: `number`

#### Defined in

[common-hid-packet-parser.js:119](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L119)

___

### type

• **type**: ``"bitvector"`` \| ``"control"`` \| ``"output"``

Must be either:
             - 'bitvector'       If value is of type HIDBitVector
             - 'control'         If value is a number
             - 'output'

#### Defined in

[common-hid-packet-parser.js:112](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L112)

___

### value

• **value**: `number` \| `boolean` \| [`HIDBitVector`](../classes/common_hid_packet_parser.HIDBitVector.md)

#### Defined in

[common-hid-packet-parser.js:116](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L116)
