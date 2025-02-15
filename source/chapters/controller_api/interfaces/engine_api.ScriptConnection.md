[Documentation](../README.md) / [Modules](../modules.md) / [engine-api](../modules/engine_api.md) / ScriptConnection

# Interface: ScriptConnection

[engine-api](../modules/engine_api.md).ScriptConnection

ScriptConnectionJSProxy

## Table of contents

### Methods

- [disconnect](engine_api.ScriptConnection.md#disconnect)
- [trigger](engine_api.ScriptConnection.md#trigger)

## Methods

### disconnect

▸ **disconnect**(): `boolean`

Disconnect the script connection,
established by [makeConnection](../modules/engine_api.engine.md#makeconnection) or [makeUnbufferedConnection](../modules/engine_api.engine.md#makeunbufferedconnection)

#### Returns

`boolean`

Returns true if the connection has been disconnected successfully

#### Defined in

[engine-api.d.ts:11](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L11)

___

### trigger

▸ **trigger**(): `void`

Triggers the execution of the callback function of the script connection,
established by [makeConnection](../modules/engine_api.engine.md#makeconnection) or [makeUnbufferedConnection](../modules/engine_api.engine.md#makeunbufferedconnection)
with the actual value of a control.

Note: To execute all callback functions connected to a ControlObject at once, use [trigger](../modules/engine_api.engine.md#trigger) instead

#### Returns

`void`

#### Defined in

[engine-api.d.ts:20](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L20)
