import cv2


def cutting_frames(name):
    vidcap = cv2.VideoCapture(name)
    success, image = vidcap.read()
    count = 0
    frame_count = 0
    while success:
      cv2.imwrite("video/frames/frame%d.jpg" % count, image)     # save frame as JPEG file
      success, image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1
      frame_count += 1
