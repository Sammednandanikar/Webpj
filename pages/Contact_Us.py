import streamlit as st
from send_email import send_email
import pandas
df = pandas.read_csv("topics.csv")

st.header("Conatct me")
with st.form(key="my_form"):
    user_email = st.text_input("Your email address")
    option = st.selectbox(
        'What topic do you want to discuss?',
        df["topic"])
    raw_message = st.text_area("Your Message")
    message= f"""
    subject: New email from {user_email}
    Topic: {option}
    From:   {user_email},
    {raw_message}"""
    button = st.form_submit_button("submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your Email was sent succesfully")