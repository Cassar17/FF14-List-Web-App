import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/3.5.jpg")

st.subheader("Main Scenario Quests")
st.checkbox("The Obvious Solution - The Far Edge of Fate")
st.divider()
st.checkbox("Tales from the Dragonsong War: Thoughts Unspoken")
st.markdown("[Thoughts Unspoken](https://na.finalfantasyxiv.com/lodestone/special/2016/short_stories/#sidestory_08)")