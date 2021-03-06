import MenuCreator.CreateMenu 
from GestorUtilizador import ListarUtilz,InserirU,AlterarU,EliminarU,PesquisaU

def MenuUtilz():
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Utilizador",["Inserir Util.","Alterar util.","Eliminar Util.","Listar Utilizadores","Pesquisar Util.","Contar"],6,"Voltar atrás")

        if (opc == 0):
            MenuCreator.CreateMenu.Clear()
            break

        elif (opc == 1):#Inserir Utilizadores
            MenuCreator.CreateMenu.Clear()
            InserirU.Inserir()

        elif (opc == 2):#Alterar dados de utilizador
            MenuCreator.CreateMenu.Clear()
            AlterarU.Alterar()

        elif (opc == 3):#Eliminar Utilizador
            MenuCreator.CreateMenu.Clear()
            EliminarU.Elim()

        elif (opc == 4): #listar Utilizadores
            MenuCreator.CreateMenu.Clear()
            ListarUtilz.ListarU("Users.html")
        
        elif (opc == 5): #pesquisar Utilizadores
            MenuCreator.CreateMenu.Clear()
            PesquisaU.PesqUtil()
        
        elif (opc == 6): #contar e agrupar Utilizadores
            MenuCreator.CreateMenu.Clear()
            PesquisaU.CountU()

#end

def MenuUTw(name):
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Utilizador",["Alterar Dados","Eliminar conta"],2,"Voltar atrás")

        if (opc == 0):
            MenuCreator.CreateMenu.Clear()
            break

        elif (opc == 1):#Alterar dados de utilizador
            MenuCreator.CreateMenu.Clear()
            name = AlterarU.Alterar(name)

        elif (opc == 2):#Eliminar Utilizador
            MenuCreator.CreateMenu.Clear()
            if(EliminarU.ElimU(name)):
                return True

#end