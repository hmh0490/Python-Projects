import cv2
import time
import glob
import os
from emailing import send_email
from threading import Thread

# 0: main camera, 1: secondary camera
video = cv2.VideoCapture(0)
# give camera some time to load, avoid black screen
time.sleep(1)

first_frame = None
status_list = []
count = 1

def clean_folder():
    print("cleaning started")
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
    print("cleaning ended")

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # amount of bluriness (21, 21), stdv = 0
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # capture the first frame, we will compare to that
    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    # if pixel has treshold of 30 or more, re-assign it to 255
    thresh_frame = cv2.threshold(delta_frame, 100, 255, cv2.THRESH_BINARY)[1]
    # remove the noise
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My video", dil_frame)

    # detect contours around white areas
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)

    # if contour around white area is < 10k pixels, it should be disregarded
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            # run the loop again
            continue
        # x, y are coordinates, width and height from that coordinate
        # this is the point the new object is discovered
        x, y, w, h = cv2.boundingRect(contour)
        # rectangle starting point (x, y) and the other corner (x+w, y+h)
        # colour of the rectangle - grey
        # 3 is width of rectangle
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]

    # send email if the object leaves
    if status_list[0] == 1 and status_list[1] == 0:
        print(status_list)
        email_thread = Thread(target=send_email, args=(image_with_object, ))
        # execute (1 line) above code in the background
        email_thread.daemon = True

        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True

        email_thread.start()

    cv2.imshow("My video frame", frame)
    # create keyboard key object",
    key = cv2.waitKey(1)

    # if we press q, the video breaks
    if key == ord("q"):
        clean_thread.start()
        break

video.release()
# clean_thread.start()
