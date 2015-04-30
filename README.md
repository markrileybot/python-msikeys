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

Load keyboard at login (in your ~/.bashrc):
```
python msikeys-init.py
```