from netmiko import ConnectHandler
from datetime import date

today= date.today()
Date = str(today.strftime("%m_%d_%y"))

cisco_iosv = {
    'device_type': 'cisco_ios',
    'host':   '192.168.42.56',
    'username': 'Nsindiso',
    'password': 'bulawayo',
    'secret': 'bulawayo',
}

cisco_iosxe1 = {
    'device_type':'cisco_xe',
    'host': '192.168.42.82',
    'username': 'Nsindiso',
    'password': 'bulawayo',
    'secret':'bulwayo'
}

cisco_iosxe2 = {
    'device_type':'cisco_xe',
    'host': '192.168.42.69',
    'username': 'Nsindiso',
    'password': 'bulawayo',
    'secret':'bulwayo'
}

for device in (cisco_iosv, cisco_iosxe1, cisco_iosxe2):
    name = device['host'] + "_" + Date
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    output = net_connect.send_command('show running-config')
    with open(name+".txt", "w") as file:
        file.write(output) 
    print(device['host'] + " "+ "configuration has been backed up")





