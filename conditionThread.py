# code
  
# import modules
  
import time
from threading import *
import random
import pdb


class appointment:
    
    def patient(self):
        condition_object.acquire()
        print('patient john waiting for appointment')

        global val
        val = 2
        
        print(val)
        info = condition_object.wait()   # Thread is in waiting state
        pdb.set_trace()
        print('successfully got the appointment')
        condition_object.release()

    def doctor(self):
        condition_object.acquire()

        global val
        val = 3
        
        print('doctor jarry checking the time for appointment')
        time=0 
        time=random.randint(1,13)
        print('time checked')
        print('oppointed time is {} PM'.format(time))
        condition_object.notify()
        condition_object.release()


condition_object = Condition()
class_obj=appointment()

T1 = Thread(target=class_obj.patient)

T2 = Thread(target=class_obj.doctor)

T1.start()

T2.start()