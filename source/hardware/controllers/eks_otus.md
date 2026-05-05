# EKS Otus


This controller has been discontinued as EKS is went out of business.

![http://one.dj/eks-legacy/EKS-DOWNLOADS\_files/otus.jpg](http://one.dj/eks-legacy/EKS-DOWNLOADS_files/otus.jpg)

:::{versionadded} 1.11
:::
:::{note}
Unfortunately a detailed description of this controller mapping is still missing.
If you own this controller, please consider
[contributing one](https://github.com/mixxxdj/mixxx/wiki/Contributing-Mappings#user-content-documenting-the-mapping).
:::

## Linux

### Set udev permissions

1.  Create/edit `/etc/udev/rules.d/10-local.rules`
2.  Add the line `KERNEL="hiddev*", NAME="usb/%k", GROUP="plugdev"`
3.  Make sure your user account is a member of plugdev: `sudo usermod $USER -a -G plugdev`
4.  Reload udev: `sudo /etc/init.d/udev reload`
5.  Now plug in the controller and start Mixxx.
