import mysql.connector
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LEDs = {'red LED': 7, 'yellow LED': 13, 'white LED': 15}

for pin in LEDs.values():
    GPIO.setup(pin,GPIO.OUT)


def getDB():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1blownFuse",
    database="sensors")
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT name, value, sensor FROM inputs")

    myresult = mycursor.fetchall()

    for x in myresult:
        name = x[0]
        value = x[1]
        sensor = x[2]
        
while(True):

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1blownFuse",
    database="sensors")
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT name, value, sensor FROM inputs")

    myresult = mycursor.fetchall()

    for x in myresult:
        name = x[0]
        value = x[1]
        sensor = x[2]
        if(sensor == 'LED'):
            if(LEDs.has_key(name)):
                pin = LEDs[name]
                if(int(value) == 0):
                    GPIO.output(pin,False)
                else:
                    GPIO.output(pin,True)

    time.sleep(1)


GPIO.cleanup()