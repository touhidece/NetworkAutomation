import paramiko
from getpass import getpass
import time


username = input("Please enter your username: ")
password = getpass()
#ip = open('routerIP')
useradd = 'set member "mdariful" "mriad" "hossains" "sazad" "momin" "mrubayat" "masud" "moniruzzaman" "adnan" "ikamrul" "tasnim" "anam" "promi" "mmhaque" "ashiq"'
#useradd = 'unselect member "rniaz" "mmoshiur" "ataslima" "shamsun"'
f=["192.168.201.155","192.168.115.19"]
for IPadr in f:
    IPadr=IPadr.strip()
    print("Firewall IP: " + IPadr)
    HOST = IPadr
    if HOST == "192.168.201.155":
        SSH = paramiko.SSHClient()
        # SSH_pre=paramiko.SSHClient()
        SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        SSH.connect(IPadr, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)
        stdin, stdout, stderr = SSH.exec_command('config vdom\n edit Altair\n config user group\n edit "Group - SSL VPN User - SPC Ext"\n' +useradd + '\n next\n end\n exit\n')
        time.sleep(.5)
        print("successfully user add at firewall ", HOST)
    elif HOST == "192.168.115.19":
        SSH = paramiko.SSHClient()
        # SSH_pre=paramiko.SSHClient()
        SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        SSH.connect(IPadr, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)
        stdin, stdout, stderr = SSH.exec_command('config vdom\n edit Arctic\n config user group\n edit "Group - SSL VPN User - SPC Ext"\n' + useradd + '\n next\n end\n exit\n')
        time.sleep(.5)
        print("successfully user add at firewall ", HOST)