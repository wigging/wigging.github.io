---
title: Essential Linux
date: 2017-09-23
layout: article
---

# Ubuntu installation

Notes on installing the Ubuntu distribution of Linux are provided below.

## General notes

The long-term support (LTS) version of Ubuntu is the recommended version to
install. To download the latest desktop version of Ubuntu visit:

https://www.ubuntu.com/download/desktop

Prepare the USB stick with Disk Utility on the Mac by formatting it as MS-DOS
(FAT) where the scheme is GUID Partition Map.

Next, to create a bootable USB stick on a Mac, follow these instructions:

https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx

Place the bootable USB into the new computer. Turn on the computer then boot
from the USB stick via the BIOS. Follow the on screen instructions to install
Ubuntu.

Note that the bootloader must be installed on `/dev/nvme0n1` for the Samsung
950 Pro M.2 NVMe SSD.

After installation, connect to the internet and run the Software Updater to
install system updates.

## NVIDIA drivers

In System Settings make sure the NVIDIA driver is selected. Then restart the
system to support the 4K display.

In System Settings set the scaling for the Display to `2` for larger icon and
font sizes.

Check NVIDIA settings with terminal command `nvidia-settings`.

