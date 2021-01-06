from MenuCreator import CreateMenu
import GestorUtilizador.MenuUtilizador

def MenuPrincipal():
    while True:
        opc = CreateMenu.PrintMenu("Teste MenuPrin",["Gerir Utilizadores","Gerir Tweets"],2)

        if opc == 0:
            break

        elif opc == 1:

            GestorUtilizador.MenuUtilizador.MenuUtilz()

        elif opc == 2:
            print("Gerir tweets Teste")
            CreateMenu.WaitEnter()

#end

MenuPrincipal()