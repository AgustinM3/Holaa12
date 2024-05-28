#EJecicio 2:
#Crear y accederr a los elementos de una tupla
#al tupla tiene que contener los numeros del 1
#al 5, imprimir el primer valor y el ultimo
'''

Numero = 1,2,3,4,5

print('Num',Numero[0],'UltiNum',Numero[-1])
      
'''

#Ejercicio 3: Desempaquetar una tupla
#crear una tupla con tres elementos
#desempaquetar la tupla en tres variables e imprimir
'''
MisDatos=("Agustin","Fuentes",22)
Nombre,apellido,edad = MisDatos
print(Nombre)
print(apellido)
print(edad)
'''

#Ejercicio 4: Crear dos tuplas con los elementos
#que quieas , concatenalas en una nueva tupla
#repite la nueva tupla dos veces y almacenala
#en una nueva tupla
'''
Años=(2024,2025,202)
Meses=('Octubre','Noviembre','Septiembre')
Tupla=Años+Meses
Tupla2=Tupla * 2
print(Tupla2)
'''
#Ejercicio 5: Crear una tupla ccon los numeros del 1 al 10
#e imprimir una sub-tupla que contenga del tercer
#al sexto elemento
''' 
T = ("Play","Tele","Celu","Piano","Compu")
SubT= T [0:4]
print(SubT)
'''

#Ejercicio 6:
#Crea una tupla con los numeros del 1 al 15 e
#Imprimir una sub-tupla que contenga los numeros
#pares

'''
T = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

SubT= T [1:15:2]

print(SubT)
'''


#Ejercicio 7:
#Hacer que la tupla que se creo antes comience
#desde al 15 y termine en 1



T = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

SubT = T [::-1]

print(SubT)



#Ejercicio 8:
# Crear una variable con tu nombre y darlo vuelta

Nombre= "Agustin"
NomR= Nombre [::-1]
print(NomR)



#Ejercicio 9


#Exprecion booleana : es verdadera o falsa