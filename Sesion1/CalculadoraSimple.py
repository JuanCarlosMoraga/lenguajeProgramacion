def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."

def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Ingrese un número válido.")

def seleccionar_operacion():
    print("Elige la operacion que deseas realizar, digitando el numero que indica cada operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        try:
            opcion = int(input("Seleccione una operación (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Error: Ingrese una opción válida (1-4).")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

# Pedir al usuario dos números
print("Buenos dias esta es una calculadora simple, el cual permite realizar suma, resta, multiplicacion y division entre dos numeros.")
numero1 = pedir_numero("Ingrese el primer número: ")
numero2 = pedir_numero("Ingrese el segundo número: ")

# Permitir al usuario seleccionar una operación
opcion = seleccionar_operacion()

# Realizar la operación seleccionada y mostrar el resultado
if opcion == 1:
    resultado = suma(numero1, numero2)
    print("Resultado:", resultado)
elif opcion == 2:
    resultado = resta(numero1, numero2)
    print("Resultado:", resultado)
elif opcion == 3:
    resultado = multiplicacion(numero1, numero2)
    print("Resultado:", resultado)
elif opcion == 4:
    resultado = division(numero1, numero2)
    print("Resultado:", resultado)