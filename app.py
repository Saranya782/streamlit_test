
import streamlit as st

# 1. Basic Text Elements
st.title("Streamlit App")
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a text')
st.write('This is also a text using write')

# 2. Text Input
user_input = st.text_input('Write your text')
st.write(user_input)

# 3. Number Input
num_input = st.number_input('Enter your number')
st.write('Your number is ', num_input)

# 4. File and Button Widgets
file_input = st.file_uploader('Upload your file')
st.button('Submit')

# 5. Radio Buttons
choice = st.radio('Choose an option', ['Option 1', 'Option 2'])

# 6. Camera Input
image = st.camera_input('Smile please')

# 7. Colorful Text using Streamlit's Markdown syntax
st.write(":rainbow[this is rainbow text]")
st.write(":green[this is green text]")