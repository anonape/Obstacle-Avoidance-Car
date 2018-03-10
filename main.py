import connectArduino

arduino = None

try:
    # Thread(target = speech.run).start()
    # speech.run()
    arduino = connectArduino.connect()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Classifier attributes
        bodies = bodyCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        count += 1

        if len(bodies) > 0:
            (x,y,w,h) = sorted(bodies, key=lambda x: x[2], reverse=True)[0]
            averages.append(rotateDegrees(x, w))
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if count > 10:
            if len(averages) > 0:
                newSum = sum(averages)
                arduino_servo.rotate(arduino, newSum)
                averages.pop(0)

        # Draw a rectangle around the bodies
        #for (x, y, w, h) in bodies:
        #    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Display the resulting frame
        cv2.imshow("GoPro OpenCV", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    arduino_servo.disconnect(arduino)

except Exception:
    traceback.print_exc()
    print("closing connection")
    if arduino:
        arduino_servo.disconnect(arduino)
