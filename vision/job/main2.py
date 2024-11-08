import numpy as np
import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('roboflow.pt')

# 동영상 파일 사용시
# video_path = "path/to/your/video/file.mp4"
# cap = cv2.VideoCapture(video_path)

# webcam 사용시
cap = cv2.VideoCapture(0)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
  
    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)
        
        # Extract bounding boxes, classes, names, and confidences
        boxes = results[0].boxes.xyxy.tolist()
        classes = results[0].boxes.cls.tolist()
        names = results[0].names
        confidences = results[0].boxes.conf.tolist()

        # Iterate through the results
        for box, cls, conf in zip(boxes, classes, confidences):
            x1, y1, x2, y2 = box 
            confidence = conf
            detected_class = cls
            name = names[int(cls)]
            print("center of {} >>".format(name), "X :", ((x1+x2)/2), "Y :", ((y1+y2)/2) )
            #print("x1 :", x1, "x2 :", x2)      # 640    # from left-top
            #print("y1 :", y1, "y2 :", y2)      # 480    # to right-bottom

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
