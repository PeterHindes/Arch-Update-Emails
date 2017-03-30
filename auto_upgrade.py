#!/usr/bin/python3

import smtplib
import sys
import time
from distutils.spawn import find_executable
from email.mime.text import MIMEText
from socket import gethostname
from subprocess import run, PIPE

# Needs to be a TLS protected SMTP server
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "INSERT EMAIL HERE"
SENDER_PASSWORD = "INSERT PASSWORD HERE"
RECEIVER_EMAIL = SENDER_EMAIL
SUBJECT_TEMPLATE = "Updates available in {hostname}"
MSG_TEMPLATE = """
At {time}, there are updates available in {hostname} thanks to an impossibility to do an auto-upgrade.
{updates}
Login to {hostname} and run:
\t# pacman -Syu
To upgrade the system.
"""

def add_prefix(prefix, text):
    result = ""
    for line in text.splitlines():
        result += prefix + line + "\n"
    return result

def do_auto_upgrade(timeout=1800):
    packages = ""
    try:
        run(["pacman", "-Syu", "--noconfirm"], timeout=timeout, universal_newlines=True)
    except TimeoutExpired:
        result = run(["checkupdates"], stdout=PIPE, universal_newlines=True)
        packages += "\nOfficial repositories:\n"
        packages += add_prefix("\t:: ", result.stdout)

    if find_executable("cower"):
        result = run(["cower", "--update", "--color=never"], stdout=PIPE, universal_newlines=True)
        if result.stdout:
            packages += "\nAUR:\n"
            # cower already adds "::" as a prefix
            packages += add_prefix("\t", result.stdout)

    return packages


def send_email(receiver, sender, password, subject, message):
    # Connect to SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.login(sender, password)

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    server.send_message(msg)
    server.quit()

def main():
    available_updates = do_auto_upgrade()
    if available_updates:
        print("Available updates thanks to a failure to auto-upgrade, sending e-mail to {}".format(RECEIVER_EMAIL))
        hostname = gethostname()
        send_email(RECEIVER_EMAIL, SENDER_EMAIL, SENDER_PASSWORD,
                   SUBJECT_TEMPLATE.format(hostname=hostname),
                   MSG_TEMPLATE.format(time=time.strftime("%c"),
                                       hostname=hostname,
                                       updates=available_updates)
                   )
    else:
        print("No available package to upgrage or auto-upgrade successful, not sending e-mail")

    sys.exit()

if __name__ == "__main__":
    main()
