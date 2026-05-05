# Reloop Digital Jockey 2 Master Edition

![http://www.reloop.com/media/catalog/product/cache/9/thumbnail/9df78eab33525d08d6e5fb8d27136e95/2/2/4/224093_Reloop_TP.png](http://www.reloop.com/media/catalog/product/cache/9/thumbnail/9df78eab33525d08d6e5fb8d27136e95/2/2/4/224093_Reloop_TP.png)

- [Manufacturer’s product page](http://www.reloop.com/reloop-digital-jockey-2-me)
- [Forum thread](https://mixxx.discourse.group/t/help-reloop-digital-jockey-2-master-edition/12583)

:::{versionadded} 1.8
:::

:::{warning}
This device is not USB {term}`MIDI` class compliant.
Its signals are translated to {term}`MIDI` by special drivers on Windows and macOS.
There is no driver available for Linux.
:::

:::{note}
Unfortunately a detailed description of this controller mapping is still missing.
If you own this controller, please consider
[contributing one](https://github.com/mixxxdj/mixxx/wiki/Contributing-Mappings#user-content-documenting-the-mapping).
:::

## Linux Support

**The Reloop Digital Jockey 2 Master Edition is not supported on Linux as of 7/2012.**

The device is not reported as a class-compliant MIDI device so it requires a driver on Linux.

`lsusb -v` dump:

```text
    Bus 002 Device 003: ID 200c:1009
    Device Descriptor:
      bLength                18
      bDescriptorType         1
      bcdUSB               2.00
      bDeviceClass          255 Vendor Specific Class
      bDeviceSubClass       255 Vendor Specific Subclass
      bDeviceProtocol       255 Vendor Specific Protocol
      bMaxPacketSize0        64
      idVendor           0x200c
      idProduct          0x1009
      bcdDevice            1.00
      iManufacturer           1 reloop
      iProduct                2 Digital Jockey2 Master Edition
      iSerial                 3 no serial number
      bNumConfigurations      1
      Configuration Descriptor:
        bLength                 9
        bDescriptorType         2
        wTotalLength           73
        bNumInterfaces          2
        bConfigurationValue     1
        iConfiguration          0
        bmAttributes         0xc0
          Self Powered
        MaxPower                0mA
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        0
          bAlternateSetting       0
          bNumEndpoints           0
          bInterfaceClass       255 Vendor Specific Class
          bInterfaceSubClass      0
          bInterfaceProtocol      0
          iInterface              0
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        0
          bAlternateSetting       1
          bNumEndpoints           3
          bInterfaceClass       255 Vendor Specific Class
          bInterfaceSubClass      0
          bInterfaceProtocol      0
          iInterface              0
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x02  EP 2 OUT
            bmAttributes            5
              Transfer Type            Isochronous
              Synch Type               Asynchronous
              Usage Type               Data
            wMaxPacketSize     0x0004  1x 4 bytes
            bInterval               1
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x83  EP 3 IN
            bmAttributes            2
              Transfer Type            Bulk
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0200  1x 512 bytes
            bInterval               1
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x05  EP 5 OUT
            bmAttributes            2
              Transfer Type            Bulk
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0200  1x 512 bytes
            bInterval               1
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       0
          bNumEndpoints           0
          bInterfaceClass       255 Vendor Specific Class
          bInterfaceSubClass      0
          bInterfaceProtocol      0
          iInterface              0
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       1
          bNumEndpoints           1
          bInterfaceClass       255 Vendor Specific Class
          bInterfaceSubClass      0
          bInterfaceProtocol      0
          iInterface              0
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x86  EP 6 IN
            bmAttributes            2
              Transfer Type            Bulk
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0200  1x 512 bytes
            bInterval               1
      Device Qualifier (for other device speed):
        bLength                10
        bDescriptorType         6
        bcdUSB               2.00
        bDeviceClass          255 Vendor Specific Class
        bDeviceSubClass       255 Vendor Specific Subclass
        bDeviceProtocol       255 Vendor Specific Protocol
        bMaxPacketSize0        64
        bNumConfigurations      1
      Device Status:     0x0000
        (Bus Powered)
```
