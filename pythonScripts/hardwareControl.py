import mysql.connector
import RPi.GPIO as GPIO
import time

THIS_MICROCONTROLLER = "pi1"


GPIO.setmode(GPIO.BOARD)

sensors = {} # key=pin, item=value

def getDB():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1blownFuse",
    database="sensors")
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT microcontroller, pin, value, read_only FROM inputs")

    myresult = mycursor.fetchall()
    
    return myresult
 

def updateSensorList(inInfo):
   for x in inInfo:
        microcontroller = x[0]
        pin = x[1]
        value = x[2]
        readOnly = x[3]
        
        if microcontroller == THIS_MICROCONTROLLER and not readOnly:
            #Check if we already have this pin as an output, if not, update
            if not sensors.has_key(pin):
                print("Added new pin", pin)
                GPIO.setup(pin,GPIO.OUT)

            sensors[pin] = value
        
        
def updateSensors():
    for pin in sensors.keys():
        value = sensors[pin]
        GPIO.output(pin,value)
        
        
while(True):
    
    DBdata = getDB()
    updateSensorList(DBdata)
    updateSensors()

    time.sleep(1)


GPIO.cleanup()
