from os import system
from Validacao.ValidarDados import Checkfile
import msvcrt

def ListarU(fileName):
    if(Checkfile("users.txt")):
        print("Listagem dos Utilizadores\n")

        f = open("users.txt","r")
        l = f.readline() #cabeçalho
        numLn = f.readlines() #informação na lista numLn
        f.close
        
        nome,email,num,tel,oper = l.split("-")

        f = open(fileName,"w",encoding="utf-8")
        print("<title>Lista Users</title>", file=f)
        print ("<table>", file=f)
        print ("<style> table,th,td{border: 2px solid black; border-collapse: collapse; padding:5px; text-align:center}</style>", file=f)
        print("<h1>Lista de utilizadores<h1>", file=f)
        print("<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % (nome, email, num, tel, oper), file=f)
        print("%-20s %-20s %-20s %-20s %s" % (nome, email, num, tel, oper))

        for ln in numLn:
            ln = ln.rstrip('\n')
            Nome,Email,Num,Telefone,Oper = ln.split("-")
            print("%-20s %-20s %-20s %-20s %s" % (Nome, Email, Num, Telefone, Oper))
            print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (Nome, Email, Num, Telefone, Oper), file=f)
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
