import streamlit as st
import folium
from streamlit_folium import st_folium
st.markdown("<img src= 'https://static.streamlit.io/examples/dog.jpg' width='50%' style='display: block; margin: 0 auto;'>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'> 김성수 & 강민승</h1>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: grey;'> 결혼합니다 </h3>",unsafe_allow_html=True)
st.markdown("""<hr style='border-left: 3px solid; height:150px; position: absolute; left: 50%; margin-left: -15px;'/>""",unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center; color: grey;margin-top:150px'> 2024.11.23 SAT 오후 1시 </h1>",unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: grey;'>장소 - 화담</h3>",unsafe_allow_html=True)

st.write('여기에 wide가 꽉 찬 사진')

st.markdown("<h3 style='text-align: center; color: grey;'> 저희 두 사람이 사랑의 이름으로</h3>",unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'> 미래를 함께 하고자 합니다. </h3>",unsafe_allow_html=True)
#st.markdown("<h3 style='text-align: center; color: grey;'> 축복해 주시면 감사하겠습니다. </h3>",unsafe_allow_html=True)
st.markdown("<hr/>",unsafe_allow_html = True)


# 연락처
#st.write("여기에 참석의사 전달")

st.markdown("<h3 style='text-align: center; color: black;'> 사 진 </h3>",unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center; color: black;'> 영 상 </h3>",unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center; color: black;'> 위치  </h3>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: grey;'> 일가 친척분들을 모시기 위해  </h5>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: grey;'> 한정식을 준비했습니다. </h5>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: grey;'> 두사람의 앞날을 축복해주시면 </h5>",unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: grey;'> 진심으로 감사하겠습니다. </h5>",unsafe_allow_html=True)

user_lat = '37.22559'
user_lon = '127.10944'
m = folium.Map(location=[user_lat, user_lon], zoom_start=18)
folium.Marker(
    [user_lat, user_lon], popup="화담", tooltip="위치"
).add_to(m)

st_data = st_folium(m)

st.write("여기에 계좌번호")

st.write("여기에 축하 메시지")
st.write("")

