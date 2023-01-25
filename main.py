import streamlit as st
import pandas


data = {
  "Names":['Qui Gon Jinn', 'Mace Windu', 'Plo koon', 'Obi-Wan', 'Yoda'],
  "More_names":["Anikan", "Vader","Padme", "Luke", "Leia"]
}

df = pandas.DataFrame(data)
st.title('My First Streamlit App')
st.subheader('An Introduction To Asing Streamlit')
st.write("""
This is my first web app
This is going to be FUN!
""")
st.write(df)
st.line_chart(df)