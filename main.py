import streamlit as st
import time

# Thông tin đăng nhập
USERNAME = "admin"
PASSWORD = "123456"
st.title("🔑 Đăng nhập")
# Nhập tài khoản
username = st.text_input("👤 Tên đăng nhập")
password = st.text_input("🔒 Mật khẩu", type="password")
# Hiển thị thanh tiến trình
progress_bar = st.progress(0)
if st.button("Đăng nhập"):
    if username == USERNAME and password == PASSWORD:
        st.success("✅ Đăng nhập thành công!")
        st.balloons()  # Hiệu ứng bóng bay 🎈
        for percent in range(101):
            time.sleep(0.02)
            progress_bar.progress(percent)

        st.write("🎉 Chào mừng bạn!")
    else:
        st.error("❌ Sai tài khoản hoặc mật khẩu!")
