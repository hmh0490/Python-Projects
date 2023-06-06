# run in terminal: streamlit run todoWebApp.py
import streamlit as st
import functions

todos = functions.get_todos()
# grab todo from inputbox
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# oder matters; if subheader code is above title code, it will be above on the webpage as well
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

# each time the webpage is reloaded, the code is executed from top to bottom
# to more user you have, the more CPU and RAM you need from the host

# st.session_state