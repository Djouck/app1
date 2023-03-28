import streamlit as st
import functions

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my Todo App")
st.write("This App is to increasing your productivity.")

for todo in todos:
    st.checkbox(todo)

