# face_rec
#this project implements a simple face recognition system using Python and OpenCV.
#The system captures images using your PC camera, trains a recognizer on the captured images,
  #and then uses the camera to detect and recognize faces in real-time.

  
## Features

- Captures 10 photos from your webcam and saves them to a specified folder.
- Trains an LBPH (Local Binary Patterns Histograms) face recognizer on captured photos.
- Detects and recognizes faces in real-time using your PC camera.
- Displays the recognized name and confidence score above the detected face.

## Requirements

- Python 3.x
- OpenCV (`opencv-python` and `opencv-contrib-python`)
- Numpy

Install dependencies using:
```bash
pip install -r requirements.txt

