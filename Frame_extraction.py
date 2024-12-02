import cv2
import os

def video_to_frames(video_path, output_folder):
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the base name of the video file (without directory and extension)
    video_name = os.path.basename(video_path)
    video_name_without_ext = os.path.splitext(video_name)[0]

    # Capture the video from the given path
    cap = cv2.VideoCapture(video_path)
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Construct the frame filename including the video name
        frame_filename = os.path.join(output_folder, f'{video_name_without_ext}frame{frame_count:04d}.jpg')
        # Save the frame as an image
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extracted {frame_count} frames to '{output_folder}'")

# Example usage
video_path = r"C:\Users\ADHISH S\Desktop\Realtime\video_2.mp4"
output_folder = r"C:\Users\ADHISH S\Desktop\Realtime\frames_02"
video_to_frames(video_path, output_folder)