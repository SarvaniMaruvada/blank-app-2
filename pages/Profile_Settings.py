import streamlit as st
from navigation import nav_page

#Sign up page

st.title("Pillchek")
st.header("Your Medication Companion")
user_name = st.text_input("Create a unique User Name", "")
email_name = st.text_input("Enter your email here", "")
option = st.selectbox("How many medications do you take?", 
     ['1', '2', '3', '4','5', '6+'])
st.write("You take ", option, "medication(s) a day")
options = st.multiselect("Choose the time(s) that you take your medication(s)", 
            ['12 - 1 AM', '1 - 2 AM', '2 - 3 AM', '3 - 4 AM', '4 - 5 AM', '5 - 6 AM', 
            '6 - 7 AM', '7 - 8 AM','8 - 9 AM', ' 9 - 10 AM','10 - 11 AM','11 AM - 12 PM',
            '12 - 1 PM', '1 - 2 PM', '2 - 3 PM', '3 - 4 PM', '4 - 5 PM', '5 - 6 PM',
            '6 - 7 PM', '7 - 8 PM', '8 - 9 PM', '9 - 10 PM', '10 - 11 PM', ' 11 PM - 12 AM'])
options2 = st.multiselect("Choose the days you take your medication", ['Monday', 'Tuesday', 'Wednesday',
                          'Thursday', 'Friday', 'Saturday', 'Sunday'])
if st.checkbox("Agree to recieve notifications"):
     if st.button("Create Your Schedule"):
          st.write("Your Schedule is")
          st.write(options2)
          st.write("at")
          st.write(options)





