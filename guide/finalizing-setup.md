---
title: Finalizing Setup
layout: single
sidebar:
  nav: "side"
---

We will now install SRLoader to the System Menu using TWLit, a program which can help us install .TIA files to the new SD NAND.

SRLoader is a homebrew application that can run homebrew and retail ROMs, and has several emulators built in.

## Downloads

- The latest release of [TWLit](/assets/files/TWLit.exe)
- The latest release of [SRLoader](https://github.com/Robz8/SRLoader/releases){:target="_blank"}
## Instructions

1. Copy `SRLoader.tia` from the SRLoader `.7z` file to a location on your PC
2. Insert your SD NAND (<2GB) SD card
3. Copy the `_nds` and `roms` folders from the SRLoader `.7z` file to the root of your SD card
4. Open TWLit
    - If TWLit does not launch, install the [Microsoft Visual C++ 2010 Redistributable Package](https://www.microsoft.com/en-us/download/details.aspx?id=5555){:target="_blank"}
5. Navigate to the **TIA Installer** tab
6. Press "Browse" on the **Input TIA** entry box
7. Navigate to the location of `SRLoader.tia`, select `SRLoader.tia`, and press **Open**
8. Press "Browse" on the **Install Dir** entry box
9. Navigate to your SD card, and press **Open**
10. (Optional) Input your system's Console ID in the **DSi Console ID** entry box
11. Press "Execute"
12. Close TWLit, unplug your SD card, and insert it in your DSi
13. Power on your system
14. "Unwrap" the new gift box by tapping on it
    - SRLoader should appear

SRLoader should now be on your System Menu, as any other DSiWare would be. With SRLoader, you can run homebrew and retail ROMs, and use the several emulators which are built into the software.
