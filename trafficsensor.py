#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

trigger = 19
echo    = 26
rot     = 0
gelb    = 1
gruen   = 2
f_rot   = 3
f_gruen = 4
taste   = 5
Ampel=[24,25,12,16,20,21]
GPIO.setmode(GPIO.BCM)
GPIO.setup(Ampel[rot], GPIO.OUT, initial=0)
GPIO.setup(Ampel[gelb], GPIO.OUT, initial=0)
GPIO.setup(Ampel[gruen], GPIO.OUT, initial=1)
GPIO.setup(Ampel[f_rot], GPIO.OUT, initial=1)
GPIO.setup(Ampel[f_gruen], GPIO.OUT, initial=0)
GPIO.setup(Ampel[taste], GPIO.IN)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
print ("Nähere Dich dem Sensor, um Fußgängerampel einzuschalten, Strg+C beendet das Programm")

def distanz_messen():

    GPIO.output(trigger, True)
    time.sleep(0.00001) 
    GPIO.output(trigger, False)

    start_zeit = time.time()
    while GPIO.input(echo) == 0:
        start_zeit = time.time()

    while GPIO.input(echo) == 1:
        stop_zeit = time.time()

    zeit_diff = stop_zeit - start_zeit
    entfernung = (zeit_diff * 34300) / 2
    return entfernung

try:
    while True:
        distanz = distanz_messen()
        print(f"Gemessene Entfernung: {distanz:.1f} cm")
        if distanz <= 5:
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            GPIO.output(Ampel[gelb],1)
            time.sleep(2)
            GPIO.output(Ampel[gelb],0)
            GPIO.output(Ampel[rot],1)
            time.sleep(2)
            GPIO.output(Ampel[f_rot],0)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(10)
            GPIO.output(Ampel[f_gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],0)
            GPIO.output(Ampel[f_rot],1)
            time.sleep(2)
            GPIO.output(Ampel[gelb],2)
            time.sleep(1)
            GPIO.output(Ampel[rot],0)
            GPIO.output(Ampel[gelb],0)
            GPIO.output(Ampel[gruen],1)
            time.sleep(3)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Messung beendet")
    GPIO.cleanup()


try:
    while True:
        if GPIO.input(Ampel[taste])==1:
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[gruen],0)
            GPIO.output(Ampel[gelb],1)
            time.sleep(2)
            GPIO.output(Ampel[gelb],0)
            GPIO.output(Ampel[rot],1)
            time.sleep(2)
            GPIO.output(Ampel[f_rot],0)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(10)
            GPIO.output(Ampel[f_gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],0)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],1)
            time.sleep(0.3)
            GPIO.output(Ampel[f_gruen],0)
            GPIO.output(Ampel[f_rot],1)
            time.sleep(2)
            GPIO.output(Ampel[gelb],2)
            time.sleep(1)
            GPIO.output(Ampel[rot],0)
            GPIO.output(Ampel[gelb],0)
            GPIO.output(Ampel[gruen],1)
            time.sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()