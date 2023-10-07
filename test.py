import requests

# Define the API endpoint
api_url = 'http://localhost:80/predict'  # Update the URL if your API is hosted elsewhere

# Replace 'YOUR_SECRET_TOKEN' with your actual authorization token
headers = {'Authorization': 'Bearer /PR?nHjHo&=L0O$<O[bR<I5}6t=*B#'}

# Specify the image file you want to test with
image_path = './test_images/cat_image.jpg'  # Replace with the actual path to your image

# Create a dictionary to hold the image data
files = {'image': open(image_path, 'rb')}

# Send the POST request to the API
response = requests.post(api_url, headers=headers, files=files)

# Check the response
if response.status_code == 200:
    result = response.json()
    print('Predicted Class:', result['class_label'])
    print('Confidence:', result['confidence'])
else:
    print('Error:', response.status_code, response.text)