import streamlit as st

st.title("📝 Simple Todo App")

# Store tasks in session
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input box
task = st.text_input("Enter a task")

# Add button
if st.button("Add"):
    if task:
        st.session_state.tasks.append(task)

st.subheader("Your Tasks")

# Display tasks
for t in st.session_state.tasks:
    st.write("•", t)


st.sidebar.text_input("Add a task", key="sidebar_task")
if st.sidebar.button("Add from sidebar"):
    if st.session_state.sidebar_task:
        st.session_state.tasks.append(st.session_state.sidebar_task)    
        

st.checkbox("Show task count", key="show_count")

st.subheader("Task Count")
if st.session_state.show_count:
    st.write(f"You have {len(st.session_state.tasks)} tasks.")  
    
st.radio("Sort tasks", options=["None", "Alphabetical"], key="sort_option")
# if st.session_state.sort_option == "Alphabetical":
#     sorted_tasks = sorted(st.session_state.tasks)
#     st.subheader("Sorted Tasks")
#     for t in sorted_tasks:
#         st.write("•", t)
        
st.selectbox("Filter tasks", options=["All", "With 'a'", "With 'e'"], key="filter_option")
if st.session_state.filter_option == "With 'a'":
    filtered_tasks = [t for t in st.session_state.tasks if 'a' in t]
    st.subheader("Tasks with 'a'")
    for t in filtered_tasks:
        st.write("•", t)
        
st.button("hello world")
st.success("Task added successfully!")
