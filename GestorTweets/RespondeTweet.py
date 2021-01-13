from Validacao.ValidarDados import CheckfileTw,VerfName,VerfExist,VerfTweet,UpdateHtmlTw,UpdateFileTw
from MenuCreator.CreateMenu import Clear,WaitEnter
import re

def RespTw(name):
    CheckfileTw("tweets.txt")
    Lk=0 #likes começão a 0
       
    while True:
        i=0
        found=0
        #p = id do tweet
        f= open("tweets.txt",'r')
        l = f.readline()
        numLn = f.readlines()
        f.close()

        p = len(numLn) + 1

        for lh in l:
            lh = lh.rstrip('\n')
            lh = lh.lower()
            lh = lh.split('-')

            if(str(p) == lh[0]):
                p+=1
            #endif
        #endfor
   
        print("Responder Tweet\n")

        try:
            sId = int(input("Insira Id do tweet a responder(0-voltar atrás): "))

        except ValueError:
            print('\033[1A'+input("Número inválido")+'\033[K',end="\r")
            print('\033[1A                            \033[K',end="\r")

      
        if(sId == 0):
            Clear()
            return
        #endif

        for ln in numLn:
            ln = ln.rstrip('\n')
            ln = ln.split("-")

            if(str(sId) == ln[0].strip()):
                found=1
                while True:
                    tw = input('Insira Tweet[250char]: ')

                    if(VerfTweet(tw)):
                        break

                    else:
                        print('\033[1A'+input("Tweet tem de ter pelo menos um character com um máximo de 250.")+'\033[K',end="\r")
                        print('\033[1A                            \033[K',end="\r")
                    #endif
                #endwhile
                top = ln[3]
                Resp = [str(p),ln[0].strip(),name,top,tw,str(Lk)]
                Resp='-'.join(Resp)
                Resp+='\n'
                numLn.insert((i+1),Resp)   

            #endif
            i+=1
        #endfor

        if(found == 1):

            UpdateFileTw("tweets.txt",numLn)
            while True:
                op = input("Resposta guardada com sucesso\nDeseja responder a mais algum?(s/n)\n")
                
                if((op != "s" and op != "S") and (op != "n" and op !="N")):
                    print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                    print('\033[1A                            \033[K',end="\r")
                            
                else:
                    break
                #endif
            #endwhile

            if(op != "s" and op != "S"):
                Clear()
                break
            else:
                op=0
                Clear()
            #endif

        else:
            input("Tweet não existe")
            Clear()
        #endif
    #endWhile
