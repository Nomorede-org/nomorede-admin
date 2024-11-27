import streamlit as st
import requests

def ProfilePage():
    st.title("Profile Page")
    response = requests.get(st.secrets['general']["BACKEND_URL"]+f"/user/profile/{st.session_state.partner_id}")
    data = response.json()
    
    st.image(data["profile_picture"], width=100)
    st.write(f"First Name: {data['first_name']}")
    st.write(f"Last Name: {data['last_name']}")
    st.write(f"Email: {data['email']}")
    st.write(f"Phone: {data['mobile_number']}")