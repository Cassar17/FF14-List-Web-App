import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/2.1.jpg")


st.subheader("Main Scenario Quests")
st.checkbox("The Price of Principles - Build on the Stone")
st.divider()
st.subheader("Dungeons:")
st.markdown("#### Pharos Sirius")
st.image("assets/Dungeon.png")
st.checkbox("Sirius Business - Why So Sirius")
st.markdown(
""" 
> Location: **Western La Noscea (X:26.5, Y:26.7)**
>
> Quest giver: Diamanda
"""
)

#st.divider()
st.markdown("#### Copperbell Mines (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("Out of Sight, Out of Mine")
st.markdown(
""" 
> Location: **Mor Dhona (X:22, Y:8.7)**
>
> Quest giver: Hugubert
"""
)

st.markdown("#### Haukke Manor (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("Maniac Manor")
st.markdown(
""" 
> Location: **Mor Dhona (X:22.1, Y:8.6)**
>
> Quest giver: Lauriane
"""
)
st.divider()
st.subheader("Alliance Raid:")
st.markdown("#### The Labyrinth of the Ancients")
st.image("assets/Raid.png")
st.checkbox("Legacy of Allag - For Prosperity")
st.markdown(
""" 
> Location: **Mor Dhona (X:21.8, Y:8.1)**
>
> Quest giver: Outlandish Man
>
> Questline: The Crystal Tower
"""
)
st.divider()
st.subheader("Other:")
#st.image(r"assets\Raid.png")
st.checkbox("The Rise and Fall of Gentlemen - The Immaculate Deception")
st.markdown(
""" 
> Location: **Ul'dah - Steps of Nald (X:9.8, Y:8.7)**
>
> Quest giver: Wymond
>
> Questline: Hildibrand Adventures
"""
)
st.divider()
st.checkbox("Tales from the Calamity: Where Victory and Glory Lead")
st.markdown("[Where Victory and Glory Lead](https://www.finalfantasyxiv.com/anniversary/na/detail/memoir_1.html?rgn=na&lng=en)")