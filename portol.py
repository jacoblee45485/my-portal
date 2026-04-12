import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="사내 통합 관리 포털", page_icon="🏢", layout="centered")

# 메인 타이틀
st.title("🏢 우리 회사 통합 관리 포털")
st.markdown("#### 원하시는 업무 시스템을 선택해 주세요.")
st.markdown("---")

# 2칸으로 나누어서 메뉴판 만들기
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚚 물류 및 차량 관리")
    st.info("트럭, 트레일러, 장비 현황 및 사고/티켓 내역을 관리하는 대시보드입니다.")
    
    # 🚨 여기에 방금 배포하신 트럭 대시보드의 실제 인터넷 주소(URL)를 넣어주세요!
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