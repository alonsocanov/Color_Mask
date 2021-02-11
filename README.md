# Color Mask

This repository aims to facilitate color object detection using HSV color space.
When runing, a window will apear with thre feeds:

1) The color gradient from the lower to upper hsv values

2) The webcam or video feed

3) The masked imaged wher it will show the colors seen by the mask and hopefully the object that whanst to be detected will be shown with a sourrounding mask

## Libraries

- opencv
- numpy
- argparse

## Repository Files

- main.py
- utils.py

## Code Run

There are two tipes of feed, one is using the  video feed and the other one is using a pretaped video.

In order to run the webcam feed run as follows:

```bash
python main.py
```

If the argument ```--path``` is given there must be the path to the pretaped video. As shown in the example:

```bash
python main.py --path path/to/video.mp4
```
