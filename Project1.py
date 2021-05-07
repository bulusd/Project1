import os

hostnames = [
    '192.168.10.30',
    '192.168.10.50',
    '192.168.10.60',
    '192.168.10.20',
]

for hostname in hostnames:
    response = os.system('ping -c 1 ' + hostname)
    if response == 0:
        print(hostname, 'is up')
    else:
        print(hostname, 'is down')