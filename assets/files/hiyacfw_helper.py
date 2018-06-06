import hashlib
import os
import sys
import subprocess

launcher_region = ""

print('---HIYACFW HELPER---')
print('This is an updated version for Au, USA, EUR, Jap DSI. Edited by LmN')
print('Running self-check')
dependencies = ['nand.bin', 'flips.exe', "00000002.app"]
try:
    if os.name == 'nt':
        char = "\\"
    else:
        char = "/"

    if os.getcwd().split(char)[-1].replace("\\", "") != 'for PC':
        raise Exception('Script not placed in the HiyaCFW "for PC" directory. Please place the script in the correct location before proceeding.')
    for dependency in dependencies:
        if not os.path.isfile(dependency):
            raise Exception('File {} not found. Ensure you placed these in the directory.'.format(dependency))
    with open('00000002.app', 'rb') as launcher:
        expected_sha1s = { 'usa': '1339bd7457484839f1d71f27de2f8da8098834b4', 'jap': '69c422a1ab1f26344a3d2b294ec714db362f57f0', 'eur': 'c5a3507181489f5190976a905b2953799e421363', 'aus': '8f79c6c1442d3e33d211454ec92bbe42c94a599d'}
        sha1 = hashlib.sha1()
        sha1.update(launcher.read())
        for region, expected_sha1 in expected_sha1s.items():
            if sha1.hexdigest() == expected_sha1:
                launcher_region = region
        if launcher_region == "":
            raise Exception('Launcher is not v512 of AUS, USA, EUR or JAP. Is your launcher the right version and decrypted?')
except Exception as e:
    print('Self-check failed! {}'.format(e))
    input('Press Enter to continue...')  
    sys.exit()

print('Decrypting NAND')
try:
    if os.name == 'nt':
        subprocess.call(["twltool", "nandcrypt", "--in", "nand.bin"])
    else:
        print("WARNING: Non-Windows operating system detected!")
        print("The script will continue, but please ensure that Wine is installed.")
        input("Press the Enter key to continue...")
        subprocess.call(["wine", "twltool", "nandcrypt", "--in", "nand.bin"])

except Exception as e:
    print('Error occured! Does this backup have the required NO$GBA footer? ({0})'.format(e))
    input('Press Enter to continue...')       
    sys.exit()

print('\nExtracting ARM7/ARM9 BIOS from NAND')
if os.name == 'nt':
    subprocess.call(["twltool", "boot2", "--in", "nand.bin"])
else: 
    subprocess.call(["wine", "twltool", "boot2", "--in", "nand.bin"])

print('\nIPS patching ARM7/ARM9 BIOS')
if os.name == 'nt':
    subprocess.call(["flips", "--apply", "bootloader files/bootloader arm7 patch.ips", "arm7.bin"])
    subprocess.call(["flips", "--apply", "bootloader files/bootloader arm9 patch.ips", "arm9.bin"])
else: 
    subprocess.call(["wine", "flips", "--apply", "bootloader files/bootloader arm7 patch.ips", "arm7.bin"])
    subprocess.call(["wine", "flips", "--apply", "bootloader files/bootloader arm9 patch.ips", "arm9.bin"])

print('\nPrepending data to ARM9 BIOS')

try:
    with open('bootloader files/bootloader arm9 append to start.bin', 'rb') as arm9_prepend, open('arm9.bin', 'rb') as arm9_bin, open('arm9_new.bin', 'ab') as arm9_new:
        arm9_new.write(arm9_prepend.read() + arm9_bin.read())
    os.remove('arm9.bin')
    os.rename('arm9_new.bin', 'arm9.bin')
except Exception as e:
    print('Error occured! Does the bootloader files folder exist?')
    input('Press Enter to continue...')       
    sys.exit()

print('\nGenerating new bootloader')
if os.name == 'nt': 
    subprocess.call(['bootloader files/ndstool', '-c', 'bootloader.nds', '-9', 'arm9.bin', '-7', 'arm7.bin', '-t', 'bootloader files/banner.bin', '-h', 'bootloader files/header.bin'])
else:
    subprocess.call(['wine', 'bootloader files/ndstool', '-c', 'bootloader.nds', '-9', 'arm9.bin', '-7', 'arm7.bin', '-t', 'bootloader files/banner.bin', '-h', 'bootloader files/header.bin'])

# wine twltool modcrypt --in "00000002.app" --out "00000002_dec.app"  
print('\nDecrypting launcher')
if os.name == 'nt':
    subprocess.call(["twltool", "modcrypt", "--in", "00000002.app"])
else:
    subprocess.call(["wine", "twltool", "modcrypt", "--in", "00000002.app"])

print('\nIPS patching launcher')
patch = "v1.4 Launcher (00000002.app) (JAP-KOR) patch.ips" if launcher_region == "jap" else "v1.4 Launcher (00000002.app) patch.ips"

if os.name == 'nt':
    subprocess.call(["flips", "--apply", patch, "00000002.app"])
else:
    subprocess.call(["wine", "flips", "--apply", patch, "00000002.app"])

print('\nMoving new files')
if not os.path.isdir('Modified Files'):
    os.mkdir('Modified Files')
os.rename('bootloader.nds', 'Modified Files/bootloader.nds')
os.rename('00000002.app', 'Modified Files/00000002.app')

print('Done!')
print('Navigate to the Modified Files folder.')
print('Copy bootloader.nds to the hiya folder on your <2GB SD card.')
print('Copy 00000002.app to title/00030017/484e41XX/content folder on your <2GB SD card.')
input('Press Enter to continue...')       
sys.exit()
