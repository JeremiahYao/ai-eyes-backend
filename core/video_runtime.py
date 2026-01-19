"""
Video runtime loop for AI Eyes backend.

Responsibilities:
- Load video
- Process each frame through navigation pipeline
- Apply priority filtering
- Generate speech output
"""

import cv2

from core.pipeline import run_navigation_pipeline
from core.priority import filter_priority
from core.speech import generate_message


def run_video(
    video_path,
    metadata,
    max_frames=30,
    frame_skip=1
):
    """
    Run AI Eyes on a video file.

    video_path: path to video file
    metadata: dict with focal_length_px, baseline_m
    max_frames: limit frames for testing
    frame_skip: process every Nth frame
    """

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise RuntimeError("❌ Failed to open video file")

    frame_idx = 0
    processed = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Skip frames if needed
        if frame_idx % frame_skip != 0:
            frame_idx += 1
            continue

        # Convert BGR → RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Run navigation pipeline
        results = run_navigation_pipeline(
            left_image=frame_rgb,
            right_image=frame_rgb,   # mono video → same frame
            metadata=metadata
        )

        # Priority filtering
        important = filter_priority(results)

        print(f"\n--- Frame {processed} ---")

        if not important:
            print("No important objects detected.")
        else:
            for r in important:
                msg = generate_message(r)
                print(msg)

        processed += 1
        frame_idx += 1

        if processed >= max_frames:
            break

    cap.release()
    print("\n✅ Video processing finished.")
