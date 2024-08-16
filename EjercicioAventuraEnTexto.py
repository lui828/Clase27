opciones ={
    "izquierda":"Te encontrastes con un dragón",
    "derecha":"Encontraste un tesoro",
    "adelante": "Caiste en un pozo"
}

eleccion = input("Estas en un cruze. ¿Quieres ir a la derecha, izquierda o adelante?: ")

if eleccion in opciones:
    print("Respuesta: ", opciones[eleccion])
else:
    print("Opción equivocada")
    
    