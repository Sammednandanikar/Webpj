import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Topper Company")

# Company introduction paragraph
content = """
Welcome to The Topper Company, where innovation meets expertise in the world of software solutions. 
Founded with a passion for cutting-edge technology, we specialize in crafting intuitive software tailored to meet the unique needs of modern businesses. 
Our team of dedicated software engineers, designers, and project managers collaborates seamlessly to deliver robust applications that redefine user experiences
and drive operational efficiency. At The Topper Company, we pride ourselves on our commitment to quality, creativity, and client satisfaction,
ensuring every line of code we write reflects our pursuit of excellence. Join us on our journey to transform ideas into powerful software solutions that propel businesses forward in the digital age.
"""

st.markdown(content)

st.subheader("Our team")

# Load data from CSV file
df = pd.read_csv("data.csv", sep=",")

# Define columns for layout
col1, col2, col3 = st.columns(3)

# Display team members in each column
for index, row in df.iterrows():
    if index < 4:
        with col1:
            st.subheader(f'{row["first name"].title()}, {row["last name"].title()}')
            st.write(row["role"])
            st.image("images/"+row["image"])
    elif index < 8:
        with col2:
            st.subheader(f'{row["first name"].title()}, {row["last name"].title()}')
            st.write(row["role"])
            st.image("images/"+row["image"])
    else:
        with col3:
            st.subheader(f'{row["first name"].title()}, {row["last name"].title()}')
            st.write(row["role"])
            st.image("images/"+row["image"])
