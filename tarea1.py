listas_wenas=[]

def suma(L,lista,t):
    if L==[]:
        return
    lista_aux=lista.copy()
    lista_aux.append(L[0])
    if(sum(lista_aux)==t):
        if(lista_aux in listas_wenas):
            None
        else:
            sumita=[]
            listas_wenas.append(lista_aux)
            for numero in lista_aux:
                sumita.append(str(numero))
                sumita.append("+")
            sumita.pop(-1)
            print(*sumita)
    elif(sum(lista_aux)>t):
        suma(L[1:],lista,t)
    elif(sum(lista_aux)<t):
        suma(L[1:],lista,t)
        suma(L[1:],lista_aux,t)
    return



#Formato de archivo de texto: T(valor de suma) L(largo de lista) N(L numeros)
flag =True
while flag == True:
    try:
        t = 0
        L = 0
        lista_1=[]
        lista_real = []
        lista = input().strip().split(" ")
        lista = [int(i) for i in lista]
        t = lista[0]
        L = lista[1]
        for i in range(2,L+2):
            lista_real.append(int(lista[i]))
        lista_real.sort()
        if (lista_real!=[]):
            print("Suma de",t,":")
            suma(lista_real,lista_1,t)
        #haz algo con la lista_real y volver todo a 0
        if (listas_wenas==[] and lista_real!=[]):
            print("NADA")
        t = 0
        L = 0
        listas_wenas=[]
        lista_1 = []
        lista_real = []
        
        
    except EOFError:
        flag= False

