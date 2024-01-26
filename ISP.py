from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Humano(Trabajador, Comedor):
    def comer(self):
        print("El humano está comiendo")

    def trabajar(self):
        print("El humano está trabajando")

    def dormir(self):
        print("El humano está durmiendo")

class Robot(Trabajador):
    @abstractmethod
    def comer(self):
        pass

    def trabajar(self):
        print("El robot está trabajando")
humano = Humano()
humano.comer()
humano.trabajar()
humano.dormir()

robot = Robot()
robot.trabajar()