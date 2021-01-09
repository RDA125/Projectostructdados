import os, os.path
from os import path
import re
import unicodedata

def Checkfile(fileName):#add return for values
    p=0

    if(path.exists(fileName)):

        if(os.stat(fileName).st_size == 0):
            f = open(fileName,"w")
            f.write("Nome-Email-Telefone\n")
            f.close()
            return False
        
        else:
            f= open(fileName,'r')
            ln = f.readlines()

            for l in ln:
                p+=1

            if(p == 1):
                return False
            else:

                return True
        #endif

    else:
        f = open(fileName,"w")
        f.write("Nome-Email-Telefone\n")
        f.close()
        return False
    #endif

def UpdateHtml(fileName):
    f = open("users.txt","r")
    l = f.readline()
    numLn = f.readlines() 
    f.close
    
    nome,email,tel = l.split("-")

    f = open(fileName,"w")
    print ("<table>", file=f)
    print ("<style> table,th,td{border: 2px solid black; border-collapse: collapse; padding:5px; text-align:center}</style>", file=f)
    print("<h1>Lista de utilizadores<h1>", file=f)
    print("<tr><th>%s</th><th>%s</th><th>%s</th></tr>" % (nome, email, tel), file=f)

    for ln in numLn:
        ln = ln.rstrip('\n')
        Nome,Email,Telefone = ln.split("-")
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (Nome, Email, Telefone), file=f)
    #endfor

    print("</table>",file=f)
    f.close()

def UpdateFile(filename,numLn):
    f = open(filename,"w")
    f.write("Nome-Email-Telefone\n")
    
    for ln in numLn:
        ln = ln.rstrip('\n')
        Nome,Email,Telefone = ln.split("-")
        print( Nome,Email,Telefone, file=f,sep="-",end='\n')
    
    f.flush()
    f.close

    UpdateHtml("teste.html")

def VerfName(name):
    #remover acentos
    name = unicodedata.normalize('NFD', name)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    if re.search("^[a-zA-Z][^0-9]+$", name):
        return True
    return False


def VerfExist(check):
    f = open("users.txt","r")
    l = f.readline() 
    numLn = f.readlines()
    
    for ln in numLn:
        ln = ln.rstrip('\n')
        ln = ln.lower()
        ln = ln.split('-')
        

        if(str(check).lower() in ln):
            return True
        #endif

    return False

def VerfEmail(email):
    if re.search(r"^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
        return True
    return False
        
            
