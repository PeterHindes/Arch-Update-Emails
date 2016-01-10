notify_update
=============
Get e-mail notifications of updates in Arch Linux
-------------------------------------------------
Small Python script to send update notifications via e-mail in Arch Linux distribution (and derivatives). Needs Python 3.5 (that you should already have if you use Arch Linux) and [cower](https://aur.archlinux.org/packages/cower/) (and **pacman**, of course).

Installation
------------
Firstly, install [cower](https://aur.archlinux.org/packages/cower/) (optional) if you want AUR updates notification.
Secondly, open `notify_updates.py` and modify according your necessities (*at least* you need to modify `EMAIL`and `PASSWORD` variables).
Afterwards, copy `notify_updates.py` to `/root` (or any other directory with 700 permission for root, so a normal user can't read your password in plain text!) and `notify_updates.service` and `notify_updates.timer` to `/etc/systemd/system`.
Finally enable the timer service by running:
  
    # systemctl enable notify_updates.timer

That's it.