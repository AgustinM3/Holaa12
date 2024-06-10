#Projecto 1: Calculadora
#Crear un programa en py que realice operaciones matematicas (suma,resta,multiplicacion,division y modulo) utilizando
#funciones. Cada funcion debe recibir dos numeros como parametro y devolver el resultado de la operacion correspondiente.
#PD: Los numeros los debe introducir el usuario

#Funciones
#Entradas
#Salidas

def suma(n1,n2):
    resultado=n1+n2
    print('El resultado de la suma es:',resultado)



def resta(n1,n2):
    resultado=n1-n2
    print('El resultado de la suma es:',resultado)


def Multiplicacion(n1,n2):
    resultado=n1*n2
    print('El resultado de la suma es:',resultado)


def Division(n1,n2):
    resultado=n1/n2
    print('El resultado de la suma es:',resultado)

n1=int(input('ingrese el primer numero:'))
n2=int(input('ingrese el primer numero:'))

suma(n1,n2)
resta(n1,n2)
Multiplicacion(n1,n2)
Division(n1,n2) 