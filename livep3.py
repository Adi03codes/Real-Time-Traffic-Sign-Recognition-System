
import cv2
import tensorflow as tf
import numpy as np

interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

labels = ["Stop", "Yield", "Speed Limit", "Turn Left", "Turn Right", "No Entry", "Pedestrian", "Rail Crossing", "Roundabout", "School Zone"]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, (224, 224))
    input_data = np.expand_dims(img / 255.0, axis=0).astype(np.float32)

    interpreter.set_tensor(input_index, input_data)
    interpreter.invoke()
    output = interpreter.get_tensor(output_index)
    pred = np.argmax(output[0])
    confidence = np.max(output[0])

    label_text = f"{labels[pred]} ({confidence:.2f})"
    cv2.putText(frame, label_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Traffic Sign Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
