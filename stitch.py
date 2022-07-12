from prama import panorama
import cv2
import argparse
import os

filename = []
images = []

# Create the parser
parser = argparse.ArgumentParser(description = 'Feature Description, Matching and stitching ')

# input and output folder path
parser.add_argument('--image',
                    action = 'store',
                    type = str, 
                    required = True, 
                    help = 'image folder path')

parser.add_argument('--output',
                    action = 'store',
                    type = str, 
                    required = True, 
                    help = 'output folder path')

# Execute the parse_args() method
arg = parser.parse_args()

for root,dirs,files in os.walk(arg.image):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"): 
            image_path = os.path.join(root, file)
            filename.append(image_path)

for img in filename:
    images.append(cv2.imread(img)) 

no_of_images = len(images)

concat = panorama()

if no_of_images==2:
    (result, matched_points) = concat.image_stitch([images[0], images[1]], match_status=True)
else:
    (result, matched_points) = concat.image_stitch([images[no_of_images-2], images[no_of_images-1]], match_status=True)
    for i in range(no_of_images - 2):
        (result, matched_points) = concat.image_stitch([images[no_of_images-i-3],result], match_status=True)

# saving the results

cv2.imwrite(os.path.join(arg.output, 'stitch.jpeg'), result)
cv2.imwrite(os.path.join(arg.output, 'matched_points.jpeg'), matched_points)
