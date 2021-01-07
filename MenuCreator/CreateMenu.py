from os import system

def Clear():
    _ = system('cls')

#end 

def WaitEnter():
    input("Prima enter para continuar ...")
    Clear()
#end

def PrintMenu(Title, opcs, numOpc, exitmsg=''):
    while True:
        try:
            print(Title+"\n")

            for i in range(numOpc):
                print(i+1,": ",opcs[i])
            #endfor

            if(exitmsg):
                print("0 : ",exitmsg,"\n")
            else:
                print("0 :  Terminar Programa.\n")
                
            #endif

            opc = int(input("Escolha uma opção:"))

        except ValueError:
            input("Opção tem que ser um valor inteiro.")
            Clear()

            continue
        #end

        if(opc<0 or opc>numOpc):
            input("Opção não existe.")
            Clear()
        else:
            break
        #endif

    return opc
#end