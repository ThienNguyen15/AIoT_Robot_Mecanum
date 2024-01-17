from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import base64
import requests

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("C:\\Project HDL\\Traffic_Signs\\keras_model.h5", compile=False)

# Load the labels
class_names = open("C:\\Project HDL\\Traffic_Signs\\labels.txt", "r", encoding="utf-8").readlines()

def get_data():
    camera_url = 'Link camera + /capture'
    response = requests.get(camera_url)
    image = cv2.imdecode(np.frombuffer(response.content, dtype=np.uint8), -1)

    return image

def image_detector():

    # camera_url = 'Link camera + /capture'

    # response = requests.get(camera_url)
    # image = cv2.imdecode(np.frombuffer(response.content, dtype=np.uint8), -1)
    #
    # # Convert the image to base64
    # res, frame = cv2.imencode('.jpg', image)
    # image_data = base64.b64encode(frame).decode('utf-8')
    image = get_data()

    # Convert the image to base64
    res, frame = cv2.imencode('.jpg', image)
    image_data = base64.b64encode(frame).decode('utf-8')

    if len(image_data) > 102400:
        print("Image is too big!")
    else:
        print("Publish image:")
    print(len(image_data))

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    return int(class_name[0]), class_name[2:], image_data, str(np.round(confidence_score * 100))[:-2]
