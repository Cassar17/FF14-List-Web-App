import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/3.3.jpg")

st.subheader("Main Scenario Quests")
st.checkbox("The Man Within - Litany of Peace")

st.divider()

st.subheader("Dungeons:")
st.markdown("#### Hullbreaker Isle (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("Storming the Hull")
st.markdown(
""" 
> Location: **Limsa Lominsa Upper Decks (X:11.0, Y:10.4)**
>
> Quest giver: Denston
"""
)

st.divider()

st.subheader("Alliance Raid:")
st.markdown("#### The Weeping City of Mhach")
st.image("assets/Raid.png")
st.checkbox("The Weeping City - Freedom for Our Skies")
st.markdown(
""" 
> Location: **The Sea of Clouds (X:6.2, Y:5.8)**
>
> Quest giver: Stacia
>
> Questline: Shadow of Mhach
"""
)

st.divider()

st.subheader("Trials:")
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
st.checkbox("The House that Death Built - The Nightmare's End")
st.markdown(
""" 
> Location: **New Gridania (X:12.0, Y:13.1)**
>
> Quest giver: Palace of the Dead
>
> Patch: 3.35
"""
)

st.divider()
st.subheader("Other:")
st.checkbox("The Paths We Walk - The Burdens We Bear")
st.markdown(
""" 
> Location: **Fortemps Manor (X:6.0, Y:6.0)**
>
> Quest giver: House Fortemps Manservant
>
> Questline: Tales of the Dragonsong War
>
"""
)

st.checkbox("The Gigi Situation - The Measure of a Mammet")
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
st.checkbox("Tales from the Dragonsong War: What Remains of a Knight")
st.markdown("[What Remains of a Knight](https://na.finalfantasyxiv.com/lodestone/special/2016/short_stories/#sidestory_05)")