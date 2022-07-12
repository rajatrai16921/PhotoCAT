# PhotoCAT
## Panoramic-Image-Stitching
I have implemented the Panoramic image stitching using invariant features from scratch. Implemented the David Lowe paper on "Image stitching using Invariant features".

NOTE: You can experiment with any images (your own choice). I have experimented with many images. You can check result below. You can find many images in "Image_Data" folder.

CREATE DATA:
- You can create multiple images like S1.jpg, S2.jpg, S3.jpg, S4.jpg and S5.jpg (shown below) .Make sure there will be some overlapping parts between two consecutive created images in a sequence. then only algorithm will find and match features and create panorama image of all images which you have provided. 
- OR you can directly feed multiple images from camera in a sequence with some overlapping parts between two consecutive images. 

Please install Libraries:
1. Numpy
2. opencv-contrib-python

TO RUN CODE:

1. Put images in a folder .

2. Enter the image name in order of left to right in way of concantenation. Like:
    Enter the 1 image: S1.jpeg
    Enter the 2 image: S2.jpeg
    
3. Run stitch.py code.
  ```sh
  python stitch.py --image <image folder path> --output <output folder path>
  ```
4. Then, you will get your panorama image as stitch.jpeg in your image dataset folder. 

- Used SIFT to detect feature and then RANSAC, compute Homography and matched points and warp prespective to get final panoramic image.

RESULTS:

Result of S1.jpeg, S2.jpeg, S3.jpeg, S4.jpeg and S5.jpeg

![alt text](https://github.com/rajatrai16921/PhotoCAT/blob/main/dataset/S1.jpeg)

![alt text](https://github.com/rajatrai16921/PhotoCAT/blob/main/dataset/S2.jpeg)

![alt text](https://github.com/rajatrai16921/PhotoCAT/blob/main/dataset/S3.jpeg)

![alt text](https://github.com/rajatrai16921/PhotoCAT/blob/main/dataset/S4.jpeg)

![alt text](https://github.com/rajatrai16921/PhotoCAT/blob/main/dataset/S5.jpeg)

![alt text](https://github.com/rajatrai16921/PhotoCAT/blob/main/dataset/matched_points.jpeg)

![alt text](https://github.com/rajatrai16921/PhotoCAT/blob/main/dataset/stitch.jpeg)
