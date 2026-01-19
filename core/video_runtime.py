import cv2
from core.pipeline import run_navigation_pipeline
from core.speech import generate_message

def run_video(video_path, metadata, max_frames=50):
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = run_navigation_pipeline(
            left_image=frame_rgb,
            right_image=frame_rgb,  # still simulated stereo
            metadata=metadata
        )

        print(f"\n--- Frame {frame_count} ---")
        for r in results:
            print(generate_message(r))

        frame_count += 1

    cap.release()
