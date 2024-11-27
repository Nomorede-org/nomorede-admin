import streamlit as st
import requests

def Login():
    with st.form("login_form"):
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")

        submitted = st.form_submit_button("Submit")
        if submitted:
            #  st.secrets["db_username"]
            payload = {"email": email, "password": password}
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }

            try:
                response = requests.post(st.secrets['general']["BACKEND_URL"]+"/user/login", json=payload, headers=headers)
                response.raise_for_status()
                if response.status_code==200:
                    if response.json()['user_type']=='admin':
                        st.session_state.partner_id=response.json()['partner_id']
                        st.session_state.email=response.json()['email']
                        st.success("Login Successful")
                else:
                    st.error("Login Failed")
            except requests.exceptions.HTTPError as e:
                # st.error(f"HTTP error occurred: {e}")
                return None
            except Exception as e:
                # st.error(f"An error occurred: {e}")
                return None

