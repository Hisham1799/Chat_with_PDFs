import streamlit as st

st.write("Hello World")
x = st.text_input("Favourite Movie?")
st.write(f"Your Favourite movie is {x}")

st.button("Test")
st.markdown("Hey **Hisham**!")
st.header("This is the header")
st.subheader("This is the subheader")
st.code("import streamlit as st")
import datetime
import streamlit as st

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)

import streamlit as st

with open("flower.png", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name="flower.png",
        mime="image/png",
    )

    import streamlit as st
st.image("flower.png", caption="Flower")