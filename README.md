# Teenager OS

A youth-friendly Linux-based operating system with modern aesthetics, an AI-powered file manager, and an intuitive user interface.

## Vision

Existing Linux distributions are primarily aimed at experienced users and developers. Teenager OS addresses this with a clearly defined, youth-oriented alternative featuring a modern UI and AI integration.

| Problem | Solution |
|---|---|
| Linux distros are visually outdated and complex | Custom desktop environment built on Wayland with a modern design system |
| File managers are based on outdated folder structures | AI-powered file manager with semantic search and automatic organization |
| Teenagers find no intuitive entry point into Linux | OS specifically designed for this target group, with onboarding and clear UX |

## Technical Stack

| Component | Decision |
|---|---|
| Kernel | Linux Kernel |
| Bootloader | Limine (custom styled) |
| Display System | Wayland |
| Package Manager | APT (Debian-based) |
| GUI Language | C/C++ + Python (tools & AI) |
| Languages | German + English |

## Design

- **Dark Mode** — default, modern, easy on the eyes
- **Light Mode** — optional, switchable
- Smooth animations & transitions
- Inspired by: Arc Browser, Linear.app, Pop!\_OS, elementaryOS

## AI File Manager

The centerpiece of the OS — a completely new approach to file management.

- **Smart Search** — search by file content, natural language queries
- **AI Auto-Organization** — recognizes file contents, suggests folder structures
- **Predictive Access** — learns user habits, surfaces relevant files at the right time

## Roadmap

### Phase 1 — Foundations *(current)*
- [x] Set up Limine bootloader (pre-built binaries, v8.x)
- [x] Create bootable ISO (boots Alpine Linux CLI via QEMU with Limine)
- [x] Custom Limine theme (dark mode, Catppuccin colors, wallpaper)
- [ ] Boot into a minimal Linux CLI environment

### Phase 2 — AI File Manager
- [ ] Build file manager as a standalone Linux app (Python + GTK)
- [ ] Implement smart search (SQLite + local embeddings)
- [ ] AI auto-organization (file content recognition)
- [ ] Predictive file access based on user habits

### Phase 3 — Desktop Environment
- [ ] Wayland compositor (wlroots as base)
- [ ] Taskbar and app launcher
- [ ] Dark / light mode
- [ ] Animation system

### Phase 4 — Custom Distro
- [ ] Debian as base system
- [ ] Integrate all custom components
- [ ] Custom GRUB styling
- [ ] Bootable ISO image

## Current Status

Limine bootloader configured, bootable ISO created (`teenager-os.iso`), boots into Alpine Linux CLI via QEMU on macOS M4.

## Resources

| Resource | Purpose |
|---|---|
| [osdev.org](https://osdev.org) | OS development bible |
| [Writing a Simple OS from Scratch](https://www.cs.bham.ac.uk/~exr/lectures/opsys/10_11/lectures/os-dev.pdf) | OS entry point |
| [wlroots Documentation](https://gitlab.freedesktop.org/wlroots/wlroots) | Wayland compositor |
| [GTK Documentation](https://docs.gtk.org) | GUI with C/Python |
