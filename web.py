import streamlit as st
import todolist_fanctions as tf

todos = tf.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    tf.write_todos(todos)




st.title("My Todo App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="" ,placeholder="Add todo...",
                on_change=add_todo, key="new_todo")