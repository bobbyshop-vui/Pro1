import streamlit as st
st.title(':collision: ĐIỀN THÔNG TIN GIỚI THIỆU BẢN THÂN')
my_bar = st.progress(0)
quiz = ["Họ và tên:", "Ngày sinh:", "Nơi sinh","Sở thích:"]
answers = []
len_quiz = len(quiz)
for i in range(len_quiz):
  tl = st.text_input(quiz[i])
  if tl !="":
    answers.append(tl)

if st.button("Confirm"):
  if len(answers)==len_quiz:
    my_bar.progress(100)
    st.write("Bạn đã điền đầy đủ thông tin")
    st.balloons()
  else:
    my_bar.progress(len(answers)/len_quiz)
    st.write("Bạn chưa điền đủ thông tin")

for i in range (len(answers)):
  st.write(quiz[i],answers[i])
