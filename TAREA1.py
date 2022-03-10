import random


print("Hola bienvenidos al proceso de asignar RAM")

a=random.randrange(20)+1
a=10

print("Se han creado ",a," procesos")

listaNew=[]
ListaReady=[]
ListaWait=[]
ListaCPU=[]

for i in range(a):
    b=random.randrange(10)+1
    listaNew.append(b)

for n in listaNew:
    print(n)

RAM=20
Disp=RAM
X=listaNew[0]

Limite=False
Terminar=False
#while Terminar==False:

#Pasar de New a Ready
while Limite==False:
    Disp=Disp-1
    X=X-1
    print("Espacio disponible en RAM",Disp)
    print("Cantidad restante en la operación ",X)
    if(Disp==0):
        Limite=True
        Y=listaNew[0]-X
        Disp=Disp+Y
        print()
        print("La RAM no tiene suficiente espacio para esta operación, pasan a esperar en lo que se libera la Ram")
    if(X==0):
        X=listaNew[1]
        print("")
        ListaReady.append(listaNew[0])
        print("Cambio de operación, nueva cantidad ",X)
        listaNew.pop(0)
    print()

print(Disp)
print("Operaciones en Ready")
print("")
i=0
for n in ListaReady:
    i=i+1
    print("Operación ",i," cantidad de Ram ",n)






#Ejecución CPU
print("")
print("Ejecución en CPU")

for m in ListaReady:

    print("")
    print("Operaciones: ",m)

    if m>3:
        for n in range(3):
            Disp=Disp+1
        print("")
        print("Nueva cant disponible ",Disp)
        Salida=random.randrange(2)
        print("Salida ",Salida)
        if Salida==1:
            ListaWait.append(m-3)
        else:
            for i in range(len(ListaReady)):
                if ListaReady[i]==m:
                    ListaReady[i]=m-3
    elif m<=3:
        for n in range(m):
            print("Operaración ",n," finalizada")
            m=m-1
            Disp=Disp+1

print("")
print("Operaciones en Ready")
print("")
i=0
for n in ListaReady:
    i=i+1
    print("Operación ",i," cantidad de Ram ",n)

#Waiting
print("")
print("Operaciones en Waiting")
print("")
i=0
for n in ListaWait:
    i=i+1
    print("Operación ",i," cantidad de Ram ",n)


print()
print("Cantidad de procesos en New",len(listaNew))

if(len(listaNew)==0):
    if(len(ListaReady)==0):
        Terminar=True