# Flask Image Classification REST API

A Flask-based REST API that uses a pre-trained VGG16 model on ImageNet to perform image classification. This API accepts image files, predicts the class label, and returns the confidence score.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)


## Getting Started

### Prerequisites

Before you begin, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- Keras
- Pillow

You can install these dependencies using the provided `requirements.txt` file.

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/flask-image-classification.git

2. Navgiate to the directory

    ```
    cd flask-image-classification

3.Install the required packages using pip:
    ```
    pip install -r requirements.txt

## Usage

1. Start the Flask API server:
    ```
    python app.py

2. Make POST requests to the /predict endpoint to classify images. Include the Authorization header with the bearer token.

## API ENDPOINT :

POST /predict: Upload an image for classification. The request should include the following:

Authorization header with a bearer token.
image file field containing the image to be classified.
Example request using Python's requests library:

```
import requests

api_url = 'http://localhost:5000/predict'
headers = {'Authorization': 'Bearer YOUR_SECRET_TOKEN'}
files = {'image': open('path_to_image.jpg', 'rb')}
response = requests.post(api_url, headers=headers, files=files)




