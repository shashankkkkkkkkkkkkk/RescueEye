# 🚨 RescueEye – AI Survivor Detection System

RescueEye is a real-time disaster rescue system that detects trapped survivors using AI and instantly alerts rescue teams.

Inspired by the **Uttarkashi Silkyara Tunnel Collapse (2023)** where 41 workers were trapped underground for days.

---

## 🌍 Problem

In disasters like earthquakes, landslides, tunnel collapses:

- Visibility becomes zero  
- Rescuers don’t know survivor location  
- Golden rescue hours are wasted  
- Manual search is slow and dangerous  

---

## ✅ Solution

RescueEye provides an **AI-powered rapid survivor detection + alert pipeline**:

- Live camera / drone feed monitoring  
- YOLOv8 human detection  
- Evidence frame saving  
- Instant Telegram alerts  
- Emergency phone call trigger  
- Command Center Dashboard  

---

## ⚡ Features

✅ Real-time survivor detection  
✅ Saves survivor evidence frames automatically  
✅ Sends image alerts to Telegram instantly  
✅ Triggers emergency rescue phone call via Twilio  
✅ SOS sound / tapping alert support  
✅ Streamlit-based Command Center Dashboard  
✅ Designed for tunnel + low visibility rescues  

---

## 🏗️ Project Structure

RescueEye/
│
├── rescue_detect.py        # Main AI detection + alerts pipeline
├── dashboard.py            # Streamlit Command Center UI
│
├── telegram_alert.py       # Sends survivor image to Telegram bot
├── call_alert.py           # Triggers emergency phone call using Twilio
├── sos_audio.py            # SOS tapping / sound detection module
│
├── config.py               # Thresholds + API keys (DO NOT upload)
├── config_example.py       # Safe template for setup
│
├── detections/             # Saved survivor evidence frames
├── rescue_log.txt          # Auto log of detections + SOS events
│
├── requirements.txt        # Dependencies
├── README.md               # Documentation
└── yolov8n.pt              # YOLO model weights

##How It Works

Live video feed is captured (phone camera / drone camera)

YOLOv8 detects humans in real-time

On detection:

Frame is saved as evidence

Telegram alert is sent instantly

Emergency phone call is triggered

Event is logged into rescue_log.txt

Streamlit Dashboard displays:

Latest survivor image

Evidence gallery

Live rescue monitoring interface
Running the Project
1. Install Requirements
pip install -r requirements.txt

2. Start Survivor Detection
python rescue_detect.py

3. Launch Command Center Dashboard
python -m streamlit run dashboard.py


Dashboard will open at:

http://localhost:8501

🔐 Config Setup

DO NOT upload real API keys.
Create your own config file:

cp config_example.py config.py


Fill in:

Telegram Bot Token

Twilio Credentials

Detection thresholds

🌟 Real-World Impact

During tunnel collapses like Silkyara (2023):

Survivors are invisible under debris

Rescue teams waste days searching blindly

AI + live alerts can reduce rescue time massively

RescueEye acts as an AI first-responder assistant for NDRF-style deployments.

📌 Future Scope

Thermal heat-signature detection

Underground robot exploration (instead of drones)

SLAM-based tunnel mapping

Radar + vibration survivor detection

Offline edge deployment for disaster zones

👨‍💻 Built For Hackathons

RescueEye is a CAPS-level rapid prototype showing how AI + automation can save lives during the golden hours of rescue.

⭐ Author

Built by Shashank
Hackathon Project – RescueTech Innovation


---

