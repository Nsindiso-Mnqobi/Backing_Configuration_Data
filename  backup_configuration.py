from netmiko import ConnectHandler
from datetime import date
import csv

today= date.today()
Date = str(today.strftime("%d_f%m_%y"))

class Backup_Configuration:
    
    def __init__(self, device_type, hostfa, username,password,secret,hostname):
        self.hostname = hostname
        self.device_type = device_type
        self.host=host
        self.username= username
        self.password = password
        self.secret = secret

    def get_backup(self):
        Device = {
            'device_type': self.device_type,
            'host':   self.host,
            'username': self.username,
            'password': self.password,
            'secret': self.secret
        }

        name = self.hostname  + "_" + Date
        net_connect = ConnectHandler(**Device)
        net_connect.enable()
        output = net_connect.send_command('show running-config')
        with open(name+".txt", "w") as file:
            file.write(output) 
        print(self.hostname + " "+ "configuration has been backed up")

if  __name__ == "__main__":
    
    with open("host_details.csv") as host_details:
        host_list = list(csv.reader(host_details))
        for row in host_list:
            device_type=row[0]
            host=row[1]
            username = row[2] 
            password = row[3] 
            secret = row[4]
            host_name = row[5]
            backup = Backup_Configuration(device_type, host, username, password, secret, host_name)
            backup.get_backup()




