import telnetlib
import getpass
HOST = input("nhap host: ")
#HOST = '1.1.1.2'
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

#tn.read_until(b"login: ")
#tn.write(user + b"\n")

tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")   
#    tn.read_until("Password: ")
    tn.write(password.encode('ascii') + b"\n")
#tn.write(b"ls\n")
#tn.write(b"ls\n")
tn.write(b'enable\n')
tn.write(b'enable\n')
tn.write(b"conf t\n")

#### config int s2/0
tn.write(b"int s2/0\n")
tn.write(b"ip add 2.2.2.1 255.255.255.252\n")
tn.write(b"no shut\n")

##### config int fa0/1
tn.write(b"int f0/1\n")
tn.write(b"ip add 192.168.1.254 255.255.255.0\n")
tn.write(b"no shut\n")

#### config dhcp
tn.write(b"ip dhcp pool abc\n")
tn.write(b"network 192.168.1.0 255.255.255.0\n")
tn.write(b"default-router 192.168.1.254\n")

##### save config
tn.write(b"end\n")
tn.write(b"copy running-config startup-config\n")
tn.write(b"\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))