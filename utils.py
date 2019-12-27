import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

import torch
import torchvision.models as models
from torch.autograd import Variable
import torchvision.transforms as transforms

def plot_image(image, figsize):

    """ Display an image """

    fig = plt.figure(figsize = figsize)
    plt.imshow(image, cmap = 'gray')
    plt.title(''), plt.xticks([]), plt.yticks([])
    plt.show()

def pattern_detection(img, figsize):
    
    """ Performs object segmentation by morphological filtering """

    # BGR to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      
    img_backup = img.copy()

    # Get image size
    height, width, _ = np.array(img).shape

    # Erosion morphological filter
    kernel = np.ones((3,3), np.uint8)
    erosion = cv2.erode(imgGray, kernel, iterations = 2)
    th = cv2.threshold(erosion, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

    # Image binarization  
    th = erosion.mean()
    imBin = erosion > th
       
    # Finding contours
    ret, thresh = cv2.threshold(erosion, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Compute contour areas for noise filtering
    areas = [cv2.contourArea(cnt) for cnt in contours]

    patterns, objects = [], []
    
    # Drawing bounding boxes around the contours
    for cnt in contours:
        # Filtering large and small bounding boxes
        if (cv2.contourArea(cnt) > 50 and cv2.contourArea(cnt) < np.max(areas)):
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(cnt)
            patterns.append([x, y, w, h])
            objects.append(cv2.cvtColor(img_backup[y:(y + h), x:(x+w)], cv2.COLOR_BGR2RGB))
            # Draw bounding box
            img_backup = cv2.rectangle(img_backup, (x, y),(x+w, y+h),(255, 0, 0), 1)

    return patterns, objects

def image_loader(image):
    
    """ Load image and returns pytorch tensor """

    imsize = 256
    loader = transforms.Compose([transforms.Resize(imsize), transforms.ToTensor()])

    image = Image.fromarray(image)
    image = loader(image).float()
    image = Variable(image, requires_grad = True)
    image = image.unsqueeze(0)
    # .cuda() assumes that you are using GPU
    return image

def build_model():

    """ Build feature extractor based on ResNet-34 """

    # If True, returns a model pre-trained on ImageNet
    convnet = models.resnet34(pretrained = True)
    convnet = list(convnet.children())[:-2]
    convnet = torch.nn.Sequential(*convnet, torch.nn.AdaptiveAvgPool2d(output_size = (4, 4)))
    
    return convnet

def feature_extraction(model, objects, patterns):

    """ Feature extraction from all detected patterns """

    feature_vectors = []

    for i in range(len(patterns)):

        x_min, y_min, width, height = patterns[i][0], patterns[i][1], patterns[i][2], patterns[i][3]
        image = image_loader(objects[i])
        # Forward pass in each pattern
        features = model.forward(image)
        features = features.flatten().detach().numpy()
        feature_vectors.append(features)

    return feature_vectors

def pairwise_matrix(feature_vectors):

    """ Compute cosine similarity between feature vectors """

    cosine_similarity = np.ones((len(feature_vectors[0]), len(feature_vectors[0])))

    for i in range(len(feature_vectors)-1):
        for j in range(len(feature_vectors)-1):
            cosine_similarity[i,j] = np.dot(feature_vectors[i], feature_vectors[j]) / (np.linalg.norm(feature_vectors[i]) * np.linalg.norm(feature_vectors[j]))

    return cosine_similarity