---
title: Installing DSiWare
layout: single
sidebar:
  nav: "side"
---

You will need [Unlaunch](/guide/installing-unlaunch/) and [HiyaCFW](/guide/installing-hiyacfw/) installed before proceeding.
{: .notice--info}

Now that we have a DSiWare to install, we can use HiyaCFW to install it to our system with ease

## Requirements
- The latest release of [maketmd](https://github.com/Tuxality/maketmd/releases){:target="_blank"}
- A folder containing the DSiWare you wish to install
    - You should have this from the previous section

## Preparation
1. Copy *the contents of* the maketmd `.zip` file to a folder on your PC
2. If your DSiWare folder is still on your 3DS SD card, copy it to a location on your PC

## Instructions
1. Open the dumped folder on your PC containing your DSiWare
2. Navigate to `content`
3. Delete the `cmd` folder, and the `.tmd` file
4. Delete any `.ctx` files if they exist
5. Drag and drop the `.app` file onto the maketmd program
    - You will see a new file named `title.tmd` be created
6. Copy the DSiWare folder to the `/title/00030004` folder on your DSi's SD card
7. Power on your DSi, and "unwrap" the new DSiWare
    - If you boot to an "error has occured" screen, you have exceeded the amount of allowed DSiWare blocks on your system
    - SRLoader can get around this limitation, see the link below for more information

[Replacing the System Menu with SRLoader](/more/replacing-system-menu){: .btn .btn--light-outline}
{: style="text-align: center;"}
