import abc

class Notificador(metaclass=abc.ABCMeta):
    def __init__(self, usuario, mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje


    def notificar(self):
        pass

class NotificadorEmail(Notificador):
    def notificar(self):
        print(F"enviado mensaje por Mail a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(F"enviado mensaje por SMS a {self.usuario.sms}")