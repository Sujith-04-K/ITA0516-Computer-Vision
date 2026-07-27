import cv2
import os

# Image path
image_path = r"C:\Users\Dell\OneDrive\Pictures\Wallpapers\download.jpg"
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
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Save the edge-detected image
    cv2.imwrite("Canny_Edges.jpg", edges)
    print("Canny edge image saved successfully.")

    # Display the image
    cv2.imshow("Edges", edges)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()