import streamlit as st
text = st.text_input('이름을 입력하세요.')
if st.button('저장') :
    if 'name' not in st.session_state:
        st.session_state.name = text
    else :
        st.session_state.name = text