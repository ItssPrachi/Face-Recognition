"C:\Users\Prachi Verma\OneDrive\Pictures\Screen Recording 2024-07-12 135557 - Face Detection - Copy.mp4"
# Face Recognition System 🧠🎯

A real-time face recognition system developed using Python, OpenCV, and MySQL. This project was completed as part of my summer internship at **HAL – Transport Aircraft Division**, aimed at enhancing surveillance by identifying authorized personnel through facial recognition.

## 🚀 Features

- 📷 **Live Face Detection:** Real-time face detection via webcam using Haar Cascade classifiers
- 🧑‍💻 **Dataset Generator:** Automatically collects and stores grayscale cropped face images in a structured format
- 🤖 **Face Recognition Module:** Classifies known vs. unknown faces using a trained LBPH (Local Binary Pattern Histogram) model
- 🗃️ **MySQL Integration:** Saves user metadata and attendance records in a backend MySQL database
- 🔐 **Authorization System:** Identifies and logs unauthorized access attempts

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Pillow
- MySQL
- Tkinter (for GUI, if applicable)

## 📁 Project Structure

Face-Recognition/
│
├── dataset/ # Grayscale cropped face images
├── trainer/ # Trained model data
├── attendance.csv # Attendance log file
├── create_dataset.py # Module to capture and store face images
├── train_model.py # Script to train LBPH classifier
├── recognizer.py # Main recognition app (with webcam stream)
├── database_config.py # MySQL connection script
└── README.md # Project documentation

## 🧪 How to Run

1. **Install dependencies:**
   ```bash
   pip install opencv-python numpy pillow mysql-connector-python
python create_dataset.py
python train_model.py
python recognizer.py
Prachi Verma
📍 Kanpur, India
📧 prachi4426verma@gmail.com
🔗 LinkedIn • GitHub
