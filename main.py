class Dog:
    especie = "Mamifero"
    numero_ojos = 2
    def __str__(self): #Metodo magico que se utiliza para visualizar la clase cuando se la defina
        return f"Yo soy un perro de raza {self.raza}, y de color {self.color}"
    def __iter__(self): #Metodo magico para convertir la clase en un iterable
        for ra in self.raza:
            yield ra


    def __len__(self): #Metodo magico definido para que se pueda usar la funcion len
        return len(self.raza)

    def __init__(self, raza: str, color:str): #__INIT__ es el metodo magico que construye
        self.raza = raza
        self.color = color
    def caminar(self):
        if self.raza == "doberman":
            return "Camino mucho"
        return "Camino poco"

    def ladrar(self):
        if self.ladrad == "Caniche":
            return "Ladrar bajo"
        return "Ladrar fuerte"

perro1 = Dog(raza= "doberman", color= "negro")
print(perro1)
print(perro1.raza)
print(perro1.caminar())
print(len(perro1))
for val in perro1: #Gracias al metodo magico inter, puedo hacer un for basico para iterar la clase
    print(val)
print("Hola")