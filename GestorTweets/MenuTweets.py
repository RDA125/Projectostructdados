import MenuCreator.CreateMenu 
from GestorTweets import ListarTweets,InserirTweets,AlterarTweets,EliminarTweets,RespondeTweet

def MenuTwts():
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Eliminar Tweet","Listar Tweets"],4,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break

        elif opc == 1:#Eliminar tweets
            MenuCreator.CreateMenu.Clear()
            EliminarTweets.ElimTw()

        elif opc == 2: #listar tweets
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarTw("Tweets.html")

#end

#menu user inserir/alterar/eliminar/listar os seus tweets
def MenuTwU(name):
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Ver Tweets","Inserir Tweet","Alterar Tweet","Eliminar Tweet","Seus Tweets"],5,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break
        
        elif opc == 1:#listar todos os tweets
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarTw("Tweets.html",name)

        elif opc == 2:#Inserir tweet
            MenuCreator.CreateMenu.Clear()
            InserirTweets.InserirTw(name)

        elif opc == 3:#Alterar dados de tweet
            MenuCreator.CreateMenu.Clear()
            AlterarTweets.AlterarTw(name)

        elif opc == 4:#Eliminar tweet
            MenuCreator.CreateMenu.Clear()
            EliminarTweets.ElimTw(name)
            ListarTweets.ListarUTw(name)

        elif opc == 5:#Listar tweet de util.
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarUTw(name)

        #pesquisa
        #contar
        #contar.agrupa

#end