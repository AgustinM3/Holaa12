#While
# Contar del 1 al 5
'''
Num = 1
while Num <= 5: # Mientras numero sea menor o igual
    print(Num)
    Num = Num + 1 # Numer +=1
    
#Ejercicio 2: Crear una variable, inicializarla en 1
#y mostrar hasta 10
    
Num = 1
while Num <=10:
   print(Num)
   Num = Num + 1
  ''' 
'''
T=input('Desea continuar con el programa sí o no?:')
 
while T != 'sí':
   T=input('Desea continuar con el programa sí o no?:')
     
'''
'''

Contraseña=input('ingrese contraseña:')
Contraseña2=input('ingrese Nueva contraseña:')

while Contraseña != Contraseña2:
    Contraseña=input('ingrese contraseña:')
'''
'''
SumNegativos = 0
SumPositivos = 0

numE = int(input('Ingrese un número: '))
while numE != 0:
    if numE > 0:
        SumPositivos += numE
        print('La sumatoria de los positivos es:', SumPositivos)
    else:
        SumNegativos += numE
        print('La sumatoria de los negativos es:', SumNegativos)
    numE = int(input('Ingrese un número: '))

print('Sumatoria total de los positivos:', SumPositivos)
print('Sumatoria total de los negativos:', SumNegativos)


'''


#Escriba un programa que simule una hucha.El Programa solicitara perimero una
#cantidad, que sera la cantidad de dinero que queremos ahorrar. A continuacion,
#el programa solicitara una y otra vez las cantidades que se iran ahorrando,
#hasta que el total ahorrado iguale o supere al objetivo . El progama no comprobara
#que las cantidades sean positivas


SumatoriaDinero= 0
objetivo= float(input('cual es tu objetivo para ahorrar?:'))
dineroIngresado= float(input('cuanto van a ingresar?:'))
while dineroIngresado != objetivo:
    SumatoriaDinero += dineroIngresado
    if sumatoriaDinero >= objetivo
       print(´cumpliste tu objetivo')
    
    print('total ahorrado hasta el momento es:',SumatoriaDinero)
    dineroIngresado=float(input('cuanto van a ingresar?:'))          
