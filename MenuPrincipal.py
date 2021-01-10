from MenuCreator import CreateMenu
from GestorUtilizador import MenuUtilizador
from GestorTweets import MenuTweets

def MenuPrincipal():
    while True:
        opc = CreateMenu.PrintMenu("Menu Principal",["Gerir Utilizadores","Gerir Tweets"],2)

        if opc == 0:
            break

        elif opc == 1:#Parte de Utilizadores
            CreateMenu.Clear()
            MenuUtilizador.MenuUtilz()

        elif opc == 2:#Parte de Tweets
            CreateMenu.Clear()
            MenuTweets.MenuTwts()

#end

MenuPrincipal()