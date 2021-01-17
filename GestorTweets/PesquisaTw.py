from Validacao.ValidarDados import CheckfileTw,VerfName,Orde,GroupTw
from MenuCreator.CreateMenu import Clear,WaitEnter,PrintMenu
import re

def PesqTw():
    if(CheckfileTw("tweets.txt")):

        while True:
            opc = -1
            sLk = -1
            found = 0

            f = open("Tweets.txt","r")
            l = f.readline()
            numLn = f.readlines() 
            f.close
            
            idtw,idresp,nome,tp,tw,lk = l.split("-")

            opc = PrintMenu("Pesquisa de Tweets",["Nome","Tópico","Número de Likes"],3,"Voltar atrás")
            
            if(opc == 0):
                Clear()
                return
            
            elif(opc == 1):
                while True:
                    sname = input("\nInsira o nome para pesquisa: ")
            
                    if(VerfName(sname)):
                        Clear()
                        print("Resultado da pesquisa\n")

                        print("%-5s  %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))

                        Orde(numLn,False,False,False,True)# ordenar do tweet com mais likes para o com menos

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                            if(sname.lower() == Nome.lower()):
                                found=1
                                print("%-5s %-5s %-5s %s - %s" % (Id,Nome,Tp,Tw,Lk))
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
                    sTop = input("\nInsira o Tópico para pesquisa: ")
            
                    if(VerfName(sTop)):
                        Clear()
                        print("Resultado da pesquisa\n")

                        print("%-5s  %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))

                        Orde(numLn,False,False,False,True)# ordenar do tweet com mais likes para o com menos

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                            if(sTop.lower() == Tp.lower()):
                                found=1
                                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
                            #endif
                        #endfor
                        if(found == 0):
                            print("Tópico inserido não foi encontrado\n")
                        #endif
                        print("\n")
                        WaitEnter()
                        break
                    else:
                        print('\033[1A'+input("Tópico inválido")+'\033[K',end="\r")
                        print('\033[2A                            \033[K',end="\r")
                    #endif
                #endwhile

            elif(opc == 3):
                while True:
                    while True:
                        try:
                            sLk = int(input("\nInsira Numero de likes: "))

                        except ValueError:
                            print('\033[1A'+input("Número inválido")+'\033[K',end="\r")
                            print('\033[2A                            \033[K',end="\r")

                        if(sLk>=0):
                            break
                        #endif
                    #endwhile
    
                    Clear()
                    print("Resultado da pesquisa\n")

                    print("%-5s  %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))

                    Orde(numLn,False,False,False,True)# ordenar do tweet com mais likes para o com menos

                    for ln in numLn:
                        ln = ln.rstrip('\n')
                        Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                        if(int(Lk) >= sLk):
                            found=1
                            print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
                        #endif
                    #endfor
                    if(found == 0):
                        print("Não existe tweets com numero de likes igual ou superior ao valor inserido\n")
                    #endif
                    print("\n")
                    WaitEnter()
                    break
                #endwhile
            elif(opc == -1):
               Clear()

            #endif
    else:
        input("Não existe Valores para serem pesquisados.")
        Clear()
    #endif


def CountTw():
    if(CheckfileTw("tweets.txt")):

        while True:
            opc = -1
            sLk = -1
            found = 0
            count=0

            f = open("Tweets.txt","r")
            l = f.readline()
            numLn = f.readlines() 
            f.close
            
            idtw,idresp,nome,tp,tw,lk = l.split("-")

            opc = PrintMenu("Contagem de Tweets",["Nome","Tópico","Número de Likes","Agrupar"],4,"Voltar atrás")
            
            if(opc == 0):
                Clear()
                return
            
            elif(opc == 1):
                while True:
                    sname = input("\nInsira o nome para contagem: ")
            
                    if(VerfName(sname)):
                        Clear()
                        print("Resultado da contagem\n")

                        Orde(numLn,False,False,False,True)# ordenar do tweet com mais likes para o com menos

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                            if(sname.lower() == Nome.lower()):
                                count+=1
                            #endif
                        #endfor

                        if(count == 0):
                            print("Nome inserido não tem tweets ou não existe.\n")
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
                    sTop = input("\nInsira o Tópico para contar: ")
            
                    if(VerfName(sTop)):
                        Clear()
                        print("Resultado da contagem\n")

                        Orde(numLn,False,False,False,True)# ordenar do tweet com mais likes para o com menos

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                            if(sTop.lower() == Tp.lower()):
                                count+=1
                            #endif
                        #endfor

                        if(count == 0):
                            print("Não existe tweets com o tópico inserido.\n")
                        else:
                            print(sTop+": "+str(count)+"\n")
                        #endif

                        WaitEnter()
                        break
                    else:
                        print('\033[1A'+input("Tópico inválido")+'\033[K',end="\r")
                        print('\033[2A                            \033[K',end="\r")
                    #endif
                #endwhile

            elif(opc == 3):
                while True:
                    while True:
                        try:
                            sLk = int(input("\nInsira Numero de likes: "))

                        except ValueError:
                            print('\033[1A'+input("Número inválido")+'\033[K',end="\r")
                            print('\033[2A                            \033[K',end="\r")

                        if(sLk>=0):
                            break
                        #endif
                    #endwhile
    
                    Clear()
                    print("Resultado da contagem\n")

                    Orde(numLn,False,False,False,True)# ordenar do tweet com mais likes para o com menos

                    for ln in numLn:
                        ln = ln.rstrip('\n')
                        Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                        if(int(Lk) == sLk):
                            count+=1
                        #endif
                    #endfor

                    if(count == 0):
                        print("Não existe tweets com numero de likes igual  ao valor inserido\n")
                    else:
                        print("Numero de tweets com valor igual a "+str(sLk)+": "+str(count)+"\n")
                    #endif

                    WaitEnter()
                    break
                #endwhile

            elif(opc == 4):
                Clear()
                while True:
                    op = PrintMenu("Agrupar por:",["Nome","Tópico","Número de Likes"],3,"Voltar atrás")

                    if(op == 0):
                        Clear()
                        break
                        
                    elif(op == 1):
                        Clear()
                        GroupTw(numLn,True)
                    
                    elif(op == 2):
                        Clear()
                        GroupTw(numLn,False,True)
                    
                    elif(op == 3):
                        Clear()
                        GroupTw(numLn,False,False,True)

                    #endif

            elif(opc == -1):
               Clear()

            #endif
    else:
        input("Não existe Valores para serem pesquisados.")
        Clear()
    #endif