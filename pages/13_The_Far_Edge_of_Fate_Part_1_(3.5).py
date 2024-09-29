import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/3.5.jpg")

st.subheader("Main Scenario Quests")
st.checkbox("Tidings From Gyr Abania - Luisoix's Finest Student")

st.divider()

st.subheader("Dungeons:")
st.markdown("#### Sohm Al (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("The Fires of Sohm Al")
st.markdown(
""" 
> Location: **Idyllshire (X:4.6, Y:8.4)**
>
> Quest giver: Gossamer Moogle
"""
)

st.divider()

st.subheader("Alliance Raid:")
st.markdown("#### Dun Scaith")
st.image("assets/Raid.png")
st.checkbox("Where Shadows Reign - A Redbill Farewell")
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
st.markdown("#### Containment Bay Z1T9")
st.image("assets/Trial.png")
st.checkbox("The Last Pillar to Fall")
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
st.checkbox("The Student Body's Revenge - ???")
st.markdown(
""" 
> Location: **The Pillars (X:8.7, Y:7.9)**
>
> Quest giver: Briardien
>
> Questline: Saint Endalim's Scholasticate
>
> Note: The final quest of this questline has a spoiler in its title. The final quest starts with "The Life..."
"""
)

st.checkbox("The Proud and the Pointy-eyed - If I Could Turn Back Time")
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
st.checkbox("Tales from the Dragonsong War: Words, Deeds, Beliefs")
st.markdown("[Words, Deeds, Beliefs](https://na.finalfantasyxiv.com/lodestone/special/2016/short_stories/#short_stories_06)")