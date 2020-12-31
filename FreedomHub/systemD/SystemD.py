import os
from subprocess import run


class SystemDUnit():
    systemd_path ='/lib/systemd/system/'
    systemctl_cmd = 'sudo systemctl '
    def __init__(self, UnitName):
        
        self.name = UnitName
        self.existanc = self.__exist__()
        self.is_active = self.__isActive__()

    def __exist__(self):
        exist = False
        for root, dirs, files in os.walk(self.systemd_path):
            if self.name +'.service' in files:
                exist = True
        return exist

    def __isActive__(self):
        if self.existanc:
            instruction =  run(self.systemctl_cmd+'is-active '+self.name, shell=True, text=True, capture_output=True)
            if instruction.returncode == 0:
                if 'active' in instruction.stdout:
                    return True
            else:
                return False
            
    def start(self):
        if self.existanc:
            if not self.is_active:
                instruction =  run(self.systemctl_cmd+'start '+self.name, shell=True, text=True, capture_output=True)
                if instruction.returncode == 0:
                    return True
                else:
                    return False
            else:
                return None
    
    def stop(self):
        if self.existanc:
            if self.is_active:
                instruction =  run(self.systemctl_cmd+'stop '+self.name, shell=True, text=True, capture_output=True)
                if instruction.returncode == 0:
                    return True
                else:
                    return False
            else:
                return None

    def restart(self):
        if self.existanc:
            if self.is_active:
                instruction =  run(self.systemctl_cmd+'restart '+self.name, shell=True, text=True, capture_output=True)
                if instruction.returncode == 0:
                    return True
                else:
                    return False
            else:
                return None

    def reload(self):
        if self.existanc:
            if self.is_active:
                instruction =  run(self.systemctl_cmd+'reload '+self.name, shell=True, text=True, capture_output=True)
                if instruction.returncode == 0:
                    return True
                else:
                    return False
            else:
                return None

    def unmask(self):
        if self.existanc:    
            instruction =  run(self.systemctl_cmd+'unmask '+self.name, shell=True, text=True, capture_output=True)
            if instruction.returncode == 0:
                return True
            else:
                return False
        else:
            return None