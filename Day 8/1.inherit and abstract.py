from abc import  abstractmethod
class Mail():
    @abstractmethod
    def disp(self):
        print("this is Mail class")
class email(Mail):
    def dis(self):
        print("this is email class")
        
class sms(Mail):
    def disp(self):
        print("this is sms class")
        
class Whatsapp(Mail):
    def disp(self):
        print("this is whatsapp class")
        
w=Whatsapp()
s=sms()
e=email()
w.disp()
s.disp()
e.disp()
e.dis()
