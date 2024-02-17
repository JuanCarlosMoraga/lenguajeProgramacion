def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
#Ejemplo de uso
nume = int(input("Digite un # entero: "))
numero = 5
resultado = factorial(numero)
print (f"El factorail de{numero} es: {resultado}")

def fibonacci(n):
    if n <= 1:
        return
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    #Ejemplo de Uso
    numero_terminos = 10
    print("Serie de Fibonacci:")
    for i in range(numero_terminos):
        print(fibonacci(i))

#Listas
lista = [1, 2, 3, "Manzana", 15.6, True]
print(lista)

#imprimir el primer elemento de la lista
print(lista[0])
#tamaño de la lista
tam = len(lista)
print(f" el tamo es [tam]")
#imprimir el ultimo valor
print(lista[tam-1])

#Imprimir los primeros 3 elementos
print(lista[0:3])

#imprimir los elementos del 4 al 6
print(lista[3:7])

#agragar un elemento  a la lista
list.append("Juan")
print(lista)

#Imprimir los ultimos elementos de la lista
final = len(lista)
inicio = final - 3
print(lista[inicio: final + 1])

#Eliminar manzana
lista.remove("Manzana")
lista.remove("Juan")

#ordenar lista
print(list.sort())