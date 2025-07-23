import streamlit as st
import numpy as np
import pickle


with open ("randomforest.pkl","rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="5G Resource Allocation Predictor", layout="centered")
st.title("5G Resource Allocation Predictor ")


st.markdown("Enter network parameters below:")

signalstrength = st.number_input("Signal_Strength", min_value=-100.0, step=0.1)
latency = st.number_input("Latency", min_value=0)
requiredbandwidth = st.number_input("Required_Bandwidth", min_value=0.0, step=0.1)
allocatedbandwidth = st.number_input("Allocated_Bandwidth",min_value=0.0, step=0.1 )

st.subheader("Select Application Types Used (Tick applicable):")

app_emergency = st.checkbox("Emergency Service")
app_file = st.checkbox("File Download")
app_iot = st.checkbox("IoT Temperature")
app_gaming = st.checkbox("Online Gaming")
app_streaming = st.checkbox("Streaming")
app_video_call = st.checkbox("Video Call")
app_video_stream = st.checkbox("Video Streaming")
app_voip = st.checkbox("VoIP Call")
app_voice = st.checkbox("Voice Call")
app_web = st.checkbox("Web Browsing")

features = np.array([[
    signalstrength,
    latency,
    requiredbandwidth,
    allocatedbandwidth,
    int(app_emergency),
    int(app_file),
    int(app_iot),
    int(app_gaming),
    int(app_streaming),
    int(app_video_call),
    int(app_video_stream),
    int(app_voip),
    int(app_voice),
    int(app_web),
]])

if st.button("Predict Resource Allocation"):
    prediction = model.predict(features)[0]
    st.success(f"Predicted Resource Allocation: **{prediction}**")
