import streamlit as st
import cv2
import numpy as np

st.title('Image processing App')

image = st.file_uploader('Upload an image', type=['jpg', 'png', 'jpeg'])

if image is not None:
    a = np.asarray(bytearray(image.read()), dtype=np.uint8)
    img = cv2.imdecode(a, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    st.image(img_rgb)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    st.image(img_gray)

    _ , enc = cv2.imencode('.jpg', img_gray)
    st.download_button('Download B&W Image', enc.tobytes(), 'bw_image.jpg', 'image/jpeg')