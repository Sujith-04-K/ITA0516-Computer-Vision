import cv2
import os

# Image path
image_path = r"C:\Users\Dell\OneDrive\Pictures\Wallpapers\54715.jpg"

# Check if the file exists
if not os.path.exists(image_path):
    print("Error: Image file not found!")
    exit()

# Read the image
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create a 5x5 rectangular kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Apply erosion
    eroded_image = cv2.erode(gray_image, kernel, iterations=1)

    # Save the eroded image
    cv2.imwrite("eroded_image.jpg", eroded_image)
    print("Eroded image saved successfully.")

    # Display the image
    cv2.imshow("Eroded Image", eroded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()