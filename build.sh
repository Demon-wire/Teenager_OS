#!/bin/bash
set -e

echo "🔨 Building Teenager OS ISO..."

# Build Limine tool
echo "→ Building Limine..."
make -C limine

# Build ISO
echo "→ Creating ISO..."
xorriso -as mkisofs -R -r -J \
    -b boot/limine/limine-bios-cd.bin \
    -no-emul-boot -boot-load-size 4 -boot-info-table \
    -hfsplus -apm-block-size 2048 \
    --efi-boot boot/limine/limine-uefi-cd.bin \
    -efi-boot-part --efi-boot-image --protective-msdos-label \
    iso_root -o teenager-os.iso

# Install Limine BIOS boot sector
echo "→ Installing Limine..."
limine/limine bios-install teenager-os.iso

echo "✅ Done! Run ./start.sh to boot."
