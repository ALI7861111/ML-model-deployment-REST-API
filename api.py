import io
import os
import numpy as np
from flask import Flask, request, jsonify, abort
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
from waitress import serve
import os
import tempfile
app = Flask(__name__)

# Load the pre-trained VGG16 model
model = VGG16(weights='imagenet')

# Define a function to preprocess an image for model input
def preprocess_image(image_bytes):
    # Create a temporary file to save the uploaded image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(image_bytes.read())
        temp_file_path = temp_file.name

    # Load the image from the temporary file
    img = image.load_img(temp_file_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    # Remove the temporary file
    os.remove(temp_file_path)

    return img

# Define a route for image prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Check if the 'Authorization' header is set correctly
    expected_token = '/PR?nHjHo&=L0O$<O[bR<I5}6t=*B#'  # Replace with your secret token
    auth_header = request.headers.get('Authorization')
    if auth_header is None or auth_header != f'Bearer {expected_token}':
        abort(401, 'Unauthorized')

    # Check if an image file is in the request
    if 'image' not in request.files:
        abort(400, 'No image file provided')

    # Get the image file from the request
    image_file = request.files['image']

    # Ensure the file has an allowed extension (e.g., JPEG, PNG)
    allowed_extensions = {'jpg', 'jpeg', 'png'}
    if not image_file.filename.lower().endswith(tuple(allowed_extensions)):
        abort(400, 'Unsupported file format')

    # Preprocess the image
    img = preprocess_image(io.BytesIO(image_file.read()))

    # Make predictions
    predictions = model.predict(img)
    decoded_predictions = decode_predictions(predictions, top=1)[0]

    # Get the top prediction result

    _, class_label, confidence = decoded_predictions[0]

    # Return the prediction result as JSON
    result = {
        'class_label': class_label,
        'confidence': str(confidence)
    }

    return jsonify(result)



if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80) 