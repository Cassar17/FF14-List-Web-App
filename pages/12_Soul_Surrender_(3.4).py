import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/3.4.jpg")

st.subheader("Main Scenario Quests")
st.checkbox("Promises Kept - An Ending to Mark a New Beginning")

st.divider()

st.subheader("Dungeons:")
st.markdown("#### The Great Gubal Library (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("Let Me Gubal That for You")
st.markdown(
""" 
> Location: **Idyllshire (X:5.5, Y:6.6)**
>
> Quest giver: Midnight Dew
"""
)

st.divider()

st.subheader("Raid:")
st.markdown("#### The Creator")
st.image("assets/Raid.png")
st.checkbox("The Coeurl and the Colossus - Of Endings and Beginnings")
st.markdown(
""" 
> Location: **The Dravanian Hinterlands (X:21.7, Y:18.8)**
>
> Quest giver: Mide
"""
)

st.divider()

st.subheader("Trials:")
st.markdown("#### Containment Bay P1T6")
st.image("assets/Trial.png")
st.checkbox("The Fate of Stars")
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
st.subheader("Deep Dungeon:")
st.markdown("#### Palace of the Dead")
st.image("assets/Deep_Dungeon.png")
st.checkbox("What Lies Beneath - Dead but not Gone")
st.markdown(
""" 
> Location: **New Gridania (X:12.0, Y:13.1)**
>
> Quest giver: Palace of the Dead
>
> Patch: 3.45
>
> Note: This questline unlocks the remaining floors of Palace of the Dead
"""
)

st.divider()
st.subheader("Other:")
st.checkbox("Divine Reckoning - Finding Ulaa")
st.markdown(
""" 
> Location: **The Pillars (X:8.7, Y:7.9)**
>
> Quest giver: Briardien
>
> Questline: Saint Endalim's Scholasticate
>
"""
)

st.checkbox("A Gazebo to Call Our Own - Don't Trust Anyone over Sixty")
st.markdown(
""" 
> Location: **Foundation (X:9.9, Y:11.4)**
>
> Quest giver: Cyr
>
> Questline: Further Hildibrand Adventures
>
"""
)

st.divider()
st.checkbox("Tales from the Dragonsong War: The Dreamer and the Dream")
st.markdown("[The Dreamer and the Dream](https://na.finalfantasyxiv.com/lodestone/special/2015/short_stories/#sidestory_02)")