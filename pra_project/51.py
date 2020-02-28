import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.10.0.221', username='root', password='NewPass@gss')
stdin, stdout, stdrr = ssh.exec_command('service --status-all')
# stdin, stdout, stdrr = ssh.exec_command('systemctl list-units --type service')

for line in stdout:
    print(line)

