import cv2
import face_recognition
import os
import csv
from datetime import datetime, timedelta
import numpy as np

# Function to load images and encode them
def loadEncodeImages(images_folder):
    images = []
    id = []
    for image_name in os.listdir(images_folder):
        if image_name.endswith(".jpg") or image_name.endswith(".png"):
            image_path = os.path.join(images_folder, image_name)
            image = face_recognition.load_image_file(image_path)
            image_encoding = face_recognition.face_encodings(image)[0]
            images.append(image_encoding)
            id.append(image_name.split('.')[0])
    return images, id

# Function to check if ID exists in employees record
def check_employee_id(employee_id, employees_record_file):
    with open(employees_record_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == employee_id:
                return row['name']
    return None

# Function to input data in a CSV file
def enter_data(csv_file, data):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['id', 'name', 'time', 'date'])
        writer.writerow(data)

# Required folders
images_folder = 'images'
employees_record_file = 'employees_record.csv'
camera_record_file = 'camera_record.csv'
known_face_encodings, known_face_ids = loadEncodeImages(images_folder)


video_capture = cv2.VideoCapture('')

# To store last recorded time for each person
last_recorded_times = {}

# Minimum time difference threshold (in seconds)
min_time_threshold = 30 


#Frame skip factor
skip_frames = 5 
frame_counter = 0

while True:
    ret, frame = video_capture.read()
    if not ret:
        break  # Exit loop if no frame is read (end of video)
    frame_counter += 1
    if frame_counter % skip_frames != 0:
        continue  # Skip this frame

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        employee_id = None

        if True in matches:
            first_match_index = matches.index(True)
            employee_id = known_face_ids[first_match_index]
            name = check_employee_id(employee_id, employees_record_file)
            
            # Check last recorded time for this person
            if employee_id in last_recorded_times:
                last_recorded_time = last_recorded_times[employee_id]
                elapsed_time = datetime.now() - last_recorded_time
                if elapsed_time.total_seconds() < min_time_threshold:
                    continue

            # Update last recorded time for this person
            last_recorded_times[employee_id] = datetime.now()

        else:
            employee_id = str(len(known_face_ids) + 1)
            known_face_encodings.append(face_encoding)
            known_face_ids.append(employee_id)

            # Crop the face from the frame
            top, right, bottom, left = face_location
            face_image = frame[top:bottom, left:right]

            # Save the cropped face image
            new_image_path = os.path.join(images_folder, f"{employee_id}.jpg")
            cv2.imwrite(new_image_path, face_image)

            with open(employees_record_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([employee_id, "Unknown"])
            
            # No match found, assign new ID and record the time
            last_recorded_times[employee_id] = datetime.now()
            

        now = datetime.now()
        time_string = now.strftime("%H:%M:%S")
        date_string = now.strftime("%Y-%m-%d")
        enter_data(camera_record_file, [employee_id, name, time_string, date_string])

        # Draw rectangle around the face and label it
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

video_capture.release()
cv2.destroyAllWindows()
