
from cola import Cola

cola1 = Cola()


class personajesdeMarvel():
    nombre, nombre_de_heroe, genero  = None, None, None


nombre = ['Tonny Stark','Carol Danvers','Scott Lang','Steven Rogers','Clint Barton','Natasha Romanoff','Wanda Maximoff'] 
nombre_de_heroe= ['Iron Man','Capitana Marvel','ANT Man','Capitan America','OJO de Alcon','Black Widow','Bruja Escarlata']
genero= ['masculino','femenino','masculino', 'masculino','masculino','femenino','femenino']


for i in range(len(nombre)):
    dato = personajesdeMarvel()
    dato.nombre = nombre[i]
    dato.nombre_de_heroe = nombre_de_heroe[i]
    dato.genero = genero[i]
    #!dic = {'nombre': nombre [i], 'nombre de heroe': nombre_de_heroe[i], 'genero': genero[i]}
    print(dato.nombre, dato.nombre_de_heroe, dato.genero)
    cola1.arribo(dato)
print(cola1.tamanio())

#!isertar= True
while (not cola1.cola_vacia()):
    dato = cola1.atencion()
    #!A
    if(dato.nombre_de_heroe =='Capitana Marvel'):
        print('El nombre de la capitana marvel es:', dato.nombre)
    
    #!B
    if(dato.genero== 'femenino'):
        print('los personajes del genero femenino son:',dato.nombre)
        #else:
        # print('No hay personajes femeninos')
    #!C
    if(dato.genero== 'masculino'):
        print('los personajes del genero masculino son:',dato.nombre) 
        #else:
        # print('No hay personajes masculinos')
    #!D
    if(dato.nombre== 'Scott Lang'):
        print('El nombre de heroe de Scott Lang es:', dato.nombre_de_heroe)
        #else: 
        # print('Scott Lang no fue cargado')
    #!E
    if((dato.nombre[0] == 'S') or (dato.nombre_de_heroe[0] == 'S')):
        print ('los datos de los personajes con nombres y nombres de heroe con S son:')
        print(dato.nombre)
        print(dato.nombre_de_heroe)
        print(dato.genero)
    else: 
        print('No hay personajes o nobres con S')
    #!F
    if((dato.nombre == 'Carol Danvers')):
        print ('Si el personaje se encuentra en la cola y su nombre de super heroe es:', dato.nombre_de_heroe)
    else:
      print('el nombre de Carol Danvers no esta en la cola')

        
    