import streamlit as st
import requests
import json
from datetime import datetime

def update_brand_status():
    st.title("Update Brand Status")


    url = st.secrets['general']['BACKEND_URL']+"/admin/brand/status"
    # Streamlit form for user input
    with st.form(key="brand_status_form"):
        # Input fields for each attribute
        brand_id = st.text_input("Brand ID")  # Default to "string" for now
        comment = st.text_input("Comment")  # Default to "string" for now
        status = st.selectbox("Status", ["approved", "rejected", ], index=0)  # Status options
        updated_by = "ADMIN"  # Default to "string" for now
        
        # Format the current date and time for updated_at field
        updated_at = st.text_input("Updated At", value=datetime.utcnow().isoformat())

        # Submit button
        submit_button = st.form_submit_button(label="Submit")

    # When the form is submitted, make the POST request
    if submit_button:
        # Prepare the payload
        payload = {
            "brand_id": brand_id,
            "comment": comment,
            "status": status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        # Headers for the POST request
        headers = {
            "Content-Type": "application/json",
        }

        # Make the POST request
        try:
            response = requests.post(url, headers=headers, json=payload)
            
            # Check if the request was successful
            if response.status_code == 200:
                st.success("Brand status updated successfully!")
                st.json(response.json())  # Display the response as JSON
            else:
                st.error(f"Failed to update brand status: {response.status_code}")
                st.write(response.text)  # Display error message
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
