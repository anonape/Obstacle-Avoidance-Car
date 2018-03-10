import connectArduino

arduino = None

try:
    # Thread(target = speech.run).start()
    # speech.run()
    arduino = connectArduino.connect()

    while True:
        # Capture frame-by-frame
        arduino_servo.rotate(arduino, newSum)

    arduino_servo.disconnect(arduino)

except Exception:
    traceback.print_exc()
    print("closing connection")
    if arduino:
        arduino_servo.disconnect(arduino)
