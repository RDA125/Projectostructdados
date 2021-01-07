from Validacao.ValidarDados import Checkfile
from MenuCreator.CreateMenu import Clear,WaitEnter

#dont forget listas
def Inserir():
    Checkfile("users.txt")

    f = open("users.txt","a")

    while True:
        print("Inserir Utilizador\n")

        nome = input("Insira Nome: ")

        # if validação nome pode usar clear
        break

    while True:
        email = input("Insira Email: ")

        # if validação nome pode usar clear

        break

    while True: 
        try:
            tel = int(input("Telefone: "))

        except ValueError:
            print("Número de Telefone inválido")
            WaitEnter()
            # maneira de limpar uma só linha

            continue 
        
        if(tel<100000000 or tel>999999999):
            input("Número de Telefone tem que ter 9 digitos")
            
            # maneira de limpar uma só linha
        
        else:
            break
        #endif
    #endwhile


    print(nome,email,tel, file=f,sep="-",end='')
    f.close()
    print("Utilizador inserido com sucesso: ")
    print("Nome: %5s" % nome)
    print("E-Mail: %5s" % email)
    print("Telefone: %5s" % tel)
    WaitEnter()
