from Validacao.ValidarDados import Checkfile,VerfName,VerfEmail,VerfExist,UpdateHtml
from MenuCreator.CreateMenu import Clear,WaitEnter

def Inserir():
    Checkfile("users.txt")

    f = open("users.txt","a")

    while True:
        print("Inserir Utilizador\n")

        name = input("Insira Nome: ")

        if(VerfName(name)):
            if(VerfExist(name)):
                input("Nome já existe.")
                Clear()

            else:
                break

        else:
            input("Nome inválido.")
            Clear()
        #endif

    while True:
        email = input("Insira Email: ")

        if(VerfEmail(email)):
            if(VerfExist(email)):
                print('\033[1A'+input("Email já existe.")+'\033[K',end="\r")
                print('\033[1A                            \033[K',end="\r")

            else:
                break

        else:
            print('\033[1A'+input("Email inválido.")+'\033[K',end="\r")
            print('\033[1A                            \033[K',end="\r")
        #endif

    while True: 
        try:
            tel = int(input("Telefone: "))

        except ValueError:
            print('\033[1A'+input("Número de Telefone inválido")+'\033[K',end="\r")
            print('\033[1A                            \033[K',end="\r")

            continue 
        
        if(tel<910000000 or tel>999999999):
            print('\033[1A'+input("Número de Telefone inválido [910000000-999999999]")+'\033[K',end="\r")
            print('\033[1A                            \033[K',end="\r")

        else:
            if(VerfExist(tel)):
                print('\033[1A'+input("Número de Telefone já existe.")+'\033[K',end="\r")
                print('\033[1A                            \033[K',end="\r")
            else:
                break
        #endif
    #endwhile


    print(name,email,tel, file=f,sep="-",end='\n')
    f.close()

    UpdateHtml("teste.html")

    Clear()
    print("Utilizador inserido com sucesso: ")
    print("Nome: %5s" % name)
    print("E-Mail: %5s" % email)
    print("Telefone: %5s" % tel)
    WaitEnter()
