
# Endometriosis Lesion Detection Using machine learning

This project integrates YOLOv5, a robust object detection algorithm, with ResNet, a powerful convolutional neural network, to detect endometriosis lesions from medical images. Targeted at healthcare providers and researchers, this tool aids in early detection and diagnosis of endometriosis, supporting improved patient care and treatment planning.

Authors


## Appendix

Any additional information goes here


## Authors

- [@Frank Appedixs (Lead Developer and Researcher)](https://www.frank-towet.netlify.app)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## features
Features
Object Detection: YOLOv5 is utilized to accurately detect and localize endometriosis lesions within medical images, providing precise diagnostic support.

Classification with ResNet: ResNet is employed for lesion classification, enhancing the system's ability to distinguish between different types and stages of endometriosis.

Interactive Web Interface: Developed with Streamlit, the application offers an intuitive user interface for uploading medical images, viewing detection results, and accessing diagnostic insights.

Real-Time Processing: Enables rapid processing and analysis of medical images, facilitating timely clinical decision-making and patient consultation.

Deployment Flexibility: Deployable locally or on cloud platforms like AWS, Azure, or Google Cloud for scalable and accessible deployment options.

## documentation
## installation 
Clone the Repository:

bash
Copy code
git clone[ https://github.com/your_username/endometriosis_detection.git](https://github.com/towet/endometriosis-detection-machine-learning)
cd endometriosis_detection
Install Dependencies:

Python 3.6+ is required.
Install required packages:
bash
Copy code
pip install -r requirements.txt
Download YOLOv5 Weights:

Download pre-trained  weights from the models folder and place them in the weights directory.
Usage
Run the Streamlit Application:

bash
Copy code
streamlit run app.py
Open your web browser and navigate to http://localhost:8501 to interact with the application.
Upload Medical Images:

Use the file uploader to select and upload medical images (JPEG or PNG format).
View Detection Results:

Once the image is uploaded, the application will display the uploaded image with detected endometriosis lesions highlighted and classified.
