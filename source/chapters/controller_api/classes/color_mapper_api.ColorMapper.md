[Documentation](../README.md) / [Modules](../modules.md) / [color-mapper-api](../modules/color_mapper_api.md) / ColorMapper

# Class: ColorMapper

[color-mapper-api](../modules/color_mapper_api.md).ColorMapper

ColorMapperJSProxy

## Table of contents

### Constructors

- [constructor](color_mapper_api.ColorMapper.md#constructor)

### Methods

- [getNearestColor](color_mapper_api.ColorMapper.md#getnearestcolor)
- [getValueForNearestColor](color_mapper_api.ColorMapper.md#getvaluefornearestcolor)

## Constructors

### constructor

• **new ColorMapper**(`availableColors`)

Constructs a ColorMapper object which maps RGB colors to device specific color codes

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `availableColors` | `Object` | List of number pairs (e.g. {0xFF0000: 1, 0x00FF00: 2} ) |

#### Defined in

[color-mapper-api.d.ts:10](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/color-mapper-api.d.ts#L10)

## Methods

### getNearestColor

▸ **getNearestColor**(`colorCode`): `Object`

For a given RGB color code (e.g. 0xFF0000), this finds the nearest
available color and returns a JS object with properties "red", "green",
"blue" (each with value range 0-255).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `colorCode` | `number` | Device specific color code |

#### Returns

`Object`

#### Defined in

[color-mapper-api.d.ts:19](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/color-mapper-api.d.ts#L19)

___

### getValueForNearestColor

▸ **getValueForNearestColor**(`rgbColor`): `number`

For a given RGB color code (e.g. 0xFF0000), this finds the nearest
available color, then returns the value associated with that color
(which could be a MIDI byte value for example).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `rgbColor` | `number` | RGB color (e.g. 0xFF00CC) |

#### Returns

`number`

#### Defined in

[color-mapper-api.d.ts:28](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/color-mapper-api.d.ts#L28)
