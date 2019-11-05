from keras.models import model_from_json
from pathlib import Path
from keras.preprocessing import image
import numpy as np
from keras.applications import vgg16
import os
import time
import uuid
from PIL import Image, ImageChops
import socket


def resizer(src, dest):
    im = Image.open(src)
    im2 = im.resize((224, 224), Image.BICUBIC)
    im2.save(dest, "png")
    print(dest)

def assescnc():
    image_path = "/home/pi/Desktop/cnc.png"

    os.system("raspistill -sa 55 -q 90 -sh 100 -ISO 50 -t 1000 -o " + image_path )

    resizer(image_path, image_path)

    class_label_names = [
        "card",
        "not_card"
    ]

    # Load the json file that contains the model's structure
    f = Path("model_structure_cnc.json")
    model_structure = f.read_text()

    # Recreate the Keras model object from the json data
    model = model_from_json(model_structure)

    # Re-load the model's trained weights
    model.load_weights("model_weights_cnc.h5")

    # Load an image file to test, resizing it to 64x64 pixels (as required by this model)
    img = image.load_img(image_path, target_size=(224, 224))
    #img = image.load_img("green.png", target_size=(224, 224))
    # Convert the image to a numpy array
    image_array = image.img_to_array(img)

    # Add a forth dimension to the image (since Keras expects a bunch of images, not a single image)
    images = np.expand_dims(image_array, axis=0)

    # Normalize the data
    images = vgg16.preprocess_input(images)

    # Use the pre-trained neural network to extract features from our test image (the same way we did to train the model)
    feature_extraction_model = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    features = feature_extraction_model.predict(images)

    # Given the extracted features, make a final prediction using our own model
    results = model.predict(features)

    # Since we are only testing one image with possible class, we only need to check the first result's first element
    single_result = results[0]
    
    # We will get a likelihood score for all 10 possible classes. Find out which class had the highest score.
    most_likely_class_index = int(np.argmax(single_result))
    class_likelihood = single_result[most_likely_class_index]


    # Get the name of the most likely class
    class_label = class_label_names[most_likely_class_index]
    print(class_label)
    return class_label

assescnc()
# Setting Up the Server Settings for Raspberry Pi
localIP     = "172.28.210.59"
localPort   = 22222
bufferSize  = 1024

#Defining Attributes
msgFromServer       = "This is sent from the server"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

# Listen for incoming datagrams
def readyToReceive():
    print("UDP server up and listening")
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)    
        print(clientMsg)

        if b"READY" in message:
            break;

        print(clientIP)
    return bytesAddressPair;

while(True):
    print("in ready to receive")
    bytesAddr = readyToReceive();
    address = bytesAddr[1]

    print("out of ready to receive")
    print (" Taking Picture")
    cnc_string = assescnc()
    print ("Took picture iwth cnc :" + cnc_string)
    print(cnc_string)
    print ("Sending protocl :")
    bytesToSend = str.encode(cnc_string)
    UDPServerSocket.sendto(bytesToSend, address)
    print (" out of protocol")
