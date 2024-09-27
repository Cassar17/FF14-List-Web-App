import streamlit as st
import global_vars as gv

st.set_page_config(
    page_title="Home",
    page_icon="XIV"
)

st.title("The List")
st.subheader("Config")

gv.show_images = st.checkbox("Hide patch key arts", value=gv.show_images) 

print(gv.show_images)

#st.sidebar.success("Select a page!")