import os
from subprocess import run
from FreedomHub.Utilities import DebianPackage


class SystemDUnit():
    systemctl_cmd = 'sudo systemctl '
    def __init__(self, UnitName):
        
        self.name = UnitName
        self.isExist = self.__exist__()
        self.isActive = self.__isActive__()

    def __exist__(self):
        pack = DebianPackage(self.name)
        if pack.isExist:
            return True
        else:
            return False

    def __isActive__(self):
        if self.isExist:
            instruction =  run(self.systemctl_cmd+'is-active '+self.name, shell=True, text=True, capture_output=True)
            if instruction.returncode == 0:
                if 'active' in instruction.stdout:
                    return True
            else:
                return False
            
    def start(self):
        if self.isExist:
            if not self.isActive:
                instruction =  run(self.systemctl_cmd+'start '+self.name, shell=True, text=True, capture_output=True)
                if instruction.returncode == 0:
                    return True
                else:
                    return False
            else:
                return None
    
    def stop(self):
        if self.isExist:
            if self.isActive:
                instruction =  run(self.systemctl_cmd+'stop '+self.name, shell=True, text=True, capture_output=True)
                if instruction.returncode == 0:
                    return True
                else:
                    return False
            else:
                return None

    def restart(self):
        if self.isExist:
            if self.isActive:
                instruction =  run(self.systemctl_cmd+'restart '+self.name, shell=True, text=True, capture_output=True)
                if instruction.returncode == 0:
                    return True
                else:
                    return False
            else:
                return None

    def reload(self):
        if self.isExist:
            if self.isActive:
                instruction =  run(self.systemctl_cmd+'reload '+self.name, shell=True, text=True, capture_output=True)
                if instruction.returncode == 0:
                    return True
                else:
                    return False
            else:
                return None

    def unmask(self):
        if self.isExist:    
            instruction =  run(self.systemctl_cmd+'unmask '+self.name, shell=True, text=True, capture_output=True)
            if instruction.returncode == 0:
                return True
            else:
                return False
        else:
            return None