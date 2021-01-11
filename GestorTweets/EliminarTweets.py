from Validacao.ValidarDados import CheckfileTw,UpdateFileTw
from MenuCreator.CreateMenu import Clear,WaitEnter
from GestorTweets import ListarTweets

def ElimTw():

    if CheckfileTw('tweets.txt'):
        while True:
            print("Eliminação de Tweets\n")

            f = open("tweets.txt","r",encoding="latin1")
            l = f.readline() #cabeçalho
            numLn = f.readlines() #informação na lista numLn
            f.close
            found=0
            i=0

            while True:
                try:
                    sId = int(input("Insira o Id do tweet que deseja Eliminar(0-Voltar atrás): "))
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

                if(str(sId) in ln[0]):
                    found=1
                    Id,Tp,Tw,Lk = ln
                    print("%-20s %-20s %s - %s\n\n" % (Id,Tp,Tw,Lk))

                    op= input('Tem a certeza que deseja eliminar este Tweet(s/n)?')

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
                input("Tweet não existe")
                Clear()

            else:

                if(found == 1):

                    UpdateFileTw("tweets.txt",numLn)
                    op = input("Tweet eliminado com sucesso\nDeseja Eliminar mais?(s/n)\n")

                else:
                    op = input("Deseja Eliminar outro Tweet?(s/n)\n")
                #endif

                if((op != "s" and op != "S") and (op != "n" and op !="N")):
                    print("Opção inválida")
                
                else:
                    if(op != "s" and op != "S"):

                        if(found == 1):
                            Clear()
                            ListarTweets.ListarTw("Tweets.html")
                            break
                        else:
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