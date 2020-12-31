from FreedomHub import SystemDUnit

class WifiAP():
    
    hostapd = SystemDUnit('hostapd')
    dnsmasq = SystemDUnit('dnsmasq')

    def __init__(self):
        self.packageStatus = self.__checkPakages__()
        self.softwareRequirementsState = all(value == True for value in self.packageStatus.values())

    def __checkPakages__(self):
        hostapd_state = False
        dnsmasq_state = False
        if self.hostapd.existanc:
            hostapd_state = True
            # self.hostapd.start
        else:
            hostapd_state = False
            print("hostapd not install!")

        if self.dnsmasq.existanc:
            dnsmasq_state = True
            # self.dnsmasq.start

        else:
            dnsmasq_state = False
            print("dnsmasq not install!")
        return {'hostapd':hostapd_state, 'dnsmasq':dnsmasq_state}

    def refresh_services(self):
        if self.hostapd.reload() and self.dnsmasq.reload():
            return True
        else:
            return False

