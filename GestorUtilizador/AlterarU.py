from Validacao.ValidarDados import Checkfile,VerfName,VerfEmail,VerfExist,VerfOper,UpdateFile
from MenuCreator.CreateMenu import Clear,WaitEnter,PrintMenu

def Alterar(name =""):

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
                if(name == ""):
                    sname = input("Insira nome do Utilizador que deseja Alterar os Dados(0-voltar atrás): ")

                    if(sname == '0'):
                        Clear()
                        return
                    #endif
                    
                    if(VerfName(sname)):
                        break

                    else:
                        print('\033[1A'+input("Nome inválido.")+'\033[K',end="\r")
                        print('\033[1A                            \033[K',end="\r")
                    #endif
                else:
                    sname = name
                    break
                #endif

            for ln in numLn:
                ln = ln.rstrip('\n')
                ln = ln.split("-")

                if(str(sname.lower()) == ln[0].lower()):
                    found=1
                   
                    while True:
                        Nome,Email,Num,Telefone,Oper = ln
                        print("%-20s %-20s %-20s %-20s %s\n\n" % (Nome,Email,Num,Telefone,Oper))

                        op = PrintMenu("Alterar",["Nome","Email","Número","Telefone","Operadora"],5,"abortar")
                            
                        
                        if(op == 1):
                            while True:

                                newname = input("\nInsira Novo nome: ")

                                if(VerfName(newname)):
                                    if(VerfExist(newname)):
                                        print('\033[1A'+input("Nome já existe.")+'\033[K',end="\r")
                                        print('\033[2A                            \033[K',end="\r")
                                    else:
                                        name = newname
                                        ln[0]=str(newname)
                                        ln='-'.join(ln)
                                        ln+='\n'
                                        numLn[i]=ln
                                        break
                                    #endif
                                else:
                                    print('\033[1A'+input("Nome inválido.")+'\033[K',end="\r")
                                    print('\033[2A                            \033[K',end="\r")
                                #endif
                            #endwhile
                            break

                        elif(op == 2):
                            while True:

                                newmail = input("\nInsira Novo email: ")

                                if(VerfEmail(newmail)):
                                    if(VerfExist(newmail)):
                                        print('\033[1A'+input("email já existe.")+'\033[K',end="\r")
                                        print('\033[2A                            \033[K',end="\r")
                                    else:
                                        ln[1]=str(newmail)
                                        ln='-'.join(ln)
                                        ln+='\n'
                                        numLn[i]=ln
                                        break
                                    #endif
                                else:
                                    print('\033[1A'+input("email inválido.")+'\033[K',end="\r")
                                    print('\033[2A                            \033[K',end="\r")
                                #endif
                            #endwhile
                            break
                        
                        elif(op == 3):
                            while True:
                                try:
                                    newnum = int(input("\nInsira Novo Número: "))

                                except ValueError:
                                    print('\033[1A'+input("Número inválido")+'\033[K',end="\r")
                                    print('\033[2A                            \033[K',end="\r")

                                    continue

                                if(newnum<1000000 or newnum>9999999):
                                    print('\033[1A'+input("Número tem que ter 7 digitos")+'\033[K',end="\r")
                                    print('\033[2A                            \033[K',end="\r")

                                else:
                                    if(VerfExist(newnum)):
                                        print('\033[1A'+input("Número de Utilizador já existe.")+'\033[K',end="\r")
                                        print('\033[2A                            \033[K',end="\r")
                                    else:
                                        ln[2]=str(newnum)
                                        ln='-'.join(ln)
                                        ln+='\n'
                                        numLn[i]=ln
                                        break
                                #endif
                            #endwhile
                            break

                        elif(op == 4):
                            while True:
                                
                                try:
                                    newtel = int(input("\nInsira Novo Nº Telefone: "))

                                except ValueError:
                                    print('\033[1A'+input("Número de Telefone inválido")+'\033[K',end="\r")
                                    print('\033[2A                            \033[K',end="\r")

                                    continue 
                                
                                if(newtel<910000000 or newtel>999999999):
                                    print('\033[1A'+input("Número de Telefone inválido [910000000-999999999]")+'\033[K',end="\r")
                                    print('\033[2A                            \033[K',end="\r")

                                else:
                                    if(VerfExist(newtel)):
                                        print('\033[1A'+input("Número de Telefone já existe.")+'\033[K',end="\r")
                                        print('\033[2A                            \033[K',end="\r")
                                    else:
                                        ln[3]=str(newtel)
                                        ln='-'.join(ln)
                                        ln+='\n'
                                        numLn[i]=ln
                                        break
                                #endif
                            #endwhile
                            break

                        elif(op == 5):
                            while True:
                                newoper = input('\nInsira Nova Operadora de Telemóveis: ').upper()

                                if(VerfOper(newoper)):
                                    if(newoper == Oper):
                                        print('\033[1A'+input("Operadora tem que ser diferente à existente")+'\033[K',end="\r")
                                        print('\033[2A                            \033[K',end="\r")
                                    
                                    else:
                                        ln[4]=str(newoper)
                                        ln='-'.join(ln)
                                        ln+='\n'
                                        numLn[i]=ln
                                        break

                                else:
                                    print('\033[1A'+input("Operadora inválida.")+'\033[K',end="\r")
                                    print('\033[2A                               \033[K',end="\r")
                                #endif
                            #endwhile
                            break

                        elif(op == 0):
                            found = -1
                            break

                        elif(op == -1):
                            found = -5
                            print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                            print('\033[2A                            \033[K',end="\r")
                        #endif
                    #endwhile
                    if(found != -5):
                        break
                #endif
                i+=1
            #endfor
            
            if(found == 0):
                input("Nome não existe")
                Clear()

            else:

                if(found == 1):

                    UpdateFile("users.txt",numLn)
                    while True:
                        op = input("Valor alterado com sucesso\nDeseja alterar mais?(s/n)\n")

                        if((op != "s" and op != "S") and (op != "n" and op !="N")):
                            print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                            print('\033[2A                            \033[K',end="\r")
                        else:
                            break
                        #endif
                    #endwhile

                elif(found == -1):
                    while True:
                        op = input("Deseja alterar mais?(s/n)\n")

                        if((op != "s" and op != "S") and (op != "n" and op !="N")):
                            print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                            print('\033[2A                            \033[K',end="\r")
                        else:
                            break
                        #endif
                    #endwhile
                #endif

                if(op != "s" and op != "S"):
                    Clear()
                    return name
                else:
                    op=0
                    Clear()
                #endif
            #endif
        #endwhile

    else:
        input('Não existe informação para ser alterada.')
        Clear()
    #endif