# Hercules DJ Console Mk2

The [Hercules](http://www.hercules.com/us/) PC DJ Consoles are a series
of USB DJ controllers for use with software such as Mixxx.

This page complements the general page about [Hercules
controllers](hercules) in this wiki.

## Drivers / Supportability

### What is the state of Hercules device support for the different Hercules DJ Consoles?

  - On Windows/OSX, you can use any of Mk1, MP3 Control, Mk2, RMX, DJ
    Steel Control via MIDI. 
  - On Linux, you can use most of the controllers, but some of them will
    require either the [Hercules Linux kernel
    module](hercules_linux_kernel_module) or the [user-mode
    driver](hercules_linux_usermode_driver). Others will work as an HID
    device directly.
  - These devices are remappable via the XML config files that
    correspond to their names. 
  - LED support works with scripts.

### Are Hercules devices USB-MIDI class compliant?

  - None of the Hercules devices from Mk1 to RMX are USB-MIDI class
    compliant, they require OS MIDI drivers, which are available for
    Windows, Linux and Mac OS X. Newer controllers from Hercules are USB
    MIDI class compliant though. See the tables on the [DJ Hardware
    Guide](hardware%20compatibility) for details.

### My Hercules Mk1/RMX doesn't work with Mixxx on Linux

  - If you have Linux you need the Hercules Linux driver installed. 
  - The Mk1 needs a modified dynamic kernel module for the Herc MIDI
    driver.

### Does the Joystick on the Mk1/Control MP3/Mk2 work in Mixxx?

  - The hercules joysticks are HID mice used to navigate library and
    playlists, they have been superseded by direction buttons on the RMX
    and DJ Steel controllers.
  - The joystick driver may mess with the MIDI driver.

## Hardware Models

Currently, there are multiple models supported in Mixxx. Check the
[hardware compatibility](hardware_compatibility) page, or the specific
controller pages that you can access from [Hercules wiki page on
Mixxx](hercules)
