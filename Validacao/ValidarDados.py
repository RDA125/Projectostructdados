import os, os.path
from os import path
import re
import unicodedata

def Checkfile(fileName):#add return for values

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


def VerfName(name):
    #remover acentos
    name = unicodedata.normalize('NFD', name)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    if re.search("^[a-zA-Z][^0-9]+$", name):
        return True
    return False


def VerfEmail(email):
    if re.search(r"^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
        return True
    return False
        
            
