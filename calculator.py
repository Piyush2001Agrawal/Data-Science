import streamlit as st
st.title("Simple Calculator")
st.markdown("This is a simple calculator app using streamlit")

c1,c2 = st.columns(2)
fnum = c1.number_input("First Number", value=0)
snum = c2.number_input("Second Number", value=0)
options =["Add", "Subtract", "Multiply", "Divide"]
choice =st.radio("Select Operation", options)

button = st.button("Calculate")

result =0
if button:
    if choice == 'Add':
        result = fnum + snum
    if choice == 'Subtract':
        result = fnum - snum
    if choice == 'Multiply':
        result = fnum * snum
    if choice == 'Divide':
        result = fnum / snum
        
st.success(f"Result:{result}")
