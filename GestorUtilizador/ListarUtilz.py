from os import system
import msvcrt

def ListarU(fileName):
    f = open("users.txt","r")
    l = f.readline() #cabeçalho
    linhas = f.readlines() #informação
    f.close
    
    nome,email,tel = l.split("-")

    f = open(fileName,"w")
    print ("<table>", file=f)
    print ("<style> table,th,td{border: 2px solid black; border-collapse: collapse; padding:5px; text-align:center}</style>", file=f)
    print("<h1>Lista de utilizadores<h1>", file=f)
    print("<tr><th>%s</th><th>%s</th><th>%s</th></tr>" % (nome, email, tel), file=f)
    print("%-20s %-20s %s" % (nome, email,tel))

    for linha in linhas:
        linha = linha.rstrip('\n')
        Nome,Email,Telefone = linha.split("-")
        print("%-20s %-20s %s" % (Nome, Email,Telefone))
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (Nome, Email, Telefone), file=f)
    #endfor

    print("</table>",file=f)
    f.close()

    while True:
        
        opc = input("\nVer HTML?(s/n) ")
        print(opc)

        if((opc != "s" and opc != "S") and (opc != "n" and opc !="N")):
            print("Opção inválida")

        else:
            if(opc == "s" or opc == "S"):
                system(fileName)
                break
            else:
                break
