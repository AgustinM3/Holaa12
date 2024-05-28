#Ejercicios de practica - NECTORES
#Ejercicio 1: Escribe n programa que solicite al usuario
#dos numeros enteros y determine si ambos numeros son
#mayores a 10

#Ejercicio 2: Escribe un programa que solicite al usuario
#dos numeros enteros y determine si al menos uno de ellos
#es par

#Ejercicio 3: Escribe un programa que solicite al usuario
#un numero entero y determine si el numero NO esta dentro de
#1 y 100 (inclusive)


#Ejercicio 4: Escribe un programa que le solicite al usuario
#un numero entero y determine si el numero es multiplo de 3
#y multiplo de 5


#Ejercicio 5: Escribe un programa que solicite al usuario
#su nombre y determine si su nombre empieza con una vocal



#Ejercicio 6: Escribe un programa que solicite al usuario
#tres numeros enteros y determine si al menos uno de ellos
#es positivo



#Ejercicio 7: Escribe un programa que solicite la usuario
#dos numeros enteros y determine si la suma de ambos es par


#Ejercicio 8: Escribe un programa que solicite al usuario
#su edad y determine si tiene al menos 18 años y menos de
#70 , y por lo tanto, esta en el rango para poder conducir


#Ejercicio 9: Escribe un programa que solicite al usuario
#un año y determine si es bisiesto.
#dato: un año bisiesto si es dibisible por 4, pero no
#por 100, a menos que tambien sea divisible por 400


#Ejercicio 10: Escribe un programa que solicite al usuario
#una palabra y determine si la palabra comienza y termina
#con la misma letra.



#EJER 1:

'''
n1=int(input('ingrese n1:'))
n2=int(input('ingrese n2:'))
if n1 >= 10 and n2 >=10:
      print('Mayores')
else:
     print('Uno no es mayor o ambos:')
     
'''     
#EJER 2:
'''
num1=int(input('ingrese n1:'))
num2=int(input('ingrese n2:'))

if num1 % 2 == 0 or num2 % 2 == 0:
    print('Alguno es par:')
else:
    print('Impar')
 '''   
#EJER 3:
'''
n1=int(input('ingrese n1:'))

if not 1<=n1 <=100:
    print('No esta entre 1 - 100')

else:
    print('esta entre 1 - 100')
    
  '''  
    
#EJER 4:
'''
n1=int(input('ingrese n1:'))

if n1 % 3 == 0 or n1 % 5 == 0:
    print('es multiplo 3 o 5')
else:
    print('no es multiplo de 3 o 5')
    
    
#EJER 5:
    
Nombre=input('ingrese nombre:')
PrimeraL=Nombre[0]
if PrimeraL.upper() in 'AEIOU':
  print('Vocal')
else:
    print('No vocal')

'''
'''
#EJER 6:
n1=int(input('ingrese n1:'))
n2=int(input('ingrese n2:'))
n3=int(input('ingrese n3:'))

if n1 > 0 or n2 > 0 or n3 > 0:
    print('hay un numero positivo')
else:
    print('todos son negativos')
'''
'''
#EJER 7:
n1=int(input('ingrese n1:'))
n2=int(input('ingrese n2:'))
suma=n1+n2      
if suma % 2 == 0:
       print('Es par')
else:
       print('Es impar')
    
'''
'''
#EJER 8:
n1=int(input('ingrese edad:'))
if not n1 <=17 <=70:
       print('Apto para conducir')
else:
       print('No apto para conducir')
'''
#EJER 9:
'''
n1=int(input('ingrese Año:'))
if n1 % 4 == 0:
       print('Es un año bisiesto')
else:
       print('No es Año bisiesto')
'''      
#EJER 10:

PL=input('ingrese cualquier PALABRA:')
PrimerL=PL[0]
UltLetra=PL[-1]
if PrimerL.upper() == UltLetra.upper():
    print('Empieza y termina con la misma Letra')
else:
    print('No Termina con la misma letra') 


   