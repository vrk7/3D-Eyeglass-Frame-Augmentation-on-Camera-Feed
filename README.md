# 🕶️ 3D Eyeglass Frame Augmentation on Camera Feed

This project demonstrates a **virtual eyeglass augmentation application** built with **OpenCV**, **MediaPipe**, and **Pyrender**.  
The application detects a face in real-time from your webcam and overlays a **3D eyeglass frame model** on the detected face.

---

## ✨ Features
- Real-time face detection using **MediaPipe Face Mesh**
- Overlays any custom **3D glasses model (.obj)**
- Renders with **Pyrender + Trimesh** for realistic placement
- Works directly on webcam feed
- Simple controls: press **`q`** to quit

---

## 📦 Requirements
- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- Pyrender
- Trimesh

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vrk7/3D-Eyeglass-Frame-Augmentation-on-Camera-Feed.git
   cd 3D-Eyeglass-Frame-Augmentation-on-Camera-Feed

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Fix OpenGL errors (Linux only)**
   If you face errors related to OpenGL, install:

   ```bash
   sudo apt-get update
   sudo apt-get install libgl1-mesa-glx
   sudo apt-get install libglm-dev

## 🚀 Usage

1. Place your 3D glasses model file (e.g., oculos.obj) in the project directory.
2. Run the script:
   ```bash
   python glasses_augmentation.py
3. A window will open with your webcam feed.
4. Glasses are automatically positioned on the detected face.
5. Press q to quit.

## 🛠️ How It Works

1. Load model – The .obj 3D glasses file is loaded with Trimesh and converted into a Pyrender mesh.
2. Detect face – MediaPipe Face Mesh detects landmarks on the face.
3. Setup scene – A Pyrender scene with a camera and glasses mesh is created.
4. Process frames – For each video frame:

   Flip horizontally for a mirror effect
   
   Convert to RGB
   
   Detect face + extract eye landmarks
   
   Compute eye center & adjust glasses position/orientation
   
   Render the glasses mesh
   
   Overlay rendered glasses onto the original frame
5. Display – Show augmented feed in real-time until the user quits.


   
   
