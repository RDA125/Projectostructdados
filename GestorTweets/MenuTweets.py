import MenuCreator.CreateMenu 
from GestorTweets import ListarTweets,InserirTweets,AlterarTweets,EliminarTweets

def MenuTwts():
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Inserir Tweet","Alterar Tweet","Eliminar Tweet","Listar Tweets"],4,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break

        elif opc == 1:#Inserir Utilizadores - Remover para admin
            MenuCreator.CreateMenu.Clear()
            #InserirTweets.InserirTw()

        elif opc == 2:#Alterar dados de utilizador - Remover para admin
            MenuCreator.CreateMenu.Clear()
            #AlterarTweets.AlterarTw()

        elif opc == 3:#Eliminar Utilizador
            MenuCreator.CreateMenu.Clear()
            EliminarTweets.ElimTw()

        elif opc == 4: #listar Utilizadores
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarTw("Tweets.html")

#end

#menu user inserir/alterar/eliminar
def MenuTwU(name):
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Inserir Tweet","Alterar Tweet","Eliminar Tweet"],3,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break

        elif opc == 1:#Inserir Utilizadores
            MenuCreator.CreateMenu.Clear()
            InserirTweets.InserirTw(name)

        elif opc == 2:#Alterar dados de utilizador
            MenuCreator.CreateMenu.Clear()
            AlterarTweets.AlterarTw(name)

        elif opc == 3:#Eliminar Utilizador
            MenuCreator.CreateMenu.Clear()
            EliminarTweets.ElimTw()

#end