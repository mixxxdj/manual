### Linux User-mode Driver for Hercules controllers

Aside of the [Hercules Linux kernel
module](hercules_linux_kernel_module), there also exists another driver
developed by Neale Pickett and available [on
GitHub](https://github.com/nealey/hdjd), that allows the controllers to
be seen as MIDI devices.

This driver can be executed as an application by the user, and supports
the MIDI mapping the following controllers:

  - Hercules DJ Control Steel
  - Hercules DJ Control MP3e2
  - Hercules DJ Control Hercules MP3 LE / Glow
  - Hercules DJ Control Hercules Mk4 (Since November 2017)
  - Hercules DJ Control Hercules Mk2
  - Hercules DJ Control 4-Mx

In order to use it, you need to download the source, and compile it
simply executing `make`. Once compiled, it can be executed as ./hdjd and
it will tell the controller that it has detected and if there is any
problem in using it.

If you are told that the controller cannot be accessed, you can follow
the instructions to allow read and write permissions to devices. See
details at this page:
<http://www.mixxx.org/wiki/doku.php/troubleshooting>
