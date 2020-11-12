matriz=[]
for i in range(3):
    matriz.append([])
    for j in range(4):
        matriz[i].append(0)

matriz[0][0]="L"
matriz[0][1]="L"
matriz[0][2]="W"
matriz[0][3]="L"
matriz[1][0]="W"
matriz[1][1]="L"
matriz[1][2]="W"
matriz[1][3]="L"
matriz[2][0]="L"
matriz[2][1]="L"
matriz[2][2]="W"
matriz[2][3]="W"

#pasar i=1,j=2
cont=0
visitados=[]
def recorrer(matriz,i,j,cont,visitados):
    if i!=0 or j!=0:
        #i=0 j=1
        if matriz[i-1][j-1] == "W" and (matriz[i-1][j-1] not in vistados):
            visitados.append(matriz[i-1][j-1])
            print(matriz[i-1][j-1])
            cont+=1
            print(cont)
            cont+=recorrer(matriz,i-1,j-1,cont,visitados)
        #i=0 j=2
        elif matriz[i-1][j]=="W" and (matriz[i-1][j] not in vistados):
            visitados.append(matriz[i-1][j])
            print(matriz[i][j-1])
            cont+=1
            print(cont)
            cont+=recorrer(matriz,i-1,j,cont,visitados)
        else:
            return cont
        
        
cont=recorrer(matriz,1,2,cont,visitados)
for i in range(3):
    print(matriz[i])
print("cont: ",cont,visitados)
    

