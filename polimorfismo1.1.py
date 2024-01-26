class Animal():
    def sonido(self):
        pass
    
class Gato ():
    def sonido(self):
        return "Miau Miau"
    
class Perro ():
    def sonido(self):
        return "Guau Guau"
    
    def hacer_sonido(animal):
        print(animal.sonido())


gato = Gato()
perro = Perro()


print(perro.sonido())

    
    
