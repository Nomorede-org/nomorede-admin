from approve_brand import update_brand_status
from login import Login
from profile import ProfilePage
import streamlit as st
from view_brand import in_review_brands
from waitlist import waitlist

# Set up the main page layout
st.set_page_config(
    page_title="Nomorede",
    page_icon="asssets/5.ico",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.nomorede.com/contactUs',
        'Report a bug': "https://www.nomorede.com/contactUs",
        'About': "One Stop Science Backed styling aggregator platform"
    }
)

# Sidebar section
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose a page", 
    ("Login", "Profile", "Waitlist","View Brands","Approved Brand","View Products","View Orders")
)

if option == "Login":
    st.title("Login Page")
    Login()

elif option == "Profile":
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        ProfilePage()

elif option == "Waitlist":
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        waitlist()
elif option=="View Brands":
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        in_review_brands()
elif option=="Approved Brand":
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        update_brand_status()
st.write("---")
st.write("Made with ❤️ using Streamlit.")