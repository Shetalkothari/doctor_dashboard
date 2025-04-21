from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense # type: ignore

# Create a simple dummy CNN model
model = Sequential([
    Conv2D(8, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')  # binary classification
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Save the dummy model
model.save("models/lung_cancer_model.h5")  # or "lung_cancer_model.h5" if you want it in the base dir
print("Dummy model created and saved!")
