import cv2
import mediapipe as mp
import numpy as np
import pyrender
import trimesh

# Load the 3D glass model
try:
    glass_trimesh = trimesh.load("C:/Users/vysak/OneDrive/Desktop/3D Work/oculos.obj")
except Exception as e:
    print(f"Error loading 3D model: {e}")
    exit()

glass_mesh = pyrender.Mesh.from_trimesh(glass_trimesh)
glass_node = pyrender.Node(mesh=glass_mesh, matrix=np.eye(4))

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize Pyrender scene
scene = pyrender.Scene(ambient_light=[0.02, 0.02, 0.02])
camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0, aspectRatio=1.0)
camera_node = scene.add(camera, pose=np.eye(4))

# Initialize Pyrender Offscreen Renderer
renderer = pyrender.OffscreenRenderer(viewport_width=640, viewport_height=480)

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)  # For Linux
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Add glass node to the scene initially
scene.add_node(glass_node)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Convert the frame color to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                try:
                    # Convert normalized landmarks to pixel coordinates
                    h, w, _ = frame.shape
                    left_eye = face_landmarks.landmark[33]
                    right_eye = face_landmarks.landmark[263]
                    left_eye_coords = np.array([left_eye.x * w, left_eye.y * h, left_eye.z * w])
                    right_eye_coords = np.array([right_eye.x * w, right_eye.y * h, right_eye.z * w])
                    center_eye = (left_eye_coords + right_eye_coords) / 2

                    # Convert center_eye to the correct type
                    center_eye = center_eye.astype(np.float32)

                    # Set the glass position and orientation based on the eye coordinates
                    glass_matrix = np.eye(4, dtype=np.float32)
                    glass_matrix[:3, 3] = center_eye
                    glass_matrix[:3, :3] = cv2.Rodrigues(np.array([0, 0, 0], dtype=np.float32))[0]
                    glass_node.matrix = glass_matrix

                    # Render the scene
                    color, depth = renderer.render(scene)
                    mask = (depth > 0)[:, :, None]
                    mask = np.repeat(mask, 3, axis=2)  # Ensure mask has the same number of dimensions as color
                    frame[mask] = color[mask]
                except Exception as e:
                    print(f"Error processing face landmarks: {e}")

        # Display the resulting frame
        cv2.imshow('Glasses Augmentation', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()
    renderer.delete()
    face_mesh.close()