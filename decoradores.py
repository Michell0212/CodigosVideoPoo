def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
    return funcion_modificada

@decorador
def saludo():
    print("Hola Dalto como andas")


saludo()