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
- An SD card that is 2GB or smaller, or a larger SD card that is partitioned to be 2GB or smaller
  - If you don't have a 2GB or smaller SD card, follow [Replacing the System Menu with DSiMenu++](/more/replacing-system-menu) once you are finished with this page
- The latest release of [twlnf](https://github.com/Jimmy-Z/twlnf/releases){:target="_blank"}
- The latest release of [HiyaCFW](https://github.com/Robz8/hiyaCFW/releases){:target="_blank"}
- [NUSDownloader](/assets/files/NUSDownloader.zip)
- A NAND backup taken from your device, with the NO$GBA Footer
  - twlnf will create this footer automatically when it makes a backup
  - You should already have this backup from the previous section
- HiyaCFW Helper
  - [.EXE for Windows](/assets/files/hiyacfw_helper.exe)
  - [.py for Others (requires Python 3.6)](/assets/files/hiyacfw_helper.py)

## Preparation
1. Insert your SDNAND SD card into your PC
2. Copy *the contents of* the NUSDownloader `.zip` file to a folder on your PC
3. Copy *the contents of* the HiyaCFW `.7z` file to a folder on your PC
4. Copy the HiyaCFW Helper file to the `for PC` folder in your HiyaCFW folder
5. Copy *the contents of* the twlnf `.7z` file to the root of your SD card, and rename `twlnf.nds` to `bootcode.dsi`
8. Open NUSDownloader on your computer
  - This can be done through [Mono](http://www.mono-project.com/) on Mac/Linux/*nix systems
9. Check the "Create Decrypted Contents (*.app)" box, and uncheck the "Keep Enc. Contents" box
10. Select **Database > System (DSi) > System Menu (Launcher) > [Your Region] > v512 > Start NUS Download!**
11. Exit NUS Downloader
12. Navigate to **titles > 00030017484e41XX > 512** in your NUS Downloader directory
13. Copy `00000002.app` from the `512` folder to the HiyaCFW `for PC` folder
14. Copy your valid NAND backup (`nand.bin`) to the HiyaCFW `for PC` folder

## Instructions
1. Insert your SD card into your system
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
8. Insert your SD card into your PC
9. Move all files from the `dump` directory to the root of the SD card
  - This prepares the "SD NAND",  which HiyaCFW will boot from
10. Navigate to the HiyaCFW `for PC` folder
11. Run `hiyacfw_helper.exe` to prepare modifications
  - Non-Windows systems can use the `.py` file, which will require [Python 3](https://www.python.org/downloads/){:target="_blank"} and [WINE](https://www.winehq.org/){:target="_blank"}
12. Copy *the contents of* the HiyaCFW `for SDNAND SD card` folder to the root of your SD card
  - If asked to replace any files, do so
1. Open the new `Modified Files` folder
2. Copy `bootloader.nds` to the `hiya` folder on your SD card
3. Copy 00000002.app to **title > 00030017 > 484e41XX > content** folder on your SD card
  - XX denotes your region: 45 for USA, 50 for EUR, 4A for JAP, 55 for AUS
4. Unplug your SD card, and insert it in your DSi
5. Power on your console
  - HiyaCFW's splash screen should appear
  - If it does not, it's most likely because your SD card is larger than 4GB; follow [Replacing the System Menu with DSiMenu++](/more/replacing-system-menu) as noted at the top of the page

Your system will now boot from the SD card instead of the internal NAND.

[Finalizing Setup](/guide/finalizing-setup){: .btn .btn--light-outline}
{: style="text-align: center;"}
