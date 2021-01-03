from FreedomHub.Utilities import DebianPackage, FileWithRoot
class Iptable():
    
    netfilter = DebianPackage('netfilter-persistent')
    iptables = DebianPackage('iptables-persistent')
    def __init__(self, config=None):
        self.packageStatus = self.__checkPakages__()
        self.softwareRequirementsState = all(value == True for value in self.packageStatus.values())
        self.Config = config
    def __checkPakages__(self):
        netfilter_state = False
        iptables_state = False
        if self.netfilter.isExist:
            netfilter_state = True

        else:
            netfilter_state = False

        if self.iptables.isExist:
            iptables_state = True
                    
        else:
            iptables_state = False
            print("dnsmasq not install!")
        return {'netfilter':netfilter_state, 'iptables':iptables_state}

        # def start(self):
        #     pass

        # def append(self):
        #     pass

        # def clearConfig(parameter_list):
        #     pass
