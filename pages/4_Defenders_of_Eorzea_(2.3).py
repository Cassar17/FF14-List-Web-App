import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/2.3.jpg")

st.subheader("Main Scenario Quests")
st.checkbox("The Great Divide - Brave New Companions")

st.divider()
st.subheader("Dungeons:")
st.markdown("#### Hullbreaker Isle")
st.image("assets/Dungeon.png")
st.checkbox("King of the Hull")
st.markdown(
""" 
> Location: **Mor Dhona (X:22.1, Y:8.7)**
>
> Quest giver: Bloezoeng
"""
)

#st.divider()
st.markdown("#### The Tam-Tara Deepcroft (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("Corpse Groom")
st.markdown(
""" 
> Location: **Ul'dah - Steps of Nald (X:12.2, Y:8.1)**
>
> Quest giver: Paiyo Reiyo
"""
)

st.markdown("#### The Stone Vigil (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("Blood for Stone")
st.markdown(
""" 
> Location: **Mor Dhona (X:21.9, Y:8.4)**
>
> Quest giver: Faillicie
"""
)

st.divider()

st.subheader("Alliance Raid:")
st.markdown("#### Syrcus Tower")
st.image("assets/Raid.png")
st.checkbox("Syrcus Tower")
st.markdown(
""" 
> Location: **Mor Dhona (X:30.4, Y:12.1)**
>
> Quest giver: Rammbroes
> 
> Questline: The Crystal Tower
"""
)

st.divider()
st.subheader("Other:")
st.checkbox("The Business of Betrothal - A Case of Indecency")
st.markdown(
""" 
> Location: **Western Thanalan (X:13.0, Y:14.1)**
>
> Quest giver: Ellie
>
> Questline: Hildibrand Adventures
"""
)

st.checkbox("Of Errant Epistles - Of Siblings and Side-whiskers")
st.markdown(
""" 
> Location: **Mor Dhona (X:30.4, Y:13.7)**
>
> Quest giver: Klynthota
>
> Questline: Delivery Moogle
"""
)

st.checkbox("Magiteknical Difficulties")
st.markdown(
""" 
> Location: **Mor Dhona (X:21.9, Y:7.8**
>
> Quest giver: Slafborn
"""
)

st.checkbox("The Greatest Story Never Told")
st.markdown(
""" 
> Location: **Western Thanalan (X:18.3, Y:17.4)**
>
> Quest giver: Valiant Hart
>
> Note: This is a complicated riddle quest, for which you can find the solution [here](https://ffxiv.consolegameswiki.com/wiki/The_Greatest_Story_Never_Told)
"""
)

st.divider()
st.checkbox("Tales from the Calamity: Of Friends Lost and Found")
st.markdown("[Of Friends Lost and Found](https://www.finalfantasyxiv.com/anniversary/na/detail/memoir_3.html?rgn=na&lng=en)")