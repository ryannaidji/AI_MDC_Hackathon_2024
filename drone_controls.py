from djitellopy import Tello
import cv2
import time
from ultralytics import YOLO

# Initialize the drone
drone = Tello()

# YOLO model for optional processing
model = YOLO("yolo11n.pt")

# Global flag for stopping video feed
stop_feed_flag = False


def connect_drone():
    """Connect to the DJI Tello drone."""
    try:
        drone.connect()
        return f"Drone connected. Battery: {drone.get_battery()}%"
    except Exception as e:
        return f"Failed to connect to the drone: {e}"


def disconnect_drone():
    """Disconnect from the DJI Tello drone."""
    try:
        drone.end()
        return "Drone disconnected."
    except Exception as e:
        return f"Failed to disconnect from the drone: {e}"


def start_camera():
    """Start the drone's camera."""
    try:
        drone.streamon()
        return "Camera started."
    except Exception as e:
        return f"Failed to start the camera: {e}"


def stop_camera():
    """Stop the drone's camera."""
    try:
        drone.streamoff()
        return "Camera stopped."
    except Exception as e:
        return f"Failed to stop the camera: {e}"


def get_frame(process=False):
    """Stream frames from the drone, optionally processing them."""
    global stop_feed_flag
    stop_feed_flag = False

    while not stop_feed_flag:
        frame = drone.get_frame_read().frame  # Get raw frame
        
        if frame is None:
            time.sleep(0.1)  # Wait if no frame is available
            continue
        
        if process:
            # Process frame with YOLO
            results = model.predict(frame)
            frame = results[0].plot() if results else frame

        # Convert frame to RGB for display in Gradio
        
        #frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #yield frame_rgb  # Send frame to Gradio
        yield frame

def stop_feed():
    """Stop the video feed."""
    global stop_feed_flag
    stop_feed_flag = True
    return "Video feed stopped."


# Movement and rotation functions remain unchanged
def take_off():
    try:
        drone.takeoff()
        return "Drone taking off."
    except Exception as e:
        return f"Failed to take off: {e}"


def land():
    try:
        drone.land()
        return "Drone landing."
    except Exception as e:
        return f"Failed to land: {e}"


def move_up():
    try:
        drone.move_up(50)
        return "Drone moved up."
    except Exception as e:
        return f"Failed to move up: {e}"


def move_down():
    try:
        drone.move_down(50)
        return "Drone moved down."
    except Exception as e:
        return f"Failed to move down: {e}"


def move_forward():
    try:
        drone.move_forward(50)
        return "Drone moved forward."
    except Exception as e:
        return f"Failed to move forward: {e}"


def move_backward():
    try:
        drone.move_back(50)
        return "Drone moved backward."
    except Exception as e:
        return f"Failed to move backward: {e}"


def move_left():
    try:
        drone.move_left(50)
        return "Drone moved left."
    except Exception as e:
        return f"Failed to move left: {e}"


def move_right():
    try:
        drone.move_right(50)
        return "Drone moved right."
    except Exception as e:
        return f"Failed to move right: {e}"


def rotate_left():
    try:
        drone.rotate_counter_clockwise(45)
        return "Drone rotated left."
    except Exception as e:
        return f"Failed to rotate left: {e}"


def rotate_right():
    try:
        drone.rotate_clockwise(45)
        return "Drone rotated right."
    except Exception as e:
        return f"Failed to rotate right: {e}"
