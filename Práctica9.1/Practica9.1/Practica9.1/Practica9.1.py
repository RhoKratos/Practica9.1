import os

def encabezado():
    print("PRACTICA 9\nIntroducción a Python I\n\tEjercicio 1:\n")

def LeerNumero(varl, lista):
   lista=[3, 5, 9, 12, 13, 98, 53]

def ImprimirList(lista):
    print ("Los números:")
    print (lista)

def EvaluarNum(varl, lista, pares, impares):
    for it in range (varl):
        if lista[it]%2 == 0:
            pares.append(lista[it])
        else:
            impares.append(lista[it])
        

    print(len(pares),"Numeros pares:")
    for it in range (len(pares)):
	    print ("\t",(it+1),". -",pares[it])

    print(len(impares),"Numeros impares:")
    for it in range (len(impares)):
	    print ("\t",(it+1),". -",impares[it])

it = 0
lista = []
pares = []
impares = []

encabezado()

try:
    varl = int (input( "Cuantos numeros deseas evaluar?\n"))
except:
    print("Introduce un número.")

LeerNumero(varl, lista)

ImprimirList(lista)

EvaluarNum(varl, lista, pares, impares)