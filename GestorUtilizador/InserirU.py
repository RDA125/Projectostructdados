from Validacao.ValidarDados import Checkfile,VerfName,VerfEmail,VerfExist,UpdateHtml
from MenuCreator.CreateMenu import Clear,WaitEnter

#dont forget listas
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
                input("Email já existe.")
                
            else:
                break

        else:
            input("Email inválido.")
            #clear uma linha
        #endif

    while True: 
        try:
            tel = int(input("Telefone: "))

        except ValueError:
            print("Número de Telefone inválido")
            WaitEnter()
            # maneira de limpar uma só linha

            continue 
        
        if(tel<910000000 or tel>999999999):
            input("Número de Telefone tem que ter 9 digitos")
            
            # maneira de limpar uma só linha
        
        else:
            if(VerfExist(tel)):
                input("Número de Telefone já existe.")
                
            else:
                break
        #endif
    #endwhile


    print(name,email,tel, file=f,sep="-",end='')
    f.close()
    UpdateHtml("teste.html")

    Clear()
    print("Utilizador inserido com sucesso: ")
    print("Nome: %5s" % name)
    print("E-Mail: %5s" % email)
    print("Telefone: %5s" % tel)
    WaitEnter()
