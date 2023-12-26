#Listas

# Definición

my_list = list() #Se puede definir una lista vacia con parentesis o con corchetes
my_other_list = []

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)

my_other_list = [35, 1.77, "Brais", "Moure"]
print(my_other_list)


# Acceso a elementos y búsqueda

print(my_other_list[0]) #35
print(my_other_list[1]) #1.77
print(my_other_list[-1]) #Moure
print(my_other_list[-4]) #35
print(my_list.count(30)) #Numero de veces que se repite el 30, 2 veces
#print(my_other_list[4]) #IndexError Se sale de rango
#print(my_other_list[-5]) #IndexError Se sale de rango

print(my_other_list.index("Brais")) #2

age, height, name, surname = my_other_list #Asignar valores a los elementos de la lista
print(name) #Brais

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age) #Lo mismo que el paso anterior pero hecho de otra forma

# Concatenación

print(my_list + my_other_list) #Concatena una despues de la otra


# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev") #Añade ese eleento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") #Añade el elemento en una posicion especifica
print(my_other_list)

my_other_list[1] = "Azul" #Actualiza el valor de la posicion 2
print(my_other_list)

my_other_list.remove("Azul") #Elimina el elemento 
print(my_other_list)

my_list.remove(30) #Elimina el primer elemento con ese valor, si hay mas solo elimina el primero
print(my_list)

print(my_list.pop()) #Elimina el ultimo valor y lo muestra por pantalla.
print(my_list) #Imprime la lista sin el valor eliminado antes

my_pop_element = my_list.pop(2) #Elimina el elemento de la posicion 2 y lo muestra por pantalla
print(my_pop_element)
print(my_list)

del my_list[2] #elimina la posicion 2
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear() #Vacia una lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #Imprime la lista al reves
print(my_new_list)

my_new_list.sort()  #Ordena la lista
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))



#Insertar: Append, insert

#Eliminar: remove, pop, del