import numpy as np
import cv2

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