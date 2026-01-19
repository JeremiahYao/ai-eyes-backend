# core/video_runtime.py

import cv2
from core.pipeline import run_navigation_pipeline
from core.memory import TemporalMemory
from core.decision import choose_primary_threat
from core.speech import generate_message

def run_video(video_path, metadata, max_frames=50, frame_skip=1):
    cap = cv2.VideoCapture(video_path)
    memory = TemporalMemory()

    frame_idx = 0
    processed = 0

    while cap.isOpened() and processed < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frame_skip != 0:
            frame_idx += 1
            continue

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = run_navigation_pipeline(
            left_image=img_rgb,
            right_image=img_rgb,
            metadata=metadata
        )

        primary = choose_primary_threat(results)
        should_alert, motion = memory.analyze(primary)

        print(f"--- Frame {frame_idx} ---")
        if should_alert and primary:
            print(generate_message(primary, motion))
        else:
            print("(no new alert)")

        frame_idx += 1
        processed += 1

    cap.release()
