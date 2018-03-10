import connectArduino

arduino = None

try:
    # Thread(target = speech.run).start()
    # speech.run()
    arduino = connectArduino.connect()

    while True:
        # Capture frame-by-frame
        connectArduino.sendCommand(arduino, command)

    connectArduino.disconnect(arduino)

except Exception:
    traceback.print_exc()
    print("closing connection")
    if arduino:
        arduino_servo.disconnect(arduino)
