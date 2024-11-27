import streamlit as st
import requests

def waitlist():
    st.title("Join Waitlist")

    # User inputs for skip and limit parameters
    skip = st.number_input("Skip:", min_value=0, value=0, step=1)
    limit = st.number_input("Limit:", min_value=1, value=10, step=1)

    if st.button("Fetch Waitlist Data"):
        # Construct the URL properly (ensure no + symbol)
        base_url = st.secrets['general']['BACKEND_URL']
        url = f"{base_url}/admin/view/joinWaitlist?skip={skip}&limit={limit}"
        
        headers = {'accept': 'application/json'}

        # Make the API request
        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()  # Parse JSON response
                if data:
                    st.subheader("Waitlist Data")
                    st.write(data)  # Optionally, use `st.json(data)` for formatted view
                else:
                    st.warning("No data found.")
            else:
                st.error(f"Failed to fetch data. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
