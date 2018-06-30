---
title: FAQ
layout: help
sidebar:
  nav: "side"
---

## Unlaunch freezes at `MISMATCH IN FAT COPIES`

This error is caused by twlnf. It has a critical bug that doesn't properly update the entire NAND after modifying it. This causes certain homebrew (like the Unlaunch installer) to throw an error.

Fortunately, this is fixable. Unfortunately, the *method* to fix it isn't set in stone, and largely varies from system to system.

Generally, deleting any DSiWare installed via twlnf in the past does the job, but make sure you have another homebrew entrypoint available if you delete an entrypoint.

It has also been reported that moving *all* DSiWare to the SD card and back to the system can help in some cases.

If this does not work, don't hesitate to ask the [Discord](/help/discord) for more help and for investigative purposes.

## Can I install HiyaCFW without Flipnote Studio?

No, you will need a hardmod to install HiyaCFW. Follow Gadorach's [hardmodding guide](https://gbatemp.net/threads/dsi-downgrading-the-complete-guide.393682/){:target="_blank"} to hardmod your DSi. Previous soldering experience is required.

## Can I use an SD card higher than 2GB with HiyaCFW yet?

Yes, using DSiMenu++. See the [Replacing System Menu with DSiMenu++](/more/replacing-system-menu/) page for more information.

Low-level "full" formatting your SD card with a tool like GUIFormat can help as well, but this will not get you around the DSi Menu's block limit, whereas DSiMenu++ does.

## Is there a safe way to remove Unlaunch?

Unfortunately, not at this time. 

Ideally there would be a tool, or an update to the Unlaunch installer itself, that allows for a direct uninstallation. Currently no such tool exists. Until one exists, all methods of installing Unlaunch either require unsafe tools like twlnf, or restoring a NAND backup.

Uninstalling via twlnf would trigger twlnf's NAND update bug, breaking the option to install unlaunch in the future, and NAND backups are not only dangerous but is also very stressful on the DSi's components.

## fuse-3ds fails to launch, or to mount my NAND backup!

This can happen for several reasons, but the most common is that your PC is missing Windows Updates that are required for the program to run.

If fuse-3ds shows nothing but a black command prompt screen, just wait a while longer- the program can be slow to start.

If fuse-3ds shows the following error at startup:

`The procedure entry point ucrtbase.terminate could not be located in the dynamic link library api-ms-win-crt-runtime-l1-1-0.dll.`

You are missing the following Windows Update: https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows

If fuse-3ds fails to mount with the error message:

`Cannot create WinFsp-FUSE file system: unspecified error.`

You are missing the following Windows Update: https://technet.microsoft.com/en-us/library/security/3033929.aspx

Both of these updates are several years old. If you're missing them, it is highly recommended that you enable Windows Update on your machine in order to keep your system updated and secure, and to avoid issues like this in the future.