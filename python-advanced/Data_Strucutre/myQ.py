import threading 
import time
class myQ:
    def __init__(self):
        self.l=[]
        pass
    def enque(self):
        i=0
        while i<10:
            print("enque")
            self.l.append(i)
            i=i+1
            time.sleep(500)
    def deque(self):
        while int(len(self.l)) !=0:
            print("Deque")
            print(self.l.pop(0))
            time.sleep(500)
q=myQ()
t1=threading.Thread(target=q.enque)
t2=threading.Thread(target=q.deque)
t1.start()
t2.start()
t1.join()
t2.join()
while True:
    t1.run()
    t2.run()
