# core/video_runtime.py

import cv2
from core.pipeline import run_navigation_pipeline
from core.decision import choose_primary_threat
from core.speech import generate_message


def run_video(video_path, metadata, max_frames=50, frame_skip=1):
    cap = cv2.VideoCapture(video_path)
    prev_results = None
    frame_idx = 0

    while cap.isOpened() and frame_idx < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frame_skip != 0:
            frame_idx += 1
            continue

        results = run_navigation_pipeline(
            left_image=frame,
            right_image=frame,
            metadata=metadata,
            prev_results=prev_results
        )

        primary = choose_primary_threat(results)

        print(f"\n--- Frame {frame_idx} ---")

        if primary:
            print(generate_message(primary))
        else:
            print("No important objects detected.")

        prev_results = results
        frame_idx += 1

    cap.release()
