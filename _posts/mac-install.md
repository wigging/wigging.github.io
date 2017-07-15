# macOS Installation

To create a bootable installer on an external USB drive:
https://support.apple.com/en-us/HT201372

To boot from an external drive, hold down the `Option` key during start up. If
using a Windows keyboard, the `Alt` key is equivalent to the option key.

# Before selling your Mac

Perform the following steps before selling your Mac:
https://support.apple.com/en-us/HT201065

# Create a live USB to install Ubuntu

Plugin the USB stick and format it using "Disk Utility". For example, to
prepare a bootable USB of Ubuntu, format the drive as FAT.

<img src="images/diskutility.png" width="600">

Now find what "/dev/diskN" the USB stick is mapped to by opening Terminal
(where "N" stands for "disk0", "disk1", "disk2" etc) and execute:

```bash
diskutil list
```

After getting the diskN name, unmount the USB disk with:

```bash
diskutil unmountDisk /dev/diskN
```

Finally write the ISO to the USB stick to create the bootable drive. This can
take several minutes depending on the size of the ISO file. For example, write
the `demo.iso` to a USB drive listed as `/dev/disk2` (note the `r` prepended to
`disk2`):

```bash
sudo dd if=/location/of/demo.iso of=/dev/rdisk2 bs=1m
```

Once the formatting is complete, the USB drive can be ejected:

```bash
diskutil eject /dev/disk2
```


