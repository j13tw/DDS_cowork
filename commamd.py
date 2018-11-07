# Network_config.py
# Design By j13tw@yahoo.com.tw
# Only for Raspi network_configure

# include class to use
import Network_config 
NC = Network_config.Net_config()
NTP = Network_config.Ntp_config()
TC = Network_config.Time_config()
FS = Network_config.File_search()
WG = Network_config.Watchdog_config()
GPS = Network_config.Gps_time()
RB = Network_config.Reboot_system()

# inner Ethernet card
NC.eth0_dhcp()
NC.eth0_static(static_ip, netmask, gateway)
NC.eth0_static('192.168.0.200', '255.255.255.0', '192.168.0.1')
NC.eth0_dns('8.8.8.8')
NC.eth0_dual_dns('8.8.8.8', '8.8.4.4')

# usb to RJ45 Adapter
NC.eth1_dhcp()
NC.eth1_static(static_ip, netmask, gateway)
NC.eth1_static('192.168.0.200', '255.255.255.0', '192.168.0.1')
NC.eth1_dns('8.8.8.8')
NC.eth1_dual_dns('8.8.8.8', '8.8.4.4')

# Restart usb to RJ45 Adapter
# 004 -> USB bus_id
os.sys("./Rest.py -d 0004")

# Get usb to RJ45 Adapter Vender_ID
os.sys('lsusb | grep "Realtek" | cut -c16,17,18')

# NTP Server time check 
NTP.ntp_set('TIME.google.com')
--> "OK" / "ERROR"

# date / time control for user By hands
TC.get_now()
--> “2018-01-31 10:20:30" 
TC.date_set('2018', '07', '31')
--> "OK" 
TC.time_set('20', '10', '30')
--> "OK"

# get on path ".ini" file list
FS.ini_list() 
-> ["ABC.ini", "BCD.ini", "CDE.ini"]

# config watchdog monitor file
WG.watchdog_status()
--> ['cpu_short_load_status', 'cpu_short_load', 'cpu_middle_load_status', 'cpu_middle_load', 'cpu_long_load_status', 'cpu_long_load']
WG.set_cpu_load_short('45')
--> "OK" / "ERROR"
WG.set_cpu_load_middle('40')
--> "OK" / "ERROR"
WG.set_cpu_load_long('30')
--> "OK" / "ERROR"
WG.set_cpu_temperature('80')
--> "OK" / "ERROR"
WG.remove_cpu_load_short()
--> "OK" / "ERROR"
WG.remove_cpu_load_middle()
--> "OK" / "ERROR"
WG.remove_cpu_load_long()
--> "OK" / "ERROR"

# use gps to fix your device date & time
GPS.get_time()
-> ERROR is GPS-Sensor not found
-> OK is set System time OK 

# restart system command
RB.reboot()
