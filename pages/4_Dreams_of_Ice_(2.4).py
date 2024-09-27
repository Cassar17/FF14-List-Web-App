import streamlit as st
import global_vars as gv

col1, col2 = st.columns(2)

if (not gv.show_images):
    st.image(r"assets\KeyArts\Widescreen\2.4.jpg")



st.subheader("Main Scenario Quests")
st.checkbox("Traitor in the Midst - Let Us Cling Together")
st.divider()
st.subheader("Dungeons:")
st.markdown("#### Sastasha (Hard)")
st.image(r"assets\Dungeon.png")
st.checkbox("It's Definitely Pirates")
st.markdown(
""" 
> Location: **Mor Dhona (X:22.1, Y:8.7)**
>
> Quest giver: Bloezoeng
>
> Unlocks: Sastasha (Hard)
"""
)

#st.divider()
st.markdown("#### The Sunkern Temple of Qarn (Hard)")
st.image(r"assets\Dungeon.png")
st.checkbox("The Wrath of Qarn")
st.markdown(
""" 
> Location: **Mor Dhona (X:22, Y:8.7)**
>
> Quest giver: Hugubert
>
> Unlocks: The Sunkern Temple of Qarn (Hard)
"""
)
st.divider()
st.subheader("Raid:")
st.markdown("#### The Final Coil of Bahamut")
st.image(r"assets\Raid.png")
st.checkbox("Fragments of Truth - Alisaie's Path")
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
#st.image(r"assets\Raid.png")
st.checkbox("Death of a Mailman - Duel Personalities")
st.markdown(
""" 
> Location: **Limsa Lominsa Lower Decks (X:10.4, Y:11.3)**
>
> Quest giver: Deputy Postmoogle
>
> Questline: Delivery Moogle
"""
)
st.checkbox("Eight-armed and Dangerous - The Coliseum Conundrum")
st.markdown(
""" 
> Location: **Eastern La Noscea (X:32.0, Y:30.4)**
>
> Quest giver: Ellie
>
> Questline: Hildibrand Adventures
"""
)
st.checkbox("Lone Survivor - The Past is a Storye we Never Tell")
st.markdown(
""" 
> Location: **Limsa Lominsa Lower Decks (X:10.4, Y:11.3)**
>
> Quest giver: Deputy Postmoogle
>
> Questline: Delivery Moogle
>
> Patch: 2.45
"""
)
st.divider()
st.checkbox("Tales from the Calamity: The Walker's Path")
st.markdown("[The Walker's Path](https://www.finalfantasyxiv.com/anniversary/na/detail/memoir_4.html?rgn=na&lng=en)")