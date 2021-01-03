import os
from subprocess import run, DEVNULL


class FileWithRootA():

    """
        This class for write file with or without root access
        depend on the state 
    """

    def __init__(self, fileName, path, rootAccess=False):
        self.name = fileName
        self.path = path
        self.rootNeed = rootAccess

    def appendLines(self, text):

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
        

    def overwrite(self, text):
        
        coolText = text.replace('\n', "\\n")
        if self.rootNeed:
            move = "sudo mv "+self.path+self.name +" "+self.path+self.name+'.backup'
            command = "echo \"" + coolText+"\" | sudo tee -a "+self.path+self.name
            instruction_m =  run(move, shell=True, text=True, capture_output=DEVNULL)
            instruction_c =  run(command, shell=True, text=True, capture_output=DEVNULL)
        
        else:
            move = "mv "+self.path+self.name +" "+self.path+self.name+'.backup'
            command = "echo \"" + coolText+"\" | sudo tee -a "+self.path+self.name
            instruction_m =  run(move, shell=True, text=True, capture_output=DEVNULL)
            instruction_c =  run(command, shell=True, text=True, capture_output=DEVNULL)
        
        if instruction_c.returncode == 0 and instruction_m.returncode == 0:
            return True
        else:
            return False


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
