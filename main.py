
# 6
class Message:
    def __init__(self, text):
        self.text = text

    def send(self):
        print(f"{self.text} Xabar yuborildi ")

    def delete(self):
        print(f" Xabar o‘chirildi")
x = Message("I hate going to school")
x.send()
x.delete()




# 7
class File:
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f"{self.name} file.txt ochildi ")

    def close(self):
        print(f" file.txt yopildi")
x = File("I hate going to school")
x.open()
x.close()



# 8
class DoorLock:
    def __init__(self, locked):
        self.locked = locked

    def lock(self):
        print(f"{self.locked} Qulflandi")

    def unlock(self):
        print(f" ochildi")
x = DoorLock("eshik")
x.lock()
x.unlock()




# 9
class Camera:
    def __init__(self, mode):
        self.mode = mode

    def capture(self):
        print(f"{self.mode}  ni Rasmi olindi")

    def switch_mode(self):
        print(f"Rejim o‘zgardi")
x = Camera("quyosh")
x.capture()
x.switch_mode()


# 10
class Email:
    def __init__(self, address):
        self.address = address

    def send(self):
        print(f"{self.address }  Email yuborildi")

    def receive(self):
        print(f"Email qabul qilindi")
x = Email ("Eqilindimail qabulvwuirdbu ")
x.send()
x.receive()
