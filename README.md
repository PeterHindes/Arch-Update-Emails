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

- [ ] Working and Ready For Use

*Install the dependencies:*
* `alias pacman='sudo pacman'`
* `pacman -Syu --noconfirm`
* `pacman -S git && git clone https://aur.archlinux.org/pacaur-git.git && cd pacaur-git && makepkg && pacman -U pacaur-git-*.tar.xz`

*Configure the program:*
1. Open `settings.py` and input your preferences
  1. The minimum required is to set your receiver email
  2. A working notification only Gmail account is already attached (please don't fu** it up)
2. Install [pacAUR](https://aur.archlinux.org/packages/pacaur/) if you want AUR update notifications.
3. Place `auto_upgrade.py` in `/root` (if you chose another path adjust auto_upgrade.service)
4. Place `auto_upgrage.service` and `auto_upgrade.timer` in `/etc/systemd/system/`.
5. Enable the timer service by running:
  1. `systemctl enable auto_upgrade.timer`

Now it should start working ;)
