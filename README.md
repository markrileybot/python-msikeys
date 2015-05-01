Python MSI Keys
===============
Neat-O python app to control your fancy MSI GT72 Dominator keyboard backlight.  I learned the protocol by reading the
code in this node project https://github.com/wearefractal/msi-keyboard.

Note that you must have permission to talk to your hid devices.  Otherwise, you have to run this code with ```sudo```

Installing
----------
```
sudo pip install .
```

You'll likely have to create a new udev rule in /etc/udev/rules.d/10-msikeys.rules so that your user can talk to this device
```
SUBSYSTEM=="usb", ATTR{idVendor}=="1770", ATTR{idProduct}=="ff00", GROUP="input", SYMLINK+="msikeyboard_backlight"
```
Note that your user must be a member of the group in the above rule.

Then reboot or do something like
```
sudo udevadm control --reload-rules && sudo udevadm trigger
```

Running
-------
To initialize your config:
```
msikeys-config.py
```

To apply your config at startup:
```
msikeys-init.py
```

Examples
--------
Green keyboard:
```
import msikeys

kb = msikeys.get_keyboard()
kb.colors = msikeys.Color.GREEN
kb.commit()
```

Team amurica keyboard:
```
import msikeys

kb = msikeys.get_keyboard()
kb.colors = [msikeys.Color.RED, msikeys.Color.WHITE, msikeys.Color.BLUE]
kb.commit()
```

Load keyboard at login (in your ~/.bash_profile):
```
python msikeys-init.py
```
