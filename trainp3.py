
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_path = "dataset/train"
val_path = "dataset/val"

base = EfficientNetB0(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
x = GlobalAveragePooling2D()(base.output)
output = Dense(10, activation='softmax')(x)  # Change 10 to your num_classes
model = Model(inputs=base.input, outputs=output)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1./255)
train = train_datagen.flow_from_directory(train_path, target_size=(224, 224), batch_size=32)
val = train_datagen.flow_from_directory(val_path, target_size=(224, 224), batch_size=32)

model.fit(train, validation_data=val, epochs=10)
model.save("traffic_sign_model.h5")
