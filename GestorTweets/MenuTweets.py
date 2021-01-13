import MenuCreator.CreateMenu 
from GestorTweets import ListarTweets,InserirTweets,AlterarTweets,EliminarTweets,RespondeTweet

def MenuTwts():
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Eliminar Tweet","Listar Tweets"],4,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break

        elif opc == 1:#Eliminar Utilizador
            MenuCreator.CreateMenu.Clear()
            EliminarTweets.ElimTw()

        elif opc == 2: #listar Utilizadores
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarTw("Tweets.html")

#end

#menu user inserir/alterar/eliminar/listar os seus tweets
def MenuTwU(name):
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Ver Tweets","Inserir Tweet","Alterar Tweet","Eliminar Tweet","Seus Tweets","Responder a Tweets"],6,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break
        
        elif opc == 1:
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarTw("Tweets.html")

        elif opc == 2:#Inserir Utilizadores
            MenuCreator.CreateMenu.Clear()
            InserirTweets.InserirTw(name)

        elif opc == 3:#Alterar dados de utilizador
            MenuCreator.CreateMenu.Clear()
            AlterarTweets.AlterarTw(name)

        elif opc == 4:#Eliminar Utilizador
            MenuCreator.CreateMenu.Clear()
            EliminarTweets.ElimTw(name)
            ListarTweets.ListarUTw(name)

        elif opc == 5:
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarUTw(name)

        elif opc == 6:
            MenuCreator.CreateMenu.Clear()
            RespondeTweet.RespTw(name)
#end