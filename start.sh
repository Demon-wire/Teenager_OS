#!/bin/bash
/opt/homebrew/bin/qemu-system-x86_64 \
    -cdrom ~/Documents/Programmieren/OS/teenager-os.iso \
    -m 512M -display cocoa -net none -no-reboot
