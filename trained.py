import tensorflow as tf
from tensorflow import keras

# Load the dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.cats_vs_dogs.load_data()

# Preprocess the data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build the model
model = keras.Sequential([
  keras.layers.Flatten(input_shape=(64, 64, 3)),
  keras.layers.Dense(128, activation='relu'),
  keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

