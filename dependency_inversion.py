from abc import ABC,abstractmethod

class IMessage(ABC):
    @abstractmethod
    def send(self, message , receiver):
        pass


class EmailService(IMessage):
    def send(self, message, receiver):
        print(f'Sending email {message} to {receiver}')


class SMSService(IMessage):
    def send(self, message,receiver):
        print(f'sending sms {message} to {receiver}')

class NotificationService:

    def __init__(self, service:IMessage):
        self._service = service


    def send_notification(self, message, receiver):
        self._service.send(message, receiver)


email_service = EmailService()
sms_service = SMSService()
notification_service = NotificationService(sms_service)


notification_service.send_notification('Bom dia brasil', 'Samarco')