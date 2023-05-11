import streamlit as st
import funicitons as fun

task_list = fun.get_tasks("todo.txt")


def add_task():
    adding = st.session_state["to_be_added"]
    if adding != "" and not (adding in task_list) and adding != ' ':
        task_list.append(adding + '\n')
        fun.write_file(task_list)
    return


def completed(task_index):
    task_list.pop(task_index)
    fun.write_file(task_list)
    return task_index


st.title("My Todo App")
st.subheader("A task scheduling app for you")
st.write("Add items here")
for index, name in enumerate(task_list):
    check_flag = st.checkbox(name, key=name)
    if check_flag:
        completed(index)
        del st.session_state[name]
        st.experimental_rerun()

task_name = st.text_input(label="input", placeholder="Add new task", on_change=add_task, key="to_be_added")
