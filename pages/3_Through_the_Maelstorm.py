import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/2.2.jpg")

st.subheader("Main Scenario Quests")
st.checkbox("Still Waters - Through the Maelstrom")
st.divider()
st.subheader("Dungeons:")
st.markdown("#### The Lost City of Amdapor")
st.image("assets/Dungeon.png")
st.checkbox("One Night in Amdapor")
st.markdown(
""" 
> Location: **Old Gridania (X:6.0, Y:10.7)**
>
> Quest giver: E-Sumi-Yan
"""
)

#st.divider()
st.markdown("#### Halatali (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("This Time's for Fun")
st.markdown(
""" 
> Location: **Mor Dhona (X:22, Y:8)**
>
> Quest giver: Hugubert
"""
)

st.markdown("#### Brayflox's Longstop (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("Curds and Slay")
st.markdown(
""" 
> Location: **Mor Dhona (X:22.1, Y:8.7)**
>
> Quest giver: Bloezoeng
"""
)

st.divider()

st.subheader("Raid:")
st.markdown("#### The Second Coil of Bahamut")
st.image("assets/Raid.png")
st.checkbox("Another Turn in the Coil - Alisaie's Resolve")
st.markdown(
""" 
> Location: **The Waking Sands (X:6.0, Y:4.9)**
>
> Quest giver: Urianger
> 
> Questline: The Coils of Bahamut
"""
)

st.divider()
st.subheader("Other:")
st.checkbox("The Science of Deduction - The Three Collectors")
st.markdown(
""" 
> Location: **Eastern Thanalan (X:10.9, Y:16.4)**
>
> Quest giver: Ellie
>
> Questline: Hildibrand Adventures
"""
)

st.divider()
st.checkbox("Tales from the Calamity: The Sultana's Seven")
st.markdown("[The Sultana's Seven](https://www.finalfantasyxiv.com/anniversary/na/detail/memoir_2.html?rgn=na&lng=en)")