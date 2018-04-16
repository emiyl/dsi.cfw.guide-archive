---
title: Installing Sudokuhax
layout: single
sidebar:
  nav: "side"
---

sudokuhax is an exploit of the Sudoku DSiWare game, allowing us to launch the Homebrew Launcher seconds after starting the application.

This guide currently only supports USA consoles.
{: .notice style="background-color: #87625a; font-weight: bold;"}

Make sure you have at least 30 blocks of space on your console's internal storage, or you will brick your device.
{: .notice style="background-color: #7e4d57; font-weight: bold;"}

## Launching twlnf

1. Open the Flipnote Studio application
  - Ensure that the *booting to Calendar mode* is disabled in Flipnote Studio's settings
2. Select **View Flipnote > SD Card > Select Folder > User > ugopwn**
3. Click on the note with the red bottom half
4. Select "Edit"
5. Click on the Flipnote frog icon in the bottom left
6. Click on the film roll icon
7. Select **Copy > Back > Exit**
8. Click on the Flipnote frog icon in the bottom left
8. Click on the film roll icon.
9. Click on the single right arrow (the next to last arrow icon) two times
  - You will see a new frame be created
10. Click on the paste button exactly 122 times.
11. Select "Erase" and then "Paste"
  - This should launch twlnf

## Installing Sudokuhax

1. If prompted in twlnf, press **A** to create a NAND backup
  - This may take a few minutes
  - Store this NAND backup in a safe location, it is a critical backup
2. Press **X** to mount the NAND directly
  - twlnf does not list this as an option
3. Open the `sudoku/content` folder
4. Navigate to `title.tmd`
5. Press **A** to install the application to NAND
6. Once finished, press **Select** to quit twlnf
7. Press **A** to confirm
  - Your console will power off

## Launching sudokuhax

1. Power on your console
2. Tap the new gift box on your Home Menu to "unwrap" Sudoku
3. Open the application
4. Wait for the ESRB and EA screens to pass
5. When prompted, touch the screen to load the entrypoint

<<<<<<< HEAD
Sudokuhax will load whatever homebrew you have on your SD card as `boot.nds`. Currently, this is twlnf. It is recommended that you install SRLoader, as it can launch both commercial ROMs and homebrew, and has several emulators built in.
=======
Sudokuhax will load whatever homebrew you have on your SD card as `boot.nds`. Currently, this is twlnf. It is recommended that you install SRLoader, as it can launch both commercial ROMs and homebrew, and has several emulators built in.

It is recommended that you backup the `nand.bin` file created on your SD card to somewhere safe on your computer.
>>>>>>> 89272d9990c1f75f41a3b6d938c888bbfb5e454f
