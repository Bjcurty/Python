# Brad Curtis
# 3/12/2020
# Program developed to block a list of websites from internet traffic on the device
# during certain hours. This program can be set as a Windows Task and scheduled to be automatic.
# It's actually a great way to act as both a productivity tool as well as a restriction tool for 
# young children.
# Inluenced by The Python Mega Course taught by Ardit Sulce
import time
from datetime import datetime as dt

# designating path of hosts file, getting the address to redirect traffic to along
# with a list of websites to not be accessable
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites=["www.facebook.com","facebook.com","mail.google.com/mail/u/0/#inbox",
"www.mail.google.com/mail/u/0/#inbox"]

# while loop to check computer time between 8am and 4pm that acesses hosts file
# and prints lines to it if they do not exist already. In the case that it is not
# during those hours, the file is sorted through, printed at the top, and then truncated
# for every line found from the list. It's a complicated way to remove lines from a file,
# but I couldn't see another way of doing so other than the suggested method.
while True:
    if 8 < dt.now().hour < 16:
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write("    "+redirect+"    "+website+"\n")
    else:
        with open(hosts_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
