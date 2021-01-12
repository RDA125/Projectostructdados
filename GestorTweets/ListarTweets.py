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
        
        idtw,nome,tp,tw,lk = l.split("-")

        f = open(fileName,"w")
        print("<title>Lista Tweets</title>", file=f)
        print ("<table>", file=f)
        print ("<style> table,th,td{border: 2px solid black; border-collapse: collapse; padding:5px; text-align:center}</style>", file=f)
        print("<h1>Lista de Tweets<h1>", file=f)
        print("<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % (idtw,nome,tp,tw,lk), file=f)
        print("%-20s %-20s %-20s %s - %s" % (idtw,nome,tp,tw,lk))

        for ln in numLn:
            ln = ln.rstrip('\n')
            Id,Nome,Tp,Tw,Lk = ln.split("-")
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
