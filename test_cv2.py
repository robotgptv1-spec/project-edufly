
import cv2

print("OpenCV Version:", cv2.__version__)

print("CascadeClassifier available:",
      hasattr(cv2, "CascadeClassifier"))

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

print("Detector loaded:", not face_detector.empty())
