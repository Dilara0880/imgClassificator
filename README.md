## Image Classification Service

This is a web service for image classification. Users can upload an image, and the service will classify the image and display the result, including the image dimensions and the predicted class.

### Installation
1. Clone the repository:
`git clone git@github.com:Dilara0880/imgClassificator.git`
2. Navigate to the project directory
3. Create a virtual environment (recommended):
`python3 -m venv venv`
4. Activate the virtual environment:
`source venv/bin/activate`
5. Install the dependencies:
`pip install -r requirements.txt`
6. Start the server:
`uvicorn main:app --reload`
7. Open your web browser and go to http://127.0.0.1:8000
8. You will see the homepage where you can upload an image
9. Click on the "Выбрать файл" button and select an image file from your local machine
10. Click on the "Загрузить изображение" button to upload the image

After the upload, the service will classify the image and display the result on a new page. The result will include the width and height of the image, as well as the predicted class.

To upload another image, you can go back to the homepage by clicking the "Upload a new image" button or by accessing http://127.0.0.1:8000 again.

### Configuration
The service uses a pre-trained ResNet-50 model for image classification. The class labels are obtained from the ImageNet dataset. The main.py file contains the necessary code for loading the model and performing the classification.

### Credits
This service uses the following libraries and frameworks:

- [FastAPI](https://fastapi.tiangolo.com)
- [PyTorch](https://pytorch.org)
- [torchvision](https://pytorch.org/vision) (pre-trained ResNet-50 model and the ImageNet class)
- [PIL](https://pillow.readthedocs.io)
- [requests](https://docs.python-requests.org)
