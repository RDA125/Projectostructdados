from Validacao.ValidarDados import CheckfileTw,VerfName,VerfTweet,UpdateFileTw
from MenuCreator.CreateMenu import Clear,WaitEnter,PrintMenu

def AlterarTw(name):

    if CheckfileTw('tweets.txt'):
        while True:
            print("Alteração de Dados\n")

            f = open("tweets.txt","r",encoding="latin1")
            l = f.readline() #cabeçalho
            numLn = f.readlines() #informação na lista numLn
            f.close
            numUTw = 0
            found=0
            sId = -1
            i=0

            for ln in numLn:
                ln = ln.rstrip('\n')
                ln = ln.strip()
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                if(name.lower() == Nome.lower()):
                    print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
                    numUTw+=1
                #endif
            #endfor

            if(numUTw != 0):
                
                try:
                    sId = int(input("\nInsira Id do Tweet que deseja Alterar os Dados(0-voltar atrás): "))
                except ValueError:
                    print('\033[1A'+input("Id inválido")+'\033[K',end="\r")
                    print('\033[1A                            \033[K',end="\r")

                
                if(sId == 0):
                    Clear()
                    return
                
                else:
                    op = -1
                    found = -2
                #endif

                for ln in numLn:
                    ln = ln.rstrip('\n')
                    ln = ln.strip()
                    ln = ln.split("-")

                    
                    if(str(sId) == ln[0] and name == ln[2]):
                        found=1
                        Clear()
                        while True:
                            Id,idResp,Nome,Tp,Tw,Lk = ln
                            print("\n%-5s %-5s %-5s \"%s\" - %s\n" % (Id,Nome,Tp,Tw,Lk))

                            op = PrintMenu("Alterar",["Tópico","Tweet"],2,"Abortar")
                            
                            if(op == 1):
                                while True:

                                    newtop = input("\nInsira Novo Tópico: ")

                                    if(VerfName(newtop)):
                                            ln[3]=str(newtop)
                                            ln='-'.join(ln)
                                            ln+='\n'
                                            numLn[i]=ln
                                            break
                                        #endif
                                    else:
                                        print('\033[1A'+input("Tópico inválido.")+'\033[K',end="\r")
                                        print('\033[2A                            \033[K',end="\r")
                                    #endif
                                #endwhile
                                break

                            elif(op == 2):
                                while True:

                                    newTw = input("\nInsira Novo Tweet: ")

                                    if(VerfTweet(newTw)):
                                        ln[4]=str(newTw)
                                        ln='-'.join(ln)
                                        ln+='\n'
                                        numLn[i]=ln
                                        break
                                        #endif
                                    else:
                                        print('\033[1A'+input("Tweet tem de ter pelo menos um character com um máximo de 250.")+'\033[K',end="\r")
                                        print('\033[2A                            \033[K',end="\r")
                                    #endif
                                #endwhile
                                break

                            elif(op == 0):
                                found = -1
                                break

                            #endif
                        #endwhile
                    #endif
                    i+=1
                #endfor
                
                if(found == 0):
                    input("Tweet não existe")
                    Clear()

                elif(found == -2):
                    Clear()
                
                else:

                    if(found == 1):

                        UpdateFileTw("tweets.txt",numLn)
                        op = input("Valor alterado com sucesso\nDeseja alterar mais?(s/n)\n")

                    elif(found == -1):
                        op = input("Deseja alterar mais?(s/n)\n")
                    #endif

                    if((op != "s" and op != "S") and (op != "n" and op !="N")):
                        print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                        print('\033[1A                            \033[K',end="\r")
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

            else:
                input("Não existe tweets para alterar.")
                Clear()
                break
        #endwhile

    else:
        input('Não existe informação para ser alterada.')
        Clear()
    #endif