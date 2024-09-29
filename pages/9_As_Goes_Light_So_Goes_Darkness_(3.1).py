import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/3.1.jpg")


st.subheader("Main Scenario Quests")
st.checkbox("An Uncertain Future - As Goes Light, So Goes Darkness")

st.divider()

st.subheader("Dungeons:")
st.markdown("#### Saint Mocianne's Arboretum")
st.image("assets/Dungeon.png")
st.checkbox("An Overgrown Ambition")
st.markdown(
""" 
> Location: **The Dravanian Hinterlands (X:12.3, Y:19.6)**
>
> Quest giver: Tetchy Treasure Hunter
"""
)

st.markdown("#### Pharos Sirius (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("Things Are Getting Sirius")
st.markdown(
""" 
> Location: **Limsa Lominsa Upper Decks (X:12.7, Y:12.8)**
>
> Quest giver: Trachraet
"""
)

st.divider()

st.subheader("Alliance Raid:")
st.markdown("#### The Void Ark")
st.image("assets/Raid.png")
st.checkbox("Sky Pirates - To Rule the Skies")
st.markdown(
""" 
> Location: **The Pillars (X:14.1, Y:10.7)**
>
> Quest giver: Unquiet Trader
>
> Questline: Shadow of Mhach
"""
)

st.divider()

st.subheader("Other:")
st.checkbox("Contradicting Convictions - More than Meets the Eye")
st.markdown(
""" 
> Location: **The Pillars (X:6.2, Y:9.4)**
>
> Quest giver: Mathye
>
> Questline: Saint Endalim's Scholasticate
>
> Requirements: All of the prior Hildibrand Adventures quests
>
> Patch: 3.15
"""
)

st.divider()
st.checkbox("Tales from the Dragonsong War: Vows Unbroken")
st.markdown("[Vows Unbroken](https://na.finalfantasyxiv.com/lodestone/special/2015/short_stories/#sidestory_03)")

