from cola import Cola

c=Cola()


class notificaciones():
    twitter, facebook, instagram  = None, None, None



dic = {'notificacion: ', 'hora: ', 'aplicacion que la emite:', 'mensaje: '}
dic=['notificacion']

aplicacion_que_la_emite=['Twitter', 'Instagram', 'Facebook', ]
hora=['10:30', '11:45', '15:00', ]
mensaje=[]


for i in range(len(notificaciones)):
    dato = notificaciones()
    dato.aplicaion_que_la_emite = aplicacion_que_la_emite[i]
    dato.mensaje = mensaje[i]
    dato.hora = hora[i]
    dic = {'notificacion: ', 'hora: ', 'aplicacion_que_la_emite: ', 'mensaje: '}




#!A escribir una función que elimine de la cola todas las notificaciones de Facebook;
