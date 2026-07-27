import cv2
import os

# Image path
image_path = r"C:\Users\Dell\OneDrive\Pictures\Wallpapers\Krishna.jpeg"

# Check if the file exists
if not os.path.exists(image_path):
    print("Error: Image file does not exist!")
    exit()

# Read the image
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image.")
else:
    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite("gray_image.jpg", gray_img)
    print("Grayscale image saved as gray_image.jpg")

    # Display the image
    cv2.imshow("Grayscale Image", gray_img)

    print("Press any key inside the image window to close it.")
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()