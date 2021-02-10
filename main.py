import cv2
from utils import hsvToCvHsv, imgResize
import numpy as np
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='',  help="Write the kind of tracking 'color' or 'face' or manual")
    args = parser.parse_args()

    if args.path:
        # video path verification
        pass
    else:
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        webcam.release()
        sys.exit("Error opening webcam")
    ret, frame = webcam.read()
    if not ret:
        webcam = cv2.VideoCapture(1)
        ret, frame = webcam.read()

    width, height = imgResize(frame)

    hsv_lower = hsvToCvHsv(np.array([45, 40, 20]))
    hsv_upper = hsvToCvHsv(np.array([65, 90, 90]))

    win_name = 'Frame'
    cv2.namedWindow(win_name)
    cv2.moveWindow(win_name, 20, 20)

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = .5
    fontColor = (255, 255, 255)
    lineType = 2


    while True:
        ret, frame = webcam.read()
        img = cv2.resize(frame, (width, height))
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
        mask = cv2.erode(mask, None, iterations=2)

        mask_color = img.copy()
        mask_color[mask == 0] = 0

        display_img = cv2.hconcat([img, mask_color])

        cv2.imshow(win_name, display_img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()