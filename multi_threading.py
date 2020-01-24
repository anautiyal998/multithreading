###Concept of multithreading in Python!!!!!
from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello!!!")
            sleep(1)

class Hii(Thread):

    def run(self):
        for i in range(5):
            print("Hii!!")
            sleep(1)

a1=Hello()
a2=Hii()
a1.start()
sleep(0.2)
a2.start()
a1.join()
a2.join()
print("Bye!!!")
print("Have a nice day!!!")
