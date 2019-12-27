import sys
import cv2
import argparse
import numpy as np
import pandas as pd
from utils import *

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", help = "Input image.", type = str)

arguments = parser.parse_args()

# Check if input image exists
try:
    f = open(arguments.data)
except IOError:
    sys.exit("File or directory not found.")

# Load image
img = cv2.imread(arguments.data)
figsize = (6, 6)

# Pattern detection through morphological filtering
patterns, objects = pattern_detection(img, figsize)

# Feature extraction of each pattern
model = build_model()
feature_vectors = feature_extraction(model, objects, patterns)

# Pairwise comparison between feature vectors
cosine_similarity = pairwise_matrix(feature_vectors)
matrix = pd.DataFrame(cosine_similarity)

# Anomaly is the pattern with smallest sum of cosine similarities
anomaly = matrix.sum().idxmin()

# Get bounding box coordinates
x_min, y_min, width, height = patterns[anomaly][0], patterns[anomaly][1], patterns[anomaly][2], patterns[anomaly][3]
# Draw bounding box
img = cv2.rectangle(img, (x_min, y_min),(x_min + width, y_min + height), (255, 0, 0), 2)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Plot anomaly detection
plt.figure(figsize = figsize)
plt.imshow(img)
plt.show()

# Save results
outfilename = 'results/' + arguments.data.split('/')[1]
cv2.imwrite(outfilename, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))