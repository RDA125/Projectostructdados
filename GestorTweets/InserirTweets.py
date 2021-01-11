from Validacao.ValidarDados import CheckfileTw,VerfName,VerfTweet,UpdateHtmlTw
from MenuCreator.CreateMenu import Clear,WaitEnter

def InserirTw():
    CheckfileTw("tweets.txt")
    Lk=0 #likes começão a 0

    #p = id do tweet
    f= open("tweets.txt",'r')
    ln = f.readlines()
    f.close()

    p = len(ln)
    #endfor

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

    print(p,top,tw,Lk, file=f,sep="-",end='\n')
    f.close()

    UpdateHtmlTw("Users.html")
    input("Tweet inserido com sucesso.")
    Clear()
