import MenuCreator.CreateMenu 
from GestorUtilizador import ListarUtilz,InserirU

def MenuUtilz():
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Teste MenuUtilizador",["Inserir Util.","Alterar util.","Eliminar Util.","Listar Utilizadores"],4,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break

        elif opc == 1:#Inserir Utilizadores
            MenuCreator.CreateMenu.Clear()
            InserirU.Inserir()

        elif opc == 2:
            print("Alterar - Progress")
            MenuCreator.CreateMenu.WaitEnter()

        elif opc == 3:
            print("Eliminar - Progress")
            MenuCreator.CreateMenu.WaitEnter()

        elif opc == 4: #listar Utilizadores
            MenuCreator.CreateMenu.Clear()
            ListarUtilz.ListarU("teste.html")

#end