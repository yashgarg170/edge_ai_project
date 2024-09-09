import cv2
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import time

# Initialize the webcam
video = cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)

segmen = SelfiSegmentation()

option1 = 0
option2 = 0

loopsvar = True


def save_image_to_desktop(image):
    # Get the user's desktop directory
    desktop_path = os.path.expanduser("~/Desktop")

    # Create a folder for the project if it doesn't exist
    project_folder = os.path.join(desktop_path, "project")
    os.makedirs(project_folder, exist_ok=True)

    # Generate a unique file name based on the current timestamp
    timestamp = int(time.time())
    file_name = f"image_{timestamp}.jpg"
    file_path = os.path.join(project_folder, file_name)

    # Save the image to the folder
    cv2.imwrite(file_path, image)

    return file_path


def apply_sepia_filter(frame):
    # Define the sepia filter kernel
    sepia_kernel = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

    sepia_image = cv2.transform(frame, sepia_kernel)
    sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)

    return sepia_image


def apply_emboss_filter(image):
    # Define the emboss filter kernel
    emboss_kernel = np.array([[-2, -1, 0],
                              [-1, 1, 1],
                              [0, 1, 2]])

    emboss_image = cv2.filter2D(image, -1, emboss_kernel)
    emboss_image = np.clip(emboss_image, 0, 255).astype(np.uint8)

    return emboss_image


def pixelate(image):
    pixel_size = 10
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Resize the image to a smaller size
    temp_image = cv2.resize(image, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_NEAREST)

    # Resize the smaller image back to the original size
    pixelated_image = cv2.resize(temp_image, (width, height), interpolation=cv2.INTER_NEAREST)

    return pixelated_image

def apply_edge_enhance(image):
    # Define the enhanced edge filter kernel
    enhanced_edge_kernel = np.array([[-1, -1, -1],
                                     [-1, 10, -1],
                                     [-1, -1, -1]])

    enhanced_edge_image = cv2.filter2D(image, -1, enhanced_edge_kernel)
    enhanced_edge_image = np.clip(enhanced_edge_image, 0, 255).astype(np.uint8)

    return enhanced_edge_image

def brightness_control(image, value):
    # Increase brightness by adding a constant value to each pixel
    brightened_image = cv2.convertScaleAbs(image, alpha=1, beta=value)

    return brightened_image





def selectionopt():
    global option1
    while True:
        ret, frame = video.read()

        # Check if the video capture was successful
        if not ret:
            print("Error: Failed to capture frame from the webcam.")
            break

        cv2.imshow("Option 1: Press 1 (Person), 2 (Background), 3 (Whole Frame)", frame)

        # Wait for user input indefinitely
        key = cv2.waitKey(0)

        if key == ord('1'):
            option1 = 1  # Apply filter to the person
            break
        elif key == ord('2'):
            option1 = 2  # Apply filter to the background
            break
        elif key == ord('3'):
            option1 = 3  # Apply filter to the whole frame
            break

    cv2.destroyWindow("Option 1: Press 1 (Person), 2 (Background), 3 (Whole Frame)")
    return option1


option1 = selectionopt()


def final(option2, frame):
    if option1 == 1:
        if option2 == 1:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            person = cv2.GaussianBlur(person, (15, 15), 0)
            frame = cv2.add(person, background)
        elif option2 == 2:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            person = apply_sepia_filter(person)
            frame = cv2.add(person, background)
        elif option2 == 3:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            person = pixelate(person)
            frame = cv2.add(person, background)
        elif option2 == 4:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            person = apply_emboss_filter(person)
            frame = cv2.add(person, background)
        elif option2 == 5:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            person = apply_edge_enhance(person)
            frame = cv2.add(person, background)
        elif option2 == 'i':
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            background=brightness_control(background,-10)
            person = brightness_control(person,10)
            frame = cv2.add(person, background)
        elif option2 == 'd':
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            background = brightness_control(background, -10)
            frame = cv2.add(person, background)

    elif option1 == 2:
        if option2 == 1:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            background = cv2.GaussianBlur(background, (15, 15), 0)
            frame = cv2.add(person, background)
        elif option2 == 2:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            background = apply_sepia_filter(background)
            frame = cv2.add(person, background)
        elif option2 == 3:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            background = pixelate(background)
            frame = cv2.add(person, background)
        elif option2 == 4:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            background = apply_emboss_filter(background)
            frame = cv2.add(person, background)
        elif option2 == 5:
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            background = apply_edge_enhance(background)
            frame = cv2.add(person, background)
        elif option2 == 'd':
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            background = brightness_control(background, -10)
            frame = cv2.add(person, background)
        elif option2 == 'i':
            person = segmen.removeBG(frame, (0, 0, 0), cutThreshold=0.8)
            background = cv2.subtract(frame, person)
            background = brightness_control(background, 30)
            person = brightness_control(person, -30)
            frame = cv2.add(person, background)
    elif option1 == 3:
        if option2 == 1:
            frame = cv2.GaussianBlur(frame, (15, 15), 0)
        elif option2 == 2:
            frame = apply_sepia_filter(frame)
        elif option2 == 3:
            frame = pixelate(frame)
        elif option2 == 4:
            frame = apply_emboss_filter(frame)
        elif option2 == 5:
            frame = apply_edge_enhance(frame)
        elif option2 == 'i':
            frame = apply_edge_enhance(frame)
        elif option2 == 'd':
            frame = apply_edge_enhance(frame)



    return frame


while loopsvar:
    check, frame = video.read()
    if not check:
        print("Error: Failed to capture frame from the webcam.")
        break

    frame = final(option2, frame)

    cv2.imshow("filtered", frame)
    key = cv2.waitKey(1)
    if key == ord('c'):
        loopsvar = False
    elif key == ord('1'):
        option2 = 1
    elif key == ord('2'):
        option2 = 2
    elif key == ord('3'):
        option2 = 3
    elif key == ord('4'):
        option2 = 4
    elif key == ord('5'):
        option2 = 5
    elif key == ord('i'):
        option2 = 'i'
    elif key == ord('d'):
        option2 = 'd'
    elif key == ord('s'):
        save_image_to_desktop(frame)

# Release video capture and close all windows
video.release()
cv2.destroyAllWindows()
