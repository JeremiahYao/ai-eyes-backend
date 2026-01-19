import cv2
from core.pipeline import run_navigation_pipeline
from core.decision import choose_primary_threat
from core.speech import generate_message

def run_video(
    video_path,
    metadata,
    max_frames=30,
    frame_skip=1
):
    cap = cv2.VideoCapture(video_path)
    prev_results = None
    frame_id = 0

    while cap.isOpened() and frame_id < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % frame_skip != 0:
            frame_id += 1
            continue

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = run_navigation_pipeline(
            img_rgb,
            img_rgb,
            metadata,
            prev_results
        )

        print(f"--- Frame {frame_id} ---")

        primary = choose_primary_threat(results)

        if primary:
            print(generate_message(primary))
        else:
            print("No important objects detected.")

        prev_results = results
        frame_id += 1

    cap.release()
