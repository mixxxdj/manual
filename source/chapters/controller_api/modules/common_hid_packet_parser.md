[Documentation](../README.md) / [Modules](../modules.md) / common-hid-packet-parser

# Module: common-hid-packet-parser

## Table of contents

### Classes

- [HIDBitVector](../classes/common_hid_packet_parser.HIDBitVector.md)
- [HIDController](../classes/common_hid_packet_parser.HIDController.md)
- [HIDModifierList](../classes/common_hid_packet_parser.HIDModifierList.md)
- [HIDPacket](../classes/common_hid_packet_parser.HIDPacket.md)

### Interfaces

- [bitObject](../interfaces/common_hid_packet_parser.bitObject.md)
- [packetField](../interfaces/common_hid_packet_parser.packetField.md)

### Type Aliases

- [controlCallback](common_hid_packet_parser.md#controlcallback)
- [fieldChangeCallback](common_hid_packet_parser.md#fieldchangecallback)
- [modifierCallback](common_hid_packet_parser.md#modifiercallback)
- [packetCallback](common_hid_packet_parser.md#packetcallback)
- [scalingCallback](common_hid_packet_parser.md#scalingcallback)
- [scratchingCallback](common_hid_packet_parser.md#scratchingcallback)

### Functions

- [HIDDebug](common_hid_packet_parser.md#hiddebug)
- [createDataView](common_hid_packet_parser.md#createdataview)

## Type Aliases

### controlCallback

Ƭ **controlCallback**<\>: <\>(`value`: `number`, `group`: `string`, `name`: `string`) => `any`

#### Type declaration

▸ <\>(`value`, `group`, `name`): `any`

##### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `value` | `number` | New value of the control |
| `group` | `string` | Mixxx control group name e.g. "[Channel1]" |
| `name` | `string` | Mixxx control name "pregain" |

##### Returns

`any`

#### Defined in

[common-hid-packet-parser.js:58](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L58)

___

### fieldChangeCallback

Ƭ **fieldChangeCallback**<\>: <\>(`Object`: [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) \| [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md)) => `any`

#### Type declaration

▸ <\>(`Object`): `any`

##### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `Object` | [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) \| [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md) | that describes a field/bit inside of a packet, which can often mapped to a Mixxx control. |

##### Returns

`any`

#### Defined in

[common-hid-packet-parser.js:50](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L50)

___

### modifierCallback

Ƭ **modifierCallback**<\>: <\>(`Value`: `boolean`) => `any`

#### Type declaration

▸ <\>(`Value`): `any`

##### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `Value` | `boolean` | of the modifier control |

##### Returns

`any`

#### Defined in

[common-hid-packet-parser.js:44](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L44)

___

### packetCallback

Ƭ **packetCallback**<\>: <\>(`packet`: [`HIDPacket`](../classes/common_hid_packet_parser.HIDPacket.md), `changed_data`: `Object`<`string`, [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) \| [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md)\>) => `any`

#### Type declaration

▸ <\>(`packet`, `changed_data`): `any`

##### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `packet` | [`HIDPacket`](../classes/common_hid_packet_parser.HIDPacket.md) | The packet that represents the InputReport |
| `changed_data` | `Object`<`string`, [`packetField`](../interfaces/common_hid_packet_parser.packetField.md) \| [`bitObject`](../interfaces/common_hid_packet_parser.bitObject.md)\> | The data received from the device |

##### Returns

`any`

#### Defined in

[common-hid-packet-parser.js:37](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L37)

___

### scalingCallback

Ƭ **scalingCallback**<\>: <\>(`group`: `string`, `name`: `string`, `value`: `number`) => `number`

#### Type declaration

▸ <\>(`group`, `name`, `value`): `number`

##### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Control group name e.g. "[Channel1]" |
| `name` | `string` | Control name "pregain" |
| `value` | `number` | Value to be scaled |

##### Returns

`number`

#### Defined in

[common-hid-packet-parser.js:75](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L75)

___

### scratchingCallback

Ƭ **scratchingCallback**<\>: <\>(`isScratchEnabled`: `boolean`) => `any`

#### Type declaration

▸ <\>(`isScratchEnabled`): `any`

##### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `isScratchEnabled` | `boolean` | True, when button 'jog_touch' is active |

##### Returns

`any`

#### Defined in

[common-hid-packet-parser.js:86](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L86)

## Functions

### HIDDebug

▸ **HIDDebug**(`message`): `void`

Common HID script debugging function. Just to get logging with 'HID' prefix.

**`Deprecated`**

Use console.log instead

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `message` | `any` | Message to be printed on controller debug console output |

#### Returns

`void`

#### Defined in

[common-hid-packet-parser.js:9](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L9)

___

### createDataView

▸ **createDataView**(`bufferLike`): `DataView`

creates a `DataView` from any ArrayBuffer, TypedArray
or plain Array (clamped to 8-bit width).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `bufferLike` | `any` | Object that can be represented as a sequence of bytes |

#### Returns

`DataView`

dataview over the bufferLike object

#### Defined in

[common-hid-packet-parser.js:19](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/common-hid-packet-parser.js#L19)
