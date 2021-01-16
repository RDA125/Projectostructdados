from Validacao.ValidarDados import CheckfileTw,VerfName,VerfOper,Orde,GroupUtil
from MenuCreator.CreateMenu import Clear,WaitEnter,PrintMenu
import re

def PesqUtil():
    if(CheckfileTw("users.txt")):

        while True:
            opc = -1
            found = 0

            f = open("users.txt","r")
            l = f.readline()
            numLn = f.readlines() 
            f.close
            
            nom,email,num,tel,oper = l.split("-")

            opc = PrintMenu("Pesquisa de Users",["Nome","Operadora"],2,"Voltar atrás")
            
            if(opc == 0):
                Clear()
                return
            
            elif(opc == 1):
                while True:
                    sname = input("\nInsira o nome para pesquisa: ").lower()
                    
                    if(VerfName(sname)):
                        Clear()
                        print("Resultado da pesquisa\n")

                        print("%-20s %-20s %-20s %-20s %s" % (nom,email,num,tel,oper))

                        Orde(numLn)#ordenar alfabeticamente

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Nome,Email,Num,Tel,Oper = ln.split("-")
                            Nome = Nome.lower()
                            sname = re.compile(sname)

                            if(sname.search(Nome)):
                                found=1
                                print("%-20s %-20s %-20s %-20s %s" % (Nome,Email,Num,Tel,Oper))
                            #endif
                        #endfor

                        if(found == 0):
                            print("Nome inserido não foi encontrado\n")
                        #endif
                        print("\n")
                        WaitEnter()
                        break
                    else:
                        print('\033[1A'+input("Nome inválido")+'\033[K',end="\r")
                        print('\033[2A                            \033[K',end="\r")
                    #endif
                #endwhile

            elif(opc == 2):
                while True:
                    sOper = input("\nInsira Operadora para pesquisa: ").upper()
            
                    if(VerfOper(sOper)):
                        Clear()
                        print("Resultado da pesquisa\n")

                        print("%-20s %-20s %-20s %-20s %s" % (nom,email,num,tel,oper))

                        Orde(numLn)# ordenar Alfabeticamente

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Nome,Email,Num,Tel,Oper = ln.split("-")

                            if(sOper.lower() == Oper.lower()):
                                found=1
                                print("%-20s %-20s %-20s %-20s %s" % (Nome,Email,Num,Tel,Oper))
                            #endif
                        #endfor
                        if(found == 0):
                            print("Operadora inserida não foi encontrado\n")
                        #endif
                        print("\n")
                        WaitEnter()
                        break
                    else:
                        print('\033[1A'+input("Operadora inválido")+'\033[K',end="\r")
                        print('\033[2A                            \033[K',end="\r")
                    #endif
                #endwhile

            elif(opc == -1):
               Clear()

            #endif
    else:
        input("Não existe Valores para serem pesquisados.")
        Clear()
    #endif


def CountU():
    if(CheckfileTw("users.txt")):

        while True:
            opc = -1
            sLk = -1
            found = 0
            count=0

            f = open("users.txt","r")
            l = f.readline()
            numLn = f.readlines() 
            f.close
            
            nom,email,num,tel,oper = l.split("-")

            opc = PrintMenu("Contagem de Tweets",["Nome","Operadora","Agrupar"],3,"Voltar atrás")
            
            if(opc == 0):
                Clear()
                return
            
            elif(opc == 1):
                while True:
                    sname = input("\nInsira o nome para contagem: ").lower
            
                    if(VerfName(sname)):
                        Clear()
                        print("Resultado da contagem para Utilizadores com o mesmo Nome iniciado com\n")

                        Orde(numLn)

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Nome,Email,Num,Tel,Oper = ln.split("-")
                            Nome = Nome.lower()
                            aux = re.compile(sname)

                            if(aux.search(Nome)):
                                count+=1
                            #endif
                        #endfor

                        if(count == 0):
                            print("Nome inserido não existe\n")
                        else:
                            print(sname+": "+str(count)+"\n")
                        #endif
                        WaitEnter()
                        break
                    else:
                        print('\033[1A'+input("Nome inválido")+'\033[K',end="\r")
                        print('\033[2A                            \033[K',end="\r")
                    #endif
                #endwhile

            elif(opc == 2):
                while True:
                    sOper = input("\nInsira Operadora para pesquisa: ").upper()
            
                    if(VerfOper(sOper)):
                        Clear()
                        print("Resultado da contagem\n")

                        Orde(numLn)

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Nome,Email,Num,Tel,Oper = ln.split("-")

                            if(sOper == Oper):
                                count+=1
                            #endif
                        #endfor

                        if(count == 0):
                            print("Não existe Utilizador com a operadora inserido.\n")
                        else:
                            print(sOper+": "+str(count)+"\n")
                        #endif

                        WaitEnter()
                        break
                    else:
                        print('\033[1A'+input("Operadora inválido")+'\033[K',end="\r")
                        print('\033[2A                            \033[K',end="\r")
                    #endif
                #endwhile

            elif(opc == 3):
                Clear()
                while True:
                    op = PrintMenu("Agrupar por:",["Nome","Operadora"],2,"Voltar atrás")

                    if(op == 0):
                        Clear()
                        break
                        
                    elif(op == 1):
                        Clear()
                        GroupUtil(numLn,True)
                    
                    elif(op == 2):
                        Clear()
                        GroupUtil(numLn,False,True)

                    #endif

            elif(opc == -1):
               Clear()

            #endif
    else:
        input("Não existe Valores para serem pesquisados.")
        Clear()
    #endif