from threading import Timer, Condition
import queue
import time
import pdb

# https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            
            # get control of the thread
            condition_object.acquire()

            # edit queue increasing his value
            self.args[0].put(self.args[0].get() + 1)

            # release the lock
            condition_object.release()

            self.function(*self.args, **self.kwargs)

def dummyfn(count, msg="foo"):
    condition_object.acquire()
    counter = que.get(False)
    print(f"{msg} {counter}")
    que.put(counter)
    condition_object.release()

bpm = 129.20
bps = bpm/60
delay_in_sec = 1/bps

# create lock object
condition_object = Condition()

# create Queue to share counter variable
que = queue.Queue()

# initialize queue, with the counter to zero, otherwise we'll receive a none object
# IT'S REALLY IMPORTANTE THE FACT THAT EACH TIME YOU 
# GET OBJ FROM QUE, THE OBJ WILL BE REMOVED FROM QUEUE
que.put(0)

#timer = RepeatTimer(1, dummyfn) # if no arguments
timer = RepeatTimer(delay_in_sec, dummyfn, args=(que, "bar",))
timer.start()
time.sleep(50)
timer.cancel()