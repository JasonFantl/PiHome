import mysql.connector
import RPi.GPIO as GPIO
import time


#Important constants
THIS_MICROCONTROLLER = "pi1"
#mySQL credentials
hostname="localhost"
username="root"
password="1blownFuse"
databaseName="sensors"

GPIO.setmode(GPIO.BOARD)

sensors = {} #key=pin, item=last reading

def getDB():
    mydb = mysql.connector.connect(
    host=hostname,
    user=username,
    passwd=password,
    database=databaseName)
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT microcontroller, pin, read_only FROM inputs")
    myresult = mycursor.fetchall()
    
    return myresult
 
def updateDB(pin, value):
    mydb = mysql.connector.connect(
    host=hostname,
    user=username,
    passwd=password,
    database=databaseName)
    
    mycursor = mydb.cursor()
    
    sqlQuery = "UPDATE inputs SET value=" + str(value) + " WHERE pin=\"" + str(pin) + "\""
    result = mycursor.execute(sqlQuery)
    mydb.commit()

    print(result, "sent:", sqlQuery)
    #on each update, also check if there are any new sensors to read
    updateSensorList(getDB())
    
def updateSensorList(inInfo):
   for x in inInfo:
        microcontroller = x[0]
        pin = x[1]
        readOnly = x[2]
        
        if microcontroller == THIS_MICROCONTROLLER and readOnly:
            #Check if we already have this pin, if not, update
            if not sensors.has_key(pin):
                print("Added new pin", pin)
                GPIO.setup(pin,GPIO.IN)
                sensors[pin] = True

        
        
def checkSensorChange():
    for pin in sensors.keys():
        lastRead = sensors[pin]
        if(lastRead == False and GPIO.input(pin) == GPIO.HIGH):
            updateDB(pin, 1)
            sensors[pin] = True
        elif(lastRead == True and GPIO.input(pin) == GPIO.LOW):
            updateDB(pin, 0)
            sensors[pin] = False
        
        

updateSensorList(getDB())

while(True):
    
    checkSensorChange()

    time.sleep(1)


GPIO.cleanup()

