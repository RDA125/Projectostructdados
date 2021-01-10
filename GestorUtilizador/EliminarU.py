from Validacao.ValidarDados import Checkfile,VerfName,VerfExist,UpdateFile
from MenuCreator.CreateMenu import Clear,WaitEnter

def Elim():

    if Checkfile('users.txt'):
        while True:
            print("Eliminaçãode Dados\n")

            f = open("users.txt","r",encoding="latin1")
            l = f.readline() #cabeçalho
            numLn = f.readlines() #informação na lista numLn
            f.close
            found=0
            i=0

            while True:
                sname = input("Insira nome do Utilizador que deseja Eliminar: ")

                if(VerfName(sname)):
                    break

                else:
                    print('\033[1A'+input("Nome inválido.")+'\033[K',end="\r")
                    print('\033[1A                            \033[K',end="\r")
                #endif

        
            for ln in numLn:
                ln = ln.rstrip('\n')
                ln = ln.split("-")

                if(str(sname.lower()) in ln[0].lower()):
                    found=1
                    Nome,Email,Telefone = ln
                    print("%-20s %-20s %s\n\n" % (Nome, Email,Telefone))

                    op= input('Tem a certeza que deseja eliminar este Utilizador?')

                    if((op != "s" and op != "S") and (op != "n" and op !="N")):
                        print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                        print('\033[1A                            \033[K',end="\r")
                    
                    else:
                        if(op != "s" and op != "S"):
                            found = -1
                            break
                                   
                        else:
                            ln='-'.join(ln)
                            ln+='\n'
                            numLn.remove(ln)
                            break
                        #endif
                       
                #endif
                i+=1
            #endfor
            if(found == 0):
                input("Nome não existe")
                Clear()

            else:

                if(found == 1):

                    UpdateFile("users.txt",numLn)
                    op = input("Utilizador eliminado com sucesso\nDeseja Eliminar mais?(s/n)\n")

                else:
                    op = input("Deseja Eliminar outro Utilizador?(s/n)\n")
                #endif

                if((op != "s" and op != "S") and (op != "n" and op !="N")):
                    print("Opção inválida")
                
                else:
                    if(op != "s" and op != "S"):
                        Clear()
                        break
                    else:
                        op=0
                        Clear()
                    #endif
                #endif
            #endif
        #endwhile

    else:
        input('Não existe informação para ser Eliminada.')
        Clear()
    #endif