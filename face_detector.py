import os
import cv2 
INPUT_DIR = "D:/edufly/cricketer_cnn/preprocessed_images"
OUTPUT_DIR = "D:/edufly/cricketer_cnn/detected_faces"
face_detect_path = "haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +face_detect_path)

def detect_faces(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60)
    )
    return image , faces


def process_data():
    total_faces = 0
    for player in os.listdir(INPUT_DIR):
        player_path = os.path.join(INPUT_DIR,player)
        if not os.path.isdir(player_path):
            continue
        output_path = os.path.join(OUTPUT_DIR,player)
        os.makedirs(output_path,exist_ok=True)
        
        for filename in os.listdir(player_path):
    
            if not filename.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            ):
                continue

            image_path = os.path.join(
                player_path, filename
            )

            image, faces = detect_faces(image_path)

            if image is None:
                continue

            for index, (x, y, w, h) in enumerate(faces):

                face = image[y:y+h, x:x+w]

                face = cv2.resize(face, (224, 224))

                save_name = (
                    f"{os.path.splitext(filename)[0]}_"
                    f"{index}.jpg"
                )

                save_path = os.path.join(
                    output_path, save_name
                )

                if cv2.imwrite(save_path, face):
                    total_faces += 1

    print("Total detected faces:", total_faces)
    
    
if __name__ == "__main__":
    process_data()