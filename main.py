import pyrebase
import streamlit as st
import pandas
import email


from datetime import datetime

firebaseConfig = {
  'apiKey': "AIzaSyBcVEHxxIE2NofVoeoezfdojbree_ur7zY",
  'authDomain': "firestore-streamlit-97b82.firebaseapp.com",
  'projectId': "firestore-streamlit-97b82",
  'databaseURL': "https://firestore-streamlit-97b82-default-rtdb.asia-southeast1.firebasedatabase.app/",
  'storageBucket': "firestore-streamlit-97b82.appspot.com",
  'messagingSenderId': "497317595554",
  'appId': "1:497317595554:web:9f6c1d3840b74879bbcafb",
  'measurementId': "G-5M4C07T8QN"
};

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db=firebase.database()
storage=firebase.storage()
st.title("Bulk sms and Email Service")
st.subtitle('"Good communication is a major factor in development of a country"')
st.sidebar.title("Our Project app")
choice=st.sidebar.selectbox('Login/SignUp',['Login','Sign up'])
email=st.sidebar.text_input("Enter your email address")
password=st.sidebar.text_input("Enter your password")




if choice=="Sign up":
  handle=st.sidebar.text_input("Please enter you name",value="Default")
  submit=st.sidebar.button('Create my Account')
  if submit:
    user=auth.create_user_with_email_and_password(email,password)
    st.success("Your account is created successfully!")
    st.balloons()
    user=auth.sign_in_with_email_and_password(email,password)
    db.child(user['localId']).child("Handle").set(handle)
    db.child(user['localId']).child("Id").set(user['localId'])
    st.title("Welcome"+handle)
    st.info("Login through login option in drop down menu")
if choice == "Login":
      login = st.sidebar.checkbox('Login')
      if login:
        user = auth.sign_in_with_email_and_password(email, password)
        bio = st.radio('Jump to', ['Home', 'Sms Service', 'Email Service'])
        if bio=="Home":
          st.info("This app is designed to provide free and bulk sms and email services. Just import your file and enjoy!")
        if bio == "Email Service":
          st.title("Drop your excel file below containing user name,interest and email id")
          uploaded_file = st.file_uploader("Choose a file")
          if uploaded_file is not None:
            ef = pandas.read_excel(uploaded_file)
            for index, row in ef.iterrows():
              st.write["hello"]
             #email.send_email()
        if bio == "Sms Service":
          st.title("Drop your excel file below containing user name and mobile no.")
          uploaded_file = st.file_uploader("Choose a file")
          if uploaded_file is not None:
            st.balloons()
#
