#el yuyo lo dejó de pana
matriz = []
consultas = []
contador = 0
m_max=0
n_max=0
numeros = ['0','1','2','3','4','5','6','7','8','9']
lista_visitados=[]
contador=0

#x = m, y=n
def recorrer(matriz1,m,n):
    global contador
    global lista_visitados
    global m_max
    global n_max
    if([m,n]) not in lista_visitados:
        lista_visitados.append([m,n])
        contador=contador+1
    if(m_max>m+1):
        if(matriz1[m+1][n]=="W"):
            if([m+1,n] not in lista_visitados):
                lista_visitados.append([m+1,n])
                contador=contador+1
                recorrer(matriz1,m+1,n)
    if(m-1>=0):
        if(matriz1[m-1][n]=="W"):
            if([m-1,n] not in lista_visitados):
                lista_visitados.append([m-1,n])
                contador=contador+1
                recorrer(matriz1,m-1,n)
    if(n_max>n+1):
        if(matriz1[m][n+1]=="W"):
            if([m,n+1] not in lista_visitados):
                lista_visitados.append([m,n+1])
                contador=contador+1
                recorrer(matriz1,m,n+1)
    if(n-1>=0):
        if(matriz1[m][n-1]=="W"):
            if([m,n-1] not in lista_visitados):
                lista_visitados.append([m,n-1])
                contador=contador+1
                recorrer(matriz1,m,n-1)
    if(m-1>=0 and n-1>=0):
        if(matriz1[m-1][n-1]=="W"):
            if([m-1,n-1] not in lista_visitados):
                lista_visitados.append([m-1,n-1])
                contador=contador+1
                recorrer(matriz1,m-1,n-1)
    if(m-1>=0 and n_max>n+1):
        if(matriz1[m-1][n+1]=="W"):
            if([m-1,n+1] not in lista_visitados):
                lista_visitados.append([m-1,n+1])
                contador=contador+1
                recorrer(matriz1,m-1,n+1)
    if(m_max>m+1 and n_max>n+1):
        if(matriz1[m+1][n+1]=="W"):
            if([m+1,n+1] not in lista_visitados):
                lista_visitados.append([m+1,n+1])
                contador=contador+1
                recorrer(matriz1,m+1,n+1)
    if(m_max>m+1 and n-1>=0):
        if(matriz1[m+1][n-1]=="W"):
            if([m+1,n-1] not in lista_visitados):
                lista_visitados.append([m+1,n-1])
                contador=contador+1
                recorrer(matriz1,m+1,n-1)

#nxm : filas(horizontal) x columnas
def pasar_a_matriz(textfile):
    global matriz
    global numeros
    global consultas
    global contador
    global lista_visitados
    global m_max
    global n_max
    n = 0;
    m = 0;
    casos = 0
    archivo = open(textfile, "r")
    casos = archivo.readline()
    archivo.readline() #se lee el espacio continuo a la cantidad de casos
    for linea in archivo:
        if (linea == "\n"):
            m = len(matriz[0])
            for elemento in consultas:
                consultas=elemento.split(" ")
                #print("consultas",consultas)
                m_max=n
                n_max=m
                recorrer(matriz,int(consultas[0])-1,int(consultas[1])-1)
                #print(lista_visitados)
                print(contador)
                contador = 0
                lista_visitados = []

 
            print("--------------")
            n = 0
            m = 0
            matriz = []
            consultas = []
        
        else:
            if(linea != "\n" and (linea[0] not in numeros)): #guardar en alguna parte
                matriz.append(linea.strip()) #se guardan las lineas de WL
                n += 1
            elif (linea[0] in numeros):
                consultas.append(linea.strip())
    
    #Esto trabaja la ultima matriz
    m = len(matriz[0])
    for elemento in consultas:
        consultas=elemento.split(" ")
        m_max=n
        n_max=m
        recorrer(matriz,int(consultas[0])-1,int(consultas[1])-1)
        #print(lista_visitados)
        print(contador)
        contador = 0
        lista_visitados = []
    matriz = []
    archivo.close()

pasar_a_matriz("algo2.txt")



