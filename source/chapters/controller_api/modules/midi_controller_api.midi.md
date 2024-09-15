[Documentation](../README.md) / [Modules](../modules.md) / [midi-controller-api](midi_controller_api.md) / midi

# Namespace: midi

[midi-controller-api](midi_controller_api.md).midi

MidiControllerJSProxy

## Table of contents

### Functions

- [send](midi_controller_api.midi.md#send)
- [sendShortMsg](midi_controller_api.midi.md#sendshortmsg)
- [sendSysexMsg](midi_controller_api.midi.md#sendsysexmsg)

## Functions

### send

▸ **send**(`dataList`, `length?`): `void`

Alias for [sendSysexMsg](midi_controller_api.midi.md#sendsysexmsg)
Sends a MIDI system-exclusive message of arbitrary number of bytes

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `dataList` | `number`[] | List of bytes to send |
| `length?` | `number` | This is no longer evaluated, and only here for backwards compatibility with old scripts [default = 0] |

#### Returns

`void`

#### Defined in

[midi-controller-api.d.ts:22](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/midi-controller-api.d.ts#L22)

___

### sendShortMsg

▸ **sendShortMsg**(`status`, `byte1`, `byte2`): `void`

Sends a 3 byte MIDI short message

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `status` | `number` | Status byte |
| `byte1` | `number` | Data byte 1 |
| `byte2` | `number` | Data byte 2 |

#### Returns

`void`

#### Defined in

[midi-controller-api.d.ts:13](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/midi-controller-api.d.ts#L13)

___

### sendSysexMsg

▸ **sendSysexMsg**(`dataList`, `length?`): `void`

Sends a MIDI system-exclusive message of arbitrary number of bytes

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `dataList` | `number`[] | List of bytes to send |
| `length?` | `number` | This is no longer evaluated, and only here for backwards compatibility with old scripts [default = 0] |

#### Returns

`void`

#### Defined in

[midi-controller-api.d.ts:30](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/midi-controller-api.d.ts#L30)
