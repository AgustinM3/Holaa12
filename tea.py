#Tupla
#Secuencia inmutable, lo que significa que no le podemos cambiar los valores
#tubla vacia
t =()
print(t)

#Tupla con un solo valor
t1 = (1,) #1=1,
print(t1)

#tupla con varios valores
t2 =(1,2,3,4) # t2 ? 1,2,3,4
print(t2)
'''
#funcion tuple()
saludo = 'hola mundo'
print(tuple(saludo))
'''
'''
#Funcion Len()
Tupla=12,45,67,12
print(len(Tupla))


tupla2=12,15,23
print(tupla2[1])
x= tupla2[2]
print(x)
'''
'''
t=14,35,23
print(t[1])
x=t[2]
print(x)
'''
'''
t=14,35,23
t[2]=18
print(t[2])
'''
NomAlu=input('ingrese Nombre Alumno:')
NomPro=input('ingrese Nombre Profesor:')
Pro=float(input('ingrese promedio CON DECIMALES:'))

datos =(NomAlu,NomPro,Pro)
print('est.', datos[0] , 'prof.',datos[1], round(Pro))





