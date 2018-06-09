---
title: Replacing the System Menu with SRLoader
layout: single
sidebar:
  nav: "side"
---

You will need [Unlaunch and HiyaCFW](/guide/installing-unlaunch/) installed before proceeding.
{: .notice--info}

Replacing the System Menu with SRLoader will allow for a few advantages over the built-in System Menu:
* SRLoader can allow for more DSiWare than the System Menu
* SRLoader, in many cases, can allow for SD cards greater than 2 GB to work
    - You can copy your entire SDNAND to a larger SD card once this process is done, and it will likely work out of the box
* SRLoader provides a unified interface for launching NES, GB(C), DS, and DSiWare titles

In this configuration, SRLoader is effectively acting as an open source alternative to the System Menu.

## Requirements
- The latest release of [SRLoader](https://github.com/Robz8/SRLoader/releases){:target="_blank"}
- The latest release of [Python 3](https://www.python.org/downloads/){:target="_blank"}
- [argvgen.py](/assets/files/argvgen.py)

## Preparation
If you already have SRLoader installed, skip to step 5
{: .notice--info}
1. Open the SRLoader `.7z` file
2. Copy *the contents of* the `CFW - SDNAND root` folder to the root of your SD card
3. Copy the `_nds` and `roms` folders to the root of your SD card
4. Copy *the contents of* the `DSiWare (your region)` folder to `_nds/srloader/dsiware` on your SD card
5. In the `Autoboot for HiyaCFW` folder in the SRLoader `.7z`, copy `autoboot.bin` to the `hiya` folder on your SD card
6. Navigate to the `shared1` folder on your SD card
7. Mark `TWLCFG0.dat` and `TWLCFG1.dat` as **read-only**
    - On Windows, this can be done by right clicking them, going to Properties, then checking "Read-only"
    - This works around a bug that can break the SDNAND
8. Navigate to `title/00030004` on your SD card
9. Copy `argvgen.py` to `title/00030004` on your SD card
10. Run `argvgen.py`
    - A new `dsiware` folder will be created
    - These contain `.argv` files, which tell SRLoader where it can find DSiWare
11. Move the `dsiware` folder to `_nds/srloader/dsiware` on your SD card
    - The two folders should be *merged*
12. Eject your SD card, and insert it in your DSi

## Instructions
1. Power on your DSi while holding **SELECT**
2. If `Autoboot title` is not checked, navigate to it and press **A**
3. Press **START** to save and continue booting
    - SRLoader will appear

SRLoader is now your System Menu.
You can press **DOWN** to access your DSiWare. Due to a limitation in EasyGL2D, the graphics library that SRLoader uses, some DSiWare images will be blank.