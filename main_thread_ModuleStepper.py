import ModuleStepper
import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)

stepper1 = ModuleStepper.Stepper(20,21,16,12,7,8) # (pin_dir, pin_step, pin_sleep, pin_M0, pin_M1, pin_M2)
stepper2 = ModuleStepper.Stepper(9,11,10,22,27,17) # (pin_dir, pin_step, pin_sleep, pin_M0, pin_M1, pin_M2)
    
def Step(stepper,direction, rev, rps, microstep):
    stepper.step(direction, rev, rps, microstep) #dir, revs, rps, microstep

def Ramp(stepper,direction, rev, rpsmin, rpsmax, rate, microstep):
    stepper.ramp(direction, rev, rpsmin, rpsmax, rate, microstep) #dir, revs, rpsmin, rpsmax,rate(r.s-2), microstep
    

#Created the Threads for step
t1 = threading.Thread(target=Step, args=(stepper1, 1,50,5,16)) #stepper,dir, revs, rps, microstep
t2 = threading.Thread(target=Step, args=(stepper2, 0,50,5,16)) #stepper,dir, revs, rps, microstep

#Created the Threads for step
#t1 = threading.Thread(target=Ramp, args=(stepper1, 1,100,0.1,10,0.00001,4)) #stepper, dir, revs, rpsmin, rpsmax,rate(r.s-2), microstep
#t2 = threading.Thread(target=Ramp, args=(stepper2, 0,100,0.1,10,0.00001,4)) #stepper, dir, revs, rpsmin, rpsmax,rate(r.s-2), microstep


#Started the threads
t1.start()
t2.start()
 
#Joined the threads
t1.join()
t2.join()

#stepper1.rate_ramp() #dir, revs, rpsmin, rpsmax,rate(r.s-2), microstep


GPIO.cleanup()