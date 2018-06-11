---
title: Finalizing Setup
layout: single
sidebar:
  nav: "side"
---

We will now install DSiMenu++ to the System Menu by copying it to your SD card.

SDSiMenu++ is a homebrew application that can launch homebrew and retail ROMs, and has several emulators built in.

## Downloads

- The latest release of [DSiMenu++](https://github.com/Robz8/DSiMenuPlusPlus/releases){:target="_blank"}

## Instructions

1. Insert your SD NAND (<2GB) SD card into your PC
2. Copy *the contents of* `CFW - SDNAND root` from the DSiMenu++ `.7z` file to the root of your SD NAND (<2GB) SD card
3. Copy the `_nds` and `roms` folders from the DSiMenu++ `.7z` file to the root of your SD card
4. Unplug your SD card, and insert it in your DSi
5. Power on your system
6. "Unwrap" the new gift box by tapping on it
    - DSiMenu++ should appear

SRLoader should now be on your System Menu, as any other DSiWare would be. With SRLoader, you can run homebrew and retail ROMs, and use the several emulators which are built into the software.

## Usage

1. Copy ROMs to their respective folders
  - Place Gameboy roms in `/roms/gb`
  - Place NDS roms in `/roms/nds`
  - Place NES roms in `/roms/nes`
  - For GBA, make a folder in `roms` named `gba` and place roms there
  - GBA requires a copy of the GBA BIOS named `bios.bin` on the root of your SD card, and currently has no saving support
2. Launch DSiMenu++ from the Home Menu
3. You will now see a list of your NDS ROMs
  - Press **Y** to launch homebrew applications without nds-bootstrap
  - Press **A** to launch commercial/homebrew ROMs using nds-bootstrap (Homebrew with DSi-extended header will not be ran by bootstrap)
  - Press **SELECT** to set a donor ROM when the compatibility list asks for one
  - Press **UP** or **DOWN** to toggle between NDS ROMs and DSiWare
  - Press **START**, then navigate to **Start GBARunner2** to run GBA ROMs
  - Press **X** in the DSi/3DS theme's START menu, to return to the DSi Menu
4. (optional) You can have DSiMenu++ as a DSi Menu replacement
  - [Replacing System Menu](/more/replacing-system-menu.md)