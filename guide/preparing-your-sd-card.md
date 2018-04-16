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
