import os
from subprocess import run, DEVNULL
import re


class FileWithRoot():

    """
        This class for write file with or without root access
        depend on the state 
    """

    def __init__(self, fileName, path, rootAccess=False):
        self.name = fileName
        self.path = path
        self.rootNeed = rootAccess
        self.isExist = self.__isExist__()

    def __isExist__(self):
        return os.path.isfile(self.path+self.name)

    def readFile(self):
        if self.isExist:
            if self.rootNeed:
                command = "sudo cat "+self.path+self.name
                instruction =  run(command, shell=True, text=True, capture_output=True)
                if instruction.returncode == 0:
                    return instruction.stdout
                else:
                    return None
            else:
                return open(self.path+self.name, 'r').read()
        else:
            print("No such file")
        
        
        
    def modefyFile(self, pattern, replacement):
        if self.isExist:
            text = self.readFile()
            if text != None:
                for i in len(pattern):
                    changedStrings = re.sub(pattern[i],replacement[i],text)
                    text = changedStrings

                if self.overwrite(text):
                    return True
                else:
                    return False
            else:
                return False
        else:
            print("No such file")
                


    def appendLines(self, text):
        if self.isExist:
            coolText = text.replace('\n', "\\n")
            if self.rootNeed:
                command = "echo \"" + coolText+"\" | sudo tee -a "+self.path+self.name
                instruction =  run(command, shell=True, text=True, capture_output=DEVNULL)
            else:
                command = "echo \"" + coolText+"\" | tee -a "+self.path+self.name
                instruction =  run(command, shell=True, text=True, capture_output=DEVNULL)
            if instruction.returncode == 0:
                return True
            else:
                return False
            
        else:
            print('No such file')
        

    def overwrite(self, text):
        if self.isExist:
            coolText = text.replace('\n', "\\n")
            if self.rootNeed:
                move = "sudo mv "+self.path+self.name +" "+self.path+self.name+'.backup'
                command = "echo \"" + coolText+"\" > "+self.path+self.name
                instruction_m =  run(move, shell=True, text=True, capture_output=DEVNULL)
                instruction_c =  run(command, shell=True, text=True, capture_output=DEVNULL)
            
            else:
                move = "mv "+self.path+self.name +" "+self.path+self.name+'.backup'
                command = "sudo echo \"" + coolText+"\" > "+self.path+self.name
                instruction_m =  run(move, shell=True, text=True, capture_output=DEVNULL)
                instruction_c =  run(command, shell=True, text=True, capture_output=DEVNULL)
            
            if instruction_c.returncode == 0 and instruction_m.returncode == 0:
                return True
            else:
                return False

        else:
            print("No such file")
        


class DebianPackage():
    
    def __init__(self, packageName):

        self.packageName = packageName
        self.isExist = self.check()

    def check(self):
        dpkg_check = "dpkg -l "
        instraction = run(dpkg_check+self.packageName, shell=True, capture_output=DEVNULL)
        if instraction.returncode == 0:
            return True
        else:
            return False

    def remove(self):
        dpkg_check = "sudo apt remove "
        instraction = run(dpkg_check+self.packageName+" -y", shell=True, capture_output=DEVNULL)
        if instraction.returncode == 0:
            return True
        else:
            return False
