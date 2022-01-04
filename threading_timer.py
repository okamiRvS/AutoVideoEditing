from threading import Timer
import time
import pdb

# https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            
            asd = list(self.args)
            asd[0] += 1
            self.args = tuple(asd)

            self.function(*self.args, **self.kwargs)

def dummyfn(count, msg="foo"):
    print(f"{msg} {count}")

bpm = 129.20
bps = bpm/60
delay_in_sec = 1/bps

#timer = RepeatTimer(1, dummyfn) # if no arguments
count = 0
timer = RepeatTimer(delay_in_sec, dummyfn, args=(count, "bar",))
timer.start()
time.sleep(50)
timer.cancel()