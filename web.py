import streamlit as st
import todolist_fanctions as tf

todos = tf.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append("\n"+todo)
    tf.write_todos(todos)

st.title("My Todo App")

st.text_input(label="" ,placeholder="Add todo...",
                on_change=add_todo, key="new_todo")


for index, todo in enumerate(todos):
    if todo == "\n":
        todos.pop(index)
        tf.write_todos(todos)
        st.experimental_rerun()
    chackbox = st.checkbox(todo, key=index)
    if chackbox:
        todos.pop(index)
        tf.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.session_state