[Documentation](../README.md) / [Modules](../modules.md) / [engine-api](engine_api.md) / engine

# Namespace: engine

[engine-api](engine_api.md).engine

ControllerScriptInterfaceLegacy

## Table of contents

### Type Aliases

- [CoCallback](engine_api.engine.md#cocallback)
- [TimerID](engine_api.engine.md#timerid)

### Functions

- [beginTimer](engine_api.engine.md#begintimer)
- [brake](engine_api.engine.md#brake)
- [connectControl](engine_api.engine.md#connectcontrol)
- [getDefaultParameter](engine_api.engine.md#getdefaultparameter)
- [getDefaultValue](engine_api.engine.md#getdefaultvalue)
- [getParameter](engine_api.engine.md#getparameter)
- [getParameterForValue](engine_api.engine.md#getparameterforvalue)
- [getValue](engine_api.engine.md#getvalue)
- [isScratching](engine_api.engine.md#isscratching)
- [log](engine_api.engine.md#log)
- [makeConnection](engine_api.engine.md#makeconnection)
- [makeUnbufferedConnection](engine_api.engine.md#makeunbufferedconnection)
- [reset](engine_api.engine.md#reset)
- [scratchDisable](engine_api.engine.md#scratchdisable)
- [scratchEnable](engine_api.engine.md#scratchenable)
- [scratchTick](engine_api.engine.md#scratchtick)
- [setParameter](engine_api.engine.md#setparameter)
- [setValue](engine_api.engine.md#setvalue)
- [softStart](engine_api.engine.md#softstart)
- [softTakeover](engine_api.engine.md#softtakeover)
- [softTakeoverIgnoreNextValue](engine_api.engine.md#softtakeoverignorenextvalue)
- [spinback](engine_api.engine.md#spinback)
- [stopTimer](engine_api.engine.md#stoptimer)
- [trigger](engine_api.engine.md#trigger)

## Type Aliases

### CoCallback

Ƭ **CoCallback**: (`value`: `number`, `group`: `string`, `name`: `string`) => `void`

#### Type declaration

▸ (`value`, `group`, `name`): `void`

##### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `number` |
| `group` | `string` |
| `name` | `string` |

##### Returns

`void`

#### Defined in

[engine-api.d.ts:104](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L104)

___

### TimerID

Ƭ **TimerID**: `number`

#### Defined in

[engine-api.d.ts:158](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L158)

## Functions

### beginTimer

▸ **beginTimer**(`interval`, `scriptCode`, `oneShot?`): [`TimerID`](engine_api.engine.md#timerid)

Starts a timer that will call the specified script function

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `interval` | `number` | Time in milliseconds until the function is executed. Intervals below 20ms are not allowed. |
| `scriptCode` | () => `any` | Function to be executed, you can also use closures as: function() { print("Executed Timer") } |
| `oneShot?` | `boolean` | If true the function is only once, if false the function is executed repeatedly [default = false] |

#### Returns

[`TimerID`](engine_api.engine.md#timerid)

timerId which is needed to stop a timer.
         In case of an error, 0 is returned.

#### Defined in

[engine-api.d.ts:173](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L173)

___

### brake

▸ **brake**(`deck`, `activate`, `factor?`, `rate?`): `void`

To achieve a brake effect of the playback speed
Both engine.softStart() and engine.brake()/engine.spinback() can interrupt each other.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deck` | `number` | The deck number to use, e.g: 1 |
| `activate` | `boolean` | Set true to activate, or false to disable |
| `factor?` | `number` | Defines how quickly the deck should come to a stop. Start with a value of 1 and increase to increase the acceleration. Be aware that brake called with low factors (about 0.5 and lower), would keep the deck running although the resulting very low sounds are not audible anymore. [default = 1.0] |
| `rate?` | `number` | The initial speed of the deck when enabled. "1" (default) means 10x speed in forward. Negative values like "-1" also work, though then it's spinning reverse obviously. [default = 1.0] |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:255](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L255)

___

### connectControl

▸ **connectControl**(`group`, `name`, `callback`, `disconnect?`): [`ScriptConnection`](../interfaces/engine_api.ScriptConnection.md) \| `boolean` \| `undefined`

This function is a legacy version of makeConnection with several alternate
ways of invoking it. The callback function can be passed either as a string of
JavaScript code that evaluates to a function or an actual JavaScript function.

**`Deprecated`**

Use [makeConnection](engine_api.engine.md#makeconnection) instead

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "VuMeter" |
| `callback` | [`CoCallback`](engine_api.engine.md#cocallback) | JS function, which will be called every time, the value of the connected control changes. |
| `disconnect?` | `boolean` | If "true", all connections to the ControlObject are removed. [default = false] |

#### Returns

[`ScriptConnection`](../interfaces/engine_api.ScriptConnection.md) \| `boolean` \| `undefined`

Returns script connection object on success, otherwise 'undefined' or 'false' depending on the error cause.

#### Defined in

[engine-api.d.ts:143](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L143)

___

### getDefaultParameter

▸ **getDefaultParameter**(`group`, `name`): `number`

Returns the default value of a control, normalized to a range of 0..1

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |

#### Returns

`number`

Default value of the specified control normalized to range of 0..1

#### Defined in

[engine-api.d.ts:102](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L102)

___

### getDefaultValue

▸ **getDefaultValue**(`group`, `name`): `number`

Returns the default value of a control

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |

#### Returns

`number`

Default value with the controls range according Mixxx Controls manual page:
         https://manual.mixxx.org/latest/chapters/appendix/mixxx_controls.html

#### Defined in

[engine-api.d.ts:93](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L93)

___

### getParameter

▸ **getParameter**(`group`, `name`): `number`

Gets the control value normalized to a range of 0..1

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |

#### Returns

`number`

Value of the control normalized to range of 0..1

#### Defined in

[engine-api.d.ts:54](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L54)

___

### getParameterForValue

▸ **getParameterForValue**(`group`, `name`, `value`): `number`

Normalizes a specified value using the range of the given control,
to the range of 0..1

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |
| `value` | `number` | Value with the controls range according Mixxx Controls manual page: https://manual.mixxx.org/latest/chapters/appendix/mixxx_controls.html |

#### Returns

`number`

Value normalized to range of 0..1

#### Defined in

[engine-api.d.ts:75](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L75)

___

### getValue

▸ **getValue**(`group`, `name`): `number`

Gets the control value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |

#### Returns

`number`

Value of the control (within it's range according Mixxx Controls manual page:
         https://manual.mixxx.org/latest/chapters/appendix/mixxx_controls.html)

#### Defined in

[engine-api.d.ts:35](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L35)

___

### isScratching

▸ **isScratching**(`deck`): `boolean`

Returns true if scratching is enabled

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deck` | `number` | The deck number to use, e.g: 1 |

#### Returns

`boolean`

True if scratching is enabled

#### Defined in

[engine-api.d.ts:218](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L218)

___

### log

▸ **log**(`message`): `void`

**`Deprecated`**

Use console.log instead

#### Parameters

| Name | Type |
| :------ | :------ |
| `message` | `string` |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:156](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L156)

___

### makeConnection

▸ **makeConnection**(`group`, `name`, `callback`): [`ScriptConnection`](../interfaces/engine_api.ScriptConnection.md) \| `undefined`

Connects a specified Mixxx Control with a callback function, which is executed if the value of the control changes

This connection has a FIFO buffer - all value change events are processed in serial order.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |
| `callback` | [`CoCallback`](engine_api.engine.md#cocallback) | JS function, which will be called every time, the value of the connected control changes. |

#### Returns

[`ScriptConnection`](../interfaces/engine_api.ScriptConnection.md) \| `undefined`

Returns script connection object on success, otherwise 'undefined''

#### Defined in

[engine-api.d.ts:116](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L116)

___

### makeUnbufferedConnection

▸ **makeUnbufferedConnection**(`group`, `name`, `callback`): [`ScriptConnection`](../interfaces/engine_api.ScriptConnection.md) \| `undefined`

Connects a specified Mixxx Control with a callback function, which is executed if the value of the control changes

This connection is unbuffered - when value change events occur faster, than the mapping can process them,
only the last value set for the control is processed.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "VuMeter" |
| `callback` | [`CoCallback`](engine_api.engine.md#cocallback) | JS function, which will be called every time, the value of the connected control changes. |

#### Returns

[`ScriptConnection`](../interfaces/engine_api.ScriptConnection.md) \| `undefined`

Returns script connection object on success, otherwise 'undefined''

#### Defined in

[engine-api.d.ts:129](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L129)

___

### reset

▸ **reset**(`group`, `name`): `void`

Resets the control to its default value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:83](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L83)

___

### scratchDisable

▸ **scratchDisable**(`deck`, `ramp?`): `void`

Jogwheel function to be called when scratching ends (usually when the wheel is released)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deck` | `number` | The deck number to use, e.g: 1 |
| `ramp?` | `boolean` | Set true to ramp the deck speed up. Set false to jump to normal play speed instantly [default = true] |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:210](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L210)

___

### scratchEnable

▸ **scratchEnable**(`deck`, `intervalsPerRev`, `rpm`, `alpha`, `beta`, `ramp?`): `void`

Jogwheel function to be called when scratching starts (usually when the wheel is touched)
This function contains an parametrizeable alpha-beta filter, which influences the
responsiveness and looseness of the imaginary slip mat

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deck` | `number` | The deck number to use, e.g: 1 |
| `intervalsPerRev` | `number` | The resolution of the MIDI control (in intervals per revolution) |
| `rpm` | `number` | The speed of the imaginary record at 0% pitch (in revolutions per minute (RPM) typically 33+1/3, adjust for comfort) |
| `alpha` | `number` | The alpha coefficient of the filter (start with 1/8 (0.125) and tune from there) |
| `beta` | `number` | The beta coefficient of the filter (start with alpha/32 and tune from there) |
| `ramp?` | `boolean` | Set true to ramp the deck speed down. Set false to stop instantly [default = true] |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:194](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L194)

___

### scratchTick

▸ **scratchTick**(`deck`, `interval`): `void`

Function to be called each time the jogwheel is moved during scratching

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deck` | `number` | The deck number to use, e.g: 1 |
| `interval` | `number` | The movement value (typically 1 for one "tick" forwards, -1 for one "tick" backwards) |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:202](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L202)

___

### setParameter

▸ **setParameter**(`group`, `name`, `newValue`): `void`

Sets the control value specified with normalized range of 0..1

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |
| `newValue` | `number` | Value to be set, normalized to a range of 0..1 |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:63](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L63)

___

### setValue

▸ **setValue**(`group`, `name`, `newValue`): `void`

Sets a control value

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |
| `newValue` | `number` | Value to be set (within it's range according Mixxx Controls manual page: https://manual.mixxx.org/latest/chapters/appendix/mixxx_controls.html) |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:45](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L45)

___

### softStart

▸ **softStart**(`deck`, `activate`, `factor?`): `void`

To achieve a forward acceleration effect from standstill to normal speed.
Both engine.softStart() and engine.brake()/engine.spinback() can interrupt each other.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deck` | `number` | The deck number to use, e.g: 1 |
| `activate` | `boolean` | Set true to activate, or false to disable |
| `factor?` | `number` | Defines how quickly the deck should come to normal playback rate. Start with a value of 1 and increase to increase the acceleration. SoftStart with low factors would take a while until sound is audible. [default = 1.0] |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:282](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L282)

___

### softTakeover

▸ **softTakeover**(`group`, `name`, `enable`): `void`

If enabled, soft-takeover prevents sudden wide parameter changes,
when on-screen control and hardware control divert.
With soft-takeover you need to turn a hardware knob, until it reaches
the position of the on-screen knob - than it takes over control.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "pregain" |
| `enable` | `boolean` | Set true to enable soft-takeover for the specified control |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:230](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L230)

___

### softTakeoverIgnoreNextValue

▸ **softTakeoverIgnoreNextValue**(`group`, `name`): `void`

Inhibits a sudden value change from the hardware control.
Should be called when receiving input for the knob/fader,
that switches its behavior (e.g. Shift-Button pressed)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "pregain" |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:240](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L240)

___

### spinback

▸ **spinback**(`deck`, `activate`, `factor?`, `rate?`): `void`

To achieve a spinback effect of the playback speed
Both engine.softStart() and engine.brake()/engine.spinback() can interrupt each other.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `deck` | `number` | The deck number to use, e.g: 1 |
| `activate` | `boolean` | Set true to activate, or false to disable |
| `factor?` | `number` | Defines how quickly the deck should come to normal playback rate. Start with a value of 1 and increase to increase the acceleration. Be aware that spinback called with low factors (about 0.5 and lower), would keep the deck running although the resulting very low sounds are not audible anymore. [default = 1.8] |
| `rate?` | `number` | The initial speed of the deck when enabled. "-10" (default) means 10x speed in reverse. Positive values like "10" also work, though then it's spinning forward obviously. [default = -10.0] |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:270](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L270)

___

### stopTimer

▸ **stopTimer**(`timerId`): `void`

Stops the specified timer

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `timerId` | `number` | ID of the timer |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:180](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L180)

___

### trigger

▸ **trigger**(`group`, `name`): `void`

Triggers the execution of all connected callback functions, with the actual value of a control.
Note: To trigger a single connection, use [trigger](../interfaces/engine_api.ScriptConnection.md#trigger) instead

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `group` | `string` | Group of the control e.g. "[Channel1]" |
| `name` | `string` | Name of the control e.g. "play_indicator" |

#### Returns

`void`

#### Defined in

[engine-api.d.ts:153](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/engine-api.d.ts#L153)
