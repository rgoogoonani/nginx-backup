import os

botToken = input("Bot Token :")
while len(botToken)<46 :
    botToken = input("invalid bot token try again: ")
print(botToken)
#-------------------------------------------------------------------
chid=input("Chatid : ")
while chid=="":
    chid = input("Chatid : ")
print(chid)
#-------------------------------------------------------------------
Name=input("Server Name : ")
print(Name)
#-------------------------------------------------------------------
FileAddres=input("File Addres : ")
if FileAddres=="":
    FileAddres="/Marzban/M1/db.sqlite3"
print(FileAddres)
with open("/NginxBackup/config.txt","w") as f:
    f.writelines(chid+"\n"+Name+"\n"+FileAddres+"\n"+botToken)


with open("/etc/systemd/system/NginxAutoBackup.service","w") as f:
    f.writelines("[Unit]\nDescription=Nginx Auto Backup\n\n[Service]\nExecStart=/usr/bin/python3 /NginxBackup/AutoBackup.py\n\n[Install]\nWantedBy=multi-user.target")
#f.writelines("[Unit]\nDescription=Nginx Auto Backup\n\n[Service]\nExecStart=screen /usr/bin/python3 "+str(os.path.abspath(__file__))+"\n\n[Install]\nWantedBy=multi-user.target")

os.system("sudo systemctl daemon-reload")
os.system("sudo systemctl start NginxAutoBackup")
os.system("sudo systemctl enable NginxAutoBackup")
