auto_upgrade
=============
Auto-upgrade Arch Linux or get e-mail in case of failure
--------------------------------------------------------
Small Python script that tries to update an Arch Linux system (by running `pacman -Syu --noconfirm`) and send update notifications via e-mail in case of failure. Needs Python >3.5, [cower](https://aur.archlinux.org/packages/cower/) and **pacman**.

Installation
------------
Firstly, install [cower](https://aur.archlinux.org/packages/cower/) (optional) if you want AUR updates notification.
Secondly, open `auto_upgrade.py` and modify according your necessities (*at least* you need to modify `EMAIL`and `PASSWORD` variables).
Afterwards, copy `auto_upgrade.py` to `/root` (or any other directory with 700 permission for root, so a normal user can't read your password in plain text!) and `auto_upgrage.service` and `auto_upgrade.timer` to `/etc/systemd/system`.
Finally enable the timer service by running:
  
    # systemctl enable auto_upgrade.timer

That's it.
