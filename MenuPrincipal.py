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

        while True:
            admin=0
            print("Login\n")
            
            email = input("Insira email: ")

            if(VerfEmail(email)):
                if(VerfExist(email) or email == "admin@admin.com"):
                    try:
                        num = int(input("Insira numero: "))

                    except ValueError:
                        input("Número inválido")
                        CreateMenu.Clear()
                        continue
                    
                    if(num == 1 and email == "admin@admin.com"):
                        admin=1
                        break
                    #endif

                    if(num<1000000 or num>9999999):
                        input("Número tem que ter 7 digitos")
                        CreateMenu.Clear()

                    else:
                    
                        if(VerfExist(num)):
                            
                            name = GetName(email,num)
                            break

                        else:
                            input("Número errado")
                            CreateMenu.Clear() 
                    #endif
                else:
                    input("Email não existe.")
                    CreateMenu.Clear()

            else:
                input("Email inválido.")
                CreateMenu.Clear()
            #endif
        #endwhile

        if(admin==1):
            CreateMenu.Clear()
            return "admin"
        
        else:
            return name
        #endif
    else:
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
            input("wait")
            CreateMenu.Clear()
            #MenuUtilizador.MenuUtilz()

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
            else:
                MenuPrinU(name)
            #   MenuPrinUtil(name)
            #MenuUtilizador.MenuUtilz()

        elif opc == 2:#sign
            CreateMenu.Clear()
            MenuTweets.MenuTwU(name)

#end

Begin()