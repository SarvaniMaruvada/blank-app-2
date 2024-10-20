

import streamlit as st
#Sign up page
st.title("Pillchek")
st.header("Your Medication Company")
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

st.write(options)
st.write("You selected: ")
for i in options: 
    st.write('\t', i)

radio_val = st.radio("Select the language we are usiong", 
         ('none', 'python', 'java','C++'))
st.write("You selected: ", radio_val)

if st.button("Finish"):
    st.write("Welcome to your personal Pillchek experience", user_name,)

#Home Page  
st.title("Pillchek") 
st.header("Your Medication Company")
st.write("We understand that being diagnosed with a chronic illness can cause a lot of stress,\n so we're here to relieve some of that stress")
st.write("We here at Pillchek make sure that you\n always take your medication on time so you don't have to worry about it")

#Your profile page
#Make the profile settings customizable
#This includes things like when they take the medication or how many
#medications they take in the day as well as notification settings
