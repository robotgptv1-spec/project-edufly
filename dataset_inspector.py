import os
import cv2 
DATASET_PATH = "D:/edufly/cricketer_cnn/Indian Cricketers Image"
valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]
valid_extensions = (".jpg", ".jpeg", ".png", ".webp")


def inspect_dataset():

    total_images = 0

    for player in os.listdir(DATASET_PATH):

        player_path = os.path.join(DATASET_PATH, player)

        if not os.path.isdir(player_path):
            continue

        valid_count = 0
        corrupted_count = 0

        for filename in os.listdir(player_path):

            if not filename.lower().endswith(valid_extensions):
                continue

            image_path = os.path.join(player_path, filename)

            image = cv2.imread(image_path)

            if image is None:
                corrupted_count += 1
            else:
                valid_count += 1

        total_images += valid_count

        print(f"\nPlayer: {player}")
        print(f"Valid Images: {valid_count}")
        print(f"Corrupted Images: {corrupted_count}")

    print("\n==========================")
    print("Total Valid Images:", total_images)


if __name__ == "__main__":
    inspect_dataset()
