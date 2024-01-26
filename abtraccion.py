class Auto():
    def __init__(self) -> None:
        self._estado ="Apagado"

    def encender(self):
        self.__estado = "Encendido"
        print("El auto esta encendido")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir()


