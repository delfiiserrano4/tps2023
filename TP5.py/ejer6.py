from arbol import Arbol
from lista import Lista

                            
arbol_nombre = nodoArbol()
arbol_ranking = nodoArbol()
arbol_especie = nodoArbol()
arbol_color = nodoArbol()
lista = Lista()
busco = busqueda() 
 
lista = [['Leila Organa', 'human','11/08/133','blue', 'Jedi Knight', 'luke skywalker'],
         ['Lezra bridger', 'human','2/05/101', 'blue',  'Jedi Master','kanan jarrus'],
         ['anakin skywalker/darth vader', 'human','22/01/10', 'blue','Jedi Master', 'bobi-wan kenobi'],
         ['rey skywalker', 'human', '32/11/98', 'green','Padawan', 'yaddle'],
         ['oppo rancisis', 'thisspiasian', '2/05/101', 'green', 'Jedi Master', 'yaddle'],
         ['ahsoka tano', 'togruta', '22/55/800', 'yellow','Padawan','anakin skywalker'],
         ['asajj ventress', 'dathomirian','4/09/234', 'yellow', 'Jedi Knight',  'ky narec'],
         ['ki-adi-mundi', 'cerean','46/76/651', 'purple',  'Jedi Knight', '-']]


for nombre, especie, nacimiento, color_sable, ranking, maestro in lista:
    datos = {'Nombre': nombre, 'Especie': especie, 'Año de nacimiento': nacimiento, 'Color del sable de luz': color_sable, 'Ranking': ranking, 'Maestro': maestro}
    print(datos)


#!A
def insertar_nodo(arbol_ranking, ranking, datos)
def insertar_nodo(arbol_especie, especie, datos)
def insertar_nodo(arbol_color, color_sable, datos)

#B 
def arbol_inorden(arbol_nombre)
print('----------Inorden Nombre----------')
def arbol_inorden(arbol_ranking)
print('----------Inorden Ranking----------')
def arbol_inorden(arbol_especie)
print('----------Inorden Especie----------')

#C
def por_nivel(arbol_especie)
print('----------Barrido por nivel especie----------')
print()
def por_nivel(arbol_ranking)
print('----------Barrido por nivel especie----------')


#D
print('----------Informacion de Luke Skywalker----------')
buscado = busqueda(arbol_nombre, 'Ahsoka Tano')
print('Datos: ', buscado['datos'])


#E    
print('----------Informacion de Jedis Master----------')
jedis = inorden_JediMaster(arbol_ranking)
print()

#F
print('----------Sable de color green----------')
for color = postorden_ColorSable(arbol_color)
if color:
    lista.inserrtar(arbol_color['dato'])
    lista.barrido()

print()

#H
print('----------Especies Togruta y Cerean----------')
especies = inorden_especies(arbol_especie)
print()

#I
print('----------Empieza con la letra "L"----------')
for letra = inorden_empieza_con(arbol_nombre, 'L')
if letra:
    lista.insertar(arbol_nombre['dato'])
    lista.barrrido()