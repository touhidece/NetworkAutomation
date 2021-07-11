import paramiko
from getpass import getpass
import time


username = input("Please enter your username: ")
password = getpass()
ip = open('routerIP')
for IPadr in ip:
    IPadr=IPadr.strip()
    SSH=paramiko.SSHClient()
    #remote_conn_pre=paramiko.SSHClient()
    SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SSH.connect(IPadr, port=22, username=username,password=password, look_for_keys=False, allow_agent=False)
    remote_conn = SSH.invoke_shell()
    #output = remote_conn.recv(65535)
    #print (output)

    remote_conn.send("copy running-config tftp:\n")
    remote_conn.send("192.168.1.1\n")
    remote_conn.send("\n")
    remote_conn.send("exit\n")
    time.sleep(.5)
    #output = remote_conn.recv(65535)
    output = remote_conn.recv(65535)
print("Connected successfully.")
