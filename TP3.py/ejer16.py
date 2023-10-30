
from heap import HeapMin
from heap import HeapMax

heap = HeapMax()
h = HeapMax()

#A
heap.agregar('DocumentoEmpleado1', 1)
heap.agregar('DocumentoEmpleado2', 1)
heap.agregar('DocumentoEmpleado3', 1)

#B
print('Primer elemeno de la cola', heap.vector[0])

#C
heap.agregar('DocumentoStaff1', 2)
heap.agregar('DocumentoStaff2', 2)

#D
heap.agregar('DocumentoGerente1', 3)

#e
print('Primer y segundo elemento de la cola: ', heap.vector[0],'y', heap.vector[1])

#F
heap.agregar('DocumentoEmpleado4', 1)
heap.agregar('DocumentoEmpleado5', 1)
heap.agregar('DocumentoGerente2', 3)

#G
print('Toda la cola de impresion: ')
print(heap.vector)