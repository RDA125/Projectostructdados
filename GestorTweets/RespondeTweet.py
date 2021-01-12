from Validacao.ValidarDados import CheckfileTw,VerfName,VerfExist,VerfTweet,UpdateHtmlTw
from MenuCreator.CreateMenu import Clear,WaitEnter

def RespTw(name):
    CheckfileTw("tweets.txt")
    Lk=0 #likes começão a 0
    i=0

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

    while True:
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

            if(str(sId) == ln[0]):
                while True:
                    tw = input('Insira Tweet[250char]: ')

                    if(VerfTweet(tw)):
                        break

                    else:
                        print('\033[1A'+input("Tweet tem de ter pelo menos um character com um máximo de 250.")+'\033[K',end="\r")
                        print('\033[1A                            \033[K',end="\r")
                    #endif
                #endwhile
                top = ln[2]
                Resp = [str(p),name,top,tw,str(Lk)]
                Resp='-'.join(Resp)
                Resp+='\n'
                numLn.insert((i+1),Resp)   

            #endif
            i+=1



    f = open("tweets.txt","a")

    while True:
        print("Inserir Tweet\n")

        top = input("Insira Tópico: ")

        if(VerfName(top)):
            break

        else:
            input("Tópico inválido.")
            Clear()
        #endif

    while True:
        tw = input('Insira Tweet[250char]: ')

        if(VerfTweet(tw)):
            break

        else:
            print('\033[1A'+input("Tweet tem de ter pelo menos um character com um máximo de 250.")+'\033[K',end="\r")
            print('\033[1A                            \033[K',end="\r")
        #endif
    #endwhile

    print(p,name,top,tw,Lk, file=f,sep="-",end='\n')
    f.close()

    UpdateHtmlTw("Users.html")
    input("Tweet inserido com sucesso.")
    Clear()
