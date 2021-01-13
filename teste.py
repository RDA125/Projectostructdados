#lista = "Teste1 teste2 teste3"
#
#l = lista.split('\n')
#
#for i in range(len(lista)):
#    l[i]+="*"
#
#lista = '\n'.join(l)
#print(lista)
#input()


#text = "Teste1\nteste2\nteste3"
## Separate line and add an asterisk
#lines = text.split('\n')
#for l in lines:
#    print(" ")
# 
# # Connecting lines
#text = '\n'.join(lines)
#
#print(text)
#input()
#

m=[1, 2, 3, [4, 5, [6, 7]], 8]
def fn(item,level=0):
    for each_item in item:
        if isinstance(each_item,list):
            fn(each_item,level+1)
        else:
            indentation = '\t' * level
            print("%s%s" %(indentation,each_item))


numLn=['\t1-0-Test-test-olá test 1 2 3-0\n','2-1-Test-test-test y-0\n','3-2-Test-test-test 2-0\n','\t6-2-Test-test-test 4-0\n','4-1-Test-test-test 3-0\n','7-4-Test-test-test 3-0\n','8-1-Test-test-test 3-0\n','5-0-Test-test-test 4-0\n']
numLn.sort()
print(numLn)
input()
def test(numLn,level=0):

    for i in range(len(numLn)):
        indentation = '\t' * level
        print("%s%s" %(indentation,numLn[i]))
        if((i+1)<len(numLn)):
            if(numLn[i+1][2] == "0"):
                level = 0
            elif(numLn[i+1][2]>numLn[i][2]):
                level+=1
            elif(numLn[i+1][2]<numLn[i][2]):
                level-=1
        elif((i+1)>len(numLn)):
            break
            

              



test(numLn,0)
input()