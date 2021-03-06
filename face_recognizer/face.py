#!/usr/bin/python

import cv2, os
import numpy as np
from PIL import Image

# library.
cascadePath = "haarcascade_frontalface.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

recognizer = cv2.createLBPHFaceRecognizer()

path = './myfaces'
inputpath='./f'


image_paths = [os.path.join(path, f) for f in os.listdir(path)]
#print image_paths

images = []

labels = []

for image_path in image_paths:
        # grayscale
        image_pil = Image.open(image_path).convert('L')
        
	# numpy array
        image = np.array(image_pil, 'uint8')
      
	n = int(os.path.split(image_path)[1].split(".")[0])
        
	# Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        
	for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(n)

            cv2.imshow("Adding !!!", image[y: y + h, x: x + w])
            cv2.waitKey(50)
 


cv2.destroyAllWindows()

# Perform the tranining
recognizer.train(images, np.array(labels))


image_paths = [os.path.join(inputpath, f) for f in os.listdir(inputpath)]
for image_path in image_paths:

    predict_image_pil = Image.open(image_path).convert('L')
    predict_image = np.array(predict_image_pil, 'uint8')

    faces = faceCascade.detectMultiScale(predict_image)
    name=(os.path.split(image_path)[1])

    for (x, y, w, h) in faces:
        n_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
	#print conf
        if (conf<50):
		print "True for %s" % name
#	else: print "false for %s" % name
        
        cv2.imshow("Authunticating Face", predict_image[y: y + h, x: x + w])
        cv2.waitKey(1000)
