import RPi.GPIO as GPIO
import time

trigger = 19
echo = 26
led_red = 25
buzzer = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

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

def piepsen(frequenz):
    interval = 1 / frequenz
    GPIO.output(led_red, GPIO.HIGH)
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(interval / 2)
    GPIO.output(led_red, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)
    time.sleep(interval / 2)

try:
    letzte_messung = time.time()
    frequenz = 0
    GPIO.output(led_red, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)
    while True:

        if time.time() - letzte_messung > 0.1:
            distanz = distanz_messen()
            print(f"Gemessene Entfernung: {distanz:.1f} cm")
            letzte_messung = time.time()

            if distanz <= 4:
                frequenz = 7
            elif distanz <= 6:
                frequenz = 3
            elif distanz <= 8:
                frequenz = 2
            else:
                frequenz = 0

        if frequenz > 0:
            piepsen(frequenz)

except KeyboardInterrupt:
    print("Messung beendet")
    GPIO.cleanup()
