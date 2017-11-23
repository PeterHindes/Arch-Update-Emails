notiman
=============
Auto-upgrade notifications for Arch Linux
--------------------------------------------------------
Small Python script that sends update notifications via e-mail and optionally updates Arch Linux (by running `pacman -Syu --noconfirm`).

Requires:
  *Python >3.5
  *[pacAUR](https://aur.archlinux.org/packages/pacaur/)
  ***pacman**.


Installation
------------
Firstly, open `settings.py` and modify according your necessities (the minimum required is to set your receiver email (a working notification only Gmail account is already attached)).

Secondly, install [pacAUR](https://aur.archlinux.org/packages/pacaur/) if you want AUR update notifications.

Afterwards, copy `auto_upgrade.py` to `/root` and `auto_upgrage.service` and `auto_upgrade.timer` to `/etc/systemd/system/`.


Finally enable the timer service by running:
    # systemctl enable auto_upgrade.timer
Then it should work ;)
