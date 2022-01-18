import os
import uuid
from os import listdir
from os.path import isfile, join, isdir
import pathlib


class AddUuid():
    
    def getAllFilesRecursive(self, root):
        files = [ join(root,f) for f in listdir(root) if isfile(join(root,f))]
        dirs = [ d for d in listdir(root) if isdir(join(root,d))]
        for d in dirs:
            files_in_d = self.getAllFilesRecursive(join(root,d))
            if files_in_d:
                for f in files_in_d:
                    files.append(join(root,f))
        return files
    
    def generateUUid(self):
        try:
            currentFilePath = pathlib.Path(__file__).parent.resolve()
            files = self.getAllFilesRecursive(os.path.join(currentFilePath,'..','NetworkElement','ApiDefinition'))
            for file in files:
                if '.yaml' in file:
                    file_output = file.replace('.yaml', '_output.yaml')
                    original = open(file,"r")
                    new = open(file_output,"a")
                
                    lastline = '';
                    for line in original:
                        if 'apis:' in line and '#' not in line and 'uuid' not in lastline:
                            new.write(line.replace('apis:', 'uuid: ' + str(uuid.uuid4()) + '\n        apis:'))
                        else:
                            new.write(line)
                        lastline = line
                
                    original.close()
                    new.close()
                    
                    # delete the original file
                    os.remove(file)
                    
                    # rename the new file
                    os.rename(file_output, file)
            
            print('completed')
        
        except Exception as exc:
            print(exc)
    
