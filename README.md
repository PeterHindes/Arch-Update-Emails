notify_update
=============
Get e-mail notifications of updates in Arch Linux
-------------------------------------------------
Small Python script to send update notifications via e-mail in Arch Linux distribution (and derivatives). Needs Python 3.5 (that you should already have if you use Arch Linux) and [cower](https://aur.archlinux.org/packages/cower/) (and **pacman**, of course).

Installation
------------
Firstly, install [cower](https://aur.archlinux.org/packages/cower/) if you don't already have it installed.
It is necessary for AUR updates (of course, you can modify `notify_updates.py` yourself to remove **cower** support).
Secondly, Open `notify_updates.py` and modify according your necessities (*at least* you need to modify `EMAIL`and `PASSWORD` variables).
Afterwards, copy `notify_updates.py` to `/usr/local/bin` and `notify_updates.service` and `notify_updates.timer` to `/etc/systemd/system`.
Finally enable the timer service by running:
  
    # systemctl enable notify_updates.timer

That's it.