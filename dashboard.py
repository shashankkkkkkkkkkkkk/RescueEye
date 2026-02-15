import streamlit as st
import os
import time
from PIL import Image

st.set_page_config(
    page_title="RescueEye Command Center",
    layout="wide"
)

st.title("🚨 RescueEye Disaster Command Center")

folder = "detections"

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📡 Live Survivor Monitoring")

    st.info("Run Rescue Detection System in another terminal.")

    cam_placeholder = st.empty()

with col2:
    st.subheader("📊 Live Stats")

    if not os.path.exists(folder):
        st.warning("No detections folder yet.")
        st.stop()

    images = sorted(os.listdir(folder))

    st.metric("Survivors Detected", len(images))

    if len(images) > 0:
        latest = images[-1]
        st.subheader("📸 Latest Evidence")
        st.image(Image.open(f"{folder}/{latest}"), width=300)

st.divider()

st.subheader("🖼 Evidence Gallery")

if len(images) == 0:
    st.info("No survivor evidence yet.")
else:
    cols = st.columns(4)

    for i, img in enumerate(images[::-1]):
        with cols[i % 4]:
            st.image(
                Image.open(f"{folder}/{img}"),
                caption=img,
                use_container_width=True
            )

st.divider()

st.caption("RescueEye © Hackathon Prototype — Edge AI + Drone Vision + Instant Alerts")

time.sleep(2)
st.rerun()
