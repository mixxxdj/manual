[Documentation](../README.md) / [Modules](../modules.md) / [common-hid-packet-parser](../modules/common_hid_packet_parser.md) / HIDPacket

# Class: HIDPacket

[common-hid-packet-parser](../modules/common_hid_packet_parser.md).HIDPacket

HID Packet object

An HIDPacket represents one HID report of type InputReport or OutputReport (FeatureReports are
currently not supported)

Each HIDPacket must be registered to HIDController.

## Table of contents

### Constructors

- [constructor](common_hid_packet_parser.HIDPacket.md#constructor)

### Properties

- [callback](common_hid_packet_parser.HIDPacket.md#callback)
- [groups](common_hid_packet_parser.HIDPacket.md#groups)
- [header](common_hid_packet_parser.HIDPacket.md#header)
- [length](common_hid_packet_parser.HIDPacket.md#length)
- [name](common_hid_packet_parser.HIDPacket.md#name)
- [packSizes](common_hid_packet_parser.HIDPacket.md#packsizes)
- [reportId](common_hid_packet_parser.HIDPacket.md#reportid)
- [signedPackFormats](common_hid_packet_parser.HIDPacket.md#signedpackformats)

### Methods

- [addControl](common_hid_packet_parser.HIDPacket.md#addcontrol)
- [addOutput](common_hid_packet_parser.HIDPacket.md#addoutput)
- [getField](common_hid_packet_parser.HIDPacket.md#getfield)
- [getFieldByOffset](common_hid_packet_parser.HIDPacket.md#getfieldbyoffset)
- [getGroup](common_hid_packet_parser.HIDPacket.md#getgroup)
- [lookupBit](common_hid_packet_parser.HIDPacket.md#lookupbit)
- [pack](common_hid_packet_parser.HIDPacket.md#pack)
- [parse](common_hid_packet_parser.HIDPacket.md#parse)
- [parseBitVector](common_hid_packet_parser.HIDPacket.md#parsebitvector)
- [removeControl](common_hid_packet_parser.HIDPacket.md#removecontrol)
- [send](common_hid_packet_parser.HIDPacket.md#send)
- [setCallback](common_hid_packet_parser.HIDPacket.md#setcallback)
- [setIgnored](common_hid_packet_parser.HIDPacket.md#setignored)
- [setMinDelta](common_hid_packet_parser.HIDPacket.md#setmindelta)
- [unpack](common_hid_packet_parser.HIDPacket.md#unpack)

## Constructors

### constructor

• **new HIDPacket**(`name`, `reportId?`, `callback?`, `header?`)

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `name` | `string` | `undefined` | Name of packet (it makes sense to refer the HID report type and HID ReportID here e.g. 'InputReport_0x02' or 'OutputReport_0x81') |
| `reportId` | `number` | `0` | ReportID of the packet. If the device does not use ReportIDs this must be 0. [default = 0] |
| `callback` | [`packetCallback`](../modules/common_hid_packet_parser.md#packetcallback) | `undefined` | function to call when the packet type represents an InputReport, and a new report is received. If packet callback is set, the packet is not parsed by delta functions. Note, that a callback is not meaningful for output packets. |
| `header` | `number`[] | `[]` | (optional) List of bytes to match from beginning of packet. Do NOT put the report ID in this - use the reportId parameter instead. |

#### Defined in

[common-hid-packet-parser.js:348](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L348)

## Properties

### callback

• **callback**: [`packetCallback`](../modules/common_hid_packet_parser.md#packetcallback)

Function to call when the packet type represents an InputReport, and a new report is received.

#### Defined in

[common-hid-packet-parser.js:368](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L368)

___

### groups

• **groups**: `Object`

Object of groups, referred by the group string

#### Defined in

[common-hid-packet-parser.js:382](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L382)

[common-hid-packet-parser.js:504](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L504)

___

### header

• **header**: `number`[]

List of bytes to match from beginning of packet

#### Defined in

[common-hid-packet-parser.js:375](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L375)

___

### length

• **length**: `number`

Length of packet in bytes

#### Defined in

[common-hid-packet-parser.js:389](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L389)

[common-hid-packet-parser.js:843](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L843)

[common-hid-packet-parser.js:891](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L891)

___

### name

• **name**: `string`

Name of packet

#### Defined in

[common-hid-packet-parser.js:354](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L354)

___

### packSizes

• **packSizes**: `Object`

Size of the 'pack' types in bytes

#### Defined in

[common-hid-packet-parser.js:396](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L396)

___

### reportId

• **reportId**: `number`

ReportID of the packet. If the device does not use ReportIDs this must be 0.

#### Defined in

[common-hid-packet-parser.js:361](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L361)

___

### signedPackFormats

• **signedPackFormats**: `string`[]

#### Defined in

[common-hid-packet-parser.js:397](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L397)

## Methods

### addControl

▸ **addControl**(`group`, `name`, `offset`, `pack`, `bitmask`, `isEncoder`, `callback`): `void`

Register a numeric value to parse from input packet

'group' and 'name' form the ID of the field, if it matches a valid Mixxx control name,
the system attempts to attach it directly to the correct field.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name e.g. "play" |
| `offset` | `number` | The field's offset from the start of the packet in bytes: - For HID devices which don't use ReportIDs, the data bytes starts at position 0 - For HID devices which use ReportIDs to enumerate the reports, the data bytes starts at position 1 |
| `pack` | `string` | Is one of the field packing types: - b signed byte (Int8) - B unsigned byte (Uint8) - h signed short (Int16 Little-Endian) - H unsigned short (Uint16 Little-Endian) - i signed integer (Int32 Little-Endian) - I unsigned integer (Uint32 Little-Endian) |
| `bitmask` | `number` | A bitwise mask of up to 32 bit. All bits set to'1' in this mask are considered. Note: For controls that use full bytes (8bit, 16bit, ...), you can set this to undefined NOTE: Parsing bitmask with multiple bits is not supported yet. |
| `isEncoder` | `boolean` | indicates if this is an encoder which should be wrapped and delta reported |
| `callback` | [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback) | Callback function for the control |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:678](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L678)

___

### addOutput

▸ **addOutput**(`group`, `name`, `offset`, `pack`, `bitmask?`, `callback?`): `void`

Register a Output control field or Output control bit to output packet
Output control field:
   Output field with no bitmask, controls Output with multiple values
Output control bit:
   Output with with bitmask, controls Output with a single bit

It is recommended to define callbacks after packet creation with
setCallback instead of adding it directly here. But you can do it.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name "VuMeter" |
| `offset` | `number` | The field's offset from the start of the packet in bytes: - For HID devices which don't use ReportIDs, the data bytes starts at position 0 - For HID devices which use ReportIDs to enumerate the reports, the data bytes starts at position 1 |
| `pack` | `string` | Is one of the field packing types: - b signed byte (Int8) - B unsigned byte (Uint8) - h signed short (Int16 Little-Endian) - H unsigned short (Uint16 Little-Endian) - i signed integer (Int32 Little-Endian) - I unsigned integer (Uint32 Little-Endian) |
| `bitmask?` | `number` | A bitwise mask of up to 32 bit. All bits set to'1' in this mask are considered. |
| `callback?` | [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback) | Callback function for the control |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:814](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L814)

___

### getField

▸ **getField**(`group`, `name`): [`packetField`](../interfaces/common_hid_packet_parser.packetField.md)

Return a field by group and name from the packet,
Returns undefined if field could not be found

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name e.g. "play" |

#### Returns

[`packetField`](../interfaces/common_hid_packet_parser.packetField.md)

Field

#### Defined in

[common-hid-packet-parser.js:573](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L573)

___

### getFieldByOffset

▸ **getFieldByOffset**(`offset`, `pack`): [`packetField`](../interfaces/common_hid_packet_parser.packetField.md)

Lookup HID packet field matching given offset and pack type

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `offset` | `number` | The field's offset from the start of the packet in bytes: - For HID devices which don't use ReportIDs, the data bytes starts at position 0 - For HID devices which use ReportIDs to enumerate the reports, the data bytes starts at position 1 |
| `pack` | `string` | Is one of the field packing types: - b signed byte (Int8) - B unsigned byte (Uint8) - h signed short (Int16 Little-Endian) - H unsigned short (Uint16 Little-Endian) - i signed integer (Int32 Little-Endian) - I unsigned integer (Uint32 Little-Endian) |

#### Returns

[`packetField`](../interfaces/common_hid_packet_parser.packetField.md)

Returns matching field or undefined if no matching field can be found.

#### Defined in

[common-hid-packet-parser.js:532](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L532)

___

### getGroup

▸ **getGroup**(`name`, `create?`): `any`

Find HID packet group matching name.
Create group if create is true

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name` | `string` | Name of the group |
| `create?` | `boolean` | If true, group will be created |

#### Returns

`any`

Group Returns group or undefined, when group is not existing and create is set
    to false

#### Defined in

[common-hid-packet-parser.js:502](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L502)

___

### lookupBit

▸ **lookupBit**(`group`, `name`): [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md)

Return reference to a bit in a bitvector field

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name e.g. "play" |

#### Returns

[`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md)

Reference to a bit in a bitvector field

#### Defined in

[common-hid-packet-parser.js:611](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L611)

___

### pack

▸ **pack**(`data`, `field`): `void`

Pack a field value to the packet.
Can only pack bits and byte values, patches welcome.

**`Todo`**

Implement multi byte bit vector outputs

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `data` | `Uint8Array` | Data to be send as OutputReport to the device |
| `field` | [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) | Object that describes a field inside of a packet, which can often mapped to a Mixxx control. |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:409](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L409)

___

### parse

▸ **parse**(`data`): `Object`

Parse input packet fields from data.
Data is expected to be a Packet() received from HID device.
BitVectors are returned as bits you can iterate separately.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `data` | `Uint8Array` | Data received as InputReport from the device |

#### Returns

`Object`

List of changed fields with new value.

#### Defined in

[common-hid-packet-parser.js:1007](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1007)

___

### parseBitVector

▸ **parseBitVector**(`field`, `value`): `Object`

Parse bitvector field values, returning object with the named bits set.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `field` | [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) | Object that describes a field inside of a packet, which can often mapped to a Mixxx control. |
| `value` | `number` | Value must be a valid unsigned byte to parse, with enough bits. |

#### Returns

`Object`

List of modified bits (delta),
                                      referred by a string of group and control name separated by a dot

#### Defined in

[common-hid-packet-parser.js:974](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L974)

___

### removeControl

▸ **removeControl**(`group`, `name`): `void`

Remove a control registered. Normally not needed

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name e.g. "play" |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:642](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L642)

___

### send

▸ **send**(`debug?`): `void`

Send this HID packet to device.
First the header bytes are copied to beginning of packet, then
field object values are packed to the HID packet according to the
field type.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `debug?` | `boolean` | Enables debug output to console |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:1089](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L1089)

___

### setCallback

▸ **setCallback**(`group`, `name`, `callback`): `void`

Register a callback to field or a bit vector bit.
Does not make sense for Output fields but you can do that.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name e.g. "play" |
| `callback` | [`fieldChangeCallback`](../modules/common_hid_packet_parser.md#fieldchangecallback) | Callback function for the control |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:902](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L902)

___

### setIgnored

▸ **setIgnored**(`group`, `name`, `ignored`): `void`

This function can be set in script code to ignore a field you don't want to be processed but
still wanted to define, to make packet format complete from specifications. If field is
ignored, it is not reported in 'delta' objects.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name "pregain" |
| `ignored` | `boolean` | 'ignored' flag for field to given value (true or false) |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:937](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L937)

___

### setMinDelta

▸ **setMinDelta**(`group`, `name`, `mindelta`): `void`

Adjust field's minimum delta value.
Input value changes smaller than this are not reported in delta

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name "pregain" |
| `mindelta` | `number` | Minimum delta value. |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:953](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L953)

___

### unpack

▸ **unpack**(`data`, `field`): `number`

Parse and return field value matching the 'pack' field from field attributes.
Valid field packing types are:
 - b       signed byte
 - B       unsigned byte
 - h       signed short
 - H       unsigned short
 - i       signed integer
 - I       unsigned integer

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `data` | `Uint8Array` | Data received as InputReport from the device |
| `field` | [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) | Object that describes a field inside of a packet, which can often mapped to a Mixxx control. |

#### Returns

`number`

Value for the field in data, represented according the fields packing type

#### Defined in

[common-hid-packet-parser.js:473](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L473)
