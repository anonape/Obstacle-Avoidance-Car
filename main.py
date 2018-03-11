import connectArduino
import cv2
import Pyro4

arduino = None

try:
    # Thread(target = speech.run).start()
    # speech.run()
    arduino = connectArduino.connect()

    while True:

        key = cv.waitKey(1) & 0xFF
        #PYRO:obj_dbc143cf36bf43f186bf0f881f06e17e@localhost:61773
        uri = input("What is the Pyro URI of the greeting object?").strip()
        name = input("What is the name?")
        # Capture frame-by-frame
        connectArduino.sendCommand(arduino, key)

    connectArduino.disconnect(arduino)

except Exception:
    traceback.print_exc()
    print("closing connection")
    if arduino:
        arduino_servo.disconnect(arduino)
