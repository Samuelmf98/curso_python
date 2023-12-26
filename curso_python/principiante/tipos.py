#Para consultar el tipo de dato que tenemos

print(type("Soy un dato str"))  # Tipo 'str'

print(type(5))  # Tipo 'int'

print(type(1.5))  # Tipo 'float'

print(type(3 + 1j))  # Tipo 'complex'

print(type(True))  # Tipo 'bool'

print(type(print("Mi cadena de texto")))  # Tipo 'NoneType' #Sale esto porque hemos metido un print con parentesis etc etc



# ¿Forzamos el tipo? 
address: str = "Mi dirección"
tipo=type(address)
print("El tipo de dato de address es:{} ".format(tipo))
address = True
address = 5
address = 1.2
print(type(address))
tipo=type(address)
print("El tipo de dato de address es:{} ".format(tipo)) #Aqui volvemos a consultar el tipo de dato y nos devuelve el ultimo que se le ha asignado: float (1.2)
