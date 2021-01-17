from os import system
from Validacao.ValidarDados import Checkfile, Orde
from MenuCreator.CreateMenu import Clear,PrintMenu
import msvcrt

def showOrdU(numLn):
    while True:

        op = PrintMenu("Ordenação de Utilizadores",["Nome","Operadora"],2,"Voltar atrás")

        if(op == 1):
            print("\nOrdenação por Nome\n")

            Orde(numLn,True)

            for ln in numLn:
                Nome,Email,Num,Telefone,Oper = ln.split("-")
                print("%-20s %-20s %-20s %-20s %s" % (Nome, Email, Num, Telefone, Oper))
            #endfor

            print("\n")
            input("Prima enter...")
            Clear()

        elif(op == 2):
            print("\nOrdenação por Operadora\n")

            Orde(numLn,False,False,False,False,True)

            for ln in numLn:
                Nome,Email,Num,Telefone,Oper = ln.split("-")
                print("%-20s %-20s %-20s %-20s %s" % (Nome, Email, Num, Telefone, Oper))
            #endfor

            print("\n")
            input("Prima enter...")
            Clear()

        elif(op == 0):
            Clear()
            return
        #endif
    #endwhile


def ListarU(fileName):
    if(Checkfile("users.txt")):
        while True:
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
            
            opc = PrintMenu(" ",["Organizar","Ver Html"],2,"Voltar atrás")

            if(opc == 1):
                Clear()
                showOrdU(numLn)
                break

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
        system('cls')
    #endif

def Listar():
    if(Checkfile("users.txt")):
       
        print("Listagem dos Utilizadores\n")
        f = open("users.txt","r")
        l = f.readline() #cabeçalho
        numLn = f.readlines() #informação na lista numLn
        f.close
        
        nome,email,num,tel,oper = l.split("-")
        print("%-20s %-20s %-20s %-20s %s" % (nome, email, num, tel, oper))
        for ln in numLn:
            ln = ln.rstrip('\n')
            Nome,Email,Num,Telefone,Oper = ln.split("-")
            print("%-20s %-20s %-20s %-20s %s" % (Nome, Email, Num, Telefone, Oper))
        #endfor
            
        input("\nPrima enter....")
        Clear()

    else:
        input("Não existe Valores para serem listados.")
        system('cls')
    #endif
