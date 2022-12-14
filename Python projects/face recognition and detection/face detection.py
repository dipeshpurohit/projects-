#Face detection
import cv2
import mediapipe as mp

# mediapipe to detect faces and show accuracy score
mp_detector = mp.solutions.face_detection
# Load the cascade
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# To capture video from webcam.
cap = cv2.VideoCapture(0)
with mp_detector.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while True:
        # Read the frame
        ret, image = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)
        # Convert the BGR image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Process the image and find faces
        results = face_detection.process(image)
        # Convert the image color back so it can be displayed
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Display the accuracy score
        if results.detections:
            for id, detection in enumerate(results.detections):
                print(id, detection)
                bBox = detection.location_data.relative_bounding_box
                w, h, b = image.shape
                boundBox = int(bBox.xmin * w), int(bBox.ymin * h), int(bBox.width * w), int(bBox.height *h)
                cv2.putText(image, f'{int(detection.score[0] * 100)}%', (boundBox[0], boundBox[1] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        # Draw the rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Display the live feed
        cv2.imshow('Detection', image)
        # Press esc to stop
        if cv2.waitKey(5) & 0xFF == 27:
            break
# Release the VideoCapture object
cap.release()
