import serial
import time
import paho.mqtt.client as mqtt


passCode=""
msg=""
IntializedFlag=0
firstFlag=0
        
                
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # subscribe, which need to put into on_connect
    # if reconnect after losing the connection with the broker, it will continue to subscribe to the raspberry/topic topic
    client.subscribe(mqtt_topic)


# the callback function, it will be triggered when receiving messages
def on_message(client, userdata, msge):
    global passCode
    global firstFlag
    global IntializedFlag
    temp= f"{msge.payload}"
    passCode=temp[2:-1]
    print("Bate5a")
    firstFlag=1
   
    if(IntializedFlag==1):
        print(passCode)
        passCode=passCode+'.'
        b=bytes(passCode,'utf-8')
        ser.write(b)
        if ser.in_waiting > 0:
            msg=ser.readline().decode('utf-8').rstrip()
            while(msg!="ACK"):
                    ser.write(b)
                    if ser.in_waiting > 0:
                        msg=ser.readline().decode('utf-8').rstrip()

    

#MQTT Connection settings
mqtt_username = "DeadSlayer"
mqtt_password = "Depression22"
mqtt_topic = "pass"
mqtt_broker_ip = "intervam.giize.com"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally, it will send the will message to other clients
client.username_pw_set(mqtt_username,mqtt_password )
# create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
client.connect(mqtt_broker_ip, 1883, 60)


def intialPass():
     global passCode
     global firstFlag
     global IntializedFlag
     
     if(passCode!=""):
        passCode=passCode+'.'
        b=bytes(passCode,'utf-8')
        ser.write(b)
        print(passCode)
        IntializedFlag=1


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()


while True:
     msg=""
     if ser.in_waiting > 0:
         msg=ser.readline().decode('utf-8').rstrip()
         if(msg=="Verify Code" and firstFlag==1):
             intialPass()
             
     time.sleep(1)
     client.loop()
     
    

      
