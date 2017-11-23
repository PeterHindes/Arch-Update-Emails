notiman
=============
Auto-upgrade notifications for Arch Linux
--------------------------------------------------------
Small Python script that sends update notifications via e-mail and optionally updates Arch Linux (by running `pacman -Syu --noconfirm`).

Requires:
  * [Python >3.5](https://www.archlinux.org/packages/extra/x86_64/python/)
  * [pacAUR](https://aur.archlinux.org/packages/pacaur/)
  * [pacman](https://www.archlinux.org/packages/core/x86_64/pacman/) (Comes with Arch Linux)


Installation
------------

Install the dependencies:
'alias pacman='sudo pacman''
'pacman -Syu --noconfirm'
'pacman -S git && git clone https://aur.archlinux.org/pacaur-git.git && cd pacaur-git && makepkg && pacman -U pacaur-git-*.tar.xz'

1. Open `settings.py` and set those things
  * The minimum required is to set your receiver email
  * A working notification only Gmail account is already attached (please don't fu** it up)
2. Install [pacAUR](https://aur.archlinux.org/packages/pacaur/) if you want AUR update notifications.

Afterwards, copy `auto_upgrade.py` to `/root` and `auto_upgrage.service` and `auto_upgrade.timer` to `/etc/systemd/system/`.


Finally enable the timer service by running:
    # systemctl enable auto_upgrade.timer
Then it should work ;)
