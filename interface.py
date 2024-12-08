import gradio as gr
from drone_controls import (
    connect_drone, disconnect_drone, start_camera, stop_camera,
    get_frame, stop_feed, take_off, land, move_up, move_down,
    move_forward, move_backward, move_left, move_right,
    rotate_left, rotate_right
)

def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("<h1 style='text-align: center;'>Drone Control Interface</h1>")
        
        emergency_button = gr.Button("🛑 EMERGENCY STOP", variant="stop", elem_id="emergency-button")
        
        with gr.Row():
            # Video feed section
            with gr.Column(scale=2):
                gr.Markdown("### Drone Video Feed")
                
                # Display video stream
                video_feed = gr.Image(label="Drone Camera", type="numpy", streaming=True)
                
                # Checkbox to toggle YOLO processing
                process_video = gr.Checkbox(value=False, label="Process video with YOLO")
                
                # Start/Stop video feed buttons
                start_feed_button = gr.Button("▶️ Start Feed")
                stop_feed_button = gr.Button("⏹️ Stop Feed")
            
            # Controls section
            with gr.Column(scale=1):
                gr.Markdown("### Controls")
                
                # Connection controls
                connect_button = gr.Button("🔌 Connect")
                disconnect_button = gr.Button("❌ Disconnect")
                
                # Camera controls
                start_camera_button = gr.Button("📷 Start Camera")
                stop_camera_button = gr.Button("📷 Stop Camera")
                
                # Takeoff and landing controls
                takeoff_button = gr.Button("🛫 Take Off")
                land_button = gr.Button("🛬 Land")
                
                # Movement controls
                gr.Markdown("### Vertical Movement")
                up_button = gr.Button("⬆️ Up")
                down_button = gr.Button("⬇️ Down")
                
                gr.Markdown("### Horizontal Movement")
                forward_button = gr.Button("⬆️ Forward")
                backward_button = gr.Button("⬇️ Backward")
                left_button = gr.Button("⬅️ Left")
                right_button = gr.Button("➡️ Right")
                
                gr.Markdown("### Rotation Controls")
                rotate_left_button = gr.Button("↺ Rotate Left")
                rotate_right_button = gr.Button("↻ Rotate Right")
        
        # Button mappings
        connect_button.click(connect_drone, outputs=gr.Textbox(label="Status"))
        disconnect_button.click(disconnect_drone, outputs=gr.Textbox(label="Status"))
        start_camera_button.click(start_camera, outputs=gr.Textbox(label="Status"))
        stop_camera_button.click(stop_camera, outputs=gr.Textbox(label="Status"))
        start_feed_button.click(get_frame, inputs=process_video, outputs=video_feed)
        stop_feed_button.click(stop_feed, outputs=gr.Textbox(label="Status"))
        takeoff_button.click(take_off, outputs=gr.Textbox(label="Status"))
        land_button.click(land, outputs=gr.Textbox(label="Status"))
        up_button.click(move_up, outputs=gr.Textbox(label="Status"))
        down_button.click(move_down, outputs=gr.Textbox(label="Status"))
        forward_button.click(move_forward, outputs=gr.Textbox(label="Status"))
        backward_button.click(move_backward, outputs=gr.Textbox(label="Status"))
        left_button.click(move_left, outputs=gr.Textbox(label="Status"))
        right_button.click(move_right, outputs=gr.Textbox(label="Status"))
        rotate_left_button.click(rotate_left, outputs=gr.Textbox(label="Status"))
        rotate_right_button.click(rotate_right, outputs=gr.Textbox(label="Status"))

    return demo
