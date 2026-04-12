import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="Giant Food System 통합 포털", page_icon="🏢", layout="centered")

# 🌟 Giant Food System 공식 로고 추가
# 회사 도메인(giantfoodusa.com)을 인식하여 로고를 자동으로 불러옵니다.
col_img1, col_img2, col_img3 = st.columns([1.5, 1, 1.5])
with col_img2:
    # 만약 로고가 안 나오거나 다른 이미지로 바꾸고 싶다면 아래 링크 대신 "logo.png" 처럼 파일 이름을 넣으시면 됩니다.
    st.image("https://logo.clearbit.com/giantfoodusa.com", use_container_width=True)

# 메인 타이틀 (가운데 정렬)
st.markdown("<h1 style='text-align: center;'>Giant Food System 통합 포털</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666;'>원하시는 업무 시스템을 선택해 주세요.</h4>", unsafe_allow_html=True)
st.markdown("---")

# 2칸으로 나누어서 메뉴판 만들기
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚚 물류 및 차량 관리")
    st.info("트럭, 트레일러, 장비 현황 및 사고/티켓 내역을 관리하는 대시보드입니다.")
    
    # 트럭 대시보드 실제 인터넷 주소(URL)
    TRUCK_APP_URL = "https://my-truck-dashboard-rwtytrjvzqzzdcnzlhn2j3.streamlit.app" 
    
    st.link_button("👉 트럭 관리 대시보드 열기", TRUCK_APP_URL, use_container_width=True)

with col2:
    st.markdown("### 👨‍💼 인사 및 근태 관리 (예시)")
    st.success("드라이버 및 직원 정보, 급여 내역을 관리하는 대시보드입니다.")
    
    # 나중에 다른 앱을 만드시면 이곳에 주소를 넣으시면 됩니다.
    HR_APP_URL = "https://your-hr-app-name.streamlit.app" 
    
    st.link_button("👉 인사 관리 대시보드 열기", HR_APP_URL, use_container_width=True)

st.markdown("---")

# 추가 메뉴 (아래에 한 줄 더 만들기)
col3, col4 = st.columns(2)

with col3:
    st.markdown("### 💰 재무 및 영수증 (예시)")
    st.warning("주유비, 톨게이트 비용 등 각종 지출 내역을 관리합니다.")
    FINANCE_APP_URL = "https://your-finance-app-name.streamlit.app"
    st.link_button("👉 재무 관리 대시보드 열기", FINANCE_APP_URL, use_container_width=True)

with col4:
    st.markdown("### 📝 사내 공지사항 (예시)")
    st.error("회사 주요 일정 및 공지사항을 확인합니다.")
    NOTICE_APP_URL = "https://your-notice-app-name.streamlit.app"
    st.link_button("👉 공지사항 확인하기", NOTICE_APP_URL, use_container_width=True)

st.markdown("---")
st.caption("💡 팁: 나중에 새로운 관리 앱을 만들 때마다 이 포털에 버튼을 하나씩 추가하시면 됩니다!")
