import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()

train_label_onehot = tf.keras.utils.to_categorical(train_label)
test_label_onehot = tf.keras.utils.to_categorical(test_label)

train_image = train_image/255
test_image = test_image/255

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), loss='categorical_crossentropy', metrics=['acc'])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
histroy = model.fit(train_image, train_label_onehot, epochs=10, validation_data=(test_image, test_label_onehot))

print(histroy.history.keys())

figure1 = plt.figure()
plt.plot(histroy.epoch, histroy.history.get('loss'), label='loss')
plt.plot(histroy.epoch, histroy.history.get('val_loss'), label='val_loss')
plt.legend()
figure2 = plt.figure()
plt.plot(histroy.epoch, histroy.history.get('acc'), label='acc')
plt.plot(histroy.epoch, histroy.history.get('val_acc'), label='val_acc')
plt.legend()
plt.show()

# predict = model.predict(test_image)
# print(predict[0],np.argmax(predict[0]))
