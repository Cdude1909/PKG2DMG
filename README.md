# `.PKG` -> `.DMG` Convertor
### A tool to create `.dmg` from Apple's `.pkg` 🎊
### NOTE: Runs on Linux only. Use VM for Windows.
- The script will automatically create `.dmg` & save it to desired location.
- `.dmg` will be bootable hence can be used for Hackintosh or offical Mac
- also works with my another script [Automated-macOS-Installer](https://www.github.com/cdude1909/Automated-macOS-Installer)

## Requirements

Make sure you have this dependencies pre-installed,
- 16 GB `.dmg` will be created hence make sure you have enough space
- Python3.3+ (it will cover all the required pip dependencies ;) ) 
- `InstallAssistant.pkg` (Can be downloaded externally from [Mr.macintosh](https://mrmacintosh.com/how-to-download-macos-catalina-mojave-or-high-sierra-full-installers/))

## Run
Simply,
```
git clone https://www.github.com/Cdude1909/PKG2DMG/
cd pkg2dmg
sudo chmod +x pkg2dmg.sh
sudo ./pkg2dmg.sh
```

## Miscellaneous
- For vm,you may use `dmg2img` to convert `dmg` to `iso` and boot it in VM. However,it requires more complex steps.
- it supports many macos bootable .pkg, untill they change the pattern. hence you can **re-use this script for newer versions.**  (Catalina -- Sequoia & maybe ahead...)
