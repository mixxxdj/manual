[Documentation](../README.md) / [Modules](../modules.md) / [common-hid-packet-parser](../modules/common_hid_packet_parser.md) / bitObject

# Interface: bitObject<\>

[common-hid-packet-parser](../modules/common_hid_packet_parser.md).bitObject

## Table of contents

### Properties

- [auto\_repeat](common_hid_packet_parser.bitObject.md#auto_repeat)
- [auto\_repeat\_interval](common_hid_packet_parser.bitObject.md#auto_repeat_interval)
- [bit\_offset](common_hid_packet_parser.bitObject.md#bit_offset)
- [bitmask](common_hid_packet_parser.bitObject.md#bitmask)
- [callback](common_hid_packet_parser.bitObject.md#callback)
- [group](common_hid_packet_parser.bitObject.md#group)
- [id](common_hid_packet_parser.bitObject.md#id)
- [mapped\_callback](common_hid_packet_parser.bitObject.md#mapped_callback)
- [mapped\_group](common_hid_packet_parser.bitObject.md#mapped_group)
- [mapped\_name](common_hid_packet_parser.bitObject.md#mapped_name)
- [name](common_hid_packet_parser.bitObject.md#name)
- [packet](common_hid_packet_parser.bitObject.md#packet)
- [toggle](common_hid_packet_parser.bitObject.md#toggle)
- [type](common_hid_packet_parser.bitObject.md#type)
- [value](common_hid_packet_parser.bitObject.md#value)

## Properties

### auto\_repeat

• **auto\_repeat**: [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback)

#### Defined in

[common-hid-packet-parser.js:135](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L135)

___

### auto\_repeat\_interval

• **auto\_repeat\_interval**: `number`

#### Defined in

[common-hid-packet-parser.js:136](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L136)

___

### bit\_offset

• **bit\_offset**: `number`

#### Defined in

[common-hid-packet-parser.js:133](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L133)

___

### bitmask

• **bitmask**: `number`

#### Defined in

[common-hid-packet-parser.js:132](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L132)

___

### callback

• **callback**: [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback)

#### Defined in

[common-hid-packet-parser.js:134](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L134)

___

### group

• **group**: `string`

#### Defined in

[common-hid-packet-parser.js:127](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L127)

___

### id

• **id**: `string`

Group and control name separated by a dot

#### Defined in

[common-hid-packet-parser.js:126](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L126)

___

### mapped\_callback

• **mapped\_callback**: [`controlCallback`](../modules/common_hid_packet_parser.md#controlcallback)

#### Defined in

[common-hid-packet-parser.js:131](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L131)

___

### mapped\_group

• **mapped\_group**: `string`

Mapped group, must be a valid Mixxx control group name e.g. "[Channel1]"

#### Defined in

[common-hid-packet-parser.js:129](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L129)

___

### mapped\_name

• **mapped\_name**: `string`

Name of mapped control, must be a valid Mixxx control name "cue_indicator"

#### Defined in

[common-hid-packet-parser.js:130](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L130)

___

### name

• **name**: `string`

#### Defined in

[common-hid-packet-parser.js:128](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L128)

___

### packet

• **packet**: [`HIDPacket`](../classes/common_hid_packet_parser.HIDPacket.md)

#### Defined in

[common-hid-packet-parser.js:125](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L125)

___

### toggle

• **toggle**: `number`

#### Defined in

[common-hid-packet-parser.js:141](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L141)

___

### type

• **type**: ``"output"`` \| ``"button"``

Must be either:
             - 'button'
             - 'output'

#### Defined in

[common-hid-packet-parser.js:137](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L137)

___

### value

• **value**: `number`

#### Defined in

[common-hid-packet-parser.js:140](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L140)
