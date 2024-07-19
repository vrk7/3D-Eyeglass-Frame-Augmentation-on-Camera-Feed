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


## How it works

1. The script loads the 3D glasses model using Trimesh and creates a Pyrender mesh from it.

2. It initializes the Mediapipe Face Mesh model for face detection and landmark estimation.

3. A Pyrender scene is created with a camera and the glasses node.

4. The script captures video frames from the webcam using OpenCV.

5. For each frame:
- The frame is flipped horizontally for a mirror effect.
- The frame is converted to RGB color space.
- Faces are detected using the Mediapipe Face Mesh model.
- For each detected face:
  - The eye coordinates are extracted from the face landmarks.
  - The center of the eyes is calculated.
  - The glasses position and orientation are set based on the eye coordinates.
  - The scene is rendered using Pyrender.
  - The rendered glasses are overlaid on the frame using a mask.

6. The resulting frame with the overlaid glasses is displayed in a window.

7. The process continues until the user presses 'q' to quit the application.
