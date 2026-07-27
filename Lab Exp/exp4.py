import cv2
import numpy as np
import os

# Image path
image_path = r"C:\Users\Dell\OneDrive\Pictures\Wallpapers\anime-style-mythical-dragon-creature.jpg"

# Check if the image exists
if not os.path.exists(image_path):
    print("Error: Image file not found!")
    exit()

# Read the image in grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not load the image.")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated_img = cv2.dilate(img, kernel, iterations=1)

    # Save the output
    cv2.imwrite("Dilated_Image.jpg", dilated_img)
    print("Dilated image saved successfully.")

    # Display the image
    cv2.imshow("Dilated Image", dilated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()