# `.PKG` -> `.DMG` Convertor
### Your utility for generating `.dmg` file from `.pkg` file 🎊
### IMPORTANT: This software is for Linux only. Use a virtual machine for Windows.
- The script generates a `.dmg` file in the specified location.
- The `.dmg` file will boot, ensuring compatibility with Hackintosh systems and genuine Macs.
- Also works with my other script [Automated-macOS-Installer](https://www.github.com/cdude1909/Automated-macOS-Installer).

## Prerequisites

Make sure to install these dependencies first,
- 16 GB `.dmg` file will be created, so ensure you have sufficient storage
- Python3.12+ (it will include all pip dependencies ;) )
- `InstallAssistant.pkg` (Download your file externally from [Mr. Macintosh](https://mrmacintosh.com/macos-sequoia-full-installer-database-download-directly-from-apple/).)

## Run
Just,
```bash
git clone https://www.github.com/Cdude1909/PKG2DMG/ --recursive --remote-submodules
cd pkg2dmg
sudo chmod +x pkg2dmg.sh
sudo ./pkg2dmg.sh
```

## Miscellaneous
- You can convert a `dmg` file to an `iso` for VM use with `dmg2img`, but the process is complex.
- The script works with macOS bootable .pkg files as long as the format is unchanged. It can **be used for future versions**, from Catalina to Sequoia and beyond.
