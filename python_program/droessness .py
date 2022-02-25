import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from keras.callbacks import ModelCheckpoint

# Assuming you have a dataset of images and corresponding labels
# X should be your images, y should be the corresponding labels (0 for closed, 1 for open)

# Load and preprocess your dataset here

# Assuming X_train, X_test, y_train, y_test are your training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reshape and normalize the input images
X_train = X_train.reshape(X_train.shape[0], 24, 24, 1).astype('float32') / 255
X_test = X_test.reshape(X_test.shape[0], 24, 24, 1).astype('float32') / 255

# One-hot encode the labels
y_train = to_categorical(y_train, 2)
y_test = to_categorical(y_test, 2)

# Define the CNN model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(24, 24, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(2, activation='softmax'))  # 2 output nodes for binary classification

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# ModelCheckpoint to save the best model during training
checkpoint = ModelCheckpoint('cnncat2.h5', monitor='val_loss', save_best_only=True)

# Train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32, callbacks=[checkpoint])

# Save the trained model
model.save('cnncat2.h5')
