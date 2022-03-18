import pyrebase
import streamlit as st
import pandas
from pyrebase import initialize_app
from PIL import Image
import sms
from io import BytesIO
import xlsxwriter
output = BytesIO()
import bulk_email



img=Image.open('icon_image.jpg')
st.set_page_config(page_title="Email and Sms Service",page_icon=img)
firebaseConfig = {
  'apiKey': "AIzaSyBcVEHxxIE2NofVoeoezfdojbree_ur7zY",
  'authDomain': "firestore-streamlit-97b82.firebaseapp.com",
  'projectId': "firestore-streamlit-97b82",
  'databaseURL': "https://firestore-streamlit-97b82-default-rtdb.asia-southeast1.firebasedatabase.app/",
  'storageBucket': "firestore-streamlit-97b82.appspot.com",
  'messagingSenderId': "497317595554",
  'appId': "1:497317595554:web:9f6c1d3840b74879bbcafb",
  'measurementId': "G-5M4C07T8QN"
}

firebase= initialize_app(firebaseConfig)
auth=firebase.auth()
db=firebase.database()
storage=firebase.storage()
st.title("Bulk Sms and Email Services")
st.subheader('"Good communication is a major factor in development of a country"')
st.info("Sign Up/Login to start using the services in Beta Mode")
col1, col2, col3 = st.columns(3)
with col2:
  image = Image.open('india connected.jpg')
  st.image(image, caption='Making communication stronger')
st.sidebar.title("WELCOME!")
choice=st.sidebar.selectbox('Login/SignUp',['Login','Sign up'])
email=st.sidebar.text_input("Enter your email address")
password=st.sidebar.text_input("Enter your password",type="password")
hide_menu_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)




if choice=="Sign up":
  handle=st.sidebar.text_input("Please enter your nickname",value="Ojas")
  submit=st.sidebar.button('Create my Account')
  if submit:
    try:
      user=auth.create_user_with_email_and_password(email,password)
      st.success("Your account is created successfully!")
      st.balloons()
      user = auth.sign_in_with_email_and_password(email, password)
      db.child(user['localId']).child("Handle").set(handle)
      db.child(user['localId']).child("Id").set(user['localId'])
      st.title("Welcome " + handle + " !")
    except:
      st.info("This account already exists !")

    st.info("Login through login option in the left drop down menu to use the services")
if choice == "Login":
      login = st.sidebar.checkbox('Login')
      if login:
        try:
          user = auth.sign_in_with_email_and_password(email, password)
          bio = st.radio('Jump to', ['Home', 'Sms Service', 'Email Service'])
          st.write('<style>div.row-widget.stRadio > div {flex-direction:row;}</style>',unsafe_allow_html=True)
          if bio == "Home":
            st.info(
              "This app is designed to provide free and bulk sms and email services. Just import your file and enjoy!")
          if bio == "Email Service":
            image2 = Image.open('bulk email.jpg')
            st.image(image2, caption='Bulk email in a click')
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            worksheet = workbook.add_worksheet()

            worksheet.write('A1', 'Name')
            worksheet.write('B1', 'Surname')
            worksheet.write('C1', 'number')
            worksheet.write('D1', 'Interest')
            worksheet.write('E1', 'Email')
            workbook.close()


            st.title("Download,fill and drop the excel file below ")
            secret = "once"
            uploaded_file = st.file_uploader("Choose a file", key=secret)

            st.download_button(
              label="Click to download Excel template file to fill and upload",
              data=output.getvalue(),
              file_name="template.xlsx",
              mime="application/vnd.ms-excel"
            )

            if uploaded_file is not None:
              ef = pandas.read_excel(uploaded_file)
              for index, row in ef.iterrows():
                bulk_email.send_email(row)
                st.write("Emails sent successfully")
                secret = "done"
                state = st.session_state['key'] = secret

          if bio == "Sms Service":
            image3 = Image.open('bulk sms.jpg')
            st.image(image3, caption='Bulk SMS in a click')
            workbook1 = xlsxwriter.Workbook(output, {'in_memory': True})
            worksheet1 = workbook1.add_worksheet()

            worksheet1.write('A1', 'number')
            workbook1.close()


            title = st.text_input('Enter the special code for using this service in the box  below',)
            if title == "PLEASE":

              msg = st.text_input('Enter your message for the receiver in the box  below')

              st.title("Drop your excel file below containing  mobile nos. in vertical column")
              secret = "fun"
              uploaded_file1 = st.file_uploader("Choose a file", key=secret)
              st.download_button(
                label="Click to download Excel template file to fill and upload",
                data=output.getvalue(),
                file_name="template.xlsx",
                mime="application/vnd.ms-excel"
              )
              if uploaded_file1 is not None:
                st.balloons()
                num = ""
                gf = pandas.read_excel(uploaded_file1)
                for index, row in gf.iterrows():
                  a = str(row['number']
                          )
                  num += a + ','
                l = len(num)
                num = num[:l - 1]
                sms.bulk_sms(num, msg)
                st.write("sms sent successfully")
                secret = "fun_over"
                state = st.session_state['key'] = secret
            elif  title!="":
              st.info("Incorrect Special Code. Contact the developer to know this Special Code!")

        except:
          st.info("Enter a valid email/password !")


