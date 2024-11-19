# 🚗 **Traffic Sign Recognition System using Deep Learning**

## 📝 **Project Description**
This project aims to develop a **Traffic Sign Recognition System** using deep learning techniques to classify various traffic signs. The system utilizes a **Convolutional Neural Network (CNN)** model built with TensorFlow/Keras to recognize 43 different types of traffic signs. This system is crucial for **autonomous vehicles** as it can help them understand road signs, ensuring safer and more efficient driving.

## 🛠 **Technologies Used**
- **Python** 🐍
- **TensorFlow/Keras** 🧠
- **OpenCV** 📷
- **NumPy** 🧮
- **Pandas** 📊
- **Matplotlib** 📈
- **Scikit-learn** 🔍

## 🚀 **How It Works**
1. **Dataset**: The model is trained on the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset, which consists of images from 43 different classes of traffic signs.
2. **Data Preprocessing**: Images are resized to 30×30 pixels and normalized for better performance.
3. **Model Architecture**: A **CNN** architecture with multiple convolutional and pooling layers is used to extract features and classify the traffic signs.
4. **Training**: The model is trained for 20 epochs, achieving 94% accuracy on the training dataset and 95% on the test dataset.
5. **Testing**: After training, the model is evaluated on a test dataset to predict the traffic signs, achieving impressive accuracy.
6. **Deployment**: The model is saved as `traffic_sign_detector.h5`, ready for deployment in real-time applications.


## 📥 **How to Run**
### 1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/Traffic-Sign-Recognition.git
cd Traffic-Sign-Recognition
```

### 2. **Install the required libraries:**
```
pip install -r requirements.txt
```
### 3. **Run the Jupyter Notebook to train the model:**
```
jupyter notebook traffic_sign_recognition.ipynb
```

### 4. **Run the Traffic Sign Classifier:**
Use the trained model (traffic_sign_detector.h5) to classify traffic signs in your images. You can deploy the model as a web application using Streamlit or Flask or Tkinter.

### 📊 **Model Performance**
- Training Accuracy: 94%
- Test Accuracy: 95%
- The model was trained with 20 epochs on a dataset containing 43 classes of traffic signs.

### 💡 **Future Work**
- Increase model accuracy by experimenting with different architectures and hyperparameters.
- Extend the system for real-time traffic sign detection using a webcam or video feed.

📄 References
- Dataset: [Kaggle - GTSRB Dataset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)
- TensorFlow: https://www.tensorflow.org
- Keras: https://keras.io

### 🙋‍♂️ **Contact**
Feel free to reach out if you have any questions or suggestions!
