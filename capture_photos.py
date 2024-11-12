import cv2
import os
import time  # Importing the time module for the sleep function

# Create directory if not exists
folder_name = "samar"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Initialize the camera
cap = cv2.VideoCapture(0)
count = 0

while count < 10:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save the frame as an image file
    img_path = os.path.join(folder_name, f"photo_{count}.jpg")
    cv2.imwrite(img_path, frame)
    print(f"Saved {img_path}")
    
    count += 1
    cv2.imshow("Capture", frame)
    
    # Wait for 2 seconds before capturing the next photo
    time.sleep(2)
    
    # Press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and close
cap.release()
cv2.destroyAllWindows()
