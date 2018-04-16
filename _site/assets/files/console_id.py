import io
import os
import subprocess

try:
	print("Extracting binary...")


	for file in os.listdir():
		if ".bin" in file:
			if os.name == 'nt':
				subprocess.call(["dsi_srl_extract.exe",  "--basename=OUT",  file])
			else:
				print("WARNING: Non-Windows operating system detected!")
				print("The script will continue, but please ensure that Wine is installed.")
				input("Press the Enter key to continue...")
				subprocess.call(["wine", "dsi_srl_extract.exe",  "--basename=OUT",  file])

	print("Extracting Console ID...")

	footer = io.open('OUT.footer', encoding = "ISO-8859-1")
	footer.seek(486)

	if os.path.isfile("console_id.txt"):
		print("Old console_id.txt found, removing")
		os.remove("console_id.txt")

	with open('console_id.txt', 'a') as consoleid:
		consoleid.write(footer.read(16))
	footer.close()

	print("Cleaning up...")
	residue = [".banner", ".footer", ".savedata", ".tmd", ".tna4", ".nds"]

	for file in os.listdir():
		for extension in residue:
			if extension in file:
				os.remove(file)
except Exception as e:
	print("ERROR: {0}".format(e))
else:
	print("Success")
input("Press Enter to continue...")