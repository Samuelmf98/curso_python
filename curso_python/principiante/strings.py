string = "Hola mundo,"
string_1 = "esta es la clase de strings"
print(string + " " + string_1) #Metemos espacio entre los strings. Tambien se puede agregar un espacio al final de la primera cadena.

string_salto_de_linea = "este es un string \n con un salto de linea" #Agrega un salto de linea
print(string_salto_de_linea)

string_con_tabulacion = "Este es un string \t con tabulacion" #Agrega una tabulacion
print(string_con_tabulacion)


string_con_escapado =  "\t Este es un string \n escapado"
print(string_con_escapado)

string_con_escapado_1 = "Este es otro string"  #De esta forma tabulamos los dos en dos lineas diferentes
string_con_escapado_2 = "también con escapado"
print("\t" + string_con_escapado_1 + "\t")
print("\t" +  string_con_escapado_2)


#Format

nombre = "Samuel"
edad = 25

print("Hola me llamo {} y tengo {} años".format(nombre,edad)) #Ejemplo1

print(f"Hola me llamo {nombre} y tengo {edad} años") #Ejemplo 2




language = "python"
a, b, c, d, e, f = language #asignamos letras a python (Tiene que coincidir en tamaño)
print(a)
print(e)


# División

language_slice = language[1:3] #Coge la palabra principal python
print(language_slice)

language_slice = language[1:] #ython
print(language_slice)

language_slice = language[-2]#o
print(language_slice)

language_slice = language[0:6:2] #pto porque primero coge el de la posicion 2 por ser menor numero que el 6
print(language_slice)

# Reverse

reversed_language = language[::-1] #nohtyp, es decir al reves
print(reversed_language)


print(language.capitalize()) #Python primera en masyuscula
print(language.upper()) #PYTHON todas en mayuscula
print(language.count("t")) #1
print(language.isnumeric()) #False
print("1".isnumeric()) #True
print(language.lower()) #python #todas en minuscula
print(language.lower().isupper()) #False si son todas en mayuscula
print(language.startswith("Py")) #False
print("Py" == "py")  # No es lo mismo "False"

