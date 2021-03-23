import getpass
import telnetlib
import sys

user = input("Enter your remote account: ")
password =getpass.getpass(prompt='Enter your password:')
#password = raw_input("Enter your password:")
##f = open('routerIP')
#need to add user
useradd = 'set "mdariful" "mriad" "hossains" "sazad" "momin" "mrubayat" "masud" "moniruzzaman" "adnan" "ikamrul" "tasnim" "anam" "promi" "mmhaque" "ashiq"'
f=["192.168.201.155","192.168.115.19"]
print(f)
for IP in f:
    IP = IP.strip()
    print("Router IP: " + IP)
    HOST = IP
    if HOST == "192.168.201.155":
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"FG5H0ETB19909452 login: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
            tn.write(b"config vdom\n")
            tn.write(b"edit Altair\n")
            tn.write(b"config user group\n")
            tn.write(b'edit "Group - SSL VPN User - SPC Ext"\n')
            tn.write(useradd.encode('ascii') + b"\n")
            #tn.write(b'append member "tohidur"\n')
            tn.write(b'next\n')
            tn.write(b'end\n')
            tn.write(b'exit\n')
    elif HOST == "192.168.115.19":
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"FG5H0E5819907055 login: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
            tn.write(b"config vdom\n")
            tn.write(b"edit Arctic\n")
            tn.write(b"config user group\n")
            tn.write(b'edit "Group - SSL VPN User - SPC Ext"\n')
            tn.write(useradd.encode('ascii') + b"\n")
            # tn.write(b'append member "tohidur"\n')
            tn.write(b'next\n')
            tn.write(b'end\n')
            tn.write(b'exit\n')

    print(tn.read_all().decode('ascii'))
