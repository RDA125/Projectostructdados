from os import system
from Validacao.ValidarDados import CheckfileTw, Orde, UpdateFileTw
from GestorTweets import RespondeTweet
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
                system('cls')
            #endif

        elif(sId == -1):
            system('cls')

        else:
            print('\033[1A'+input("Id de Tweet inválido")+'\033[K',end="\r")
            system('cls')
        #endif
    #endwhile
#end        


def showOrd(numLn):
    while True:
        print("Ordenação de Tweets\n")
        try:
            op = int(input("\033[1A\n1-Id\n2-Nome\n3-Tópico\n4-Likes\n0-Voltar atrás\n\033[K"))
        except ValueError:
            print('\033[1A'+input("Tem que ser inteiro")+'\033[K',end="\r")
            print('\033[1A                            \033[K',end="\r")
            print('\033[3A                            \033[K',end="\r")

        if(op == 1):
            print("\nOrdenação por Id\n")

            Orde(numLn)
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endf
            input("Prima enter...")
            system('cls')

        elif(op == 2):
            print("\nOrdenação por Nome\n")

            Orde(numLn,True)
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endf
            input("Prima enter...")
            system('cls')

        elif(op == 3):
            print("\nOrdenação por Tópico\n")

            Orde(numLn,False,True)
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endf
            input("Prima enter...")
            system('cls')

        elif(op == 4):
            print("\nOrdenação por Likes\n")

            Orde(numLn,False,False,True)
            for ln in numLn:
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endf
            input("Prima enter...")
            system('cls')
        elif(op == 0):
            system('cls')
            return
        else:
            print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
            print('\033[1A                            \033[K',end="\r")
            print('\033[3A                            \033[K',end="\r")
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
        
            f = open(fileName,"w")
            print("<title>Lista Tweets</title>", file=f)
            print ("<table>", file=f)
            print ("<style> table,th,td{border: 2px solid black; border-collapse: collapse; padding:10px;}</style>", file=f)
            print("<h1>Lista de Tweets<h1>", file=f)
            print("<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % (idtw,nome,tp,tw,lk), file=f)
            print("%-5s  %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))

            for ln in numLn:
                ln = ln.rstrip('\n')
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                print("<tr><td>%s</td><td>%s</td><td>%s</td><td width='200px' max-width='400px'>%s</td><td>%s</td></tr>" % (Id,Nome,Tp,Tw,Lk), file=f)
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endfor

            print("</table>",file=f)
            f.close()
          
            try:
                opc = int(input("\033[1A\n1-Responder\n2-Dar like\n3-organizar\n4-ver Html\n0-Voltar atrás\n\033[K"))
            except ValueError:
                print('\033[1A'+input("Tem que ser inteiro")+'\033[K',end="\r")
                system('cls')

            if(opc == 1):
                system('cls')
                RespondeTweet.RespTw(name)
                opc = -1

            elif(opc == 2):
                system('cls')
                GivLike(numLn)
                opc=-1
            if(opc == 3):
                system('cls')
                showOrd(numLn)#ordenar Id Nome topico Like

            elif(opc == 4):
                system(fileName)
                system('cls')
                break
            elif(opc == 0):
                system('cls')
                break

            elif(opc == -1):
                system('cls')

            else:
                print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                system('cls')
            #endif
            opc=-1
        #endwhile
    
    else:
        input("Não existe Valores para serem listados.")
        system('cls')
    #endif

def ListarUTw(name):
    if(CheckfileTw("tweets.txt")):
        print("Listagem dos Tweets\n")

        f = open("Tweets.txt","r")
        l = f.readline()
        numLn = f.readlines() 
        f.close

        idtw,idresp,nome,tp,tw,lk = l.split("-")
        print("%-5s %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))

        numLn = Orde(numLn) #(list,Nome=false,Top=false,likes=false) default = id

        for ln in numLn:
            Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

            if(name.lower() == Nome.lower()):
                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
            #endif
        #endfor

        input("\nPrima enter....")
        system('cls')
    else:
        input("Não tem tweets para listar")
        system('cls')
    #endif
