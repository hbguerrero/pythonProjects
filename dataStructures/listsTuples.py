#################LISTAS####################

my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

print(my_lista)
print(type(my_lista))
print(my_lista[2])

print("my_lista size: ", len(my_lista))
print(my_lista[0:2])
print(my_lista[:2])

my_lista.append('Blanco')      
print(my_lista)

my_lista.insert(3, 'Negro')
print(my_lista)

extend_list = ['Marron','Gris']
my_lista.extend(extend_list)
print(my_lista)

print(my_lista.index('Azul'))

#Añadir y remover elementos de una lista
my_lista.remove('Marron')
print(my_lista)

my_lista.insert(8, 'Marron')
print(my_lista)

print(my_lista.pop()) 
size = len(my_lista)
print("size = ", size)

#Multiplicando elementos de la lista
my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)

#Ordenando alfabeticamente una lista de cadenas de caracteres
print("Sort:")
my_lista.sort()
print(my_lista)

#Ordenando listas numericas de menor a mayor
my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)


#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De mayor a menor: ", my_NumList)



################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
