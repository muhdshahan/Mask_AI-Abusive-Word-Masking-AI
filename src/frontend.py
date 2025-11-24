""" Streamlit file for a frontend view to the user """

import streamlit as st
from train import is_toxic, mask_abusive_words

st.set_page_config(page_title="Mask AI", page_icon="🛡️")
st.title("🛡️ Toxic Text Masker")
st.write("Enter any text below, and abusive/toxic words will be masked.")

# user input
user_input = st.text_area("Enter text here:")

# Threshold input
threshold = st.slider("Toxicity threshold:", min_value=0.0, max_value=1.0, value=0.6, step=0.05)

# Detect & mask
if st.button("Check toxicity and Mask"):
    if not user_input.strip():
        st.warning("Please enter some text!")
    else:
        cleaned_text = mask_abusive_words(user_input, threshold)
        toxic_flag = is_toxic(user_input, threshold)

        st.subheader("Results")
        st.write(f" Original Text: {user_input}")
        st.write(f"**Is Toxic:** {toxic_flag}")
        st.write(f"**Cleaned Text:** {cleaned_text}")
