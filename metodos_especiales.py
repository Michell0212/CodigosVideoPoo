class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    
    def __repr__(self) -> str:
        return f'Persona("{self.nombre}",edad={self.edad})'
    
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
michell = Persona("Michell", 21)
will = Persona("Will", 32)

resultado = michell+ will
print(resultado)