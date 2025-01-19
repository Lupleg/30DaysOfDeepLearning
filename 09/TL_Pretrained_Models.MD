Transfer learning is a powerful technique in deep learning where a model developed for one task is reused as the starting point for a model on a second task. This is particularly useful when you have limited data for the second task. Keras provides several pretrained models, such as VGG16, ResNet, Inception, etc., which can be used for transfer learning.

Here's an example of how to use the VGG16 model pretrained on ImageNet for a new classification task:

```python
import keras
from keras.applications import VGG16
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

# Load the VGG16 model, excluding the top (fully connected) layers
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(150, 150, 3))

# Freeze the layers of the base model
for layer in base_model.layers:
    layer.trainable = False

# Build the new model on top of the base model
model = Sequential()
model.add(base_model)
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Assuming binary classification

# Compile the model
model.compile(optimizer=Adam(lr=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

# Prepare the data
train_datagen = ImageDataGenerator(rescale=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'path_to_train_data',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

validation_generator = test_datagen.flow_from_directory(
    'path_to_validation_data',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# Train the model
model.fit(
    train_generator,
    steps_per_epoch=100,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=50
)

# Evaluate the model
test_loss, test_acc = model.evaluate(validation_generator)
print('Test accuracy:', test_acc)
```

### Explanation:

1. **Loading the Pretrained Model**:

   - The `VGG16` model is loaded with weights pretrained on the ImageNet dataset. The `include_top=False` argument excludes the top fully connected layers, allowing us to add our own custom layers for the new task.

2. **Freezing the Base Model Layers**:

   - The layers of the base model are frozen to prevent them from being updated during training. This ensures that the pretrained weights are not modified.

3. **Building the New Model**:

   - A new `Sequential` model is created, and the base model is added to it.
   - A `Flatten` layer is added to convert the 3D output of the base model to 1D.
   - A `Dense` layer with 256 units and ReLU activation is added.
   - A final `Dense` layer with a single unit and sigmoid activation is added for binary classification.

4. **Compiling the Model**:

   - The model is compiled with the Adam optimizer, binary cross-entropy loss, and accuracy as the metric.

5. **Preparing the Data**:

   - `ImageDataGenerator` is used to preprocess the images and augment the training data.
   - `train_generator` and `validation_generator` are created to load the training and validation data from directories.

6. **Training the Model**:

   - The model is trained using the `fit` method, with the training and validation generators.

7. **Evaluating the Model**:
   - The model is evaluated on the validation data to determine its accuracy.

This example demonstrates how to leverage a pretrained model like VGG16 for a new classification task using transfer learning in Keras. This approach can significantly reduce training time and improve performance, especially when you have limited data for the new task.
