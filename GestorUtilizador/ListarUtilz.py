from os import system
import msvcrt

def ListarU(fileName):
    system('cls')
    print("Listagem dos Utilizadores\n")

    f = open("users.txt","r")
    l = f.readline() #cabeçalho
    numLn = f.readlines() #informação na lista numLn
    f.close
    
    nome,email,tel = l.split("-")

    f = open(fileName,"w")
    print ("<table>", file=f)
    print ("<style> table,th,td{border: 2px solid black; border-collapse: collapse; padding:5px; text-align:center}</style>", file=f)
    print("<h1>Lista de utilizadores<h1>", file=f)
    print("<tr><th>%s</th><th>%s</th><th>%s</th></tr>" % (nome, email, tel), file=f)
    print("%-20s %-20s %s" % (nome, email,tel))

    for ln in numLn:
        ln = ln.rstrip('\n')
        Nome,Email,Telefone = ln.split("-")
        print("%-20s %-20s %s" % (Nome.encode('latin1').decode('utf-8'), Email,Telefone))
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (Nome, Email, Telefone), file=f)
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
                break
            else:
                system('cls')
                break
