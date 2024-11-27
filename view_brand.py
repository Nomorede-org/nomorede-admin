import streamlit as st
import requests
import pandas as pd


# def get_user_details(user_id):
#     """Fetch user data based on the brand's user ID."""
#     try:
#         response = requests.get(st.secrets['general']['BACKEND_URL'] + f"/user/profile/{user_id}")
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"Failed to fetch user data. Status code: {response.status_code}")
#             return {}
#     except requests.exceptions.RequestException as e:
#         st.error(f"Error fetching user details: {e}")
#         return {}

# def fetch_in_review_brands(skip, limit):
#     """Fetches in-review brands from the API."""
#     try:
#         base_url = st.secrets['general']['BACKEND_URL']
#         url = f"{base_url}/admin/brand/inreview?skip={skip}&limit={limit}"
#         headers = {'accept': 'application/json'}

#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"Failed to fetch in-review brands. Status code: {response.status_code}")
#             return None
#     except requests.exceptions.RequestException as e:
#         st.error(f"Error fetching brands: {e}")
#         return None

# def show_brand_details(brand):
#     """Displays the details of the selected brand."""
#     user_details = get_user_details(brand['_id'])  # Corrected user_id reference

#     if user_details:
#         st.subheader(f"Brand: {user_details.get('brand_name', 'N/A')}")
#         st.write("**Company Name:**", user_details.get('company_name', 'N/A'))
#         st.write("**Brand Website:**", user_details.get('brand_website', 'N/A'))
#         st.write("**Description:**", user_details.get('description', 'N/A'))
#         st.write("**Account Status:**", user_details.get('account_status', 'N/A'))

#         # Contact Information
#         contact_info = user_details.get('contact_info', {})
#         if 'address' in contact_info:
#             for addr in contact_info['address']:
#                 st.write("**Address:**", addr.get('street_address', 'N/A'), 
#                          addr.get('city', 'N/A'), addr.get('state', 'N/A'), 
#                          addr.get('country', 'N/A'), addr.get('postal_code', 'N/A'))
#         if 'mobile_number' in contact_info:
#             st.write("**Mobile Number:**", contact_info['mobile_number'].get('mobile_number', 'N/A'))

#         # Bank Details
#         bank_details = user_details.get('bank_details', {})
#         if bank_details:
#             st.write("**Bank Account Holder:**", bank_details.get('account_holder_name', 'N/A'))
#             st.write("**IFSC Code:**", bank_details.get('ifsc_code', 'N/A'))
#             st.write("**Account Type:**", bank_details.get('account_type', 'N/A'))
#             # st.write("**Cancelled Cheque**",bank_details.get('cancel_cheque'))

#         # Social Media
#         social_media = user_details.get('social_media', {})
#         st.write("**Facebook:**", social_media.get('facebook', 'N/A'))
#         st.write("**Twitter:**", social_media.get('twitter', 'N/A'))
#         st.write("**Instagram:**", social_media.get('instagram', 'N/A'))

#         # Verification Details
#         verification = user_details.get('varification_details', {})
#         if verification:
#             st.write("**GST Number:**", verification.get('gst_no', 'N/A'))
#             st.write("**PAN Card:**", verification.get('pan_card', 'N/A'))
#             # st.image(verification.get('document_url'), caption="Verification Document")
#             # st.image(verification.get('sign_url'), caption="Signature")

def in_review_brands():
    st.title("In-Review Brands")
    API_URL = st.secrets['general']['BACKEND_URL']+"/get-brands/"
    try:
        response = requests.get(API_URL)
        # print(response)
        if response.status_code == 200:
            data = response.json()
            # print(data)
            # Convert the data into a DataFrame
            brands_df = pd.DataFrame(data)  # Adjust based on JSON structure if necessary
            # Filter necessary columns
            print(brands_df)
            display_columns = ['_id', 'first_name','brand_name','company_name', 'account_status', 'isVarified']
            if not set(display_columns).issubset(brands_df.columns):
                st.error("Some required columns are missing in the API response.")
            else:
                brands_df = brands_df[display_columns]
                # Display the table
                st.dataframe(brands_df, use_container_width=True)
        else:
            st.error(f"Failed to fetch data: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
