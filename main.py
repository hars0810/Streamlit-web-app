import streamlit as st

st.title("Compass")

name = st.text_input("Enter your name")
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
age = st.number_input("Enter your age", min_value=1, max_value=120)


uploaded_image_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_image_file is not None: 
    st.write("Image uploaded")
    st.image(uploaded_image_file)

# CSS to change button background color and hover effect, and remove focus effect
css = """
<style>
div.stButton > button {
    background-color: #4CAF50; /* Green */
    color: black;
}

div.stButton > button:hover {
    background-color: #3e8e41; /* Darker Green */
    color: black;
}

div.stButton > button:focus {
    background-color: #4CAF50; /* Green */
    color: white;
    outline: none;
    box-shadow: none;
}
</style>
"""

# Inject CSS
st.markdown(css, unsafe_allow_html=True)

if st.button("Calculate Probability"):
    st.write("Probability is... ")



