import os 
import csv 
import cv2
import numpy as np
INPUT_DIR = "D:/edufly/cricketer_cnn/Indian Cricketers Image"
OUTPUT_DIR = "D:/edufly/cricketer_cnn/preprocessed_images"
IMAGE_SIZE = (224, 224)  # Resize images to 224x224 pixels
VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

def preprocess_images(Image_path):
    image = cv2.imread(Image_path)
    if image is None:
        return None
    image = cv2.resize(image, IMAGE_SIZE)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype(np.float32) / 255.0  # Normalize to [0, 1]
    return image

def process_dataset():
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total_processed = 0
    total_failed = 0

    for player in os.listdir(INPUT_DIR):

        player_path = os.path.join(INPUT_DIR, player)

        if not os.path.isdir(player_path):
            continue

        output_player_path = os.path.join(
            OUTPUT_DIR,
            player
        )

        os.makedirs(output_player_path, exist_ok=True)

        for filename in os.listdir(player_path):

            if not filename.lower().endswith(
                VALID_EXTENSIONS
            ):
                continue

            image_path = os.path.join(
                player_path,
                filename
            )

            processed = preprocess_images(image_path)

            if processed is None:
                total_failed += 1
                continue

            # Convert normalized RGB back to uint8
            save_image = (
                processed * 255
            ).clip(0, 255).astype(np.uint8)

            # OpenCV saves BGR
            save_image = cv2.cvtColor(
                save_image,
                cv2.COLOR_RGB2BGR
            )

            output_path = os.path.join(
                output_player_path,
                os.path.splitext(filename)[0] + ".jpg"
            )

            success = cv2.imwrite(
                output_path,
                save_image
            )

            if success:
                total_processed += 1
            else:
                total_failed += 1

    print("\n===== PREPROCESSING REPORT =====")
    print("Processed Images:", total_processed)
    print("Failed Images:", total_failed)


if __name__ == "__main__":
    process_dataset()
