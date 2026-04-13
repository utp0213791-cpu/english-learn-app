import streamlit as st

st.title("Learn English")

st.write("Choose your English study method:")

method = st.radio(
    "Select one option:",
    ("Study with Edutubers", "Study with Online Books")
)

if method == "Study with Edutubers":
    st.header("Learn English with Edutubers")

    st.write("Recommended channels:")
    st.write("- BBC Learning English")
    st.write("- English Addict")
    st.write("- Learn English with TV Series")

    st.video("https://www.youtube.com/watch?v=JuJxV1sPbqA")

elif method == "Study with Online Books":
    st.header("Learn English with Online Books")

    st.write("Recommended books:")
    st.write("- English Grammar in Use")
    st.write("- Oxford English Grammar")
    st.write("- Cambridge English Readers")

    st.link_button("Read English Book Online",
                   "https://www.gutenberg.org")
