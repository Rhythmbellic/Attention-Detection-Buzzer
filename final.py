from keras.models import load_model
import cv2
import numpy as np
import serial
import time

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Serial communication setup
arduino_port = 'COM9'  # Change this to the correct port for your Arduino
ser = serial.Serial(arduino_port, 9600, timeout=1)
time.sleep(2)  # Allow some time for the Arduino to initialize

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the web camera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the model's input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predict the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Send corresponding command to Arduino based on prediction
    if "class 1" in class_name.lower():
        ser.write(b'1')  # Command to turn on LED
        print("LED ON")
    elif "class 2" in class_name.lower():
        ser.write(b'2')  # Command to turn on Buzzer
        print("Buzzer ON")
    else:
        ser.write(b'0')  # Command to turn off both
        print("LED and Buzzer OFF")

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

# Close the serial connection
ser.close()

# Release the camera
camera.release()
cv2.destroyAllWindows()
