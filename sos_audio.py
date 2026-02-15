import sounddevice as sd
import numpy as np

def detect_sos(threshold=20):
    duration = 1  # seconds

    audio = sd.rec(
        int(44100 * duration),
        samplerate=44100,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    volume = np.linalg.norm(audio)

    if volume > threshold:
        print("🚨 SOS SOUND DETECTED!")
        return True

    return False
