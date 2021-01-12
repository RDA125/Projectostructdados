import MenuCreator.CreateMenu 
from GestorTweets import ListarTweets,InserirTweets,AlterarTweets,EliminarTweets

def MenuTwts():
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Eliminar Tweet","Listar Tweets"],4,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break

        elif opc == 1:#Eliminar Utilizador
            MenuCreator.CreateMenu.Clear()
            EliminarTweets.ElimTw("")

        elif opc == 2: #listar Utilizadores
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarTw("Tweets.html")

#end

#menu user inserir/alterar/eliminar/listar os seus tweets
def MenuTwU(name):
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Inserir Tweet","Alterar Tweet","Eliminar Tweet","Seus Tweets"],4,"Voltar atrás")

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
            EliminarTweets.ElimTw(name)

        elif opc == 4:
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarUTw(name)
#end