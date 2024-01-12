class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return "Woof!"

# Creando un objeto de la clase Perro
mi_perro = Perro("Fido", 3)
print(mi_perro.ladrar())  # Imprime: Woof!
