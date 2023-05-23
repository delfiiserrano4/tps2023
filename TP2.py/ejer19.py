from pila import Pila
from random import randint

pila1 = Pila()
pila_invertida = Pila()
pila_2 = Pila()



class Pelicula():
    estreno, pelicula, estudio_cinematografico = None, None, None

dic = {'pelicula': 'Avengesrs', 'pelicula': 'dasdsa', 'estado': 'asdads'}

dic['pelicula']


estreno = ['2014', '2016', '2018']
peliculas = ['Capitan America: Civil War', 'Doctor Strange: Hechicero Supremo','Batman', 'Avengers1', 'Spider-Man: Homecoming']
estudio_cinematografico = ['Marvel', 'DC Comics']

from random import choice

for i in range(len(peliculas)):
    dato = Pelicula()
    dato.peliculas = peliculas[i]
    dato.estreno = estreno[i]
    dato.estudio_cinematografico = choice(estudio_cinematografico)
    dic = {'estreno': estreno[i], 'pelicula': peliculas[i], 'estudio cinematografico': choice(estudio_cinematografico)}
    print(dato.traje, dato.pelicula, dato.estudio_cinematografico)
    pila1.apilar(dato)

print()
pelicula = input('ingrese una pelicula de Marvel o DC que le guste')
insertar = True
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    # !A
    if(dato.estreno == 'Guardianes de la Galaxia'):
        print('La pelicula Guardianes de la Galaxia se estreno en 2014', dato.pelicula)
    # !B
    if(dato.estado == 'Estrenadas'):
        print(f'Las peliculas estrnadas en 2018 fueron {dato.estreno} y pertenecen a {dato.estudio_cinematografico} ')
    # !C
    if(dato.pelicula in ['Doctor Strange: Hechicero Supremo', 'Capitan America: Civil War']):
        print(f'Las peliculas de marvel estrenadas en 2016 fueron {dato.estreno} ')
    