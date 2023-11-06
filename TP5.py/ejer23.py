from arbol import 
from lista import Lista

arbol = nodoArbol()
lista_derrotados = Lista()
heroesdioses = nodoArbol()
derrotados = nodoArbol()

lista = [['Ceto', '-'], 
         ['Cerda de Cromion', 'Teseo'],
         ['Tifon', 'Zeus'], 
         ['Heracles', 'Ortro'],
         ['Equidna', 'Argos Panoptes'], 
         ['Toro de Creta', 'Teseo'],
         ['Dino', '-'], 
         ['Jabali de Calidon','Atlanta'],
         ['Pefredo', '-'], 
         ['Carcinos', '-'],
         ['Enio', '-'], 
         ['Heracles','Gerion'],
         ['Escila', '-'], 
         ['Cloto', '-'],
         ['Caribdis', '-'], 
         ['Laquesis', '-'],
         ['Euriale','-'], 
         ['Atropos', '-'],
         ['Esteno', '-'],
         ['Minotaurod de Creta', 'Teseo'],
         ['Medusa','Perseo'], 
         ['Harpias', '-'],
         ['Heracles', 'Ladon'],
         ['Argos Panoptes', 'Hermes'],
         ['Qimera', 'Belerofonte'], 
         ['Talos', 'Medea'],
         ['Heracles', 'Hidra de Lerna'], 
         ['Sirenas', '-'],
         ['Heracles', 'Leon de Nemea'], 
         ['Piton', 'Apolo'],
         ['Esfinge', 'Edipo'], 
         ['Cierva de Cerinea', '-'],
         ['Dragon de Colquida', '-'], 
         ['Basilisco', '-'],
         ['Cerbero', '-'], 
         ['Jabali de Erimanto', '-'],
         ['Aves del Estínfalo', '-']
]

NuevoCampo = {}


    

#!A
print('----------Barrido inorden----------')
def inorden(arbol)
print()

#!B
for criatura, derrotado in lista:
    descripcion = input(f'Ingrese una breve descripcion de {criatura}: ')

#C
print('----------Informacion de Talos----------')
for busq = busqueda(arbol, 'Talos')
if busq:
    print('Informacion: ', busq['datos'])
print(' ')

#D determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
   

#E
print('----------Criaturas que derroto Heracles----------')
def inorden_heracles(arbol)

#F
print('----------Criaturas no derrotadas----------')
def inorden_no_derrotadas(arbol)


#!G
for criatura, derrotado in lista:
    captura = input(f'Ingrese quien campturo al personaje {criatura}: ')
    datos = {'nombre de la criatura': criatura, 'derroto a': derrotado,'descripcion': descripcion, 'capturo': captura}
    print(datos)
    def insertar_nodo(arbol, criatura, derrotado)  
     print()

#!H modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;

for cerbero = busqueda(arbol, 'Aves del Estinfalo')
if cerbero:
    modificacion = modificar(arbol, campo = captura) 
    if modificacion:   
        cerbero_modificacion = 'Heracles'
        def insertar_nodo(arbol, cerbero_modificacion)
print(datos)

for toro_de_creta = buqueda(arbol, 'Toro de creta')
if toro_de_creta:
    modificacion = modificar(arbol, campo = captura) 
    if modificacion:   
        toro_de_creta_modificacion = 'Heracles'
        def insertar_nodo(arbol, toro_de_creta_modificacion)
print(datos)

for cierva_cerinea = busqueda(arbol, 'Cierva Cerinea')
if cierva_cerinea:
    modificacion = modificar(arbol, campo = captura) 
    if modificacion:   
        cierva_cerinea_modificacion = 'Heracles'
        def insertar_nodo(arbol, cierva_cerinea_modificacion)
print(datos)

for jabali_de_erimato = busqueda(arbol, 'Jabali de Erimato')
if jabali_de_erimato:
    modificacion = modificar(arbol, campo = captura) 
    if modificacion:   
        jabali_de_erimato_modificacion = 'Heracles'
        def insertar_nodo(arbol, cerbero_modificacion)
print(datos)

#I, #i. se debe permitir búsquedas por coincidencia;


#J
def eliminar_basilico = eliminar_nodo(arbol, 'Basilisco')
print('Personaje eliminado: ', eliminar_basilico)
print()

def eliminar_sirenas = eliminar_nodo(arbol, 'Sirenas')
print('Personaje eliminado: ', eliminar_sirenas)
print('-------------------------------------')
    
    
#K
aves = busqueda(arbol, 'Aves del Estinfalo')
if aves:
   def eliminar_nodo(arbol, '-')
    aves_modificado = input('Ingrese el nombre correcto')
    insertar_nodo(arbol, aves_modificado)
    
#L
ladon = busqueda(arbol, 'Heracles') #ingreso por el campo criatura
if ladon: 
   eliminar_nodo(arbol, 'Ladon') #elimino el nodo donde se almacena Ladon
     ladon_modificado = input('Ingrese el nombre correcto: ')
   insertar_nodo(arbol, ladon_modificado)
inorden(arbol)


#M
print('----------Listado por nivel----------')
por_nivel(arbol) 
print('-------------------------------------')

#!N muestre las criaturas capturadas por Heracles. 

    