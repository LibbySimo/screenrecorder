import pyautogui
import cv2
import numpy as np

# Set the resolution
resolution = (1920, 1080)

# Define the codec and create a VideoWriter object
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create a named window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    # Take a screenshot
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert the frame from RGB to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to the video file
    out.write(frame)

    # Display the frame
    cv2.imshow('Live', frame)

    # Check for close window event
    if cv2.getWindowProperty("Live", cv2.WND_PROP_VISIBLE) < 1:
        break

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoWriter and destroy all windows
out.release()
cv2.destroyAllWindows()
