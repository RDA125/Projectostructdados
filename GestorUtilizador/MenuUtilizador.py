import MenuCreator.CreateMenu 
from GestorUtilizador import ListarUtilz

def MenuUtilz():
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Teste MenuUtilizador",["Inserir Util.","Alterar util.","Eliminar Util.","Listar Utilizadores"],4,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break

        elif opc == 1:

            print("Inserir - Progress")
            MenuCreator.CreateMenu.WaitEnter()

        elif opc == 2:
            print("Alterar - Progress")
            MenuCreator.CreateMenu.WaitEnter()

        elif opc == 3:
            print("Eliminar - Progress")
            MenuCreator.CreateMenu.WaitEnter()

        elif opc == 4:
            MenuCreator.CreateMenu.Clear()
            print("Listagem dos Utilizadores\n")
            ListarUtilz.ListarU("teste.html")
            print("\n")
            MenuCreator.CreateMenu.WaitEnter()
#end