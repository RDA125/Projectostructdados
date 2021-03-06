import os, os.path
from os import path
from MenuCreator.CreateMenu import WaitEnter,Clear
import re
import unicodedata

def Orde(numLn,User=False,Nom=False,Top=False,Lk=False,Oper=False): #ordena por id
    for i in range(len(numLn)):
        numLn[i] = numLn[i].rstrip('\n')
        numLn[i] = numLn[i].strip()
        numLn[i] = numLn[i].split('-')
    #endfor

    if(Nom):
        numLn.sort(key= lambda x: str(x[2]))

    elif(Top):
        numLn.sort(key= lambda x: str(x[3]))

    elif(Lk):
        numLn.sort(key= lambda x: int(x[-1]),reverse=True)

    elif(Oper):
        numLn.sort(key= lambda x: str(x[4]))
    
    elif(User):
        numLn.sort(key= lambda x: str(x[0]))

    else:
        numLn.sort(key= lambda x: int(x[0]))

    for i in range(len(numLn)):
        numLn[i] = '-'.join(numLn[i])
    #endfor

    return numLn
#end

#User specific verf

def Checkfile(fileName):

    if(path.exists(fileName)):

        if(os.stat(fileName).st_size == 0):
            f = open(fileName,"w")
            f.write("Nome-Email-Número-Telefone-Operadora\n")
            f.close()
            return False
        
        else:
            f= open(fileName,'r')
            ln = f.readlines()
            f.close()

            if(len(ln) == 1):
                return False
            else:

                return True
        #endif

    else:
        f = open(fileName,"w")
        f.write("Nome-Email-Número-Telefone-Operadora\n")
        f.close()
        return False
    #endif


def UpdateHtml(fileName):
    f = open("users.txt","r")
    l = f.readline()
    numLn = f.readlines() 
    f.close
    
    nome,email,num,tel,oper = l.split("-")

    f = open(fileName,"w")
    print("<title>Lista Users</title>", file=f)
    print ("<table>", file=f)
    print ("<style> table,th,td{border: 2px solid black; border-collapse: collapse; padding:5px; text-align:center}</style>", file=f)
    print("<h1>Lista de utilizadores<h1>", file=f)
    print("<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % (nome, email, num, tel, oper), file=f)

    for ln in numLn:
        ln = ln.rstrip('\n')
        Nome,Email,Num,Telefone,Oper = ln.split("-")
        print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (Nome, Email, Num, Telefone, Oper), file=f)
    #endfor

    print("</table>",file=f)
    f.close()


def UpdateFile(filename,numLn):
    f = open(filename,"w")
    f.write("Nome-Email-Número-Telefone-Operadora\n")
    
    for ln in numLn:
        ln = ln.rstrip('\n')
        Nome,Email,Num,Telefone,Oper = ln.split("-")
        print( Nome,Email,Num,Telefone,Oper, file=f,sep="-",end='\n')
    #endfor

    f.flush()
    f.close

    UpdateHtml("Users.html")


def VerfName(name):
    #remover acentos
    name = unicodedata.normalize('NFD', name)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    if re.search("^[a-zA-Z][^0-9]+$", name):
        return True
    #endif
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
    #endfor
    return False


def VerfEmail(email):
    if re.search(r"^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
        return True
    #endif
    return False
        
            
def VerfOper(oper):
    OperTel = ['NOS','VODAFONE','MEO','NOWO']

    if re.search("^[a-zA-Z][^0-9]+$", oper):

        for OpT in OperTel:

            if(oper in OpT):
                return True
            #endif
        #endfor
    #endif
    return False

def GetName(email,num):
    f = 0
    f = open("users.txt","r")
    l = f.readline() 
    numLn = f.readlines()
    
    for ln in numLn:
        ln = ln.rstrip('\n')
        ln = ln.split('-')
        
        if((str(email).lower() in ln ) and (str(num) in ln)):
            return ln[0]
        #endif
    #endfor

    if(f == 0):
        return None
    #endif


def GroupUtil(numLn,Nom=False,Oper=False):
    count=0

    if(Nom):
        nomes = []
        print("Agrupado por Nomes\n")
        
        Orde(numLn,True)

        for ln in numLn:
            nome,email,num,tel,oper = ln.split('-')
            nomes.append(nome)
        #endfor

        nomes = list(dict.fromkeys(nomes))#remove nomes repetidos

        for nome in nomes:
            for ln in numLn:
                ln = ln.split('-')
                aux = re.compile(nome)
                
                if(aux.search(ln[0])):
                    count+=1
                #endif
            #endfor
        
            print(nome,": ",count,"\n")
            count=0
        #endfor
        WaitEnter()
        return 

    elif(Oper):
        OperTel = ['NOS','VODAFONE','MEO','NOWO']
        print("Numero de Utilizadores por Operadora\n")
        
        Orde(numLn,True)

        for OpTl in OperTel:
            for ln in numLn:
                ln = ln.split('-')
                
                if(ln[4] == OpTl):
                    count+=1
                #endif

            #endfor
        
            print(OpTl,": ",count,"\n")
            count=0
        #endfor
        WaitEnter()
        return 
    #endif


#Tweet specific verf

def CheckfileTw(fileName):

    if(path.exists(fileName)):

        if(os.stat(fileName).st_size == 0):
            f = open(fileName,"w")
            f.write("Id-IdResp-Nome-Tópico-Tweet-Likes\n")
            f.close()
            return False
        
        else:
            f= open(fileName,'r')
            ln = f.readlines()
            f.close()

            if(len(ln) == 1):
                return False
            else:

                return True
        #endif

    else:
        f = open(fileName,"w")
        f.write("Id-IdResp-Nome-Tópico-Tweet-Likes\n")
        f.close()
        return False
    #endif


def VerfTweet(tweet):
    TwLen = len(tweet)

    if(TwLen<= 0 or TwLen>280):
        return False
    else:
        return True
    #endif


def UpdateHtmlTw(fileName):
    f = open("tweets.txt","r")
    l = f.readline()
    numLn = f.readlines() 
    f.close
    
    idtw,idResp,nome,tp,tw,lk = l.split("-")

    f = open(fileName,"w")
    print("<title>Lista Tweets</title>", file=f)
    print ("<table>", file=f)
    print ("<style> table,th,td{border: 2px solid black; border-collapse: collapse; padding:5px; text-align:center}</style>", file=f)
    print("<h1>Lista de Tweets<h1>", file=f)
    print("<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % (idtw,nome,tp,tw,lk), file=f)

    for ln in numLn:
        ln = ln.rstrip('\n')
        Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
        print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (Id,Nome,Tp,Tw,Lk), file=f)
    #endfor

    print("</table>",file=f)
    f.close()


def UpdateFileTw(filename,numLn):
    f = open(filename,"w")
    f.write("Id-IdResp-Nome-Tópico-Tweet-Likes\n")
    level=0
    indentation = 0

    for i in range(len(numLn)):
        numLn[i] = numLn[i].rstrip('\n')
        numLn[i] = numLn[i].strip()
        antes = numLn[i].split('-')

        if(i+1<len(numLn)):
            numLn[i+1] = numLn[i+1].rstrip('\n')
            numLn[i+1] = numLn[i+1].strip()
            frente = numLn[i+1].split('-')
        #endif

        indentation = '\t' * level
        print(indentation,numLn[i],file=f,end='\n')

        if((i+1)<len(numLn)):
            if(frente[1] == "0"):
                level = 0
            elif(frente[1]>antes[1]):
                level+=1
            elif(frente[1]<antes[1]):
                level-=1
        elif((i+1)>=len(numLn)):
            break
        #endif
    #endfor


    f.flush()
    f.close

    UpdateHtmlTw("Tweets.html")
#end

def GroupTw(numLn,Nom=False,Top=False,Lk=False):
    count=0

    if(Nom):
        nomes = []
        print("Numero de Tweets por User\n")
        
        Orde(numLn,False,True)

        for ln in numLn:
            id,idresp,nome,top,tw,lk = ln.split('-')
            nomes.append(nome)
        #endfor

        nomes = list(dict.fromkeys(nomes))#remove nomes repetidos

        for nome in nomes:
            for ln in numLn:
                ln = ln.split('-')
                
                if(ln[2] == nome):
                    count+=1
                #endif

            #endfor
        
            print(nome,": ",count,"\n")
            count=0
        #endfor
        WaitEnter()
        return 

    elif(Top):
        topicos = []
        print("Numero de Tweets por Tópico\n")
        
        Orde(numLn,False,False,True)

        for ln in numLn:
            id,idresp,nome,top,tw,lk = ln.split('-')
            topicos.append(top)
        #endfor

        topicos = list(dict.fromkeys(topicos))#remove topicos repetidos

        for topico in topicos:
            for ln in numLn:
                ln = ln.split('-')
                
                if(ln[3] == topico):
                    count+=1
                #endif

            #endfor
        
            print(topico,": ",count,"\n")
            count=0
        #endfor
        WaitEnter()
        return 
    
    elif(Lk):
        lks = [0,5,10,25,50,75,100]
        print("Numero de likes dos tweets superior a: \n")
        
        Orde(numLn,False,False,False,True)

        for lk in lks:
            for ln in numLn:
                ln = ln.split('-')
                
                if(int(ln[5]) >= lk):
                    count+=1
                #endif

            #endfor
        
            print(lk,"Likes: ",count,"\n")
            count=0
        #endfor
        WaitEnter()
        return 
    #endif