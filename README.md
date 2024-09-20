# `.PKG` -> `.DMG` Convertor
## A tool to create `.dmg` from Apple's `.pkg`
## NOTE: Runs on Linux/macOS only. Use VM for Windows.
- The script will automatically create `.dmg` & save it to desired location.
- it will be bootable hence can be used for Hackintosh or MacOS
- also works with my another script [Automated-macOS-Installer](https://www.github.com/cdude1909/Automated-macOS-Installer)

### Requirements

Make sure you have this dependencies pre-installed,
- python3 
- qemu-x86_64
- `InstallAssistant.pkg` (Can be downlaoded externally from [Mr.macintosh](https://mrmacintosh.com/how-to-download-macos-catalina-mojave-or-high-sierra-full-installers/))

in `python` you must have this dependencies,
```
sudo pip install argparse lzma
```
### Run
Simply,
``` 
python3 /path/to/convertor.py
```

###Screenshot:
