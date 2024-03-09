def contar_letras(frase):
    # Eliminar espacios en blanco y contar el número de letras
    cantidad_letras = sum(c.isalpha() for c in frase)
    return cantidad_letras

def obtener_frase_usuario():
    while True:
        frase = input("Ingresa una frase o palabra (solo letras): ")
        if frase.isalpha():  # Verificar que la frase contenga solo letras
            return frase
        else:
            print("Error: La frase debe contener solo letras. Intenta de nuevo.")

if __name__ == "__main__":
    # Solicitar al usuario que ingrese una frase
    frase = obtener_frase_usuario()

    # Contar el número de letras en la frase
    cantidad_letras = contar_letras(frase)

    # Mostrar el resultado en la consola
    print(f"La cantidad de letras en la frase es: {cantidad_letras}")