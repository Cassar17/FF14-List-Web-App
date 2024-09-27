import streamlit as st
import global_vars as gv
from st_pages import hide_pages


st.title("The List")
st.subheader("Config")
latest_patch = []


gv.hide_images = st.checkbox("Hide patch key arts", value=gv.hide_images)
gv.hide_titles = st.checkbox("Hide future patch titles", value=gv.hide_titles)
if (gv.hide_titles):
    latest_patch = st.selectbox("Select your patch...",["2.0","2.1","2.2","2.3","2.4","2.5","3.0","3.1","3.2","3.3","3.4","3.5","4.0","4.1","4.2","4.3","4.4","4.5","5.0","5.1","5.2","5.3","5.4","5.5","6.0","6.1","6.2","6.3","6.4","6.5","7.0"])

pages_to_hide = []
if (len(latest_patch) > 0):
    pages_to_hide = gv.pages_list.copy()
    count = 0
    for patch in gv.pages_list:
        if latest_patch not in patch:
            pages_to_hide.remove(patch)
            count += 1
        else:
            pages_to_hide.remove(patch)
            if (".5" in latest_patch):
                pages_to_hide.pop(0)
            break
    hide_pages(pages_to_hide)
else:
    hide_pages([])

#st.sidebar.success("Select a page!")