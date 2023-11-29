import os
import subprocess
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def convert_ivf_to_jpegs(input_ivf, output_pattern):
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_ivf,
        "-vf", "fps=1",  # Adjust frame rate if needed
        output_pattern
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print("IVF file converted to JPEGs successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting IVF to JPEGs: {e}")

def find_jpeg_frames(directory):
    jpeg_frames = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg"):
                jpeg_frames.append(os.path.join(root, file))
                
    return jpeg_frames

directory_path = "/Users/dan/Desktop/softwareDev/save-to-disk"
input_ivf = "/Users/dan/Desktop/softwareDev/save-to-disk/output.ivf"
output_pattern = "/Users/dan/Desktop/softwareDev/save-to-disk/output%04d.jpg"

# Convert IVF to JPEGs
convert_ivf_to_jpegs(input_ivf, output_pattern)

# Find JPEG keyframes in the directory
jpeg_files = find_jpeg_frames(directory_path)

if jpeg_files:
    print("Success! JPEG files found:")
    for jpeg_file in jpeg_files:
        results = model(directory_path)
        success = model.export(format='onnx')
        #  print(jpeg_file)
    # Add your code to interact with the AI processing application here
else:
    print("No JPEG files found.")

