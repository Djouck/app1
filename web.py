import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my Todo App")
st.write("This App is to increasing your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


st.session_state
