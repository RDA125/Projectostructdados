import os
import sys
from MenuCreator import CreateMenu
from GestorUtilizador import MenuUtilizador,InserirU
from GestorTweets import MenuTweets
from Validacao.ValidarDados import Checkfile,VerfName,VerfEmail,VerfExist,GetName

def Login():
    
    if(Checkfile("users.txt")):
        f=open("users.txt","r")
        l= f.readline()
        numLn = f.readlines
        name = ""
        success = -1
        c = 3

        while True:
            admin=0

            print("Login\n(0-Voltar atrás)\n")
           
            email = input("Insira email: ")

            if(email == "0"):
                name = None
                return name
            #endif

            if(VerfEmail(email)):
                if(VerfExist(email) or email == "admin@admin.com"):
                    try:
                        num = int(input("Insira numero: "))

                    except ValueError:
                        c-=1
                        input("Número inválido. %d Tentativa(s) restante(s)." % c)
                        CreateMenu.Clear()
                        continue
                    
                    if(num == 1 and email == "admin@admin.com"):
                        admin=1
                        break
                    #endif

                    if(num<1000000 or num>9999999):
                        c-=1
                        input("Número tem que ter 7 digitos. %d Tentativa(s) restante(s)." % c)
                        CreateMenu.Clear()

                    else:
                        
                        if(VerfExist(num) and email != "admin@admin.com"):
                            
                            name = GetName(email,num)
                            break

                        else:
                            c-=1
                            input("Número errado.\n%d Tentativa(s) restante(s)." % c)
                            CreateMenu.Clear() 
                    #endif
                else:
                    input("Email não existe.\n%d Tentativa(s) restante(s)." % c)
                    CreateMenu.Clear()

            else:
                c-=1
                input("Email inválido.\n%d Tentativa(s) restante(s)." % c)
                CreateMenu.Clear()
            #endif
            
            if(c <= 0):
                input("Tentativas gastas, tente depois.")
                return
            #endif
            
        #endwhile

        if(admin==1):
            CreateMenu.Clear()
            return "admin"
        else:
            return name
        #endif
    else:
        input("Não existe users para fazer login.\nPrima enter para fazer Sign in")
        InserirU.Inserir()
        name = Login()
    #endif


def MenuPrincipal():
    while True:
        opc = CreateMenu.PrintMenu("Menu Principal Admin",["Gerir Utilizadores","Gerir Tweets"],2,"Logout")

        if opc == 0:
            CreateMenu.Clear()
            break

        elif opc == 1:#Parte de Utilizadores
            CreateMenu.Clear()
            MenuUtilizador.MenuUtilz()

        elif opc == 2:#Parte de Tweets
            CreateMenu.Clear()
            MenuTweets.MenuTwts()

#end

def MenuPrinU(name):
    while True:
        opc = CreateMenu.PrintMenu("Menu Principal",["Gerir Dados","Gerir Tweets"],2,"Logout")

        if opc == 0:
            CreateMenu.Clear()
            break

        elif opc == 1:#Parte de Utilizadores
            CreateMenu.Clear()
            if(MenuUtilizador.MenuUTw(name)):
                break

        elif opc == 2:#Parte de Tweets
            CreateMenu.Clear()
            MenuTweets.MenuTwU(name)

#end

def Begin():
    while True:
        opc = CreateMenu.PrintMenu("",["Login","Sign in"],2)

        if opc == 0:
            break

        elif opc == 1:#login
            CreateMenu.Clear()
            name = Login()
            CreateMenu.Clear()
            
            if(name == "admin"):
                MenuPrincipal()

            elif(name == None):
                CreateMenu.Clear()

            else:
                MenuPrinU(name)
            #endif

        elif opc == 2:#sign
            CreateMenu.Clear()
            InserirU.Inserir()
        #endif

#end

Begin()