# Pioneer DDJ-RB

[Manufacturer's product
page](http://www.pioneerdj.com/en/product/controller/ddj-rb/)

The Pioneer DDJ-RB is a USB controller with a built in sound card. It is
a class compliant HID but the sound card is proprietary.

## Drivers

### Windows & MacOS

You can download the latest drivers and firmware from
<https://www.pioneerdj.com/en/support/software/DDJ-RB/>.

### Linux

The sound card is proprietary and there are **no drivers available for
Linux**. The HID, however, can be used after adding the following udev
rule (eg. to /etc/udev/rules.d/mixxx.usb.rules )

`SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ATTRS{idVendor}=="2b73",
GROUP="users", MODE="0660"`

## Mapping

There is a preliminary mapping at
<https://github.com/jbramsden/DDJ-RB-MIXXX> which could be used as a
starting point. Failing that, check out
[DDJ-SB2](https://www.mixxx.org/wiki/doku.php/pioneer_ddj-sb2) as well
([Forum
link](https://www.mixxx.org/forums/viewtopic.php?f=3&t=9464#p34297))
