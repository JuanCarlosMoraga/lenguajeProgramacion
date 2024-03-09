# Elegir un número de dos dígitos
number = 52

# Separar los dígitos
digito1 = number // 10  # División entera para obtener el primer dígito
digito2 = number % 10   # Obtener el segundo dígito usando el residuo

# Sumar los dígitos individualmente
suma_digitos = digito1 + digito2

# Mostrar el resultado
print(f"El número es: {number}")
print(f"La suma de los dígitos es: {suma_digitos}")