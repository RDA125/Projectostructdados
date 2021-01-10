from Validacao.ValidarDados import Checkfile,VerfName,VerfEmail,VerfExist,UpdateFile
from MenuCreator.CreateMenu import Clear,WaitEnter
import unicodedata

def Alterar():

    if Checkfile('users.txt'):
        while True:
            print("Alteração de Dados\n")

            f = open("users.txt","r",encoding="latin1")
            l = f.readline() #cabeçalho
            numLn = f.readlines() #informação na lista numLn
            f.close
            found=0
            i=0

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
                ln = ln.split("-")

                if(str(sname.lower()) in ln[0].lower()):
                    found=1
                    Nome,Email,Telefone = ln
                    print("%-20s %-20s %s\n\n" % (Nome, Email,Telefone))

                    op= int(input('Alterar:\n 1-Nome\n 2-Email\n 3-Telefone\n 0-abortar\n'))
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
                                #endif
                            else:
                                print('\033[1A'+input("Nome inválido.")+'\033[K',end="\r")
                                print('\033[1A                            \033[K',end="\r")
                            #endif
                        #endwhile

                    elif(op == 2):
                        while True:

                            newmail = input("\nInsira Novo email: ")

                            if(VerfEmail(newmail)):
                                if(VerfExist(newmail)):
                                    print('\033[1A'+input("email já existe.")+'\033[K',end="\r")
                                    print('\033[1A                            \033[K',end="\r")
                                else:
                                    ln[1]=str(newmail)
                                    ln='-'.join(ln)
                                    ln+='\n'
                                    numLn[i]=ln
                                    break
                                #endif
                            else:
                                print('\033[1A'+input("email inválido.")+'\033[K',end="\r")
                                print('\033[1A                            \033[K',end="\r")
                            #endif
                        #endwhile
                    
                    elif(op == 3):
                        while True:
                            
                            try:
                                newtel = int(input("\nInsira Novo Nº Telefone: "))

                            except ValueError:
                                print('\033[1A'+input("Número de Telefone inválido")+'\033[K',end="\r")
                                print('\033[1A                            \033[K',end="\r")

                                continue 
                            
                            if(newtel<910000000 or newtel>999999999):
                                print('\033[1A'+input("Número de Telefone inválido [910000000-999999999]")+'\033[K',end="\r")
                                print('\033[1A                            \033[K',end="\r")

                            else:
                                if(VerfExist(newtel)):
                                    print('\033[1A'+input("Número de Telefone já existe.")+'\033[K',end="\r")
                                    print('\033[1A                            \033[K',end="\r")
                                else:
                                    ln[2]=str(newtel)
                                    ln='-'.join(ln)
                                    ln+='\n'
                                    numLn[i]=ln
                                    break
                            #endif
                        #endwhile

                    elif(op == 0):
                        found = -1
                        break
                    #endif
                       
                #endif
                i+=1
            #endfor
            if(found == 0):
                input("Nome não existe")
                Clear()
            
            elif(found == -1):
                Clear()
                continue

            else:
                UpdateFile("users.txt",numLn)
                op = input("Valor alterado com sucesso\nDeseja alterar mais?(s/n)\n")

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
        input('Não existe informação para ser alterada.')
        Clear()
    #endif