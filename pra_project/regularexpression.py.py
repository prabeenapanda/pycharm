import re

filename = 'testfile.txt'
data_column = ['name', 'email', 'phone', 'address', 'gender', 'ip']

userdata = ''
for column in data_column:
    userdata += "\t" + input(f'Please input users {column} ')

with open(filename,'w') as fh:
    fh.write(userdata)
print('Data saved successfully..')

print('The entered emails are: ')
emails = re.findall(r'[\w\.-]+@[\w\.-]+', userdata)
for email in emails:
    print(email)

print('The entered phone nos are: ')
ph_nos = re.findall(r'\d{10}', userdata)
for ph in ph_nos:
    print(ph)

print('The entered IPs are: ')
ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', userdata)
# ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', userdata)
for ip in ips:
    print(ip)


