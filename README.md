# 3D-Eyeglass-Frame-Augmentation-on-Camera-Feed

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
   git clone https://github.com/vrk7/3D-Eyeglass-Frame-Augmentation-on-Camera-Feed.git

2. Install the required dependencies:
   pip install -r requirements.txt

3. In case any error is coming, being the sudo user intsall the below:

  sudo apt-get update
  sudo apt-get install libgl1-mesa-glx
  sudo apt-get install libglm-dev


## Usage

1. Place your 3D glasses model file (e.g., `oculos.obj`) in the project directory.

2. Run the script:
  python glasses_augmentation.py

3. The application will open a window displaying the real-time video feed from your webcam.

4. The glasses will be automatically overlaid on the detected face.

5. Press 'q' to quit the application.
