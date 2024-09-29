import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/2.5.jpg")

st.subheader("Main Scenario Quests")
st.checkbox("Good Intentions - ???")
st.markdown(
"""
> Obs: The final quest of this patch has a spoiler in its title. Therefore, the title of the quest *before* that is "An Uninvited Ascian". 
"""
)

st.divider()
st.subheader("Dungeons:")
st.markdown("#### The Wanderer's Palace (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("Not Easy Being Green")
st.markdown(
""" 
> Location: **Mor Dhona (X:22.1, Y:8.7)**
>
> Quest giver: Bloezoeng
"""
)

#st.divider()
st.markdown("#### Amdapor Keep (Hard)")
st.image("assets/Dungeon.png")
st.checkbox("For Keep's Sake")
st.markdown(
""" 
> Location: **Mor Dhona (X:22.1, Y:8.6)**
>
> Quest giver: Lauriane
"""
)

st.divider()

st.subheader("Alliance Raid:")
st.markdown("#### The World of Darkness")
st.image("assets/Raid.png")
st.checkbox("The World of Darkness - The Light of Hope")
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
st.subheader("Trials:")
st.markdown("#### Urth's Fount")
st.image("assets/Trial.png")
st.checkbox("Fear and Odin in the Shroud")
st.markdown(
""" 
> Location: **New Gridania (X:9.9, Y:11.4)**
>
> Quest giver: Scarlet
>
> Note: Even though not marked as an Extreme trial, this fight is considered to be in the same level of difficulty. It is recommended to find a party through party finder, or do it unsynced.
"""
)

st.divider()
st.subheader("Other:")
st.checkbox("Thanks For Your Support - Hostages to Fortune")
st.markdown(
""" 
> Location: **Limsa Lominsa Lower Decks (X:10.4, Y:11.3)**
>
> Quest giver: Deputy Postmoogle
>
> Questline: Delivery Moogle
"""
)

st.checkbox("Shades of Sil'dih - Her Last Vow")
st.markdown(
""" 
> Location: **Ul'dah - Steps of Thal (X:9.8, Y:11.2)**
>
> Quest giver: Ellie
>
> Questline: Hildibrand Adventures
"""
)

st.checkbox("A Qiqirn Always Pays His Debts - The Hazy Professor")
st.markdown(
""" 
> Location: **Limsa Lominsa Lower Decks (X:10.4, Y:11.3)**
>
> Quest giver: Deputy Postmoogle
>
> Questline: Delivery Moogle
>
> Patch: 2.51
"""
)

st.checkbox("Blues on Emerald Avenue - The Little Postmoogle That Could")
st.markdown(
""" 
> Location: **Limsa Lominsa Lower Decks (X:10.4, Y:11.3)**
>
> Quest giver: Deputy Postmoogle
>
> Questline: Delivery Moogle
>
> Patch: 2.55
>
> Note: Even though this is a 2.55 patch quest, it is recommended to do it before getting into 2.55 MSQ.
"""
)
