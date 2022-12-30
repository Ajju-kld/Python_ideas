import tensorflow as tf
from tensorflow import keras

# Load the trained model
model = keras.models.load_model('cat_dog_model.h5')

while True:
  # Prompt the user to enter an image file
  image_path = input('Enter the path to an image file: ')

  # Load and preprocess the image
  image = keras.preprocessing.image.load_img(image_path, target_size=(64, 64))
  image = keras.preprocessing.image.img_to_array(image) / 255.0
  image = image[None, ...]

  # Use the model to make a prediction
  prediction = model.predict(image)

  # Print the prediction
  if prediction > 0.5:
    print('This image contains a cat.')
  else:
    print('This image contains a dog.')
