import cv2
from utils import hsvToCvHsv, imgResize, fileExist, colorGradient
import numpy as np
import argparse



def main():

    hsv_lower = hsvToCvHsv(np.array([40, 40, 50]))
    hsv_upper = hsvToCvHsv(np.array([65, 100, 100]))

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='0',  help="path to file if thre is one")
    parser.add_argument('--save_video', type=bool, default=False, help='set true to save video')
    args = parser.parse_args()


    video = fileExist(args.path)

    ret, frame = video.read()
    width, height = imgResize(frame)
    img = cv2.resize(frame, (width, height))

    img_range = colorGradient(img, hsv_lower, hsv_upper)


    win_name = 'Frame'
    cv2.namedWindow(win_name)
    cv2.moveWindow(win_name, 20, 20)

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = .5
    fontColor = (255, 255, 255)
    lineType = 2

    if args.save_video:
        # Define the codec and create VideoWriter object
        out = cv2.VideoWriter('outputs/video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 24, (3*width, height))


    while True:
        ret, frame = video.read()
        img = cv2.resize(frame, (width, height))
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
        mask = cv2.erode(mask, None, iterations=2)

        mask_color = img.copy()
        mask_color[mask == 0] = 0
        display_img = cv2.hconcat([img_range, img, mask_color])

        if args.save_video:
            out.write(display_img)
        cv2.imshow(win_name, display_img)


        key = cv2.waitKey(1) & 0xFF

        if key == ord('p'):
            cv2.imwrite('outputs/img.jpeg', display_img)

        if key == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()