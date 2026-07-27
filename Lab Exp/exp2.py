import cv2
import os

# Specify the image path
image_path = r"C:\Users\Dell\OneDrive\Pictures\Wallpapers\Wanda Witch.jpeg"

# Check if the image exists
if not os.path.exists(image_path):
    print("Error: Image file not found!")
    exit()

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load the image.")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(image, (5, 5), 10)

    # Save the blurred image
    cv2.imwrite("blurred_image.jpg", blur)
    print("Blurred image saved successfully.")

    # Display the blurred image
    cv2.imshow("Blurred Image", blur)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()