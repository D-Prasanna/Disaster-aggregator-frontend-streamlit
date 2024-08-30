import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

data = {
    'Disaster Type': ['Flood', 'Earthquake', 'Hurricane'],
    'Tweets': [1500, 1200, 800]
}
df = pd.DataFrame(data)
# st.title("Project")
st.title("Disaster Management")
st.header("Introduction")
st.write("""This is a simple Streamlit app to demonstrate basic functionalities. In the upcoming lessons, we'll build a comprehensive dashboard for disaster data aggregation""")

user_input= st.text_input("Naam dal do ","Ya pe likhana hai")

st.write("hello",user_input)

st.subheader("Sample DataFrame")
if st.button("Press me"):
    st.write(df)

image = Image.open("C:\\Users\\prasa\\Hackathon\\testing stuff\\Post-and-Grant-Avenue-Look.jpg")
st.subheader("Sample Image")
if st.button("Press me for image"):
    st.image(image, caption='Disaster Image', use_column_width=True)

st.subheader("Sample Matplotlib Chart")

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, marker='o')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sample Line Chart')

# Display the plot
st.pyplot(fig)

st.sidebar.title("Sidebar")
option = st.sidebar.selectbox(
    'Select a disaster type:',
    ('None','Flood', 'Earthquake', 'Hurricane')
)
if option=='Earthquake' or option=="Flood" or option=="Hurricane":
    st.sidebar.write(f'You selected: {option}')
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age}")
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")