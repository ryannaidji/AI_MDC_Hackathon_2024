
# 🚁 Drone Control Interface and Real-time Object Detection using AI.

## Overview

This project was developed as part of the **MDC Hackathon in Artificial Intelligence** 🧠, where participants were challenged to create innovative solutions in less than 48 hours. It provides a comprehensive and user-friendly interface to control a DJI Tello drone. Using djitellopy for drone communication, Gradio for an intuitive web-based user interface, and YOLO for optional video frame processing, this system enables seamless control and monitoring of the drone.


The project consists of three main modules:
1. `drone_controls.py` - Handles drone connection, movement, and camera operations.
2. `interface.py` - Creates a Gradio-based web interface for user interaction.
3. `main.py` - Launches the web interface.

## Features 🚀

- **Drone Control**: Perform basic drone movements (takeoff, landing, move up, down, forward, backward, left, right, rotate).
- **Camera Operations**: Start/stop the camera feed.
- **Video Processing**: Use a pre-trained YOLO model (`yolo11n.pt`) for real-time object detection in video frames. You can also create your own YOLO models for specific object detection tasks.
- **Emergency Stop ⚠️**: Quickly stop all operations in case of emergencies.

## Getting Started 🛠️

### Prerequisites

Ensure you have Python installed (version >= 3.8). Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Files Overview

- `drone_controls.py`: Contains the logic for controlling the drone and processing the camera feed.
- `interface.py`: Defines the Gradio-based user interface.
- `main.py`: Entry point to run the application.
- `requirements.txt`: Lists the Python dependencies.
- `yolo11n.pt`: Pre-trained YOLO model file for object detection.

### Running the Project ▶️

1. Ensure the DJI Tello Drone is turned on and connected to your network.
2. Run the application:

   ```bash
   python main.py
   ```

3. Open the Gradio interface link in your browser.

### Interface Overview 🖥️

The Gradio interface consists of:
- **Drone Video Feed**: Displays live video from the drone. Toggle YOLO processing for real-time object detection.
- **Control Buttons**:
  - 🔌 **Connection**: Connect and disconnect the drone.
  - 📷 **Camera**: Start and stop the camera.
  - 🚁 **Flight Controls**: Take off, land, and move in various directions.
  - 🔄 **Rotation**: Rotate the drone left or right.
  - ⚠️ **Emergency Stop**: Stops all operations immediately.

### YOLO Processing 🔍

This project utilizes a **pre-trained YOLO model (`yolo11n.pt`)** for object detection. You can also create and integrate your own YOLO models for specific object detection needs.

### Drone Commands ✈️

Here are the key drone control functions:

- `connect_drone()`: Connect to the drone.
- `disconnect_drone()`: Disconnect from the drone.
- `start_camera()`: Start the camera feed.
- `stop_camera()`: Stop the camera feed.
- `take_off()`: Take off the drone.
- `land()`: Land the drone.
- Movement:
  - `move_up()`
  - `move_down()`
  - `move_forward()`
  - `move_backward()`
  - `move_left()`
  - `move_right()`
- Rotation:
  - `rotate_left()`
  - `rotate_right()`

## File Structure 📂

```plaintext
.
├── drone_controls.py    # Drone control logic
├── interface.py         # Gradio-based UI
├── main.py              # Launches the application
├── requirements.txt     # Project dependencies
├── yolo11n.pt           # YOLO model file for object detection
```

## Contributors 🤝

This project was a collaborative effort during the **MDC Hackathon in Artificial Intelligence 🧠**. Each team member contributed to the development, design, and implementation of the project. Thank you for your hard work and dedication! 🎉

### Core Contributors 💡

- **[Ryan NAIDJI](https://www.linkedin.com/in/ryannaidji/)**  - AI Developer | MDC Student
- **[Reza NAIDJI](https://www.linkedin.com/in/reza-naidji/)** - Senior Cloud Data Architect | Data Architect | MDC Student
- **[Abdelkrim INNOUCHE](https://www.linkedin.com/in/abdelkriminnouche/)** - AI Developer | MDC Student


We are proud of what we’ve accomplished together and hope this project serves as an inspiration for future innovations in drone technology and artificial intelligence. 🚀

### Special Thanks ❤️

- **Hackathon Organizers**: For providing us with the opportunity to participate and innovate, and for generously lending us a DJI Tello drone to use during the event.
- **Mentors**: For their guidance and insights throughout the project.

Thank you to everyone who contributes to making this project better every day! 🌟



