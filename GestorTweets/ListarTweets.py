from os import system
from Validacao.ValidarDados import CheckfileTw, Orde, UpdateFileTw
from GestorTweets import RespondeTweet
from MenuCreator.CreateMenu import Clear,PrintMenu
import textwrap
import msvcrt

def GivLike(numLn):
    while True:
        print("Aumentar likes\n")
        i=0
        found = 0
        try:
            sId = int(input("\033[1A\nInsira o Id do Tweet para dar like: \033[K"))
        except ValueError:
            sId=-1
            print('\033[1A'+input("Tem que ser inteiro")+'\033[K',end="\r")
            print('\033[1A                            \033[K',end="\r")
            print('\033[3A                            \033[K',end="\r")

        if(sId>0):

            for ln in numLn:
                ln = ln.split("-")

                if(sId == int(ln[0])):
                    ln[5]= str(int(ln[5])+1)
                    ln='-'.join(ln)
                    ln+='\n'
                    numLn[i]=ln
                    UpdateFileTw("tweets.txt",numLn)
                    return
                #endif
                i+=1
            #endfor
            if(found == 0):
                print('\033[1A'+input("Tweet não existe")+'\033[K',end="\r")
                Clear()
            #endif

        elif(sId == -1):
            Clear()

        else:
            print('\033[1A'+input("Id de Tweet inválido")+'\033[K',end="\r")
            Clear()
        #endif
    #endwhile
#end        


def showOrd(numLn):
    while True:

        op = PrintMenu("Ordenação de Tweets",["Id","Nome","Tópico","Likes"],4,"Voltar atrás")

        if(op == 1):
            print("\nOrdenação por Id\n")

            Orde(numLn)
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endf
            input("Prima enter...")
            Clear()

        elif(op == 2):
            print("\nOrdenação por Nome\n")

            Orde(numLn,True)
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endf
            input("Prima enter...")
            Clear()

        elif(op == 3):
            print("\nOrdenação por Tópico\n")

            Orde(numLn,False,True)
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endf
            input("Prima enter...")
            Clear()

        elif(op == 4):
            print("\nOrdenação por Likes\n")

            Orde(numLn,False,False,True)
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endf
            input("Prima enter...")
            Clear()

        elif(op == 0):
            Clear()
            return
        #endif
    #endwhile

def ListarTw(fileName,name=""):
    if(CheckfileTw("tweets.txt")):
        while True:
            print("Listagem dos Tweets\n")
            opc=-1

            f = open("Tweets.txt","r")
            l = f.readline()
            numLn = f.readlines() 
            f.close
            
            idtw,idresp,nome,tp,tw,lk = l.split("-")
        
            print("%-5s  %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))

            for ln in numLn:
                ln = ln.rstrip('\n')
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
               
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endfor
            print("\n")
            
            if(name != ""):
               
                opc = PrintMenu("",["Responder","Dar like","Organizar","Ver Html"],4,"Voltar atrás")

                if(opc == 1):
                    Clear()
                    RespondeTweet.RespTw(name)
                    opc = -1

                elif(opc == 2):
                    Clear()
                    GivLike(numLn)
                    opc=-1
                elif(opc == 3):
                    Clear()
                    showOrd(numLn)#ordenar Id Nome topico Like

                elif(opc == 4):
                    system(fileName)
                    Clear()
                    break
                elif(opc == 0):
                    Clear()
                    break
                else:
                    Clear()
                #endif
            
            else:
                opc = PrintMenu("",["Organizar","Ver Html"],2,"Voltar atrás")

                if(opc == 1):
                    Clear()
                    showOrd(numLn)

                elif(opc == 2):
                    system(fileName)
                    Clear()
                    break
                elif(opc == 0):
                    Clear()
                    break
                else:
                    Clear()
                #endif
        #endwhile
    else:
        input("Não existe Valores para serem listados.")
        Clear()
    #endif

def ListarUTw(name=""):
    if(CheckfileTw("tweets.txt")):
        print("Listagem dos Tweets\n")

        f = open("Tweets.txt","r")
        l = f.readline()
        numLn = f.readlines() 
        f.close

        idtw,idresp,nome,tp,tw,lk = l.split("-")
        print("%-5s %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))

        Orde(numLn) #(list,Nome=false,Top=false,likes=false) default = id
        if(name != ""):
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                if(name.lower() == Nome.lower()):
                    print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
                #endif
            #endfor
        else:
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endfor
        #endif

        input("\nPrima enter....")
        Clear()
    else:
        input("Não tem tweets para listar")
        Clear()
    #endif
