'''def mensaje ():
    print('hola mundo')
mensaje ()
'''
'''def mensajeRetorno():
    return'mensaje de la funcion'

imprimir=mensajeRetorno()
print(imprimir)
'''

'''def nom_ape(nombre,apellido):
    nombre_completo= nombre +' '+apellido
    print(nombre_completo)
nom_ape('Agustin','Fuentes')'''



'''def suma(n1,n2):
    resultado=n1+n2
    print('El resultado de la suma es:',resultado)
suma(6,2)'''


#Ejercicio
#Crear una funcion que muestre por pantalla el nombre completo

def datos(nom,ape,edad):
    nomCompleto = nom+' '+ape
    print('su nombre completo es:',nomCompleto,'y tiene:',edad,'años')
    
#darles los valores
'''datos('Carlitos','perez',20)'''
#Pidiendo al usuario los datos
nombre = input('ingrese su nombre:')
apellido= input('ingrese su apellido:')
edad1=int(input('ingrese su edad:'))
datos(nombre,apellido,edad1)




