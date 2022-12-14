# Arduino Face Tracking
## Introduction:
This is a simple project using facial recognition, an arduino and a web camera to track and follow a face. I'm using the
[CascadeClassifier](https://docs.opencv.org/4.x/d1/de5/classcv_1_1CascadeClassifier.html) from the open-source library 
[OpenCV](https://github.com/opencv/opencv) for Python. The coordinates from the detection gets fed into an arduino where
it gets translated to motor-controls, pointing the camera at the face.

<a href="url"><img src="https://github.com/danj98/ArduinoFaceTracker/blob/master/resources/prototype.jpg" height="400" width="300" ></a>

## Dependencies:
* [Pyserial](https://pypi.org/project/pyserial/)
* [OpenCV](https://pypi.org/project/opencv-python/)

## TODO:
- [ ] Integration with OV7670 camera module
- [ ] Model and print custom parts for servos and camera
- [ ] Integrate laser module to blind guests (???)

## Arduino schematics:
<a href="url"><img src="https://github.com/danj98/ArduinoFaceTracker/blob/master/resources/diagram.png" height="400" width="300" ></a>
