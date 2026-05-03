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
| Bootloader | GRUB (custom styled) |
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
- [x] Compile GRUB from source
- [x] Create bootable disk image (boots into CLI via QEMU)
- [ ] Complete CS50 & obtain certificate
- [ ] Work through Nand2Tetris
- [ ] Assembly basics (x86, NASM)

### Phase 2 — First App
- [ ] Build file manager as a standalone Linux app
- [ ] Python + GTK as base
- [ ] Implement AI search (locally, SQLite + Embeddings)
- [ ] Publish on GitHub

### Phase 3 — Desktop Environment
- [ ] Develop Wayland compositor (wlroots as base)
- [ ] Custom GUI components (taskbar, app launcher)
- [ ] Dark/light mode + animation system

### Phase 4 — Custom Distro
- [ ] Use Debian as base
- [ ] Integrate custom components
- [ ] Style GRUB individually
- [ ] Create ISO image

## Current Status

GRUB compiled from source, bootable ISO created, boots into Alpine Linux CLI via QEMU on macOS M4.

## Resources

| Resource | Purpose |
|---|---|
| [osdev.org](https://osdev.org) | OS development bible |
| [Writing a Simple OS from Scratch](https://www.cs.bham.ac.uk/~exr/lectures/opsys/10_11/lectures/os-dev.pdf) | OS entry point |
| [wlroots Documentation](https://gitlab.freedesktop.org/wlroots/wlroots) | Wayland compositor |
| [GTK Documentation](https://docs.gtk.org) | GUI with C/Python |
