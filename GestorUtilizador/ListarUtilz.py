import os

def ListarU(fileName):
    f = open("users.txt","r")
    linhas = f.readlines()
    f.close

    f = open(fileName,"wt")
    print ("<table>", file=f)
    print("<h1>Lista de utilizadores<h1>", file=f)

    for linha in linhas:
        linha = linha.rstrip('\n')
        Nome,Email,Telefone = linha.split("-")
        print("%-20s %-20s %s" % (Nome, Email,Telefone))
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (Nome, Email, Telefone), file=f)
    #endfor

    print("</table>",file=f)
    f.close()