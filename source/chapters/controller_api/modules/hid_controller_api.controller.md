[Documentation](../README.md) / [Modules](../modules.md) / [hid-controller-api](hid_controller_api.md) / controller

# Namespace: controller

[hid-controller-api](hid_controller_api.md).controller

HidControllerJSProxy

## Table of contents

### Functions

- [getFeatureReport](hid_controller_api.controller.md#getfeaturereport)
- [getInputReport](hid_controller_api.controller.md#getinputreport)
- [send](hid_controller_api.controller.md#send)
- [sendFeatureReport](hid_controller_api.controller.md#sendfeaturereport)
- [sendOutputReport](hid_controller_api.controller.md#sendoutputreport)

## Functions

### getFeatureReport

▸ **getFeatureReport**(`reportID`): `ArrayBuffer`

getFeatureReport receives a FeatureReport from the HID device on request.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `reportID` | `number` | 1...255 for HID devices that uses ReportIDs - or 0 for devices, which don't use |

#### Returns

`ArrayBuffer`

The returned array matches the input format of sendFeatureReport,
         allowing it to be read, modified and sent it back to the controller.

#### Defined in

[hid-controller-api.d.ts:61](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/hid-controller-api.d.ts#L61)

___

### getInputReport

▸ **getInputReport**(`reportID`): `ArrayBuffer`

getInputReport receives an InputReport from the HID device on request.

This can be used on startup to initialize the knob positions in Mixxx
to the physical position of the hardware knobs on the controller.
This is an optional command in the HID standard - not all devices support it.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `reportID` | `number` | 1...255 for HID devices that uses ReportIDs - or 0 for devices, which don't use |

#### Returns

`ArrayBuffer`

Returns report data with ReportID byte as prefix

#### Defined in

[hid-controller-api.d.ts:44](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/hid-controller-api.d.ts#L44)

___

### send

▸ **send**(`dataList`, `length?`): `void`

Sends HID OutputReport with hard coded ReportID 0 to HID device

This function only works with HID devices, which don't use ReportIDs

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `dataList` | `number`[] | Data to send as list of bytes |
| `length?` | `number` | Unused but mandatory argument for backwards compatibility |

#### Returns

`void`

#### Defined in

[hid-controller-api.d.ts:13](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/hid-controller-api.d.ts#L13)

▸ **send**(`dataList`, `length`, `reportID`, `resendUnchangedReport?`): `void`

Sends HID OutputReport to HID device

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `dataList` | `number`[] | Data to send as list of bytes |
| `length` | `number` | Unused but mandatory argument for backwards compatibility |
| `reportID` | `number` | 1...255 for HID devices that uses ReportIDs - or 0 for devices, which don't use ReportIDs |
| `resendUnchangedReport?` | `boolean` | If set, the report will also be send, if the data are unchanged since last sending [default = false] |

#### Returns

`void`

#### Defined in

[hid-controller-api.d.ts:23](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/hid-controller-api.d.ts#L23)

___

### sendFeatureReport

▸ **sendFeatureReport**(`reportID`, `reportData`): `void`

Sends a FeatureReport to HID device

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `reportID` | `number` | 1...255 for HID devices that uses ReportIDs - or 0 for devices, which don't use |
| `reportData` | `ArrayBuffer` | Data to send as byte array |

#### Returns

`void`

#### Defined in

[hid-controller-api.d.ts:52](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/hid-controller-api.d.ts#L52)

___

### sendOutputReport

▸ **sendOutputReport**(`reportID`, `dataArray`, `resendUnchangedReport?`): `void`

Sends an OutputReport to HID device

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `reportID` | `number` | 1...255 for HID devices that uses ReportIDs - or 0 for devices, which don't use ReportIDs |
| `dataArray` | `ArrayBuffer` | Data to send as byte array |
| `resendUnchangedReport?` | `boolean` | If set, the report will also be send, if the data are unchanged since last sending [default = false] |

#### Returns

`void`

#### Defined in

[hid-controller-api.d.ts:32](https://github.com/JoergAtGithub/mixxx/blob/8d2d71e396/res/controllers/hid-controller-api.d.ts#L32)
