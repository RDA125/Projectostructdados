import os, os.path
from os import path


def Checkfile(fileName):

    if(path.exists(fileName)):

        if(os.stat(fileName).st_size == 0):
            f = open(fileName,"w")
            f.write("Nome-Email-Telefone\n")
            f.close()
        #endif

    else:
        f = open(fileName,"w")
        f.write("Nome-Email-Telefone\n")
        f.close()
    #endif
    
        
            
