from Validacao.ValidarDados import Checkfile,VerfName,VerfEmail,VerfExist,UpdateFile
from MenuCreator.CreateMenu import Clear,WaitEnter

def Alterar():

    if Checkfile('users.txt'):
        
        print("Alteração de Dados\n")

        f = open("users.txt","r")
        l = f.readline() #cabeçalho
        numLn = f.readlines() #informação na lista numLn
        f.close
        found=0
        i=0

        #f = open("users.txt","wt")

        while True:
            sname = input("Insira nome do Utilizador que deseja Alterar os Dados: ")

            if(VerfName(sname)):    
                break

            else:
                print('\033[1A'+input("Nome inválido.")+'\033[K',end="\r")
                print('\033[1A                            \033[K',end="\r")
        #endif
        
        for ln in numLn:
            ln = ln.rstrip('\n')
            ln = ln.lower()
            ln = ln.split("-")
            

            if(str(sname.lower()) in ln):
                found=1
                Nome,Email,Telefone = ln
                print("%-20s %-20s %s\n\n" % (Nome.encode('latin1').decode('utf-8'), Email,Telefone))

                op= int(input('Alterar:\n 1-Nome\n 2-Email\n 2-Telefone\n'))
                if(op == 1):
                    while True:

                        newname = input("\nInsira Novo nome: ")

                        if(VerfName(newname)):
                            if(VerfExist(newname)):
                                print('\033[1A'+input("Nome já existe.")+'\033[K',end="\r")
                                print('\033[1A                            \033[K',end="\r")
                            else:
                                ln[0]=str(newname)
                                ln='-'.join(ln)
                                ln+='\n'
                                numLn[i]=ln
                                break

                        else:
                            print('\033[1A'+input("Nome inválido.")+'\033[K',end="\r")
                            print('\033[1A                            \033[K',end="\r")
                        #endif   
            #endif
            i+=1
        #endfor
        if(found == 0):
            print("Nome não existe")
        
        else:
            UpdateFile("users.txt",numLn)
            input("Valor alterado com sucesso")
            Clear()

    else:
        input('Não existe informação para ser alterada.')
        Clear()
    #endif