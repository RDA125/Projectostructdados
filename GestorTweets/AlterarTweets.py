from Validacao.ValidarDados import CheckfileTw,VerfName,VerfTweet,UpdateFileTw
from MenuCreator.CreateMenu import Clear,WaitEnter

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
            i=0

            for ln in numLn:
                ln = ln.rstrip('\n')
                Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                if(name.lower() == Nome.lower()):
                    print("%-20s %-20s %-20s %s - %s" % (Id,Nome,Tp,Tw,Lk))
                    numUTw+=1
                #endif
            #endfor

            if(numUTw != 0):
                while True:
                    try:
                        sId = int(input("Insira Id do Tweet que deseja Alterar os Dados(0-voltar atrás): "))
                    except ValueError:
                        print('\033[1A'+input("Id inválido")+'\033[K',end="\r")
                        print('\033[1A                            \033[K',end="\r")

                    finally:
                        break
                #endwhile
                
                if(sId == 0):
                    Clear()
                    return
                #endif

                for ln in numLn:
                    ln = ln.rstrip('\n')
                    ln = ln.split("-")

                    
                    if(str(sId) == ln[0]):
                        found=1
                        Id,idResp,Nome,Tp,Tw,Lk = ln
                        print("%-20s %-20s %-20s %s - %s" % (Id,Nome,Tp,Tw,Lk))
                        print('Alterar:\n 1-Tópico\n 2-Tweet\n 0-abortar')

                        while True:
                            try:
                                op = int(input())
                            except ValueError:
                                print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                                print('\033[1A                            \033[K',end="\r")
                            
                            if(op == 1):
                                while True:

                                    newtop = input("\nInsira Novo Tópico: ")

                                    if(VerfName(newtop)):
                                            ln[2]=str(newtop)
                                            ln='-'.join(ln)
                                            ln+='\n'
                                            numLn[i]=ln
                                            break
                                        #endif
                                    else:
                                        print('\033[1A'+input("Tópicoinválido.")+'\033[K',end="\r")
                                        print('\033[1A                            \033[K',end="\r")
                                    #endif
                                #endwhile
                                break

                            elif(op == 2):
                                while True:

                                    newTw = input("\nInsira Novo Tweet: ")

                                    if(VerfTweet(newTw)):
                                        ln[3]=str(newTw)
                                        ln='-'.join(ln)
                                        ln+='\n'
                                        numLn[i]=ln
                                        break
                                        #endif
                                    else:
                                        print('\033[1A'+input("Tweet tem de ter pelo menos um character com um máximo de 250.")+'\033[K',end="\r")
                                        print('\033[1A                            \033[K',end="\r")
                                    #endif
                                #endwhile
                                break

                            elif(op == 0):
                                found = -1
                                break

                            else:
                                found = -5
                                print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                                print('\033[1A                            \033[K',end="\r")
                            #endif
                        #endwhile
                        if(found != -5):
                            break
                    #endif
                    i+=1
                #endfor
                
                if(found == 0):
                    input("Tweet não existe")
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