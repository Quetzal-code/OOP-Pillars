class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    def hablar(self):  # Método común a todas las subclases
        pass

    def get_nombre(self):  # Getter para el nombre
        return self.__nombre

class Perro(Animal):
    def hablar(self):  # Sobrescritura del método hablar
        return "Woof!"

class Gato(Animal):
    def hablar(self):
        return "Meow!"

# Creación de objetos y demostración de polimorfismo
mi_perro = Perro("Fido")
mi_gato = Gato("Whiskers")

animales = [mi_perro, mi_gato]
for animal in animales:
    print(f"{animal.get_nombre()} dice {animal.hablar()}")
