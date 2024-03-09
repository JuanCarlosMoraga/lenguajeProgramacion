def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10  # Obtener el último dígito y sumarlo
        numero //= 10  # Eliminar el último dígito
    return suma

if __name__ == "__main__":
    # Pedir al usuario que ingrese un número entero
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero >= 0:
            # Calcular la suma de los dígitos y mostrar el resultado
            resultado = suma_digitos(numero)
            print(f"La suma de los dígitos de {numero} es: {resultado}")
        else:
            print("Error: Ingrese un número entero no negativo.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")