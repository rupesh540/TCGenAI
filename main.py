import langchain_helper
import streamlit as st

head = '<p style="font-family:Courier; color:Blue; font-size: 40px;"><b>TCGenAI</b></p>'
st.markdown(head, unsafe_allow_html=True)

top_title = '<p style="font-family:Courier; color:Blue; font-size: 30px;"><b>Test Case Generator</b></p>'
st.markdown(top_title, unsafe_allow_html=True)

small_title = '<p style="font-family:sans-serif; color:Blue; font-size: 15px;"><i>Generate test cases on the fly...</i></p>'
st.markdown(small_title, unsafe_allow_html=True)

domain = st.sidebar.selectbox("Select Domain or Industry", ("Insurance", "TTH", "Banking", "Others"))
functionality = st.sidebar.text_input("Functionality Name")
number = st.sidebar.text_input("Number Of Test Cases")
type = st.sidebar.selectbox("Format", ("Table", "Text"))

if functionality:
    response = langchain_helper.generate_Test_Cases(domain, functionality, number, type)
    st.write(response.strip())


