import os
from subprocess import run


class FileWithRoot():

    def __init__(self, fileName, path):
        
        self.name = fileName
        self.path = path
        self.existanc = self.__exist__()

    def __exist__(self):
        exist = False
        for root, dirs, files in os.walk(self.path):
            if self.name in files:
                exist = True
        return exist

    def appendLines(self, text):
        text.replace('\\n', '\n').replace('\\t', '\t')
        cmd = "sudo \"echo -e "+ text+"\" >> "+self.path+self.name
        print(cmd)
        
        if self.existanc:
            instruction =  run(cmd, shell=True, text=True, capture_output=True)
            print(instruction.returncode)
        else:
            run("sudo touch "+self.path+self.name, shell=True, text=True, capture_output=True)
            instruction =  run(cmd, shell=True, text=True, capture_output=True)
            print(instruction.returncode)
        

    def overwrite(self):
        
        pass

rule = FileWithRoot('root.txt','/')

rule.appendLines("jlskfjakljakfjlksjfaksjdlkfljasdfjaslkjflks")