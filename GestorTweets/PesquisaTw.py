from Validacao.ValidarDados import CheckfileTw,VerfName,UpdateHtmlTw,UpdateFileTw, Orde
from MenuCreator.CreateMenu import Clear,WaitEnter
import re

def PesqTw():
    if(CheckfileTw("tweets.txt")):

        while True:
            print("Pesquisa de Tweets\n\n")
            opc = -1
            found = 0

            f = open("Tweets.txt","r")
            l = f.readline()
            numLn = f.readlines() 
            f.close
            
            idtw,idresp,nome,tp,tw,lk = l.split("-")
            
                                                                                        #print("%-5s  %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))
                                                                                        #for ln in numLn:
                                                                                        #    ln = ln.rstrip('\n')
                                                                                        #    Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")
                                                                                        #    print("%-5s %-5s %-5s %s - %s" % (Id,Nome,Tp,Tw,Lk))
                                                                                        ##endfor

            try:
                opc = int(input("\033[1A\n1-Nome\n2-tópico\n3-Número de Likes\n0-Voltar atrás\n\033[K"))
            except ValueError:
                print('\033[1A'+input("Tem que ser inteiro")+'\033[K',end="\r")
                Clear()
            
            if(opc == 0):
                Clear()
                return
            
            elif(opc == 1):
                while True:
                    sname = input("\nInsira o nome para pesquisa: ")
            
                    if(VerfName(sname)):
                        Clear()
                        print("Resultado da pesquisa.")

                        print("%-5s  %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))

                        Orde(numLn,False,False,True)# ordenar do tweet com mais likes para o com menos

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                            if(sname.lower() == Nome.lower()):
                                found=1
                                print("%-5s %-5s %-5s %s - %s" % (Id,Nome,Tp,Tw,Lk))
                            #endif
                        #endfor
                        if(found == 0):
                            print("\nNome inserido não foi encontrado")
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
                    sTop = input("\nInsira o Tópico para pesquisa: ")
            
                    if(VerfName(sTop)):
                        Clear()
                        print("Resultado da pesquisa.")

                        print("%-5s  %-5s %-5s %s - %s" % (idtw,nome,tp,tw,lk))

                        Orde(numLn,False,False,True)# ordenar do tweet com mais likes para o com menos

                        for ln in numLn:
                            ln = ln.rstrip('\n')
                            Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                            if(sTop.lower() == Tp.lower()):
                                found=1
                                print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
                            #endif
                        #endfor
                        if(found == 0):
                            print("\nTópico inserido não foi encontrado")
                        #endif
                        WaitEnter()
                        break
                    else:
                        print('\033[1A'+input("Tópico inválido")+'\033[K',end="\r")
                        print('\033[2A                            \033[K',end="\r")
                    #endif
                #endwhile

            elif(opc == -1):
               Clear()

            else:
                print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                Clear()
            #endif
    else:
        input("Não existe Valores para serem pesquisados.")
        Clear()
    #endif