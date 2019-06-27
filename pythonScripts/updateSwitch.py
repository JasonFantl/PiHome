import mysql.connector
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

switchs = {'wire button': 11}
switchState = {'wire button': True}

for pin in switchs.values():
    GPIO.setup(pin,GPIO.IN)

def updateDB(inName, inValue):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1blownFuse",
    database="sensors")
    
    mycursor = mydb.cursor()
    
    sqlQuery = "UPDATE inputs SET value=" + str(inValue) + " WHERE name=\"" + str(inName) + "\""
    result = mycursor.execute(sqlQuery)
    mydb.commit()

    print(result, "sent:", sqlQuery)

while(True):
    
    for switch in switchs.keys():
        pin = switchs[switch]
        if(switchState[switch] == False and GPIO.input(pin) == GPIO.HIGH):
            updateDB(switch, 1)
            switchState = True
        elif(switchState[switch] == True and GPIO.input(pin) == GPIO.LOW):
            updateDB(switch, 0)
            switchState[switch] = False
        
    time.sleep(1)


GPIO.cleanup()
