from MenuCreator import CreateMenu
import GestorUtilizador.MenuUtilizador

def MenuPrincipal():
    while True:
        opc = CreateMenu.PrintMenu("Menu Principal",["Gerir Utilizadores","Gerir Tweets"],2)

        if opc == 0:
            break

        elif opc == 1:
            CreateMenu.Clear()
            GestorUtilizador.MenuUtilizador.MenuUtilz()

        elif opc == 2:
            print("Gerir tweets Teste")
            CreateMenu.WaitEnter()

#end

MenuPrincipal()