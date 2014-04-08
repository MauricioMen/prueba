# -*- coding: iso-8859-15
import sys 

def getLista(nombre):
	lista=[]
	archivo=open(nombre,'r')
	linea=archivo.readline()
	while linea!="":
		lista.append(int(linea))
		linea=archivo.readline()
	return lista


def burbuja(lista):
    for i in range(len(lista)-1):
	for j in range(len(lista)-i-1):
            if(lista[j+1]<lista[j]):
		aux = lista[j+1]
		lista[j+1] = lista[j]
		lista[j] = aux
    return lista

if(len(sys.argv)==1):
	print 'archivo no recibido'
else:
		burbuja(getLista(sys.argv[1]))


