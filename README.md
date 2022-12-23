# MQTT-Based-Locking-System
This is an Arduino based locking system that comminicates with an already setup MQTT broker with the help of a Raspberry Pi.
The arduino system subscribes to the MQTT broker.

To setup:
- Upload FingerFinal.ino to arduino
- Connect raspberry pi to arudino via USB
- In Connection.py , make sure line 56 is '/dev/ttyACM1' or '/dev/ttyACM0' depending on the USB port arduino is connected to
- Run Connection.py

A mobile application was written to act as the main user interface for the system.
The mobile application publishes on the MQTT broker.

App repo: https://github.com/InterVam/Network-Secura
Through the application the user can:
- Create an account on the system
- Log user into the application
- Change locking system passcode
