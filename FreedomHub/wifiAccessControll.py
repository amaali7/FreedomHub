from FreedomHub.SystemD import SystemDUnit
from FreedomHub.Utilities import FileWithRoot
import re
class WifiAP():
    """
        Check your wireless dongle supports AP mode (Access Point)
    """
    hostapd = SystemDUnit('hostapd')
    isc_dhcp_server = SystemDUnit('isc-dhcp-server')

    def __init__(self, interface="wlan0", accept_mac_file='/etc/hostapd/hostapd.accept', deny_mac_file='/etc/hostapd/hostapd.deny'):
    
        self.packageStatus = self.__checkPakages__()
        self.softwareRequirementsState = all(value == True for value in self.packageStatus.values())
        self.interface= interface
        self.hostapd_cofig = self.__hostapd_config__()
        self.accept_mac_file = accept_mac_file
        self.deny_mac_file = deny_mac_file



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


    def __getIp__(self,ip):
        pattern = re.compile(r'^\d*\.\d*\.\d*\.\d*$')
        match = pattern.search(ip)
        if match:
            return match.string
        else:
            return None
        
    def __hostapd_config__(self):
        hostapd_config = FileWithRoot('hostapd.conf','/etc/hostapd/',True)
        acept_config = FileWithRoot('hostapd.conf','/etc/hostapd/',True)
        denay_config = FileWithRoot('hostapd.conf','/etc/hostapd/',True)
        return hostapd_config.readFile

    def refresh_services(self):
        if self.hostapd.reload() and self.isc_dhcp_server.reload():
            return True
        else:
            return False

    def setInterfaceIp(self,ipAddress,netmask):
        path ='/etc/network/'
        name = 'interfaces'
        ins = FileWithRoot(name, path, True)
        # Remove the dhcp entry 
        ins.modefyFile(['iface default inet dhcp'],['#iface default inet dhcp'])
        ip = self.__getIp__(ipAddress)
        net = self.__getIp__(netmask)
        # Configures a static IP address. 
        if ip and net:
            conf = "iface wlan0 inet static"+'\n\t'+"address "+ip+'\n\t'+"netmask "+net
            
            if ins.appendLines(conf):
                return True
            else:
                return False
        else:
            return False
        



    def isc_dhcp_server_conf(self, subnet="10.5.5.0", netmask="255.255.255.0", range_start="10.5.5.100",
                             range_end="10.5.5.254", routers="10.5.5.1", broadcast_address="10.5.5.255",
                              default_lease_time="600", max_lease_time="7200"):
        # /etc/dhcp/dhcpd.conf
        name = 'dhcpd.conf'
        path = '/etc/dhcp/'
        ins = FileWithRoot(name, path, True)
        # Remove the dhcp entry and configure internal subnet
        ins.modefyFile(['option domain-name','option domain-name-servers','#authoritative'],
                        ['#option domain-name','#option domain-name-servers','authoritative'])
        
        conf =("subnet "+subnet+" netmask "+netmask+" {"+'\n\t'+"range "+range_start+" "+range_end+";"+'\n\t'
        +"option routers "+routers+";"+'\n\t'+"option broadcast-address "+broadcast_address+";"+'\n\t'+
        "default-lease-time "+default_lease_time+";"+'\n\t'+"max-lease-time "+max_lease_time+";"+'\n\t'+"}")
        main_conf = ins.appendLines(conf)   
        # /etc/default/isc-dhcp-server
        isc = FileWithRoot('isc-dhcp-server','/etc/default/',True)
        isc.modefyFile(r'INTERFACES=\".\"','INTERFACES=\"'+self.interface+'\"')

        if main_conf:
            return True
        else:
            return False


    def confgure_hostapd(self,ssid='FreedomHub',password='freedomhub',
            country_code='SD',hw_mode='g',channel='0', macaddr_acl='1',
            wpa='2',wpa_key_mgmt='WPA-PSK',wpa_pairwise='TKIP', rsn_pairwise='CCMP',
            extra_conf=[],extra_conf_value=[]):
        
        conf = f'interface={self.interface}\ndriver=hostap\nssid={ssid}\ncountry_code={country_code}\nhw_mode={hw_mode}\nchannel={channel}\nmacaddr_acl={macaddr_acl}\ndeny_mac_file={self.deny_mac_file}\nauth_algs=1\nwpa={wpa}\nwpa_passphrase={password}\nwpa_key_mgmt={wpa_key_mgmt}\nwpa_pairwise={wpa_pairwise}\nrsn_pairwise={rsn_pairwise}'
        if len(extra_conf)>0:
            for con,val in zip(extra_conf,extra_conf_value):
                conf+=f'\n{con}={val}'

        print( conf)