opciones = {
    "izquierda": "Te encontraste con un dragón",
    "derecha": "Encontraste un tesoro",
    "adelante": "Caíste en un pozo"
}

eleccion = input("Estás en un cruce. ¿Quieres ir a la derecha, izquierda o adelante?: ")

eleccion_normalizada = eleccion.strip().lower()

if eleccion_normalizada in opciones:
    print("Respuesta: ", opciones[eleccion_normalizada])
else:
    print("Opción equivocada")