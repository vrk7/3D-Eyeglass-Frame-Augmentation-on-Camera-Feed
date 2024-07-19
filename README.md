# 3D-Eyeglass-Frame-Augmentation-on-Camera-Feed
The goal of this assignment is to create a Python function that can render a 3d glass frame approximately on the eyes of the detected face from the webcam feed. You can use any open-source Python packages and libraries to achieve this.

Run the requirements file and make the obj location correctly given.

pip install -r requirements.txt

Then run the Python file:

python glasses_augmentation.py

In case any error is coming, being the sudo user intsall the below:

sudo apt-get update
sudo apt-get install libgl1-mesa-glx
sudo apt-get install libglm-dev

Below is the explanation of the code:
# Virtual Glasses Augmentation

This project demonstrates a virtual glasses augmentation application using OpenCV, Mediapipe, and Pyrender. The application detects faces in real-time video frames captured from the webcam and overlays a 3D glasses model on the detected face.

## Requirements

- Python 3.x
- OpenCV
- Mediapipe
- Numpy
- Pyrender
- Trimesh

## Installation

1. Clone the repository:


