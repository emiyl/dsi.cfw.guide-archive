---
title: Installing an Entrypoint (pre-owned title)
layout: single
sidebar:
  nav: "side"
---

We will now use pre-made scripts to simplify the installation of homebrew entrypoints. These entrypoints will allow us to load homebrew within seconds of launching the target application.

## What you need

* The [twlnf entrypoint installation pack](/assets/files/twlnf-entrypoint-pack.zip)

## Preparation

1. Insert your device's SD card into your computer
2. Copy the contents of the twlnf entrypoint installation `.zip` to the root of your SD card
3. Unplug your SD card, and insert it in your DSi

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

## Installing your Entrypoint

1. If prompted in twlnf, press **A** to create a NAND backup
  - This may take a few minutes
  - Store this NAND backup in a safe location, it is a critical backup
2. Press **X** to mount the NAND directly

  - twlnf does not list this as an option

3. Navigate to the .nfs script corresponding with the DSiWare you have
  - Fieldrunners - `install_fieldrunhax_usa.nfs`
  - Legends of Exidia - `install_exidiahax_usa.nfs`
  - Guitar Rock Tour - `install_grtpwn_usa.nfs`
  -  The Legend of Zelda: Four Swords Anniversary - `install_4swordshax_usa.nfs`
4. Press **A** to execute the script
  - If the dry run fails, you do not have the DSiWare installed
5. Press **A** to install the application to NAND
6. Once finished, press **Select** to quit twlnf
7. Press **A** to confirm
  - Your console will power off

## Launching your Entrypoint

1. Power on your console
2. Open your exploited application
3. Perform the following:
  - Fieldrunners - Wait for the game to load, and press **Scores** on the main menu
  - Legends of Exidia - Navigate past the two start screens, select the first save file, and press **Continue**
  - Guitar Rock Tour - Scroll down, and press **High Scores** > **Drums** > **Easy**
  -  The Legend of Zelda: Four Swords Anniversary - Just launch the game, 4swordshax requires no user intervention

Your entrypoint will load whatever homebrew you have on your SD card as `boot.nds`. Currently, this is twlnf. It is recommended that you install SRLoader, as it can launch both commercial ROMs and homebrew, and has several emulators built in.

4swordshax will not work with SRLoader to launch commercial ROMs, however it can still use emulators and homebrew.

- [Using SRLoader](/more/using-srloader){: .btn .btn--light-outline}