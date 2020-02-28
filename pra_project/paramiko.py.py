import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='10.10.0.210',username='root', password='NewPass@123')

stdin, stdout, stderr = client.exec_command('service --status-all')

for line in stdout:
    print(line.strip('\n'))

client.close()
