import MenuCreator.CreateMenu 
from GestorUtilizador import ListarUtilz,InserirU,AlterarU,EliminarU

def MenuTwts():
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Inserir Tweet","Alterar Tweet","Eliminar Tweet","Listar Tweets"],4,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break

        elif opc == 1:#Inserir Utilizadores
            print("Inserir tweets Teste")
            MenuCreator.CreateMenu.WaitEnter()

        elif opc == 2:#Alterar dados de utilizador
            print("Alterar tweets Teste")
            MenuCreator.CreateMenu.WaitEnter()

        elif opc == 3:#Eliminar Utilizador
            print("Eliminar tweets Teste")
            MenuCreator.CreateMenu.WaitEnter()

        elif opc == 4: #listar Utilizadores
            print("Listar tweets Teste")
            MenuCreator.CreateMenu.WaitEnter()

#end