
class Notification:
    def send(self,message):
        print("Sending notification",message)

class EmailNotification(Notification):
    def send(self,message):
        print("Sending email",message)

class SMSNotification(Notification):
    def send(self,message):
         print("Sending sms",message)

class PushNotification(Notification):
    def send(self,message):
        print("Sending push notification",message)
n1=EmailNotification()
n1.send("Order Confirmed")

n2=SMSNotification()
n2.send("OTP is 4536")

n3=PushNotification()
n3.send("You have a new message")