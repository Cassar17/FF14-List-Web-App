import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/3.0.jpg")


st.subheader("Main Scenario Quests")
st.checkbox("Close to Home - Sounding Out the Amphitheatre")
st.markdown("#### The Dusk Vigil")
st.image("assets/Dungeon.png")
st.checkbox("For All the Nights to Come")
st.markdown(
""" 
> Location: **Coerthas Western Highlands (X:16.9, Y:22.8)**
>
> Quest giver: Wealdtheow
>
> Level: 51
>
> Obs: This quest is the first in a questline. Although this is a blue quest, the following quests in this line are not, but they serve as the regional quests for Western Highlands.
"""
)
st.checkbox("Camp of the Convictors - Heavensward")

st.divider()

st.subheader("Dungeons:")
st.markdown("#### Neverreap")
st.image("assets/Dungeon.png")
st.checkbox("Reap What You Sow")
st.markdown(
""" 
> Location: **The Sea of Clouds (X:11.8, Y:14.8)**
>
> Quest giver: Sanu Vanu
"""
)

st.markdown("#### The Fractal Continuum")
st.image("assets/Dungeon.png")
st.checkbox("Do It for Gilly")
st.markdown(
""" 
> Location: **The Pillars (X:14.6, Y:12.2)**
>
> Quest giver: Notrelchamps
"""
)

st.divider()

st.subheader("Trials:")
st.markdown("#### The Warring Triad")
st.image("assets/Trial.png")
st.checkbox("Gods of Eld")
st.markdown(
""" 
> Location: **The Pillars (X:11.7, Y:11.5)**
>
> Quest giver: Torsefers
>
> Note: This is the introduction to the trial questline for Heavensward.
>
> Note 2: You might need to complete "Thok Around the Clock" and "The Diabolical Bismark" to progress with this questline
"""
)

st.divider()

st.subheader("Raid:")
st.markdown("#### Gordias")
st.image("assets/Raid.png")
st.checkbox("Disarmed - Enigma")
st.markdown(
""" 
> Location: **Idyllshire (X:7.5, Y:6.5)**
>
> Quest giver: Slowfix
"""
)

st.divider()

st.subheader("Other:")
st.checkbox("Keeping the Ledger")
st.markdown(
""" 
> Location: **The Pillars (X:6.2, Y:9.4)**
>
> Quest giver: Mathye
>
> Questline: Saint Endalim's Scholasticate
"""
)

st.checkbox("Toll Booty - Short Arms of the Law")
st.markdown(
""" 
> Location: **Mor Dhona (X:22.9, Y:7.0)**
>
> Quest giver: Rhesh Polaali
>
> Questline: Doman's Adventure Guild
"""
)
