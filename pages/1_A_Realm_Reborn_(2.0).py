import streamlit as st
import global_vars as gv

if (not gv.hide_images):
    st.image("assets/KeyArts/Widescreen/2.0.jpg")



st.subheader("Main Scenario Quests")
st.checkbox("Close to Home - Dressed to deceive")
st.markdown("#### Halatali")
st.image("assets/Dungeon.png")
st.checkbox("Hallo Halatali")
st.markdown(
""" 
> Location: **Western Thanalan (X:12.0, Y:14.3)**
>
> Quest giver: Nedrick Ironheart
"""
)
st.markdown("#### The Sunken Temple of Qarn")
st.image("assets/Dungeon.png")
st.checkbox("At level 35: Braving New Depths")
st.markdown(
""" 
> Location: **Western Thanalan (X:12, Y:14)**
>
> Quest giver: Nedrick Ironheart
"""
)
st.markdown("#### Cutter's Cry")
st.image("assets/Dungeon.png")
st.checkbox("At level 38: Dishonor Before Death")
st.markdown(
""" 
> Location: **Ul'dah - Steps of Thal (X:14, Y:10)**
>
> Quest giver: Sibold
"""
)
st.markdown("#### Dzemael Darkhold")
st.image("assets/Dungeon.png")
st.checkbox("At level 44: Fort of Fear")
st.markdown(
""" 
> Location: **Coerthas Central Highlands (X:24.7, Y:28.8)**
>
> Quest giver: Carrilaut
"""
)
st.markdown("#### The Aurum Vale")
st.image("assets/Dungeon.png")
st.checkbox("At level 47: Going for Gold")
st.markdown(
""" 
> Location: **Western Thanalan (X:12.0, Y:14.3)**
>
> Quest giver: Nedrick Ironheart
"""
)
st.checkbox("Your current MSQ - The Ultimate Weapon")

st.divider()

st.subheader("Dungeons:")
st.markdown("#### The Wanderer's Palace")
st.image("assets/Dungeon.png")
st.checkbox("Trauma Queen")
st.markdown(
""" 
> Location: **Western Thanalan (X:11.4, Y:13.9)**
>
> Quest giver: Allene
"""
)
st.markdown("#### Amdapor Keep")
st.image("assets/Dungeon.png")
st.checkbox("Ghosts of Amdapor")
st.markdown(
""" 
> Location: **Western Thanalan (X:12, Y:14)**
>
> Quest giver: Nedrick Ironheart
>
> Requirement: The Aurum Vale cleared
"""
)

st.divider()

st.subheader("Trials:")
st.markdown("#### The Primals Hard Mode")
st.image("assets/Trial.png")
st.checkbox("A Recurring Problem - In a Titan Spot")
st.markdown(
""" 
> Location: **The Waking Sands (X:6.9, Y:6.1)**
>
> Quest giver: Minfilia Warde
>
> Note: This is the entire trial questline for A Realm Reborn. It can be done all at once in this patch, or you can choose to do them later.
"""
)

st.divider()

st.subheader("Miscellaneous:")
st.checkbox("All You Wanted to Know about Odin")
st.markdown(
""" 
> Location: **South Shroud (X:25.6, Y:21.0)**
>
> Quest giver: Simmie
>
> Note: This quest is necessary for another quest in the future
"""
)
st.checkbox("Fungal Frolic - In Too Deep")
st.markdown(
""" 
> Location: **Central Shroud (X:16.6, Y:18.6)**
>
> Quest giver: Hobriaut
>
> Note: This quest is necessary for another quest in the future
"""
)
st.checkbox("Doing the Dirty Work")
st.markdown(
""" 
> Location: **Central Shroud (X:16.5, Y:18.6)**
>
> Quest giver: Marcette
>
> Requirement: Fungal Frolic
>
> Note: This quest is necessary for another quest in the future
"""
)

st.divider()

st.subheader("Raid:")
st.markdown("#### The Binding Coil of Bahamut")
st.image("assets/Raid.png")
st.checkbox("Primal Awakening - Alisaie's Pledge")
st.markdown(
""" 
> Location: **The Waking Sands (X:6.0, Y:4.9)**
>
> Quest giver: Urianger
>
> Questline: The Coils of Bahamut
"""
)