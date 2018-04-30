---
title: Installing Sudokuhax
layout: single
sidebar:
  nav: "side"
---

This guide only supports USA consoles for now.
{: .notice--info}

Make sure you have at least 30 blocks of space on your console's internal storage, or you **will brick** your device.
{: .notice--danger}

sudokuhax is an exploit of the Sudoku DSiWare game, allowing us to launch the Homebrew Launcher seconds after starting the application.

To use the [magnet](https://en.wikipedia.org/wiki/Magnet_URI_scheme) links on this page, you will need a torrent client like [Deluge](https://dev.deluge-torrent.org/wiki/Download).

## What you need
- <i class="fa fa-magnet" aria-hidden="true" title="This is a magnet link. Use a torrent client to download the file."></i> -  [sudokuhax](magnet:?xt=urn:btih:fd4dcb2f954f48adb2af96326609f9c3f3ae2a7a&dn=sudokuhax.zip&tr=http%3a%2f%2ftracker.tfile.me%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2710%2fannounce&tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounce&tr=udp%3a%2f%2ftorrent.gresille.org%3a80%2fannounce&tr=udp%3a%2f%2ftracker.yoshi210.com%3a6969%2fannounce&tr=http%3a%2f%2fexplodie.org%3a6969%2fannounce&tr=http%3a%2f%2ftracker1.wasabii.com.tw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fp4p.arenabg.com%3a1337%2fannounce&tr=http%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=http%3a%2f%2ftorrent.gresille.org%2fannounce&tr=udp%3a%2f%2ftracker.filetracker.pl%3a8089%2fannounce&tr=http%3a%2f%2ftracker.aletorrenty.pl%3a2710%2fannounce&tr=udp%3a%2f%2fzer0day.ch%3a1337%2fannounce&tr=http%3a%2f%2fp4p.arenabg.com%3a1337%2fannounce&tr=http%3a%2f%2ftracker.baravik.org%3a6970%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.aletorrenty.pl%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce)

## Preparation

1. Insert your device's SD card into your computer
2. Copy the contents of the sudokuhax `.zip` to the root of your SD card
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
8. Click the second note.
9. Click on the Flipnote frog icon in the bottom left
10. Click on the film roll icon.
11. Click on the single right arrow (the next to last arrow icon) two times
  - You will see a new frame be created
12. Click on the paste button exactly 122 times.
13. Select "Erase" and then "Paste"
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

Sudokuhax will now load whatever homebrew you have on your SD card as `boot.nds`.
