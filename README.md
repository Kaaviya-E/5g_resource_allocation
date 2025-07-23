# 📶 5G Resource Allocation Predictor

This project is a machine learning-based predictor that estimates the optimal **Resource Allocation** (as a percentage) for 5G networks based on real-time network conditions and application usage.

Built using:
- 🧠 **Random Forest Regressor**
- 📊 **Streamlit** for UI
- 📁 CSV dataset of Quality of Service metrics
- 🧮 Features like Signal Strength, Latency, Bandwidths, Application Type

---

## 🎯 Objective

Efficient spectrum management is key in 5G systems. This tool predicts how much resource (in %) should be allocated to a user or application based on:

- Signal Strength (in dBm)
- Latency (in ms)
- Required & Allocated Bandwidth (in Mbps)
- Application Types in use (Video Call, Gaming, Emergency Services, etc.)

---

## 🖥️ Streamlit Interface

### Input Parameters:

![Streamlit UI 1](images/screenshot1.png)

- Signal Strength
- Latency
- Required Bandwidth
- Allocated Bandwidth
- Application checkboxes (e.g., Video Call, IoT, Gaming, etc.)

### Prediction Output:

![Streamlit UI 2](images/screenshot2.png)

Displays the **predicted resource allocation** percentage based on selected parameters.

---

## 📁 Project Structure

