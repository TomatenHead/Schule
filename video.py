import os
import subprocess
import time

def play_video(video_path):
    # Replace 'mpv' with your preferred video player
    os.system(f'mpv {video_path}')

def open_script(script_path):
    subprocess.Popen(['python', script_path])

def main():
    video_path = 'path/to/your/video.mp4'  # Replace with your video file path
    script_path = 'path/to/your/script.py'  # Replace with your Python script path
    
    play_video(video_path)
    time.sleep(5)  # Adjust the delay time as needed
    
    open_script(script_path)

if __name__ == "__main__":
    main()
