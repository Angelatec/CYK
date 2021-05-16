
"""Ángela Rodríguez Maldonado A01636960 Proyecto segundo Parcial Matemáticas computacionales
Algoritmo CYK:
Este Programa tiene como entrada dos listas una que representa los símbolos generadores, y otra 
los símbolos que son generados, esto representando una gramática libre de contexto en la forma normalizada
de Chomsky, y tiene como entrada también una cadena la cual se evalua para ver si puede ser generada
con esa gramática.
De salida tenemos la respuesta de si es generada o no, y en caso de que se pueda generar nos muestra el 
árbol de derivación de esta"""
class Nodo:
    def __init__(self,stri,izq,der):
        self.stri=stri
        self.izq=izq
        self.der=der
        #self.padre=padre

    def left(self,izq):
        self.izq=izq
    def right(self,der):
        self.der=der
    
    def nivel(self):
        queue=[]
        queue.append(self)
        string=[]
        while(len(queue)!=0):
            print(queue[0].stri,end=" ")
            
            if queue[0].izq!=None:queue.append(queue[0].izq)
            if queue[0].der!=None:queue.append(queue[0].der)
            nulo=Nodo("\n",None,None)
            queue.pop(0)
        
    
        

def printTree(node, level=0):
        if node != None:
            printTree(node.izq, level + 1)
            print(' ' * 4 * level + '->', node.stri)
            printTree(node.der, level + 1)




def CYK(left, right, chain):
    
    cad=list(chain)
    mat= []
    #Inicializo una matriz 3d vacía con el tamaño de la cadena a evaluar
    for i in range(len(cad)):
        row=[]
        for j in range(len(cad)):
            row.append([])
        mat.append(row)
    
    for i in range(len(cad)):
        aux=cad[i] 
        
        if(aux in right): #Aquí checamos si se puede producir (ya que del lado derecho tenemos las producciones)
            siz=len(left[right.index(aux)])#Aquí nos dice cuantos productores hay para aux
            hijo= Nodo(aux,None,None) 
            for num in range(siz):
                padre=Nodo(left[right.index(aux)][num],hijo,None)#Es con el que se produce 
                mat[i][i].append(padre) #si es posible agregamos con qué se produce 
            
        else: 
            nulo=Nodo("0",None,None)
            mat[i][i].append(nulo)
    #ya que tenemos llenamos todos los de longitud 1 

    cont=0
    for aux in range(len(cad)-1,0,-1): 
        cont+=1
        i=0 #siempre se inicializa en la primer posición
        j=i+cont
        
        for aux1 in range(aux,0,-1): 
            for k in range(i,j):
                size1=len(mat[i][k])#Sacamos el tamaño de cada casilla ya que puede tener varios Nodos
                size2=len(mat[k+1][j])#De esta manera concatenamos cada Nodo en busca de alguna concatenación que sí se produzca
                for x in range(size1):
                    for y in range(size2):
                        conc=mat[i][k][x].stri+mat[k+1][j][y].stri
                        if(conc in right):
                            siz=len(left[right.index(conc)])#Aquí nos dice cuantos productores hay para conc
                            hijoIzq=mat[i][k][x]
                            hijoDer=mat[k+1][j][y]
                            for c in range(siz):
                                padre=Nodo(left[right.index(conc)][c],hijoIzq,hijoDer)#Es con el que se produce 
                                mat[i][j].append(padre) #si es posible agregamos con qué se produce     
            if(mat[i][j]==[]): #si está vacia agregamos el 0  
                nulo=Nodo("0",None,None)
                mat[i][j].append(nulo)
            
            
            i+=1
            j+=1

        
    auxiliar=len(mat[0][len(cad)-1])
    for i in range(auxiliar):
        if(mat[0][len(cad)-1][i].stri=="S"):
            print("Sí se acepta la cadena "+chain)
            print("El árbol de derivación es el siguiente:")
            printTree(mat[0][len(cad)-1][i])
            return 
    print("no se acepta la cadena ")


if __name__ == "__main__":
    #left=[["S","T"],["S","T"],["X"],["A"],["B"]]
    #right=["AB","XB","AT","a","b"]
    left=[]
    right=[]
    num=int(input("Ingrese el número de producciones que tiene la GLC: "))
    for i in range(num):
        aux=input("Ingrese la producción #"+str(i+1)+": ")
        right.append(aux)
        num1=int(input("Ingrese la cantidad de Generadores que generan "+aux+": "))
        left.append([]) 
        for j in range(num1):
            aux1=input("Ingrese el símbolo generador #"+str(j+1)+" que genera "+aux+": ")
            
            left[i].append(aux1)
    chain=input("Ingrese la cadena a evaluar ")
    CYK(left,right,chain)
    

    
    
