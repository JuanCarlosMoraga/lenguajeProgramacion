#import random

def jugar_adivinanza():
    # Generar un número aleatorio entre 0 y 100
    numero_secreto = 50 #random.randint(0, 100)

    intentos = 0
    adivinanza = None

    print("¡Bienvenido al juego del numero secreto!")

    while adivinanza != numero_secreto:
        try:
            adivinanza = int(input("Adivina el número (entre 0 y 100): "))
            if 0 <= adivinanza <= 100:
                intentos += 1

                if adivinanza < numero_secreto:
                    print("Demasiado bajo. Intenta de nuevo.")
                elif adivinanza > numero_secreto:
                    print("Demasiado alto. Intenta de nuevo.")
                else:
                    print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            else:
                print("Error: Ingresa un número dentro del rango estalecido del 0 al 100")
        except ValueError:
            print("Error: Ingresa un número entero válido.")

if __name__ == "__main__":
    jugar_adivinanza()