#An object means that a structure has both state and behavior
#behavior relates to the object's ability to perform some action
#State (or attibutes) pertains to the information about an object

#Classes are commonly described as blueprints for an object

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return "Woof!"

# Creando un objeto de la clase Perro
mi_perro = Perro("Fido", 3)
print(mi_perro.ladrar())  # Imprime: Woof!


#Another example 

Player player1 = new Player(agility = 54, speed = 88, fitness = 90); 

Player player2 = new Player(agility = 90, speed = 64, fitness = 83);

player1.set_fitness(80) 

