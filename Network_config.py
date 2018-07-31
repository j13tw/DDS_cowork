import os, sys
import glob

class File_search():
    def __init__(self):
        pass

    def ini_list(self):
        self.ini_table = glob.glob('/etc/network/*')
        for x in range(0, len(self.ini_table)):
            self.ini_table[x] = self.ini_table[x].split('/')[3]
        return  self.ini_table

class Time_config():
    def __init__(self):
        pass

    def date_set(self, year, month, date):
        self.date_command = 'sudo date -s ' + year + month + date
        os.system(self.date_command)
    
    def time_set(self, hour, minute, second):
        self.time_command = 'sudo date -s ' + hour + ':' + minute + ':' + second
        os.system(self.time_command)

class Ntp_config():
    def __init__(self):
        os.system('timedatectl set-timezone "Asia/Taipei"')
        os.system('sudo /etc/init.d/ntp stop')
        try:
            self.f = open('/etc/network/ntp_log', 'r')
            self.ntp_host = self.f.read()
            self.ntp_command = 'sudo ntpdate ' + self.ntp_host
            self.f.close()
            os.system(self.ntp_command)
        except:
            os.system('sudo apt-get install ntpdate')
            self.f = open('/etc/network/ntp_log', 'w')
            self.f.write('TOCK.stdtime.gov.tw')
            self.f.close()
            self.f = open('/etc/network/ntp_log', 'r')
            self.ntp_host = self.f.read()
            self.ntp_command = 'sudo ntpdate ' + self.ntp_host
            self.f.close()
    def ntp_set(self, ntp_host):
        self.ntp_command = 'sudo ntpdate ' + ntp_host
        self.f = open('/etc/network/ntp_log', 'w')
        self.f.write(ntp_host)
        self.f.close()
        os.system(self.ntp_command)

class Net_config():
    def __init__(self):
        try:
            self.f = open('/etc/network/interfaces.bak', 'r')
            os.system('sudo cp /etc/network/interfaces.bak /etc/network/interfaces')
            print(self.f.read())
            self.f.close()
        except:
            self.f = open('/etc/network/interfaces.bak', 'w')
            self.f.write('auto lo eth0\n\n')
            self.f.write('iface eth0 inet dhcp\n')
            self.f.write('                              \n')
            self.f.write('                              \n')
            self.f.write('                              \n')
            self.f.write('                              \n')
            self.f.write('                              \n')
            self.f.write('allow-hotplug eth1\n\n')
            self.f.write('iface eth1 inet dhcp\n')
            self.f.write('                              \n')
            self.f.write('                              \n')
            self.f.write('                              \n')
            self.f.write('                              \n')
            self.f.write('                              \n')
            self.f.close()
            os.system('sudo cp /etc/network/interfaces.bak /etc/network/interfaces')
            self.f = open('/etc/network/interfaces', 'r')
            print(self.f.read())
            self.f.close()

    def eth0_dhcp(self):
        self.f = open('/etc/network/interfaces', 'r+')
        self.f.write('auto lo eth0\n\n')
        self.f.write('iface eth0 inet dhcp\n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.close()
        os.system('sudo ifdown eth0')
        os.system('sudo ifup eth0')
        os.system('sudo cp /etc/network/interfaces /etc/network/interfaces.bak')
        self.f = open('/etc/network/interfaces', 'r')
        print(self.f.read())
        self.f.close()

    def eth1_dhcp(self):
        self.f = open('/etc/network/interfaces', 'r+')
        self.f.seek(190)
        self.f.write('allow-hotplug eth1\n\n')
        self.f.write('iface eth1 inet dhcp\n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.close()
        os.system('lsusb | grep "Realtek" | cut -c16,17,18 >/tmp/usb.txt')
        self.usb_id = open('/tmp/usb.txt')
        self.usb_reset = 'sudo python /etc/network/Restusb.py -d ' + self.usb_id.read()
        os.system(self.usb_reset)
        os.system('sudo cp /etc/network/interfaces /etc/network/interfaces.bak')
        self.f = open('/etc/network/interfaces', 'r')
        print(self.f.read())
        self.f.close()

    def eth0_static(self, ip, netmask, gateway):
        self.f = open('/etc/network/interfaces', 'r+')
        self.f.write('auto lo eth0\n\n')
        self.f.write('iface eth0 inet static\n')
        self.f.write('address ')
        self.f.write(ip)
        self.f.write('\n')
        self.f.write('netmask ')
        self.f.write(netmask)
        self.f.write('\n')
        self.f.write('gateway ')
        self.f.write(gateway)
        self.f.write('\n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.close()
        os.system('sudo ifdown eth0')
        os.system('sudo ifup eth0')
        os.system('sudo cp /etc/network/interfaces /etc/network/interfaces.bak')
        self.f = open('/etc/network/interfaces', 'r')
        print(self.f.read())
        self.f.close()

    def eth1_static(self, ip, netmask, gateway):
        self.f = open('/etc/network/interfaces', 'r+')
        self.f.seek(190)
        self.f.write('allow-hotplug eth1\n\n')
        self.f.write('iface eth1 inet static\n')
        self.f.write('address ')
        self.f.write(ip)
        self.f.write('\n')
        self.f.write('netmask ')
        self.f.write(netmask)
        self.f.write('\n')
        self.f.write('gateway ')
        self.f.write(gateway)
        self.f.write('\n')
        self.f.write('                              \n')
        self.f.write('                              \n')
        self.f.close()
        os.system('lsusb | grep "Realtek" | cut -c16,17,18 >/tmp/usb.txt')
        self.usb_id = open('/tmp/usb.txt')
        self.usb_reset = 'sudo python /etc/network/Restusb.py -d ' + self.usb_id.read()
        os.system(self.usb_reset)
        os.system('sudo cp /etc/network/interfaces /etc/network/interfaces.bak')
        self.f = open('/etc/network/interfaces', 'r')
        print(self.f.read())
        self.f.close()

    def eth0_dns(self, dns):
        self.f = open('/etc/network/interfaces', 'r+')
        self.f.seek(101)
        self.f.write('dns-nameserver ')
        self.f.write(dns)
        self.f.write('\n')
        self.f.write('                              \n')
        os.system('sudo ifdown eth0')
        os.system('sudo ifup eth0')
        os.system('sudo cp /etc/network/interfaces /etc/network/interfaces.bak')
        self.f = open('/etc/network/interfaces', 'r')
        print(self.f.read())
        self.f.close()

    def eth1_dns(self, dns):
        self.f = open('/etc/network/interfaces', 'r+')
        self.f.seek(296)
        self.f.write('dns-nameserver ')
        self.f.write(dns)
        self.f.write('\n')
        self.f.write('                              \n')
        os.system('lsusb | grep "Realtek" | cut -c16,17,18 >/tmp/usb.txt')
        self.usb_id = open('/tmp/usb.txt')
        self.usb_reset = 'sudo python /etc/network/Restusb.py -d ' + self.usb_id.read()
        os.system(self.usb_reset)
        self.f = open('/etc/network/interfaces', 'r')
        print(self.f.read())
        self.f.close()
    
    def eth0_dual_dns(self, dns, sub_dns):
        self.f = open('/etc/network/interfaces', 'r+')
        self.f.seek(101)
        self.f.write('dns-nameserver ')
        self.f.write(dns)
        self.f.write('\n')
        self.f.write('dns-nameserver ')
        self.f.write(sub_dns)
        self.f.write('\n')
        os.system('sudo ifdown eth0')
        os.system('sudo ifup eth0')
        self.f = open('/etc/network/interfaces', 'r')
        print(self.f.read())
        self.f.close()
    
    def eth1_dual_dns(self, dns, sub_dns):
        self.f = open('/etc/network/interfaces', 'r+')
        self.f.seek(296)
        self.f.write('dns-nameserver ')
        self.f.write(dns)
        self.f.write('\n')
        self.f.write('dns-nameserver ')
        self.f.write(sub_dns)
        self.f.write('\n')
        os.system('lsusb | grep "Realtek" | cut -c16,17,18 >/tmp/usb.txt')
        self.usb_id = open('/tmp/usb.txt')
        self.usb_reset = 'sudo python /etc/network/Restusb.py -d ' + self.usb_id.read()
        os.system(self.usb_reset)
        self.f = open('/etc/network/interfaces', 'r')
        print(self.f.read())
        self.f.close()