import paramiko
from getpass import getpass
import time


username = input("Please enter your username: ")
password = getpass()
UserID=input("Please Enter the User ID:")
#ip = open('routerIP')
#useradd = 'set member "mitali" "halim" "mdariful" "mriad" "hossains" "sazad" "momin" "mrubayat" "masud" "moniruzzaman" "adnan" "ikamrul" "tasnim" "anam" "promi" "mmhaque" "ashiq" "abut" "arifeen" "ferdous" "hfaisal" "husain" "jubayer" "koushik" "mdelowar" "mdzakir" "mjalal" "msazzad" "mushfiqur" "nrobin" "rakybul" "samiul" "shikha" "tanvirh" "adnan" "dalilur" "foysal" "hmehedi" "ikamrul" "jyoti" "kuddin" "mdhafizur" "mhmehedi" "mmhaque" "mshariful" "nahian" "omarf" "ralam" "shabib" "sumanch" "tanzim" "alom" "eyamin" "golams" "hmmehedi" "ishtiaq" "kislam" "mahir" "mdimran" "mimam" "mnafiz" "mshuvo" "nahsan" "raisul" "robin" "shefath" "sushmita" "abusaleh" "ahmedr" "amunny" "arozina" "farjanay" "hhasan" "kimmia" "lmamun" "rhasibur" "salekin" "shoaib" "tanzir" "adnan" "ahosan" "aniks" "bokteyar" "ftamanna" "islams" "mmhaque" "riya" "sonia" "taraqul" "afsanay" "amena" "arifh" "bonny" "junayed" "litonc" "nazmulh" "rsiddiqur" "shikha" "sushmita" "tithi" "shamsun"'
useradd = 'append member "rniaz" "mmoshiur" "ataslima" "shamsun"'
#useradd = 'unselect member '+UserID
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