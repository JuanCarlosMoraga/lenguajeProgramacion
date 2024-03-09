def convertir_moneda(cantidad, moneda_origen, moneda_destino):
    # Definir tasas de conversión (ejemplo)
    tasas_conversion = {
        ('USD', 'EUR'): 0.91,
        ('USD', 'NIO'): 36.25,
        ('CRC', 'NIO'): 0.0688,
        ('EUR', 'USD'): 1.08925,
        ('NIO', 'USD'): 0.02704,
        ('NIO', 'CRC'): 13.5544
    }

    if moneda_origen == moneda_destino:
        return cantidad  # No hay conversión necesaria para la misma moneda

    if (moneda_origen, moneda_destino) in tasas_conversion:
        tasa = tasas_conversion[(moneda_origen, moneda_destino)]
        monto_convertido = cantidad * tasa
        return monto_convertido
    else:
        return "Error: Tasas de conversión no disponibles para esta combinación de monedas."

if __name__ == "__main__":
    # Pedir al usuario la cantidad de dinero y la moneda de origen
    cantidad = float(input("Ingrese la cantidad de dinero: "))
    moneda_origen = input("Ingrese la moneda de origen (USD, EUR, NIO, CRC): ").upper()

    # Permitir al usuario seleccionar la moneda de destino
    moneda_destino = input("Ingrese la moneda de destino (USD, EUR, NIO, CRC): ").upper()

    # Realizar la conversión y mostrar el resultado
    resultado = convertir_moneda(cantidad, moneda_origen, moneda_destino)
    if isinstance(resultado, (float, float)):
        print(f"{cantidad} {moneda_origen} equivale a {resultado:.4f} {moneda_destino}")
    else:
        print(resultado)