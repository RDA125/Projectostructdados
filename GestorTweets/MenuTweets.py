import MenuCreator.CreateMenu 
from GestorTweets import ListarTweets,InserirTweets,AlterarTweets#,EliminarU

def MenuTwts():
    while True:
        opc = MenuCreator.CreateMenu.PrintMenu("Menu Tweets",["Inserir Tweet","Alterar Tweet","Eliminar Tweet","Listar Tweets"],4,"Voltar atrás")

        if opc == 0:
            MenuCreator.CreateMenu.Clear()
            break

        elif opc == 1:#Inserir Utilizadores
            MenuCreator.CreateMenu.Clear()
            InserirTweets.InserirTw()

        elif opc == 2:#Alterar dados de utilizador
            MenuCreator.CreateMenu.Clear()
            AlterarTweets.AlterarTw()

        elif opc == 3:#Eliminar Utilizador
            print("Eliminar tweets Teste")
            MenuCreator.CreateMenu.WaitEnter()

        elif opc == 4: #listar Utilizadores
            MenuCreator.CreateMenu.Clear()
            ListarTweets.ListarTw("Tweets.html")

#end