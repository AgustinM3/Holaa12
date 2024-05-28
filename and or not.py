'''
#conectores logicos
#and
sueldo = 110000
antiguedad =11
if sueldo < 15000 and antiguedad >=10:
   print('verdadero')
else:
    print('falso')
# or
opcion = int(input('ingrese opcion:'))
if opcion == 1 or opcion == 3 or opcion ==5:
    print('verdadero')
else:
    print('falso')
'''
#not
edad = 22
if edad > 18:
    print('se consede el permiso')
else:
    print('no se consede el permiso')



n1=int(input('ingrese n1:'))
n2=int(input('ingrese n2:'))
n3=int(input('ingrese n3:'))
if n1 >= 0 and n2 >= 0 or n3 >= 0:
      print('todas son correctas')
else:
      print('Alguno es incorrecto: Negativo') 
