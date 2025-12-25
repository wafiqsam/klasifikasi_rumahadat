import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input as mobilenet_preprocess
from tensorflow.keras.applications.efficientnet import preprocess_input as efficientnet_preprocess

# CONFIG
st.set_page_config(
    page_title="Klasifikasi Rumah Adat",
    layout="centered"
)

st.title("Klasifikasi Rumah Adat Indonesia")
st.write("CNN & Transfer Learning (MobileNetV2, EfficientNetB0)")

# LOAD MODELS
@st.cache_resource
def load_models():
    cnn = tf.keras.models.load_model("cnn_rumah_adat.h5")
    mobilenet = tf.keras.models.load_model("mobilenetv2_rumah_adat.h5")
    efficientnet = tf.keras.models.load_model("efficientnet_rumah_adat.h5")
    return cnn, mobilenet, efficientnet

cnn_model, mobilenet_model, efficientnet_model = load_models()


# CLASS LABELS
class_names = ['gadang', 'honai', 'joglo', 'panjang', 'tongkonan']


# MODEL SELECTION
model_option = st.selectbox(
    "Pilih Model",
    ("CNN", "MobileNetV2", "EfficientNetB0")
)

# IMAGE UPLOAD
uploaded_file = st.file_uploader(
    "Upload gambar rumah adat",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Gambar Input", use_column_width=True)

    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # PREPROCESSING
    if model_option == "CNN":
        img_array = img_array / 255.0
        model = cnn_model

    elif model_option == "MobileNetV2":
        img_array = mobilenet_preprocess(img_array)
        model = mobilenet_model

    else:  # EfficientNetB0
        img_array = efficientnet_preprocess(img_array)
        model = efficientnet_model

    # PREDICTION
    pred = model.predict(img_array)
    confidence = np.max(pred) * 100
    predicted_class = class_names[np.argmax(pred)]

    # OUTPUT
    st.success(f"**Prediksi: {predicted_class.upper()}**")
    st.info(f"Tingkat Kepercayaan: **{confidence:.2f}%**")
