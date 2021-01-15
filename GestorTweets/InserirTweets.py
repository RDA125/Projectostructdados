from Validacao.ValidarDados import CheckfileTw,VerfName,VerfExist,VerfTweet,UpdateHtmlTw
from MenuCreator.CreateMenu import Clear,WaitEnter

def InserirTw(name):
    CheckfileTw("tweets.txt")
    Lk=0 #likes começão a 0
    idResp = 0 #Inserir <=> postar um tweet

    #p = id do tweet
    f= open("tweets.txt",'r')
    ln = f.readlines()
    f.close()

    p = len(ln)

    for l in ln:
        l = l.rstrip('\n')
        l = l.lower()
        l = l.split('-')

        if(str(p) == l[0]):
            p+=1
        #endif
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
        tw = input('Insira Tweet[280char]: ')

        if(VerfTweet(tw)):
            break

        else:
            print('\033[1A'+input("Tweet tem de ter pelo menos um character com um máximo de 280.")+'\033[K',end="\r")
            print('\033[1A                            \033[K',end="\r")
        #endif
    #endwhile

    print(p,idResp,name,top,tw,Lk, file=f,sep="-",end='\n')
    f.close()

    UpdateHtmlTw("Tweets.html")
    input("Tweet inserido com sucesso.")
    Clear()
