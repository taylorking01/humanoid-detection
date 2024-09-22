# main.py

import cv2

def say_hello(): # Returns a string
    return "Hello, World!"

def open_camera(): # Opens the camera and returns when 'q' is pressed
    cap = cv2.VideoCapture(0)  # Open the default camera (usually camera 0)

    if not cap.isOpened():
        raise ValueError("Unable to open the camera")

    while True:
        ret, frame = cap.read()  # Capture frame-by-frame

        if not ret:
            raise RuntimeError("Failed to capture frame")

        cv2.imshow('Camera Feed', frame)  # Display the resulting frame

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the camera when done
    cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    assert say_hello() == "Hello, World!"  # Basic assert test for TDD
    print(say_hello())

    # Open the camera until 'q' is pressed
    try:
        open_camera()
    except Exception as e:
        print(f"An error occurred: {e}")
