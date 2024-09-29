import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/3.2.jpg")

st.subheader("Main Scenario Quests")
st.checkbox("As It Once Was - Causes and Costs")

st.divider()

st.subheader("Dungeons:")
st.markdown("#### The Lost City of Amdapor (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("One More Night in Amdapor")
st.markdown(
""" 
> Location: **Old Gridania (X:6.0, Y:10.6)**
>
> Quest giver: E-Sumi-Yan
"""
)

st.divider()

st.subheader("Raid:")
st.markdown("#### Midas")
st.image("assets/Raid.png")
st.checkbox("Rearmed - A Gob in the Machine")
st.markdown(
""" 
> Location: **The Dravanian Hinterlands (X:21, Y:18)**
>
> Quest giver: Roundrox
"""
)

st.divider()

st.subheader("Trials:")
st.markdown("#### Containment Bay S1T7")
st.image("assets/Trial.png")
st.checkbox("When the Bough Wakes")
st.markdown(
""" 
> Location: **The Rising Stones (X:6, Y:5)**
>
> Quest giver: Unukalhai
>
> Questline: The Warring Triad
"""
)

st.divider()

st.subheader("Other:")
st.checkbox("A Gentleman Falls, Rather than Flies - Don't Call It a Comeback")
st.markdown(
""" 
> Location: **The Pillars (X:5.9, Y:9.9)**
>
> Quest giver: Nashu Mhakaracca
>
> Questline: Further Hildibrand Adventures
>
"""
)

st.divider()
st.checkbox("Tales from the Dragonsong War: Through Fire and Blood")
st.markdown("[Through Fire and Blood](https://na.finalfantasyxiv.com/lodestone/special/2015/short_stories/#sidestory_01)")