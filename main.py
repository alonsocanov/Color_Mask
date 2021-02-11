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

    hsv_lower = hsvToCvHsv(np.array([40, 40, 50]))
    hsv_upper = hsvToCvHsv(np.array([65, 100, 100]))

    h_l, s_l, v_l = hsv_lower
    h_u, s_u, v_u = hsv_upper

    img_range = cv2.resize(frame, (width, height))
    h_gard = np.linspace(h_l, h_u, width)
    s_gard = np.linspace(s_l, s_u, width)
    v_gard = np.linspace(v_l, v_u, width)

    img_range[:, :, 0] = np.tile(h_gard, (height, 1))
    img_range[:, :, 1] = np.tile(s_gard, (height, 1))
    img_range[:, :, 2] = np.tile(v_gard, (height, 1))

    img_range = cv2.cvtColor(img_range.astype(np.uint8), cv2.COLOR_HSV2BGR)


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
        display_img = cv2.hconcat([img_range, img, mask_color])

        cv2.imshow(win_name, display_img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    webcam.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()