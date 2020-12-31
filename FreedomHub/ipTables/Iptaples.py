import os
from subprocess import run, DEVNULL


class FileWithRoot():

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
            command = "echo \"" + coolText+"\" | sudo tee -a "+self.path+self.name
            instruction =  run(command, shell=True, text=True, capture_output=DEVNULL)
        
        else:
            command = "echo \"" + coolText+"\" | tee -a "+self.path+self.name
            instruction =  run(command, shell=True, text=True, capture_output=DEVNULL)
        
        if instruction.returncode == 0:
            return True
        else:
            return False
