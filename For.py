"""
nombre=("Agustin","Martin","Gabriel","Susana")
for nom in nombre:
    print(nom)
"""
"""
ciudad="Rio Grande"
for caracter in ciudad:
    print(caracter) #"Rio grande"
   """ 
#1- Imprimir numeros del 1 al 10
'''
for num in range (1,11):
    print(num)
'''
#2- imprimir los elemento de una tupla que contenga frutas
'''    
Frutas=("Pera","palta","banana","Manzana")
for caracter in Frutas:
    print(caracter)
'''
#3-Sumar numeros de tupla
'''
numeros=1,2,3,4
Sumatoria= 0
for num in numeros:
    Sumatoria += num
print('EL resultado es:',Sumatoria)
'''
#4-imprimir los caracter de una cadena
'''
Nombre="Agustin"
for caracter in Nombre:
    print(caracter)
    
    '''
#5-imprimir numeros pare del 1 al 20
'''
for num in range(1,21):
    if num % 2==0:
        print(num)
        '''
#6-imprimir los primeros 10 numeros elvados al cuadrado
'''
for num in range(1,11):
    pow(num,2)
    print(pow(num,2))
    '''
#7-contar vocales en una cadena
'''
vocales="aeiou"
Nom="agustin"
contador=0
for caracter in Nom:
    if caracter in vocales:
        contador+=1
print('la cantidad de vocales es:',contador)'''
#8-multiplicacion de los primeros 5 resultado = 1
'''
resultado = 1
for num in range(1, 6):
    resultado *= num

print("El resultado de la multiplicación de los primeros 5 números es:", resultado)'''
#9-vamos a crear las tablas de multiplicar (la del 5)
'''
for num in range (1,11):
    print('5x',num,'=',num*5)'''
#10-contar la cantidad de elementos de una tupla
'''
edades = ('12','12','12','12','12')
sumatoria = 0
for cant in edades:
    sumatoria +=1
print('la cantidad de elementos es:',sumatoria)'''
#11-imprimir los numeros impares del 1 al 20
'''
for num in range (1,21):
    if num %2 !=0:
        print(num)'''
   

#12-Encontrar el numero mas grande de una tupla
'''Num=1,22,3,4,5
for num in Num:
    m = max(Num)
print(m)
    '''
#13-contar la cantidad de letras que hay en una palabra

'''Nom="agustin"
contador=0
for caracter in Nom:
        contador+=1
print('la cantidad de vocales es:',contador)'''
#14-Escribe un programa que calcule la suma de todos los numeros del 1 al 10 e imprimir resultado
'''resultado=0
for num in range (1,11):
    resultado += num
print("El resultado:", resultado)'''
#15-carga una tupla con 5 herramientas y luego imprimir

#16-escribe un programa que cuente y muestre la cant de vocales que hay en una palabra dada por el usuario
#17-imprimir numeros entre el 5 y el 20, saltando de tres en tres
#18-Escribe un programa que imprima un patron de asteriscos en forma de triangulo debe contener un numero
#c
#19-Contar cuantos numeros son mayores a cero
#20-Requerir al usuario que ingre un numero positivo e imprimir todos los numeros correlativos entre la ingresado
#por el usuario y uno menos del doble