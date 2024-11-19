import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model('traffic_sign_detector.h5')

# Dictionary to label all traffic signs classes
classes = {
    1: '🚸 Speed limit (20km/h)',
    2: '🚸 Speed limit (30km/h)',
    3: '🚸 Speed limit (50km/h)',
    4: '🚸 Speed limit (60km/h)',
    5: '🚸 Speed limit (70km/h)',
    6: '🚸 Speed limit (80km/h)',
    7: '🚸 End of speed limit (80km/h)',
    8: '🚸 Speed limit (100km/h)',
    9: '🚸 Speed limit (120km/h)',
    10: '🚫 No passing',
    11: '🚫 No passing vehicles over 3.5 tons',
    12: '⚠️ Right-of-way at intersection',
    13: '⚠️ Priority road',
    14: '⚠️ Yield',
    15: '🛑 Stop',
    16: '🚫 No vehicles',
    17: '🚫 Vehicles > 3.5 tons prohibited',
    18: '🚫 No entry',
    19: '⚠️ General caution',
    20: '⚠️ Dangerous curve left',
    21: '⚠️ Dangerous curve right',
    22: '⚠️ Double curve',
    23: '⚠️ Bumpy road',
    24: '⚠️ Slippery road',
    25: '⚠️ Road narrows on the right',
    26: '⚠️ Road work',
    27: '⚠️ Traffic signals',
    28: '⚠️ Pedestrians',
    29: '⚠️ Children crossing',
    30: '⚠️ Bicycles crossing',
    31: '⚠️ Beware of ice/snow',
    32: '⚠️ Wild animals crossing',
    33: '⚠️ End speed + passing limits',
    34: '➡️ Turn right ahead',
    35: '⬅️ Turn left ahead',
    36: '⬆️ Ahead only',
    37: '↗️ Go straight or right',
    38: '↖️ Go straight or left',
    39: '↪️ Keep right',
    40: '↩️ Keep left',
    41: '🔁 Roundabout mandatory',
    42: '⚠️ End of no passing',
    43: '⚠️ End no passing vehicles > 3.5 tons',
}

# Set page configuration
st.set_page_config(page_title="Traffic Sign Predictor", page_icon="🚦", layout="centered")

# Title and description
st.markdown(
    """
    <h1 style="text-align: center; color: #f7d6c9;">🚦 Traffic Sign Predictor 🚦</h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h3 style="text-align: center; color: #f7d6c9;">
        Upload an image of a traffic sign, and the model will predict its class.
    </h3>
    """,
    unsafe_allow_html=True,
)

# File uploader
uploaded_file = st.file_uploader("📤 Upload an image of a traffic sign:", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    try:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        # Process the image
        image = Image.open(uploaded_file)
        image = image.resize((30, 30))
        image = np.expand_dims(np.array(image), axis=0)
        
        # Predict the class
        pred = model.predict(image)
        sign_class = classes[np.argmax(pred) + 1]
        
        # Display the prediction
        st.markdown(
            f"""
            <h2 style="text-align: center; color: #ff3114; font-size: 26px; font-weight: bold;">
                🔍 Prediction: {sign_class}
            </h2>
            """,
            unsafe_allow_html=True,
        )
    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("🖼️ Please upload an image to get started.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>"
    "Developed by Rohit | Powered by 🐍 Python and 🧠 TensorFlow"
    "</div>",
    unsafe_allow_html=True,
)
