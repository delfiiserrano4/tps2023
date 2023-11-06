from lista import Lista
from random import randint


class Personajes:

    def __init__(self, nombre, anio_aparicion, casa, biografia)
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return '{self.nombre} - {self.anio_aparicion} - {self.casa} - {self.biografia}'   
    

lista_Personajes = Lista()

personajes = [
{'nombre': 'Linterna verde', 'anio_aparicion':'1940', 'casa': 'DC', 'biografia': 'Porta un anillo de poder y una batería en forma de linterna que otorga al portador la capacidad de crear manifestaciones de luz verde sólida con ellos.Alan Scott, fue el primer Linterna Verde,lleva generalmente un traje de color verde con partes negras o gris oscura y a veces blancas. Una curiosidad del uniforme es que el símbolo del pecho se alza unos centímetros por encima de la superficie del traje en un constructo de luz.' }
{'nombre': 'Wolverine', 'anio_aparicion': '1974', 'casa': 'Marvel', 'biografia': 'Es un mutante que posee sentidos afinados a los animales, capacidades físicas mejoradas, poderosa capacidad de regeneración conocida como un factor de curación, y tres garras retráctiles en cada mano. '}
{'nombre': 'Dr.Strange', 'anio_aparicion': '1963', 'casa': 'DC', 'biografia': 'Sirve como el Hechicero Supremo, el principal protector de la Tierra contra las amenazas mágicas y místicas.Posee la capa de levitacion'}
{'nombre': 'Iron Man', 'anio_aparicion': '1963', 'casa': 'Marvel', 'biografia': 'Anthony Edward "Tony" Stark es un multimillonario magnate empresarial y filántropo estadounidense, playboy e ingenioso científico, que sufrió una grave lesión en el pecho durante un secuestro en el Medio Oriente.Creo una armadura cuando sus captores intentaron forzarlo a construir un arma de destrucción masiva'}
{'nombre': 'Capitana Marvel', 'anio_aparicion': '1968', 'casa': 'Marvel', 'biografia': 'Carol apareció por primera vez como oficial de la Fuerza Aérea de los Estados Unidos y colega del superhéroe Kree llamado Mar-Vell ' }
{'nombre': 'Black Widow', 'anio_aparicion': '1964', 'casa': 'Marvel', 'biografia': 'Ella fue presentada como una espía rusa, antagonista del superhéroe Iron Man. Más tarde, desertó a los Estados Unidos y se convirtió en agente de la organización ficticia S.H.I.E.L.D., y miembro del equipo de superhéroes Los Vengadores.'}
{'nombre': 'Star Lord', 'anio_aparicion': '1976', 'casa': 'Marvel', 'biografia': 'Es hijo de la humana llamada Meredith Quill y del Spartoi Jason, y como adulto Peter Quill asume el manto de Star-Lord, un policía interplanetario.'}
{'nombre': 'Flash', 'anio_aparicion': '1940', 'casa': 'DC', 'biografia': 'Barry Allen es un científico asistente de la División de Ciencia Criminal y Forense del Departamento de Policía de Ciudad Central en 1956, conocido por ser lento y llegar siempre tarde a su trabajo, lo cual enojaba a su prometida Iris West. Una noche, un rayo cayó en su laboratorio lleno de químicos que bañaron a Allen, creando un accidente que le otorgaría una súper velocidad e increíbles reflejos . Con un traje rojo y el símbolo de un rayo su novia lo nombro "Flash"'}
{'nombre': 'Mujer Maravilla', 'anio_aparicion': '1941', 'casa': 'DC', 'biografia': 'Es una princesa guerrera de las Amazonas, en su tierra natal es conocida como la princesa Diana de Temiscira pero fuera de esta utiliza la identidad secreta de Diana Prince. Está dotada de una amplia gama de poderes superhumanos y habilidades de combate de batalla superiores. Posee armas tales como el Lazo de la Verdad, n par de brazaletes mágicos indestructibles y su tiara '}
{'nombre': 'Batman', 'anio_aparicion': '1939', 'casa': 'DC', 'biografia': 'La identidad secreta de Batman es Bruce Wayne, un multimillonario magnate empresarial y filántropo dueño de Empresas Wayne en Gotham City. Después de presenciar el asesinato de sus padres, el Dr. Thomas Wayne y Martha Wayne en un violento y fallido asalto cuando era niño, juró venganza contra los criminales, un juramento moderado por el sentido de la justicia. Bruce Wayne se entrena física e intelectualmente y crea un traje inspirado en los murciélagos para combatir el crimen, con sus gadgets de combate del batcinturón y sus vehículos.'}
]


for personaje in personajes
 lista_Personajes.insertar(Personajes(personaje['name'],personaje['anio de aparicion'],personaje['casa'],personaje['biografia']))
                                           


#!A
print('Personaje eliminado:')
personajeDelete = ['Linterna verde']
for elimiar in personajes:
    datos = lista_Personajes.eliminar(elimiar, 'personaje')
    if datos:
        print("--personaje {datos} eliminado de la lista")
print()


#!B
for i in range(lista.size()):
    if lista.get_element_by_index(i).nombre == 'Wolverine':
        print ('El anio de aparicion de Wolverine es: ', lista.get_element_by_index(i))

#!C 
edit = input('Cambiar casa Dr.Strange')
        if edit in Lista:
            newValue = input(f'Cambiar de DC a Marvel{edit}: ')
            findAndReplace(Lista,edit,newValue)
            print('Se ha cambiado exitosamente')

#!D
print('Personajes con traje o armadura')
lista_Personajes.barrido_traje_armadura()
print()

#!E
print('Personajes aparecidos antes de 1963 y sus casas: ')
if anio_aparicion < 1963 in lista_Personajes:
   if lista.get_element_by_index(i).nombre == ' ':
      lista.get_elemanto_by_index(i).casa == ' ':
        print ('Los superheroes aparecidos antes del 1963 son: ', lista.get_element_by_index(i)) 

#!F
for i in range(lista.size()):
    if lista.get_element_by_index(i).nombre == 'Capitana Marvel':
        print ('La casa a la que pertenece Capitana Marvel es: ', lista.get_element_by_index(i))
        if lista.get_element_by_index(i).nombre == 'Mujer Maravilla':
            print ('La casa a la que pertenece la Mujer Maravilla es: ', lista.get_element_by_index(i))


#!G
for i in range(lista.size()):
    if lista.get_element_by_index(i).nombre == 'Flash':
        print (' ', lista.get_element_by_index(i))
    for i in range(lista.size()):
    if lista.get_element_by_index(i).nombre == 'Stard Lord':
        print (' ', lista.get_element_by_index(i))