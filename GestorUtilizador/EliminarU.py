from Validacao.ValidarDados import Checkfile,VerfName,VerfExist,UpdateFile
from MenuCreator.CreateMenu import Clear,WaitEnter
from GestorUtilizador import ListarUtilz

def Elim():

    if Checkfile('users.txt'):
        while True:
            print("Eliminação de Dados\n")

            f = open("users.txt","r",encoding="latin1")
            l = f.readline() #cabeçalho
            numLn = f.readlines() #informação na lista numLn
            f.close
            found=0
            i=0

            while True:
                sname = input("Insira nome do Utilizador que deseja Eliminar(0-Voltar atrás): ")

                if(sname == '0'):
                    Clear()
                    return

                if(VerfName(sname)):
                    break

                else:
                    print('\033[1A'+input("Nome inválido.")+'\033[K',end="\r")
                    print('\033[1A                            \033[K',end="\r")
                #endif
            #endwhile

        
            for ln in numLn:
                ln = ln.rstrip('\n')
                ln = ln.split("-")

                if(str(sname.lower()) in ln[0].lower()):
                    found=1
                    Nome,Email,Num,Telefone,Oper = ln
                    print("%-20s %-20s %-20s %-20s %s\n\n" % (Nome,Email,Num,Telefone,Oper))
                    
                    while True:
                        op= input('Tem a certeza que deseja eliminar este Utilizador(s/n)?')
                        
                        if((op != "s" and op != "S") and (op != "n" and op !="N")):
                            print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                            print('\033[1A                            \033[K',end="\r")
                        
                        else:
                            break
                        #endif
                    #endwhile

                    if(op != "s" and op != "S"):
                        found = -1
                        break
                               
                    else:
                        ln='-'.join(ln)
                        ln+='\n'
                        numLn.remove(ln)
                        break
                    #endif
                       
                #endif
                i+=1
            #endfor
            if(found == 0):
                input("Nome não existe")
                Clear()

            else:

                if(found == 1):

                    UpdateFile("users.txt",numLn)
                    
                    while True:
                        op = input("Utilizador eliminado com sucesso\nDeseja Eliminar mais?(s/n)\n")
                        
                        if((op != "s" and op != "S") and (op != "n" and op !="N")):
                            print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                            print('\033[3A                            \033[K',end="\r")
                        
                        else:
                            break
                        #endif
                    #endwhile
                else:
                   
                    while True:
                        op = input("Deseja Eliminar outro Utilizador?(s/n)\n")
                        
                        if((op != "s" and op != "S") and (op != "n" and op !="N")):
                            print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                            print('\033[2A                            \033[K',end="\r")
                        
                        else:
                            break
                        #endif
                    #endwhile
                #endif

                if(op != "s" and op != "S"):
                    if(found == 1):
                        Clear()
                        ListarUtilz.Listar()
                        break
                    else:
                        Clear()
                        break
                else:
                    op=0
                    Clear()
                #endif
            #endif
        #endwhile

    else:
        input('Não existe informação para ser Eliminada.')
        Clear()
    #endif

def ElimU(name):

    if Checkfile('users.txt'):
        while True:
            print("Eliminação de Dados\n")

            f = open("users.txt","r",encoding="latin1")
            l = f.readline() #cabeçalho
            numLn = f.readlines() #informação na lista numLn
            f.close
            found=0
            i=0
            
            sname = name
        
            for ln in numLn:
                ln = ln.rstrip('\n')
                ln = ln.split("-")

                if(str(sname.lower()) in ln[0].lower()):
                    found=1
                    Nome,Email,Num,Telefone,Oper = ln
                    print("%-20s %-20s %-20s %-20s %s\n\n" % (Nome,Email,Num,Telefone,Oper))

                    op= input('Tem a certeza que deseja eliminar(s/n)?')

                    if((op != "s" and op != "S") and (op != "n" and op !="N")):
                        found = -2
                        print('\033[1A'+input("Opção inválida")+'\033[K',end="\r")
                        print('\033[1A                            \033[K',end="\r")
                    
                    else:
                        if(op != "s" and op != "S"):
                            found = -1
                            break
                                   
                        else:
                            ln='-'.join(ln)
                            ln+='\n'
                            numLn.remove(ln)
                            break
                        #endif
                       
                #endif
                i+=1
            #endfor

            if(found == 1):
                UpdateFile("users.txt",numLn)
                op = input("Utilizador eliminado com sucesso\n")
                Clear()
                return True

            elif(found == -1):
                Clear()
                return False
            
            else:
                Clear()
            #endif
        #endwhile

    else:
        input('Não existe informação para ser Eliminada.')
        Clear()
    #endif