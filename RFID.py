from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

def lese_rfid():
    try:
        print("Bitte die RFID-Karte vor den Leser halten...")
        id, text = reader.read()
        print(f"ID: {id}")
        print(f"Text: {text}")
    except KeyboardInterrupt:
        print("Lesen abgebrochen.")
    finally:
        GPIO.cleanup()

def schreibe_rfid():
    try:
        text = input("Daten zum Schreiben eingeben: ")
        print("Bitte die RFID-Karte vor den Leser halten...")
        reader.write(text)
        print("Daten geschrieben!")
    except KeyboardInterrupt:
        print("Schreiben abgebrochen.")
    finally:
        GPIO.cleanup()

try:
    print("Wähle eine Option:")
    print("1. Lesen")
    print("2. Schreiben")
    choice = input("Eingabe (1/2): ")

    if choice == "1":
        lese_rfid()
    elif choice == "2":
        schreibe_rfid()
    else:
        print("Ungültige Auswahl.")
finally:
    GPIO.cleanup()