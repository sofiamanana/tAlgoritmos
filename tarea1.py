#Falta dejar el formato de salida de texto
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
            listas_wenas.append(lista_aux)
            print(lista_aux)
    elif(sum(lista_aux)>t):
        suma(L[1:],lista,t)
    elif(sum(lista_aux)<t):
        suma(L[1:],lista,t)
        suma(L[1:],lista_aux,t)
    return


#Formato de archivo de texto: T(valor de suma) L(largo de lista) N(L numeros)
def pasar_a_lista(textfile):
    t = 0;
    L = 0;
    lista_1=[]
    global listas_wenas
    archivo = open(textfile, "r")
    lista = []
    lista_real = []
    for linea in archivo:
        lista = linea.split()
        t = int(lista[0])
        L = int(lista[1])
        for i in range(2,L+2):
            lista_real.append(int(lista[i]))
        lista_real.sort()
        #print(lista_real)
        print("Suma de",t,":")
        if (lista_real == []):
            print("Lista vacia")
        else:
            suma(lista_real,lista_1,t)
        #haz algo con la lista_real y volver todo a 0
        t = 0
        L = 0
        listas_wenas=[]
        lista_1 = []
        lista_real = []

        print("------------")
    archivo.close()

pasar_a_lista("algo.txt")
