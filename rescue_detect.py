from ultralytics import YOLO
import cv2
import os
import time
import winsound
import threading

from sos_audio import detect_sos
from telegram_alert import send_telegram_alert
from call_alert import make_call_alert
from config import CONF_THRESHOLD, ALERT_GAP, CALL_ENABLED


model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("http://192.168.137.206:8080/video")

cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

os.makedirs("detections", exist_ok=True)

survivor_count = 0
last_alert_time = 0
log_file = "rescue_log.txt"

frame_skip = 5
frame_id = 0

print("\n🚨 RescueEye Live System Started...\n")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera feed not available.")
        break

    frame = cv2.resize(frame, (640, 360))

    frame_id += 1
    if frame_id % frame_skip != 0:
        cv2.imshow("RescueEye Live", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        continue

    current_time = time.time()

    if detect_sos():
        print("\n🚨 SOS SOUND DETECTED!")

        sos_file = "detections/sos_sound.jpg"
        cv2.imwrite(sos_file, frame)

        winsound.Beep(2000, 800)

        threading.Thread(
            target=send_telegram_alert,
            args=(sos_file, "SOS Sound Alert")
        ).start()

        if CALL_ENABLED:
            threading.Thread(target=make_call_alert).start()

        with open(log_file, "a") as f:
            f.write(f"SOS SOUND detected at {time.ctime()}\n")

        time.sleep(1)

    results = model(frame, verbose=False)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            if cls == 0 and conf > CONF_THRESHOLD:

                if (current_time - last_alert_time) > ALERT_GAP:

                    survivor_count += 1

                    filename = f"detections/survivor_{survivor_count}.jpg"
                    cv2.imwrite(filename, frame)

                    print(f"\n🚨 SURVIVOR FOUND #{survivor_count}")
                    print("📸 Saved:", filename)

                    winsound.Beep(1500, 500)

                    threading.Thread(
                        target=send_telegram_alert,
                        args=(filename, survivor_count)
                    ).start()

                    if CALL_ENABLED:
                        threading.Thread(target=make_call_alert).start()

                    with open(log_file, "a") as f:
                        f.write(
                            f"Survivor #{survivor_count} detected at {time.ctime()}\n"
                        )

                    last_alert_time = current_time

    cv2.putText(
        frame,
        f"Survivors Found: {survivor_count}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 255),
        2
    )

    cv2.imshow("RescueEye Live Detection + Alerts", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("\n🛑 RescueEye stopped manually.")
        break

cap.release()
cv2.destroyAllWindows()

print("\n✅ RescueEye Finished.")
