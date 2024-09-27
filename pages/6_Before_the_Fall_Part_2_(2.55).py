import streamlit as st
import global_vars as gv

st.title("Before the Fall Part 2")

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/2.5.jpg")

st.subheader("Main Scenario Quests")
st.checkbox("Mask of Grief - Before the Dawn")
st.divider()
st.checkbox("Tales from the Calamity: In Louisoix's Wake")
st.markdown("[In Louisoix's Wake](https://www.finalfantasyxiv.com/anniversary/na/detail/memoir_5.html?rgn=na&lng=en)")