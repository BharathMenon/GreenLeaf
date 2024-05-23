import streamlit as st
from pages import main_page, pot_class,corn_class,tomato_class,tea_class

PAGES = {
    "Main Page": main_page,
    "Potato Leaf Disease Classification": pot_class,
    "Corn Leaf Disease Classification": corn_class,
    "Tomato Leaf Disease Classification":tomato_class,
    "Tea Leaf Disease Classification":tea_class
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.main()