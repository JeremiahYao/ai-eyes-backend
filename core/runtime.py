import time
import cv2

from core.pipeline import run_navigation_pipeline
from core.speech import generate_message

def run_loop(image, metadata, iterations=3, delay=1.0):
    """
    Simulated real-time loop using the same image.
    """

    for i in range(iterations):
        print(f"\n--- Frame {i+1} ---")

        results = run_navigation_pipeline(
            left_image=image,
            right_image=image,
            metadata=metadata
        )

        for r in results:
            print(generate_message(r))

        time.sleep(delay)
