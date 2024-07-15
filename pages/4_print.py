import streamlit as st
if st.button('불러오기'):
    st.write(st.session_state.name)