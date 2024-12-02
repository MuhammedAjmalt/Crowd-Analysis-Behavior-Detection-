# Crowd-Analysis-Behavior-Detection-
 #Video Frame Extraction and Crowd Behavior Analysis

## Overview
This project consists of two main components: a Python script for extracting frames from video files and a Jupyter Notebook for analyzing crowd behavior using machine learning techniques. The primary goal is to facilitate the extraction of frames from videos and to apply computer vision algorithms for crowd analysis.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Video Frame Extraction](#video-frame-extraction)
- [Crowd Behavior Analysis](#crowd-behavior-analysis)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation
To set up the project, ensure you have Python installed on your system. Then, install the required libraries using pip:

```bash
pip install opencv-python ultralytics torch torchvision tqdm
```

## Usage

### Video Frame Extraction
To extract frames from a video, use the `Frame_extraction.py` script. Modify the `video_path` and `output_folder` variables in the script to specify your video file and the directory where you want to save the extracted frames.

**Example:**
```python
video_path = r"C:\path\to\your\video.mp4"
output_folder = r"C:\path\to\output\frames"
video_to_frames(video_path, output_folder)
```

### Crowd Behavior Analysis
The Jupyter Notebook (`crowd_behavoiur.ipynb`) contains code for analyzing crowd behavior using YOLO (You Only Look Once) object detection. Open the notebook in Jupyter Lab or Jupyter Notebook and run the cells sequentially to perform the analysis.

## Video Frame Extraction
The `Frame_extraction.py` script works as follows:
1. **Input:** A video file path and an output folder.
2. **Process:** It reads the video file frame by frame.
3. **Output:** Each frame is saved as a JPEG image in the specified output folder.

### Code Snippet
```python
import cv2
import os

def video_to_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join(output_folder, f'frame{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames to '{output_folder}'")
```

## Crowd Behavior Analysis
The notebook leverages YOLO for detecting objects in real-time. It requires a pretrained YOLO model (`yolov8n.pt`) to function effectively.

### Key Steps:
1. Load the YOLO model.
2. Configure settings for detection.
3. Run detection on input data and visualize results.

## Dependencies
This project requires the following libraries:
- OpenCV: For video processing.
- PyTorch: For deep learning tasks.
- Ultralytics: For YOLO model implementation.
- Other libraries: NumPy, Pandas, Matplotlib, etc.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/43377108/2a366511-73db-4376-8421-cceafa5f42a7/Frame_extraction.py
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/43377108/5d873356-4776-4d68-8a19-cbbef19b91b1/crowd_behavoiur.ipynb
