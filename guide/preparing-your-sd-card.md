---
title: Preparing your SD card
layout: single
sidebar:
  nav: "side"
---

ugopwn is an exploit that allows for homebrew access on all DSi firmwares. It requires you to have a copy of Flipnote Studio already installed on your console. There is no way to install Flipnote Studio without homebrew as of March 31st 2017.

We can use ugopwn to install sudokuhax. Since ugopwn can be very time consuming, we can install sudokuhax instead, which launches the Homebrew Launcher a few seconds after you start the application.

As of now, ugopwn only supports USA consoles, however a EUR and JPN release have been promised to come soon.

## Downloads

- The latest release of [ugopwn](/assets/files/ugopwn.zip)
- The latest release of [twlnf](https://github.com/Jimmy-Z/twlnf/releases){:target="_blank"}
- The latest release of [Python 3](https://www.python.org/downloads/){:target="_blank"}
- The latest release of [DSi SRL Extractor](/assets/files/dsi_srl_extract.zip)
- <i class="fa fa-magnet" aria-hidden="true" title="This is a magnet link. Use a torrent client to download the file."></i> -  [sudokuhax](magnet:?xt=urn:btih:fd4dcb2f954f48adb2af96326609f9c3f3ae2a7a&dn=sudokuhax.zip&tr=http%3a%2f%2ftracker.tfile.me%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2710%2fannounce&tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounce&tr=udp%3a%2f%2ftorrent.gresille.org%3a80%2fannounce&tr=udp%3a%2f%2ftracker.yoshi210.com%3a6969%2fannounce&tr=http%3a%2f%2fexplodie.org%3a6969%2fannounce&tr=http%3a%2f%2ftracker1.wasabii.com.tw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fp4p.arenabg.com%3a1337%2fannounce&tr=http%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=http%3a%2f%2ftorrent.gresille.org%2fannounce&tr=udp%3a%2f%2ftracker.filetracker.pl%3a8089%2fannounce&tr=http%3a%2f%2ftracker.aletorrenty.pl%3a2710%2fannounce&tr=udp%3a%2f%2fzer0day.ch%3a1337%2fannounce&tr=http%3a%2f%2fp4p.arenabg.com%3a1337%2fannounce&tr=http%3a%2f%2ftracker.baravik.org%3a6970%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.aletorrenty.pl%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce)


## Instructions

1. Install Python 3 on your computer
2. Open the System Settings application
3. Select **Data Management > System Memory > Flipnote Studio > Copy > Yes**
	- If Data Management isn't appearing, open the DSi Shop, close it, and then try again
4. Once finished, power off your device
5. Take your SD card out of your console and insert it into your computer
6. Copy the contents of the ugopwn `.zip` file to the root of your SD card
7. Copy the contents of the twlnf `.7z` file to the root of your SD card, and rename `twlnf.nds` to `boot.nds`
8. Copy the contents of the sudokuhax `.zip` file to the root of your SD card
9. Copy the contents of the DSi SRL Extractor `.zip` file to a folder on your Desktop
10. Open the SD card drive on your computer
11. Navigate to /Private/DS/Title/
12. Copy the `.bin` file to your DSi SRL Extractor folder
13. Run the console_id `.py` file inside the folder
  - On Unix-based systems, such as Mac and Linux, [WINE](https://www.winehq.org/){:target="_blank"} is required for this script to run
14. When prompted, press Enter
15. Copy the new console_id `.txt` file to the root of your SD card
16. Eject your SD card and insert it back into your DSi


[Installing Sudokuhax](/guide/installing-sudokuhax){: .btn .btn--light-outline}
{: style="text-align: center;"}
