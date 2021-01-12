from os import system
from Validacao.ValidarDados import CheckfileTw
import textwrap
import msvcrt

def ListarTw(fileName):
    if(CheckfileTw("tweets.txt")):
        print("Listagem dos Tweets\n")

        f = open("Tweets.txt","r")
        l = f.readline()
        numLn = f.readlines() 
        f.close
        
        idtw,idresp,nome,tp,tw,lk = l.split("-")

        f = open(fileName,"w")
        print("<title>Lista Tweets</title>", file=f)
        print ("<table>", file=f)
        print ("<style> table,th,td{border: 2px solid black; border-collapse: collapse; padding:5px; text-align:center}</style>", file=f)
        print("<h1>Lista de Tweets<h1>", file=f)
        print("<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % (idtw,nome,tp,tw,lk), file=f)
        print("%-20s  %-20s %-20s %s - %s" % (idtw,nome,tp,tw,lk))

        for ln in numLn:
            ln = ln.rstrip('\n')
            Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
            print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (Id,Nome,Tp,Tw,Lk), file=f)
            print("%-20s %-20s %-20s %s - %s" % (Id,Nome,Tp,Tw,Lk))
        #endfor

        print("</table>",file=f)
        f.close()

        while True:
            
            opc = input("\nVer HTML?(s/n) ")

            if((opc != "s" and opc != "S") and (opc != "n" and opc !="N")):
                print("Opção inválida")

            else:
                if(opc == "s" or opc == "S"):
                    system(fileName)
                    system('cls')
                    break
                else:
                    system('cls')
                    break
    
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
        print("%-20s %-20s %-20s %s - %s" % (idtw,nome,tp,tw,lk))

        for ln in numLn:
            ln = ln.rstrip('\n')
            Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

            if(name.lower() == Nome.lower()):
                print("%-20s %-20s %-20s %s - %s" % (Id,Nome,Tp,Tw,Lk))
            #endif
        #endfor

        while True:
            try:
                opc = int(input("\n0-Voltar atrás\n"))
            except ValueError:
                print('\033[1A'+input("Tem que ser inteiro")+'\033[K',end="\r")
                print('\033[1A                            \033[K',end="\r")

            if(opc != 0):
                print("Opção inválida")
                
            else:
                system('cls')
                break
            #endif
        #endwhile
    else:
        input("Não tem tweets para listar")
        system('cls')
    #endif
