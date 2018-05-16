---
title: Using SRLoader
layout: single
sidebar:
  nav: "side"
---

nds-bootstrap is currently a proof-of-concept, and is far from complete. Expect long loading times and compatibility issues. It is highly recommended that you check and bookmark the [compatibility chart](https://docs.google.com/spreadsheets/d/1M7MxYQzVhb4604esdvo57a7crSvbGzFIdotLW0bm0Co/edit#gid=0){:target="_blank"}.
{: .notice--info}

SRLoader is a homebrew application that will allow you to run homebrew applications, as well as commercial ROMs using [nds-bootstrap](https://github.com/ahezard/nds-bootstrap){:target="_blank"}. SRLoader also has various emulators built in, as well as a GBA runner, which will let you run Gameboy Color, NES and GBA ROMs.

You can learn more about SRLoader [here](https://gbatemp.net/threads/srloader-gui-for-flashcards-also-a-nds-app-for-dsi.472200/){:target="_blank"}.

## Downloads

- The latest release of [SRLoader](https://github.com/Robz8/SRLoader/releases)

## Installation
1. Insert your system's SD card into your computer
2. Copy the contents of the twlnf `.7z` file to the root of your SD card
  - If prompted to replace boot.nds, say yes
3. Copy ROMs to their respective folders
  - Place Gameboy roms in `/roms/gb`
  - Place NDS roms in `/roms/nds`
  - Place NES roms in `/roms/nes`
  - For GBA, make a folder in `roms` named `gba` and place roms there
  - GBA requires a copy of the GBA BIOS named `bios.bin` on the root of your SD card, and currently has no saving support

## Usage
1. Launch SRLoader using your homebrew entrypoint of choice
2. You will now see a list of your NDS ROMs
  - Press **Y** to launch homebrew applications without nds-bootstrap
  - Press **A** to launch commercial/homebrew ROMs using nds-bootstrap (Homebrew with DSi-extended header will not be ran by bootstrap)
  - Press **SELECT** to set a donor ROM when the compatibility list asks for one
  - Press **UP** or **DOWN** to toggle between NDS ROMs and DSiWare
  - Press **START**, then navigate to **Start GBARunner2** to run GBA ROMs
  - Press **B** to return to the DSi Menu
