import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites=["www.facebook.com","facebook.com","mail.google.com/mail/u/0/#inbox",
"www.mail.google.com/mail/u/0/#inbox"]

while True:
    if 8 < dt.now().hour < 16:
        print("No no no...")
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write("    "+redirect+"    "+website+"\n")
    else:
        print("Ja ja ja...")
        with open(hosts_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
