#### ScreenShot :

![ScreenShot](https://raw.githubusercontent.com/stking68/OpenConnect-Linux-GUI/main/screenshot1.png) 

### Features :

- A Simple GUI Interface for the Openconnect VPN

- Built In Database for Storing Account information powered By Sqlite3

- a Data base file called `database.db` will be created after running the app for the first time that will store all the account info, if you choose to do so.

- No sudo password will be stored! You'll be prompted to enter your password every-time when running the app for maximum security

### Prerequisite's :

1. Have Tk Installed on Your System
2. Have tkterminal Installed 
3. Openconnect and vpnc
4. Python's Pip

### Installing Prerequisite's Using a Package Manager :

Arch:

`sudo pacman -S tk openconnect vpnc python-pip`

Ubuntu/Debian:

`sudo apt install python3-tk openconnect vpnc vpnc-script python3-pip`

Fedora:

`sudo dnf install python3-tkinter openconnect vpnc vpnc-script python3-pip`

<br>

### Installing tkterminal Using Pip :

```
pip install tkterminal
```

### Usage / Installation :

###### Note : if Git is not installed do so with :

Ubuntu/Debian:

```
sudo apt update && sudo apt install git
```

Fedora:

```
sudo dnf upgrade --refresh && sudo dnf install git
```

##### Installation :

```
git clone https://github.com/stking68/OpenConnect-Linux-GUI.git
cd OpenConnect-Linux-GUI/
python3 oc-gui.py
```

<br>
