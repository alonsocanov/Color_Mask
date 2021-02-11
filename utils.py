import numpy as np
import cv2
import os
import sys

# color normalization of HSV to OpenCV HSV
def hsvToCvHsv(hsv: np.array) -> np.array:
    # For HSV, Hue range is [0,179], Saturation range is [0,255]
    # and Value range is [0,255]. Different software use different scales.
    # So if you are comparinn in OpenCV values with them, you need to normalize these ranges.
    hsv_cv = np.array([179, 255, 255])
    hsv_orig = np.array([360, 100, 100])
    cv_hsv = np.divide((hsv * hsv_cv), hsv_orig)
    return cv_hsv


def imgResize(img:np.ndarray, factor:float = None):
    h, w = img.shape[:2]
    if not factor:
        factor = 500 / w
    return int(factor * w), int(factor * h)


def fileExist(path:str):
    if path.isnumeric():
        path = int(path)
    video = cv2.VideoCapture(path)
    ret, frame = video.read()
    message = ''
    if video.isOpened() == False or not ret:
        if isinstance(path, int):
            video = cv2.VideoCapture(path + 1)
            ret, frame = video.read()
            if video.isOpened() == False or not ret:
                message = 'Error opening video stream'
        else:
            message = 'Error opening file'
    if message:
        video.release()
        sys.exit(message)
    return video

def colorGradient(img, hsv_lower, hsv_upper):
    height, width = img.shape[:2]
    img = cv2.resize(img, (width, height))

    h_l, s_l, v_l = hsv_lower
    h_u, s_u, v_u = hsv_upper


    h_gard = np.linspace(h_l, h_u, width)
    s_gard = np.linspace(s_l, s_u, width)
    v_gard = np.linspace(v_l, v_u, width)

    img[:, :, 0] = np.tile(h_gard, (height, 1))
    img[:, :, 1] = np.tile(s_gard, (height, 1))
    img[:, :, 2] = np.tile(v_gard, (height, 1))

    img = img.astype(np.uint8)

    return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
