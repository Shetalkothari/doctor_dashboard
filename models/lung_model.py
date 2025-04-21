# lung_model.py

import numpy as np
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore

# Load your trained model once when the app starts
model = load_model('models/lung_cancer_model.h5')  # adjust path to your model

# Image dimensions expected by your model (change if different)
IMG_WIDTH = 224
IMG_HEIGHT = 224

def predict_lung_cancer(img_path):
    try:
        img = image.load_img(img_path, target_size=(IMG_WIDTH, IMG_HEIGHT))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # normalize

        prediction = model.predict(img_array)[0]

        # Adjust based on how your model outputs predictions
        if prediction[0] > 0.5:
            result = "⚠️ High chance of Lung Cancer detected."
        else:
            result = "✅ No significant signs of Lung Cancer detected."

        return result
    except Exception as e:
        return f"Error in prediction: {str(e)}"
