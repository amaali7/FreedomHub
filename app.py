from FreedomHub.SystemD import SystemDUnit
from FreedomHub.Utilities import FileWithRootA, DebianPackage
from subprocess import run, PIPE, DEVNULL

# class FileWithRootB():

#     """
#         This class for write file with or without root access
#         depend on the state 
#     """

#     def __init__(self, fileName, path, rootAccess=False):
#         self.name = fileName
#         self.path = path
#         self.rootNeed = rootAccess

#     def readFile(self):
#         return open(self.path+self.name, 'r')
        
#     def modefyFile(self):
#         pass

#     def appendLines(self, text):
#         coolText = text.replace('\n', "\\n")
#         if self.rootNeed:
#             command = "echo \"" + coolText+"\" | sudo tee -a "+self.path+self.name
#             instruction =  run(command, shell=True, text=True, capture_output=DEVNULL)
#         else:
#             command = "echo \"" + coolText+"\" | tee -a "+self.path+self.name
#             instruction =  run(command, shell=True, text=True, capture_output=DEVNULL)
#         if instruction.returncode == 0:
#             return True
#         else:
#             return False
        

#     def overwrite(self, text):
        
#         coolText = text.replace('\n', "\\n")
#         if self.rootNeed:
#             move = "sudo mv "+self.path+self.name +" "+self.path+self.name+'.backup'
#             command = "echo \"" + coolText+"\" | sudo tee -a "+self.path+self.name
#             instruction_m =  run(move, shell=True, text=True, capture_output=DEVNULL)
#             instruction_c =  run(command, shell=True, text=True, capture_output=DEVNULL)
        
#         else:
#             move = "mv "+self.path+self.name +" "+self.path+self.name+'.backup'
#             command = "echo \"" + coolText+"\" | sudo tee -a "+self.path+self.name
#             instruction_m =  run(move, shell=True, text=True, capture_output=DEVNULL)
#             instruction_c =  run(command, shell=True, text=True, capture_output=DEVNULL)
        
#         if instruction_c.returncode == 0 and instruction_m.returncode == 0:
#             return True
#         else:
#             return False

from FreedomHub.wifiAccessControll import  WifiAP

wi = WifiAP()

wi.isc_dhcp_server_conf()