class MiClase:
    def __init__(self) -> None:
        self.__satributo_privado = "Valor"

    def _hablar(self):
        print("hola, como estas")

objeto = MiClase()
print(objeto._hablar())



