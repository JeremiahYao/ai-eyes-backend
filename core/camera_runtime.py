import cv2
from core.pipeline import run_navigation_pipeline
from core.memory import TemporalMemory
from core.decision import choose_primary_threat
from core.speech import generate_message

def run_camera(metadata, camera_id=0):
    cap = cv2.VideoCapture(camera_id)
    memory = TemporalMemory()

    frame_idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = run_navigation_pipeline(
            left_image=img_rgb,
            right_image=img_rgb,
            metadata=metadata
        )

        primary = choose_primary_threat(results)
        should_alert, motion = memory.analyze(primary)

        if should_alert:
            print(generate_message(primary, motion))

        cv2.imshow("AI Eyes", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        frame_idx += 1

    cap.release()
    cv2.destroyAllWindows()
