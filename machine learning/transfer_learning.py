'''
- fecha: 2022-10-08 || Autor: Josué Huamán
- codigo separado por los bloques del codigo original para seguir un orden. 
- para el entrenamiento ver la esta documentacion https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit
  ya que es una forma especial de pasar datos a una red para el entrenamiento.
- ya se sabe que modelo usar, que pasos tener, como lograr el mejor rendimiento. Lo unico que falta es hacer el procesamiento puro. 
  Para eso es este codigo (parafrasear nuevamente para que se entienda mejor)

math: bath mini, bath, and stocastic
https://towardsdatascience.com/the-math-behind-gradient-descent-and-backpropagation-code-example-in-java-using-deeplearning4j-f7340f137ca5

diference between bath mini, bath, and stocastic
https://www.youtube.com/watch?v=IU5fuoYBTAM
'''
# ########################
# FIRST STEP: FEATURE EXTRACTION
# ########################
# ----------------------- import the libraries that will be used
import os
import tensorflow as tf

# ----------------------- load train set
_URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
path_to_zip = tf.keras.utils.get_file('cats_and_dogs.zip', origin=_URL, extract=True)
PATH = os.path.join(os.path.dirname(path_to_zip), 'cats_and_dogs_filtered')

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')

BATCH_SIZE = 32
IMG_SIZE = (160, 160)

train_dataset = tf.keras.utils.image_dataset_from_directory(train_dir,
                                                            shuffle=True,
                                                            batch_size=BATCH_SIZE,
                                                            image_size=IMG_SIZE)

# ----------------------- load validation stet
validation_dataset = tf.keras.utils.image_dataset_from_directory(validation_dir,
                                                                 shuffle=True,
                                                                 batch_size=BATCH_SIZE,
                                                                 image_size=IMG_SIZE)
    
# -----------------------
class_names = train_dataset.class_names

# ----------------------- split validation into test and validation set
val_batches = tf.data.experimental.cardinality(validation_dataset)
test_dataset = validation_dataset.take(val_batches // 5)
validation_dataset = validation_dataset.skip(val_batches // 5)

# ----------------------- improve time of training using prefetching
AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)
test_dataset = test_dataset.prefetch(buffer_size=AUTOTUNE)

# ----------------------- create sequential model for data augmentation
data_augmentation = tf.keras.Sequential([
  tf.keras.layers.RandomFlip('horizontal'),
  tf.keras.layers.RandomRotation(0.2),
])

# ----------------------- create scale layer
preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input

# ----------------------- load mobilenet network
# Create the base model from the pre-trained model MobileNetV2
IMG_SHAPE = IMG_SIZE + (3,)
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                               include_top=False,
                                               weights='imagenet')

# ----------------------- all the weights and biases of the imagenet model will not be modified
base_model.trainable = False

# ----------------------- create shrink layer
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()

# ----------------------- create last layer
prediction_layer = tf.keras.layers.Dense(1)

# ----------------------- now create graph model
inputs = tf.keras.Input(shape=(160, 160, 3))
x = data_augmentation(inputs)
x = preprocess_input(x)
x = base_model(x, training=False)
x = global_average_layer(x)
x = tf.keras.layers.Dropout(0.2)(x) # -- drops 20% of the connections between the global_average_layer and prediction_layer layers.
outputs = prediction_layer(x)
model = tf.keras.Model(inputs, outputs)

# ----------------------- first: compile
base_learning_rate = 0.0001
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])
  
# ----------------------- set total epochs
initial_epochs = 10

# ----------------------- second: train 
history = model.fit(train_dataset,
                    epochs=initial_epochs,
                    validation_data=validation_dataset)


# ########################
# SECOND STEP: FINE TUNNING
# ########################

# ----------------------- now we are going to train some layers of the mobilnet network
base_model.trainable = True

# ----------------------- there 154 layers in the model. We are going to train only 54 of them
# Fine-tune from this layer onwards
fine_tune_at = 100

# Freeze all the layers before the `fine_tune_at` layer
for layer in base_model.layers[:fine_tune_at]:
  layer.trainable = False

# ----------------------- first: compile
model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              optimizer = tf.keras.optimizers.RMSprop(learning_rate=base_learning_rate/10),
              metrics=['accuracy'])

# ----------------------- second: train 
fine_tune_epochs = 10
total_epochs =  initial_epochs + fine_tune_epochs

history_fine = model.fit(train_dataset,
                         epochs=total_epochs,
                         initial_epoch=history.epoch[-1],
                         validation_data=validation_dataset)

# ----------------------- third: predict (we are going to predict using batches of data)
# Retrieve a batch of images from the test set
image_batch, label_batch = test_dataset.as_numpy_iterator().next()
predictions = model.predict_on_batch(image_batch).flatten()

# Apply a sigmoid since our model returns logits
predictions = tf.nn.sigmoid(predictions)
predictions = tf.where(predictions < 0.5, 0, 1)

print('Predictions:\n', predictions.numpy())
print('Labels:\n', label_batch)
