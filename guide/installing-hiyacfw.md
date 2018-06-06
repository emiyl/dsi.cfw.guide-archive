---
title: Installing HiyaCFW
layout: single
sidebar:
  nav: "side"
---

You will need [Unlaunch](/guide/installing-unlaunch/) installed before proceeding.
{: .notice--info}

Do not system update after installing HiyaCFW. This will remove HiyaCFW's SD patches.
{: .notice--danger}

HiyaCFW is a custom firmware for the Nintendo DSi that, once installed, will allow:
- Booting the system from SD card
- Installing homebrew applications to the Home Menu
- Launching blocked flashcards on later versions

## Requirements
- The latest release of [Python 3](https://www.python.org/downloads/){:target="_blank"}
  - You should already have this from previous section
- An SD card that is 2GB or smaller, or a larger SD card that is partitioned to be 2GB or smaller
- The latest release of [twlnf](https://github.com/Jimmy-Z/twlnf/releases){:target="_blank"}
- [NUSDownloader](/assets/files/NUSDownloader.zip)
- A NAND backup taken from your device, with the NO$GBA Footer
  - twlnf will create this footer automatically when it makes a backup
  - You should already have this backup from the previous section
- [Helper scripts for HiyaCFW installation](/assets/files/hiyacfw_helper.zip)

## Preparation
1. Insert your <2GB SD card into your PC
2. Copy *the contents of* the NUSDownloader `.zip` file to a folder on your PC
3. Copy *the contents of* the HiyaCFW `.7z` file to a folder on your PC
4. Copy *the contents of* the HiyaCFW helper `.7z` to the `for PC` folder in your HiyaCFW folder
5. Copy *the contents of* the twlnf `.7z` file to the root of your <2GB SD card, and rename `twlnf.nds` to `bootcode.dsi`
6. Copy `console_id.txt` from the root of your normal SD card to the root of your <2GB SD card
  - Of course, this only applies if your <2GB SD card is not your normal one
7. Copy `nand.bin` and `nand.bin.sha` from the root of your normal SD card to the root of your <2GB SD card
8. Open NUSDownloader on your computer
  - This can be done through [Mono](http://www.mono-project.com/) on Mac/Linux/*nix systems
9. Check the "Create Decrypted Contents (*.app)" box, and uncheck the "Keep Enc. Contents" box
10. Select **Database > System (DSi) > System Menu (Launcher) > [Your Region] > v512 > Start NUS Download!**
11. Exit NUS Downloader
12. Navigate to **titles > 00030017484e41XX > 512** in your NUS Downloader directory
13. Copy `00000002.app` from the `512` folder to the HiyaCFW `for PC` folder
14. Copy your valid NAND backup (`nand.bin`) to the HiyaCFW `for PC` folder

## Instructions
1. Insert your <2GB SD card into your system
2. Power on your DSi
  - twlnf will appear
3. Press **X** to mount the system NAND directly
4. Press **START** to open twlnf's menu
5. Press **R** to dump the NAND contents to your SD card
  - This will take several minutes
  - Keep your system plugged in during this process, to avoid sudden power loss
  - When `walk returned 0` appears, the process is complete
6. Once finished, press **Select** to quit twlnf
7. Press **A** to confirm
  - Your console will power off
8. Insert your <2GB SD card into your PC
9. Move all files from the `dump` directory to the root of the SD card
  - This prepares the "SD NAND",  which HiyaCFW will boot from
10. Navigate to the HiyaCFW `for PC` folder
11. Run `hiyacfw_helper.py` to prepare modifications
  - This script requires [WINE](https://www.winehq.org/){:target="_blank"} on Mac/Linux/*nix systems
12. Copy *the contents of* the HiyaCFW `for 2GB (or lower) SD card (SDNAND)` folder to the root of your <2GB SD card
  - If asked to replace any files, do so
1. Open the new `Modified Files` folder
2. Copy `bootloader.nds` to the `hiya` folder on your <2GB SD card
3. Copy 00000002.app to **title > 00030017 > 484e41XX > content** folder on your <2GB SD card
  - XX denotes your region: 45 for USA, 50 for EUR, 4A for JAP, 55 for AUS
4. Unplug your <2GB SD card, and insert it in your DSi
5. Power on your console
  - HiyaCFW's splash screen should appear

Your system should now boot from the SD card instead of the internal NAND.

[Finalizing Setup](/guide/finalizing-setup){: .btn .btn--light-outline}
{: style="text-align: center;"}
