from pathlib import Path

import tensorflow as tf

MODEL_PATH = "cricket_cnn.keras"
CLASS_DIR = Path(__file__).resolve().parent / "detected_faces"
IMG_SIZE = (224, 224)

model = tf.keras.models.load_model(MODEL_PATH)
class_names = sorted(
    path.name for path in CLASS_DIR.iterdir() if path.is_dir()
)


def predict(image_path: str) -> str:
    """Return the predicted cricketer name for an image."""
    image = tf.keras.utils.load_img(image_path, target_size=IMG_SIZE)
    image_array = tf.keras.utils.img_to_array(image)
    predictions = model.predict(tf.expand_dims(image_array, axis=0), verbose=0)
    predicted_index = int(tf.argmax(predictions[0]).numpy())
    return class_names[predicted_index]

print(predict("D:/edufly/cricketer_cnn/detected_faces/Ravindra Jadeja/Image_18_0.jpg"))