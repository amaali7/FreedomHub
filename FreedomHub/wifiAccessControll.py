from FreedomHub.SystemD import SystemDUnit

class WifiAP():
    
    hostapd = SystemDUnit('hostapd')
    isc_dhcp_server = SystemDUnit('isc-dhcp-server')

    def __init__(self, interface="wlan0"):
        self.packageStatus = self.__checkPakages__()
        self.softwareRequirementsState = all(value == True for value in self.packageStatus.values())
        self.interface= interface

    def __checkPakages__(self):
        hostapd_state = False
        isc_dhcp_server_state = False
        if self.hostapd.isExist:
            hostapd_state = True
        else:
            hostapd_state = False

        if self.isc_dhcp_server.isExist:
            isc_dhcp_server_state = True

        else:
            isc_dhcp_server_state = False
            print("dnsmasq not install!")
        return {'hostapd':hostapd_state, 'isc-dhcp-server':isc_dhcp_server_state}

    def refresh_services(self):
        if self.hostapd.reload() and self.isc_dhcp_server.reload():
            return True
        else:
            return False


    def isc_dhcp_server_conf(self, subnet="10.5.5.0", netmask="255.255.255.0", range_start="10.5.5.100",
                             range_end="10.5.5.254", routers="10.5.5.1", broadcast_address="10.5.5.255",
                              default_lease_time="600", max_lease_time="7200"):

        conf =("subnet "+subnet+" netmask "+netmask+" {"+'\n\t'+"range "+range_start+" "+range_end+";"+'\n\t'
        +"option routers "+routers+";"+'\n\t'+"option broadcast-address "+broadcast_address+";"+'\n\t'+
        "default-lease-time "+default_lease_time+";"+'\n\t'+"max-lease-time "+max_lease_time+";"+'\n\t'+"}")

        # conf = 'interface ' + self.interface+'\n'+'\tstatic ip_address='+self.serverIP+'\n'+"\tnohook wpa_supplicant"
        # dhcpcd_conf_file = FileWithRoot('dhcpd.conf','/etc/dhcp/dhcpd.conf',True)
        # dhcpcd_conf_file.appendLines(conf)   
        print(conf)
