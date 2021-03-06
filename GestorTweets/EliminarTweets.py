from Validacao.ValidarDados import CheckfileTw,UpdateFileTw
from MenuCreator.CreateMenu import Clear,WaitEnter
from GestorTweets import ListarTweets

def ElimTw(name=""):

    if CheckfileTw('tweets.txt'):
        while True:
            print("Eliminação de Tweets\n")

            f = open("tweets.txt","r",encoding="latin1")
            l = f.readline() #cabeçalho
            numLn = f.readlines() #informação na lista numLn
            f.close
            numUTw = 0
            found=0
            sId = -1
            i=0

            
            if(name != ""):
                for ln in numLn:
                    ln = ln.rstrip('\n')
                    ln = ln.strip()
                    Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                    if(name.lower() == Nome.lower()):
                        print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
                        numUTw+=1
                    #endif
                #endfor
            else:
                for ln in numLn:
                    ln = ln.rstrip('\n')
                    Id,idResp,Nome,Tp,Tw,Lk = ln.split("-")

                    print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
                #endfor
                numUTw = -1
            #endif

            if(numUTw != 0):
                try:
                    sId = int(input("Insira o Id do tweet que deseja Eliminar(0-Voltar atrás): "))
                except ValueError:
                    found = -2
                    print('\033[1A'+input("Id inválido")+'\033[K',end="\r")
                    print('\033[1A                            \033[K',end="\r")

                   
                if(sId == 0):
                    Clear()
                    return
                #endif
            
                for ln in numLn:
                    ln = ln.rstrip('\n')
                    ln = ln.split("-")

                    if(str(sId) in ln[0]):
                        found=1
                        Id,idResp,Nome,Tp,Tw,Lk = ln
                        print("%-5s %-5s %-5s \"%s\" - %s" % (Id,Nome,Tp,Tw,Lk))
                        
                        while True:
                            op= input('Tem a certeza que deseja eliminar este Tweet(s/n)?')

                            if((op != "s" and op != "S") and (op != "n" and op !="N")):
                                print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                                print('\033[1A                            \033[K',end="\r")

                            else:
                                break
                            #endif
                        #endwhile
                        
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
                    input("Tweet não existe")
                    Clear()

                elif(found == -2):
                    Clear()

                else:

                    if(found == 1):

                        UpdateFileTw("tweets.txt",numLn)
                        while True:
                            op = input("Tweet eliminado com sucesso\nDeseja Eliminar mais?(s/n)")
                            
                            if((op != "s" and op != "S") and (op != "n" and op !="N")):
                                print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                                print('\033[2A                            \033[K',end="\r")
                            
                            else:
                                break
                            #endif
                        #endwhile

                    else:
                        while True:
                            op = input("Deseja Eliminar outro Tweet?(s/n)\n")
                            
                            if((op != "s" and op != "S") and (op != "n" and op !="N")):
                                print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                                print('\033[2A                            \033[K',end="\r")
                            
                            else:
                                break
                            #endif
                        #endwhile
                    #endif

                    if(op != "s" and op != "S"):
                        if(found == 1):
                            Clear()
                            ListarTweets.ListarUTw(name)
                            break
                        else:
                            Clear()
                            break
                    else:
                        op=0
                        Clear()
                    #endif
                #endif
            else:
                input("Não tem tweets para eliminar.")
                Clear()
                break
        #endwhile

    else:
        input('Não existe informação para ser Eliminada.')
        Clear()
    #endif