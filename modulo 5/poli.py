from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self,mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoByEmail(Notificacao):
    def enviar(self) -> bool: 
        print('Notificação por Email - ',self.mensagem)
        return True
    
class NotificacaoByTel(Notificacao):
    def enviar(self) -> bool: 
        print('Notificação por telefone - ',self.mensagem)
        return False
    
n = NotificacaoByEmail('TESTE')
n.enviar()


def notificar(n : Notificacao) -> None:
    notificacao_enviada = n.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÂO enviada')
    
not_email = NotificacaoByEmail('testeando e-mail')
not_Tel = NotificacaoByTel('testeando Tel')

notificar(not_email)
notificar(not_Tel)