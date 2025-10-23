
import streamlit as st

# 1) 제목과 설명
st.title("나의 첫 스트림릿 어플리케이션")
st.subheader("Python으로 웹앱 만들기")
st.write("streamlit으로 간단한게 어플리케이션을 만들수 있습니다.")

# 2) 구분선
st.markdown("---")
st.divider()

# 3) 사용자 입력
name = st.text_input("이름을 입력해주세요")
#    챗봇 입력창
st.chat_input("질문을 입력해주세요")

# 4) 버튼 / 이벤트
if st.button("인사하기"): 
    st.success(f"안녕하세요 {name}님 streamlit에 오신것을 환영합니다")

# 5) 슬라이더(상태조절)
age = st.slider("나이를 선택해 주세요: ", 0, 100, 25)
st.info(f"선택한 나이 : {age}세 입니다")

# 6) 선택박스
hobby = st.selectbox("취미를 선택해주세요", ["독서", "운동", "영화감상", "코딩"])
st.write(f"취미 : {hobby}")
