import streamlit as st
import time

st.title('my progress')

bar = st.progress(0)
if st.button('Nhấn'):
    st.balloons()
for progress_completed in range(100):
    time.sleep(0.5)
    bar.progress(progress_completed + 1)