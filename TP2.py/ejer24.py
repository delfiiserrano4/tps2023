from pila import Pila
from random import randint

pila1 = Pila()
pila_invertida = Pila()
pila_2 = Pila()


class Traje():
    personaje, pelicula, estado = None, None, None

dic = {'traje': 'Mark1', 'pelicula': 'dasdsa', 'estado': 'asdads'}

dic['traje']


trajes = ['Mark LXXXV', 'Mark II', 'Mark IV', 'Mark V', 'Mark X', 'Mark XLIV']
peliculas = ['iron man I', 'iron man II','iron man III', 'Avengers1', 'Spider-Man: Homecoming', 'Capitan America: Civil War']
estado = ['Dañado', 'Impecable', 'Destruido']

from random import choice

for i in range(len(trajes)):
    dato = Traje()
    dato.traje = trajes[i]
    dato.pelicula = peliculas[i]
    dato.estado = choice(estado)
    dic = {'traje': trajes[i], 'pelicula': peliculas[i], 'estado': choice(estado)}
    print(dato.traje, dato.pelicula, dato.estado)
    pila1.apilar(dato)

print()
pelicula = input('ingrese la pelicula en la que se uso el traje Mark LXXXV ')
insertar = True
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    # !A
    if(dato.traje == 'Mark XLIV'):
        print('el traje Mark XLIV fue usado en la pelicula', dato.pelicula)
    # !B
    if(dato.estado == 'Dañado'):
        print(f'el modelo {dato.traje} resulto dañado')
    
    # !F
    if(dato.pelicula in ['Spider-Man: Homecoming', 'Capitan America: Civil War']):
        print(f'el modelo {dato.traje} fue utilizado en la pelicula {dato.pelicula}')
    # !E
    if(dato.traje == 'Mark LXXXV' and dato.pelicula == pelicula):
        insertar = False
    if(dato.estado != 'Destruido'):
        pila_2.apilar(dato)

while(not pila_2.pila_vacia()):
    pila1.apilar(pila_2.desapilar())

if(insertar):
    dato = Traje()
    dato.traje = 'Mark LXXXV'
    dato.pelicula = pelicula
    dato.estado = choice(estado)
    pila1.apilar(dato)

print()
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    print(dato.traje, dato.pelicula, dato.estado)
