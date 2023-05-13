[Documentation](../README.md) / [Modules](../modules.md) / [console-api](console_api.md) / console

# Namespace: console

[console-api](console_api.md).console

Mixxx installs the QJSEngine::ConsoleExtension for the use in controller mapping scripts.
See also:
 https://doc.qt.io/qt-5/qtquick-debugging.html#console-api
 https://developer.mozilla.org/en-US/docs/Web/API/console
 https://console.spec.whatwg.org/

## Table of contents

### Functions

- [assert](console_api.console.md#assert)
- [count](console_api.console.md#count)
- [debug](console_api.console.md#debug)
- [error](console_api.console.md#error)
- [exception](console_api.console.md#exception)
- [info](console_api.console.md#info)
- [log](console_api.console.md#log)
- [profile](console_api.console.md#profile)
- [profileEnd](console_api.console.md#profileend)
- [time](console_api.console.md#time)
- [timeEnd](console_api.console.md#timeend)
- [trace](console_api.console.md#trace)
- [warn](console_api.console.md#warn)

## Functions

### assert

▸ **assert**(`condition`, `...data`): `void`

Tests that a boolean expression is true,
if not, it writes an (optional) message to the console and prints the stack trace.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `condition` | `boolean` | If the condition is false, it prints message and stack trace |
| `...data` | `any`[] | Message to print - Either a list of objects whose string representations get concatenated into the message string - Or a string containing zero or more substitution strings followed by a list of objects to replace them |

#### Returns

`void`

#### Defined in

[console-api.d.ts:77](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L77)

___

### count

▸ **count**(`label?`): `void`

Prints the current number of times a particular piece of code has run, along with a message.

#### Parameters

| Name | Type |
| :------ | :------ |
| `label?` | `string` |

#### Returns

`void`

#### Defined in

[console-api.d.ts:113](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L113)

___

### debug

▸ **debug**(`...data`): `void`

Prints debugging information to the console, when
QT_LOGGING_RULES="js.debug=true;" or
Mixxx is started with --controller-debug
This function is identical to console.log

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `...data` | `any`[] | Message to print - Either a list of objects whose string representations get concatenated into the message string - Or a string containing zero or more substitution strings followed by a list of objects to replace them |

#### Returns

`void`

#### Defined in

[console-api.d.ts:33](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L33)

___

### error

▸ **error**(`...data`): `void`

Prints an error message to the console, when
QT_LOGGING_RULES="js.critical=true;" or
Mixxx is started with --controller-debug

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `...data` | `any`[] | Message to print - Either a list of objects whose string representations get concatenated into the message string - Or a string containing zero or more substitution strings followed by a list of objects to replace them |

#### Returns

`void`

#### Defined in

[console-api.d.ts:66](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L66)

___

### exception

▸ **exception**(`...data`): `void`

Prints an error message together with the stack trace of JavaScript execution at the point where it is called.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `...data` | `any`[] | Message to print - Either a list of objects whose string representations get concatenated into the message string - Or a string containing zero or more substitution strings followed by a list of objects to replace them |

#### Returns

`void`

#### Defined in

[console-api.d.ts:136](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L136)

___

### info

▸ **info**(`...data`): `void`

Prints information to the console, when
QT_LOGGING_RULES="js.info=true;" or
Mixxx is started with --controller-debug

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `...data` | `any`[] | Message to print - Either a list of objects whose string representations get concatenated into the message string - Or a string containing zero or more substitution strings followed by a list of objects to replace them |

#### Returns

`void`

#### Defined in

[console-api.d.ts:44](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L44)

___

### log

▸ **log**(`...data`): `void`

Prints debugging information to the console, when
QT_LOGGING_RULES="js.debug=true;" or
Mixxx is started with --controller-debug
This function is identical to console.debug

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `...data` | `any`[] | Message to print - Either a list of objects whose string representations get concatenated into the message string - Or a string containing zero or more substitution strings followed by a list of objects to replace them |

#### Returns

`void`

#### Defined in

[console-api.d.ts:21](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L21)

___

### profile

▸ **profile**(`label?`): `void`

Turns on the JavaScript profiler.

**`Deprecated`**

Not usable for controller mappings for now [see QTBUG-65419][https://bugreports.qt.io/browse/QTBUG-65419](https://bugreports.qt.io/browse/QTBUG-65419)

#### Parameters

| Name | Type |
| :------ | :------ |
| `label?` | `string` |

#### Returns

`void`

#### Defined in

[console-api.d.ts:120](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L120)

___

### profileEnd

▸ **profileEnd**(`label?`): `void`

Turns off the JavaScript profiler.

**`Deprecated`**

Not usable for controller mappings for now [see QTBUG-65419][https://bugreports.qt.io/browse/QTBUG-65419](https://bugreports.qt.io/browse/QTBUG-65419)

#### Parameters

| Name | Type |
| :------ | :------ |
| `label?` | `string` |

#### Returns

`void`

#### Defined in

[console-api.d.ts:127](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L127)

___

### time

▸ **time**(`label?`): `void`

Starts the time measurement, which will be printed by timeEnd

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `label?` | `string` | string argument that identifies the measurement. |

#### Returns

`void`

#### Defined in

[console-api.d.ts:84](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L84)

___

### timeEnd

▸ **timeEnd**(`label?`): `void`

Logs the time (in milliseconds) that was spent since the call of the time method.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `label?` | `string` | string argument that identifies the measurement. |

#### Returns

`void`

#### Defined in

[console-api.d.ts:90](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L90)

___

### trace

▸ **trace**(`...data`): `void`

Prints the stack trace of the JavaScript execution at the point where it was called.
This stack trace information contains the function name, file name, line number, and column number.
The stack trace is limited to last 10 stack frames.

Unfortunately this function does use the wrong logging category "default" instead of "js",
which is set when you start Mixxx with --controller-debug. Without setting logging category
"default" manually, you will not see any output.
[see QTBUG-108673][https://bugreports.qt.io/browse/QTBUG-108673](https://bugreports.qt.io/browse/QTBUG-108673)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `...data` | `any`[] | Message to print - Either a list of objects whose string representations get concatenated into the message string - Or a string containing zero or more substitution strings followed by a list of objects to replace them |

#### Returns

`void`

#### Defined in

[console-api.d.ts:106](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L106)

___

### warn

▸ **warn**(`...data`): `void`

Prints a warning message to the console, when
QT_LOGGING_RULES="js.warning=true;" or
Mixxx is started with --controller-debug

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `...data` | `any`[] | Message to print - Either a list of objects whose string representations get concatenated into the message string - Or a string containing zero or more substitution strings followed by a list of objects to replace them |

#### Returns

`void`

#### Defined in

[console-api.d.ts:55](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/console-api.d.ts#L55)
