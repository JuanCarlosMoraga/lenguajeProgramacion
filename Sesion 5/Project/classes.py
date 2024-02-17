class student:
    def __init__(self, id, name, major):
        self.id = id
        self.name = name
        self.major = major
    
    def __str__(self):
        return f"Nombre: {self.name}\nCarrera: {self.major}"
    
erving = student(1, "Erving Artola", "ISI")
print(erving)
#print(erving.__str__())