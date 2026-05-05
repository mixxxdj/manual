# Hercules Linux kernel module

Hercules released a linux driver for the MIDI part of their DJ consoles
and controllers. Since it's been outdated by newer kernel versions,
community members are now maintaining it, so it works also in newer
kernel versions.

\*\* Note: This module supports only the following models: \*\*

  - DJ Console MK1
  - DJ Console MK2
  - DJ Console Rmx
  - DJ Console Steel

Also, you don't need this kernel if you just want to use them with
recent Mixxx versions, because they are supported with HID mappings,
which communicate directly with the controller.

## Ubuntu PPA

<https://launchpad.net/~rojtberg/+archive/hdjmod>

There are builds for Ubuntu 12.04, 14.04, 14.10, 15.04, 15.10, 16.04,
16.10 and 17.04:

You can get it using the following instructions:

  - sudo add-apt-repository ppa:rojtberg/hdjmod
  - sudo apt-get update
  - sudo apt-get install hdjmod-dkms
  - sudo modprobe hdj\_mod

## lightrush fork

There was a fork of the previous repository that fixed some problems
with versions 10.04 and 10.10 of Ubuntu. These are no longer needed
because rojtberg repository was updated and is currently more up to
date:

You will find here some instructions on how to install the control
panel, so here it is.

<https://sites.google.com/site/lightrush/random-1/herculesdjconsoleonkernel2635orubuntumaverick>.

## Package dkms

Another old source of this kernel is here:

<http://slist.lilotux.net/linux/deejay/mixxx/>

## Related pages

[Hercules/Guillemot DJ Console Series Controllers](hercules)

[](hercules_pc_dj_console)

[Linux user mode driver](hercules_linux_usermode_driver)

[Old forum thread talking about this kernel
module](http://mixxx.org/forums/viewtopic.php?f=1&t=851)
