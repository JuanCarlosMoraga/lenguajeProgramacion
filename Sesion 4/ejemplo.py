class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
    
#Crear objeto persona

persona1 = Persona("Ulises", 38)
persona1.saludar()
