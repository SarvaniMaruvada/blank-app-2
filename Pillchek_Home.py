import streamlit as st
from navigation import nav_page
st.title("Pillchek") 
st.header("Your Medication Companion")
st.write("We understand that being diagnosed with a chronic illness can cause a lot of stress,\n so we're here to relieve some of that stress")
st.write("We here at Pillchek make sure that you\n always take your medication on time so you don't have to worry about it")
st.write("Sign in to get started!")
if st.button("Create an Account!"):
    nav_page("Profile_Settings")

